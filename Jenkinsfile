pipeline {
    agent any

    environment {
        MYSQL_CONTAINER = "mysql_db1"
        MYSQL_ROOT_PASSWORD = "nandhu01"
        MYSQL_DATABASE = "test_db"
        MYSQL_USER = "root"
        MYSQL_PASSWORD = "nandhu01"
    }

    stages {
        // Install Python dependencies inside a virtual environment
        stage('Install Dependencies') {
            steps {
                script {
                    // Create a virtual environment and activate it
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate && pip install -r requirements.txt'  // Activate venv and install dependencies
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
                        -p 3308:3306 \
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
                    sh '. venv/bin/activate && python3 test_mysql.py'  // Run python script using the virtual environment
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    sh 'docker stop ${MYSQL_CONTAINER} && docker rm ${MYSQL_CONTAINER}'
                    sh 'deactivate'  // Deactivate virtual environment after use
                }
            }
        }
    }
}
