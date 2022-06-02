#pylint:disable=E0001
from requests import post
from rubika.client import Bot
import requests
import json

search ='متن'
bot = Bot('appname',auth='kljgniakxetdayrhziuwjejkbncmexbo')
target='c0BGk7v01e5cf64a51a042d06014ae44'

try:
    url = json.loads(requests.get('http://api.codebazan.ir/music/?type=search&query=' +search+ '&page=1').text)
    results =url['Result']
    for result in results:
        Titel=result['Title']
        Like=result['Like']
        View=result['View']
        Link=result['Music_128']
        Link_320=result['Music_320']
        Photo=result['Photo']
        shortlink=result['shortlink']
        bot.sendPhoto(target,Photo,caption=f"نام موزیک :\n {Titel} ")
        print ("send-photo")
        bot.sendDocument(target,Link)
except:
        Titel=result['Title']
        Like=result['Like']
        View=result['View']
        Link=result['Music_128']
        Link_320=result['Music_320']
        Photo=result['Photo']
        shortlink=result['shortlink']
        bot.sendPhoto(target,Photo,caption=f"name music : {Titel}\n Like : {Like} \n view : {View}\n link Download :\n\n 128: {Link} \n\n320 :{Link_320}\n\nshortlink: {shortlink} ")
        print ("send-photo-try")
