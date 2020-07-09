from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts = [
    {
        'author':'notatharva',
        'title':'July 09 Another shitty day',
        'content':'Today a dark spot on the internet was born',
        'date_post':'July 09, 2020'
    },
    {
        'author':'notatharva',
        'title':'July 09 Another shitty post',
        'content':'kill me before i get you',
        'date_post':'July 09, 2020'
    }
]



def home(request):
  context = {
      'posts':posts
  }
  return render(request, 'home.html',context)
def about(request):
  return render(request, 'about.html',{'title': 'about'}) 