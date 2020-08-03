from django.shortcuts import render
from django.db.models.fields import reverse_related, AutoField, related
from phones.models import Phone, ApplePhone, AndroidPhone, HuaweiPhone
from random import choice


def get_data_fields(model):
    return [field.name for field in model._meta.get_fields()
            if not isinstance(
                field,
                (reverse_related.OneToOneRel, related.OneToOneField, AutoField))
            ]


def show_catalog(request):
    template = 'catalog.html'
    fields = []
    for model in [ApplePhone, AndroidPhone, HuaweiPhone]:
        fields.extend(get_data_fields(model))
    fields = set(fields)
    fields.discard('name')
    context = {
        'phones': [
            choice(ApplePhone.objects.all()),
            choice(AndroidPhone.objects.all()),
            choice(HuaweiPhone.objects.all()),
        ],
        'fields': fields
    }

    return render(
        request,
        template,
        context
    )
