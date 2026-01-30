def final_decision(prob_bert: float, risco: float):
    if risco >= 0.35:
        return {
            "label": "SENSÍVEL",
            "probabilidade": max(prob_bert, risco),
            "camadas": ["bert", "risco"],
            "justificativa": "Risco semântico elevado"
        }

    return {
        "label": "NÃO SENSÍVEL",
        "probabilidade": prob_bert,
        "camadas": [],
        "justificativa": "Baixo risco"
    }
