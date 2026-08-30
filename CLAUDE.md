# Cómo trabajar sobre expert-brain

Dos capas y una regla que las separa:

- `<experto>/raw/transcripciones/` — una ficha por fuente: título, autor y enlace al vídeo. Es
  lo que el wiki cita, y va en el repo: son metadatos públicos.
- `<experto>/raw/texto/` — el texto corrido de cada fuente. **No se publica** (es obra de sus
  autores); `scripts/ingest.py` lo genera en local y está en `.gitignore`.
- `<experto>/wiki/` — el destilado. **Cada afirmación cita su fuente.** Si una página no se puede
  rastrear hasta un raw, sobra.

`<experto>/<experto>.md` es el índice de cada brain y el núcleo de su cúmulo en el grafo.
`expert-brain.md` es a la vez la entrada y el centro.

## El centro

`super-expert-brain/wiki/` solo lleva lo que ningún brain puede contener por separado:
contradicciones, consensos y linaje.

**Regla: si una página se puede escribir leyendo un solo brain, no va en el centro.**

Cada página del centro depende de los cinco. Al añadir un experto hay que revisarlas todas — por
eso son pocas y densas a propósito.

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
3. Cita la fuente con un wikilink al stub, y enlaza a las páginas relacionadas, incluidas las de otros expertos.
4. Verifica: cero enlaces rotos, cero páginas huérfanas, cero fuentes sin citar.
5. Actualiza `como-leer-a-…` si aparece un sesgo o un dato que no se sostiene. Es el paso que más
   valor añade y el que nadie hace.
