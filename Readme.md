Req:

- league modeli yaratılacak
- lig sıralaması haftalık olarak json dosyasında tutulacak
- team modeli yaratılacak
- takımların logoları file sistemde tutulacak path'ler databasede tutulacak
- get_lig(hafta, sezon) : lig sıralaması json olarak döndürülecek

bu kadar.

# mongodb kullanımı eklenmesi

\$pip install django-rest-framework-mongoengine

- add INSTALLED_APP section in settings.py

- install djongo for connect mongo db
  \$pip install djongo
  -add fallowing lines into DATABASES section in settings.py

-- DATABASES = {
-- 'default': {
-- 'ENGINE': 'djongo',
-- 'NAME': 'bezkoder_db',
-- 'HOST': '127.0.0.1',
-- 'PORT': 27017,
-- }
-- }

- multiple database settings see:https://programmersought.com/article/81771060541/

# mongodb with djongo rest

- refs : https://bezkoder.com/django-mongodb-crud-rest-framework/
  https://github.com/radzhome/djongo-count-bug
  https://github.com/nesdis/djongo
  https://nesdis.github.io/djongo/api/

# file upload

- refs : https://www.techiediaries.com/django-rest-image-file-upload-tutorial/
  https://stackoverflow.com/questions/1729051/django-upload-to-outside-of-media-root

# data analize :

refs :
https://www.tff.org
https://www.mackolik.com
https://www.flashscore.com

# mongo dump - restore

mongodump --host localhost -d football --port 27017 --out c:/mongoDump

mongorestore --host localhost -d football --port 27017 ./data/db

mongorestore --host localhost -d football --port 27017 ./data/backup


# mongo query notes

- updateMany aggregation
'''
    db.football_match.updateMany(     
      {"guest.name":'Çaykur Rizespor'},      
      {$set: {"guest.name": 'Rizespor'}} 
    )
'''
- find
'''
    db.football_match.find({"host.name":'Çaykur Rizespor'})
'''