from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .models import CustomUser
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import CustomUserCreationForm
from .tokens import email_verification_token

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)

            email_subject = "Verify Your Email"

            message = render_to_string(
                'verify_email.html',
                {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': email_verification_token.make_token(user),
                }
            )

            email = EmailMessage(
                email_subject,
                message,
                to=[user.email]
            )

            email.send()

            return render(request, 'email_sent.html')

    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


def verify_email(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user and email_verification_token.check_token(user, token):
        user.is_active = True
        user.email_verified = True
        user.save(update_fields=['is_active', 'email_verified'])

        login(request, user)
        messages.success(request, "Email verified successfully.")
        return redirect('home')

    messages.error(request, "Invalid verification link.")
    return redirect('register')


# Login
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            if not user.is_active:
                messages.error(
                    request,
                    "Please verify your email before logging in."
                )
                return redirect("login")

            login(request, user)
            messages.success(request, "Login successful.")
            return redirect("home")

        messages.error(request, "Invalid username or password.")

    return render(request, "login.html")


# Logout
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("login")
