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
    skill_1 = models.CharField(max_length=300)
    skill_2 = models.CharField(max_length=300, default='unknown')
    skill_3 = models.CharField(max_length=300, default='unknown')
    favorite_character = models.CharField(max_length=300)
    motivation = models.CharField(max_length=300)
    quote = models.CharField(max_length=300)
    appreciation = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.position} - {self.department}"