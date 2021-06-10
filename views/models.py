from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class View(models.Model):
    # The text content of the View.
    content = models.CharField(max_length=560, null=False, blank=False)

    # The user that created the View.
    user = models.ForeignKey(User, related_name='+', null=True, blank=True, on_delete=models.SET_NULL)

    # The time the view was posted.
    created_at = models.DateTimeField(default=timezone.now)

    # Whether or not this view has been flagged by the content moderator.
    flagged = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('view_detail', kwargs={'pk': self.pk})


class ViewReview(models.Model):
    # The view this model is linked to.
    view = models.OneToOneField(View, on_delete=models.CASCADE, null=False, related_name='view_review')

    category_one_score = models.DecimalField(max_digits=11, decimal_places=10)

    category_two_score = models.DecimalField(max_digits=11, decimal_places=10)

    category_three_score = models.DecimalField(max_digits=11, decimal_places=10)

    def __str__(self):
        return f'[{self.view}]({self.category_one_score}, {self.category_two_score}, {self.category_three_score})'


class Term(models.Model):
    # The ViewReview model that is attached to this term.
    view_review = models.ForeignKey(ViewReview, on_delete=models.CASCADE, null=False, related_name='terms')

    term = models.CharField(max_length=560)

    def __str__(self):
        return f'{self.term}'
