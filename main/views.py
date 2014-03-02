from django.shortcuts import HttpResponseRedirect, render_to_response

def home_view(request):
    return render_to_response('index.html')