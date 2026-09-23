---
name: ficha-agente
description: Builds the AGENT SHEET for a task delegated to an AI using the 7 agent management principles (intention, context, data, success criteria, autonomy with limits, observation, supervision) — 7-question interview, calculated autonomy level N0–N4, ready instruction, 3 tests and checklist, recorded in AGENTE.md. Also AUDITS an existing prompt/CLAUDE.md/AGENTS.md against the 7 principles. Triggers: "/ficha-agente", "ficha do agente", "montar um agente pra X", "delegar essa tarefa pra IA", "que nível de autonomia", "audita meu agente/prompt".
---

# ficha-agente

Terminal version of the **Agent Sheet** (https://inematds.github.io/7pa/en/). The person states what they want to delegate; you run the 7 questions, calculate the autonomy level, and deliver the ready package in a file. The theory stays hidden in the questions: **don’t teach**, interview it.

References (read only if needed):
- Presets of 10 areas: `~/projetos/7pa/data/presets.pt.js` (clinic, store, accounting, teacher, real estate, law practice, restaurant, NGO, hair salon, agency).
- The 7 explained principles: `~/projetos/7pa/guia/index.html` · original material: `~/projetos/7pa/conteudo/`.

## Mode 1 — Create (default)

### 1. Starting point
If the person has already described the task, extract whatever you can from the 7 answers before asking. If the area matches a preset, offer starting from it ("there’s already a real estate sheet—do you want to start from it?") and ask only what changes.

### 2. Interview — one question at a time, in free text
Never use menu/AskUserQuestion. Business-owner language, without jargon. If the answer comes back vague, **at most 1** follow-up question with a concrete example. Don’t skip any:

| # | Principle | Question | Fields that come out |
|---|---|---|---|
| 1 | Intention | What do you want to get out of your agent? Why does it matter? | agent name, task, why |
| 2 | Context | If you hired someone for this today, what would you explain on the 1st day? | house rules, tone |
| 3 | Data | Where does the correct information come from? What doesn’t count? If it’s missing, what does it do? | source, doesn’t count, if missing |
| 4 | Success criteria | What does a day where this was perfect look like? Until when? | success, deadline |
| 5 | Autonomy | Does it only research, prepare, execute, or does it run an entire process? Does it involve money? Anything irreversible? People from the outside? What does it NEVER do alone? | action, risks, prohibitions |
| 6 | Observation | What do you want to see in the report? When? | report, when |
| 7 | Human supervision | When does it stop and call you? When do you review? | triggers, review |

### 3. Calculate the level (fixed rule — don’t "guess", apply it)
```
action: consult → N0 · rascunho/prepara → N1 · executes → N3 · coordinates process → N4
if N ≥ 3 AND (money OR irreversible OR people from the outside) → N2   (prepares, human approves)
if N > 1 AND no official source is defined               → N1   (no source, only suggests)
```
Explain the level in 1 sentence with the real reason, and say what needs to happen to move up (N1→N2: defined source + 2 weeks of draft attempts with no errors; N2→N3: 4 weeks approving without corrections, only in the part with no risk; N3→N4: 2 months of clean reports and alarms working). If you’re between two levels, **take the lower one**.

### 4. Deliver — save `AGENTE.md`
Save in the current directory (or `agentes/<slug>.md` if an existing `AGENTE.md` from another agent is already there — **never overwrite without asking**). Structure:

```markdown
# Agent Sheet — <Name>
> Level <Nx> · <level name> — <reason in 1 sentence>. To move up: <condition>.

## 1. Mission (intention) … ## 7. Human supervision
(the 7 blocks, short)

## Ready instruction
(second-person prompt, to paste: mission + why it matters; house rules and tone;
official source, what doesn’t count, "if faltar/conflitar: <rule>", "never invent data";
definition of done; level with what it can and can’t do — N2 = "nothing comes out without my explicit OK";
prohibitions + "if they ask, tell them you’ll pass it to me"; when to stop and call me;
report format and schedule, including errors; "before you start, confirm in 3 lines".)

## 3 tests before trusting
1. Information faltando/contraditória in the source → expected: <rule for "if missing">.
2. Prohibited request: "<1st prohibition>" → expected: refusal and calling you.
3. Alarm: "<1st trigger>" → expected: stop and call you.

## Supervision checklist
Before turning it on · Every day (2 min) · Every week (10 min, adjust ONE rule) · Every month (is the level still the right one?)

## Failure log
| date | what broke | smallest correction | changed sheet rule |
```

After saving, show in the conversation only: the level + reason, the file path, and the 3 tests. Don’t dump the whole file.

### 5. If the agent is a CODE agent (Claude Code, Codex, etc.)
Translate the level into the real configuration and add a section `## Configuração sugerida` in AGENTE.md:

| Level | Claude Code | What else |
|---|---|---|
| N0 · N1 | flat mode (`plan`) — only reads and proposes | instruction in `CLAUDE.md`/`AGENTS.md` |
| N2 | standard mode — asks for approval for every edição/comando | prohibitions as rules `deny` in permissions |
| N3 | `acceptEdits` — edits alone, commands keep asking | testes/build as the definition of done; `FALHAS.md` |
| N4 | only with hooks that block irreversibles (push, deploy, delete) + isolated environment | never "bypass" in a repo with production |

Don’t change `settings.json` by yourself: propose the snippet and apply it only if the person asks.

## Mode 2 — Audit
When the person pastes a prompt, a `CLAUDE.md`/`AGENTS.md`, or a description of an existing agent:
1. Give a score **0 (absent) · 1 (vague) · 2 (clear)** for each of the 7 principles, with the evidence (quoted excerpt) or "not found".
2. Apply the level rule to what the text allows and say whether the current autonomy is **above** what the rule accepts — this is the most important finding.
3. List at most 5 corrections, from most risky to least risky, each with the ready-to-paste text.
4. Offer to generate the full Agent Sheet (Mode 1) from what already exists, asking only what’s missing.

## Rules
- One task per sheet. If the person describes three, suggest three sheets and start with the one with the lowest risk.
- Never raise the level to "be useful". The rule only goes down.
- Don’t invent house rules, source, or prohibitions: ask. What the person didn’t say is marked as `[DEFINIR]`.
- Web version for people who don’t use a terminal: https://inematds.github.io/7pa/en/ · gallery: https://inematds.github.io/7pa/galeria/en/
