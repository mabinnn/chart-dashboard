from django.shortcuts import render, HttpResponse

# Create your views here.
def covetfahion_index(request):
    print " --- views.index"
    return render(request, 'dashboard/covetfashionindex.html')

def cf_dash1(request):
    print " --- views.cf_dash1"
    return render(request, 'dashboard/covetfashiondashboard_1.html')

def cf_dash2(request):
    print " --- views.cf_dash_2"
    return render(request, 'dashboard/covetfashiondashboard_2.html')

def designhome_index(request):
    print " -- views.designhome_index"
    return render(request, 'dashboard/homedesign.html')

def design_dash1(request):
    print " --- views.design_dash1"
    return render(request, 'dashboard/designhomedashboard_1.html')

def design_dash2(request):
    print " --- views.design_dash2"
    return render(request, 'dashboard/designhomedashboard_2.html')
