import os
import pandas as pd
import json

def save_to_csv(df, filename="data/produtos.csv"):
    os.makedirs("data", exist_ok=True)
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"[OK] Arquivo CSV salvo em: {filename}")

def save_to_json(df, filename="data/produtos.json"):
    os.makedirs("data", exist_ok=True)
    df.to_json(filename, orient="records", force_ascii=False, indent=4)
    print(f"[OK] Arquivo JSON salvo em: {filename}")
