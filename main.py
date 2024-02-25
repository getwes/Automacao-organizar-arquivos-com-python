"""Importando"""
import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="selecione uma pasta")

lista_arquivos = os.listdir(caminho)
print(lista_arquivos)

locais = {
    "imagens": [".png", ".jpg"],
    "planilhas": [".exe", ".rar", ".zip", ".xlsx", "docx", ".msi"],
    "pdfs": [".pdf"],
    "csv": [".csv"]
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")