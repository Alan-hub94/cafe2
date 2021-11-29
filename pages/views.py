from django.shortcuts import render, get_object_or_404

from django.shortcuts import get_object_or_404, render
from .models import Policy

def politicas(request, policy_id):
    politicas = get_object_or_404(Policy, id= policy_id )
    return render(request, 'pages/sample.html', { 'politicas': politicas })
