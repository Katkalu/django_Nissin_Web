from django.urls import path, include
from . import views



urlpatterns = [
    path('home', views.home, name="home"), #ez a views.py ban levő 'home' fügvvényt hivja meg
    path('base', views.base, name="base"), #ez a views.py ban levő 'base' fügvvényt hivja meg
    path('news', views.news, name="news"), #ez a views.py ban levő 'news' fügvvényt hivja meg
    path('news_pk', views.news_pk, name="news_pk"), #ez a views.py ban levő 'news' fügvvényt hivja meg
    path('events', views.events, name="events"), #ez a views.py ban levő 'events' fügvvényt hivja meg
    path('events_pk', views.events_pk, name="events_pk"),
    path('announcements', views.announcements, name="announcements"), #ez a views.py ban levő 'announcements' fügvvényt hivja meg
    path('announc_pk', views.announc_pk, name="announc_pk"),
    path('documents', views.documents, name="documents"), #ez a views.py ban levő 'documents' fügvvényt hivja meg
    path('search_result', views.search_result, name="search_result"), 
    path('calendar', views.calendar, name="calendar"), 
    path('', views.home, name="home"),
]

