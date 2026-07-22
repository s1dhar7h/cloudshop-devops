pipeline{
    agent any
    stages{
        stage('Checkout Source'){
            steps{
                    echo 'Source code checked out from GitHub'
            }
        }
        stage('Build Docker Images'){
            steps{
                sh 'docker compose build'
            }
        }
        stage('Stop Existing Containers') {
            steps {
                sh 'docker compose down'
            }
        }
        stage('Start Containers') {
            steps {
                sh 'docker compose up -d'
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