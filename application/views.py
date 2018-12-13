from django.shortcuts import render

def IndexView(request):
    template_name = 'application/index.html'
    array = ['new','tong','nok']
    j = 5
    yo = ""
    if request.method == 'POST':
        yo = request.POST.get('hayato')
    context = {
        'call' : array,
        'japan' : j,
        'yoyo' : yo,    
    }
    return render(request,template_name,context)