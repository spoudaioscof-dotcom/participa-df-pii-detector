import pandas as pd

from src.preprocessing.text_cleaner import clean_text
from src.layer1_rules.rule_engine import rule_based_detector
from src.layer2_nlp.predictor import bert_predict
from src.layer3_risk.risk_classifier import risk_score
from src.decision_engine.aggregator import final_decision


def main():
    print("Detector de Dados Pessoais – Desafio Participa DF\n")

    pedidos = [
        {"id": 1, "texto": "Solicito informações sobre o servidor João Silva."},
        {"id": 2, "texto": "Quantos contratos foram assinados em 2023?"}
    ]

    for p in pedidos:
        texto = clean_text(p["texto"])

        hit, reason = rule_based_detector(texto)
        if hit:
            print(p["id"], "→ SENSÍVEL |", reason)
            continue

        prob = bert_predict(texto)
        if prob >= 0.60:
            print(p["id"], "→ SENSÍVEL | NLP contextual")
            continue

        if 0.40 <= prob < 0.60:
            risco = risk_score(texto)
            decisao = final_decision(prob, risco)
            print(p["id"], "→", decisao["label"])
            continue

        print(p["id"], "→ NÃO SENSÍVEL")

    print("\nExecução finalizada com sucesso.")


if __name__ == "__main__":
    main()
