from re import *


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace("ё", "е")
        text = text.replace("Ё", "Е")
    for i in ["\t", "\n", "\r"]:
        text = text.replace(i, " ")
    text = " ".join(text.split()).strip()
    return text


def tokenize(text: str) -> list[str]:
    text = normalize(text)
    return findall(r"\w+(?:-\w+)*", text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    a = {}
    for i in tokens:
        a[i] = tokens.count(i)
    return a


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    items = list(freq.items())
    items = sorted(items, key=lambda l: (-l[1], l[0]))
    return items[:n]
