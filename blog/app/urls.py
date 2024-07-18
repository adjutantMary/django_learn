from django.urls import path
from app import views


app_name = 'blog'

urlpatterns = [
    # представление поста
    # path('', views.post_list, name='post_list'),
    
    #year: требует целое число
    #month:требует целое число
    #day:требует целое число
    #slug: требуется слаг 
    #(строка, содержащая только буквы, цифры, знаки подчеркивания или дефисы)
    
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/',
         views.post_list, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail, name='post_detail'),
    path('<int:post_id>/share/',
         views.post_share, name='post_share'),
    path('<int:post_id>/comment/',
         views.post_comment, name='post_comment'),
]
