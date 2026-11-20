pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'CloudCart source checkout'
                checkout scm
            }
        }

        stage('Environment Check') {
            steps {
                sh 'git --version'
                sh 'kubectl version --client'
            }
        }

        stage('Kubernetes Verification') {
            steps {
                sh 'kubectl get pods -n cloudcart'
                sh 'kubectl get deployments -n cloudcart'
                sh 'kubectl get services -n cloudcart'
            }
        }

        stage('Complete') {
            steps {
                echo 'CloudCart CI pipeline completed successfully!'
            }
        }
    }
}
