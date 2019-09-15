pipeline {
    agent none
    stages {
        stage('Build') {
            agent { docker { image 'maven:3-alpine'
                    } 
            }
            steps {
                checkout scm
                sh 'ls -l'
                echo 'Hello, Maven'
                sh "mvn --version"
            }
        }
        stage('Unit Test') {
            agent { docker { image 'python:3.7-slim'
                    } 
            }
            steps {
                sh 'python src/unit_test.py -v'
                sh 'ls -l '
            }
        }
        stage('Deploy') {
            agent { 
                    node {
                        label 'production'
                    } 
                }
            steps {
                echo 'Hello production'
                sh 'docker build -t flask_app:0.1 .'
                sh 'docker rm -f devops_flask_app ||  true'
                sh 'docker run -d --name devops_flask_app -p 3005:5000 flask_app:0.1'
            }
        }

    }
}