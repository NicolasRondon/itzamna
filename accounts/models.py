from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, username, password=None, is_staff=False,
                    is_admin=False, is_active=True):

        if not email:
            raise ValueError("El usuario debe tener un email")

        if not first_name:
            raise ValueError("El usuario debe tener un nombre")

        if not password:
            raise ValueError("El usuario debe tener una contraseña")

        if not last_name:
            raise ValueError("El usuario debe tener un apellido")

        if not username:
            raise ValueError("El usuario debe tener un nombre de usuario")

        user_obj = self.model(
            email=self.normalize_email(email)
        )

        user_obj.first_name = first_name
        user_obj.last_name = last_name
        user_obj.username = username
        user_obj.staff = is_staff
        user_obj.is_superuser = is_admin
        user_obj.active = is_active
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, first_name, last_name, username, password=None):
        user = self.create_user(
            email,
            first_name,
            last_name,
            username,
            is_staff=True,
            password=password,
        )
        return user

    def create_superuser(self, email, first_name, last_name, username, password=None):
        user = self.create_user(
            email,
            first_name,
            last_name,
            username,
            is_staff=True,
            is_admin=True,
            password=password,
        )
        return user


class User(AbstractBaseUser, PermissionsMixin):
    # Lista de cohortes de Academlo

    COURSE_START = [
        ('J2019', 'Julio 2019'),
        ('E2020', 'Enero 2020'),
        ('M2020', 'Mayo 2020'),
    ]

    GENDER = [
        ('M', 'Hombre'),
        ('F', 'Mujer')
    ]

    # Campos de usuario
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    username = models.CharField(max_length=200, blank=False)
    email = models.EmailField(unique=True, max_length=300, blank=False)
    course = models.CharField(choices=COURSE_START, max_length=5)
    gender = models.CharField(choices=GENDER, max_length=1)
    active = models.BooleanField()
    staff = models.BooleanField()
    is_superuser = models.BooleanField()
    joined_date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    objects = UserManager()


    def get_full_name(self):
        return self.first_name + self.last_name

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
