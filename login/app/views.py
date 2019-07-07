from django.shortcuts import render

# Create your views here.
def login(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm
        return render(request,"login.html",{'form':form})