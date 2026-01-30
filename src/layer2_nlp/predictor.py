def bert_predict(text: str) -> float:
    keywords = ["servidor", "filho", "doença"]
    for k in keywords:
        if k in text:
            return 0.65
    return 0.20
