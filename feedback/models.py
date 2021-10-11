from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

class Author(models.Model): # add more fields like profile picture, etc. integrate with cloudinary
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={
            'pk': self.pk
        })

class Theme_label(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name


class NPS(models.Model): # needs review, update types, add more fields, later connect this to booking model
    loaded_in_db_timestamp = models.DateTimeField(auto_now_add=True)
    age = models.CharField(max_length=100, null=True, blank=True)
    age_bucket = models.CharField(max_length=100, null=True, blank=True)
    airlines = models.CharField(max_length=100, null=True, blank=True)
    airlines_names = models.CharField(max_length=100, null=True, blank=True)
    bags = models.CharField(max_length=100, null=True, blank=True)
    bags_bucket = models.CharField(max_length=100, null=True, blank=True)
    haul = models.CharField(max_length=100, null=True, blank=True)
    bid = models.CharField(max_length=100, null=True, blank=True)
    comment = models.CharField(max_length=100, null=True, blank=True)
    comment_original = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    customer_nationality = models.CharField(max_length=100, null=True, blank=True)
    fare_type_name = models.CharField(max_length=100, null=True, blank=True)
    has_score = models.BooleanField()
    review_id = models.CharField(max_length=250, null=True, blank=True)
    nomad = models.BooleanField()
    partner = models.CharField(max_length=100, null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    score_category = models.CharField(max_length=100, null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    theme_label = models.ManyToManyField(Theme_label, related_name='theme_labels', blank=True)

   
    def __str__(self):
        return self.bid

    # add here redirect links args, kwargs    


# create CSAT model here and connect it to helpcentre model(s)