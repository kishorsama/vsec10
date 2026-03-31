pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build & Test') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python -m unittest discover' 
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t your-dockerhub-username/ai-model-api:latest .'
            }
        }
    }
}