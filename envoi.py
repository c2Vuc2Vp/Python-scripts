#!/usr/bin/python
#-*-coding:utf-8-*-

#envoi

import nexmo

client = nexmo.Client(key="56395bd6", secret="ff16abef3eab6c8a")


client.send_message({
    'from': '58591558',
    'to': 58591558,
    'text': 'A text message sent using the Nexmo SMS API',
})

#reception
"""
from flask import Flask, request, jsonify
from pprint import pprint

app = Flask(__name__)

@app.route('/webhooks/inbound-sms', methods=['GET', 'POST'])
def delivery_receipt():
    if request.is_json:
        pprint(request.get_json())
    else:
        data = dict(request.form) or dict(request.args)
        pprint(data)

    return ('', 204)

app.run(port=3000)
"""
