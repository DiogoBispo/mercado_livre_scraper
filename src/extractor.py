import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}

def get_page(url: str):
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return BeautifulSoup(response.text, "lxml")


def extract_products(search: str, max_pages: int = 10):

    base_url = f"https://lista.mercadolivre.com.br/tenis-corrida-masculino"
    current_url = base_url
    page_count = 1

    all_data = []

    while page_count <= max_pages:

        print(f" Extraindo página {page_count}/{max_pages} ...")
        soup = get_page(current_url)

        items = soup.find_all("li", class_="ui-search-layout__item")

        for product in items:
            # ---------- TITULO ----------
            title_tag = product.find("a", class_="poly-component__title")
            nome = title_tag.get_text(strip=True) if title_tag else None
            link = title_tag["href"] if title_tag else None

            # ---------- MARCA ----------
            brand_tag = product.find("span", class_="poly-phrase-label poly-fw-semibold")
            marca = brand_tag.get_text(strip=True) if brand_tag else None

            # ---------- AVALIAÇÃO ----------
            avaliacao = None
            vendidos = None
            review_box = product.find("span", class_="poly-component__review-compacted")
            if review_box:
                labels = review_box.find_all("span", class_="poly-phrase-label")
                if len(labels) >= 1:
                    avaliacao = labels[0].get_text(strip=True)
                if len(labels) >= 2:
                    vendidos = labels[1].get_text(strip=True)

            # ---------- PREÇO ANTIGO ----------
            old_price = None
            old_tag = product.find("s", class_="andes-money-amount")
            if old_tag:
                frac = old_tag.find("span", class_="andes-money-amount__fraction")
                cents = old_tag.find("span", class_="andes-money-amount__cents")
                if frac:
                    old_price = frac.get_text(strip=True)
                    if cents:
                        old_price += "," + cents.get_text(strip=True)

            # ---------- PREÇO NOVO ----------
            new_price = None
            current_box = product.find("div", class_="poly-price__current")
            if current_box:
                frac = current_box.find("span", class_="andes-money-amount__fraction")
                cents = current_box.find("span", class_="andes-money-amount__cents")
                if frac:
                    new_price = frac.get_text(strip=True)
                    if cents:
                        new_price += "," + cents.get_text(strip=True)

            # ---------- DESCONTO ----------
            discount = None
            disc_tag = product.find("span", class_="poly-price__disc_label")
            if disc_tag:
                discount = disc_tag.get_text(strip=True)

            # ---------- ADICIONA ----------
            all_data.append({
                "marca": marca,
                "descricao": nome,
                "preco_novo": new_price,
                "preco_antigo": old_price,
                "avaliacao": avaliacao,
                "vendidos": vendidos,
                "desconto": discount,
                "link": link
            })
       
        # ---------- PAGINAÇÃO ----------
        next_btn = soup.select_one("li.andes-pagination__button--next a")

        if not next_btn:
            print(" Nenhum botão 'Seguinte' encontrado. Fim das páginas.")
            break
        
        next_href = next_btn.get("href", "")

        if not next_href.strip():
            print(" Botão 'Seguinte' sem URL (provável última página).")
            break
        
        print(f"👉 Indo para próxima página: {next_href}")

        current_url = next_href
        page_count += 1


    return all_data
