################# Accuracy : 94.05

#1
python3 Main.py
--data folder.

#2. Installation
pymongo
telepot
tflearn - numpy
tensorflow
nltk - punkt
pip install nltk



#3. run 
python3 TelServer.py
#on local
python3 SocketServer.py
--text format
http://127.0.0.1:3126/?query=download boss&id=1

###mongo shell
mongo "mongodb://bossdb-shard-00-00-w54dc.mongodb.net:27017,bossdb-shard-00-01-w54dc.mongodb.net:27017,bossdb-shard-00-02-w54dc.mongodb.net:27017/test?replicaSet=BOSSDB-shard-0" --ssl --authenticationDatabase admin --username admin --password pass


#mongodb in new dbpath
####### sudo mongod --repair
mongod --dbpath /var/lib/mongodbnew/ 

#mongodb Qry
db.database.find({response:'Hey! Anything I can help with?'}, {})

###TO DO ###
1.  work with telegram and create bot
1.1 make sure whts is permAdmin and admin in TelServer.py
2. work with training part - addd new qury and check.
3. few question (boss vs eduboss, boss etc) throws error like, 
[
 raise exception.TelegramError(description, error_code, data)
telepot.exception.TelegramError: ('Bad Request: message text is empty', 400, {'description': 'Bad Request: message text is empty', 'error_code': 400, 'ok': False})
]
4.bot name : cdac_bot user name faqAI
5.how to chnage the BOT userName (faqAI)
6.  how to add unique id to this bot.?
6.1.all the question from the same user must be stroed with assigned unique id. 
7.how to get the user name and mobile number from the telegram
8. trainig from mongodb instead of JSON.? is it possible.?
9.integration with exsiting website. 
10. why not with whatsapp.?

