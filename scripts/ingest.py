#!/usr/bin/env python3
"""
Regenera las transcripciones de expert-brain en local.

    pip install yt-dlp   (o brew install yt-dlp)
    python3 scripts/ingest.py

Deja un .txt por fuente en experts/<experto>/raw/texto/, que es el texto corrido de la fuente.
No se publica en el repo: es obra de sus autores. Las fichas que el wiki cita, en
<experto>/raw/transcripciones/, sí están versionadas y este script no las toca.

Trampa verificada: el cliente por defecto de yt-dlp choca con el bot-check de YouTube y
devuelve un 429 que parece "este vídeo no tiene subtítulos". Por eso player_client=web_embedded.
"""
import json, subprocess, glob, os, re, sys, time, textwrap

XARGS = "youtube:player_client=web_embedded"
CANALES = {
    "experts/alex-hormozi":       ("https://www.youtube.com/@AlexHormozi/videos",      "en"),
    "experts/caleb-ralston":      ("https://www.youtube.com/@CalebRalston/videos",     "en"),
    "experts/victor-heras":       ("https://www.youtube.com/@Victorherasmedia/videos", "es"),
    "experts/emilio-puigrredon":  ("https://www.youtube.com/@EmilioPuigrredon/videos", "es"),
}
# Brian Tracy es un solo vídeo de 11 h partido por sus 25 capítulos
SEMINARIO = ("experts/brian-tracy", "https://www.youtube.com/watch?v=zUxj7J8HttM", "es")


def yt(args):
    r = subprocess.run(["yt-dlp", *args], capture_output=True, text=True)
    return r.stdout


def meta(url, lang=None):
    x = XARGS + (f";lang={lang}" if lang else "")
    out = yt(["-J", "--skip-download", "--extractor-args", x, "--ignore-no-formats-error", url])
    return json.loads(out) if out.strip() else None


def track(m):
    subs, auto = m.get("subtitles") or {}, m.get("automatic_captions") or {}
    for c in ("es", "es-orig", "en", "en-US"):
        if c in subs:
            return c
    for c in ("es-orig", "en-orig", "es", "en"):
        if c in auto:
            return c
    return None


def texto(vid, tr, url, tmp):
    if not glob.glob(f"{tmp}/{vid}.*.json3"):
        yt(["--skip-download", "--write-sub", "--write-auto-sub", "--sub-langs", tr,
            "--sub-format", "json3", "--extractor-args", XARGS,
            "--ignore-no-formats-error", "-o", f"{tmp}/{vid}.%(ext)s", url])
        time.sleep(2)
    f = glob.glob(f"{tmp}/{vid}.*.json3")
    if not f:
        return None
    d = json.load(open(f[0], encoding="utf-8"))
    ev = []
    for e in d.get("events", []):
        if "segs" not in e:
            continue
        t = "".join(s.get("utf8", "") for s in e["segs"]).strip()
        if t:
            ev.append((e.get("tStartMs", 0) / 1000.0, t))
    return sorted(ev)


def escribe(dest, slug, campos, cuerpo):
    os.makedirs(dest, exist_ok=True)
    fm = "---\n" + "".join(f"{k}: {v}\n" for k, v in campos.items()) + "---\n\n"
    body = "\n".join(textwrap.wrap(re.sub(r"\s+", " ", cuerpo).strip(), 100,
                                   break_long_words=False, break_on_hyphens=False))
    open(f"{dest}/{slug}.txt", "w", encoding="utf-8").write(fm + f"# {campos['titulo']}\n\n" + body + "\n")


def main():
    tmp = ".ingest-cache"
    os.makedirs(tmp, exist_ok=True)
    print("Las fuentes concretas de cada brain están en su <experto>.md.")
    print("Este script trae el seminario de Tracy, que es el único partido por capítulos.\n")

    b, url, lang = SEMINARIO
    m = meta(url, lang)
    if not m:
        sys.exit("no se pudo leer la metadata")
    tr = track(m)
    ev = texto(m["id"], tr, url, tmp)
    caps = [c for c in (m.get("chapters") or []) if not c["title"].startswith("<Untitled")]
    dest = f"{b}/raw/texto"
    for i, c in enumerate(caps):
        a = c["start_time"]
        z = caps[i + 1]["start_time"] if i + 1 < len(caps) else 1e9
        slug = f"{i+1:02d}-" + "-".join(re.sub(r"[^a-z0-9]+", "-",
                 c["title"].lower().encode("ascii", "ignore").decode()).strip("-").split("-")[:7])
        escribe(dest, slug, {
            "video": slug, "modulo": f"{i+1} de {len(caps)}", "titulo": c["title"],
            "seminario": "Seminario Fenix", "autor": "Brian Tracy",
            "url": f"{url}&t={int(a)}s", "duracion_s": int(min(z, m['duration']) - a),
            "idioma": "es", "modelo": f"subtitulos automaticos de YouTube ({tr})",
        }, " ".join(t for ts, t in ev if a <= ts < z))
        print(f"  {slug}")
    print(f"\n{len(caps)} módulos en {dest}/")
    print("\nPara los otros cuatro brains, los IDs de cada fuente están en su <experto>.md;")
    print("misma receta: meta -> track -> json3 -> texto corrido.")


if __name__ == "__main__":
    main()
