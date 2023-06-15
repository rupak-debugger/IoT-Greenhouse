from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from greenhouse.models import SensorData, RelayControl
from django.http.response import JsonResponse
# Create your views here.


@login_required(login_url='/accounts')
def home(request):
    sdata = SensorData.objects.last()
    bdata = RelayControl.objects.get(id=1)
    return render(request, 'home.html', {'sdata': sdata, 'bdata': bdata, })


@login_required(login_url='/accounts')
def change_control_value(request):
    if request.method == 'POST':
        p = request.POST['relay']
        if p == 'relay1off':
            RelayControl.objects.filter(id=1).update(relay1=True)
            return redirect('/')
        elif p == 'relay2off':
            RelayControl.objects.filter(id=1).update(relay2=True)
            return redirect('/')
        elif p == 'relay1on':
            RelayControl.objects.filter(id=1).update(relay1=False)
            return redirect('/')
        elif p == 'relay2on':
            RelayControl.objects.filter(id=1).update(relay2=False)
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/')


def histogram(request):
    sensor_data = SensorData.objects.all().order_by('-id')[:20]
    temperature = []
    humidity = []
    date = []

    for s in sensor_data:
        temperature.append(s.temperature)
        humidity.append(s.humidity)
        date.append(s.date_posted.strftime('%H:%m : %S'))

    response = {
        'temperature': temperature,
        'humidity': humidity,
        'date': date,
    }

    return JsonResponse(response)
