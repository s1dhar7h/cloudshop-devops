pipeline{
    agent any
    stages{
        stage('Checkout Source'){
            steps{
                    echo 'Source code checked out from GitHub'
            }
        }
    
    stage('Run Tests') {
        steps {
            sh '''
                docker build -t cloudshop-test -f ci/Dockerfile.test .

                docker run --rm cloudshop-test -m pytest user-service/tests
                docker run --rm cloudshop-test -m pytest product-service/tests
                docker run --rm cloudshop-test -m pytest order-service/tests
                docker run --rm cloudshop-test -m pytest notification-service/tests
            '''
        }
    }

        stage('Build Docker Images'){
            steps{
                sh 'docker compose build'
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
            docker push s1dhar7h/cloudshop-product-service:latest
            docker push s1dhar7h/cloudshop-order-service:latest
            docker push s1dhar7h/cloudshop-notification-service:latest
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