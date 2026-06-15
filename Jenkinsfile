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
                pip install python3

                python3 -m venv venv

                . venv/bin/activate
                   pip install -r requirements.txt
                python app.py
               '''
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
     }

}
