from django.shortcuts import render
from django.http import HttpResponse
from .models import FeedBack
# Create your views here.


def index(request):
    if request.method == 'POST':
        experience = request.POST['experience']
        comprehensiveness = request.POST['comprehensiveness']
        price_rate=request.POST['price_rate']
        order_delivery = request.POST['order_delivery']
        customer_support = request.POST['customer_support']
        recommend = request.POST['recommend']
        expectations=request.POST['expectations']
        user = FeedBack.objects.create(experience=experience,comprehensiveness=comprehensiveness,price_rate=price_rate, order_delivery=order_delivery, customer_support=customer_support, recommend=recommend, expectations=expectations)
        user.save()
        return render(request, 'thankyou.html')
    return render(request, 'index.html')