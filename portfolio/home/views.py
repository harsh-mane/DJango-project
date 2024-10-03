from django.shortcuts import render, HttpResponse
from home.models import contact
# Create your views here.
def home(request):
    #return HttpResponse("This is my Homepage(/)")
    context = {'name': 'Harsh', 'course' : 'DJango'}
    return render(request,'home.html')

def about(request):
    # return HttpResponse("This is my about page(/about)")
    return render(request,'about.html')

def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        text = request.POST.get('text')
      
        
        print(f"{text}, {name},{phone}, {email}")
        print('Data has been inserted')
        c = contact.objects.create(
            name = name,
            email = email,
            phone = phone,
            text = text
        )
        c.save()

     

      
        
        print("the data has been written to the Database")
    # return HttpResponse("This is my contacts page(/contacts)")
    return render(request,'contact.html')

def project(request):
   
   # return HttpResponse("This is my project page(/project)")
   return render(request,'project.html')