pipeline {
          agent any

stages {
     stage('pull code')
      steps {
          checkout scm
        }


     stage ('create envirnoment')
      steps {
        sh 'source venv/bin/activate'
        } 
          
     stage ('run command')
      steps {
        sh 'python app.py'
        }
      
      post {
        success {
             echo 'Pipeline Success'
          }
         failure {
            echo 'Pipeline Failed'
             }
}
}
}
