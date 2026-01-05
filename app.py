import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, Symbol

# Título de la app
st.title("Graficador de Funciones Matemáticas")

# Instrucciones para el usuario
st.write("""
Ingresa una función matemática en términos de **x**.  
Ejemplos válidos:
- `x**2`
- `sin(x)`
- `x**3 + 2*x + 1`
- `exp(-x**2)`
- `sqrt(x)`
""")

# Campo de texto para que el usuario ingrese la función
funcion_texto = st.text_input("Escribe tu función:", value="x**2")

# Rango para graficar (puedes cambiarlo después si quieres)
x_min = st.number_input("Valor mínimo de x:", value=-10.0)
x_max = st.number_input("Valor máximo de x:", value=10.0)

# Botón para graficar
if st.button("Graficar"):
    try:
        # Convertir el texto a una expresión matemática
        x = Symbol('x')
        expr = sympify(funcion_texto)
        
        # Crear puntos para graficar
        x_vals = np.linspace(x_min, x_max, 500)
        y_vals = [expr.subs(x, val) for val in x_vals]
        
        # Crear el gráfico con matplotlib
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label=f"f(x) = {funcion_texto}")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.set_title("Gráfico de la función")
        ax.grid(True)
        ax.legend()
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        
        # Mostrar el gráfico en Streamlit
        st.pyplot(fig)
        
        st.success("¡Gráfico generado correctamente!")
        
    except Exception as e:
        st.error("Error en la función. Verifica la sintaxis.")
        st.error(f"Detalles: {str(e)}")
# sync
