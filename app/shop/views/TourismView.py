from django.shortcuts import render

from shop.models.Tourism import Tourism


def tourism_view(request):
    tourism = Tourism.objects.all()
    return render(request, "shop/Tourism.html", {'tourism': tourism})
