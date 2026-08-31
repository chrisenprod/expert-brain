# Cómo trabajar sobre expert-brain

La raíz se parte en dos por lo que puedes hacer con cada cosa:

- **`experts/`** — se lee, no se reescribe. Es la obra de otros, destilada.
- **`work/`** — se escribe. Es del usuario, y el repo funciona sin ello.

## `experts/` — las tres capas

- `experts/<experto>/raw/transcripciones/` — una ficha por fuente: título, autor y enlace al
  vídeo. Es lo que el wiki cita, y va en el repo: son metadatos públicos.
- `experts/<experto>/raw/texto/` — el texto corrido. **No se publica** (es obra de sus autores);
  `scripts/ingest.py` lo genera en local y está en `.gitignore`.
- `experts/<experto>/wiki/` — el destilado. **Cada afirmación cita su fuente.** Si una página no
  se puede rastrear hasta un raw, sobra.

`experts/<experto>/<experto>.md` es el índice de cada brain y el núcleo de su cúmulo en el grafo.
`expert-brain.md`, en la raíz, es a la vez la entrada y el centro.

## El centro

`experts/super-expert-brain/wiki/` solo lleva lo que ningún brain puede contener por separado:
contradicciones, consensos y linaje.

**Regla: si una página se puede escribir leyendo un solo brain, no va en el centro.**

Cada página del centro depende de los cinco. Al añadir un experto hay que revisarlas todas — por
eso son pocas y densas a propósito.

## `work/` — lo del usuario

- `work/mi-marca/` — once fichas de decisión (`00`–`10`), más `diagnostico.md`, que es una
  medición con fecha y no una decisión, e `historial.md`.
- `work/contenido/` — la producción. **Cada pieza enlaza a la ficha que la justifica**, o son
  nodos huérfanos y el grafo deja de servir.

Al tocar una ficha, añade la entrada en `work/mi-marca/historial.md`: qué cambió y **por qué**.
El porqué es lo único que no se puede reconstruir después.

## Las skills

Cinco en `.claude/skills/`, por dominio: `marca`, `contenido`, `ventas`, `mentalidad` y
`preguntar`. Dos reglas que llevan todas y que son el motivo de que existan:

1. **Los cinco expertos, siempre.** Si una respuesta sale de uno solo, no se ha usado el repo.
2. **Cuando discrepan, el desacuerdo va antes que la respuesta.** Un consenso falso es peor que
   no responder. La variable que resuelve casi todos sus desacuerdos es el ticket y el plazo —
   `experts/super-expert-brain/wiki/precio-y-ticket-comparado.md`.

Y ninguna decide por el usuario: una respuesta por turno, y nunca una que no haya dicho o
aprobado.

## Ingesta

El cliente por defecto de yt-dlp choca con el bot-check de YouTube y devuelve un 429 que **parece**
"este vídeo no tiene subtítulos". Usa siempre:

```
yt-dlp --extractor-args "youtube:player_client=web_embedded" ...
```

Para distinguir un bloqueo de una ausencia real: si llega el título en la metadata y
`automatic_captions` viene vacío, no hay pista. `mweb` además lo dice con todas las letras.

Casos particulares ya resueltos:

- **Tracy** es un solo vídeo de 11 h partido por sus 25 capítulos, usando `tStartMs` del `json3`
  contra los `chapters` de la metadata.
- **Heras** publica títulos en inglés y español; `lang=es` trae el original, a costa de perder
  `upload_date`.
- **Hormozi** solo tiene subtítulos en los uploads recientes. Ahí la ausencia es real.

## Al escribir una página nueva

1. Lee las fuentes enteras, no las busques por palabra clave.
2. Una página por **concepto**, no por vídeo, cruzando fuentes.
3. Cita la fuente con un wikilink al stub, y enlaza a las páginas relacionadas, incluidas las de
   otros expertos.
4. Verifica: cero enlaces rotos, cero páginas huérfanas, cero fuentes sin citar.
5. Actualiza `como-leer-a-…` si aparece un sesgo o un dato que no se sostiene. Es el paso que más
   valor añade y el que nadie hace.

## Sobre mover archivos

Los `[[wikilinks]]` resuelven por **nombre de archivo**, no por ruta: mover una carpeta no los
rompe. Lo que sí rompe son las rutas escritas — este archivo, el README, las cinco skills,
`scripts/ingest.py`, el patrón de `.gitignore` y los `colorGroups` de `.obsidian/graph.json`.
