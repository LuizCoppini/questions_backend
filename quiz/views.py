from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .repository import get_questions_by_type_and_level, get_random_question
from .openai_service import generate_procedural_question

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
    question_type = request.GET.get("type")
    level = request.GET.get("level")

    result = get_random_question(question_type, level)
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