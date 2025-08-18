from django.db import models

class FamilyInfo(models.Model):
    tribe = models.CharField(max_length=100)
    foods = models.TextField(blank=True)
    origin = models.CharField(max_length=200,blank=True)
    traditions = models.TextField(blank=True)
    banner_photo = models.ImageField(upload_to='family_banners/', blank=True,null=True)
    additional_notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.tribe} family information"