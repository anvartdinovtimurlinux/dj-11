from django.urls import path

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам
from app.views import file_list, file_content

urlpatterns = [
    path('', file_list, name='file_list'),
    path('<dt:date>', file_list, name='file_list'),
    path('file/<str:name>', file_content, name='file_content'),
]
