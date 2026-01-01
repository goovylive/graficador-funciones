import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, Symbol

st.title("Graficador de Funciones Matemáticas")

st.write("""
Ingresa una función matemática en términos de **x**.  
Ejemplos válidos:
- `x**2`
- `sin(x)`
- `x**3 + 2*x + 1`
- `exp(-x**2)`
- `sqrt(x)`
""")

funcion_texto = st.text_input("Escribe tu función:", value="x**2")

x_min = st.number_input("Valor mínimo de x:", value=-10.0)
x_max = st.number_input("Valor máximo de x:", value=10.0)

if st.button("Graficar"):
    try:
        x = Symbol('x')
        expr = sympify(funcion_texto)
        
        x_vals = np.linspace(x_min, x_max, 500)
        y_vals = [expr.subs(x, val) for val in x_vals]
        
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label=f"f(x) = {funcion_texto}")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.set_title("Gráfico de la función")
        ax.grid(True)
        ax.legend()
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        
        st.pyplot(fig)
        
        st.success("¡Gráfico generado correctamente!")
        
    except Exception as e:
        st.error("Error en la función. Verifica la sintaxis.")
        st.error(f"Detalles: {str(e)}")
