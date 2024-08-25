from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import CreateView
from .forms import GoalForm
from .models import Goal
from django.core.mail import send_mail
from .utils import send_goal_emails
class GoalCreateView(CreateView):
    model = Goal
    form_class = GoalForm
    template_name = 'goal_form.html'

    def form_valid(self, form):
        # Call the parent class's form_valid method
        response = super().form_valid(form)
        
        # Add a success message
        messages.success(self.request, "Bạn đã tạo thử thách thành công, vui lòng kiểm tra email của bạn.")
        user_email = form.cleaned_data['user_email']
        friend_email = form.cleaned_data['friend_email']
        goal_content = form.cleaned_data['content']

        # Send email to user
        send_goal_emails(user_email, friend_email, goal_content)
        # Redirect to the success URL
        return response

    def get_success_url(self):
        # Redirect to the same page or any other URL after success
        return reverse('goal-create')  # Update 'goal-create' to the name of your view's URL
