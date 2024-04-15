from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import DetailView, View
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from .models import Cart,Customer, Product
from .forms import DiseaseDetectionForm
from .forms import ContactForm, SignupForm, LoginForm, CustomerProfileForm


def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = f"New message from {name}"
            body = f"Email: {email}\n\nMessage: {message}"
            sender_email = settings.EMAIL_HOST_USER
            recipient_email = 'projectmushroom2@gmail.com'
            try:
                send_mail(subject, body, sender_email, [recipient_email])
                messages.success(request, 'Your message has been sent. We will get back to you soon!')
            except Exception:
                messages.error(request, 'Sorry, there was an error while sending your message. Please try again later.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'app/contact.html', {'form': form})

class CategoryView(View):
    def get(self, request, val):
        category = val
        products = Product.objects.filter(category=category)
        return render(request, 'app/category.html', {'products': products, 'category': category})

class ProductDetailView(DetailView):
    model = Product
    template_name = 'app/product_detail.html' 
    context_object_name = 'product'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return Product.objects.get(pk=pk)

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, 'Signup failed. Invalid user data.')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        user = request.user
        if hasattr(user, 'customer_set'):
            profile = user.customer_set.first()
            form = CustomerProfileForm(instance=profile)
            return render(request, 'app/profile.html', {'profile': profile, 'form': form})
        else:
            form = CustomerProfileForm()
            return render(request, 'app/profile.html', {'form': form})

    def post(self, request):
        user = request.user
        profile = user.customer_set.first()
        form = CustomerProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
        else:
            messages.error(request, 'Profile update failed. Invalid data')
            return render(request, 'app/profile.html', {'form': form})

def add_to_cart(request):
    if request.method == 'POST':
        user = request.user
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        Cart.objects.create(user=user, product=product)
        return redirect('/cart')
    else:
        # Handle GET request gracefully (optional)
        return HttpResponseNotAllowed(['POST'])
def show_cart(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    return render(request, 'app/addtocart.html', {'cart_items': cart_items})

def detect_disease(request):
    if request.method == 'POST':
        form = DiseaseDetectionForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle image processing and disease detection here
            # For example:
            uploaded_image = form.cleaned_data['image']
            # Process the image and get the disease detection result
            # Then display the result to the user
    else:
        form = DiseaseDetectionForm()
    return render(request, 'app/detectdisease.html', {'form': form})
 
    