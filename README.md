# Chatbot de Pizzaria com Rasa NLU

Projeto acadêmico para estudar Processamento de Linguagem Natural (NLP) e criar um chatbot de atendimento para uma pizzaria usando o framework Rasa.

## O que o chatbot aprende

O arquivo `data/nlu.yml` contém exemplos de mensagens para o Rasa identificar:

- `fazer_pedido`: cliente quer pedir uma pizza;
- `consultar_preco`: cliente quer saber um preço;
- `consultar_entrega`: cliente pergunta sobre entrega;
- `consultar_horario`: cliente pergunta o horário de funcionamento.

O projeto também utiliza entidades, que são informações específicas extraídas da mensagem:

- `sabor`: calabresa, mussarela, chocolate;
- `tamanho`: pequena, média, grande;
- `bairro`: local de entrega.

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

## Observação

A pasta `.venv` contém a instalação local do Python e não deve ser enviada ao GitHub. O arquivo `.gitignore` já impede que ela seja adicionada ao repositório.

