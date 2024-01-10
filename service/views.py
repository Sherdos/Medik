from django.shortcuts import render, redirect
from service import models
from service import forms

# Create your views here.
def add_feedback(request):
    form = forms.AddFeedbackForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')

def add_request_of_leave(request):
    form = forms.AddRequestOfLeaveForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')


def setting(fun):
    def wapper(request):
        setting = models.Setting.objects.latest('id')
        form = forms.AddFeedbackForm()
        respon = fun(request)
        respon['context']['setting']=setting
        respon['context']['form']=form
        return render(**respon)
    return wapper

@setting
def index(request):
    services = models.Service.objects.all()
    after_before = models.BeforeAfter.objects.all()
    team = models.Team.objects.all()
    feedbacks = models.Feedback.objects.all()[:5]
    context = {
        'services':services,
        'after_before':after_before,
        'team':team,
        'feedbacks':feedbacks
    }
    return {'request':request,'template_name':'index.html', 'context':context}

@setting
def after_before(request):
    after_before = models.BeforeAfter.objects.all()
    context = {
        'after_before':after_before,
        'setting':setting
    }
    return {'request':request,'template_name':'after__before.html', 'context':context}

@setting
def confidentialitly(request):
    return {'request':request,'template_name':'confidentiality.html', 'context':{}}

@setting
def price_list(request):
    return {'request':request, 'template_name':'price_list.html','context':{}}

@setting
def sale(request):
    sales = models.Sale.objects.all()
    context = {
        'sales':sales,
    }
    return {'request':request,'template_name':'sale.html', 'context':context}