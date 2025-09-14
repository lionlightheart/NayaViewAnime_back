pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git(
                    url: 'https://github.com/lionlightheart/NayaViewAnime_back.git',
                    branch: 'main',
                    credentialsId: 'github-token'
                )
            }
        }

        stage('Build Docker') {
            steps {
                script {
                    // Build la imagen
                    sh 'docker build -t nayaview_django .'
                }
            }
        }

        stage('Run Django container') {
            steps {
                script {
                    // Si el contenedor no existe, crear y levantar
                    sh '''
                    if [ ! "$(docker ps -aq -f name=nayaview_django)" ]; then
                        docker run -d \
                          --name nayaview_django \
                          --network django_red \
                          -p 8000:8000 \
                          nayaview_django
                    else
                        docker start nayaview_django
                    fi
                    '''
                }
            }
        }

        stage('Run Migrations') {
            steps {
                sh 'docker exec nayaview_django python manage.py migrate'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker exec nayaview_django python manage.py test'
            }
        }
    }
}
