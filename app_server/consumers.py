# -*- coding:UTF-8 -*-
from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group
import demjson
from channels.sessions import channel_session

from app_websocket_method import process_request
import time
#message.reply_channel.send(chunk)  用来唯一返回这个客户端
#message.reply_channel  可能是某个客户端通道的对象
#一个管道大概会持续30s


#这里有个问题是ws_message函数在ws_connect函数执行前就执行了？？？
# @channel_session
# def ws_message(message):
#     #送给全组人
#     #print message.content['text']
#     #Group("chat-%s" % message.channel_session['room']).send({
#     #    "text": message.content['text'],
#     #})
#     data = {'text':message.content['text']}
#     print data
#     time.sleep(1)
#     message.reply_channel.send(data)
#     # time.sleep(1)
#     # str = message.content['text']
#     # str = str + '+1s'
#     # data = {'text': str}
#     # message.reply_channel.send(data)


@channel_session
def ws_message(message):

    json = message.content['text']
    data = demjson.decode(json)
    #确认消息只需记录一下，不用返回
    if data['type'] == 0:
        process_request.process(json)
    else:
        message.reply_channel.send(demjson.encode({'type': '0','request_id':data['request_id']}))
        process_request.process(message,data)



@channel_session
def ws_connect(message):
    print message.content['path']
    room = message.content['path'].strip("/")
    message.channel_session['room'] = room
    Group("chat-%s" % room).add(message.reply_channel)
    #message.reply_channel.send('connect sucess')


@channel_session
def ws_disconnect(message):
    print 'disconnect'
    #print message.channel_session['room']
    #Group("chat-%s" % message.channel_session['room']).discard(message.reply_channel)
