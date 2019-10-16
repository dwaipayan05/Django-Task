from django.shortcuts import render
from .models import Names
from django.http import Http404, HttpResponse
from .helper_function import distance_finder

def address1(request):
    return render(request, 'friends/Input Form.html')

def calculate(request):
    if request.method == 'POST':
        latit = float(request.POST.get('Latitude', None))
        longit = float(request.POST.get('Longitude', None))
        kilometers = float(request.POST.get('range', None))
        print(latit, longit, kilometers)
        all_names = Names.objects.all()
        required_names = []
        user = []

        for entry in all_names:
            if(distance_finder(latit,longit,entry.latitude,entry.longitude)<=range):
                required_names.append([entry.user_id,entry.friend_name])

        print(required_names)
        context = {'required_names': required_names, 'user': user}

        return render(request, 'friends/Distance Condition.html')
    else:
        html = "<html><body>It is now</body></html>"
        return HttpResponse(html)

def index(request):
            all_names = Names.objects.all()
            context = {'all_names': all_names}
            return render(request, 'friends/index.html')

def check(request,userid):
    try:
        entry = Names.objects.get(user_id=userid)
    except Names.DoesNotExist:
        raise Http404("Name not Found")
    return render(request, 'friends/check.html')

