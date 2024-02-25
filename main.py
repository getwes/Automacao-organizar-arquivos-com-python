"""Importando"""
import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="selecione uma pasta")
print(caminho)