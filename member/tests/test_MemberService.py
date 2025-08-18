from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import date
from member.models import Member
from family_tree.models import FamilyTree, FamilyInfo

User = get_user_model()


class MemberServiceTest(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(username="testuser", password="password")


        self.root_family = FamilyInfo.objects.create(
            tribe="Root Tribe",
            foods="Rice, Yam, Beans",
            origin="West Africa",
            traditions="Marriage ceremonies, Festivals",
            additional_notes="Test root family setup"
        )


        self.tree = FamilyTree.objects.create(
            owner=self.user,
            name="Fake Tree",
            root_family=self.root_family
        )


        self.member = Member.objects.create(
            tree=self.tree,
            name="John Doe",
            birth_date=date(1995, 5, 20)
        )

    def test_member_creation(self):
        self.assertEqual(self.member.name, "John Doe")
        self.assertEqual(self.member.tree, self.tree)
        self.assertEqual(self.member.birth_date, date(1995, 5, 20))
