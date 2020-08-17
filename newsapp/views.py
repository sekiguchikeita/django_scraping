from django.shortcuts import render
from .models import News
from django.views.generic import CreateView
from django.urls import reverse_lazy
import urllib.request
import requests
# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup



class Create(CreateView):
   template_name = 'home.html'
   model = News
   fields = ('url',)
   success_url = reverse_lazy('list')



# urlのHTMLを取得
def listfunc(request):
    for post in News.objects.all():
        url = post.url
  
    response = requests.get(url)
    html = urllib.request.urlopen(url)
# htmlをBeautifulSoupでパース
    soup = BeautifulSoup(html, "html.parser")
# タイトル要素の文字列を取得
    # soup_title = str(soup.title) 
    
    soup_title = soup.title.string

    # soup_title = "aaa"
    # print(soup_title)

    context = {'soup_title':soup_title}
   
    print(context)

    return render(request, 'list.html',context)
