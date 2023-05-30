from django.shortcuts import render, redirect
from .models import Food, Consume

# Create your views here.

def index(request):
    if request.method == 'POST':
        food_consumed = request.POST['food_consumed']
        consumed = Food.objects.get(name=food_consumed)
        # getting the user object who is currently logged in
        user = request.user
        consume = Consume(consumed_user=user, food_consumed_by_user=consumed)
        consume.save()
        foods = Food.objects.all()
        
    else:
        foods = Food.objects.all()
        
    consumed_food = Consume.objects.filter(consumed_user=request.user)
    return render(request, 'myapp/index.html', {'foods': foods, 'consumed_food': consumed_food})

def delete_item(request, id):
    food_c = Consume.objects.get(id=id)
    if request.method == 'POST':
        food_c.delete()
        return redirect('/')
    
    return render(request, 'myapp/delete.html')
    