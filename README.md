# API Cargar Archivos

![DjangoRestFramework](https://img.stackshare.io/service/1630/New_Project__67_.png "Django Rest Framework")
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

API REST que permite a los usuarios cargar un archivo CSV desde su computador a la nube, y leer cada una de las filas para hacer un control de versionamiento ante un cambio.

**Metodos**
  - POST : A traves del endpoint se recibe un archivo se guarda en servidor y se guardan filas en BD
  - GET : Visualiza Los archivos y filas que han sido guardadas en la BD



## Tecnologias Usadas

Para la construcción de esta API se usaron los siguientes lenguajes y librerías:

![python](https://img.shields.io/badge/3.8-Python-FFD43B?style=for-the-badge&logo=python&logoColor=white) ![Django](https://img.shields.io/badge/3.1.4-Django-092E20?style=for-the-badge&logo=Django&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/3.1.4-PostgreSQL-008bb9?style=for-the-badge&logo=Postgresql&logoColor=white)

* [Python](https://www.python.org/) - Lenguaje de programación multiparadigma, que soporta 
    * Programación Orientada a Objetos.
    * Programación imperativa.
    * Programación funcional.

    con este lenguaje creamos nuestro entorno virtual de desarrollo e instalamos los paquetes necesario

* [Django](https://www.djangoproject.com/) - framework de desarrollo web de código abierto, escrito en Python y que maneja el MVT
    * A traves de su librería Django Rest Framework se utilizo su estructura para realizar la carga del archivo y mostrar la información en Formato Json


* [PostgreSQL](https://www.postgresql.org/) - Gestor de BD relacional Orientada a Objetos y de codigo abierto.



## Installation

Debes tener instalado python versión 3.8 o superior, Virtualenv, pip. Para verificar utilizamos los siguientes comandos:
- Windows
    ```  sh
    C:\> python --version
    C:\> python --pip
    C:\> virtualenv --version
    ```
- Linux
    ```  sh
    $ python3 --version
    $ pip3 --version
    $ virtualenv --version
    ```
En caso de no tenerlo instalado puedes ir a la referencia del lengua para instalar [Python.org](https://www.python.org/).

Crear una carpeta vacia en la ubicación deseada e ingresar a esta, posterior ejecutamos los siguientes comandos para crear el entorno virtual en Python
```sh
$ virtualenv venv --python=python38
```
Activar el entorno virtual e intalar los paquetes necesarios para correr la API
```sh
$ source venv/bin/activate
$ pip install -r requirements.txt
```
[Instalación de PostgreSQL](https://todopostgresql.com/tipos-de-instalaciones-de-postgresql/) (ver referencia de instalación para Windows y Linux)

Clonar el repositorio 
```sh
$ git clone https://github.com/JhonJBautistaB/apiFileCharger.git
```

Ingresar a la consola o a PgAdmin (Como lo prefiera) y crear una Base de Datons vacia con el nombre "fileCharger", ejecutar el siguiente comando

```sh
$ CREATE DATABASE fileCharger
```
Realizar las migración de la base de datos utilizando los siguientes comandos

```sh
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```
