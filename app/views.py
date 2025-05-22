from django.shortcuts import render, redirect
from django.views import View
from cinemas.models import Cinemas, CinemaComents
from news.models import News, NewsComents
from datetime import date
from contact.models import Contact
import requests, json
# Create your views here.

class IndexView(View):
    def get(self, request):
        start_date = date(2025, 5, 1)
        end_date = date(2025, 5, 31)
        cinemas = Cinemas.objects.all()
        release_date = Cinemas.objects.filter(created_at__range=(start_date, end_date))

        soon = Cinemas.objects.filter(category=2)
        news = News.objects.all()

        return render(request, 'index.html', {'cinemas': cinemas, 'release_date': release_date, 'start_date': start_date, 'end_date': end_date, 'soon': soon, 'news': news})
    
    def post(self , request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(name=name, email=email, text=message)

        bot_token = "7289685219:AAE2sMIatykwNy_7797yFGBDrSC9aKKdG48"
        my_id = '7318128389'

        url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        headers = {'Content-Type': 'application/json'}
        data = {
            'chat_id': my_id,
            'text': f'Name: {name}\nEmail: {email}\nMessage: {message}'
        }

        try :
            response = requests.post(url, headers=headers, data=json.dumps(data))
            response.raise_for_status()
            print('Message sent successfully')
            return redirect('app:index')
        except: print('Xatolik')


class SingleView(View):
    def get(self, request, id):
        cinema = Cinemas.objects.get(id=id)
        cinemas = Cinemas.objects.all()[:3]
        comment = CinemaComents.objects.filter(cinema=cinema)
        range_10 = range(1, 11)
        return render(request, 'single.html', {'cinema': cinema, 'cinemas': cinemas, 'comment': comment, 'range_10': range_10})
    def post(self, request, id):
        cinema = Cinemas.objects.get(id=id)
        comment = CinemaComents()
        comment.comment_text = request.POST.get('review')
        comment.comment_author = request.POST.get('name')
        comment.commentAuthorEmail = request.POST.get('email')
        comment.rating = request.POST.get('rating')
        comment.cinema = cinema
        comment.save()
        return redirect('app:singlePage', id=cinema.id)

class ArticleView(View):
    def get(self, request, id):
        news = News.objects.get(id=id)
        comment = NewsComents.objects.filter(news=news)
        new = News.objects.all()[:3]
        return render(request, 'news_single.html', {'new': news, 'comment': comment, 'news': new})

    def post(self, request, id):
        news = News.objects.get(id=id)
        comment = NewsComents()
        comment.comment_text = request.POST.get('review')
        comment.comment_author = request.POST.get('name')
        comment.commentAuthorEmail = request.POST.get('email')
        comment.rating = request.POST.get('rating')
        comment.news = news
        comment.save()
        return redirect('app:articlePage', id=news.id)