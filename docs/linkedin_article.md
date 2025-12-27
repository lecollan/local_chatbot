# 🤖 Crea tu propio Chatbot Local con IA en minutos: Python + Ollama + Gemma

¿Te preocupa la privacidad de tus datos al usar IA? ¿O simplemente quieres tener un asistente inteligente que funcione 100% offline en tu portátil?

Recientemente he estado experimentando con la ejecución de **LLMs (Large Language Models)** en local y los resultados son sorprendentes. En este artículo, quiero compartir cómo puedes montar tu propio chatbot utilizando **Gemma** (el modelo abierto de Google), **Ollama** y **Streamlit**.

## ¿Por qué en Local?

Más allá del "hype", correr modelos en tu propia infraestructura (o portátil) tiene ventajas claras:
- **Privacidad Total**: Tus datos nunca salen de tu máquina. Ideal para consultoría o manejo de información sensible.
- **Coste Cero**: No hay facturas de API por token.
- **Latencia**: Respuesta inmediata sin depender de tu conexión a internet.

## El Stack Tecnológico

Para este proyecto he utilizado:
1.  **[Ollama](https://ollama.com)**: La herramienta definitiva para gestionar y ejecutar LLMs en local (Windows/Mac/Linux).
2.  **[Gemma:2b](https://blog.google/technology/developers/gemma-open-models/)**: La versión ligera del modelo de Google, optimizada para correr en hardware de consumo.
3.  **Python + Streamlit**: Para crear la interfaz de chat en menos de 50 líneas de código.

## Paso a Paso

### 1. Preparando el Motor: Ollama
Lo primero es instalar Ollama y descargar el modelo. Desde la terminal:

```bash
ollama pull gemma:2b
```

Este comando descarga el modelo (unos 1.7GB) y lo deja listo para usar.

### 2. El Código (Python)

La magia ocurre en un script de Python muy sencillo. Usamos la librería oficial de `ollama` para Python y `streamlit` para la UI.

Aquí tienes la estructura básica de `chatbot_app.py`:

```python
import streamlit as st
import ollama

st.title("🤖 Gemma Local Chatbot")

# Inicializar historial
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Mostrar mensajes anteriores
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Capturar input del usuario
if prompt := st.chat_input("Escribe tu mensaje..."):
    # Guardar y mostrar mensaje usuario
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generar respuesta
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Llamada a Ollama en modo stream
        stream = ollama.chat(
            model='gemma:2b',
            messages=st.session_state['messages'],
            stream=True,
        )
        
        for chunk in stream:
            content = chunk['message']['content']
            if content:
                full_response += content
                message_placeholder.markdown(full_response + "▌")
                
        message_placeholder.markdown(full_response)
    
    st.session_state["messages"].append({"role": "assistant", "content": full_response})
```

### 3. ¡A funcionar!

Con una simple línea en la terminal, tu chatbot cobra vida:

```bash
streamlit run chatbot_app.py
```

## Resultados

Usando el modelo `gemma:2b`, la velocidad es impresionante incluso en equipos sin una GPU dedicada potente. La capacidad de razonamiento es suficiente para tareas de asistencia, resumen y generación de texto creativa.

Este pequeño proyecto demuestra que la **IA Soberana** es accesible hoy para cualquier desarrollador. Ya no dependemos exclusivamente de las grandes APIs para integrar inteligencia en nuestras aplicaciones.

---
¿Has probado a correr modelos en local? ¿Qué uso le darías en tu entorno profesional? 👇

#IA #LocalLLM #Python #Ollama #Gemma #PrivacidadDeDatos #DevCommunity
