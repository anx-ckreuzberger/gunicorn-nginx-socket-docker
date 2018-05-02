from django.template import Template, Context
from django.http import HttpResponse
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    t = Template("<html><body>It is now {{ current_date }}. Your IP is #{{ ip }}#</body></html>")
    html = t.render(Context({
        'current_date': now,
        'ip': request.META.get('REMOTE_ADDR', "[empty]")
    }))

    return HttpResponse(html)
