pipeline {
    agent {
        '/Applications/Docker.app/Contents/Resources/bin/docker' { image 'node:20.11.1-alpine3.19' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'node --version'
            }
        }
    }
}