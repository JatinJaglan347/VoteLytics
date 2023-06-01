from django.db import models

class Image(models.Model):
    backgroundimg = models.ImageField(upload_to="backgroundimg")
    brandtitle = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    discription = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="myimage")
    votetitle = models.CharField(max_length=200)
    candidate1 = models.ImageField(upload_to="candidate1")
    name_candidate1 = models.CharField(max_length=200)
    candidate2 = models.ImageField(upload_to="candidate2")
    name_candidate2 = models.CharField(max_length=200)
    candidate3 = models.ImageField(upload_to="candidate3")
    name_candidate3 = models.CharField(max_length=200)
    candidate4 = models.ImageField(upload_to="candidate4")
    name_candidate4 = models.CharField(max_length=200)
    candidate5 = models.ImageField(upload_to="candidate5")
    name_candidate5 = models.CharField(max_length=200)
    candidate6 = models.ImageField(upload_to="candidate6")
    name_candidate6 = models.CharField(max_length=200)
    footerimg = models.ImageField(upload_to="footerimg")
    footerbg = models.ImageField(upload_to="footerimg")
    instagramlink = models.CharField(max_length=200)
    facebooklink = models.CharField(max_length=200)
    youtubelink = models.CharField(max_length=200)
    twitterlink = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    
    
    
    
    
from django.db import models

class Vote(models.Model):
    option1_votes = models.PositiveIntegerField(default=0)
    option2_votes = models.PositiveIntegerField(default=0)
    option3_votes = models.PositiveIntegerField(default=0)
    option4_votes = models.PositiveIntegerField(default=0)
    option5_votes = models.PositiveIntegerField(default=0)
    option6_votes = models.PositiveIntegerField(default=0)
    total_votes = models.PositiveIntegerField(default=0)
    option1_percentage = models.FloatField(default=0)
    option2_percentage = models.FloatField(default=0)
    option3_percentage = models.FloatField(default=0)
    option4_percentage = models.FloatField(default=0)
    option5_percentage = models.FloatField(default=0)
    option6_percentage = models.FloatField(default=0)



