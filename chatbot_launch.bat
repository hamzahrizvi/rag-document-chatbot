@echo off
call C:\Users\hrizvi\AppData\Local\anaconda3\Scripts\activate.bat rag-env

:: Start Ollama service (if not already running)
start "" ollama serve

timeout /t 3 >nul

streamlit run app.py

pause