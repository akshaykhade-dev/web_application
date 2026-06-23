from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
    <h1>🚀 DevOps CI/CD Pipeline Project</h1>
     <h3>👨‍💻 Developed By: Akshay</h3>
    <ul>
    
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Project Architecture</title>
</head>
<body>

    <h1>DevOps End-to-End Project</h1>

    <h2>Project Objective</h2>
    <p>
        This project demonstrates a complete DevOps workflow including source code management,
        web application deployment, reverse proxy configuration, HTTPS setup, CI/CD automation,
        monitoring, and log management.
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
Flask Web Application
    |
    v
Nginx Reverse Proxy
    |
    v
HTTPS (Self-Signed SSL)
    |
    +--------------------+
    |                    |
    v                    v
Prometheus          Promtail
    |                    |
    v                    v
Grafana             Loki
    |
    v
Monitoring Dashboard
    </pre>

    <h2>Tools Used</h2>

    <h3>Git & GitHub</h3>
    <p>
        Used for version control and source code management. The application code is stored
        and maintained in a GitHub repository.
    </p>

    <h3>Flask</h3>
    <p>
        Flask is used as the Python web framework to run the application.
    </p>

    <h3>Hosts File Configuration</h3>
    <p>
        A local domain was configured using the system hosts file to access the application
        through a custom domain name.
    </p>

    <h3>Nginx Reverse Proxy</h3>
    <p>
        Nginx forwards incoming requests from the custom domain to the Flask application
        running on the local server.
    </p>

    <h3>SSL Certificate</h3>
    <p>
        A self-signed SSL certificate was configured to enable HTTPS communication.
    </p>

    <h3>Jenkins</h3>
    <p>
        Jenkins automates deployment using a CI/CD pipeline. It pulls the latest code
        from GitHub and redeploys the application automatically.
    </p>

    <h3>Prometheus</h3>
    <p>
        Prometheus collects server metrics such as CPU utilization, memory usage,
        disk usage, and network statistics.
    </p>

    <h3>Loki</h3>
    <p>
        Loki is used as a centralized log storage solution for application logs.
    </p>

    <h3>Promtail</h3>
    <p>
        Promtail collects log files from the server and forwards them to Loki.
    </p>

    <h3>Grafana</h3>
    <p>
        Grafana provides dashboards for monitoring system metrics and visualizing
        application logs collected by Prometheus and Loki.
    </p>

    <h2>Project Features</h2>

    <ul>
        <li>Version Control using Git and GitHub</li>
        <li>Local Domain Configuration</li>
        <li>Nginx Reverse Proxy Setup</li>
        <li>HTTPS using Self-Signed SSL Certificate</li>
        <li>Jenkins CI/CD Pipeline</li>
        <li>System Monitoring with Prometheus</li>
        <li>Centralized Logging with Loki and Promtail</li>
        <li>Visualization and Dashboards using Grafana</li>
    </ul>

</body>
</html>
    </ul>
    <h3>✅ Application is running successfully!</h3>
    """


app.run(host="0.0.0.0", port=5000)

