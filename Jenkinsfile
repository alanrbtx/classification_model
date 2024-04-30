pipeline {
    agent {
        docker { image 'alan1402/bigdata:0.1' }
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