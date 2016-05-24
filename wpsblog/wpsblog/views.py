from django.http.response import HttpResponse

# MVC Controller
def home(request):
    return HttpResponse("hello world")

def room(request, room_id):
    return HttpResponse("This is a room detail " + room_id)

