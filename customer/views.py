from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView, View
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import BasicUserInfoForm, BasicCustomerForm
from django.contrib import messages


class ProfileRedirectView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('customer:profile')


class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_form = BasicUserInfoForm(instance=self.request.user)
        customer_form = BasicCustomerForm(instance=self.request.user.customer)
        return render(
            self.request, 'customer/profile.html', {
                'user_form': user_form,
                'customer_form': customer_form
            }
        )

    def post(self, request, *args, **kwargs):
        user_form = BasicUserInfoForm(
            self.request.POST, instance=self.request.user
        )
        customer_form = BasicCustomerForm(
            self.request.POST, self.request.FILES, instance=self.request.user.customer
        )
        if user_form.is_valid() and customer_form.is_valid():
            user_form.save()
            customer_form.save()
            messages.success(self.request, 'Profile details updated.')
            return redirect('customer:profile')
