from django.http import HttpResponse

# Create your views here.
def homePageView(request):
    return HttpResponse("Hello, world! This is the home page.")