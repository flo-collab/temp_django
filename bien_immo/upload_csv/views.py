from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os







def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def upload_csv(request):
    return render(request,'upload_csv/upload_csv.html')


def home(request):
    return HttpResponse('<h1>Welcome</h1>')

listfile = []
 
# def upload1(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         #print(myfile
#         print(myfile.name)
#         print(settings.MEDIA_ROOT)
#         print('laliste',os.listdir(settings.MEDIA_ROOT))
#         if myfile.name in os.listdir(settings.MEDIA_ROOT):
#             print("il faudra l'effacer")
#         #     return render(request,'upload_csv/first_delete.html')
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         print(filename)
#         return render(request, 'upload_csv/upload1.html', {
#             'uploaded_file_url': uploaded_file_url
#         })


#     else:
#         #print(type(request))
#     #elif (request.FILES['myfile']==None):
#         print('ooups')
#     #else:
#         #myfile = request.FILES['myfile']
#         #print(myfile)
#     # elif request.method == 'POST' and ~(request.FILES['myfile']):
#     #     nothing_uploaded = 'Aucun fichier uploadé !'
#     #     return render(request, 'upload_csv/upload1.html',{
#     #         'nothing_uploaded':nothing_uploaded
#     #     })

#     return render(request, 'upload_csv/upload1.html')


#   return render(request,'home.html')

#    
# Create your views here.


def upload1(request):
    if request.method == 'POST' and 'myfile' in request.FILES:
        print('check','myfile' in request.FILES)
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        print(myfile.name)
        print(settings.MEDIA_ROOT)
        print('laliste',os.listdir(settings.MEDIA_ROOT))
        # if myfile.name in os.listdir(settings.MEDIA_ROOT):
                   
        #     return render(request,'upload_csv/first_delete.html')
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print(filename)
        return render(request, 'upload_csv/upload1.html', {
            'uploaded_file_url': uploaded_file_url
        })
    #else:
        #print(type(request))
    elif request.method == 'POST' and 'myfile' not in request.FILES:
        nothing_uploaded = 'Aucun fichier uploadé !'        
        print('ooups')
        return render(request, 'upload_csv/upload1.html',{
            'nothing_uploaded':nothing_uploaded
        })
    else:
        nothing_uploaded = False 
        #myfile = request.FILES['myfile']
        #print(myfile)
    # elif request.method == 'POST' and ~(request.FILES['myfile']):
    #     


        return render(request, 'upload_csv/upload1.html')



