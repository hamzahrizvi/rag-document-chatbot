@echo off
call C:\Users\hrizvi\AppData\Local\anaconda3\Scripts\activate.bat rag-env
start "" cmd /k "ollama run mistral-nemo"
timeout /t 5 >nul
streamlit run app.py
pause