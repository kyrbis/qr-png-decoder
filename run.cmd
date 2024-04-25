
IF NOT EXIST venv (
python -V
python -m venv venv
.\venv\Scripts\python -m pip install --upgrade pip
.\venv\Scripts\python -m pip install -r requirements.txt
)

.\venv\Scripts\python -V

.\venv\Scripts\python main.py

timeout 8
exit /B 0
