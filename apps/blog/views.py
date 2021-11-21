from apps.blog.models import Post, Contact
from django.shortcuts import redirect, render
from django.views.generic import TemplateView ,CreateView 
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignupForm, UserForm, ProfileForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.
class HomeView(TemplateView):
    template_name = 'blog/home.html'

def articles(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/articles.html', context)
    
# for contact
def contact(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']

        mycontact = Contact(name = name, email = email, messages = text)
        mycontact.save()
        
        messages.success(request, 'Your messages is successfully sent')
        return redirect('/')
    return render(request, 'blog/contact.html')


class ProfileView(TemplateView):
    template_name = 'blog/profile.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/dashboard.html'
    login_url = reverse_lazy('home')

class SignupForm(CreateView):
    form_class = SignupForm
    # redirecting 
    success_url = reverse_lazy('login')  
    template_name = 'blog/register.html'

class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'blog/profile-update.html'

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.error(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

