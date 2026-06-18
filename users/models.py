from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email обязателен")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Payment(models.Model):
    PAYMENT_METHODS = (
        ("cash", "Наличные"),
        ("transfer", "Перевод"),
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="payments"
    )

    course = models.ForeignKey(
        "materials.Course",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    lesson = models.ForeignKey(
        "materials.Lesson",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    date = models.DateTimeField(auto_now_add=True)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    method = models.CharField(max_length=20, choices=PAYMENT_METHODS)

    def __str__(self):
        return f"{self.user.email} - {self.amount}"

