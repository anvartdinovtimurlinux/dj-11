from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'

    with open('./inflation_russia.csv', encoding='utf-8') as f:
        inflation = list(csv.reader(f, delimiter=';'))

    context = {
        'table_header': inflation[0],
        'table_body': inflation[1:],
    }

    return render(request, template_name,
                  context)
