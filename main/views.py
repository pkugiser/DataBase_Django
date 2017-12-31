from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from django.core import serializers
from django.contrib.auth.decorators import login_required
from . import models
from . import funcs
import json

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')

@login_required
def map(request):
    return render(request, 'main/map.html')


@login_required
def result(request):
    if (request.method == 'POST' and 'input' in request.POST
            and request.POST['input']):
        search = True
        string = request.POST['input']
    elif(request.method == 'GET' and 'string' in request.GET):
        search = True
        string = request.GET.get('string')

    else:
        # return HttpResponseRedirect(reverse('main:index'))
        # data = "We could not perform this search. \
        # Search text is required when searching."
        search = False
    if(search):
        data = models.TravelPoiUserinfoSuzhou.objects.filter(
            screen_name__contains=string).order_by("created_at_int")
        page = request.GET.get('page')
        paginator = Paginator(data, 20)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        context = {'data': data, 'string': string}
        return render(request, 'main/result.html', context)
    else:
        return HttpResponseRedirect(reverse('main:index'))


@login_required
def userinfo(request, uid):
    userR = models.TravelPoiUserinfoSuzhou.objects.get(id=uid)
    #data = models.TravelPoiWeibosSuzhou.objects.filter(uid__exact=uid)
    data = models.TravelPoiUsersWeibodataSuzhou.objects.filter(
        userid__exact=uid).order_by('id')
    page = request.GET.get('page')
    paginator = Paginator(data, 20)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    context = {'userR': userR, 'data': data}
    return render(request, 'main/userinfo.html', context)


@login_required
def test(request):
    page = request.GET.get('page')
    data = models.TravelPoiUserinfoSuzhou.objects.all().order_by('created_at_int')
    paginator = Paginator(data, 20)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    context = {'data': data}
    return render(request, 'main/test.html', context)


@login_required
def EmotionAnalysis(request):
    # uid = 1216254405
    # data = models.TravelPoiUsersWeibodataSuzhou.objects.filter(userid__exact=uid).order_by('id')
    # lt = list(data.values_list('text',flat=True))
    # plotdiv = funcs.plots(lt)
    plotdiv = '''<div id="eb1342ac-4d8a-42b7-b0fc-c32919429d2c" style="height: 100%; width: 100%;"\
     class="plotly-graph-div"></div><script type="text/javascript">window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("eb1342ac-4d8a-42b7-b0fc-c32919429d2c", \
     [{"type": "scatter", "x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], \
     "y": [0.5, 0.5, 0.73863857984543, 0.1946309953928, 0.5, 0.50593131780624, 0.84168702363968, 0.5, 0, 0.5, 0.5, 0.5, 0.99047619104385, 0.57216626405716, 0.5, 0.63471966981888, 0.32888880372047, 0.57931786775589]}], \
     {"xaxis": {"autorange": true}, "yaxis": {"autorange": true}}, {"showLink": true, "linkText": "Export to plot.ly"})</script>'''
    context = {'plot': plotdiv}
    return render(request, 'main/EmotionAnalysis.html', context)


@login_required
def DaypartsAnalysis(request):
    plotdiv = funcs.plot2()
    context = {'plot': plotdiv}
    return render(request, 'main/DaypartsAnalysis.html', context)


@login_required
def POIAnalysis(request):
    return render(request, 'main/POIAnalysis.html')


@login_required
def RegionAnalysis(request):
    plotdiv = funcs.plot1()
    context = {'plot': plotdiv}
    return render(request, 'main/ra.html', context)


@login_required
def ea(request, uid):
    data = models.TravelPoiUsersWeibodataSuzhou.objects.filter(
        userid__exact=uid).order_by('id')
    # if(data.count()>30):
    #     data = data[:30]
    lt = list(data.values_list('text', flat=True))
    plotdiv = funcs.plots(lt)
    context = {'plot': plotdiv}
    return render(request, 'main/EmotionAnalysis.html', context)


@login_required
def da(request, uid):
    data = models.TravelPoiUsersWeibodataSuzhou.objects.filter(
        userid__exact=uid).order_by('id')
    lt = list(data.values_list('created_at', flat=True))
    plotdiv = funcs.plots2(lt)
    context = {'plot': plotdiv}
    return render(request, 'main/da.html', context)


@login_required
def pa(request, uid):
    data = models.TravelPoiUsersWeibodataSuzhou.objects.filter(
        userid__exact=uid).order_by('id')
    lt = list(data.values_list('text', flat=True))
    poi = funcs.pois(lt)
    context = {'plot': poi}
    return render(request, 'main/POIAnalysis.html', context)


@login_required
def ra(request, uid):
    #plotdiv = funcs.plot1()
    userR = models.TravelPoiUserinfoSuzhou.objects.get(id=uid)
    #data = models.TravelPoiWeibosSuzhou.objects.filter(uid__exact=uid)
    data = models.TravelPoiUsersWeibodataSuzhou.objects.filter(
        userid__exact=uid).order_by('created_at')
    lat = list(data.values_list('latitude', flat=True))
    lon = list(data.values_list('longitude', flat=True))
    context = {'userR': userR, 'lat': json.dumps(lat), 'lon': json.dumps(lon)}
    return render(request, 'main/RegionAnalysis.html', context)


@login_required
def poirst(request):
    if (request.method == 'POST' and 'input' in request.POST
            and request.POST['input']):
        search = True
        string = request.POST['input']
    elif(request.method == 'GET' and 'string' in request.GET):
        search = True
        string = request.GET.get('string')

    else:
        # return HttpResponseRedirect(reverse('main:index'))
        # data = "We could not perform this search. \
        # Search text is required when searching."
        search = False
    if(search):
        data = models.DistinctPoisSuzhou.objects.filter(
            title__contains=string).exclude(checkin_num__exact=0).order_by("-checkin_user_num","-checkin_num")
        page = request.GET.get('page')
        paginator = Paginator(data, 20)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        context = {'data': data, 'string': string}
        return render(request, 'main/poirst.html', context)
    else:
        return HttpResponseRedirect(reverse('main:map'))

@login_required
def category(request):
    if (request.method == 'POST' and 'input' in request.POST
            and request.POST['input']):
        search = True
        string = request.POST['input']
    elif(request.method == 'GET' and 'string' in request.GET):
        search = True
        string = request.GET.get('string')

    else:
        # return HttpResponseRedirect(reverse('main:index'))
        # data = "We could not perform this search. \
        # Search text is required when searching."
        search = False
    if(search):
        data = models.DistinctPoisSuzhou.objects.filter(
            category_name__contains=string).exclude(checkin_num__exact=0).order_by("-checkin_user_num","-checkin_num")
        page = request.GET.get('page')
        paginator = Paginator(data, 20)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        context = {'data': data, 'string': string}
        return render(request, 'main/category.html', context)
    else:
        return HttpResponseRedirect(reverse('main:map'))

@login_required
def dheatmap(request):
    #plotdiv = funcs.plot1()
    #data = models.TravelPoiWeibosSuzhou.objects.filter(uid__exact=uid)
    #
    #
    data = models.TravelPoiUsersWeibodataSuzhou.objects.all()[:100000]
    lat = list(data.values_list('latitude', flat=True))
    lon = list(data.values_list('longitude', flat=True))
    date = list(data.values_list('created_at', flat=True))
    context = {'lat': json.dumps(lat), 'lon': json.dumps(lon), 'date': json.dumps(date)}
    return render(request, 'main/dheatmap.html', context)


@login_required
def cheatmap(request):
    if(request.method == 'GET' and 'string' in request.GET):
        search = True
        string = request.GET.get('string')

    else:
        # return HttpResponseRedirect(reverse('main:index'))
        # data = "We could not perform this search. \
        # Search text is required when searching."
        search = False
    if(search):
        data = models.DistinctPoisSuzhou.objects.filter(
            category_name__contains=string).exclude(checkin_num__exact=0).order_by("-checkin_user_num","-checkin_num")
        lat = list(data.values_list('latitude', flat=True))
        lon = list(data.values_list('longitude', flat=True))
        num = list(data.values_list('checkin_num', flat=True))
        context = {'string': string, 'lat': json.dumps(lat), 'lon': json.dumps(lon), 'num': json.dumps(num)}
        return render(request, 'main/cheatmap.html', context)
    else:
        return HttpResponseRedirect(reverse('main:map'))