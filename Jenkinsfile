pipeline{
    agent any
    environment{
        IMAGE_TAG = "${BUILD_NUMBER}"
    }
    stages{
        stage('Checkout Source'){
            steps{
                    echo 'Source code checked out from GitHub'
            }
        }
    
    stage('Run Unit Tests') {
        when {
            anyOf {
                changeset "user-service/**"
                changeset "product-service/**"
                changeset "order-service/**"
                changeset "notification-service/**"
                changeset "ci/**"
                changeset "Jenkinsfile"
            }
        }
        steps {
            sh '''
                docker build -t cloudshop-test -f ci/Dockerfile.test .

                docker run --rm -w /app/user-service cloudshop-test python -m pytest tests
                docker run --rm -w /app/product-service cloudshop-test python -m pytest tests
                docker run --rm -w /app/order-service cloudshop-test python -m pytest tests
                docker run --rm -w /app/notification-service cloudshop-test python -m pytest tests
            '''
        }
    }

        stage('Build Docker Images'){
            steps{
                sh '''
                    docker compose build
                    docker tag s1dhar7h/cloudshop-user-service:latest s1dhar7h/cloudshop-user-service:${IMAGE_TAG}
                    docker tag s1dhar7h/cloudshop-product-service:latest s1dhar7h/cloudshop-product-service:${IMAGE_TAG}
                    docker tag s1dhar7h/cloudshop-order-service:latest s1dhar7h/cloudshop-order-service:${IMAGE_TAG}
                    docker tag s1dhar7h/cloudshop-notification-service:latest s1dhar7h/cloudshop-notification-service:${IMAGE_TAG}
                '''
            }
        }
        stage('Login to Docker Hub'){
            steps{
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    '''
                    }
            }
        }
        stage('Push Images') {
            steps {
                sh '''
                    docker push s1dhar7h/cloudshop-user-service:latest
                    docker push s1dhar7h/cloudshop-user-service:${IMAGE_TAG}
                    docker push s1dhar7h/cloudshop-product-service:latest
                    docker push s1dhar7h/cloudshop-product-service:${IMAGE_TAG}
                    docker push s1dhar7h/cloudshop-order-service:latest
                    docker push s1dhar7h/cloudshop-order-service:${IMAGE_TAG}
                    docker push s1dhar7h/cloudshop-notification-service:latest
                    docker push s1dhar7h/cloudshop-notification-service:${IMAGE_TAG}
                '''
            }
        }
        stage('Logout Docker Hub') {
            steps {
                sh 'docker logout'
            }
        }

    }
    post{
        always{
            echo 'Pipeline Finished'
        }
        success{
            echo 'Build Successfull'
        }
        failure{
            echo 'Build Failed'
        }
    }
}