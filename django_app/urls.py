from django.urls import path
from . import views

app_name = 'django_app'

urlpatterns = [
    path('good/', views.index, name='index'),
    path('home/<str:user_name>', views.home, name='home'),
    path('memo/', views.memo, name='memo'),
    path('new_memo/', views.new_memo, name='new_memo'),
    # path('edit_memo/', views.edit_memo, name='edit_memo'),
    path('edit_memo/<int:memo_id>', views.edit_memo, name='edit_memo'),
    path('delete_memo/<int:memo_id>', views.delete_memo, name='delete_memo'),
]
