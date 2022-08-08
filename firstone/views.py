# I have created this file - Harsh

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("HOME")
def removepunc(request):
    djtext = (request.POST.get("inputtext", "default"))
    punctuations = ''':()-[]{};!'"\,<>./?@#$%^&*_~|'''
    analysed = ""
    for char in djtext:
        if char not in punctuations:
            analysed = analysed + char
    params = {'change': 'removed the punctuations', 'analysed_text': analysed, 'original_text': djtext}

    return render(request, 'template1.html', params)
def capall(request):
    djtext = (request.POST.get("inputtext", "default"))
    analysed = ""
    for char in djtext:
        analysed = analysed + char.upper()

    params = {'change': 'capitalised all the letters', 'analysed_text': analysed, 'original_text': djtext}
    return render(request, 'template1.html', params)
def exspaceremove(request):
    djtext = (request.POST.get("inputtext", "default"))
    analysed = ""
    for i in range(0, len(djtext)):
        if not(djtext[i] == " " and djtext[i+1] == " " and i < len((djtext))):
            analysed = analysed + djtext[i]

    params = {'change': 'removed the extra spaces', 'analysed_text': analysed, 'original_text': djtext}
    return render(request, 'template1.html', params)
