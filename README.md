## Запуск api:
```bash
git clone https://github.com/n1kkj/polls.git
cd polls
pip install -r requirements.txt
docker-compose up -d
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```
```bash
python3 manage.py runserver
```
## Запуск на docker:
```bash
sudo docker build . -t core
sudo docker run -d -p 8000:8080 core
```
## Документация api на Swagger:
http://localhost:8000/swagger/
