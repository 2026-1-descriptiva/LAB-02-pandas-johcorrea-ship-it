"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd
import os

def pregunta_10():
    path = os.path.join(os.path.dirname(__file__), "..", "files", "input", "tbl0.tsv")
    df = pd.read_csv(path, sep="\t")
    result = (
        df.groupby("c1")["c2"]
        .apply(lambda x: ":".join(str(v) for v in sorted(x.tolist())))
        .rename_axis("_c1")
        .to_frame()
    )
    return result