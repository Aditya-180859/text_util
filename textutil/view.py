from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')


def analyze(request):

    #get text
    djtext=request.POST.get('text','default')

    #chexking check box value
    removepunc=request.POST.get('removepunc','OFF')
    fullcap = request.POST.get('fullcap', 'OFF')
    newlineremover= request.POST.get('newlineremover', 'OFF')

    task=""
    #checking which check box is on
    if removepunc== "on":
        punctuations=''' !()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char  not in punctuations:
                analyzed= analyzed+char
        task+="remove Punctuations|"
        dictionary={'purpose':task, 'analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',dictionary)

    if fullcap=="on":
        analyzed=""
        for char in djtext:
            analyzed =analyzed+char.upper()

        task+="Full capitiliztion"
        dictionary = {'purpose': task, 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', dictionary)


    if newlineremover == "on":
        analyzed = ""

        for char in djtext:
            if char != "\n" and char !='\r':
                analyzed = analyzed + char

        task+='|remove new line'
        dictionary = {'purpose': task, 'analyzed_text': analyzed}

        #return render(request, 'analyze.html', dictionary)

    if(newlineremover != "on" and fullcap!="on" and removepunc!= "on"):
        return HttpResponse("error")

    return render(request, 'analyze.html', dictionary)



