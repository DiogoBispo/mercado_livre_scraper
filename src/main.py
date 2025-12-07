from extractor import extract_products
from transform import clean_data
from loader import save_to_csv
from loader import save_to_json

def run_pipeline():
    print("Extraindo dados do Mercado Livre...")
    produtos = extract_products("smartphone Samsung")

    print("Transformando os dados...")
    df = clean_data(produtos)

    print("Salvando resultado...")
    save_to_json(df)
    save_to_csv(df)

    print("Pipeline finalizado com sucesso!") 
    print(df.head())

if __name__ == "__main__":
    run_pipeline()

