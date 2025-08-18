from django.db import models
from django.conf import settings
from family_info.models import FamilyInfo

class FamilyTree(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='trees')
    name = models.CharField(max_length=100)
    root_family = models.OneToOneField(FamilyInfo, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
