#!/usr/bin/env python3
"""
Regenera en local el texto de las fuentes de expert-brain.

    pip install yt-dlp   (o brew install yt-dlp)
    python3 scripts/ingest.py            # todo
    python3 scripts/ingest.py victor     # solo los brains que coincidan

Lee las fichas de experts/*/raw/transcripciones/ —que sí van en el repo— y deja un .txt por
fuente en experts/<experto>/raw/texto/. Ese texto no se publica: es obra de sus autores.

No hay lista de canales dentro: las URLs salen de las fichas. Así funciona igual para cualquier
experto que se añada después, sin tocar este archivo.

Trampa verificada: el cliente por defecto de yt-dlp choca con el bot-check de YouTube y devuelve
un 429 que parece "este vídeo no tiene subtítulos". Por eso player_client=web_embedded.
"""
import glob, json, os, re, subprocess, sys, textwrap, time
from collections import defaultdict

XARGS = "youtube:player_client=web_embedded"
TMP = ".ingest-cache"


def yt(args):
    return subprocess.run(["yt-dlp", *args], capture_output=True, text=True).stdout


def ficha(path):
    """Frontmatter de una ficha. Devuelve None si no tiene url."""
    head = open(path, encoding="utf-8").read().split("---")[1] if "---" in open(
        path, encoding="utf-8").read() else ""
    campos = dict(re.findall(r"^([a-z_]+):\s*(.*)$", head, re.M))
    if not campos.get("url"):
        return None
    campos["path"] = path
    campos["slug"] = os.path.basename(path)[:-3]
    campos["experto"] = path.split(os.sep)[1]
    campos["vid"] = re.search(r"[?&]v=([\w-]+)", campos["url"]).group(1)
    return campos


def meta(url, lang):
    x = XARGS + (f";lang={lang}" if lang else "")
    out = yt(["-J", "--skip-download", "--extractor-args", x,
              "--ignore-no-formats-error", url])
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


def eventos(vid, tr, url):
    """[(segundo, texto)] del json3, cacheado en disco."""
    if not glob.glob(f"{TMP}/{vid}.*.json3"):
        yt(["--skip-download", "--write-sub", "--write-auto-sub", "--sub-langs", tr,
            "--sub-format", "json3", "--extractor-args", XARGS,
            "--ignore-no-formats-error", "-o", f"{TMP}/{vid}.%(ext)s", url])
        time.sleep(2)
    f = glob.glob(f"{TMP}/{vid}.*.json3")
    if not f:
        return None
    ev = []
    for e in json.load(open(f[0], encoding="utf-8")).get("events", []):
        t = "".join(s.get("utf8", "") for s in e.get("segs", [])).strip()
        if t:
            ev.append((e.get("tStartMs", 0) / 1000.0, t))
    return sorted(ev)


def escribe(f, cuerpo):
    dest = f"experts/{f['experto']}/raw/texto"
    os.makedirs(dest, exist_ok=True)
    cab = f"# {f['titulo']}\n\n{f['autor']} · {f.get('duracion','')} · {f['url']}\n\n"
    body = "\n".join(textwrap.wrap(re.sub(r"\s+", " ", cuerpo).strip(), 100,
                                   break_long_words=False, break_on_hyphens=False))
    open(f"{dest}/{f['slug']}.txt", "w", encoding="utf-8").write(cab + body + "\n")


def main():
    filtro = sys.argv[1] if len(sys.argv) > 1 else ""
    os.makedirs(TMP, exist_ok=True)

    fichas = [x for x in map(ficha, sorted(glob.glob("experts/*/raw/transcripciones/*.md"))) if x]
    if filtro:
        fichas = [f for f in fichas if filtro in f["experto"]]
    if not fichas:
        sys.exit("no hay fichas que coincidan. ¿Estás en la raíz del repo?")

    porvideo = defaultdict(list)
    for f in fichas:
        porvideo[f["vid"]].append(f)

    print(f"{len(fichas)} fuentes en {len(porvideo)} vídeos\n")
    hechas = fallos = 0

    for vid, grupo in porvideo.items():
        pendientes = [f for f in grupo
                      if not os.path.exists(f"experts/{f['experto']}/raw/texto/{f['slug']}.txt")]
        if not pendientes:
            continue
        url, lang = grupo[0]["url"], grupo[0].get("idioma") or None
        m = meta(url, lang)
        if not m:
            print(f"  ! {vid} — sin metadata (¿bot-check? reintenta más tarde)")
            fallos += len(pendientes)
            continue
        tr = track(m)
        if not tr:
            # Con título en la metadata y automatic_captions vacío, la ausencia es real.
            print(f"  – {m.get('title','?')[:60]} — no tiene subtítulos")
            fallos += len(pendientes)
            continue
        ev = eventos(vid, tr, url)
        if not ev:
            print(f"  ! {vid} — no se pudo bajar la pista {tr}")
            fallos += len(pendientes)
            continue

        # Un vídeo partido en módulos: cada ficha es un capítulo (Tracy y sus 11 h).
        caps = [c for c in (m.get("chapters") or []) if not c["title"].startswith("<Untitled")]
        parte = len(grupo) > 1 and len(caps) >= len(grupo)

        for f in pendientes:
            if parte:
                i = int(f["modulo"].split()[0]) - 1
                a = caps[i]["start_time"]
                z = caps[i + 1]["start_time"] if i + 1 < len(caps) else m["duration"]
                cuerpo = " ".join(t for ts, t in ev if a <= ts < z)
            else:
                cuerpo = " ".join(t for _, t in ev)
            escribe(f, cuerpo)
            print(f"  ✓ {f['experto']}/{f['slug']}")
            hechas += 1

    print(f"\n{hechas} escritas, {fallos} sin texto.")
    if fallos:
        print("Un 429 del bot-check se parece a 'no hay subtítulos': vuelve a correrlo, "
              "que lo ya hecho no se repite.")


if __name__ == "__main__":
    main()
