from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>
            <p>This is my 1st project</p>
            <h2>All done</h2>'


app.run(host="0.0.0.0", port=5000)

