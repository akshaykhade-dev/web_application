pipeline {
    agent any
          
              environment {
            	IMAGE_NAME = "akshay1092003/web_application"
                          }
    stages {
        stage('pull code') {
          steps {
                checkout scm
            }
        }
        stage('Docker Build') {
          steps {  
            sh ' docker build -t --network host $IMAGE_NAME . '
            }
        }
        stage('Docker Run container') {
          steps {
               sh ' docker run --network host --name web-application $IMAGE_NAME ' 
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
