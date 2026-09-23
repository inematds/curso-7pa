from pathlib import Path
from html import escape as e
import json,re,zipfile
from content import MODULES,TRACKS
ROOT=Path(__file__).resolve().parents[1]
COLORS=['#34d399','#60a5fa','#c084fc','#fbbf24']
COURSE='gestao-agentes-7pa'
FICHA='https://inematds.github.io/7pa/'
anti=(ROOT/'assets/head.js').read_text()
manifest={'course':COURSE,'tracks':[{'n':str(i),'title':t[0],'modules':[{'id':m['id'],'title':m['title'],'topics':len(m['topics']),'href':f"curso/trilha{i}/modulo-{m['id']}.html"} for m in MODULES if m['id'].startswith(str(i))]} for i,t in enumerate(TRACKS,1)]}
def meter(scope):
 return f'<div class="meter" data-inema-meter="{scope}" role="progressbar" aria-label="Progresso de leitura" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0"><div class="meter-top"><span data-inema-meter-frac>0 de 0</span><span data-inema-meter-pct>0%</span></div><div class="inema-bar"><div data-inema-meter-fill></div></div></div>'
def appearance():
 groups=[('Tema','theme',[('inema-dark','Escuro'),('claro','Claro'),('sepia','Sépia'),('foco','Foco'),('contraste','Alto contraste')]),('Fonte','font',[('inter','Inter / sistema'),('system','Sistema'),('leitura','Leitura')]),('Tamanho','fontscale',[(100,'100%'),(112,'112%'),(125,'125%')]),('Largura de texto','linewidth',[(60,'Estreita'),(68,'Média'),(75,'Larga')]),('Entrelinha','leading',[(1.45,'Compacta'),(1.7,'Confortável')]),('Acento dos controles','accent',[(x,y) for x,y in [('emerald','Verde'),('blue','Azul'),('purple','Roxo'),('amber','Âmbar'),('teal','Turquesa'),('rose','Rosa')]])]
 return '<div class="appearance-wrap"><button data-inema-appearance-toggle="#appearance" aria-controls="appearance" aria-expanded="false">Aparência</button><div id="appearance" class="inema-appearance-pop" data-inema-appearance data-open="false">'+''.join(f'<h3>{title}</h3><div class="inema-segment">'+''.join(f'<button data-inema-set-{attr}="{v}" aria-pressed="false">{s}</button>' for v,s in opts)+'</div>' for title,attr,opts in groups)+'</div></div>'
def nav(rel,track):
 links=''.join(f'<a class="{"active" if i==track else ""}" href="{rel}curso/trilha{i}/index.html"'+(' aria-current="page"' if i==track else '')+f'><span class="nav-full">{t[0]}</span><span class="nav-short">T{i}</span></a>' for i,t in enumerate(TRACKS,1))
 return f'''<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<nav class="site-nav" aria-label="Navegação principal"><div class="wrap nav-row">
<a class="brand" href="{rel}index.html" aria-label="7 Princípios, início"><svg viewBox="0 0 32 32" fill="none" aria-hidden="true"><circle cx="16" cy="16" r="12" stroke="currentColor" stroke-width="2.2"/><circle cx="16" cy="16" r="3.2" fill="currentColor"/><path d="M16 4v5M16 23v5M4 16h5M23 16h5" stroke="currentColor" stroke-width="2.2"/></svg><span class="brand-name">7 PRINCÍPIOS</span></a>
<a class="text-sky-400" href="https://inema.club" target="_blank" rel="noopener">INEMA.CLUB</a><span class="nav-sep" aria-hidden="true">-</span><a class="nav-pro text-amber-700 dark:text-slate-300" href="https://inema.pro" target="_blank" rel="noopener">PRO</a><div class="nav-links">{links}</div>
<button class="theme-toggle" id="theme-toggle" aria-label="Alternar tema claro e escuro"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.6"/><path d="M12 1v3m0 16v3M1 12h3m16 0h3M4 4l2 2m12 12 2 2M4 20l2-2M18 6l2-2" stroke="currentColor" stroke-width="1.6"/></svg></button></div></nav>
<div class="wrap studybar"><div class="tools"><button data-inema-journey-open>Minha jornada</button><button data-course-resume>Continuar leitura</button>{appearance()}</div>{meter('curso')}</div>'''
def page(title,body,rel='',track=0,quiz=None):
 q=''
 if quiz:
  id,vals=quiz; question,opts,answer,explain=vals
  q=f'<script type="application/json" id="quiz-data">'+json.dumps({'id':id,'q':question,'options':opts,'answer':str(answer),'explain':{str(i):explain for i in range(len(opts))}},ensure_ascii=False)+'</script>'
 return f'''<!DOCTYPE html>
<html lang="pt-BR" class="dark"><head>
<script>{anti}</script>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} | Gestão de Agentes de IA · INEMA</title>
<meta name="description" content="Curso de gestão de agentes de IA: intenção, contexto, dados, critério de sucesso, autonomia com limites, observação e supervisão humana. Com a Ficha do Agente, galeria de casos e projeto final.">
<meta name="inema-course" content="{COURSE}"><meta name="course-root" content="{rel or './'}">
<script type="application/json" data-inema-manifest>{json.dumps(manifest,ensure_ascii=False)}</script>
<link rel="icon" href="{rel}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{rel}assets/course.css"><link rel="stylesheet" href="{rel}assets/learn.css"><link rel="stylesheet" href="{rel}assets/patches.css">
</head><body class="track-{track}">
{nav(rel,track)}
<noscript><p class="wrap no-script">Você pode ler todas as aulas sem JavaScript. Progresso, notas e controles de aparência precisam de JavaScript.</p></noscript>
<main id="conteudo" class="wrap">{body}</main>
<footer><div class="wrap">Gestão de Agentes de IA: os 7 Princípios · INEMA.CLUB · v1.0.0 · Curso em português<br>Material educativo autoral do projeto 7PA. Progresso salvo neste navegador; exporte uma cópia em Minha jornada.<br><a href="{rel}index.html#fontes">Fontes e critérios editoriais</a> · <a href="{FICHA}" target="_blank" rel="noopener">Ficha do Agente</a> · <a href="{rel}materiais/entrevistador.md" download>Prompt entrevistador</a></div></footer>
<dialog id="module-modal" aria-label="Leitura do módulo"><button data-close-modal>Fechar módulo</button><iframe title="Conteúdo completo do módulo"></iframe></dialog>
{q}<script src="{rel}assets/learn.js"></script><script src="{rel}assets/course.js"></script>
</body></html>'''
def diagram(labels,caption,uid,track=4,kind='flow'):
 c=COLORS[track-1]; labels=labels[:4]; w=720;h=200
 defs=f'''<defs><pattern id="{uid}-grid" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="{c}" opacity=".13"/></pattern><filter id="{uid}-glow"><feGaussianBlur stdDeviation="1.8" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter><marker id="{uid}-arrow" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0 7 3.5 0 7" fill="{c}"/></marker></defs>'''
 def box(x,y,ww,hh,text,idx):
  words=text.split();lines=['']
  for word in words:
   if len(lines[-1]+' '+word)>20:lines.append(word)
   else:lines[-1]=(lines[-1]+' '+word).strip()
  yy=y+hh/2-(len(lines)-1)*9+5
  return f'<g><rect x="{x}" y="{y}" width="{ww}" height="{hh}" rx="10" fill="#111827" stroke="{c if idx==0 else "#38bdf8"}" stroke-width="2"'+(f' filter="url(#{uid}-glow)"' if idx==0 else '')+'/>'+''.join(f'<text x="{x+ww/2}" y="{yy+j*19}" text-anchor="middle" fill="#e5e7eb" font-size="14" font-weight="600">{e(s)}</text>' for j,s in enumerate(lines))+'</g>'
 def line(d):return f'<path d="{d}" fill="none" stroke="{c}" opacity=".6" stroke-width="1.8" marker-end="url(#{uid}-arrow)"/>'
 bits=[]
 if kind=='cycle':
  pts=[(40,22),(420,22),(420,116),(40,116)]
  bits=[line('M280 54 H414'),line('M540 87 V110'),line('M420 148 H287'),line('M160 116 V92')]
  bits += [box(x,y,240,64,t,i) for i,((x,y),t) in enumerate(zip(pts,labels))]
 elif kind=='tree':
  bits=[line(f'M225 100 C310 100 315 {y+24} 365 {y+24}') for y in [10,76,142]]
  bits+=[box(20,65,205,70,labels[0],0)]+[box(370,y,325,48,labels[i+1],i+1) for i,y in enumerate([10,76,142])]
 elif kind=='layers':
  for i,t in enumerate(labels):
   x=25+i*175;y=25+i*26
   if i<3:bits.append(line(f'M{x+154} {y+40} H{x+167} V{y+66} H{x+172}'))
   bits.append(box(x,y,150,72,t,i))
 elif kind=='steps':
  for i,t in enumerate(labels):
   x=20+i*175;y=105-i*27
   if i<3:bits.append(line(f'M{x+150} {y+32} H{x+162} V{y+5} H{x+172}'))
   bits.append(box(x,y,150,62,t,i))
 else:
  for i,t in enumerate(labels):
   if i<3:bits.append(line(f'M{175+i*175} 100 H{193+i*175}'))
   bits.append(box(20+i*175,63,150,74,t,i))
 return f'''<figure class="diagram"><div class="diagram-scroll" tabindex="0" role="region" aria-label="Diagrama com rolagem horizontal em telas pequenas"><svg viewBox="0 0 {w} {h}" class="w-full h-auto" role="img" aria-label="{e(' → '.join(labels))}">{defs}<rect width="720" height="200" fill="#0f172a"/><rect width="720" height="200" fill="url(#{uid}-grid)"/>{''.join(bits)}</svg></div><figcaption>{e(caption)}</figcaption></figure>'''
TRACK_FLOW=[['IA que responde','IA que executa','Você define a intenção','Você gerencia o sistema'],['Intenção','Contexto','Dados confiáveis','Critério de sucesso'],['Nível calculado','Limites claros','Relatório e alarmes','Evolução com evidência'],['Gestão de gente','Agentes de código','Sua ficha','Agente em produção']]
def stats(values):return '<div class="stats">'+''.join(f'<div class="stat"><strong>{a}</strong><span>{b}</span></div>' for a,b in values)+'</div>'
def sources():
 return '''<section id="fontes" class="source-box"><h2>Fontes e critérios editoriais</h2><p>O curso parte de três textos do projeto 7PA: um relatório sobre a nova lógica do trabalho com agentes de IA, uma análise crítica que separa a camada promocional do que é tecnicamente relevante, e a síntese dos 7 princípios. Os originais estão em <a href="https://github.com/inematds/7pa/tree/main/conteudo">github.com/inematds/7pa/conteudo</a>. Exemplos, exercícios, diagramas e casos foram desenvolvidos para este curso.</p><p>A regra de cálculo do nível de autonomia (N0 a N4) e os critérios para subir de nível são uma proposta didática do projeto 7PA, pensada para começar com segurança. Não são uma norma técnica nem um padrão de mercado. Adapte ao seu contexto, sempre na direção de mais controle quando houver dúvida.</p><p>As menções a agentes de programação (Claude Code, Codex, CLAUDE.md, AGENTS.md, modos de permissão) descrevem recursos disponíveis em setembro de 2026. Nomes e opções podem mudar conforme a versão e a conta. Estimativas de duração incluem prática; não são medições de alunos.</p><p>Ferramentas do projeto: <a href="https://inematds.github.io/7pa/">Ficha do Agente</a>, <a href="https://inematds.github.io/7pa/galeria/">galeria de fichas</a>, <a href="https://inematds.github.io/7pa/guia/">guia dos 7 princípios</a> e <a href="https://inematds.github.io/7pa-segredo/">O Segredo dos 7 Princípios</a>.</p></section>'''
def landing():
 steps=[('Intenção','o que e por quê'),('Contexto','o mínimo que decide bem'),('Dados confiáveis','a fonte da verdade'),('Critério de sucesso','o que é pronto'),('Autonomia com limites','de N0 a N4'),('Observação','relatório e falhas'),('Supervisão humana','o ciclo que evolui')]
 hero='''<header class="hero hero-split"><div><span class="eyebrow">FORMAÇÃO PRÁTICA · GESTÃO DE AGENTES DE IA · INEMA V2</span><h1>Não basta criar agentes.<br><span style="color:var(--primary)">É preciso gerenciá-los.</span></h1><p class="lead">Aprenda a delegar trabalho para a IA com objetivo claro, limites certos e supervisão que cabe na sua semana.</p><p class="muted">Dos 7 princípios à ficha do seu primeiro agente: explicações visuais, casos de 10 áreas, exemplos prontos para copiar e um projeto final.</p><div class="actions"><a class="btn cta" href="curso/trilha1/modulo-1-1.html">Começar o curso <span aria-hidden="true">→</span></a><a class="btn" href="#trilhas">Explorar as trilhas</a></div></div><div class="hero-panel"><span class="eyebrow">OS 7 PRINCÍPIOS</span><h2>Um ciclo, não uma lista.</h2><div class="source-to-skill">'''+''.join(f'<div class="recipe-line"><span class="num">0{i}</span><span>{a}</span><small>{b}</small></div>' for i,(a,b) in enumerate(steps,1))+'''</div><div class="code-preview"><code>intenção → contexto → dados → critério<br>→ autonomia → observação → supervisão ↺</code></div></div></header>'''
 body=hero+stats([('4','trilhas progressivas'),('8','módulos completos'),('48','tópicos com prática'),('6–8 h','estimativa com exercícios')])
 body+='<section id="trilhas"><div class="section-intro"><div><span class="eyebrow">SEU PERCURSO</span><h2>Da virada ao agente em produção.</h2></div><p>Siga na ordem para chegar ao projeto final com a ficha do seu agente pronta. Já usa agentes? Entre pela trilha que resolve sua próxima dificuldade.</p></div><div class="track-grid">'
 for i,(title,desc,col,num) in enumerate(TRACKS,1):
  names=' / '.join(m['title'] for m in MODULES if m['id'].startswith(str(i)))
  body+=f'<a class="track-card track-{i}" href="curso/trilha{i}/index.html"><div class="meta-row"><span class="eyebrow">TRILHA {num}</span><span>2 módulos · 12 tópicos</span></div><h3>{title}</h3><p>{desc}</p><small>{names}</small><span class="arrow">Explorar trilha →</span></a>'
 body+='</div></section>'
 body+=diagram(['Intenção e contexto','Dados e critério','Autonomia com limites','Observação e supervisão'],'Os 7 princípios formam um ciclo: o que você observa na supervisão volta para ajustar a intenção e as regras do agente.','home',4,'cycle')
 body+='''<section class="editorial-band"><div><span class="eyebrow">VOCÊ VAI CONSTRUIR</span><h2>A ficha do seu primeiro agente, testada e supervisionada.</h2></div><div><p>O projeto final transforma uma tarefa real do seu trabalho em um agente bem gerido: missão, regras da casa, fonte da verdade, definição de pronto, nível de autonomia calculado, relatório, gatilhos e ritual de revisão. Casos de 10 áreas acompanham o percurso, da clínica à agência de marketing.</p><ol class="step-list"><li>Escolher uma tarefa frequente, com saída visível e erro barato.</li><li>Responder as 7 perguntas e calcular o nível de autonomia.</li><li>Rodar os 3 testes antes de confiar e ajustar uma regra por vez.</li><li>Supervisionar a primeira semana com registro de falhas.</li></ol></div></section>
<section id="materiais"><span class="eyebrow">FERRAMENTAS PRONTAS PARA PRATICAR</span><h2>Abra, preencha, use.</h2><p>Tudo gratuito, sem login e rodando no navegador. A skill é opcional, para quem usa Claude Code no terminal.</p><div class="download-list"><a class="btn cta" href="https://inematds.github.io/7pa/" target="_blank" rel="noopener">Ficha do Agente (7 perguntas)</a><a href="https://inematds.github.io/7pa/galeria/" target="_blank" rel="noopener">Galeria com 10 fichas prontas</a><a href="https://inematds.github.io/7pa/guia/" target="_blank" rel="noopener">Guia dos 7 princípios</a><a href="https://inematds.github.io/7pa-segredo/" target="_blank" rel="noopener">O Segredo dos 7 Princípios</a><a href="materiais/entrevistador.md" download>Prompt entrevistador (.md)</a><a href="materiais/ficha-agente-SKILL.md" download>Skill /ficha-agente (.md)</a></div></section>
<section class="editorial-band"><h2>Estude com o seu próprio rastro.</h2><div><p>Marque os tópicos lidos, sinalize dúvidas e selecione trechos das explicações para grifar ou anotar. Em <strong>Minha jornada</strong>, reúna suas notas, exporte um backup e retome o último tópico.</p><p>O progresso mede tópicos marcados como lidos; não é uma certificação de domínio. Resolva os exercícios antes de abrir as respostas. Suas anotações ficam no navegador e não são enviadas a um servidor.</p><p><strong>Pré-requisitos:</strong> nenhum conhecimento técnico. Basta já ter usado o ChatGPT, o Claude ou o Gemini alguma vez. Cada termo novo é explicado na primeira vez que aparece.</p></div></section>'''+sources()
 (ROOT/'index.html').write_text(page('Gestão de Agentes de IA: os 7 Princípios',body))
def trackpage(i):
 title,desc,*_=TRACKS[i-1];mods=[m for m in MODULES if m['id'].startswith(str(i))]
 body=f'<div class="breadcrumb"><a href="../../index.html">Início</a> / Trilha {i}</div><header class="hero"><span class="pill">TRILHA {i:02}</span><h1>{title}</h1><p class="lead">{desc}</p></header>'+stats([('2','módulos'),('12','tópicos'),(str(sum(m['minutes'] for m in mods))+' min','estimativa com prática'),('Prático','nível progressivo')])+meter(f'trilha:{i}')
 body+=diagram(TRACK_FLOW[i-1],desc,f'track{i}',i,'steps')
 body+='<h2>Mapa da trilha</h2><div class="map-grid">'
 for m in mods:body+=f'<a class="map-card" href="#modulo-{m["id"]}"><div class="meta-row"><span>{m["id"].replace("-",".")}</span><span>~{m["minutes"]} min</span></div><h3>🧭 {m["title"]}</h3><p>{m["punch"]}</p></a>'
 body+='</div><h2 class="text-2xl font-bold">Conteúdo detalhado</h2>'
 for m in mods:
  mid=m['id'];body+=f'<article id="modulo-{mid}" class="module-card" data-inema-module="{mid}" data-inema-track="{i}"><span class="eyebrow">MÓDULO {mid.replace("-",".")}</span><h2 class="text-2xl font-bold">{m["title"]}</h2><p>{m["desc"]}</p>{meter("modulo:"+mid)}'
  for j,t in enumerate(m['topics'],1):
   pid=f'panel-{mid}-{j}'
   body+=f'<div class="topic-item"><button class="topic-toggle" aria-expanded="false" aria-controls="{pid}" onclick="toggleTopic(this)"><span class="circle">{j}</span><span>{t["title"]}</span></button><div id="{pid}" class="topic-explanation"><h3>O que é</h3><p>{t["what"]}</p><h3>Por que aprender</h3><p>{t["why"]}</p><h3>Conceitos-chave</h3><ul>'+''.join(f'<li>{v}</li>' for v in t['keys'])+f'</ul><a href="modulo-{mid}.html#topico-{j}">Estudar este tópico e fazer o exercício →</a></div></div>'
  body+=f'<div class="actions"><button data-open-modal="modulo-{mid}.html">Ver em Modal</button><a class="btn cta" href="modulo-{mid}.html">Ver Completo →</a></div></article>'
 body+='<div class="actions"><a class="btn" href="../../index.html">← Todas as trilhas</a>'+ (f'<a class="btn" href="../trilha{i+1}/index.html">Próxima trilha →</a>' if i<4 else '')+'</div>'
 d=ROOT/f'curso/trilha{i}';d.mkdir(parents=True,exist_ok=True);(d/'index.html').write_text(page(title,body,'../../',i))
def modulepage(m):
 mid=m['id'];i=int(mid[0]);title=m['title']
 body=f'<div class="breadcrumb"><a href="../../index.html">Início</a> / <a href="index.html">{TRACKS[i-1][0]}</a> / Módulo {mid.replace("-",".")}</div><header class="hero"><span class="pill">MÓDULO {mid.replace("-",".")}</span><h1>{title}</h1><p class="lead">{m["desc"]}</p><p><strong>Ao final:</strong> {m["goal"]}</p></header>'+stats([('6','tópicos'),(str(m['minutes'])+' min','estimativa com prática'),('6','exercícios comentados'),('1','checagem final')])
 body+='<div class="reading-layout"><aside class="toc" data-inema-toc aria-label="Índice do módulo"><h2>Neste módulo</h2><span data-inema-section-counter>Seção 1 de 6</span><ol>'+''.join(f'<li><a href="#topico-{j}">{j}. {t["title"]}</a></li>' for j,t in enumerate(m['topics'],1))+'</ol>'+meter('modulo:'+mid)+'<p class="muted">Selecione um trecho das explicações para grifar ou anotar.</p></aside>'+f'<article class="lesson-content" data-inema-module="{mid}" data-inema-track="{i}">'
 for j,t in enumerate(m['topics'],1):
  tid=f'modulo-{mid}#topico-{j}';bid=f'm{mid}-t{j}'
  body+=f'<section class="lesson" id="topico-{j}" data-inema-topic="{tid}"><div class="lesson-head"><span class="circle">{j}</span><h2>{t["title"]}</h2></div>'
  body+=diagram(t['labels'],t['caption'],f'd{mid}-{j}',i,t['kind'])
  body+=f'<div class="inema-prose"><h3>O que é</h3><p id="{bid}-p1" data-inema-block="{bid}-p1">{t["what"]}</p><h3>Por que aprender</h3><p id="{bid}-p2" data-inema-block="{bid}-p2">{t["why"]}</p><h3>Conceitos-chave</h3></div><div class="key-grid">'
  for key in t['keys']:
   a,_,b=key.partition(':');body+=f'<div class="key"><strong>{a}</strong>{b.strip()}</div>'
  body+='</div>'
  body+=f'<div class="code-box"><div class="code-head"><span>EXEMPLO COMENTADO · {mid.replace("-",".")}.{j}</span><button data-copy="code-{mid}-{j}">Copiar exemplo</button></div><pre id="code-{mid}-{j}"><code>{e(t["example"])}</code></pre></div>'
  if j in [2,5]:
   body+='<div class="timeline"><h3>Do conceito à ação</h3><ol>'+''.join(f'<li>{e(s)}</li>' for s in [t['labels'][0]+': identificar a condição inicial.',t['labels'][1]+': aplicar a decisão descrita.',t['labels'][2]+': conferir o efeito no exemplo.',t['labels'][3]+': registrar a evidência de saída.'])+'</ol></div>'
  body+=f'<div class="comparison"><div class="compare-good"><h3>✓ Faça assim</h3><p>{t["do"]}</p></div><div class="compare-bad"><h3>✗ Evite este erro</h3><p>{t["avoid"]}</p></div></div>'
  if j in [1,4]:body+=f'<aside class="tip"><strong>Leve para o seu agente.</strong> {t["caption"]} Use essa ideia para revisar a ficha do seu agente antes de avançar.</aside>'
  body+=f'<div class="practice"><h3>Pratique antes de revelar</h3><p>{t["exercise"]}</p><details><summary>Ver resposta comentada</summary><p>{t["answer"]}</p></details></div><div class="read-controls"><button data-inema-read-toggle aria-pressed="false"><span aria-hidden="true">✓</span><span data-inema-read-label>Marcar como lido</span></button><button data-inema-doubt-toggle aria-pressed="false">Tenho uma dúvida</button></div></section>'
 question,opts,answer,expl=m['quiz'];qid='q-'+mid
 body+=f'<section class="quiz" data-inema-check="{qid}"><span class="eyebrow">CHECAGEM SEM BLOQUEIO</span><h2>Confira seu entendimento</h2><p>{question}</p><div class="quiz-options">'+''.join(f'<button data-inema-check-option="{n}">{e(o)}</button>' for n,o in enumerate(opts))+'</div><div data-inema-check-feedback role="status" aria-live="polite"></div></section>'
 body+=f'<section class="module-summary"><h2>O que você leva deste módulo</h2><p>{m["goal"]}</p><ul>'+''.join(f'<li>{t["title"]}.</li>' for t in m['topics'])+'</ul><p>Próxima ação: aplique o que aprendeu na ficha do seu agente e anote o que ainda precisa de revisão.</p></section>'
 idx=MODULES.index(m);body+='<div class="actions"><a class="btn" href="index.html">← Mapa da trilha</a>'
 if idx<len(MODULES)-1:
  nm=MODULES[idx+1];body+=f'<a class="btn cta" href="../trilha{nm["id"][0]}/modulo-{nm["id"]}.html">Próximo: {nm["title"]} →</a>'
 else:body+=f'<a class="btn cta" href="{FICHA}" target="_blank" rel="noopener">Concluir: montar a ficha do seu agente →</a>'
 body+='</div></article></div><p class="muted">Referência deste módulo: materiais do projeto 7PA e <a href="../../index.html#fontes">fontes e critérios editoriais do curso</a>.</p>'
 html=page(title,body,'../../',i,(qid,m['quiz']))
 # HTML formatado por elemento facilita a revisão, sem linhas vazias artificiais.
 html=re.sub(r'><', '>\n<',html)
 (ROOT/f'curso/trilha{i}/modulo-{mid}.html').write_text(html)
landing()
for i in range(1,5):trackpage(i)
for m in MODULES:modulepage(m)
(ROOT/'assets/manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print(f'Geradas 13 páginas, {sum(len(m["topics"]) for m in MODULES)} tópicos e {1+4+sum(len(m["topics"]) for m in MODULES)} diagramas SVG.')
