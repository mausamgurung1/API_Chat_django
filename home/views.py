import os

import openai
from django.http import JsonResponse
from django.shortcuts import HttpResponse, render

openai.api_key = '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'
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def ChatAPI(request):
    if request.method =="POST":
        prompt = request.POST["prompt"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
        print(response)
        return JsonResponse(response)
    return HttpResponse("bad request")
