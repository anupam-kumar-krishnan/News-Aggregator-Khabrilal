from django.http import HttpResponse
from django.shortcuts import render
from newsapi import NewsApiClient

def index(request):
    return render(request,"index.html")


def business(request):
    newsapi = NewsApiClient(api_key = "3020db5daf77473dad1742f6293a3429")   
    businessnews = newsapi.get_top_headlines(category="business",country="in") 
    articles = businessnews['articles']
    desc = []
    news = []
    img = []
    url= []
    auth = []
    date = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        auth.append(myarticles['author'])
        date.append(myarticles['publishedAt'])

    mylist = zip(news, desc, img, url, auth, date)

    return render(request, 'news.html', context = {"mylist": mylist})

def health(request):
    newsapi = NewsApiClient(api_key = "3020db5daf77473dad1742f6293a3429")   
    healthnews = newsapi.get_top_headlines(category="health",country="in") 
    articles = healthnews['articles']
    desc = []
    news = []
    img = []
    url= []
    auth = []
    date = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        auth.append(myarticles['author'])
        date.append(myarticles['publishedAt'])

    mylist = zip(news, desc, img, url, auth, date)

    return render(request, 'news.html', context = {"mylist": mylist})



def science(request):
    newsapi = NewsApiClient(api_key = "3020db5daf77473dad1742f6293a3429")   
    sciencenews = newsapi.get_top_headlines(category="science",country="in") 
    articles = sciencenews['articles']
    desc = []
    news = []
    img = []
    url= []
    auth = []
    date = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        auth.append(myarticles['author'])
        date.append(myarticles['publishedAt'])

    mylist = zip(news, desc, img, url, auth, date)

    return render(request, 'news.html', context = {"mylist": mylist})


def technology(request):
    newsapi = NewsApiClient(api_key = "3020db5daf77473dad1742f6293a3429")   
    technologynews = newsapi.get_top_headlines(category="technology",country="in") 
    articles = technologynews['articles']
    desc = []
    news = []
    img = []
    url= []
    auth = []
    date = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        auth.append(myarticles['author'])
        date.append(myarticles['publishedAt'])

    mylist = zip(news, desc, img, url, auth, date)

    return render(request, 'news.html', context = {"mylist": mylist})

def general(request):
    newsapi = NewsApiClient(api_key = "3020db5daf77473dad1742f6293a3429")   
    generalnews = newsapi.get_top_headlines(category="general",country="in") 
    articles = generalnews['articles']
    desc = []
    news = []
    img = []
    url= []
    auth = []
    date = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        auth.append(myarticles['author'])
        date.append(myarticles['publishedAt'])

    mylist = zip(news, desc, img, url, auth, date)

    return render(request, 'news.html', context = {"mylist": mylist})

def entertainment(request):
    newsapi = NewsApiClient(api_key = "3020db5daf77473dad1742f6293a3429")   
    entertainmentnews = newsapi.get_top_headlines(category="entertainment",country="in") 
    articles = entertainmentnews['articles']
    desc = []
    news = []
    img = []
    url= []
    auth = []
    date = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        auth.append(myarticles['author'])
        date.append(myarticles['publishedAt'])

    mylist = zip(news, desc, img, url, auth, date)

    return render(request, 'news.html', context = {"mylist": mylist})

def sports(request):
    newsapi = NewsApiClient(api_key = "3020db5daf77473dad1742f6293a3429")   
    sportsnews = newsapi.get_top_headlines(category="sports",country="in") 
    articles = sportsnews['articles']
    desc = []
    news = []
    img = []
    url= []
    auth = []
    date = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        auth.append(myarticles['author'])
        date.append(myarticles['publishedAt'])

    mylist = zip(news, desc, img, url, auth, date)

    return render(request, 'news.html', context = {"mylist": mylist})
    