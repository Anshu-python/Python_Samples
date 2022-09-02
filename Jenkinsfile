pipeline {
  agent any
  stages {
    stage('Print') {
      parallel {
        stage('Print') {
          steps {
            echo '1st stage'
          }
        }

        stage('Parallel') {
          steps {
            echo 'parallel flow'
          }
        }

      }
    }

    stage('condition') {
      steps {
        waitUntil(initialRecurrencePeriod: 1)
      }
    }

    stage('end') {
      steps {
        echo 'end'
      }
    }

  }
}