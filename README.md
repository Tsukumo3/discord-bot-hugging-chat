# Discord-Bot-Hugging-Chat

## 環境

- windows
- python 3.12

## 環境構築

```sh
py -3.12 -m venv venv
.\venv\Scripts\Activate.ps1
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```

## サーバー起動

dev

```sh
python app/main.py
```

production (windows では fcntl が未対応のため動かない render で動かす)

```sh
gunicorn -w -b 0.0.0.0:8080 app/main:app
```
