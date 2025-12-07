```markdown
<h1 align="center">🛒 Mercado Livre Scraper + ETL + Dashboard</h1>

<p align="center">
  <strong>Pipeline completo de coleta, transformação, análise e visualização de preços do Mercado Livre.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python" />
  <img src="https://img.shields.io/badge/BeautifulSoup-4.x-green" />
  <img src="https://img.shields.io/badge/Pandas-2.x-yellow" />
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit" />
  <img src="https://img.shields.io/badge/Status-Ativo-success" />
</p>

---

## 📌 Sobre o Projeto

Este projeto implementa um **scraper profissional do Mercado Livre**, com:

✔ Extração automática de produtos  
✔ Paginação até N páginas  
✔ ETL completo (Extração → Transformação → Load)  
✔ Cálculo de variação de preço  
✔ Exportação para JSON e CSV  
✔ Dashboard interativo em Streamlit

Ideal para:

- Trabalhos acadêmicos
- Portfólio profissional
- Estudos de Data Engineering
- Monitores reais de preço / oferta

---

## 🧱 Arquitetura do Projeto
```

mercado_livre_scraper/
│
├── data/ # Saída do ETL
│ ├── produtos.json
│ ├── produtos.csv
│
├── src/
│ ├── extractor.py # Scraper do Mercado Livre
│ ├── transform.py # Limpeza e normalização
│ ├── loader.py # Salvamento local
│ └── main.py # Pipeline ETL
│
├── dashboard/
│ └── dashboard.py # Dashboard Streamlit
│
├── requirements.txt
└── README.md

````

---

## 🚀 Como Executar o Projeto

### 1️⃣ Criar e ativar ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate     # Linux/macOS
# .venv\Scripts\activate      # Windows
````

### 2️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 3️⃣ Executar o pipeline ETL

```bash
python3 src/main.py
```

Saída será salva em:

```
data/produtos.json
data/produtos.csv
```

---

## 📊 Executar o Dashboard

Dentro da pasta `dashboard/`:

```bash
streamlit run dashboard.py
```

Acesse no navegador:
👉 [http://localhost:8501](http://localhost:8501)

---

## ✨ Funcionalidades

### 🟡 Scraping Inteligente

- Coleta nome, marca, avaliação, vendidos, preço novo, preço antigo, desconto.
- Extração a partir do DOM real do Mercado Livre (2025).
- Paginação até N páginas.
- Tratamento para evitar erros quando o botão “Seguinte” está desativado.

### 🔵 Transformações (ETL)

- Conversão de strings de preço para float.
- Cálculo de variação percentual.
- Normalização dos campos nulos.
- Limpeza de estrutura para análise.

### 🟢 Dashboard Interativo (Streamlit)

- Tabela dinâmica de produtos.
- Filtros por marca e faixa de preço.
- Histogramas e gráficos com Plotly.
- Exibição dos maiores descontos.
- Métricas de performance (KPIs).

---

### 🔍 Pipeline ETL

```
Extraindo dados do Mercado Livre...
Transformando...
Salvando JSON...
Pipeline finalizado com sucesso!
```

## 🔧 Tecnologias Utilizadas

| Categoria | Tecnologias                |
| --------- | -------------------------- |
| Extração  | Requests, BeautifulSoup    |
| ETL       | Pandas, LXML               |
| Dashboard | Streamlit, Plotly          |
| Ambiente  | Python 3.9+                |
| Deploy    | (opcional) Streamlit Cloud |

---

## 🤝 Contribuição

Sinta-se livre para:

- Abrir PRs
- Melhorar o dashboard
- Criar novas transformações
- Sugestões de features

---

## 🧑‍💻 Autor

**Diogo Bispo**
Automation & AI Engineer
GitHub: [https://github.com/DiogoBispo](https://github.com/DiogoBispo)

---

## ⭐ Se gostou do projeto...

Deixe uma estrela (⭐) no repositório — incentiva e fortalece o portfólio!

```

---
```
