# Comments service
### System for adding comments
### Link - [comments-app-vovkdev.herokuapp.com/start_page/]([http://host/start_page](https://comments-app-vovkdev.herokuapp.com/start_page/))
![Screenshot from 2023-04-15 10-35-03](https://user-images.githubusercontent.com/104986485/232308608-0d0b0fee-4263-4092-9127-d101e3035c52.png)
![Screenshot from 2023-04-15 16-31-23](https://user-images.githubusercontent.com/104986485/232308637-ccc12c52-a614-4280-8cfd-055b7e0e31d7.png)
![Screenshot from 2023-04-15 10-35-40](https://user-images.githubusercontent.com/104986485/232308702-dc40d65a-c9d1-4338-9700-631287dd503d.png)
![Screenshot from 2023-04-15 16-32-28](https://user-images.githubusercontent.com/104986485/232308660-f2f6ccbe-d395-4f10-b53d-8c7842bd50d0.png)
___
## Content
 - [Technologies](#what-we-used)
 - [Desription](#what-we-do)
 - [Star Project](#how-to-start-project)
 - [Sources](#sources)
___
## What we used?
_Technologies used_: Djando, Recaptcha, Celery Worker, Pillow, Docker, Postgres SQL

## What we do?
In this service, you can compose blocks for writing comments. 
You can write an answer for each cometary in the block. 
You can also attach text files up to 100 kb and images. <br>
Comments can only be written by a registered user. Any user can create blocks with comments, 
all users can leave comments.Users have a personal account where you can upload an avatar or 
view information about the user.<br>
**Paths:**
- [http://host/start_page](http://host/start_page) - start page

**Feauters:**
- Answer on comments 
- Captha validation on create 
- Add txt, image files 
- Validate images format and text 
- Pagination
- Sorting system
- Image resizing on upload
- Regular expressions for text validation
- User cabinet with avatar
<br>
Database relationships:
![auth_group](https://user-images.githubusercontent.com/104986485/232308466-64e3ab0d-0aeb-408d-8266-9d74230a2ff2.png)

## How to start project?
1. Run `git clone {SSH-link from GitHub}` on your PC;
2. Create virtual environment `python -m venv venv` and run it `source venv/bin/activate`;
3. Run `pip install -r requirements.txt`;
4. Create '.env' file and write to it the enviroment variables:
	- SECRET_KEY (Fot example: 'django-insecure-5tj_b9&8y82i5lpeh1cc_3k^rgp4=!ti1wnu7x8!nop0@!281$')
    - DEBUG (False if deploy on the server);
    - POSTGRES_USER;
    - POSTGRES_PASSWORD;
    - POSTGRES_DB;
    - DB_HOST;
    - DB_PORT;
    - RECAPTCHA_PUBLIC_KEY;
    - RECAPTCHA_PRIVATE_KEY;
5. Run `python3 manage.py migrate`;
6. Create superuser `python3 manage.py createsuperuser`; 
7. Run application `python3 manage.py runserver`

## Sources
1. [Django REST framework official](https://www.django-rest-framework.org/)
2. [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)
