from django.shortcuts import render
from django.views.generic import  ListView
from news.models import Articles
def index(request):
    data={
        'title': 'ну типо очень главная страница',
        'values': ['kek','Hell','Smert']
    }
    return render(request,'main/index.html',data)
def about(request):
    return render(request,'main/about.html', {'rer':'ну тут типо про нас написано '})
def contact(request):
    return render(request, 'main/contact.html', {'rer': 'ну тут типо про нас написано '})

