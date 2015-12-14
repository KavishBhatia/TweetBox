#!/usr/bin/env python
import sys
from twython import Twython

from Tkinter import *

def tweet(t):
	tweetStr = t

	apiKey = '' #your account's api key
	apiSecret = '' #your account's api secret
	accessToken = '' #access token
	accessTokenSecret = '' #access token secret

	api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
	auth = api.get_authentication_tokens()
	api.update_status(status=tweetStr)
	
	print "Tweeted: " + tweetStr

#---------------------------------------------------------
root = Tk()
nameLabel = Label(root, text="Your Tweet(140 char)")
ent = Entry(root, bd=5)
root.geometry("300x150+600+300")
def getName():
    #print ent.get()
    a = ent.get()
    t = a
    tweet(t)	
    root.destroy()	
submit = Button(root, text ="Submit", command = getName)

nameLabel.pack()
ent.pack()

submit.pack(side = BOTTOM) 
root.mainloop()

#-------------------------------------------------------


