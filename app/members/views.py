from django.shortcuts import render, get_object_or_404, redirect

from .forms import UserForm
from .models import User

# Create your views here.

def member_list(request):
    users = User.objects.all()
    content = {
        'users': users
    }
    return render(request, 'members/member_list.html', content)

def member_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    content = {
        'user': user
    }
    return render(request, 'members/member_detail.html', content)

def member_new(request):
    # form = UserForm()
    # content = {
    #     'form': form
    # }
    # return render(request, 'members/member_edit.html', content)

    if request.method == 'POST':
        form = UserForm(request.POST)


        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('member_detail', pk=user.pk)
    else:
        form = UserForm()

    content = {
        'form': form
    }

    return render(request, 'members/member_edit.html', content)