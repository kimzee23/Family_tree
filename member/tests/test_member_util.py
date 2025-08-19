from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist

from family_info.models import FamilyInfo
from member.models import Member
from member.services import get_family_members


class MemberServiceTests(TestCase):

    def setUp(self):
        self.family = FamilyInfo.objects.create(
            tribe="Yoruba Tribe",
            foods="Rice, Yam",
            origin="Nigeria",
            traditions="Traditional ceremonies",
            additional_notes="Some notes"
        )


        self.member1 = Member.objects.create(
            name="John Ada",
            birth_date="1995-05-12",
            family_info=self.family,
        )
        self.member2 = Member.objects.create(
            name="micheal",
            birth_date="1998-09-20",
            family_info=self.family,
        )

    def test_get_family_members(self):
        members = get_family_members(self.family.id)  #expects family_id
        self.assertIn(self.member1, members)
        self.assertIn(self.member2, members)
        self.assertEqual(members.count(), 2)

    def test_update_member(self):
        self.member1.name = "John Updated"
        self.member1.save()

        updated_member = Member.objects.get(id=self.member1.id)
        self.assertEqual(updated_member.name, "John Updated")

    def test_delete_member(self):
        member_id = self.member2.id
        self.member2.delete()

        with self.assertRaises(ObjectDoesNotExist):
            Member.objects.get(id=member_id)
