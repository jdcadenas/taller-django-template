from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# esto esta modificado por josé


@login_required(login_url="/accounts/login/")
def index(request):

    # Page from the theme 
    return render(request, 'accounts/sign-in.html') 
