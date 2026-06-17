from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
    <h1>🚀 DevOps CI/CD Pipeline Project</h1>
     <h3>👨‍💻 Developed By: Akshay</h3>
    <p>This application is deployed using Ubuntu, github, Nginx and Jenkins.</p>
    <p>Tools used:</p>
    <ul>
        <li>Ubuntu: used command to write app.py, jenkinsfile, requirements.txt</li>
        <li>github</li>
        <li>s</li>
        <li>g</li>
        <li>A</li>
    </ul>
    <h3>✅ Application is running successfully!</h3>
    """


app.run(host="0.0.0.0", port=5000)

