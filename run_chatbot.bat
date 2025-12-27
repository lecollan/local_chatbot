@echo off
echo Starting Chatbot...
echo Ensure 'ollama pull gemma:2b' has finished!
python -m streamlit run chatbot_app.py
pause
