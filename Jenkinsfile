pipeline {
    agent any

    environment {
        MYSQL_CONTAINER = "mysql_db"
        MYSQL_ROOT_PASSWORD = "nandhu01"
        MYSQL_DATABASE = "test_db"
        MYSQL_USER = "root"
        MYSQL_PASSWORD = "nandhu01"
    }

    stages {
        // Install Python dependencies
        stage('Install Dependencies') {
            steps {
                script {
                    // Install the necessary packages, including mysql-connector-python
                    sh 'pip install -r requirements.txt'  // Or manually install: pip install mysql-connector-python
                }
            }
        }

        stage('Start MySQL Container') {
            steps {
                script {
                    sh '''
                    docker run -d --name ${MYSQL_CONTAINER} \
                        -e MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD} \
                        -e MYSQL_DATABASE=${MYSQL_DATABASE} \
                        -e MYSQL_USER=${MYSQL_USER} \
                        -e MYSQL_PASSWORD=${MYSQL_PASSWORD} \
                        -p 3306:3306 \
                        mysql:latest

                    echo "Waiting for MySQL to be ready..."
                    sleep 20
                    '''
                }
            }
        }

        stage('Run Python Code') {
            steps {
                script {
                    sh 'python3 test_mysql.py'
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    sh 'docker stop ${MYSQL_CONTAINER} && docker rm ${MYSQL_CONTAINER}'
                }
            }
        }
    }
}
