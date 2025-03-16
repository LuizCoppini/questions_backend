from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .repository import get_questions_by_type_and_level, get_random_question
from .openai_service import generate_procedural_question, translate_json

@require_GET
def questions_list(request):

    question_type = request.GET.get("type")
    level = request.GET.get("level")

    if not question_type or not level:
        return JsonResponse({"error": "Parâmetros 'type' e 'level' são obrigatórios."}, status=400)

    results = get_questions_by_type_and_level(question_type, level)
    return JsonResponse(results, safe=False)


@require_GET
def search_random_question(request):

    id = request.GET.get("id")
    question_types = request.GET.getlist("types")  # ["artificial_intelligence", "history"]
    language = request.GET.get("lang", "en").lower()

    if not question_types or not id:
        return JsonResponse({"error": "Params 'id' and 'types' are required."}, status=400)

    # Busca questão aleatória
    result = get_random_question(id, question_types)
    if not result:
        return JsonResponse({"error": "No question found"}, status=404)

    # Só traduz se o idioma for diferente de inglês
    if language != "en":
        result = translate_json(result, idioma_destino=language) or result

    return JsonResponse(result, safe=False)



@require_GET
def procedural_question(request):
    # Pegar parâmetros ?type=xxx&level=xxx&lang=xxx
    question_type = request.GET.get("type", "variety")
    level = request.GET.get("level", "easy")
    language = request.GET.get("lang", "en")

    question_data = generate_procedural_question(question_type, level, language)
    if question_data is None:
        return JsonResponse({"error": "Failed to generate question"}, status=500)

    return JsonResponse(question_data, safe=False)