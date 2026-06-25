import streamlit as st
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

st.title("Optimización de Monitoreo UTI")

st.write("Modelo de Programación Lineal aplicado a un sistema biomédico")

energia = st.slider("Energía disponible (Wh)", 150, 240, 240)

if st.button("Calcular"):

    c = [-10, -5, -8, -6, -4]

    A = [
        [1, 1, 1, 1, 1],
        [4, 2, 3, 2, 1],
        [3, 1, 2, 1, 1],
        [-1, 1, 0, 1, 0],
        [-1, 0, 1, 0, 0]
    ]

    bu = [120, 360, energia, 0, 0]
    bl = [-np.inf, -np.inf, -np.inf, -np.inf, -np.inf]

    constraints = LinearConstraint(A, bl, bu)

    bounds = Bounds(
        [20, 15, 10, 10, 5],
        [np.inf, np.inf, np.inf, np.inf, np.inf]
    )

    res = milp(
        c=c,
        constraints=constraints,
        bounds=bounds,
        integrality=[0,0,0,0,0]
    )

    st.subheader("Resultados")

    st.write("PUD máximo:", -res.fun)
    st.write("ECG:", res.x[0])
    st.write("SpO₂:", res.x[1])
    st.write("Presión arterial:", res.x[2])
    st.write("Frecuencia respiratoria:", res.x[3])
    st.write("Temperatura corporal:", res.x[4])
