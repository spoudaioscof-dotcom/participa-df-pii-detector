def risk_score(text: str) -> float:
    if "meu" in text or "minha" in text:
        return 0.5
    return 0.1
