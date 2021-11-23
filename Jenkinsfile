pipeline { 
agent any
    stages {
        stage('Clone Git') {
            steps {
				git 'https://github.com/Nandakishore-Menon/JenkinsDemo.git'
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
            
             emailext body: "Job ${env.JOB_NAME} build ${env.BUILD_NUMBER} finished with STATUS: ${currentBuild.currentResult}: \n Details at: ${env.BUILD_URL}",
                 recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']],
                 subject: "Jenkins Build ${currentBuild.currentResult}",
                 to: 'nandakishore.s.menon@gmail.com'
            
             echo 'Email Sent.'
         }
    }
}
