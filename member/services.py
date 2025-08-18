from datetime import date
from typing import Optional, List

from django.shortcuts import get_object_or_404
from pydantic import ValidationError

from family_info.models import FamilyInfo
from member.models import Member


def add_member_to_family(
        family: FamilyInfo,
        name: str,
        birth_date : date,
        death_date : date,
        relation :Optional[str]='',
        photo = None,
        marital_status: str='single',
        spouse : Optional[Member]=None,
        parent: Optional[Member]=None,
)-> Member:
    if Member is None:
        raise ValidationError('Member object has not been created')

    if birth_date > date.today():
        raise ValidationError("Birth date must be before today or today")

    member = Member(
        tree=family,
        name=name,
        birth_date=birth_date,
        death_date=death_date,
        relation=relation,
        photo=photo,
        marital_status=marital_status,
        spouse=spouse,
        parent=parent,
    )
    member.save()
    return member

def get_family_members(family: FamilyInfo) :
    return  Member.objects.filter(family=family)

def update_member(number_id, **kwargs):
    member = get_object_or_404(Member, id=number_id)
    for field, value in kwargs.items() :
        setattr(member, field, value)
        member.save()
        return member
def delete_member(number_id) :
    member = get_object_or_404(Member, id=number_id)
    member.delete()
    return True