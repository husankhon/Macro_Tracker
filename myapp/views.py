from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Food, FoodLog

# Create your views here.
def index(request):
    if request.method == 'POST':
        food_id = request.POST.get('food_id')
        servings = request.POST.get('servings', 1)
        user_id = request.POST.get('user_id')
        if food_id:
            food = Food.objects.filter(id=food_id).first()
            user = User.objects.filter(id=user_id).first() if user_id else None
            if food:
                FoodLog.objects.create(
                    user=user,
                    food=food,
                    servings=float(servings) if servings else 1.0,
                )
        return redirect('index')

    foods = Food.objects.all()
    users = User.objects.all()
    logs = FoodLog.objects.filter(user= request.user)
    totals = {
        'calories': sum(log.calories for log in logs),
        'protein': round(sum(log.protein for log in logs), 1),
        'carbs': round(sum(log.carbs for log in logs), 1),
        'fat': round(sum(log.fat for log in logs), 1),
    }
    return render(request, 'myapp/index.html', {
        'foods': foods,
        'users': users,
        'logs': logs,
        'totals': totals,
    })


def delete_food(request, food_id):
    log = FoodLog.objects.filter(id=food_id).first()
    if not log:
        return redirect('/')
    if request.method == 'POST':
        log.delete()
        return redirect('/')
    return render(request, 'myapp/delete.html', {'log': log})