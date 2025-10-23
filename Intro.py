import streamlit as st
from PIL import Image
st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Aplicaciones con Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Detección de Objetos en Imágenes")
 image = Image.open('imagen1_col1.png')
 st.image(image, width=190)
 url = "https://isabelyolo.streamlit.app/"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader("Análisis de imágenes")
 image = Image.open('imagen2_col1.png')
 url = "https://visionisabelapp-bt9afjddxmus3nskd5c4bb.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Análisis de polaridad y subjetividad")
 image = Image.open('3_col1.png')
 st.image(image, width=200)
 url = "https://bbeipob42jp8alcurgsuie.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader(" Lector de Sensor MQTT")
 image = Image.open('4_col1.png')
 st.image(image, width=200)
 url = "https://recepmqttisabel-v7a4dmdsj48oeg4vck8wae.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader(" Explorador de Arquitectura Brutalista 🇬🇧 (Intro)")
 image = Image.open('5_col1.png')
 st.image(image, width=200)
 url = "https://intro-isabel-mctfjnlul2nxavcbmbuqgn.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("INTERFACES MULTIMODALES control por voz")
 image = Image.open('5_col1.png')
 st.image(image, width=200)
 url = "https://ctrlvoiceisabel-bsia3noomxkcyffrknkbcv.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")


with col2: 
 st.subheader("TRADUCTOR · AURA")
 image = Image.open('1_col2.png')
 st.image(image, width=200)
 url = "https://traductorisabel-uvkvhzxyowgzgtvtm8taln.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("Análisis de Datos")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 url = "https://asistpy-csv.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Reconocimiento de Imágenes")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 url = "https://gestosmachine.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")

 st.subheader("Reconocimiento óptico de Caracteres")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 url = "https://ocrisabel-ryfbpkgiqtz9nro5vq5znt.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")

 st.subheader("Canva inteligente")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 url = "https://histinfisabelgit-cwhyqj6ypdcqhzlw6it3p7.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")

 st.subheader("Generación Aumentada por Recuperación ")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 url = "https://chatisabelpdf-ieutr2vhlb4tmhnznvsrpq.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("TF-IDF Interactivo — Preguntas y Respuestas (Español)")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 url = "https://tdfespisabel-aawiceq9b3tyu8cxmsamtn.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Tablero para dibujo")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 url = "https://tab2git-fe2tebsswksrevwuaud8fr.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("MQTT Control")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 url = "https://sendcmqttisabel-9vbwhsystfshosy79muzr7.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")

 st.subheader("BridgeSpeak — Tu puente de idiomas")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 url = "https://ocr-audio-isabel-3cc87gyk7bcgbxnbvbjeg3.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")


 st.subheader("Tablero Inteligente")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 url = "https://drawrecogisabelgit-ntkewzqrr9kpzzkcubuhhl.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")

 st.subheader(" Analizador de Texto")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 url = "https://4mjf64a34dork5epmuo38o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")



