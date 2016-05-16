from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Product
from .models import Category
from django.template import loader
from django.http import Http404


def index(request):
    cat_list = Category.objects.all()
    template = loader.get_template("pycharmfirst/index.html")
    context = {
        'cat_list' : cat_list
    }
    return HttpResponse(template.render(context,request))

def products(request,cat_id):
    try:
        cat = Category.objects.get(pk=cat_id)

    except Category.DoesNotExist:
        raise Http404("Empty")
    return render(request,"pycharmfirst/products.html",{'cat': cat})


def categoryaddform(request):
    return render(request,"pycharmfirst/addcategory.html")


def addcategory(request,cat_id=0):
    cat_name = request.POST['cat_name']
    cat = Category(category_name=cat_name)
    cat.save()
    return HttpResponseRedirect(reverse('pycharmfirst:index'))
