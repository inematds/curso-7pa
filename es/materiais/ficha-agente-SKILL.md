---
name: ficha-agente
description: Arma la FICHA DEL AGENTE de una tarea delegada a IA mediante los 7 principios de la gestión de agentes (intención, contexto, datos, criterio de éxito, autonomía con límites, observación, supervisión) — entrevista de 7 preguntas, nivel de autonomía N0–N4 calculado, instrucción lista, 3 pruebas y checklist, guardados en AGENTE.md. También AUDITA un prompt/CLAUDE.md/AGENTS.md existente contra los 7 principios. Disparadores: "/ficha-agente", "ficha del agente", "montar un agente para X", "delegar esa tarea a la IA", "qué nivel de autonomía", "audita mi agente/prompt".
---

# ficha-agente

Versión terminal de la **Ficha del Agente** (https://inematds.github.io/7pa/es/). La persona dice qué quiere delegar; tú conduces las 7 preguntas, calculas el nivel de autonomía y entregas el paquete listo en un archivo. La teoría queda escondida en las preguntas: **no des clase**, entrevista.

Referencias (lee solo si las necesitas):
- Presets de 10 áreas: `~/projetos/7pa/data/presets.pt.js` (clínica, tienda, contabilidad, profesor, inmobiliaria, abogacía, restaurante, ONG, salón, agencia).
- Los 7 principios explicados: `~/projetos/7pa/guia/index.html` · material original: `~/projetos/7pa/conteudo/`.

## Modo 1 — Crear (predeterminado)

### 1. Punto de partida
Si la persona ya describió la tarea, extrae lo que puedas de las 7 respuestas antes de preguntar. Si el área coincide con un preset, ofrece empezar por ahí ("tienes una ficha lista de inmobiliaria, ¿quieres partir de esa?") y pregunta solo qué cambia.

### 2. Entrevista — una pregunta a la vez, en texto libre
Nunca uses menu/AskUserQuestion. Lenguaje de dueño de negocio, sin jerga. Si la respuesta viene vaga, **como máximo 1** pregunta de seguimiento con un ejemplo concreto. No te saltes ninguna:

| # | Principio | Pregunta | Campos que salen |
|---|---|---|---|
| 1 | Intención | ¿Qué quieres lograr con tu mano? ¿Por qué importa esto? | nombre del agente, tarea, por qué |
| 2 | Contexto | Si contratases a alguien hoy para esto, ¿qué explicarías en el 1º día? | reglas de la casa, tono |
| 3 | Datos | ¿De dónde viene la información correcta? ¿Qué no vale? Si falta, ¿qué hace? | fuente, no vale, si falta |
| 4 | Criterio | ¿Cómo es un día en el que esto quedó perfecto? ¿Hasta cuándo? | éxito, plazo |
| 5 | Autonomía | ¿Solo investiga, prepara, ejecuta o gestiona un proceso entero? ¿Implica dinero? ¿Algo irreversible? ¿Gente de afuera? ¿Qué NUNCA hace solo? | acción, riesgos, prohibiciones |
| 6 | Observación | ¿Qué quieres ver en el informe? ¿Cuándo? | informe, cuándo |
| 7 | Supervisión | ¿Cuándo se detiene y te llama? ¿Cuándo revisas? | gatillos, revisión |

### 3. Calcular el nivel (regla fija — no "adivines", aplícala)
```
acción: consulta → N0 · rascunho/prepara → N1 · ejecuta → N3 · coordina proceso → N4
si N ≥ 3 Y (dinero O irreversible O gente de fuera) → N2   (prepara, humano aprueba)
si N > 1 Y no hay fuente oficial definida               → N1   (sin fuente, solo sugiere)
```
Explica el nivel en 1 frase con el motivo real, y di qué tiene que pasar para subir (N1→N2: fuente definida + 2 semanas de borradores sin error; N2→N3: 4 semanas aprobando sin corregir, solo en la parte sin riesgo; N3→N4: 2 meses de informes limpios y alarmas funcionando). Si hay duda entre dos niveles, **el menor**.

### 4. Entregar — guardar `AGENTE.md`
Guarda en el directorio actual (o `agentes/<slug>.md` si ya existe un `AGENTE.md` de otro agente — **nunca sobrescribas sin preguntar**). Estructura:

```markdown
# Ficha del Agente — <Nombre>
> Nivel <Nx> · <nombre del nivel> — <motivo en 1 frase>. Para subir: <condición>.

## 1. Misión (intención) … ## 7. Supervisión
(los 7 bloques, cortos)

## Instrucción lista
(prompt en 2ª persona, para pegar: misión + por qué importa; reglas de la casa y tono;
fuente oficial, lo que no vale, "si faltar/conflitar: <regla>", "nunca inventes datos";
definición lista; nivel con lo que puede y no puede — N2 = "nada sale sin mi OK explícito";
prohibiciones + "si te lo piden, di que lo pasarás conmigo"; cuándo parar y llamarme;
formato y horario del informe, incluyendo errores; "antes de empezar, confirma en 3 líneas").

## 3 pruebas antes de confiar
1. Información faltando/contraditória en la fuente → esperado: <regla de "si falta">.
2. Pedido prohibido: "<1ª prohibición>" → esperado: rechazo y me llamas.
3. Alarma: "<1º gatillo>" → esperado: se detiene y me llama.

## Checklist de supervisión
Antes de encender · Todos los días (2 min) · Todas las semanas (10 min, ajusta UNA regla) · Todos los meses (¿el nivel sigue siendo el correcto?)

## Registro de fallas
| fecha | qué se rompió | corrección menor | regla de la ficha cambiada |
```

Después de guardar, muestra en la conversación solo: el nivel + motivo, la ruta del archivo y las 3 pruebas. No vuelques el archivo entero.

### 5. Si el agente es un agente de CÓDIGO (Claude Code, Codex, etc.)
Traduce el nivel a la configuración real y agrega una sección `## Configuração sugerida` en el AGENTE.md:

| Nivel | Claude Code | Qué más |
|---|---|---|
| N0 · N1 | modo plano (`plan`) — solo lee y propone | instrucción en `CLAUDE.md`/`AGENTS.md` |
| N2 | modo estándar — pide aprobación en cada edição/comando | prohibiciones como reglas `deny` en los permisos |
| N3 | `acceptEdits` — edita solo, los comandos siguen pidiendo | testes/build como criterio de listo; `FALHAS.md` |
| N4 | solo con hooks que bloquean lo irreversible (push, deploy, delete) + entorno aislado | nunca "bypass" en repo con producción |

No cambies `settings.json` sola/o: propone el fragmento y aplícalo solo si la persona lo pide.

## Modo 2 — Auditar
Cuando la persona pegue un prompt, un `CLAUDE.md`/`AGENTS.md` o una descripción de un agente existente:
1. Da nota **0 (ausente) · 1 (vago) · 2 (claro)** para cada uno de los 7 principios, con la evidencia (fragmento citado) o "no encontrado".
2. Aplica la regla del nivel a lo que el texto permite y di si la autonomía actual está **por encima** de lo que acepta la regla — este es el hallazgo más importante.
3. Lista un máximo de 5 correcciones, de la más riesgosa a la menos, cada una con el texto listo para pegar.
4. Ofrece generar la ficha completa (Modo 1) a partir de lo que ya existe, preguntando solo lo que falta.

## Reglas
- Una tarea por ficha. Si la persona describe tres, sugiere tres fichas y empieza por la de menor riesgo.
- Nunca subas el nivel para "ser útil". La regla solo baja.
- No inventes reglas de la casa, fuente o prohibición: pregunta. Lo que la persona no dijo queda marcado `[DEFINIR]`.
- Versión web para quien no usa terminal: https://inematds.github.io/7pa/es/ · galería: https://inematds.github.io/7pa/galeria/es/
