import json
from django.http import JsonResponse
from registration.models import user ,shopkeeper



def shop_category(request):
	if request.method == "POST":
		print(request.body)
		data= json.loads(request.body)
		category=data['shopname']
		message=list(shopkeeper.objects.filter(category=category).values('shopname','id'))
		print(message)
	return JsonResponse(message,safe=False)	
