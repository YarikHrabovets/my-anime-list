from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.utils.text import slugify
from django_countries.fields import CountryField

import os
from PIL import Image

from .managers import AnilistUserManager


class AnilistUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AnilistUserManager()

    class Meta:
        verbose_name = 'Anilist User'
        verbose_name_plural = 'Anilist Users'

    def __str__(self):
        return self.email


class Profile(models.Model):
    GENDER_CHOICES = [
        ('NONE', 'none'),
        ('MALE', 'male'),
        ('FEMALE', 'female')
    ]
    user = models.OneToOneField(AnilistUser, on_delete=models.CASCADE)
    profile_pic = models.ImageField('Profile picture', null=True, blank=True, upload_to='profile_pics')
    bio = models.TextField('Biography', default='No bio data', max_length=400)
    gender = models.CharField('Gender', max_length=6, choices=GENDER_CHOICES, default='NONE')
    country = CountryField(blank_label='(select country)')
    friends = models.ManyToManyField('self')
    slug = models.SlugField('URL', unique=True, max_length=255)

    class Meta:
        verbose_name = 'Anilist Profile'
        verbose_name_plural = 'Anilist Profiles'

    def __str__(self):
        return f'Profile of the {self.user}'

    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = Profile.objects.get(pk=self.pk)

            if old_instance.profile_pic != self.profile_pic:
                if old_instance.profile_pic and os.path.isfile(old_instance.profile_pic.path):
                    os.remove(old_instance.profile_pic.path)

        self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

        if self.profile_pic:
            img = Image.open(self.profile_pic.path)
            img = img.resize((300, 300), Image.LANCZOS)
            img.save(self.profile_pic.path, quality=100)
            img.close()

    def get_absolute_url(self):
        return reverse('profile', kwargs={'slug': self.slug})
