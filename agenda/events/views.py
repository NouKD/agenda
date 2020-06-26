from django.shortcuts import render

# Create your views here.
def events(request):
    
    data = {
        
    }
    
    return render(request, 'pages/events.html', data)

def event_N(request):
    
    data = {
        
    }
    
    return render(request, 'pages/events-news.html', data)

def single_event(request):
    
    data = {
        
    }
    
    return render(request, 'pages/single-event.html', data)    
