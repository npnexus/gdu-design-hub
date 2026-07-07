from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import OrderModel
from .forms import AdminOrderForm
from accounts.models import CustomUser

@login_required
def dashboard(request):
    orders = OrderModel.objects.filter(user=request.user)

    context = {
        'orders': orders,
        'total_orders': orders.count(),
        'pending_orders': orders.filter(status='pending').count(),
        'processing_orders': orders.filter(status='processing').count(),
        'completed_orders': orders.filter(status='completed').count(),
    }

    return render(request, 'dash.html', context)


@login_required
def order_list(request):
    users = CustomUser.objects.all().order_by('-id')
    orders = OrderModel.objects.select_related('user').order_by('-id')

    context = {
        'users': users,
        'orders': orders,
    }

    return render(request, 'list.html', context)


@login_required
def order_detail(request, pk):
    order = get_object_or_404(OrderModel, pk=pk)

    return render(request, 'detail.html', {
        'order': order
    })


@login_required
def update_order(request, pk):
    order = get_object_or_404(OrderModel, pk=pk)

    if request.method == 'POST':
        form = AdminOrderForm(
            request.POST,
            request.FILES,
            instance=order
        )

        if form.is_valid():
            form.save()
            return redirect('order_list')

    else:
        form = AdminOrderForm(instance=order)

    return render(request, 'update.html', {
        'form': form,
        'order': order
    })


@login_required
def delete_order(request, pk):
    order = get_object_or_404(OrderModel, pk=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('order_list')

    return render(request, 'delete.html', {
        'order': order
    })