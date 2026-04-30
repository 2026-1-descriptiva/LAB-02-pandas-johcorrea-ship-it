"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd
import os

def pregunta_13():
    path0 = os.path.join(os.path.dirname(__file__), "..", "files", "input", "tbl0.tsv")
    path2 = os.path.join(os.path.dirname(__file__), "..", "files", "input", "tbl2.tsv")
    tbl0 = pd.read_csv(path0, sep="\t")
    tbl2 = pd.read_csv(path2, sep="\t")
    merged = tbl0.merge(tbl2, on="c0")
    return merged.groupby("c1")["c5b"].sum()
