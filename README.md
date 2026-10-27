# Estudos de NLP com Rasa

Projeto acadêmico para estudar Processamento de Linguagem Natural (NLP) e desenvolver chatbots usando o framework Rasa.

O exemplo de pizzaria utilizado neste repositório é apenas um exercício inicial para compreender os conceitos de intenção, entidade, treinamento e regras de conversa. O projeto poderá ser adaptado posteriormente para outros contextos, como atendimento público, serviços institucionais ou educação.

## Conceitos estudados

O arquivo `data/nlu.yml` contém exemplos de mensagens para o Rasa identificar intenções, ou seja, o objetivo do usuário na conversa:

- `fazer_pedido`: exemplo de uma solicitação do usuário;
- `consultar_preco`: exemplo de uma consulta;
- `consultar_entrega`: exemplo de uma dúvida sobre serviço;
- `consultar_horario`: exemplo de uma consulta de informação.

O projeto também utiliza entidades, que são informações específicas extraídas da mensagem. No exemplo atual:

- `sabor`: informação sobre o sabor escolhido;
- `tamanho`: informação sobre o tamanho escolhido;
- `bairro`: informação sobre o local de entrega.

## Estrutura principal

```text
projeto-RASA-NLU/
├── actions/          # Ações personalizadas, quando forem necessárias
├── data/
│   ├── nlu.yml       # Exemplos de intenções e entidades
│   ├── rules.yml     # Regras de resposta
│   └── stories.yml   # Histórias de conversas
├── tests/            # Testes do assistente
├── config.yml        # Configuração do treinamento
├── credentials.yml   # Canais de comunicação
├── domain.yml        # Intenções, entidades e respostas
└── endpoints.yml     # Endpoints de serviços externos
```

## Requisitos

- Python compatível com a versão do Rasa instalada;
- Rasa instalado em um ambiente virtual;
- Git, para versionamento do projeto.

## Como executar localmente

No Git Bash, entre na pasta do projeto:

```bash
cd ~/Documents/projeto-RASA-NLU
```

Ative o ambiente virtual:

```bash
source .venv/Scripts/activate
```

Treine o modelo:

```bash
rasa train
```

Inicie o chatbot:

```bash
rasa shell
```

Para sair do chatbot, digite:

```text
/stop
```

## Exemplos para testar

```text
Quero pedir uma pizza de calabresa
Quanto custa a pizza?
Vocês entregam no Centro?
Qual é o horário de funcionamento?
```

Essas frases pertencem ao cenário didático da pizzaria. Elas podem ser substituídas por frases de qualquer outro domínio estudado.

## Observação

A pasta `.venv` contém a instalação local do Python e não deve ser enviada ao GitHub. O arquivo `.gitignore` já impede que ela seja adicionada ao repositório.
