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
            sh ' docker build --network host -t $IMAGE_NAME . '
            }
        }
        stage('Remove old container') {
          steps { 
            sh ' docker rm -f web-application || true '
            }
        }

        stage('Run New Container') {
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
