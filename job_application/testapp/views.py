from django.shortcuts import render
from django.http import HttpResponse
from testapp import templates
#from css import text
# Create your views here.
def view(request):

    return render(request,'testapp/results.html')
    return render(request, 'testapp/Thank.html')
    #return render(request,'css/test.css')