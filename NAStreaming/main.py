#Define the imports
import twitch
import logging
import normalMode
import violenceMode
import time
import datetime
import keypresser

keypresser = keypresser.keyPresser()
violence = violenceMode.violenceMode()
normal = normalMode.normalMode()
twitch = twitch.Twitch()
logging.basicConfig(filename='commands.log', level=logging.INFO,format='%(asctime)s - %(message)s', datefmt='%Y/%m/%d %I:%M:%S')
gameStart = True
gameMode = 'normal'
normalMode = 'normal'
democracyMode = 'democracy'
violenceMode = 'violence'
startTime = datetime.datetime.now()
waitTime = 3
cacheCommand = []
lastRecvTime = startTime
newMessages = ''


#Enter your twitch username and oauth-key below, and the app connects to twitch with the details.
#Your oauth-key can be generated at http://twitchapps.com/tmi/
usr = 'easychien';
key = 'oauth:fj8k048zl94xc5l0pn0cvbzwhhscdd'
twitch.twitchConnect(usr, key);



#The main loop
while gameStart:
    #Check for new mesasages
    newMessages = twitch.twitchRecieveMessages()

    #initialize democracy commands
    longestCommand = ['',0]

    if not newMessages:
        #No new messages...
        continue
    else:
        for message in newMessages:
            
            #Wuhu we got a message. Let's extract some details from it

            msg = message['message'].lower()
            username = message['username'].lower()
            elapseTime = datetime.datetime.now() - startTime
            logging.info(username + ': ' + msg + " - GameMode: " + gameMode + " - Elapsed time: " + time.strftime("%H:%M:%S",time.gmtime(elapseTime.seconds)))
            # print(username + ': ' + msg)
            if msg == 'normal' and username == usr:
                gameMode = normalMode
                # print('Now normalMode')
                twitch.sendMessage('Now Normal Mode')
                break
            elif msg == 'democracy' and username == usr:
                gameMode = democracyMode
                # print('Now democracyMode')
                twitch.sendMessage('Now Democracy Mode')
                break
            elif msg == 'violence' and username == usr:
                gameMode = violenceMode
                # print('Now violenceMode')
                twitch.sendMessage('Now Violence Mode')
                break
            elif msg == 'random' and username == usr:
                gameMode = randomMode
                # print('Now randomMode')
                twitch.sendMessage('Now Random Mode')
                break

            if msg == 'quit':
                gameStart = False
                twitch.sendMessage('Game has stopped,please restart the program')
                break

            if gameMode == 'normal':
                cacheCommand += normal.count(msg)
                
            elif gameMode == 'violence':
                temp = violence.countMostCommand(msg)
                if temp[1] > longestCommand[1]:
                    longestCommand[0]=temp[0]
                    longestCommand[1]=temp[1]
            elif gameMode == 'democracy':
                cacheCommand += normal.count(msg)
                pass

        if gameMode == violenceMode:
            cacheCommand = longestCommand
            print(cacheCommand)

        if (datetime.datetime.now() - lastRecvTime) >= datetime.timedelta(seconds=waitTime) and cacheCommand:
            lastRecvTime = datetime.datetime.now()
            execCommand = cacheCommand
            if (gameMode == democracyMode):
                listCommand = list(set(cacheCommand))
                twitch.sendMessage('Vote for command')
                twitch.sendMessage(listCommand)
                cacheCommand = []
                democracytime = datetime.datetime.now()
                while (datetime.datetime.now() - democracytime) <= datetime.timedelta(seconds=waitTime):
                    votes = twitch.twitchRecieveMessages()
                    for message in votes:
                        msg = message['message'].lower()
                        cacheCommand += normal.count(msg)
                countVote = {}
                print(cacheCommand)
                for k in listCommand:
                    countVote[k] = 0
                for i in cacheCommand:
                    if (i in countVote):
                        countVote[i] += 1
                for j in countVote.keys():
                    if countVote[j] == max(countVote.keys(),key= lambda x:countVote[x]):
                        execCommand = j
            logging.info('Execute command: '+execCommand)
            for i in execCommand:
                keypresser.pressKey(i)

            cacheCommand = []

        


    

def initExecCommand():
    execCommand = {'up': 0,
                'down': 0,
               'left': 0,
               'right': 0,
                 'a': 0,
                 'b': 0,
              'select': 0,
               'start': 0}
    pass




            