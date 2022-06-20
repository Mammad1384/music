from requests import get
from re import findall
import os
import glob
from rubika.client import Bot
import requests
from rubika.tools import Tools
from rubika.encryption import encryption
from gtts import gTTS
from mutagen.mp3 import MP3
import json
from json import load , dump
import time
from time import sleep
import random
import urllib
import io
from random import choice
from PIL import Image


#شناسه اکانت
bot = Bot("AppName", auth="nmhcmsxejupcisastngawlwlegrmnhig")
#......
#شناسه گروه
target = "g0BkKci09901fda5b96cf940a401b650"
#......
#شناسه کانال
channell = "c0vxMX07181d7a79a55618b859ff2c57"

def hasAds(msg):
	links = ["http://","https://",".ir",".com",".org",".net",".me"]
	for i in links:
		if i in msg:
			return True
			
def hasInsult(msg):
	swData = [False,None]
	for i in open("dontReadMe.txt").read().split("\n"):
		if i in msg:
			swData = [True, i]
			break
		else: continue
	return swData

	
# static variable
answered, sleeped, retries = [], False, {}
alerts, blacklist, stars = [] , [] , []

while True:
	# time.sleep(15)
	try:
		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		min_id = bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]

		while True:
			try:
				messages = bot.getMessages(target,min_id)
				break
			except:
				continue

		for msg in messages:
			try:
				if msg["type"]=="Text" and not msg.get("message_id") in answered:
					if not sleeped:
						if hasAds(msg.get("text")) and not msg.get("author_object_guid") in admins :
							guid = msg.get("author_object_guid")
							user = bot.getUserInfo(guid)["data"]["user"]["username"]
							bot.deleteMessages(target, [msg.get("message_id")])
							alert(guid,user,True)
							
						elif msg.get("text") == "خاموش" or msg.get("text") == "\stop":
							try:
								if msg.get("author_object_guid") in admins:
								   sleeped = True
								   bot.sendMessage(target, "✅ ربات اکنون خاموش است", message_id=msg.get("message_id"))
								else:
									bot.sendMessage(target, '❌ اجازه دسترسی به شما داده نشد',message_id=msg.get("message_id"))
							except:
								print('error off bot')
							
						elif msg.get("text").startswith("سین زن روشن"):
							try:
								bot.sendMessage(target, "🤖در پیام بعدی لینک گروه مورد نظر را ثبت نمائید🤖\nمثال:\n\nجوین گپ\nhttps://rubika.ir/joinc/BEDJEHGJ0LXSIPACCXGCQCBIJBZESKWA")
							except:
								print("error ersal start1")

						elif msg.get("text").startswith("جوین گپ"):
							try:
								matnsingzf = open("banerlinkdoneSINZAN.txt","w",encoding='utf-8').write(str(msg.get("text").strip("جوین گروه")))
								matnsingz = open("banerlinkdoneSINZAN.txt").read().split("\n")
								bot.sendMessage(target,  "✅ با موفقیت لینک گروه مورد نظر ثبت شد")
								bot.sendMessage(target,  "\n🤖بنر خود را برای سین زنی در پیام بعدی ثبت نمائید🤖\n\nمثال رو پیامی که می خواهید سین زده شود ریپ بزنید و بگویید [سین بزن]\n")
							except:
								print("error sabt_link-sinzan")

						elif msg.get("text").startswith("سین بزن"):
							while True:
								time.sleep(70)
								sleep(5)
								matntabb = list(matnsingz)
								randomli = choice(matntabb)
								writelin = open("TARGET_SINZAN.txt","w",encoding='utf-8').write(str(randomli))
								tabgligh = open("TARGET_SINZAN.txt","r",encoding='utf-8').read()
								tabeligh = bot.joinGroup(tabgligh)
								tabrligh = tabeligh['data']['group']['group_guid']
								bot.forwardMessages(target,[msg.get("reply_to_message_id")],tabrligh)
								
								print("err Joined member Answer")
							
				else:
					if "forwarded_from" in msg.keys() and bot.getMessagesInfo(target, [msg.get("message_id")])[0]["forwarded_from"]["type_from"] == "Channel" and not msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [msg.get("message_id")])
						guid = msg.get("author_object_guid")
						user = bot.getUserInfo(guid)["data"]["user"]["username"]
						bot.deleteMessages(target, [msg.get("message_id")])
						alert(guid,user,True)
						
					else:
						if msg.get("text") == "روشن" or msg.get("text") == "\start":
							try:
								if msg.get("author_object_guid") in admins:
								   sleeped = False
								   bot.sendMessage(target, "ربا‌ت با موفقیت روشن شد!", message_id=msg.get("message_id"))
								else:
									bot.sendMessage(target, '❌ اجازه دسترسی به شما داده نشد',message_id=msg.get("message_id"))
							except:
								print('error one bot')
					
					continue
			except:
				continue

			answered.append(msg.get("message_id"))
			print("[" + msg.get("message_id")+ "] >>> " + msg.get("text") + "\n")

	except KeyboardInterrupt:
		exit()

	except Exception as e:
		if type(e) in list(retries.keys()):
			if retries[type(e)] < 3:
				retries[type(e)] += 1
				continue
			else:
				retries.pop(type(e))
		else:
			retries[type(e)] = 1
			continue