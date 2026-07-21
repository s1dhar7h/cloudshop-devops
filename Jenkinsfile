pipeline{
    agent any
    stages{
        stage('Hello World'){
            steps{
                    echo 'Hello World'
            }
        }
        stage('Workspace'){
            steps{
                sh 'pwd'
                sh 'ls -la'
            }
        }
        stage('Docker Check'){
            steps{
                sh 'docker version'
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