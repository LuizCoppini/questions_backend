from .cosmos_client import container
import random

def get_questions_by_type_and_level(question_type, level):
    query = f"SELECT * FROM c WHERE c.type='{question_type}' AND c.level='{level}'"
    items = container.query_items(query=query, enable_cross_partition_query=True)
    return list(items)


def get_random_question(question_type, level):
    # 1) Query todos os documentos
    query = "SELECT c.question, c.options, c.correct FROM c"
    items = list(container.query_items(query=query, enable_cross_partition_query=True))

    # 2) Se não vier nada, retorne None ou faça outro tratamento
    if not items:
        return None

    # 3) Escolha um item aleatório
    return random.choice(items)
