# API социальной сети [Yatube](https://github.com/iliakoll/project-Yatube.git)

### Технологии проекта:
```
Python 3.8.9
Django 2.2.16
DjangoRestFramework 3.12.4
Djoser 2.1.0
Django-filter 22.1
```
### Как запустить проект:

* Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/iliakoll/api_final_yatube.git
```

```
cd api_final_yatube
```

* Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

* Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

* Выполнить миграции:

```
python3 manage.py migrate
```

* Запустить проект:

```
python3 manage.py runserver
```

* Запросы к API доступны через стандарт OpenAPI типа ReDoc:


  #### [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)
