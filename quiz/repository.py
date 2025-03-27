from .cosmos_client import container
import random

def get_questions_by_type_and_level(id_question, question_type):
    query = f"SELECT * FROM c WHERE c.id = {id_question} AND c.type='{question_type}'"
    items = container.query_items(query=query, enable_cross_partition_query=True)
    return list(items)


def get_random_question(id, types):

    chosen_type = random.choice(types)

    query = f"""
        SELECT c.question, c.type, c.options, c.level, c.id_correct, c.correct
        FROM c
        WHERE c.id = '{id}' AND c.type = '{chosen_type}'
        """

    items = list(container.query_items(
        query=query,
        enable_cross_partition_query=True
    ))

    if not items:
        return None

    return random.choice(items)
