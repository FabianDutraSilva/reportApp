## ReportApp: el software de reporte de incidentes de TALAR
Aplicación web dedicada al registro de incidentes de producción de la planta industrial TALAR.
Se trata de una web con backend basado en Python mediante el framework Django y frontend basado en la librería bootstrap.

### Alta de equipos
Funcionalidad sólo disponible para el superadministrador del sistema, para dar de alta los equipos de la planta.
### Reporte de incidentes
Funcionalidad disponible para todos los usuarios registrados.
Los usuarios pueden ver todos los incidentes registrados.
Los usuarios pueden editar y eliminar únicamente los incidentes creados por ellos.
El superadmin puede ver, editar y eliminar todos los registros.

## Instalar requierements
Ejecutar el comando
```
pip install -r requirements.txt
```