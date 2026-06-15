pipeline {
    agent any

    stages {
        stage('pull code') {
            steps {
                checkout scm
            }
        }

        stage('Execute Application') {
          steps {
            sh ''' 
                source venv/bin/activate
            
                python app.py
               '''
        }
      }
   }
}

post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline execution failed.'
        }

