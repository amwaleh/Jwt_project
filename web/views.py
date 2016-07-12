from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# include the login decorator to protect views
# https://docs.djangoproject.com/en/1.9/topics/class-based-views/intro/
@method_decorator(login_required, name='dispatch')
class homeview (View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)