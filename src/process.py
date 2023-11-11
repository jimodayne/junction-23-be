import re
from typing import Literal

from loguru import logger

from .ai import Template, fitmodel, get_answer_chatGPT

available_keys = set(
    [
        "stainless steel hc304",
        "stainless steel hc316",
        "stainless steel hr304",
        "stainless steel hr316",
        "stainless steel cr304",
        "stainless steel cr316",
        "stainless steel cr430",
        "stainless steel bd304",
        "stainless steel bd316",
        "nickel",
    ]
)


def inteprete_action(message: str) -> Literal["predict", "look up", "search"]:
    out = get_answer_chatGPT(Template.gen_ask_action_type(message)).lower()
    if "predict" in out:
        action = "predict"
    elif "search" in out:
        action = "search"
    else:
        action = ""

    return action


def interprete_content2(message: str):
    out = get_answer_chatGPT(Template.gen_ask_what_content(message))

    types = re.findall(r"\"(.*)\"", out)
    if len(types) == 0:
        return ""

    return types[0].lower()


def interprete_content1(message: str):
    out = get_answer_chatGPT(Template.gen_ask_what_predict(message))
    if "price" in out:
        content = "price"
    elif "trend" in out:
        content = "trend"
    else:
        content = ""

    return content


def interprete_time(message: str):
    out = get_answer_chatGPT(Template.gen_ask_time_period(message))

    times = re.findall(r"(\d{1,})", out)
    if len(times) == 0:
        return ""

    return int(times[0])


def polish(prediction, days, content):
    return get_answer_chatGPT(
        Template.gen_polish(content, f"{days} days", prediction),
    )


def gen_response(answer: str = "", references: list = []):
    return {
        "answer": answer,
        "references": references,
    }


def process(message: str) -> dict:
    # Inteprete message
    action = inteprete_action(message)
    logger.info(f"Action: {action}")

    if action != "predict":
        return gen_response("Sorry, you question is quite ambigous.")

    content = interprete_content1(message)
    logger.info(f"Content1: {content}")

    if content != "price":
        return gen_response("Sorry, the content for prediction is quite ambigous.")

    content2 = interprete_content2(message)
    logger.info(f"Content2: {content2}")

    if content2 == "":
        return gen_response("Sorry, the content for prediction is quite ambigous.")
    if content2 not in available_keys:
        return gen_response(f"Sorry, the alloy type '{content2}' not available in database.")

    time = interprete_time(message)
    logger.info(f"Time: {time}")

    if time == "":
        return gen_response("Sorry, the time period is not mentioned.")

    prediction, sources = fitmodel.predict(content2, time, "day")

    polished = polish(prediction, time, content2)

    return gen_response(polished, [sources])
