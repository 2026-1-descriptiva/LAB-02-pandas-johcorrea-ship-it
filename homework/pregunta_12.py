"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd
import os

def pregunta_12():
    path = os.path.join(os.path.dirname(__file__), "..", "files", "input", "tbl2.tsv")
    df = pd.read_csv(path, sep="\t")
    df["pair"] = df["c5a"] + ":" + df["c5b"].astype(str)
    result = (
        df.groupby("c0")["pair"]
        .apply(lambda x: ",".join(sorted(x.tolist())))
        .reset_index()
        .rename(columns={"pair": "c5"})
    )
    return result
