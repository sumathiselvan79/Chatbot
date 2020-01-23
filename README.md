# BOSSBot
A contextual Chatbot that gives you details about Bharat Operating System Solutions Linux

## Requirements
1. Python - TensorFlow, telepot
3. A Telegram account
4. MongoDB
5. MongoDB Atlas for Ccreating an online cluster for the database, MongoDB Compass for accessing the Database
6. Cloud services for hosting telepot server

## Testing
        python3 SocketServer.py
        #if you want test in the browser start SocketServer.py
 then see the  real time result  by sending messeges in  the index.html(responsive UI is added)
 - If you want to test out a version of this Bot, download telegram and search for DertsBot

## Features
This chatbot figures out the context from what you type in and chooses a reply from one of the replies that are pre-built. A system where all the chats will be recorded for further improving the Bot. 

## To Be Implemented
GUI for desktops

## How to use the code
1. Make context.json. This is your training data
2. Run Main.py. This will train your model using TensorFlow
3. Run Python terminal and import Bot.py and check if the responses are correct
4. Queries in the terminal should be of the form Bot.response('YOURQUESTIONS')
5. Run TelServer and open your terlegram app on your mobile device and search for @DertsBot
6. You can now use the bot for your queries
7. To access the cloud database you require MongoDB Compass Community Edition. Connect it to bossdb-w54dc.mongodb.net
8. Username - user, password - pass check the SRV Record box# BossBot
