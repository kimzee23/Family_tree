from datetime import datetime, timedelta
from django.test import TestCase

from User.models import CustomUser
from family_tree.models import FamilyTree
from member.services import add_member_to_family
from family_info.models import FamilyInfo


class TestMemberService(TestCase):   # <-- starts with "Test"
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="gazar",
            password='password',
            email="gzar@gmail.com",
            phone_number='080123456678'
        )
        self.root_family = FamilyInfo.objects.create(
            tribe="Test Tribe",
            origin="Test Origin"
        )
        self.tree = FamilyTree.objects.create(
            owner=self.user,
            name="fake tree",
            root_family=self.root_family
        )

    def test_add_member_success(self):   # <-- starts with "test_"
        member = add_member_to_family(
            family=self.tree,
            name="Ade",
            birth_date=datetime.today().date() - timedelta(days=368),
            death_date=None
        )
        self.assertEqual(member.name, "Ade")
        self.assertEqual(member.tree, self.tree)
        self.assertIsNone(member.death_date)
