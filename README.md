<p align="center">
    Trabajo Práctico Integrador - TADP - UP
    <br>
    2C - 2022
    <br>
</p>

# :pencil: Table of Contents
- [Acerca De](#about)
- [Levantar Proyecto](#run_project)
- [Herramientas Utilizadas](#built_using)
- [Autores](#authors)
- [Reconocimientos](#acknowledgement)

# :information_source: Acerca De <a name = "about"></a>
- Repositorio que contiene el trabajo práctico de la materia Técnicas Avanzadas de Programación de la Universidad de Palermo.

# :wrench: Levantar Proyecto <a name = "run_project"></a>

## Server
1. Ver "Instalar paquetes de requirements.txt" en este mismo archivo.
2. Levantar una terminal (cmd, powershell, etc.) en modo administrador
3. Navegar hasta nuestra carpeta de servidor y correr los siguientes comandos:
```
tadp-venv\Scripts\activate
cd tadp_api
./manage.py runserver
```
4. Navegar a alguna de las rutas definidas en nuestro urls.py (Ej: http://127.0.0.1:8000/api/v1/questions/)

## Crear o Cambiar Password de Usuario Admin Django
1. Levantar una terminal (cmd, powershell, etc.) en modo administrador
2. Navegar hasta nuestra carpeta de servidor y correr los siguientes comandos:
```
tadp-venv\Scripts\activate
cd tadp_api
```
3. 
```
./manage.py migrate
```
4. 
```
./manage.py createsuperuser
```
- Recomendamos utilizar:
    - User: admin 
    - Pass: test1234

# :hammer: Herramientas Utilizadas <a name = "built_using"></a>

## Herramientas
Recomendamos utilizar [chocolatey](https://community.chocolatey.org/) para instalar estos paquetes:
- [vscode](https://community.chocolatey.org/packages/vscode)
- [Python3](https://community.chocolatey.org/packages/python3/3.10.8) -> v3.10.8
- [nodejs-lts](https://community.chocolatey.org/packages/nodejs-lts) -> v16.18.0
- [postgresql](https://community.chocolatey.org/packages/postgresql14) -> v14.5.1
```
--params '/Password:test1234'
```
- [pgadmin4](https://community.chocolatey.org/packages/pgadmin4) -> v6.13

## Paquetes npm
Recomendamos utilizar la versión de npm que viene incluído en la versión de nodejs LTS (v16.18.0) para instalar los siguientes paquetes:
- [@angular/cli](https://www.npmjs.com/package/@angular/cli) -> v13-lts (tag)
```
npm install -g @angular/cli@v13-lts
```
- [typescript](https://www.npmjs.com/package/typescript) -> v4.8.4
```
npm install -g typescript@4.8.4
```
- [sass](https://www.npmjs.com/package/sass) -> v1.55.0
```
npm install -g sass@1.55.0
```
- El resto de los paquetes utilizados se encuentran en el archivo package.json y pueden ser instalados localmente al proyecto con el comando:
```
npm install
```

## Paquetes pip
Recomendamos utilizar la versión de pip que viene incluído en la versión de python3 (v3.10.8) para instalar los siguientes paquetes:
- [djangorestframework](https://pypi.org/project/djangorestframework/)
```
pip install -Iv djangorestframework==3.14.0
```
- [django-cors-headers](https://pypi.org/project/django-cors-headers/)
```
pip install -Iv django-cors-headers==3.13.0
```
- [requests](https://pypi.org/project/requests/)
```
pip install -Iv requests==2.28.1
```
- [SQLAlchemy](https://pypi.org/project/SQLAlchemy/)
```
pip install -Iv SQLAlchemy==1.4.42
```
- [pytest](https://pypi.org/project/pytest/)
```
pip install -Iv pytest==7.1.3
```
- [coverage](https://pypi.org/project/coverage/)
```
pip install -Iv coverage==6.5.0
```
- [drf-yasg](https://pypi.org/project/drf-yasg/)
```
pip install -Iv drf-yasg==1.21.4
```

### pip comandos
- Instalar paquetes de requirements.txt:
```
python -m venv tadp-venv
python -m pip install -r requirements.txt
```
- Extraer paquetes instalados a requirements.txt:
```
python -m pip freeze > requirements.txt
```

## Postgresql
- Default Port: 5432

### Login
- Admin: postgres 
- Admin Pass: test1234
```
psql -U postgres
```

### pgAdmin4
- Master Password: test1234

# :speech_balloon: Autores <a name = "authors"></a>
- [@mily96](https://github.com/mily96)
- [@andresbiso](https://github.com/andresbiso)

# :tada: Reconocimientos <a name = "acknowledgement"></a>
- https://github.com/github/gitignore
- https://gist.github.com/rxaviers/7360908 -> github emojis
