import openai
import json
from django.conf import settings

# Inicializa a API key
openai.api_key = settings.OPENAI_API_KEY

def generate_procedural_question(question_type, level, language):

    prompt = f"""
    Generate a JSON object with a multiple-choice question about {question_type}.
    The question must have 4 answer options and only one correct answer.
    The difficulty level should be {level}.
    Language: {language}.

    Return only a JSON object with the following structure:

    {{
      "type": "{question_type}",
      "level": "{level}",
      "question": "Generated question",
      "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
      "correct": "Correct answer"
    }}

    Ensure that the JSON format is always valid, without additional text or explanations.
    """

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
        temperature=0.7
    )

    content = response.choices[0].message.content

    try:
        question_data = json.loads(content)
    except json.JSONDecodeError:
        return None

    return question_data
