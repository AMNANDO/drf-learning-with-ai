# from django.test import TestCase
# from django.urls import reverse
# from api.models import Profile
# from django.contrib.auth.models import User
# from rest_framework.test import APITestCase
# from rest_framework import status
# # Create your tests here.
# class ProfileTest(APITestCase):
#
#
#     def test_create_profile_authenticated(self):
#         user = User.objects.create_user(
#             username="testuser",
#             password="1234"
#         )
#
#         self.client.force_authenticate(user=user)
#
#         response = self.client.post(
#             "/api/profile/",
#             {
#                 "name": "Ali",
#                 "age": 20,
#                 "email": "alimoh@gmail.com",
#             },
#             format="json"
#         )
#
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         print(response.status_code)
#         print(response.data)
#
#     def test_retrieve_inactive_profile(self):
#         user = User.objects.create_user(
#             username="testuser",
#             password="1234"
#         )
#         self.client.force_authenticate(user=user)
#
#         profile = Profile.objects.create(
#             name="Reza",
#             age=40,
#             isActive=False
#         )
#
#         url = reverse('profile-detail', args=[profile.id])
#         response = self.client.get(url)
#
#         self.assertEqual(response.status_code, 403)
#         self.assertFalse(response.data['success'])
#         self.assertEqual(
#             response.data['error']['code'],
#             'inactive_profile'
#         )
#         print(response.status_code)
#         print(response.data)
#
#     def test_create_invalid_profile(self):
#         user = User.objects.create_user(
#             username="testuser",
#             password="1234"
#         )
#         self.client.force_authenticate(user=user)
#
#         url = reverse('profile-list')
#         data = {"name": "", "age": 10}
#
#
#         response = self.client.post(url, data)
#
#         self.assertEqual(response.status_code, 400)
#         self.assertFalse(response.data['success'])
#         print(response.status_code)
#         print(response.data)
#
from django.urls import reverse
from api.models import Profile
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

class ProfileTest(APITestCase):

    def setUp(self):
        # ایجاد یک کاربر مشترک برای همه تست‌ها
        self.user = User.objects.create_user(username="testuser", password="1234")
        self.client.force_authenticate(user=self.user)

    def test_create_profile_authenticated(self):
        # تست ایجاد پروفایل با user لاگین‌شده
        response = self.client.post(
            "/api/profile/",
            {
                "name": "Ali",
                "age": 20,
                "email": "alimoh@gmail.com",
            },
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print('test_create_profile_authenticated')
        print(response.status_code)
        print(response.data)

    def test_retrieve_inactive_profile(self):
        # ایجاد پروفایل inactive با user ست شده
        profile = Profile.objects.create(
            user=self.user,
            name="Reza",
            age=40,
            email="reza@gmail.com",
            isActive=False
        )

        url = reverse('profile-detail', args=[profile.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code,403)
        self.assertFalse(response.data['success'])
        self.assertEqual(
            response.data['error']['code'],
            'inActive Profile'
        )
        print('test_retrieve_inactive_profile')
        print(response.status_code)
        print(response.data)

    def test_create_invalid_profile(self):
        # تست ارسال داده نامعتبر
        url = reverse('profile-list')
        data = {"name": "", "age": 10}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 400)
        self.assertFalse(response.data['success'])
        print("test_create_invalid_profile")
        print(response.status_code)
        print(response.data)
