pipeline{
    agent any
    stages{
        stage('Checkout Source'){
            steps{
                    echo 'Source code checked out from GitHub'
            }
        }
        stage('Show Workspace'){
            steps{
                sh 'pwd'
                sh 'ls -la'
            }
        }
        stage('Build Docker Images'){
            steps{
                sh 'docker compose build'
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