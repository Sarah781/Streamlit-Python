import streamlit as st
import matplotlib.pyplot as plt
import random

st.set_page_config(page_title='Streamlit', page_icon="👋")


st.title('Streamlit'.upper())

# Função do chatbot
def chatbot(resposta):
    respostas = {
        "Olá": ["Olá!", "Oi! Como posso te ajudar?", "Oi, tudo bem?"],
        "Como você está?": ["Estou bem, obrigado por perguntar!", "Estou ótimo, obrigado!", "Estou bem, e você?"],
        "Qual é o seu nome?": ["Meu nome é ChatBot.", "Pode me chamar de ChatBot.", "Eu sou o ChatBot."],
        "Qual é a sua idade?": ["Eu sou um programa de computador, não tenho idade.", "Idade é apenas um conceito humano para mim.", "Não tenho uma idade física."],
        "Obrigado": ["De nada!", "Por nada!", "Estou aqui para ajudar!"],
        "Tchau": ["Até logo!", "Tchau! Espero te ver em breve.", "Até mais!"],
        "": ["Desculpe, não entendi. Poderia repetir?", "Não entendi o que você disse. Pode reformular?", "Não entendi. Pode ser mais claro?"],
    }
    if resposta in respostas:
        return random.choice(respostas[resposta])
    else:
        return random.choice(respostas[""])

nav = st.sidebar.radio('Navegação', ['Home', 'Sobre', 'Utilidades'])
st.markdown('---')


if nav == 'Home':
    st.subheader('Bem vindo a home')
    st.write('Escolha uma opção no menu lateral para navegar pelo aplicativo')



elif nav == 'Sobre':
    st.write('Streamlit é uma biblioteca de código aberto para Python que torna a criação de aplicativos da web interativos e visualizações de dados em Python mais fácil e rápida')
    # Adicionando o chatbot
    st.sidebar.header('ChatBot')
    st.sidebar.subheader('Converse com o ChatBot')
    entrada_usuario = st.sidebar.text_input("Você: ")

    if st.sidebar.button("Enviar"):
        if entrada_usuario:
            resposta = chatbot(entrada_usuario)
            st.sidebar.text_area("ChatBot:", value=resposta, height=100)
        else:
            st.sidebar.warning("Por favor, digite algo para conversar.")
    

else:
    st.write('Funcionalidades')
    #grafico de linha
    st.text('Gráfico de linha')
    st.line_chart([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    #grafico de area
    st.text('Gráfico de área')
    st.area_chart([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    #grafico de barra
    st.text('Gráfico de barras')
    st.bar_chart([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    #mapa usando lat long
    st.text('Mapa')
    st.map(latitude=0, longitude=0, zoom=0)

    #grafico de pizza
    st.text('Gráfico de pizza')
    labels = 'Relógio', 'Bolsa', 'Mochila', 'Cinto'
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0.1, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=30)
    ax1.axis('equal') 

    st.pyplot(fig1)

    #grafico de dispersão
    st.text('Gráfico de dispersão')
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 3, 4, 2], 'o') 
    st.pyplot(fig)

    #grafico de histograma
    st.text('Gráfico de histograma')
    fig, ax = plt.subplots()
    ax.hist([1, 2, 1], bins=[0, 1, 2, 3, 5])
    st.pyplot(fig)





   


