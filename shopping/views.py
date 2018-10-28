from django.shortcuts import render
from .buttons import item_list
from .core_shopping_list import *

# Create your views here.
def shopping(request):
    if request.method == "POST":
        shopping_list = []
        #print(request.POST)
        for item in request.POST:
            if item in item_list:
                shopping_list.append(item)
        min_shop = main(shopping_list)
        return render(request, 'shopping/min_shop.html', {'min_shop':min_shop})    
                
        
    return render(request, 'shopping/shopping_list.html', {'buttons':item_list})    
    