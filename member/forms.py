from django import  forms

from member.models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name','birth_date','death_date','relation','photo','spouse','marital_status']
        widgets ={
            'birth_date':forms.DateInput(attrs={'type':'date'}),
            'death_date':forms.DateInput(attrs={'type':'date'}),
        }