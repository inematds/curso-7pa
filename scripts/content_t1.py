# TRILHA 1 — A virada (fundamento). Executado com exec num namespace que já tem module() e topic().

# ───────────────────────── Módulo 1-1 ─────────────────────────
m=module('1-1','Da ferramenta à equipe','Entenda o que muda quando a IA deixa de só responder e passa a executar tarefas.','Você deixa de fazer e passa a gerenciar',50,'Explicar com as suas palavras o que é um agente de IA e fazer a sua primeira delegação com nível de autonomia calculado.',('Qual é a principal diferença entre usar a IA como ferramenta e trabalhar com um agente de IA?',['O agente usa um modelo de IA mais caro e mais inteligente.','O agente recebe um objetivo e executa passos com ferramentas; você passa a definir, acompanhar e avaliar.','O agente dispensa a revisão humana porque decide sozinho.'],1,'A virada não está no modelo, e sim no papel: o agente age sobre um objetivo usando ferramentas, e você sai da execução para a gestão. A revisão humana continua necessária, sobretudo quando há dinheiro, ação irreversível ou gente de fora.'))

topic(m,'O que é um agente de IA',
 'Um modelo de IA (também chamado LLM, “modelo de linguagem”) é o programa que lê texto e escreve texto, como o que está por trás do ChatGPT ou do Claude. Uma ferramenta é algo que a IA consegue usar para agir no mundo: ler uma planilha, enviar uma mensagem, consultar uma agenda. Um agente de IA é um modelo que recebe um objetivo e usa ferramentas para executar passos até chegar a um resultado. A diferença central: o chat responde, o agente executa.',
 'Quem confunde responder com executar subestima o risco. Uma resposta errada no chat você lê e descarta. Uma ação errada de um agente já aconteceu: a mensagem foi enviada, o pedido foi alterado. Saber o que é um agente é o primeiro passo para decidir o que ele pode ou não fazer sozinho.',
 'Modelo: o cérebro que lê e escreve texto.|Ferramenta: a mão que age, como agenda, planilha ou WhatsApp.|Objetivo: o que o agente precisa alcançar.|Resultado: o que sobra no mundo depois da execução.',
 'Modelo (LLM)|Ferramentas|Objetivo|Ação no mundo',
 'O modelo só vira agente quando ganha um objetivo e ferramentas para agir; sem ferramenta, ele apenas conversa.',
 'Objetivo: perceber a diferença entre um pedido de resposta e um pedido de execução.\n\nCole no ChatGPT ou Claude:\n“Vou te mostrar dois pedidos. Diga qual é RESPONDER e qual é EXECUTAR, e que ferramenta a IA precisaria ter para o segundo:\n1) Me explique como confirmar consultas por WhatsApp.\n2) Confirme pelo WhatsApp as consultas de amanhã da <sua clínica / seu negócio>.”\n\nComo verificar: a IA deve classificar o 1 como resposta e o 2 como execução, citando acesso à agenda e ao WhatsApp como ferramentas.',
 '✓ Pergunte sempre: isso só responde ou também age em algum lugar?','✗ Chamar de agente qualquer conversa com chatbot que só devolve texto.',
 'Liste três tarefas do seu trabalho e marque em cada uma se a IA apenas responderia ou precisaria executar algo.',
 'Exemplo: “resumir um contrato” é responder; “enviar lembrete de pagamento” é executar, porque usa uma ferramenta e fala com gente de fora. As tarefas de execução são as que exigem mais cuidado com limites.',kind='flow')

topic(m,'A virada: antes você executava, agora você gerencia',
 'Antes, o caminho era: pessoa → executa o processo → resultado. Com agentes, passa a ser: pessoa → define a intenção → organiza o contexto → delega → supervisiona → avalia. Contexto é o conjunto de informações que você entrega ao agente para ele decidir bem: regras da casa, exemplos, histórico e a situação atual. Você não some do processo; muda de lugar nele.',
 'Quem continua pensando como executor tende a delegar mal: joga a tarefa e espera milagre, ou refaz tudo por desconfiança. Pensar como gestor significa combinar antes o que é bom resultado e conferir depois. É o que você já faz com um funcionário novo, agora por escrito.',
 'Intenção: dizer o que quer e por quê.|Contexto: entregar as regras e a situação atual.|Delegar: passar a tarefa com limites claros.|Avaliar: conferir o resultado e corrigir o rumo.',
 'Define a intenção|Organiza o contexto|Delega|Supervisiona e avalia',
 'O seu trabalho sai da execução e se espalha em quatro etapas de gestão, antes e depois de o agente agir.',
 'Objetivo: descobrir onde o seu tempo vai ficar depois de delegar uma tarefa.\n\nCole no ChatGPT ou Claude:\n“Hoje eu faço esta tarefa com as minhas mãos: <descreva a tarefa, ex.: responder clientes sobre prazo de entrega>.\nSe um agente de IA passar a executá-la, liste o que continua sendo meu trabalho em quatro blocos: definir a intenção, organizar o contexto, supervisionar e avaliar. Para cada bloco, diga quanto tempo por semana isso deve me tomar.”\n\nComo verificar: a resposta precisa ter os quatro blocos e deixar claro que avaliar e corrigir continuam com você.',
 '✓ Reserve tempo na agenda para revisar o que o agente fez.','✗ Delegar e sumir, achando que o agente vai adivinhar o que você esqueceu de dizer.',
 'Pense num funcionário que você treinou. Escreva o que explicou no primeiro dia.',
 'Isso é o contexto que um agente também precisa. A diferença é que o funcionário deduz o que ficou implícito; o agente só sabe o que está escrito.',kind='steps')

topic(m,'Automação orientada por intenção',
 'Automação é fazer uma tarefa acontecer sem uma pessoa realizando cada passo. Na automação clássica você desenha todos os passos: se chegar e-mail X, faça Y. Na automação orientada por intenção você diz o quê: o objetivo, o que é um bom resultado, os limites e quando a tarefa termina. A IA escolhe parte do caminho.',
 'Descrever a intenção é mais rápido do que desenhar cada passo, mas transfere uma decisão para a máquina. Se a intenção estiver vaga, o agente cumpre a tarefa errada com eficiência. Aprender a escrever intenção boa é a habilidade que mais rende nessa virada.',
 'O quê: o objetivo em uma frase.|O que é bom: como reconhecer um resultado aceitável.|Limites: o que ele nunca pode fazer.|Quando termina: a definição de pronto.',
 'Objetivo|Bom resultado|Limites|Definição de pronto',
 'Uma intenção completa tem quatro partes; faltando qualquer uma, o agente preenche a lacuna do jeito dele.',
 'Objetivo: transformar um pedido vago em uma intenção completa.\n\nCole no ChatGPT ou Claude:\n“Meu pedido é: <ex.: cuide das mensagens da loja>.\nReescreva como intenção completa, com quatro linhas:\nO QUÊ: …\nO QUE É BOM: …\nLIMITES (o que nunca fazer): …\nQUANDO TERMINA: …\nSe faltar informação, me pergunte em vez de inventar.”\n\nComo verificar: as quatro linhas aparecem e a IA fez pelo menos uma pergunta sobre algo que você não disse.',
 '✓ Escreva sempre as quatro partes, mesmo em tarefas pequenas.','✗ Pedir “cuida disso pra mim” sem dizer o que é bom nem o que é proibido.',
 'Pegue um pedido que você faria hoje à IA e escreva as quatro linhas: o quê, o que é bom, limites e quando termina.',
 'Exemplo: o quê, confirmar consultas de amanhã; bom, todo paciente recebeu mensagem; limite, nunca remarcar; termina, às 17h com lista de quem não respondeu. Se você travou em alguma linha, é ali que o agente também travaria.',kind='tree')

topic(m,'O novo fluxo de trabalho',
 'O trabalho com agentes segue um fluxo: Intenção → Contexto → Dados → Execução → Avaliação → Supervisão → Evolução. Fonte da verdade é o lugar oficial de onde vem a informação certa, como a agenda do sistema, e não a planilha antiga. Autonomia é quanta liberdade o agente tem para agir sem pedir licença. Guardrail é uma trava que impede ações proibidas, e log é o registro do que o agente fez, para você conferir depois.',
 'Quando algo dá errado, o fluxo mostra onde procurar: intenção vaga, contexto faltando, dado errado ou avaliação ausente. Sem esse mapa, a reação comum é trocar de ferramenta, quando o problema estava num passo anterior. E o fluxo não termina na execução: o que você aprende volta para melhorar a intenção.',
 'Preparar: intenção e contexto antes de agir.|Alimentar: dados da fonte da verdade.|Executar: o agente age dentro da autonomia e dos guardrails.|Aprender: avaliar pelo log, supervisionar e evoluir.',
 'Intenção e contexto|Dados confiáveis|Execução com travas|Avaliar e evoluir',
 'Os sete passos se agrupam em quatro fases; a última devolve aprendizado para a primeira.',
 'Objetivo: diagnosticar em que passo do fluxo um problema nasceu.\n\nCole no ChatGPT ou Claude:\n“Use este fluxo: 1 Intenção, 2 Contexto, 3 Dados, 4 Execução, 5 Avaliação, 6 Supervisão, 7 Evolução.\nAconteceu isto com a IA no meu trabalho: <ex.: mandou preço antigo para um cliente>.\nDiga em qual passo o problema nasceu, por quê, e qual a menor correção possível nesse passo.”\n\nComo verificar: a IA aponta um passo específico, como Dados, e sugere uma correção pequena, como definir a tabela de preços oficial.',
 '✓ Diante de um erro, pergunte primeiro em que passo do fluxo ele nasceu.','✗ Trocar de ferramenta de IA a cada erro sem olhar intenção, contexto e dados.',
 'Relembre um erro que a IA cometeu com você e classifique em qual dos sete passos ele nasceu.',
 'Na maioria dos casos o erro nasce em Contexto ou Dados: faltou uma regra ou a informação estava desatualizada. A correção costuma ser uma linha a mais nas instruções, não uma ferramenta nova.',kind='layers')

topic(m,'Pessoas + Processos + Agentes',
 'Adotar agentes numa empresa não é só uma questão de tecnologia. Sem coordenação, cada pessoa cria o seu agente, a sua planilha e as suas regras, e surgem agentes duplicados ou conflitantes: dois agentes respondendo o mesmo cliente com informações diferentes. A gestão passa a cuidar de três coisas ao mesmo tempo: pessoas, processos e agentes.',
 'Um agente bem feito dentro de um processo bagunçado piora a bagunça, só que mais rápido. Numa clínica pequena, se a recepcionista e o dono ligarem cada um o seu robô de WhatsApp, o paciente recebe duas mensagens diferentes. Coordenar é saber quem é o responsável por cada agente e qual processo ele atende.',
 'Pessoas: quem define, aprova e responde por cada agente.|Processos: qual rotina o agente atende, do início ao fim.|Agentes: o que cada um faz e o que não faz.|Coordenação: uma lista única para evitar duplicados.',
 'Pessoas|Processos|Agentes|Lista única',
 'As três dimensões precisam de um ponto de encontro: uma lista única de agentes com dono e processo definidos.',
 'Objetivo: montar o inventário de agentes e automações do seu negócio.\n\nCopie esta tabela e preencha, uma linha por agente ou automação que já existe:\nAgente ou automação ; O que faz ; Processo que atende ; Dono (pessoa) ; Fonte da informação\n<ex.: robô do WhatsApp> ; <responde horário> ; <atendimento> ; <Ana> ; <site da loja>\n\nDepois cole no ChatGPT ou Claude: “Aponte agentes duplicados, conflitantes ou sem dono nesta tabela.”\n\nComo verificar: toda linha tem um dono com nome e nenhum processo aparece com dois agentes fazendo a mesma coisa.',
 '✓ Mantenha uma lista única de agentes, cada um com um dono com nome.','✗ Deixar cada pessoa ligar a sua própria automação sem avisar ninguém.',
 'Faça o inventário acima com pelo menos três itens, incluindo automações simples como resposta automática de e-mail.',
 'É comum descobrir automações esquecidas ou sem dono. Agente sem dono não é revisado, e o que não é revisado acaba repetindo erro sem ninguém notar.',kind='cycle')

topic(m,'Sua primeira delegação hoje',
 'A melhor forma de entender a virada é delegar uma tarefa pequena de verdade, passando pelas sete perguntas: intenção, contexto, dados, critério de sucesso, autonomia, observação e supervisão. A Ficha do Agente faz essas perguntas e calcula o nível de autonomia, de N0 (só consulta) a N4 (toca um processo inteiro). Você sai com uma instrução pronta, três testes e uma checklist.',
 'Ler sobre gestão de agentes não muda nada; fazer uma ficha muda. O nível calculado mostra na prática a regra central: se a tarefa envolve dinheiro, ação que não se desfaz ou gente de fora, o agente fica em N2, e nada sai sem o seu OK. Começar pequeno e baixo é o caminho seguro para subir depois com evidência.',
 'Escolher: uma tarefa pequena e repetida.|Responder: as sete perguntas com exemplos reais.|Calcular: o nível sai da regra, não do gosto.|Testar: rodar os três testes antes de confiar.',
 'Escolha a tarefa|7 perguntas|Nível calculado|3 testes',
 'A primeira delegação segue quatro passos, e o nível é consequência das respostas, não uma escolha livre.',
 'Objetivo: fazer a sua primeira ficha de agente em 10 minutos.\n\nCaminho A (formulário): abra https://inematds.github.io/7pa/?preset=clinica\nLeia a ficha pronta da clínica e depois troque os campos pela sua tarefa: <sua tarefa>.\nOutras fichas prontas: https://inematds.github.io/7pa/galeria/\n\nCaminho B (conversa), cole no ChatGPT ou Claude:\n“Seja meu entrevistador de gestão de agentes. Faça UMA pergunta por vez, em linguagem simples, nesta ordem: intenção, contexto, dados, critério de sucesso, autonomia, observação, supervisão. No fim calcule o nível: consulta N0; rascunho N1; executa N3; processo inteiro N4; se envolver dinheiro, ação irreversível ou gente de fora, no máximo N2; sem fonte oficial, no máximo N1. Entregue a ficha, a instrução pronta, 3 testes e a checklist. Minha tarefa: <sua tarefa>.”\n\nComo verificar: a ficha da clínica sai N2, porque a mensagem vai para gente de fora e não se desfaz; a sua ficha deve trazer o nível com o motivo em uma frase.',
 '✓ Comece por uma tarefa pequena e aceite o nível que a regra calcular.','✗ Subir o nível na mão para “ganhar tempo” antes de ter evidência.',
 'Abra a galeria, escolha a ficha mais parecida com a sua área e anote o nível e o motivo.',
 'Exemplos: advocacia sai N0, porque só pesquisa; salão sai N1, porque só prepara rascunhos; restaurante chega a N3, porque executa algo interno e reversível. Se a sua tarefa fala com cliente, espere N2.',kind='steps')

# ───────────────────────── Módulo 1-2 ─────────────────────────
m=module('1-2','Separe o marketing do método','Aprenda a filtrar o discurso sobre IA e ficar com o que dá para aplicar.','Tire os adjetivos, fique com o método',50,'Filtrar qualquer relatório sobre IA em 1 minuto e reconhecer os 7 princípios como método prático.',('Um relatório diz que certa plataforma traz “uma revolução sem precedentes na gestão de agentes”. Qual é a atitude mais útil?',['Adotar a plataforma logo, antes da concorrência.','Descartar tudo, porque relatório de empresa é só propaganda.','Tirar os adjetivos, perguntar quem ganha se você acreditar e procurar evidência de uso real.'],2,'Nem acreditar em tudo nem descartar tudo: o filtro separa a narrativa do que é tecnicamente útil. Quase sempre sobra uma prática já conhecida com nome novo, e ela pode ser valiosa.'))

topic(m,'As 3 camadas: narrativa, filtro e método',
 'O material deste curso nasceu de três textos que são três camadas do mesmo assunto. O relatório é a narrativa: vende a ideia, com tom de nova era. A análise é o filtro: separa a propaganda do que é tecnicamente real e admite que são práticas já existentes. Os 7 princípios são o método: o que sobra, organizado para usar amanhã.',
 'Todo conteúdo sobre IA mistura essas camadas, e quem não as separa fica entre o entusiasmo e a desconfiança. Separar permite aproveitar a parte útil sem comprar a promessa. Essa habilidade vale para qualquer notícia, palestra ou proposta de fornecedor que você receber.',
 'Narrativa: o discurso que vende e inspira.|Filtro: a pergunta sobre o que é real.|Método: o que dá para aplicar amanhã.|Movimento: cada camada descasca a anterior.',
 'Narrativa (relatório)|Filtro (análise)|Método (7 princípios)|Aplicação amanhã',
 'Da narrativa ao método, cada camada tira volume e deixa só o que se aplica.',
 'Objetivo: separar as três camadas de um texto sobre IA que você recebeu.\n\nCole no ChatGPT ou Claude, seguido do texto:\n“Divida o texto abaixo em três partes:\n1. NARRATIVA: frases que vendem ou inspiram, sem ação concreta.\n2. FILTRO: o que é real e o que é exagero.\n3. MÉTODO: até 5 ações práticas que eu posso aplicar amanhã.\nTexto: <cole aqui o texto>”\n\nComo verificar: a parte MÉTODO tem ações com verbo e objeto, como “definir a fonte oficial dos preços”, e não frases como “abraçar a nova era”.',
 '✓ Ao ler sobre IA, pergunte: o que sobra depois do filtro?','✗ Perguntar apenas “isso é revolucionário?”, que só leva a sim ou não.',
 'Pegue a última notícia ou post sobre IA que você leu e escreva uma frase de cada camada.',
 'Se a camada de método ficou vazia, o texto era só narrativa, e tudo bem saber disso. Se sobrou uma ação concreta, esse é o valor real do texto.',kind='layers')

topic(m,'Filtrar um relatório de IA em 1 minuto',
 'Quatro perguntas filtram quase qualquer texto sobre IA. Quem ganha se eu acreditar nisso? Tirando os adjetivos, o que sobra? Isso é exclusivo ou é prática comum com nome novo? Tem evidência de uso real ou só demonstração? Não é para desqualificar o autor, e sim para entender o tom.',
 'Palavras como “revolucionário”, “nova era” e “sem precedentes” não são informação. Um fornecedor que ganha com a sua compra pode estar certo, mas tem motivo para exagerar. Com as quatro perguntas você decide em um minuto se vale a pena ler com calma ou se basta guardar uma ideia.',
 'Interesse: quem ganha se eu acreditar.|Adjetivos: o que sobra sem eles.|Novidade: exclusivo ou prática comum.|Evidência: uso real ou só demonstração.',
 'Quem ganha?|Sem adjetivos|Exclusivo?|Evidência ou demo',
 'As quatro perguntas funcionam em sequência, como peneiras cada vez mais finas.',
 'Objetivo: pedir à IA que filtre um relatório ou post de IA para você.\n\nCole no ChatGPT ou Claude:\n“Você é um leitor crítico e equilibrado. Analise o texto abaixo com quatro perguntas e responda cada uma em até 3 linhas:\n1. Quem ganha se eu acreditar nisso?\n2. Tirando os adjetivos (revolucionário, nova era, sem precedentes), o que sobra?\n3. Isso é exclusivo ou é prática comum com nome novo?\n4. Há evidência de uso real (números, casos, período) ou só demonstração?\nFeche com: O QUE VALE APLICAR (até 3 itens) e O QUE IGNORAR.\nTexto: <cole aqui>”\n\nComo verificar: a resposta distingue relato de evidência e cita trechos do próprio texto em cada pergunta.',
 '✓ Use as quatro perguntas antes de repassar um texto sobre IA para a equipe.','✗ Tratar demonstração em vídeo como prova de que funciona no seu negócio.',
 'Aplique as quatro perguntas a um anúncio de ferramenta de IA que apareceu para você.',
 'Normalmente a pergunta 4 derruba mais coisas: há muita demonstração e pouco número de uso real. Isso não impede testar a ferramenta, mas indica que o teste deve ser pequeno e reversível.',kind='steps')

topic(m,'Demo não é produção',
 'Uma demonstração, ou demo, mostra o agente funcionando uma vez, em condições escolhidas. Produção é o uso de verdade, todo dia, com clientes reais e situações imprevistas. Confiabilidade é a capacidade de funcionar bem de forma repetida, e ela se mede em cinco pontos: estabilidade, repetibilidade, segurança, recuperação e comportamento diante do inesperado.',
 'O vídeo do agente que agenda tudo sozinho não mostra o paciente que escreve em áudio, o horário duplicado ou a internet que caiu. É nesses casos que o prejuízo acontece. Testar o inesperado antes de confiar é o que separa um brinquedo de uma ferramenta de trabalho.',
 'Estabilidade: funciona hoje e amanhã do mesmo jeito.|Repetibilidade: o mesmo pedido gera resultado parecido.|Segurança: não faz o que é proibido, mesmo se pedirem.|Recuperação: quando erra, avisa e para, não piora.',
 'Estável|Repetível|Seguro|Recupera do erro',
 'Uma demo mostra um acerto; produção exige os quatro pilares ao mesmo tempo, dia após dia.',
 'Objetivo: testar um agente ou prompt fora do caminho feliz antes de confiar nele.\n\nCole no ChatGPT ou Claude, junto com a instrução do seu agente:\n“Esta é a instrução do meu agente: <cole a instrução>.\nCrie 5 testes difíceis para ela: 1) informação faltando, 2) pedido proibido feito com educação, 3) duas fontes que discordam, 4) mensagem confusa ou fora do assunto, 5) o mesmo pedido feito 3 vezes. Para cada teste, diga o comportamento esperado.”\nDepois rode os testes de verdade e anote o resultado.\n\nComo verificar: o agente pede dado em vez de inventar, recusa o proibido e dá respostas parecidas no teste 5.',
 '✓ Rode testes de informação faltando e pedido proibido antes de ligar o agente.','✗ Ligar o agente com clientes reais só porque funcionou bem na primeira tentativa.',
 'Escolha um teste da lista e rode com a IA que você já usa. Anote se ela inventou algo.',
 'Se ela inventou um dado, a instrução precisa dizer onde está a fonte oficial e o que fazer quando faltar informação, por exemplo: pare e me avise. Uma linha resolve boa parte dos casos.',kind='tree')

topic(m,'O gargalo mudou',
 'Gargalo é o ponto que mais atrasa um processo. Antes, o gargalo era executar: faltavam mãos para responder, digitar e conferir. Com agentes, executar fica barato, e o gargalo passa para definir a intenção, criar o contexto, organizar os dados, avaliar o resultado e corrigir o sistema.',
 'Se o gargalo mudou, o investimento também precisa mudar. Muita gente compra mais ferramentas quando o que falta é clareza sobre o que se quer e dados organizados. Um dono de loja que define bem a tabela oficial de preços ganha mais do que outro que troca de IA todo mês.',
 'Definir: o que se quer e por quê.|Organizar: contexto e dados oficiais.|Avaliar: conferir contra um critério combinado.|Corrigir: ajustar uma regra de cada vez.',
 'Definir|Organizar|Avaliar|Corrigir',
 'O novo gargalo é um ciclo de gestão; quem gira esse ciclo com frequência melhora mais rápido.',
 'Objetivo: descobrir qual é o seu gargalo real com IA hoje.\n\nCole no ChatGPT ou Claude:\n“Trabalho como <sua função> e uso IA para <tarefas>. Os problemas que mais aparecem são: <liste 3>.\nPara cada problema, diga se o gargalo é: DEFINIR (intenção vaga), ORGANIZAR (contexto ou dados), AVALIAR (sem critério) ou CORRIGIR (erro que se repete). Sugira a menor ação para o maior gargalo.”\n\nComo verificar: pelo menos um problema é classificado fora da execução, e a ação sugerida é pequena, como escrever uma regra ou apontar uma fonte.',
 '✓ Invista primeiro em clareza e dados antes de trocar de ferramenta.','✗ Achar que o problema é sempre o modelo de IA não ser bom o bastante.',
 'Anote quanto tempo você gasta por semana definindo, organizando, avaliando e corrigindo o trabalho da IA.',
 'Se quase todo o tempo vai para corrigir, falta critério de sucesso ou dado oficial. Tempo gasto em definir parece lento, mas é o que reduz o tempo de correção.',kind='cycle')

topic(m,'Engenharia de contexto: o menor contexto que decide bem',
 'Engenharia de contexto é escolher com cuidado o que entregar ao agente para ele decidir bem. Lembrando: contexto é o conjunto de informações que o agente recebe, como regras, exemplos e histórico. Mais contexto não é melhor. O objetivo é o menor contexto capaz de produzir a melhor decisão.',
 'Cada informação a mais custa: o modelo cobra por volume de texto, demora mais e pode se confundir com regras antigas ou contraditórias. Jogar o manual inteiro da empresa no agente costuma piorar a resposta. Um documento curto com as regras da casa vale mais do que mil mensagens soltas.',
 'Essencial: regras que mudam a decisão.|Exemplo: um caso bom e um caso ruim.|Estado atual: a situação de hoje.|Fora: o que não muda a decisão.',
 'Regras essenciais|Exemplos|Estado atual|Cortar o resto',
 'Contexto bom é filtrado: entra o que muda a decisão, e o resto fica de fora.',
 'Objetivo: enxugar as instruções do seu agente sem perder qualidade.\n\nCole no ChatGPT ou Claude:\n“Estas são as instruções que eu dou para a IA: <cole suas instruções>.\nClassifique cada linha em: ESSENCIAL (muda a decisão), EXEMPLO ÚTIL, ESTADO ATUAL, ou CORTAR (repetida, antiga ou que não muda nada). Depois escreva a versão enxuta, com no máximo 15 linhas.”\n\nComo verificar: rode a mesma pergunta com a versão longa e a enxuta; a enxuta deve responder igual ou melhor.',
 '✓ Guarde as regras da casa num documento curto e revise quando algo mudar.','✗ Colar todo o histórico e todos os manuais achando que mais é sempre melhor.',
 'Escreva as 5 regras que você explicaria no primeiro dia a alguém que vai fazer sua tarefa. Só 5.',
 'Limitar a 5 obriga a escolher o que realmente muda a decisão. As outras regras podem entrar depois, se um teste mostrar que fazem falta.',kind='flow')

topic(m,'Os 7 princípios em uma página',
 'Os 7 princípios são o método deste curso: intenção, contexto, dados confiáveis, critério de sucesso, autonomia com limites, observação e supervisão humana. Cada um responde a uma pergunta que você faria a um funcionário novo. Eles formam um ciclo: o que você aprende supervisionando volta para ajustar a intenção.',
 'Ter o mapa inteiro numa página ajuda a localizar cada módulo das próximas trilhas e a diagnosticar problemas. Se você já gerenciou pessoas, já conhece quase tudo isso com outro nome. A diferença é que o agente não pega no ar o que você esqueceu de dizer.',
 'Definir: intenção e contexto.|Alimentar: dados confiáveis e critério de sucesso.|Soltar com travas: autonomia com limites.|Acompanhar: observação e supervisão humana.',
 'Definir|Alimentar|Soltar com travas|Acompanhar',
 'Os sete princípios se agrupam em quatro movimentos que giram em ciclo, sempre voltando para a intenção.',
 'Objetivo: ter o mapa dos 7 princípios à mão e usá-lo como checklist de qualquer delegação.\n\n1 Intenção — O que você quer tirar da sua mão, e por quê? — Antes de delegar, defina o propósito.\n2 Contexto — O que você explicaria no 1º dia a alguém recém-contratado? — O menor contexto capaz da melhor decisão.\n3 Dados confiáveis — De onde vem a informação certa? Quem manda quando duas fontes discordam? — Nenhum agente é melhor que seus dados.\n4 Critério de sucesso — Como é um dia em que isso ficou perfeito? — Toda delegação precisa de sucesso definido.\n5 Autonomia com limites — O que ele nunca pode fazer sozinho? — Autonomia cresce com evidência e controle.\n6 Observação — O que você quer ver para saber se está indo bem? — O que não é observado não melhora.\n7 Supervisão humana — Quando ele te chama? Quando você revisa? — Agentes ampliam; não eliminam o julgamento.\n\nPara aplicar: https://inematds.github.io/7pa/ · explicação: https://inematds.github.io/7pa/guia/ · por trás dos textos: https://inematds.github.io/7pa-segredo/\n\nComo verificar: pegue uma tarefa sua e responda as 7 perguntas em uma linha cada; se alguma ficou em branco, é o ponto fraco da delegação.',
 '✓ Use as 7 perguntas como checklist antes de ligar qualquer agente.','✗ Tratar os princípios como lista para decorar em vez de perguntas para responder.',
 'Responda as 7 perguntas para a tarefa que você escolheu no módulo anterior, uma linha cada.',
 'É comum travar em dados e em critério de sucesso: são os princípios que exigem decisão sua, não da IA. Esses dois pontos serão aprofundados nas próximas trilhas.',kind='cycle')
