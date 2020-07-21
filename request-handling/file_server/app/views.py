from datetime import datetime
import os

from django.conf import settings
from django.shortcuts import render
from django.urls import register_converter


class DateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value: str) -> datetime:
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value: datetime) -> str:
        return value.strftime('%Y-%m-%d')


register_converter(DateConverter, 'dt')


def file_list(request, date=None):
    files_list = os.listdir(settings.FILES_PATH)
    files = []
    for file in files_list:
        file_path = os.path.join(settings.FILES_PATH, file)
        file_stat = os.stat(file_path)
        files.append({
            'name': file,
            'ctime': datetime.utcfromtimestamp(file_stat.st_ctime),
            'mtime': datetime.utcfromtimestamp(file_stat.st_mtime)
        })

    if date:
        files = [file for file in files
                 if file['ctime'].date() == date.date()]

    context = {
        'files': files
    }

    return render(request, 'index.html', context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    file_path = os.path.join(settings.FILES_PATH, name)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    return render(
        request,
        'file_content.html',
        context={'file_name': 'file_name_1.txt', 'file_content': content}
    )

