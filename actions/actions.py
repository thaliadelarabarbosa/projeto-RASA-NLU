
import re

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


class ActionProcessarPedido(Action):

    def name(self):
        return "action_processar_pedido"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):

        texto = tracker.latest_message.get("text", "").lower()
        entidades = tracker.latest_message.get("entities", [])

        entidades = sorted(
            entidades,
            key=lambda entidade: entidade.get("start", 0)
        )

        numeros = {
            "um": 1,
            "uma": 1,
            "dois": 2,
            "duas": 2,
            "três": 3,
            "tres": 3,
            "quatro": 4,
            "cinco": 5,
            "seis": 6,
            "sete": 7,
            "oito": 8,
            "nove": 9,
            "dez": 10
        }

        # Lista dos sabores disponíveis
        lista_sabores = [
            "frango com catupiry",
            "quatro queijos",
            "calabresa",
            "portuguesa",
            "marguerita",
            "pepperoni",
            "brócolis",
            "bacon",
            "atum",
            "frango"
        ]

        quantidades = []
        sabores = []

        # Identifica os sabores diretamente no texto
        # Isso evita depender somente da classificação do Rasa
        for nome_sabor in lista_sabores:

            padrao = r"\b" + re.escape(nome_sabor) + r"\b"

            for correspondencia in re.finditer(padrao, texto):

                inicio = correspondencia.start()
                fim = correspondencia.end()

                # Evita duplicar um sabor já identificado
                ja_existe = any(
                    sabor["start"] == inicio
                    and sabor["end"] == fim
                    for sabor in sabores
                )

                if not ja_existe:
                    sabores.append({
                        "valor": nome_sabor,
                        "start": inicio,
                        "end": fim
                    })

        # Identifica quantidades pelo texto e pelas entidades
        for entidade in entidades:

            tipo = entidade.get("entity")
            inicio = entidade.get("start", 0)
            fim = entidade.get("end", 0)

            trecho = texto[inicio:fim].lower().strip()

            # Se for "quatro queijos", não é quantidade
            if trecho == "quatro queijos":
                continue

            # Corrige "quatro" quando aparece antes de pizza/pizzas
            depois = texto[fim:].lstrip()

            if trecho == "quatro" and re.match(
                r"pizzas?\b", depois
            ):
                tipo = "quantidade"

            if tipo == "quantidade":

                try:
                    numero = int(trecho)
                except ValueError:
                    numero = numeros.get(trecho)

                if numero is not None:
                    quantidades.append({
                        "valor": numero,
                        "start": inicio,
                        "end": fim,
                        "usada": False
                    })

        # Ordena os sabores pela posição na frase
        sabores.sort(key=lambda sabor: sabor["start"])

        # Relaciona cada sabor com sua quantidade
        itens_pedido = []

        for sabor in sabores:

            quantidade = 1
            quantidade_encontrada = None

            # Primeiro procura a quantidade antes do sabor
            anteriores = [
                item for item in quantidades
                if not item["usada"]
                and item["end"] <= sabor["start"]
            ]

            if anteriores:

                quantidade_encontrada = max(
                    anteriores,
                    key=lambda item: item["end"]
                )

            else:

                # Se não houver quantidade antes, procura depois
                posteriores = [
                    item for item in quantidades
                    if not item["usada"]
                    and item["start"] >= sabor["end"]
                ]

                if posteriores:

                    quantidade_encontrada = min(
                        posteriores,
                        key=lambda item: item["start"]
                    )

            if quantidade_encontrada is not None:
                quantidade = quantidade_encontrada["valor"]
                quantidade_encontrada["usada"] = True

            itens_pedido.append(
                f"{quantidade} pizza(s) de {sabor['valor']}"
            )

        # Se nenhum sabor foi identificado
        if not itens_pedido:

            dispatcher.utter_message(
                text="Não consegui identificar os sabores do pedido. Pode informar novamente?"
            )

            return [
                SlotSet("itens_pedido", None)
            ]

        # Monta e envia a confirmação
        mensagem = "\n".join(itens_pedido)

        dispatcher.utter_message(
            text=f"Entendi seu pedido:\n{mensagem}"
        )

        return [
            SlotSet("itens_pedido", mensagem)
        ]
