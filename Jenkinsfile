pipeline {
    agent {
        docker { image 'node:20.11.1-alpine3.19' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'node --version'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t alan1402/bigdata:0.1 .'
                sh 'node --version'
            }
        }
        
        
    }
}