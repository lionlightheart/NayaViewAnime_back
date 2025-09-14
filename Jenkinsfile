pipeline {
    agent any

    // Trigger con push a GitHub
    triggers {
        githubPush()
    }

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
                    sh 'docker build -t nayaview_django .'
                }
            }
        }

        stage('Run Django container') {
            steps {
                script {
                    sh '''
                    # Si existe el contenedor, lo detenemos y eliminamos
                    if [ "$(docker ps -aq -f name=nayaview_django)" ]; then
                        docker stop nayaview_django
                        docker rm nayaview_django
                    fi

                    # Ejecutamos un nuevo contenedor con la última imagen
                    docker run -d \
                      --name nayaview_django \
                      --network django_red \
                      -p 8000:8000 \
                      nayaview_django
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

