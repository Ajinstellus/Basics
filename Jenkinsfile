pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Ajinstellus/Basics.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh """
                    cd python
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                    cd python
                    . venv/bin/activate
                    pytest || true
                """
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t ajin0809/python-app:latest python/'
            }
        }

        stage('Docker Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials',
                                                  usernameVariable: 'USER',
                                                  passwordVariable: 'PASS')]) {
                    sh """
                        echo $PASS | docker login -u $USER --password-stdin
                        docker push ajin0809/python-app:latest
                    """
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent(['ec2-key']) {
                    sh """
                        ssh -o StrictHostKeyChecking=no ubuntu@52.53.118.179 \
                        'docker pull ajin0809/python-app:latest &&
                        docker stop py || true &&
                        docker rm py || true &&
                        docker run -d --name py -p 80:80 ajin0809/python-app:latest'
                    """
                }
            }
        }
    }
}
