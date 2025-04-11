import streamlit as st
from scipy.stats import bernoulli
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

def caminata_aleatoria_bernoulli(pasos, probabilidad, walks=1):
    """
    Realiza una caminata aleatoria de Bernoulli.

    Args:
        pasos (int): El número de pasos en la caminata.
        probabilidad (float): La probabilidad de que cada paso sea hacia arriba (1) o hacia abajo (-1).

    Returns:
        list: Una lista que representa la posición en cada paso de la caminata.
    """
    random_walks = []
    for i in range(walks):
        random_step = bernoulli.rvs(probabilidad, size=pasos)*2-1
        random_walk = np.insert(random_step.cumsum(), 0, 0)
        random_walks.append(random_walk)

    return random_walks

def graficar_caminata_aleatoria_bernoulli(random_walks, steps, proba=0.5):
    """
    Grafica una caminata aleatoria de Bernoulli.

    Args:
        random_walk (list): Una lista que representa la posición en cada paso de la caminata.
        steps (int): El número de pasos en la caminata.
        proba (float): La probabilidad de que cada paso sea hacia arriba (1) o hacia abajo (-1).
    """
    colors = px.colors.qualitative.Plotly
    fig = go.Figure()

    x = np.arange(0, steps + 1 ) 
    for i, trayectoria in enumerate(random_walks):
        print(trayectoria)

        fig.add_trace(
            go.Scatter(
                x=x,
                y=trayectoria,
                mode="lines+markers" if steps <= 100 else "lines",
                line=dict(color=colors[i % len(colors)], width=1),
                showlegend=False,
            )
        )

    
    # Esperanza step(proba(1-proba))
    fig.add_hline(y=steps*(proba-(1-proba)), line_dash="dash", line_color="red", annotation_text="E(X_n) = n(p-q)", annotation_position="bottom right")

    # Varianza step(4*proba*(1-proba))
    x_band = np.concatenate([x, x[::-1]])


    banda_sup = np.sqrt(4*x*proba*(1-proba))
    banda_inf = -np.sqrt(4*x*proba*(1-proba))
    

    y_band = np.concatenate([banda_sup, banda_inf[::-1]])
    fig.add_trace(
         go.Scatter(
             x=x_band,
             y=y_band,
             fill="toself",
             fillcolor="rgba(72, 126, 176, 0.2)",
             line=dict(color="rgba(0,0,0,0)"),
             hoverinfo="skip",
             showlegend=True,
            name="Varianza 4npq",
        )
    )


    fig.update_layout(title='Caminata Aleatoria de Bernoulli', xaxis_title='Pasos', yaxis_title='Posición',  template="plotly_white",
                        margin=dict(l=40, r=40, t=80, b=40),height=700,
                        xaxis=dict(range=[0, steps+1]))
    return fig





st.set_page_config(
    page_title="Caminata Aleatoria de Bernoulli",
    page_icon="🪙",
    layout="wide",  # Para que ocupe toda la pantalla
    initial_sidebar_state="expanded"
)


with st.sidebar:
    st.title("Caminata Aleatoria de Bernoulli")
    steps = st.slider("Pasos", 1, 1000, 30)
    proba = st.number_input("Probabilidad de subir", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    walks = st.slider("Caminatas", min_value=1, max_value=10, value=1, step=1)
    generate_btn = st.button("Generar Caminata")



    st.write("<img ")


st.title("Caminata Aleatoria de Bernoulli")
st.write("Una caminata aleatoria de Bernoulli es una secuencia de pasos aleatorios en la que cada paso tiene una probabilidad de éxito (p) y una probabilidad de fracaso (q=1-p).\
         En este caso, cada paso puede ser hacia arriba (1) o hacia abajo (-1).")
st.latex(r"X_i = \begin{cases} 1 & \text{con probabilidad } p \\ -1 & \text{con probabilidad } q=1-p \end{cases}")
st.write("La caminata aleatoria de Bernoulli se define como:")
st.latex(r"X_n = \sum_{i=1}^n X_i")
st.write("La caminata tiene las siguientes propiedades:")
st.latex(r"E(X_n) = n(p-q)")
st.latex(r"Var(X_n) = 4npq")
st.write("Cuando $p=q=0.5$, la caminata aleatoria de Bernoulli es una caminata simétrica. en el cual $E(X_n)=0$ y $Var(X_n)=n$.")
st.write("La caminata aleatoria de Bernoulli se puede utilizar para modelar el precio de una acción, el movimiento de un camión, el estado de un sistema, etc.")


if generate_btn:
    st.write("---")
    st.write(f"Generando caminata aleatoria de Bernoulli con {steps} pasos y probabilidad p={round(proba, 2)}, q={round(1-proba)}...")


    random_walks = caminata_aleatoria_bernoulli(steps, proba, walks)
    fig = graficar_caminata_aleatoria_bernoulli(random_walks, steps)
    st.write("Caminata aleatoria de Bernoulli generada:")
    st.plotly_chart(fig, use_container_width=True)
    


