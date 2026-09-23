"""Conteúdo autoral do curso Gestão de Agentes de IA: os 7 Princípios.
Fonte: ~/projetos/7pa (conteudo/, guia/, galeria, skill ficha-agente) e ~/projetos/7pa-segredo.
Cada trilha vive em content_t<N>.py e é executada neste namespace (usa module() e topic())."""
from pathlib import Path

TRACKS = [
 ('A virada', 'Da IA que responde à IA que trabalha, e o que muda no seu papel.', 'emerald', '01'),
 ('Delegar bem', 'Intenção, contexto, dados e critério: o que o agente precisa saber antes de começar.', 'blue', '02'),
 ('Autonomia e supervisão', 'Quanta liberdade dar, como acompanhar e quando subir de nível.', 'purple', '03'),
 ('O segredo e o projeto', 'Gestão de gente com outro nome, agentes de código e o seu agente em produção.', 'amber', '04'),
]
MODULES = []

def module(id, title, desc, punch, minutes, goal, quiz):
    m = dict(id=id, title=title, desc=desc, punch=punch, minutes=minutes, goal=goal, quiz=quiz, topics=[])
    MODULES.append(m)
    return m

def topic(m, title, what, why, keys, labels, caption, example, do, avoid, exercise, answer, kind='flow'):
    m['topics'].append(dict(title=title, what=what, why=why, keys=keys.split('|'), labels=labels.split('|'),
                            caption=caption, example=example, do=do, avoid=avoid, exercise=exercise, answer=answer, kind=kind))

_here = Path(__file__).resolve().parent
for _n in (1, 2, 3, 4):
    exec((_here / f'content_t{_n}.py').read_text(), globals())

assert [m['id'] for m in MODULES] == ['1-1', '1-2', '2-1', '2-2', '3-1', '3-2', '4-1', '4-2'], [m['id'] for m in MODULES]
for _m in MODULES:
    assert len(_m['topics']) == 6, (_m['id'], len(_m['topics']))
    for _t in _m['topics']:
        assert len(_t['keys']) == 4 and len(_t['labels']) == 4, (_m['id'], _t['title'])
        assert _t['kind'] in ('flow', 'cycle', 'tree', 'layers', 'steps'), _t['kind']
