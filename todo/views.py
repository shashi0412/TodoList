from django.shortcuts import render, HttpResponse, redirect
from todo.models import TodoItem

# Create your views here.
def main(request):
    items = TodoItem.objects.all()
    context = {
        'items' : items
    }
    return render(request, 'index.html', context)

def additem(request):
    new_item = TodoItem(content=request.POST['add_item'])
    new_item.save()
    return redirect('/')

def deleteitem(request, item_id):
    item_to_delete = TodoItem.objects.get(id = item_id)
    item_to_delete.delete()
    return redirect('/')