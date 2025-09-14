pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/lionlightheart/NayaViewAnime_back.git'
      }
    }

    stage('Build Docker') {
      steps {
        sh 'docker build -t nayaview_django .'
      }
    }

    stage('Run Migrations') {
      steps {
        sh 'docker run --rm --network django_red nayaview_django python manage.py migrate'
      }
    }

    stage('Run Tests') {
      steps {
        sh 'docker run --rm --network django_red nayaview_django python manage.py test'
      }
    }

  }
}