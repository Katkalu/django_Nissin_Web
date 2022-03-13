from asyncio.windows_events import NULL
from unicodedata import decimal
from django.shortcuts import render
from django.utils.translation import gettext as _  #multi language
from django.utils.translation import get_language, activate, gettext
from itsdangerous import json
from .models import News
from .models import Delta_Time
from .models import Product_value
from .models import Slide
from .models import Announcement
from .models import Document
from .models import Event
from PIL import Image
from datetime import datetime, timedelta, timezone, date, time
from django.db.models import Q
from django.core import serializers
from django.http import JsonResponse

def base(request):
    return render(request, 'base.html', {})

def home(request):
    all_news_home = News.objects.all().order_by('-record_date',)
        
    all_egyutt = unio_egyutt()
    c = delta()
    
    all_slide = Slide.objects.all()
    all_value = Product_value.objects.all()
    return render(request, 'home.html', {'all':all_news_home, 'c':c, 'all_slide':all_slide, 'all_value':all_value, 'all_egyutt':all_egyutt})

#def join(request):
 #   return render(request, 'join.html', {})

def news(request):
    all_news = News.objects.all().order_by('-record_date',) ## fordított sorrendben írja ki őket a dátum alapján 
    c = delta()
    all_value = Product_value.objects.all()
    return render(request, 'news.html', {'all':all_news, 'c':c, 'all_value':all_value})

def news_pk(request):
    news_id = int(request.GET["pk"])
    all_news_pk = News.objects.all().filter(pk = int(news_id)) # a GET el átadott pk -ju elemet teszi bele csak - egy elem
    c = delta()
    all_value = Product_value.objects.all()
    return render(request, 'news_pk.html', {'all':all_news_pk, 'c':c, 'all_value':all_value})
    
def events(request):
    c = delta()
    all_value = Product_value.objects.all()
    all_events = Event.objects.all().order_by('-record_date',)
    return render(request, 'events.html', {'c':c, 'all_value':all_value, 'all_event':all_events})

def events_pk(request):
    events_id = int(request.GET["pk"])
    all_events_pk = Event.objects.all().filter(pk = int(events_id)) # a GET el átadott pk -ju elemet teszi bele csak - egy elem
    c = delta()
    all_value = Product_value.objects.all()
    return render(request, 'events_pk.html', {'all':all_events_pk, 'c':c, 'all_value':all_value})
    
def announcements(request):
    all_announcements = Announcement.objects.all().order_by('-record_date',)
    c = delta()
    all_value = Product_value.objects.all()
    return render(request, 'announcements.html', {'all_announcements':all_announcements, 'c':c, 'all_value':all_value})

def announc_pk(request):
    ann_id = int(request.GET["pk"])
    all_ann_pk = Announcement.objects.all().filter(pk = int(ann_id)) # a GET el átadott pk -ju elemet teszi bele csak - egy elem
    c = delta()
    all_value = Product_value.objects.all()
    return render(request, 'announc_pk.html', {'all':all_ann_pk, 'c':c, 'all_value':all_value})

def documents(request):
    all_docu = Document.objects.all()

    db_hr = Document.objects.filter(department = 'hr').count()
    db_it = Document.objects.filter(department = 'it').count()
    db_egyeb = Document.objects.filter(department = 'egyeb').count()
    db_production = Document.objects.filter(department = 'production').count()
    db_maintenance = Document.objects.filter(department = 'maintenance').count()
    db_qaqc = Document.objects.filter(department = 'qaqc').count()
    db_scm = Document.objects.filter(department = 'scm').count()
    db_randd = Document.objects.filter(department = 'r&d').count()
    db_purchasing = Document.objects.filter(department = 'purchasing').count()
    db_kaizen = Document.objects.filter(department = 'kaizen').count()
    db_sales = Document.objects.filter(department = 'sales').count()
    db_marketing = Document.objects.filter(department = 'marketing').count()
    db_finance = Document.objects.filter(department = 'finance').count()
    db_ga = Document.objects.filter(department = 'ga').count()
    
    now = datetime.now(timezone.utc).date
    c = delta()
    all_value = Product_value.objects.all()
    return render(request, 'documents.html', {'c':c, 'now':now ,'all_value':all_value, 'all_docu':all_docu, 
    'db_hr':db_hr, 'db_it':db_it, 'db_egyeb':db_egyeb, 'db_production':db_production, 'db_maintenance':db_maintenance,
    'db_qaqc':db_qaqc, 'db_scm':db_scm, 'db_randd':db_randd, 'db_purchasing':db_purchasing, 'db_kaizen':db_kaizen, 'db_sales':db_sales, 
    'db_marketing':db_marketing, 'db_finance':db_finance, 'db_ga':db_ga })



def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('hello')
    finally:
        activate(cur_language)
    return text

def delta():
    one_entry = Delta_Time.objects.get(pk=1)  #a start détum lekérése, benne csak egy idő elem
    b = one_entry.record_date # b ben a datum elem
    a = datetime.now(timezone.utc)  # mai dátim , időzona kellett hozzá
    days = a - b #az eltelt idő 
    c = days.days # csak napokban
    return c

def unio_egyutt():  # uniot képez a hír és közlemény táblákból
    all_egyutt = News.objects.values(
        "pk", "type", "titel_hu", "titel_en", "short_text_hu", "short_text_en", "img"
    ).union(
    Announcement.objects.values(
        "pk", "type", "titel_hu", "titel_en", "short_text_hu", "short_text_en", "img"
    )).order_by('-record_date',)

    return all_egyutt

def search_result(request):
    query = request.GET["q"] #keresesi mező tartalma
    all_egyutt = News.objects.filter(
            Q(titel_hu__icontains=query) | Q(titel_en__icontains=query) | Q(short_text_hu__icontains=query) | Q(short_text_en__icontains=query) | Q(content_hu__icontains=query) | Q(content_en__icontains=query)
        ).values(
        "pk", "type", "titel_hu", "titel_en", "short_text_hu", "short_text_en", "img"
    ).union(
    Announcement.objects.filter(
            Q(titel_hu__icontains=query) | Q(titel_en__icontains=query) | Q(short_text_hu__icontains=query) | Q(short_text_en__icontains=query) | Q(content_hu__icontains=query) | Q(content_en__icontains=query)
        ).values(
        "pk", "type", "titel_hu", "titel_en", "short_text_hu", "short_text_en", "img"
    )).union(
    Event.objects.filter(
            Q(titel_hu__icontains=query) | Q(titel_en__icontains=query) | Q(short_text_hu__icontains=query) | Q(short_text_en__icontains=query) | Q(content_hu__icontains=query) | Q(content_en__icontains=query)
        ).values(
        "pk", "type", "titel_hu", "titel_en", "short_text_hu", "short_text_en", "img"
    ))
 
    c = delta() 
    all_value = Product_value.objects.all()   

    return render(request, 'search_result.html', {'c':c, 'all_value':all_value, 'all_egyutt':all_egyutt, 'query':query})

def calendar(request):
    data_normal = Event.objects.all().values('titel_hu', 'titel_en') 
    data = serializers.serialize("json", Event.objects.all(), fields=('titel_hu', 'titel_en', 'start_date', 'end_date'))
    data_date = serializers.serialize("json", Event.objects.all(), fields=('start_date', 'end_date'))
    #data_l = list(Event.objects.all().values('titel_hu', 'titel_en')) 
    #data_d = json.loads(data)

    return render(request, 'calendar.html', {'data':data, 'data_normal':data_normal,'data_date':data_date})

