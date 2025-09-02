from django.shortcuts import render

# Create your views here.
def vista1_app2(req):
  return render(req, 'app2/vista1_app2.html')

def vista2_app2(req):
  return render(req, 'app2/vista2_app2.html')
