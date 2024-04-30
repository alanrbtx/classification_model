pipeline {
    agent {
        docker { image 'python:3.9.6' }
    }
    stages {
        stage('Docker Build') {
            agent any
            steps {
                sh 'cat Dockerfile'
                sh 'docker build -t alan1402/bigdata:0.1 .'
            }
        }
    }
}