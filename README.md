# 🧭 Gestão de Agentes de IA: os 7 Princípios

[![Gestão de Agentes de IA: os 7 Princípios](capa/capa.png)](https://inematds.github.io/curso-7pa/)

> **Não basta criar agentes. É preciso gerenciá-los.**
> Curso INEMA (formato v2) para delegar trabalho à IA com objetivo claro, limites certos e supervisão que cabe na sua semana.

**Curso:** [Português](https://inematds.github.io/curso-7pa/) · [English](https://inematds.github.io/curso-7pa/en/) · [Español](https://inematds.github.io/curso-7pa/es/)

## Percurso — 4 trilhas · 8 módulos · 48 tópicos · 6–8 h

| Trilha | Módulos | Princípios |
|---|---|---|
| 1 · A virada | Da ferramenta à equipe · Separe o marketing do método | fundamentos, os 7 em uma página |
| 2 · Delegar bem | Intenção e contexto · Dados confiáveis e critério de sucesso | 1, 2, 3, 4 |
| 3 · Autonomia e supervisão | Autonomia com limites · Observação e supervisão | 5, 6, 7 |
| 4 · O segredo e o projeto | O segredo: você já sabe isso · Projeto final: seu agente em produção | as 5 revelações + projeto |

Cada tópico tem diagrama SVG, “O que é / Por que aprender / Conceitos-chave”, exemplo pronto para copiar (com objetivo e como verificar), faça/evite, exercício com resposta comentada, e cada módulo termina com uma checagem. Camada de aprendizagem v2: marcar lido, dúvidas, grifos e notas, Minha jornada, export/import e 5 temas de leitura.

## Ferramentas usadas no curso (projeto [7PA](https://github.com/inematds/7pa))

- [Ficha do Agente](https://inematds.github.io/7pa/) — 7 perguntas, nível de autonomia calculado, instrução pronta, testes e checklist
- [Galeria com 10 fichas prontas](https://inematds.github.io/7pa/galeria/) · [Guia dos 7 princípios](https://inematds.github.io/7pa/guia/) · [O Segredo dos 7 Princípios](https://inematds.github.io/7pa-segredo/)
- `materiais/entrevistador.md` (prompt para conversar com o ChatGPT/Claude) e `materiais/ficha-agente-SKILL.md` (skill `/ficha-agente` para Claude Code)

## Como é gerado

O conteúdo autoral fica em `scripts/content_t1.py` … `content_t4.py`; `scripts/build_course.py` gera as 13 páginas PT; `scripts/build_locales.py` monta `en/` e `es/` a partir de traduções em cache (`i18n/en.json`, `i18n/es.json`, GPT-5.4 nano via OpenRouter, só texto, com IDs, código e URLs protegidos). Pipeline adaptado do curso Agent Skills.

```bash
python3 scripts/build_course.py                 # PT
python3 scripts/build_locales.py --source       # extrai unidades de texto
python3 scripts/acquire_locales.py              # traduz só o que é novo (cache + teto de custo)
python3 scripts/build_locales.py                # gera en/ e es/
npm test                                        # 37 checagens de navegador (PT)
node scripts/verify_locales.mjs                 # PT/EN/ES
```

---

[INEMA.CLUB](https://inema.club) · [INEMA.PRO](https://inema.pro)
