from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!<h1>'


app.run(ssl_context=('cert.pem','key_unlocked.pem'), port=5000)

