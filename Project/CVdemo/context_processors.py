import imp
from multiprocessing import context
from django.contrib.auth.models import User

def project_context(request):

    context = {
        'me':User.objects.first(),
    }

    return context
    