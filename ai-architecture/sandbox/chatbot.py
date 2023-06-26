import pip
import os

try:
    import openai
except ImportError as e:
    pip.main(['install', 'openai'])
    import openai

from typing import List, Dict

openai.organization = "org-plLq512k1ocxDkVHLYDsmQXz"
# openai.api_key = os.getenv("OPENAI-API-KEY")
openai.api_key = "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"


def ai_request(request_text,
               system_role="You are a helpful assistant",
               training_messages=None,
               model="gpt-3.5-turbo",
               tokens=1000) -> str:
    """
    Return the AI response generated by the OpenAI GPT-3 model.

    Parameters
    ----------
    request_text : str
        The user's request or question in string format.

    system_role : str
        A

    tokens : int, optional
        The maximum number of tokens (words) that the response can contain. Defaults to 2000.

    Returns
    -------
    str
        The AI-generated response in string format.
    """
    # system role for this project:
    # "You are a health guidance figure helping a user live a healthy life."
    messages = [{"role": "system", "content": system_role}]
    if training_messages and type(training_messages) == list:
        messages += training_messages
    elif training_messages and type(training_messages) == dict:
        messages.append(training_messages)
    messages.append({"role": "user", "content": f"{request_text}"})
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=tokens
    )
    first_choice = 0
    text = response["choices"][first_choice]["message"]["content"]
    return text