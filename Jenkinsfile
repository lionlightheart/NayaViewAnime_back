pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git(url: 'https://github.com/lionlightheart/NayaViewAnime_back.git', branch: 'main')
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