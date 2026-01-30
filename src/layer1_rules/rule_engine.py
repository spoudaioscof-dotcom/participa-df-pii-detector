import re

def rule_based_detector(text: str):
    patterns = [
        r"\bcpf\b",
        r"\be-mail\b",
        r"\bjoão\b"
    ]

    for p in patterns:
        if re.search(p, text):
            return True, "Padrão explícito de dado pessoal identificado"

    return False, ""
