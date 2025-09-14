pipeline {
    agent any
    environment {
        VENV_DIR = "venv"
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/lionlightheart/NayaViewAnime_back.git'
            }
        }
        stage('Setup Python') {
            steps {
                sh 'python3 -m venv $VENV_DIR'
                sh '. $VENV_DIR/bin/activate && pip install --upgrade pip'
                sh '. $VENV_DIR/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Migrate Database') {
            steps {
                sh '. $VENV_DIR/bin/activate && python manage.py migrate'
            }
        }
        stage('Run Tests') {
            steps {
                sh '. $VENV_DIR/bin/activate && python manage.py test'
            }
        }
        stage('Build Complete') {
            steps {
                echo 'Pipeline finished successfully!'
            }
        }
    }
}
