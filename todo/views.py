from django.shortcuts import render, redirect
from .models import Item
from django.views import generic
from .models import Post


# --- This is a FUNCTIONAL View
# | Returns context so that 'items' is available in our html file ---
# This function READS items from the database
def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


# This function CREATES new items.
def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)
        return redirect('get_todo_list')
    return render(request, 'todo/add_item.html')


# --- This is a CLASS-BASED View
# --- Allows use of inheritence of django generic views
# https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-display/


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html'
    paginate_by = 6
