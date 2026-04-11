from django.shortcuts import render, redirect
from .forms import List
from .models import ListModel
# Create your views here.

# Home View
def home_view(request):
    return render(request, 'static/home.html')

# Create List View
def create_list(request):
    form = List()
    if request.method == "POST":
        form =  List(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'static/create_list.html', {'form':form})

# Show list View
def show_list(request):
    lists = ListModel.objects.all()
    return render(request, 'static/show_list.html', {'lists':lists})
    

# Delete View
def delete_view(request, Title):
    title = ListModel.objects.get(Title=Title)
    if request.method == 'POST':
        title.delete()
        return redirect('show_list')
    return render(request, 'static/confirm_delete.html', {'title':title})
