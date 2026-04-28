# Integración Jenkins con Slack

## Descripción del Proyecto
Sistema simple de cálculos en Python para demostrar la integración de Jenkins con Slack mediante notificaciones automatizadas.

## Estructura del Proyecto
```
Actividad/
├── app.py                  # Aplicación principal
├── test_app.py            # Tests unitarios
├── Jenkinsfile            # Pipeline exitoso
├── Jenkinsfile_error      # Pipeline con error simulado
└── README.md              # Este archivo
```

## Requisitos
- Python 3.x
- Jenkins instalado
- Cuenta de Slack
- Plugin Slack Notification en Jenkins

## Cómo ejecutar localmente

### Ejecutar la aplicación:
```bash
python app.py
```

### Ejecutar los tests:
```bash
python test_app.py
```

## Pipeline de Jenkins

El pipeline incluye las siguientes etapas:

1. **Inicio**: Notifica el inicio del pipeline
2. **Build**: Construye el proyecto
3. **Test**: Ejecuta pruebas unitarias
4. **Deploy**: Despliega la aplicación

## Notificaciones de Slack

El pipeline envía notificaciones en los siguientes casos:

- ✅ **Inicio del pipeline**: Color azul
- ✅ **Ejecución exitosa**: Color verde
- ❌ **Ejecución fallida**: Color rojo

Cada notificación incluye:
- Nombre del proyecto
- Número de build
- Fecha y hora
- Duración
- Estado del proceso
- Link a los detalles
