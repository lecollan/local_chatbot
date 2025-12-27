# Local Gemini/Gemma Chatbot

Este repositorio contiene un chatbot local que utiliza el modelo **Gemma** (versión abierta de Gemini Nano) ejecutado a través de **Ollama**.

## Requisitos Previos

1.  **Windows 10/11**.
2.  **Ollama**: Descárgalo e instálalo desde [ollama.com](https://ollama.com).
3.  **Python 3.8+**.
4.  **Modelo Gemma**: Asegúrate de tener el modelo descargado:
    ```bash
    ollama pull gemma:2b
    ```

## Instalación

1.  Clona este repositorio o descarga los archivos.
2.  Instala las dependencias de Python:
    ```bash
    pip install -r requirements.txt
    ```

## Ejecución

Simplemente haz doble clic en el archivo **`run_chatbot.bat`**.

O manualmente desde la terminal:
```bash
python -m streamlit run chatbot_app.py
```

## Estructura del Proyecto

- `chatbot_app.py`: El código fuente de la interfaz del chat (Streamlit).
- `run_chatbot.bat`: Script para iniciar el chat fácilmente en Windows.
- `requirements.txt`: Lista de librerías necesarias.
- `docs/`: Documentación del proceso de creación y planes de implementación.
