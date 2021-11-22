pipeline { 
agent any
    stages {
        stage('Clone Git') {
            steps {
				checkout([
                    $class: 'GitSCM', 
                    branches: [[name: '*/master']], 
                    extensions: [], 
                    userRemoteConfigs: [[url: 'git@github.com:jaggu21/JenkinsDemo.git']]
                ])
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x execute.py"
                sh "./execute.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x test.py"
                sh "./test.py"
            }
        }
    } 
	post {
        always {
             echo 'Sending Email.'
            
             emailext body: "${currentBuild.currentResult}: Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n More info at: ${env.BUILD_URL}",
                 recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']],
                 subject: "Jenkins Build ${currentBuild.currentResult}: Job ${env.JOB_NAME}",
                 to: 'nandakishore.s.menon@gmail.com'
            
             echo 'Email Sent.'
         }
    }
}
