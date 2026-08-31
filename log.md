# Log

Historia de construcción del vault. Formato: `## [YYYY-MM-DD] operacion | Título`.


---

# Brian Tracy

## [2026-08-30] setup | Vault creado, con un encuadre distinto

Quinto brain de `expert-brain`, y el primero que **no** alimenta contenido de marca. Chris lo pidió
explícitamente para uso propio; el veto del ADN sobre desarrollo personal sigue en pie para lo
que se publica.

## [2026-08-30] ingest | El Seminario Fénix, partido en 25 módulos

Un solo video de 11 horas, no un canal. Se descargó el `json3` completo (12 MB, con `tStartMs`
por evento) y se repartió por los 25 capítulos marcados en la metadata. 612.263 caracteres.

La decisión de partirlo por capítulos es lo que hace que esto funcione como brain: 25 archivos
citables por concepto, en vez de un muro de 600k caracteres. Cada uno enlaza al minuto exacto.

## [2026-08-30] ingest | Wiki destilado de los 25 módulos

24 páginas. El núcleo real del seminario es el bloque de metas (módulos 15-17), y de ahí salen
las páginas más aprovechables: los doce pasos, la roca, las siete preguntas y el área de
excelencia.

**Lo que quedó registrado en criterio**, y es la parte que más importa de este vault: el estudio
de Yale de 1953 sobre metas escritas —que Tracy cita como prueba central— no existe. Es un mito
documentado. También el 15% del potencial mental de Einstein. Están marcados en la página de
criterio y en las páginas donde aparecen, porque son citas que circulan como hechos.

El seminario tiene dos capas separables: una metafísica (ley de atracción, superconsciente) que
no se sostiene, y una operativa (metas, obstáculos, compensación, fracaso) que sí. El filtro está
escrito en `como-leer-el-seminario-fenix.md`.


---

# Víctor Heras

## [2026-08-30] setup | Vault creado

Estructura desde el kit `chrisenprod/second-brain-kit`, adaptada igual que `emilio-brain`:
`raw/transcripciones/` para las fuentes crudas.

## [2026-08-30] ingest | 19 videos de @Victorherasmedia

Los más recientes del canal (180 videos en total), saltando los nueve episodios del reto
"De 0 a 100.000" —formato concurso, poco contenido de método— y los vlogs. Todos salieron de
los subtítulos automáticos de YouTube en pista `es-orig`: el canal publica títulos en inglés y
español, pero el audio original es español.

Dos trampas verificadas en el camino:

- **El cliente por defecto de yt-dlp choca con el bot-check.** Da `HTTP 429` seguido de
  "Sign in to confirm you're not a bot", que en un sondeo por lotes se lee como "este video no
  tiene subtítulos". No es eso. La solución sin cookies es
  `--extractor-args "youtube:player_client=web_embedded"`. Probados y descartados: `ios`,
  `tv_simply`, `mweb`, `tv`.
- **`lang=es` en los extractor-args** devuelve el título original en español en vez del inglés
  localizado. Con este cliente `upload_date` viene vacío, por eso el frontmatter no lleva
  `publicado`.

Pipeline de los pasos 1–3 de la skill `yt-knowledge` (meta → track json3 → texto corrido). Sin
el documento de conocimiento: este vault es de experto, no de video suelto.

## [2026-08-30] ingest | Wiki destilado de las 19 fuentes

30 páginas por concepto en `wiki/`, con citas `[[...]]` a las transcripciones. Los cinco
clusters: algoritmo y diagnóstico de cuenta, contenido, marca personal, sistemas y negocio,
dinero.

195 enlaces, ninguno roto, ninguna página huérfana, ninguna transcripción sin citar.

La página que más cuelga del resto es `seguidor-ideal.md`: casi todas sus fuentes vuelven a esa
tesis. Las tres transcripciones más citadas son `curso-100k-en-90-dias`,
`por-que-fracasan-las-marcas-personales` y `como-funciona-el-algoritmo`.

## [2026-08-30] criterio | Se elimina la capa raw/criterio/

Estaba casi vacía en los dos brains. Lo que sí tenía contenido —las salvedades sobre cómo leer
a Víctor— pasa a `wiki/como-leer-a-victor-heras.md`, que además queda enlazado desde el wiki en
vez de colgar aparte. Wiki queda en 31 páginas.

## [2026-08-30] setup | Vault de Obsidian, en la raíz y aquí

`expert-brain/` se abre como vault y muestra los dos cerebros con el grafo coloreado por brain;
esta carpeta tiene su propio `.obsidian` y también se abre sola.

Dos renombres para que los `[[enlaces]]` no queden ambiguos, porque en el vault compartido se
resuelven por nombre de archivo y no por ruta:

- `wiki/leyes-del-dinero.md` → `wiki/siete-leyes-del-dinero.md`. Chocaba con la transcripción
  del mismo nombre; la página se estaba enlazando a sí misma en vez de a su fuente.
- El `no-hacer.md` del criterio chocaba con el de Emilio. Resuelto al mover su contenido al wiki.

`index.md`, `log.md` y `CLAUDE.md` siguen repetidos entre los dos brains, pero nadie los enlaza.


---

# Caleb Ralston

## [2026-08-30] setup | Vault creado

Cuarto brain de `expert-brain`, misma estructura que los otros tres.

## [2026-08-30] ingest | El canal entero de @CalebRalston

27 videos, **todos con subtítulos**, sin descartes: el canal es monotemático sobre marca personal
y no había nada fuera de tema. 2.019.104 caracteres, unas 33 horas.

Sin sorpresas en el pipeline esta vez: `web_embedded` y los pasos 1–3 de la skill `yt-knowledge`.

La particularidad del canal es la distribución del texto: seis cursos de entre 2 y 6,4 horas
suman el 67% del total. Para el wiki se leyeron completos los videos cortos y medianos —donde los
marcos aparecen comprimidos— y los cursos se navegaron por nombre de marco. Los conceptos se
repiten mucho entre fuentes, así que la cobertura no sufre.

## [2026-08-30] ingest | Wiki destilado de las 27 fuentes

27 páginas. El marco más original del canal es el worldbuilding en siete elementos, que no
aparece en los otros tres brains.

El hallazgo de conexión: **su definición de marca es idéntica a la de Hormozi** —branding es
emparejar, marca es la asociación resultante—, lo cual tiene sentido porque construyó su marca.
Queda enlazado en las dos direcciones.


---

# Emilio Puigrredon

## [2026-08-29] setup | Vault creado

Estructura desde el kit `chrisenprod/second-brain-kit`, adaptada: `raw/transcripciones/`
para las fuentes crudas.

## [2026-08-29] ingest | 10 videos de @EmilioPuigrredon

Los 10 más recientes del canal. Seis salieron de los subtítulos automáticos de YouTube;
los otros cuatro no tenían captions de ningún tipo y se transcribieron con whisper.cpp
medium sobre el audio. Sin editar, sin destilar.

## [2026-08-29] ingest | Se descartan tres vlogs

`dia-en-mi-vida-ceo-empresa-internacional`, `semana-viajando-el-mundo-ceo-27` y
`equipo-viajo-una-semana-a-chile`: sin captions y con audio dominado por música.
Quedan 7 fuentes.

## [2026-08-29] ingest | Wiki destilado de las 7 fuentes

16 páginas por concepto en `wiki/`, con citas `[[...]]` a las transcripciones. 111 enlaces,
ninguno roto, ninguna página huérfana. Las cuatro fuentes más citadas son los videos de
estrategia; los dos vlogs aportan poco y se citan dos veces cada uno.

## [2026-08-29] ingest | 10 videos más del canal

Videos 11 a 25 del canal, filtrando los que tenían pista `es-orig` disponible y salteando
los vlogs. Los 20 revisados la tenían; se bajaron 10. Solo transcripción cruda — el wiki
todavía no las cubre.

## [2026-08-29] ingest | Wiki extendido a las 17 fuentes

9 páginas nuevas (ecosistemas, ranking-de-embudos, ascension, webinars, dm-ads, atribucion,
roas, preparar-stories, ia-en-el-negocio) y 13 páginas existentes extendidas. 25 páginas,
205 enlaces, ninguno roto. Las 17 transcripciones quedan citadas al menos dos veces.


---

# Alex Hormozi

## [2026-08-30] setup | Vault creado

Estructura desde el kit `chrisenprod/second-brain-kit`, igual que `victor-heras-brain` y
`emilio-puigrredon`, ya sin la capa `raw/criterio/`.

## [2026-08-30] ingest | 21 videos de @AlexHormozi

Del canal (más de 500 videos), elegidos por densidad de método y cubriendo sus seis dominios:
oferta y venta, marketing, negocio y retención, contenido y marca, dinero, e IA.

Una diferencia con los otros dos brains: **aquí la ausencia de subtítulos sí es real**. Ocho de
los candidatos originales no tenían pista de ningún tipo, y solo los uploads recientes del canal
las traen. La forma de distinguirlo del bot-check es mirar si llega el título en la metadata: si
llega y `automatic_captions` viene vacío, no hay pista. `mweb` además lo dice con todas las
letras. Se sustituyeron por siete videos recientes que sí las tenían.

El resto del pipeline igual que en los otros: `web_embedded` para saltar el 429, pasos 1–3 de la
skill `yt-knowledge`.

Las transcripciones quedan en inglés. Traducirlas sería reescribir la fuente, que es justo lo que
la capa `raw/` no hace.

## [2026-08-30] ingest | Wiki destilado de las 21 fuentes

29 páginas en español, con las citas textuales en inglés. La fuente más citada es
`crecer-una-audiencia` (160 min), seguida de `vender-como-el-1-por-ciento`.

Un renombre para evitar ambigüedad en el vault compartido, donde los `[[enlaces]]` se resuelven
por nombre de archivo: la página de wiki sobre las cinco ventajas se llama `las-cinco-ventajas.md`
y no `el-negocio-perfecto.md`, que es la transcripción. Lo mismo con `los-cuatro-caminos.md` y
`el-camino-a-los-primeros-100k.md`.


---

# El centro

## [2026-08-30] setup | Centro creado

Sexta carpeta de `expert-brain`, y la única sin `raw/` propio.

La idea original era meter aquí todos los raw y un wiki consolidado de los cinco. Se cambiaron
las dos mitades por una razón concreta en cada caso:

- **Los raw no se duplican.** 313 enlaces del wiki apuntan a un raw; copiarlos dejaría todos esos
  enlaces resolviendo a dos archivos con el mismo nombre. En su lugar,
  `wiki/catalogo-de-fuentes.md` los indexa todos y desde el vault compartido resuelven igual.
- **El wiki no consolida, cruza.** Un resumen de los cinco sería la cuarta copia de la misma
  información —después de los 109 raw, las 137 páginas y los índices— y se desincronizaría al
  primer cambio.

## [2026-08-30] ingest | Ocho páginas de cruce

Tres de desacuerdo, dos de consenso, una de linaje, el catálogo y el filtro.

Lo que apareció al cruzar y no estaba en ningún brain:

- **El gran desacuerdo no es sobre el valor.** Heras, Ralston y Hormozi usan la palabra para cosas
  distintas. Lo que de verdad los separa es **dónde ponen el filtro**, y la variable que lo
  explica es el ticket y el plazo.
- **Que Hormozi y Ralston coincidan no es confirmación independiente** — Ralston construyó la
  marca de Hormozi y su definición de marca es idéntica. Que Heras coincida, viniendo de otro
  mercado, sí lo es. Queda escrito en `linaje.md`.
- **Tracy es el antepasado con la capa metafísica puesta.** Hormozi es el mismo material con
  Kahneman en vez de la ley de la atracción.

Lo que queda por escribir, y solo lo puede escribir quien use esto: el filtro propio. Qué de estos
cinco entra en tu caso tal cual, qué entra traducido y qué no entra. El centro se queda en el
cruce; la decisión es de cada uno.

---

## [2026-08-30] centro | Tres consensos que estaban sin escribir

Análisis del grafo de wikilinks para buscar cabos sueltos. Cabos sueltos, ninguno: las únicas
notas con grado ≤2 eran los meta-archivos de la raíz. Lo que sí apareció fueron **grupos de
páginas que dicen lo mismo en varios brains sin enlazarse entre sí**.

Tres tenían masa para una página del centro:

- **`volumen-y-ejecucion`** — 5 de 5 brains, 18 pares sin enlace. El único consenso completo del
  vault. Y al escribirlo apareció la grieta: los cuatro modernos acumulan información sobre el
  mercado, Tracy acumula creencia en uno mismo. Misma conducta, dos teorías incompatibles.
- **`anatomia-del-embudo`** — 4 brains, 11 pares sin enlace. No se contradicen: cubren tramos
  distintos y dan por supuesto el resto. Cuatro de cinco terminan en la primera venta.
- **`la-ia-segun-los-cinco`** — 4 brains, y los 4 pares posibles sin enlace pese a hablar del
  mismo tema. Son cuatro capas, no cuatro opiniones.

Además se tendieron los enlaces de vuelta en 14 páginas fuente, que es lo que cierra el ciclo:
`brian-tracy ↔ emilio-puigrredon` estaba en 0 en ambas direcciones y `alex-hormozi → caleb-ralston`
en 0. Queda una celda en cero, `caleb-ralston → brian-tracy`; el puente sería
`estudiante-o-experto ↔ autoconcepto`, y eso es otra página del centro, no un enlace suelto.

Estado: 280 notas · 1490 enlaces · 0 rotos · 0 duplicados.

## [2026-08-30] fix | raw se parte en dos capas

`.gitignore` excluía `*/raw/`, que era correcto cuando ahí vivían las transcripciones completas.
Desde que son fichas de título + enlace, esa regla borraba 109 notas del clon y dejaba **425
enlaces rotos en 138 páginas**: el grafo se partía en cuanto alguien clonaba el repo.

Ahora `raw/transcripciones/` (las fichas) va versionado y `raw/texto/` (el texto corrido, que sí es
obra de sus autores) está ignorado. `scripts/ingest.py` escribe en `raw/texto/` y ya no pisa las
fichas.

## [2026-08-30] centro | Mentalidad, y el desacuerdo que estaba escondido

Sexta y última página del cruce, la que cierra `caleb-ralston ↔ brian-tracy`, que era la única
celda en cero que quedaba en la matriz.

Cuatro de los cinco usan el mismo mecanismo —lo que crees decide lo que haces— pero lo apuntan a
tres blancos distintos: tu creencia (Tracy, Heras), la del cliente (Emilio) y la que declaras en
público (Ralston, Hormozi). Puesto así aparece un desacuerdo que no estaba escrito en ningún
sitio: **Tracy dice que subas la creencia por encima de la evidencia; Ralston y Hormozi dicen que
la bajes hasta que coincida con los hechos.** Para Tracy el síndrome del impostor es un
autoconcepto que reprogramar; para Hormozi es información correcta.

El otro hallazgo es que `probabilidad-de-exito` de Emilio, que estaba archivado como página de
precio, es la ley de la expectativa de Tracy aplicada al comprador — y la única versión del vault
donde la creencia se fabrica con data en vez de con afirmaciones.

## [2026-08-30] fichas | Extensión esperada en cada hueco de mi-marca

Faltaba la señal de cuánto escribir: quien clona el repo se encuentra 50 huecos en blanco sin
saber si se espera una frase o media página. Cada hueco lleva ahora la extensión típica —
`*(~300 caracteres)*` para prosa, `*(10 líneas, ~80 caracteres cada una)*` para listas — y
`mi-marca.md` explica que es una referencia, no un límite: la mitad suele significar que falta
concretar, el triple que la decisión no está tomada.

De paso, `banner.png` (1,3 MB) pasa a `banner.webp` (126 KB, `cwebp -q 88`), y se corrige "doce
fichas" por "once" en el README — son 00 a 10.
