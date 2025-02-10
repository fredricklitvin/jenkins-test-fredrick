pipeline {
    agent { label 'master' }
    stages {
        stage('build playbook') {
            steps {
                script {
                    sh ' echo " building the playbook" '
                    ls ' tree ' 
                    sh ' ls '
                    sh ' pwd '
                    sh ' ansible-playbook build_playbook.yml' 
                }
            }
        }
     stage('build container') {
        steps {
            agent { label 'slave' }
            script {
                sh ' echo " build the container " '
                sh ' sudo docker-compose build '
                sh ' sudo docker-compose up -d '
            }
        }
    }     

    stage('test') {
        steps {
            agent { label 'slave' }
            script {
                sh ' echo " test " '
                sh ' curl  http://127.0.0.1:5000 '
                sh ' curl  http://127.0.0.1:9090 '
            }
        }
    }

        stage('deploy') {
            steps {
                agent { label 'slave' }
                script {
                    sh ' echo "deploy" '
                    sh ' aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 992382545251.dkr.ecr.us-east-1.amazonaws.com '               
                    sh ' docker build -t fredrick-repository . '
                    sh ' docker tag fredrick-repository:latest 992382545251.dkr.ecr.us-east-1.amazonaws.com/fredrick-repository:latest '
                    sh ' docker push 992382545251.dkr.ecr.us-east-1.amazonaws.com/fredrick-repository:latest '
                
                
                
                }
            }
        }
    }

        post { 
        always { 
            sh ' echo " removing docker " '
           sh ' docker rm -f web '
        }
    }  
}
