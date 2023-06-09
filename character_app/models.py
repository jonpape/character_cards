from django.db import models

# Character Card model
class Character(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    hire_date = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='images/')
    lifestyle_image = models.ImageField(upload_to='images/')
    character_image = models.ImageField(upload_to='images/')
    superpower = models.CharField(max_length=300)
    skills = models.CharField(max_length=300)
    favorite_character = models.CharField(max_length=300)
    motivation = models.CharField(max_length=300)
    quote = models.CharField(max_length=300)
    appreciated_for = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.created_at}"