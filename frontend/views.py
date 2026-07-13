from django.shortcuts import render, redirect, get_object_or_404
from backend.models import OrderModel
from accounts.models import *
from frontend.forms import  OrderForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def custom_404(request, exception):
    return render(request, "404.html", status=404)

# Create your views here.
def home_views(request):
    return render(request,'index.html')

# Create
@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)

        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            return redirect('client_order_list')
    else:
        form = OrderForm()

    return render(request, 'create_order.html', {'form': form})


@login_required
def client_delete_order(request, pk):
    client_order = get_object_or_404(OrderModel, pk=pk)

    if request.method == 'POST':
        client_order.delete()
        return redirect('client_order_list')

    return render(request, 'client_delete.html', {'client_order': client_order})


# Read All
@login_required
def client_order_list(request):
    client_oders = OrderModel.objects.filter(user=request.user).order_by('-id')
    return render(request, 'client_list.html', {'client_oders': client_oders})
