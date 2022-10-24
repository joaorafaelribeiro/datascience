from flask import Flask
from redis import Redis

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)