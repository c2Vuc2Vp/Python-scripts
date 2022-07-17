#!/usr/bin/python
#-*-coding:utf-8-*-

from twilio.rest import TwilioRestClient

client = TwilioRestClient()

client.messages.create(from_="(225) 58591558",
			to = "(225) 58591558",
			body = "test")
