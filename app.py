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
    
<h2>Project Overview</h2>
<p>
This project demonstrates a complete DevOps workflow using Git, GitHub,
Docker, Jenkins, Nginx, Grafana, Loki, Promtail, and Prometheus.
The application is deployed and managed using CI/CD automation and monitoring tools.
</p>

<h2>Tools and Technologies Used</h2>

<h3>Git & GitHub</h3>
<p>
Git is used for version control and source code management.
GitHub is used as the central repository to store and manage application code.
</p>

<h3>Docker</h3>
<p>
Docker is used to create a containerized environment for the application,
ensuring consistent deployment across different systems.
</p>

<h3>Jenkins</h3>
<p>
Jenkins is used to implement a CI/CD pipeline. Whenever code changes are pushed
to GitHub, Jenkins automatically pulls the latest code and deploys the application.
</p>

<h3>Nginx</h3>
<p>
Nginx is configured as a reverse proxy server and routes incoming requests
to the Flask application.
</p>

<h3>SSL Certificate</h3>
<p>
A self-signed SSL certificate is configured to enable secure HTTPS communication.
</p>

<h3>Grafana</h3>
<p>
Grafana is used to visualize application and server metrics through dashboards.
</p>

<h3>Loki</h3>
<p>
Loki is used for centralized log storage and log aggregation.
</p>

<h3>Promtail</h3>
<p>
Promtail collects application logs and sends them to Loki for storage and analysis.
</p>

<h3>Prometheus</h3>
<p>
Prometheus collects system metrics such as CPU usage, memory utilization,
disk usage, and network statistics.
</p>

<h2>Project Workflow</h2>

<pre>
Developer
    |
    v
GitHub Repository
    |
    v
Jenkins CI/CD Pipeline
    |
    v
Application Deployment
    |
    v
Docker Container
    |
    v
Nginx Reverse Proxy
    |
    +------> Prometheus (Metrics)
    |
    +------> Promtail -> Loki (Logs)
    |
    v
Grafana Dashboards
</pre>
    </ul>
    <h3>✅ Application is running successfully!</h3>
    """


app.run(host="0.0.0.0", port=5000)

