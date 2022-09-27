from django.shortcuts import render
from .models import Item


# --- This is a FUNCTIONAL View
# | Returns context so that 'items' is available in our html file ---
def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)
