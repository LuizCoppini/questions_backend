from .cosmos_client import container
import random

def get_questions_by_type_and_level(question_type, level):
    query = f"SELECT * FROM c WHERE c.type='{question_type}' AND c.level='{level}'"
    items = container.query_items(query=query, enable_cross_partition_query=True)
    return list(items)


def get_random_question(id, types):
    # 1) Escolhe aleatoriamente um tipo da lista
    chosen_type = random.choice(types)

    # 2) Monta a query Cosmos DB usando o ID e o tipo escolhido
    #    Exemplo: SELECT question, options, correct de docs onde c.id == my_id e c.type == chosen_type
    query = f"""
        SELECT c.question, c.options, c.correct
        FROM c
        WHERE c.id = '{id}' AND c.type = '{chosen_type}'
        """

    # 3) Executa a query
    items = list(container.query_items(
        query=query,
        enable_cross_partition_query=True
    ))

    # 4) Se não vier nada, retorna None ou outro tratamento
    if not items:
        return None

    # 5) Escolhe aleatoriamente um doc da lista retornada (caso haja mais de 1)
    return random.choice(items)
