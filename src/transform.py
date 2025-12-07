import pandas as pd
import numpy as np

def to_float(price):
    """Converte preços brasileiro para float."""
    if price is None:
        return np.nan
    try:
        return float(price.replace(".", "").replace(",", "."))
    except:
        return np.nan

def clean_data(data):
    df = pd.DataFrame(data)

    # Converte preços
    df["preco_novo"] = df["preco_novo"].apply(to_float)
    df["preco_antigo"] = df["preco_antigo"].apply(to_float)

    # Garante que as colunas são numéricas
    df["preco_novo"] = pd.to_numeric(df["preco_novo"], errors="coerce")
    df["preco_antigo"] = pd.to_numeric(df["preco_antigo"], errors="coerce")

    # Calcula variação somente onde há valor antigo
    df["variacao_preco"] = np.where(
        df["preco_antigo"] > 0,
        ((df["preco_novo"] - df["preco_antigo"]) / df["preco_antigo"]) * 100,
        np.nan
    )

    # Arredonda com segurança
    df["variacao_preco"] = df["variacao_preco"].round(2)

    return df
