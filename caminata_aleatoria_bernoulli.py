import streamlit as st
from scipy.stats import bernoulli
import plotly.graph_objects as go
import plotly.express as px

def caminata_aleatoria_bernoulli(pasos, probabilidad):
    """
    Realiza una caminata aleatoria de Bernoulli.

    Args:
        pasos (int): El número de pasos en la caminata.
        probabilidad (float): La probabilidad de que cada paso sea hacia arriba (1) o hacia abajo (-1).

    Returns:
        list: Una lista que representa la posición en cada paso de la caminata.
    """
    random_step = bernoulli.rvs(probabilidad, size=pasos)*2-1
    random_walk = random_step.cumsum()
    return random_walk

def graficar_caminata_aleatoria_bernoulli(random_walk):
    """
    Grafica una caminata aleatoria de Bernoulli.

    Args:
        random_walk (list): Una lista que representa la posición en cada paso de la caminata.
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(range(len(random_walk))), y=random_walk, mode='lines+markers'))
    fig.update_layout(title='Caminata Aleatoria de Bernoulli', xaxis_title='Pasos', yaxis_title='Posición')
    return fig





st.set_page_config(
    page_title="Caminata Aleatoria de Bernoulli",
    page_icon="🪙",
    layout="wide",  # Para que ocupe toda la pantalla
    initial_sidebar_state="expanded"
)


with st.sidebar:
    st.title("Caminata Aleatoria de Bernoulli")
    setps = st.slider("Pasos", 1, 100, 10)
    proba = st.slider("Probabilidad", 0.0, 1.0, 0.5)
    st.button("Generar Caminata")


st.title("Caminata Aleatoria de Bernoulli")
st.write("Una caminata aleatoria de Bernoulli es una secuencia de pasos aleatorios en la que cada paso tiene una probabilidad de éxito (p) y una probabilidad de fracaso (1-p).\
         En este caso, cada paso puede ser hacia arriba (1) o hacia abajo (-1).")
st.latex(r"X_i = \begin{cases} 1 & \text{con probabilidad } p \\ -1 & \text{con probabilidad } 1-p \end{cases}")
st.write("La caminata aleatoria de Bernoulli se define como:")
st.latex(r"X_n = \sum_{i=1}^n X_i")









caminata_aleatoria_bernoulli(10, 0.5)
    


