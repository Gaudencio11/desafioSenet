
from allauth.account.forms import SignupForm
from django import forms
from .models import *
from django.contrib.auth.models import User

from allauth.account  import views


           
class CustomSignupForm(SignupForm):
    #Usamos aqui a coluna 'lastname' do allauth para introduzirmos o cpf do usuário
    #Ainda estamos no processo de entender como realizar a validação desse cpf a partir de um bd


    first_name = forms.CharField(max_length=200, label='Nome completo')
 
    def save(self, request):

        user = super(CustomSignupForm, self).save(request)

        return user
    
class UpdatePerfilForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name']
    
class UpdatePerfilPhotoForm(forms.ModelForm):

    class Meta:
        model = UserProfilePhoto
        fields = ['image']

class CoinForm(forms.ModelForm):

    class Meta:
        model = Coin
        fields = ['title','image','description','price']
