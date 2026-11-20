pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'kedarvhanaje/cloudcart'
        DOCKER_TAG = "build-${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'CloudCart source checkout'
                checkout scm
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
            }
        }

        stage('Docker Hub Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push "$DOCKER_IMAGE:$DOCKER_TAG"
                        docker logout
                    '''
                }
            }
        }

        stage('Kubernetes Deploy') {
            steps {
                sh '''
                    kubectl set image deployment/cloudcart \
                    cloudcart=$DOCKER_IMAGE:$DOCKER_TAG \
                    -n cloudcart

                    kubectl rollout status deployment/cloudcart -n cloudcart
                '''
            }
        }
    }

    post {
        always {
            sh 'docker image prune -f || true'
        }
        success {
            echo 'CloudCart CI/CD completed successfully!'
        }
        failure {
            echo 'CloudCart CI/CD failed. Check Console Output.'
        }
    }
}
