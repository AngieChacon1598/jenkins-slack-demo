pipeline {
    agent any
    
    environment {
        PROJECT_NAME = 'Sistema de Gestion de Tareas'
    }
    
    stages {
        stage('Inicio') {
            steps {
                script {
                    slackSend(
                        channel: '#notificaciones-dev',
                        color: '#439FE0',
                        message: """
*Pipeline Iniciado*
Proyecto: ${PROJECT_NAME}
Build: #${BUILD_NUMBER}
Fecha: ${new Date().format('yyyy-MM-dd HH:mm:ss')}
Iniciado por: Jenkins
                        """.stripIndent()
                    )
                }
                echo 'Pipeline iniciado correctamente'
            }
        }
        
        stage('Build') {
            steps {
                echo 'Construyendo el proyecto...'
                script {
                    bat 'python --version'
                    bat 'echo Instalando dependencias...'
                }
                echo 'Build completado'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Ejecutando pruebas unitarias...'
                script {
                    bat 'python test_app.py'
                }
                echo 'Tests completados exitosamente'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Desplegando aplicacion...'
                script {
                    sleep 2
                }
                echo 'Deploy completado'
            }
        }
    }
    
    post {
        success {
            script {
                slackSend(
                    channel: '#notificaciones-dev',
                    color: 'good',
                    message: """
*Build Exitoso*
Proyecto: ${PROJECT_NAME}
Build: #${BUILD_NUMBER}
Duracion: ${currentBuild.durationString.replace(' and counting', '')}
Fecha: ${new Date().format('yyyy-MM-dd HH:mm:ss')}
Estado: SUCCESS
Ver detalles: ${BUILD_URL}
                    """.stripIndent()
                )
            }
            echo 'Pipeline completado exitosamente'
        }
        
        failure {
            script {
                slackSend(
                    channel: '#notificaciones-dev',
                    color: 'danger',
                    message: """
*Build Fallido*
Proyecto: ${PROJECT_NAME}
Build: #${BUILD_NUMBER}
Duracion: ${currentBuild.durationString.replace(' and counting', '')}
Fecha: ${new Date().format('yyyy-MM-dd HH:mm:ss')}
Estado: FAILURE
Ver logs: ${BUILD_URL}console
@channel Por favor revisar
                    """.stripIndent()
                )
            }
            echo 'Pipeline fallo'
        }
    }
}
