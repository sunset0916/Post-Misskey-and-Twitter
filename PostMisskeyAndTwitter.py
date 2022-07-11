import unicodedata
from misskey import Misskey
import tweepy
import sys

CONSUMER_KEY = '[TWITTER_API_CONSUMER_KEY]'
CONSUMER_SECRET = '[TWITTER_API_CONSUMER_KEY_SECRET]'
ACCESS_TOKEN = '[TWITTER_API_ACCESS_TOKEN]'
ACCESS_TOKEN_SECRET = '[TWITTER_API_ACCESS_TOKEN_SECRET]'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

TOKEN='[MISSKEY_API_TOKEN]'
msk = Misskey('[MISSKEY_INSTANCE_URL]', i=TOKEN)

input = sys.argv

def getTextLengthForTwitter(message):
    count = 0
    for c in message:
        if unicodedata.east_asian_width(c) == 'Na':
            count += 1
        else:
            count += 2
    return count

if len(input) != 1:
    if input[1] == '-m':
        if len(input) != 2:
            message = input[2]
            for i in range(3,len(input)):
                message = message + '\n' + input[i]
            msk.notes_create(text=message)
        else:
            print('【悲報】投稿が入力されていません！')
    elif input[1] == '-t':
        if len(input) != 2:
            message = input[2]
            for i in range(3,len(input)):
                message = message + '\n' + input[i]
            if(getTextLengthForTwitter(message) <= 140):
                api.update_status(message)
            else:
                print('【悲報】Twitterの文字数制限を超えています！')
        else:
            print('【悲報】投稿が入力されていません！')
    else:
        message = input[1]
        for i in range(2,len(input)):
            message = message + '\n' + input[i]
        if(getTextLengthForTwitter(message) <= 140):
                api.update_status(message)
        else:
            print('【悲報】Twitterの文字数制限を超えています！')
        msk.notes_create(text=message)
else:
    print('【悲報】引数が入力されていません！')
