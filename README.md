# Chatbot de Pizzaria com Rasa

Projeto acadêmico para estudar Processamento de Linguagem Natural (NLP) com um chatbot de pizzaria.

## Objetivos da atividade

O chatbot deve:

1. Identificar a intenção `fazer_pedido`;
2. reconhecer dez sabores de pizza;
3. extrair a quantidade de pizzas;
4. testar se o treinamento foi aprendido corretamente.

### Conceitos principais

- **Intenção (`intent`)**: objetivo da mensagem, como `fazer_pedido`.
- **Entidade (`entity`)**: informação extraída da mensagem, como `sabor` e
  `quantidade`.
- **Slot**: espaço em que o Rasa guarda uma entidade para usá-la na resposta.

Os dez sabores treinados são: calabresa, mussarela, margherita, portuguesa,
frango com catupiry, quatro queijos, pepperoni, carne seca, napolitana e
vegetariana.

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

## Testar o reconhecimento

Para validar os arquivos:

```bash
rasa data validate
```

Para treinar o modelo:

```bash
rasa train
```

Para testar o NLU:

```bash
rasa test nlu --nlu data/nlu.yml
```

Para testar exemplos separados do treinamento:

```bash
rasa test nlu --nlu tests/nlu.yml
```

Para conversar com o chatbot:

```text
Quero duas pizzas de calabresa
Pode fazer 3 pizzas de quatro queijos
Gostaria de uma pizza vegetariana
```

## Observação

A pasta `.venv` contém a instalação local do Python e não deve ser enviada ao GitHub. O arquivo `.gitignore` já impede que ela seja adicionada ao repositório.
