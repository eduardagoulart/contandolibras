from django.shortcuts import render,  redirect

from .forms import SubscriptionForm
from django.templatetags.static import static


def home(request):
    return render(request, 'core/index.html')


def contato(request):
    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('success')
    else:
        form = SubscriptionForm()
    return render(request, 'core/contato.html', {'form': form})


def contos(request):
    return render(request, 'core/contos.html')


def jogos(request):
    return render(request, 'core/jogos.html')


def memoria(request):
    images = [
        {'src': static('img/%s.gif' % str(i)), 'id': i % 8}
        for i in range(0, 16)
    ]
    return render(request, 'core/memoria.html', {'images': images})


def desenhos(request):
    return render(request, 'core/desenhos.html')


def success(request):
    return render(request, 'core/success.html')