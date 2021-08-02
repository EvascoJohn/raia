from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
  return "Raia is Up!"

def run():
  app.run(host="0.0.0.0", port=443)

def keep_alive():
  t = Thread(target=run)
  t.start()