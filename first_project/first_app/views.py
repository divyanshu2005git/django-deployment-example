from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,webPage,Topic
from . import forms 
# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,"first_app/index.html", context=date_dict) 

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("validated")
            print("name  :"+form.cleaned_data['name'])
            print("email  :"+form.cleaned_data['email'])
            print("text  :"+form.cleaned_data['text'])




    return render(request, 'first_app/formpg.html', {'form':form})