Запуск api:

git clone https://github.com/n1kkj/polls.git
cd polls
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver

Запуск на docker:

sudo docker build . -t core
sudo docker run -d -p 8000:8080 core

Документация на Swagger:

http://localhost:8000/redoc/
http://localhost:8000/swagger/
