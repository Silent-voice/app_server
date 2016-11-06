# -*- coding:UTF-8 -*-
import demjson
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from app_http_method import Register, Login, create_room, join_room, get_record, updata_user_info, get_room_info, get_room_list


@csrf_exempt
def register(request):
	if request.method == 'POST':
		json = request.POST['data']
		data = demjson.decode(json)

		user_name = data['user_name']
		nick_name = data['nick_name']
		password = data['password']
		intro = data['introduce']

		_type = Register.addUser(user_name, nick_name, password, intro)
		data = [{'type' : _type}]
		json = demjson.encode(data)
		return HttpResponse(json)
	else:
		data = [{'type': 2}]
		json = demjson.encode(data)
		return HttpResponse(json)

@csrf_exempt
def login(request):
	if request.method == 'POST':
		json = request.POST['data']
		data = demjson.decode(json)
		name = data['user_name']
		password = data['password']

		_id = Login.checkUser(name, password)

		if _id == -1:
			data = [{'type':1,'id':-1}]
		elif _id == -2:
			data = [{'type': 2, 'id': -1}]
		else :
			data = [{'type': 0, 'id': _id}]

		json = demjson.encode(data)
		return HttpResponse(json)
	else:
		return HttpResponse('not POST message')

@csrf_exempt
def createRoom(request):
	json = request.POST['data']
	data = demjson.decode(json)

	user_id = data['user_id']
	room_name = data['room_name']

	result = create_room.create(user_id, room_name)

	if result == -1:
		data={'result':1,'number':result}
	else:
		data={'result': 0, 'number': result}
	json = demjson.encode(data)
	return HttpResponse(json)

@csrf_exempt
def joinRoom(request):
	json = request.POST['data']
	data = demjson.decode(json)

	room_id = data['room_id']
	user_id = data['user_id']

	result = join_room.join(user_id, room_id)
	data = {'result':result}
	json = demjson.encode(data)
	return HttpResponse(json)

#查询战绩
@csrf_exempt
def getRecord(request):
	json = request.POST['data']
	data = demjson.decode(json)

	user_id = data['user_id']
	message = get_record.get(user_id)
	json = demjson.encode(message)
	return HttpResponse(json)

#更新用户信息
@csrf_exempt
def updataInfo(request):
	json = request.POST['data']
	data = demjson.decode(json)

	user_id = data['user_id']
	type = data['type']
	message = data['data']

	result = updata_user_info.updata(user_id, type, message)
	json = demjson.encode(result)
	return HttpResponse(json)

#获取房间列表
@csrf_exempt
def getRoomList(request):

	message = get_room_list.get()
	json = demjson.encode(message)
	return HttpResponse(json)

#获取指定房间房间
@csrf_exempt
def getRoomInfo(request):
	json = request.POST['data']
	data = demjson.decode(json)

	room_id = data['room_id']
	message = get_room_info.get(room_id)
	json = demjson.encode(message)
	return HttpResponse(json)


















