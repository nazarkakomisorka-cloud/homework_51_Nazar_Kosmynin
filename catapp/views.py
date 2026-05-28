from django.shortcuts import render, redirect
from .cat import Cat


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if name:
            cat = Cat(name)
            request.session['cat'] = cat.to_dict()
            return redirect('cat_page')
    return render(request, 'catapp/index.html')


def cat_page(request):
    cat_data = request.session.get('cat')
    if not cat_data:
        return redirect('index')

    cat = Cat.from_dict(cat_data)

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'feed':
            cat.feed()
        elif action == 'play':
            cat.play()
        elif action == 'sleep':
            cat.sleep()
        request.session['cat'] = cat.to_dict()

    return render(request, 'catapp/cat.html', {
        'cat': cat,
        'avatar': cat.get_avatar(),
    })
