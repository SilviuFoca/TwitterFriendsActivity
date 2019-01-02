from twython import Twython, TwythonError
import configparser
import datetime
import time

config = configparser.RawConfigParser()
config.read('settings.conf')

autor = config.get('Conectare', 'Copyright')
username = config.get('User', 'Username')
app_key = config.get('User', 'AppKey')
app_secret = config.get('User', 'AppSecret')
oauth_token = config.get('User', 'OAuthToken')
oauth_token_secret = config.get('User', 'OAuthTokenSecret')
sleeptime = int(config.get('User', 'SleepTime'))
verbose = int(config.get('User', 'Verbose'))

if autor != "silviu@foca.ro":
    sys.exit("Copyright??? Bye, bye!!!")

twitter = Twython(app_key,app_secret,oauth_token,oauth_token_secret)
azi = datetime.datetime.now().strftime("%Y-%m-%d")
ieri = datetime.datetime.now() - datetime.timedelta(days=1)
ieri.strftime("%Y-%m-%d")
datestamp = datetime.datetime.now().strftime("%Y-%m-%d")
raport = "raport-friends-"+username+"-"+str(azi)+".html"
tweetsdata = {}
index = 1

next_cursor = -1
save = open(raport,'w', encoding="utf-8")
save.write("<!DOCTYPE html> <html lang=\"en\"> <head> <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>")
while(next_cursor):
    get_friends = twitter.get_friends_list(screen_name=username,count=200,cursor=next_cursor)
    for friend in get_friends["users"]:
        location = friend["location"]
        location = location.replace("'"," ")
        nume = friend["name"]
        nume = nume.replace("'"," ")
        try:
            time.sleep(sleeptime)
            get_tweets = twitter.get_user_timeline(screen_name=friend['screen_name'],count=1, include_rts=True)
            for x in get_tweets:
                x['text'] = Twython.html_for_tweet(x)
                if (verbose > 0):
                    print(str(index)+" - <a href=\"https://twitter.com/"+x['user']['screen_name']+"\" target=_blank>"+x['user']['name']+"</a> : "+x['text']+" - "+ x['created_at'])
                save.write(str(index)+" - <a href=\"https://twitter.com/"+x['user']['screen_name']+"\" target=_blank>"+x['user']['name']+"</a> : "+x['text']+" - "+ x['created_at']+"<br/><br/> ")
                index = index + 1
        except TwythonError as e:
            print (e)
            continue
        next_cursor = get_friends["next_cursor"]
save.close()
