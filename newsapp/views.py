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
        print("aaa" + url)
        list = []
  
    # for post in News.objects.all():
    # url = request
    # print("aaa" + url)
    # print(request)
    # list = []
    

    response = requests.get(url)
    html = urllib.request.urlopen(url)
# htmlをBeautifulSoupでパース
    soup = BeautifulSoup(html, "html.parser")
# タイトル要素の文字列を取得
    # soup_title = str(soup.title) 
    
    head_info = soup.find('head')

    meta_img = head_info.find('meta', {'property' : 'og:image'})
    soup_img = meta_img['content']

    meta_description = head_info.find('meta', {'name' : 'description'})
    soup_desc = meta_description['content']

    soup_title = head_info.find('title').getText()

    # print(soup_desc)

    # soup_title = "aaa"
    # print(soup_desc)

    # context1 = {'soup_title':soup_title}
    # context2 = {'soup_desc': soup_desc}
   
    # print(context1)
    # print(context2)
   
   
    list.append([soup_title, soup_desc, soup_img])
    # list.clear()
    

    context = {'list':list}
  

    # return render(request, 'list.html',context1)
    return render(request, 'home.html',context)
    
