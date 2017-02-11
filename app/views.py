import xlwt
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView

from app.forms import ProfileForm


def home(request):
    return render(request, 'app/home.html')


def user_select(request):
    return render(request, 'app/user_select.html', {'users': User.objects.all()})


def export_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Username', 'Birthday', 'Eligible', 'Random Number', 'BizzFuzz']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    users = User.objects.all()
    for user in users:
        row_num += 1
        row = (
            user.username,
            user.profile.birthday.strftime('%d/%m/%Y'),
            user.profile.eligible,
            user.profile.random_number,
            user.profile.bizz_fuzz,
        )
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


@transaction.atomic
def user_edit(request, pk):
    user = User.objects.get(pk=pk)

    if request.method == 'POST':
        user_form = UserChangeForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, instance=user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, 'User {} updated successfully'.format(user.username))
            return redirect('user_list')
    else:
        user_form = UserChangeForm(instance=user)
        profile_form = ProfileForm(instance=user.profile)

    return render(request, 'auth/user_edit_form.html', {
        'form': user_form,
        'profile_form': profile_form,
    })


class UserCreate(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserCreationForm
    success_message = 'User %(username)s created successfully'
    success_url = reverse_lazy('user_list')
    template_name = 'auth/user_add_form.html'


class UserDelete(SuccessMessageMixin, DeleteView):
    model = User
    success_message = 'User %(username)s deleted successfully'
    success_url = reverse_lazy('user_list')

    def delete(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        messages.success(self.request, self.success_message % {'username': user.username})
        return super(UserDelete, self).delete(request, *args, **kwargs)
