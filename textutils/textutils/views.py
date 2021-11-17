# Manually Created
from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request,"index.html")

def analyze(request):


    djtext=request.POST.get("text","default")
    removepunc=request.POST.get("removepunc","off")
    fullcap=request.POST.get("fullcap","off")
    newlineremover=request.POST.get("newlineremover","off")
    extraspaceremover=request.POST.get("extraspaceremover","off")
    charactercounter=request.POST.get("charactercounter","off")



    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for  char in djtext:
           if char not in punctuations:
               analyzed=analyzed+char


        dict1 = {"purpose": "Removed Punctuation","analyzed_text": analyzed}
        djtext=analyzed


    if fullcap == "on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+ str(char).upper()

        dict1 = {"purpose": "Changed to Upper case", "analyzed_text": analyzed}
        djtext=analyzed


    if newlineremover == "on":
        analyzed=""
        for char in djtext:
            if char !="\n" and char !="\r":
             analyzed=analyzed+ char

        dict1 = {"purpose": "Remove new line", "analyzed_text": analyzed}
        djtext=analyzed



    if extraspaceremover == "on":

        analyzed = ""

        for index, char in enumerate(djtext):

            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        dict1 = {"purpose": "Remove Extra Space", "analyzed_text": analyzed}
        djtext=analyzed


    if charactercounter == "on":

        analyzed =len(djtext)





        dict1 = {"purpose": "charctercounter", "analyzed_text":analyzed}


    if removepunc != "on" and fullcap != "on" and newlineremover != "on" and extraspaceremover != "on" and charactercounter != "on":

        return HttpResponse("Please Select any Operation")

    return render(request, "analyze.html", dict1)




