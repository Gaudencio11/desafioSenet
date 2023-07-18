from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User

from loja_moedas.forms import CoinForm, UpdatePerfilForm, UpdatePerfilPhotoForm
from .models import Coin, UserProfilePhoto

def homeView(request): 
    if not request.user.is_authenticated:
        return redirect('/') 
    
    coinList = Coin.objects.all()
    if coinList:
         print("não vazia")

    return render(request, 'home.html', {"coinList":coinList})


def editarPerfilView(request):
    if not request.user.is_authenticated:
        return redirect('/')

    #user profile form
    userLogged = get_object_or_404(User, pk = request.user.id)

    form = UpdatePerfilForm(request.POST or None, instance= userLogged)
    if form.is_valid():
        form.save()
        return redirect("editarPerfil")

    #Image form
    try:
        image = UserProfilePhoto.objects.get(user = request.user.id)
    except UserProfilePhoto.DoesNotExist:
        image = None
    
    if image:
        image_form = UpdatePerfilPhotoForm(request.POST or None,request.FILES or None, instance= image)
        print("entrou if")
        if image_form.is_valid():
            image_form.save()
            return redirect("editarPerfil")
    else:
        image_form = UpdatePerfilPhotoForm(request.FILES)
        if image_form.is_valid():
            obj = image_form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect("editarPerfil")


    return render(request, 'editarPerfil.html', {'form':form,  'image_form': image_form, 'image':image})

def createCoinPostView(request):
    if not request.user.is_authenticated:
            return redirect('/')
    
    form = CoinForm(request.POST,request.FILES)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect("home")
    return render(request, 'createCoinPost.html', {'form':form})

def detailCoinPostView(request, slug):
    if not request.user.is_authenticated:
            return redirect('/')
    
    coinPost = get_object_or_404(Coin, pk = slug)
    return render(request, 'detailCoinPost.html', {'coin':coinPost})

""" 

 """
