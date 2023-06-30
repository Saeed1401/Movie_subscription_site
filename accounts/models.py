from django.contrib.auth.models import AbstractBaseUser
from persiantools.jdatetime import JalaliDate
from django.utils import timezone
from .managers import UserManager
from django.db import models


class Subscription(models.Model):
    pass

class User(AbstractBaseUser):
    LANGUAGE_CHOICES = (
        ('Persian', "فارسی"),		
        ('English', "انگلیسی"),	
        ('German', "آلمانی"),
    )
    GENDER_CHOICES=(
        ('man',"مرد"),
        ('woman',"زن"),
    )
    email = models.EmailField('آدرس ایمیل', max_length=255)
    full_name = models.CharField('نام و نام خانوادگی', max_length=55)
    image = models.ImageField('تصویر', upload_to='images/users', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="جنسیت",null=True, blank=True)
    birth = models.DateField('تاریخ تولد',null=True, blank=True)
    language=models.CharField(max_length=10, choices=LANGUAGE_CHOICES, verbose_name="زبان",null=True, blank=True)
    Subscription_plan=models.ForeignKey(Subscription, related_name="Subscription",on_delete=models.CASCADE,default=None, blank=True)

    date_joined = models.DateTimeField('تاریخ عضویت', auto_now_add=True)
    is_active = models.BooleanField('فعال', default=True)
    is_staff = models.BooleanField('کارمند', default=False)

    is_superuser = models.BooleanField('ادمین', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["full_name"]

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربرها'

    def get_jalali_date(self):
        return JalaliDate(self.date_joined, locale=('fa')).strftime('%c')

    get_jalali_date.short_description = 'تاریخ ثبت نام'

    def get_jalali_birth(self):
        return JalaliDate(self.birth, locale=('fa')).strftime('%c')

    get_jalali_birth.short_description = 'تاریخ تولد'

    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

