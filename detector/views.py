from django.shortcuts import render, redirect
from .models import News

# Dummy logic (you can replace with ML later)
def check_fake_news(text):
    fake_keywords = ["fake", "fraud", "scam", "rumor"]
    for word in fake_keywords:
        if word in text.lower():
            return "Fake"
    return "Real"

def index(request):
    return render(request, 'detector/index.html')

def detect(request):
    if request.method == "POST":
        content = request.POST.get('content')

        result = check_fake_news(content)

        # Save to DB
        News.objects.create(content=content, result=result)

        return render(request, 'detector/result.html', {
            'content': content,
            'result': result
        })

    return redirect('/')