from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class CustomUserManager(BaseUserManager):
    def create_user(self, identifier, date_of_birth,
                    email, is_a_chicken, password=None):

        if not identifier:
            raise ValueError('Users must have a name.')

        user = self.model(
            identifier=identifier,
            date_of_birth=date_of_birth,
            email=email,
            is_a_chicken=is_a_chicken,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, identifier, date_of_birth,
                         email, is_a_chicken, password):
        user = self.create_user(
            identifier,
            password=password,
            date_of_birth=date_of_birth,
            email=email,
            is_a_chicken=is_a_chicken,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    identifier = models.CharField(max_length=40, unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_a_chicken = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'identifier'
    REQUIRED_FIELDS = ['date_of_birth', 'email']

    def get_full_name(self):
        return self.identifier

    def get_short_name(self):
        return self.identifier

    def __unicode__(self):
        return self.identifier

    def has_perm(self, perm, obj=None):
        "Does this user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
# Create your models here.
