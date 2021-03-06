import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

--------------------------------------------------




----------------------------------------------------------


class listener(StreamListener):

    def on_data(self, data):
        dictTweet = json.loads(data)
        try:

            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print("SAVED" + str(doc) + "=>" + str(data))
        except:
            print("Already exists")
            pass
        return True

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())


-----------------------------------------------------

# ('http://115.146.93.184:5984/')
server = couchdb.Server('http://admin:admin@localhost:5984/')
try:
    db = server.create('juegosolimpicos_ciudades')
except:
    db = server['juegosolimpicos_ciudades']

---------------------------------------------------------

#twitterStream.filter(locations=[-90.9242,13.7963,-90.7396,14.0464], track=['juegos olimpicos','Tokio'])
#twitterStream.filter(locations=[-78.455723,-0.220076,-78.394749,-0.183272], track=['juegos olimpicos','Tokio'])
twitterStream.filter(locations=[8.7387, 45.3143, 9.4319, 45.6558], track=[
                     'juegos olimpicos', 'Tokio'])
