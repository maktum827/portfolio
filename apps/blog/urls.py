from django.urls import path
from apps.blog import views
from apps.blog.views import articles
from django.contrib.auth import views as auth_views

# importing views  
from apps.blog.views import SignupForm  ,ProfileUpdateView, ProfileView


urlpatterns = [
    path('', views.articles, name='articles'),
    path('register/', SignupForm.as_view(), name='register'),
    path('contact/', views.contact, name='contact'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),

    # login logout
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),name='logout'),

     # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='blog/password-reset/password_reset.html',
             subject_template_name='blog/password-reset/password_reset_subject.txt',
             email_template_name='blog/password-reset/password_reset_email.html',
             success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='blog/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='blog/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='blog/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),

]