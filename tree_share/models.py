from django.db import models
from django.conf import settings

from family_tree.models import FamilyTree


class TreeShare(models.Model):
    tree = models.ForeignKey(FamilyTree, on_delete=models.CASCADE, related_name='shares_with')
    shared_with = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    ACCESS_CHOICES = [
        ('view', 'View'),
        ('edit', 'Edit'),
    ]
    access_type = models.CharField(max_length=5, choices=ACCESS_CHOICES, default='view')
    shared_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tree.name} shared with {self.shared_with.username}"
