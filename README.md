# Registro y listado de autos con Flask

Aplicación web Python con inicio de sesión de demostración, formularios para agregar autos y plantillas para consultar el listado.

## Requisitos

Python 3 y dependencias de requirements.txt. La clave de sesión se toma de FLASK_SECRET_KEY; en desarrollo se genera una clave temporal si no se configura.

## Ejecución

Los comandos parten de la raíz del repositorio, salvo donde se indica otra terminal.

```bash
python -m pip install -r requirements.txt
python app.py
```

## Recorrido de demostración

Abrir http://127.0.0.1:5000. Entrar al flujo de opciones, registrar un auto y revisar el listado. app.py define las rutas y poo.py el modelo utilizado.

## Organización

Carpetas de la entrega: [`templates/`](templates/).

## Alcance y límites

La autenticación y las colecciones son de demostración. Para conservar sesiones entre reinicios, definir FLASK_SECRET_KEY en el entorno. No usar el servidor de desarrollo como despliegue público.

## Contexto y licencia

Trabajo académico o de aprendizaje conservado en el portafolio de [Enner Mendizabal](https://github.com/Ennero). Los créditos de los trabajos en grupo se conservan en sus entregas y manuales.

Consultar [LICENSE](LICENSE) para la licencia de la raíz. Las dependencias y los componentes con avisos o licencias propios conservan sus condiciones.
