<<<<<<< HEAD

=======
from django.shortcuts import render
>>>>>>> d77c8f17a2ae35f3f7df9eab3215b105e2dbcfe1
import json
from django.http import JsonResponse
from .models import user ,shopkeeper

# Create your views here.
<<<<<<< HEAD
#signup for user or customer
=======
>>>>>>> d77c8f17a2ae35f3f7df9eab3215b105e2dbcfe1
def signup(request):
	if request.method =="POST":
		print(request.body)
		data= json.loads(request.body)
		username=data['email']

		mobile_nom=data['mobile_no']
		unique_email=user.objects.filter(email=username , mobile_no= mobile_nom).exists()
		if(unique_email):
			message ="This user is already registered"
		else:
			user.objects.create(**data)
			message="Registered Sucessfully"
<<<<<<< HEAD
	return JsonResponse(message,safe=False) 


#signup for shopkeeper
=======
	return JsonResponse(message,safe=False)  


>>>>>>> d77c8f17a2ae35f3f7df9eab3215b105e2dbcfe1
def shop_signup(request):
	if request.method =="POST":
		print(request.body)
		data= json.loads(request.body)
		username=data['email']
		mobile_nom=data['mobile_no']
		unique_email=shopkeeper.objects.filter(email=username , mobile_no= mobile_nom).exists()
		if(unique_email):
			message ="This user is already registered"
		else:
			shopkeeper.objects.create(**data)
			message="Registered Sucessfully"
<<<<<<< HEAD
	return JsonResponse(message,safe=False) 


#login for user or customer 
=======
	return JsonResponse(message,safe=False)  


>>>>>>> d77c8f17a2ae35f3f7df9eab3215b105e2dbcfe1
def login(request):
	if request.method == "POST":
		print(request.body)
		data= json.loads(request.body)
		username=data['email']
		password=data['password']
		bool_filter=user.objects.filter(email=username,password=password).exists()  
		print(bool_filter)
		if (bool_filter):
			message=list(user.objects.filter(email=username).values('name','email','mobile_no','id','address'))
		else:
			message="invalid credentials"	
	return JsonResponse(message,safe=False)

<<<<<<< HEAD

#login for shopkeeper
=======
>>>>>>> d77c8f17a2ae35f3f7df9eab3215b105e2dbcfe1
def shop_login(request):
	if request.method == "POST":
		print(request.body)
		data= json.loads(request.body)
		username=data['email']
		password=data['password']
		bool_filter=shopkeeper.objects.filter(email=username,password=password).exists()  
		print(bool_filter)
		if (bool_filter):
			message=list(shopkeeper.objects.filter(email=username).values('name','email','mobile_no','id','address'))
		else:
			message="invalid credentials"	
	return JsonResponse(message,safe=False)

<<<<<<< HEAD

#address for user or customer
def update_user(request):
	if request.method == "POST":
		print(request.body)
		data= json.loads(request.body)
		Id=data['id']
		address=data['address']
		latitude=data['latitude']
		longitude=data['longitude']
		user.objects.filter(id=Id).update(address=address,latitude=latitude,longitude=longitude)
		message="Success"
	return JsonResponse(message,safe=False)	
=======
>>>>>>> d77c8f17a2ae35f3f7df9eab3215b105e2dbcfe1
