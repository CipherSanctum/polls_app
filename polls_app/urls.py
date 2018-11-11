from django.urls import path
from . import views
# from django.views.decorators.cache import cache_page


app_name = 'polls_app'

urlpatterns = [
    path('', views.vote, name='vote'),  # Global votes go to this page/view... It's intended for the .latest() poll on a home page, etc.
    path('blog/<int:year>/<int:month>/<int:day>/<slug:post>/', views.blog_vote, name='blog_vote'),  # votes for question on a particular blog
]
