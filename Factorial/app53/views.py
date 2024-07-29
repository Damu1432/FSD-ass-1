from django.shortcuts import render
from math import factorial

def factorial_view(request):
    numbers = list(range(3, 9))
    factorials = {n: factorial(n) for n in numbers}
    return render(request, 'app53/factorial.html', {'factorials': factorials})
