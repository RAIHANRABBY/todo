
from django.shortcuts import render,redirect
from .forms import ActivityForm
from .models import Activity

# Create your views here.
def homeView(request):
    form=ActivityForm()
    if request.method =='POST':
        form=ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
        
 
    content={'activityForm':form,'activity':Activity.objects.all()}
    return render(request,'base/home.html',content)

def remove_event(request,pk):
    event=Activity.objects.get(id=pk)
    if request.method== "POST":
        event.delete()
            
        return redirect('home')

    content={'event':event}
    return render(request,'base/home.html',content)
