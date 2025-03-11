from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.conf import settings

from .cosmos_client import container


@require_GET
def questions_list(request):
    """
    Retorna perguntas com base em ?type=XXX&level=XXX
    Exemplo de chamada: /api/questions?type=biology&level=easy
    """
    question_type = request.GET.get("type")
    level = request.GET.get("level")

    # Montar query dinâmica
    # Se a 'type' e 'level' forem obrigatórias, podemos fazer:
    if not question_type or not level:
        return JsonResponse({"error": "Parâmetros 'type' e 'level' são obrigatórios."}, status=400)

    # Query no Cosmos DB
    # Ex: SELECT * FROM c WHERE c.type = "biology" AND c.level = "easy"
    query = f"SELECT * FROM c WHERE c.type = '{question_type}' AND c.level = '{level}'"

    items = container.query_items(query=query, enable_cross_partition_query=True)

    # Convertemos para lista (o objeto retornado é um iterador)
    results = list(items)

    # Retornamos JSON
    return JsonResponse(results, safe=False)
