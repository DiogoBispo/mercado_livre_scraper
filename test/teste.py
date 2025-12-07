import sys
import os

# adiciona o diretório src ao PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

#from src.extractor import extract_products

from extractor import extract_products

print(extract_products("tenis-corrida-masculino")[:3])