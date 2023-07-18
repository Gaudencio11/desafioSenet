
from django.urls import path, re_path
from .views import detailCoinPostView, createCoinPostView, homeView, editarPerfilView

from allauth.account import views as allauthViews


#Criar app pra isso
urlpatterns = [
    path('', allauthViews.login, name='account_login'),
    path('logout/', allauthViews.logout, name='logout'),
    path('signup/', allauthViews.signup, name='account_signup'),

    #esse serve para abrir a página dizendo que seu email de verificação foi enviado (o mais simples)
    path(
        "confirm-email/",
        allauthViews.email_verification_sent,
        name="account_email_verification_sent",
    ),
    #esse serve para realizar o envio do email de confirmação para o usuário
    re_path(
        r"^confirm-email/(?P<key>[-:\w]+)/$",
        allauthViews.confirm_email,
        name="account_confirm_email",
    ),

    #Reset password
    path("redefinir-senha/", allauthViews.password_reset, name="account_reset_password"
    ),
    path(
        "password/reset/done/",
        allauthViews.password_reset_done,
        name="account_reset_password_done",
    ),
    re_path(
        r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        allauthViews.password_reset_from_key,
        name="account_reset_password_from_key",),
    path(
        "password/reset/key/done/",
        allauthViews.password_reset_from_key_done,
        name="account_reset_password_from_key_done",
    ),

    #change password
    path("alterar-senha/", allauthViews.password_change, name="account_change_password"),
    path("alterar-senha/", allauthViews.password_change, name="account_change_password"),


    #app
    path('home/', homeView, name='home'),
    path('editarPerfil/', editarPerfilView, name='editarPerfil'),
    path('criar-postagem/', createCoinPostView, name='createCoinPost'),
    path('detalhes-moeda/<slug:slug>', detailCoinPostView, name='detailCoinPost'),
]