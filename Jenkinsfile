pipeline {
    agent any

    environment {
        FRONTEND_DIR = 'frontend'  // React frontend directory
        BACKEND_DIR = '.'    // Python backend directory
        DOCKER_IMAGE_FRONTEND = 'my-react-app'
        DOCKER_IMAGE_BACKEND = 'my-python-api-app'
        DOCKER_IMAGE_MYSQL = 'my-mysql-db'
        MYSQL_CONTAINER = 'mysql_db'
        PATH = "/usr/local/bin:${env.PATH}"
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }

        stage('Test Docker') {
            steps {
                script {
                    echo 'Checking Docker version and running containers...'
                    sh 'docker --version'  // Get Docker version
                    sh 'docker ps'         // List running containers
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    echo 'Building Docker image for the frontend...'
                    sh 'docker build -t ${DOCKER_IMAGE_FRONTEND} -f Dockerfile.frontend .'

                    echo 'Building Docker image for the backend app...'
                    sh 'docker build -t ${DOCKER_IMAGE_BACKEND} -f Dockerfile.backend .'

                    echo 'Building Docker image for MySQL...'
                    sh 'docker build -t ${DOCKER_IMAGE_MYSQL} -f Dockerfile.mysql .'
                }
            }
        }

        stage('Run Containers with Docker Compose') {
            steps {
                script {
                    echo 'Starting containers using Docker Compose...'
                    sh 'docker-compose up -d --build'

                    echo 'Waiting for MySQL to be ready...'
                    sh 'docker exec ${MYSQL_CONTAINER} mysqladmin ping -h mysql --silent || exit 1'
                }
            }
        }

        stage('Test Services') {
            parallel {
                stage('Test Frontend') {
                    steps {
                        script {
                            echo 'Running frontend tests...'
                            sh 'curl --fail http://localhost:3000 || exit 1'
                        }
                    }
                }

                stage('Test Backend') {
                    steps {
                        script {
                            echo 'Running backend tests...'
                            sh 'curl --fail http://localhost:5000 || exit 1'
                            sh 'curl --fail http://localhost:5000/signup || exit 1'
                            sh 'curl --fail http://localhost:5000/login || exit 1'
                        }
                    }
                }

                stage('Test MySQL') {
                    steps {
                        script {
                            echo 'Testing MySQL connection...'
                            sh 'docker exec ${MYSQL_CONTAINER} mysql -uroot -pnandhu01 -e "SHOW DATABASES;" || exit 1'
                        }
                    }
                }
            }
        }

        stage('Clean Up') {
            steps {
                script {
                    echo 'Cleaning up the containers...'
                    sh 'docker-compose down'
                }
            }
        }
    }

    post {
        always {
            echo 'Pruning Docker system...'
            sh 'docker system prune -af'
        }
    }
}
