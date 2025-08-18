from django.db import models
from family_tree.models import FamilyTree

class Member(models.Model):
    MARITAL_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
    ]

    tree = models.ForeignKey(FamilyTree, on_delete=models.CASCADE)
    # related_name='members'
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    death_date = models.DateField(blank=True, null=True)
    relation = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='member_photos/', blank=True, null=True)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, default='single')
    spouse = models.OneToOneField('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='partner')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='children')

    def __str__(self):
        return f"{self.name} ({self.birth_date})"
