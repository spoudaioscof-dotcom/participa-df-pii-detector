# Detector de Dados Pessoais em Pedidos de Acesso à Informação

> **1º Hackathon em Controle Social – Desafio Participa DF**
> Categoria: **Acesso à Informação**

## Visão Geral

Este projeto implementa um **modelo híbrido, explicável e reprodutível** para identificar automaticamente pedidos de acesso à informação classificados como públicos que **contêm dados pessoais**, em conformidade com a **LGPD**.

A solução foi desenhada para **uso real no Participa DF**, priorizando **alta sensibilidade (recall)** — critério-chave do edital — sem comprometer a precisão, utilizando uma **arquitetura em camadas** que combina regras determinísticas e NLP contextual.

---

## Objetivo

Classificar pedidos em duas classes:

* **Sensível (1):** contém dados pessoais (diretos ou indiretos)
* **Não sensível (0):** não contém dados pessoais

A métrica principal é o **F1-score**, com ênfase em **minimizar falsos negativos** para evitar exposição indevida de dados pessoais.

---

## Arquitetura da Solução

A solução adota uma **arquitetura híbrida em três camadas**, seguida de um motor de decisão explicável:

1. **Camada 1 – Regras Determinísticas (Alto Recall)**
   Detecção imediata de PII explícita ou mascarada (CPF, e-mail, telefone etc.).

2. **Camada 2 – NLP Contextual (Transformer)**
   Fine-tuning de modelo BERT em português para identificar dados pessoais implícitos e contextuais.

3. **Camada 3 – Validador de Risco Semântico (LGPD)**
   Classificação de casos limítrofes com base em sinais semânticos (cargo + unidade + período, relatos pessoais, histórico funcional).

4. **Motor de Decisão e Explainability**
   Agregação hierárquica das camadas e geração de justificativas auditáveis.

---

## Estrutura do Projeto

```
participa-df-pii-detector/
│
├── data/
│   ├── raw/                  # Dados sintéticos fornecidos
│   ├── processed/            # Dados tratados
│   └── splits/               # Treino / validação / teste
│
├── models/
│   ├── bert/                 # Checkpoints do modelo NLP
│   └── artifacts/            # Thresholds e métricas
│
├── src/
│   ├── preprocessing/
│   ├── layer1_rules/
│   ├── layer2_nlp/
│   ├── layer3_risk/
│   ├── decision_engine/
│   └── evaluation/
│
├── main.py                   # Execução end-to-end
├── config.yaml               # Parâmetros do modelo
├── requirements.txt
└── README.md
```

---

## Tecnologias Utilizadas

* Python 3.9+
* Hugging Face Transformers
* BERTimbau (`neuralmind/bert-base-portuguese-cased`)
* Scikit-learn
* Regex (re)
* Pandas / NumPy

---

## Instalação

```bash
# Clone o repositório
git clone https://github.com/<usuario>/participa-df-pii-detector.git
cd participa-df-pii-detector

# (Opcional) Crie um ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\\Scripts\\activate  # Windows

# Instale as dependências
pip install -r requirements.txt
```

---

## Execução

```bash
python main.py \
  --input data/raw/pedidos.csv \
  --output results.json
```

---

## Saída do Sistema

Para cada pedido analisado, o sistema retorna:

```json
{
  "id_pedido": "12345",
  "contem_dados_pessoais": true,
  "probabilidade": 0.94,
  "camadas_ativadas": ["regex", "bert"],
  "justificativa": "Padrão de CPF parcialmente mascarado detectado e confirmação contextual via modelo NLP"
}
```

---

## Avaliação e Métricas

* **Precisão**
* **Recall (Sensibilidade)**
* **F1-score (métrica principal)**

O pipeline gera automaticamente relatórios de:

* Falsos negativos (prioridade máxima)
* Falsos positivos
* Casos críticos comentados

---

## Explainability e Conformidade LGPD

* Nenhum dado pessoal real é utilizado
* Cada decisão é rastreável e explicável
* Justificativas claras para auditoria humana
* Arquitetura compatível com uso institucional no setor público

