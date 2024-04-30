pipeline {
    agent {
        docker { image 'python:3.9.6' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'node --version'
            }
        }
        stage('Docker Build') {
            agent any
            steps {
                sh 'docker build -t alan1402/bigdata:0.1 .'
            }
        }
    }
}