from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import  MinValueValidator
class Goal(models.Model):
    content = models.TextField(max_length=255)  # Use CharField instead of TextField for shorter content to save space.
    start_time = models.DateTimeField()
    completion_time = models.DateTimeField()
    cash_amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    user_email = models.EmailField()
    friend_email = models.EmailField(blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['start_time', 'completion_time']),  # Adding an index for faster queries
            models.Index(fields=['completion_time']),  # Adding an index for faster queries
            models.Index(fields=['user_email']),  # Indexing user_email for frequent lookups
        ]
        ordering = ['completion_time']  # Default ordering by completion time

    def __str__(self):
        return self.content

    def clean(self):
        # Ensure the completion_time is greater than the start_time
        if self.completion_time <= self.start_time:
            raise ValidationError('Completion time must be later than the start time.')