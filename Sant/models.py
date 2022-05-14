from enum import IntEnum

from django.db import models

# Create your models here.
from django.utils.html import format_html
from phonenumber_field.modelfields import PhoneNumberField

DikshaType = (
    ("Bhagvadi", "Bhagvadi"),
    ("Parshadi", "Parshadi"),
    ("Sadhak", "Sadhak")
)

Year = (('Present', 'Present'),) + tuple((str(i), str(i)) for i in range(1975, 2024))


class Sant(models.Model):
    Name = models.CharField(max_length=100, verbose_name="નામ")
    english_name = models.CharField(max_length=100, verbose_name="english નામ")
    Photo = models.ImageField(upload_to='santo/', blank=True, null=True, verbose_name="ફોટો")
    mobile_no = PhoneNumberField(blank=True, verbose_name="મોબાઈલ નંબર")
    remark = models.CharField(max_length=1000,blank=True, null=True,verbose_name="વિશેષ વિગત")
    def __str__(self):
        return "પૂજ્ય " + self.Name

    class Meta:
        ordering = ['Name']

    @property
    def PhotoPreview(self, obj):
        if obj.Photo:
            s = '<img src={} height="150px" width="150px" style="border: 1px solid black" alt="{}"/></div>'.format(
                obj.Photo.url,obj.Name)
        else:
            s = '<img  height="80px" width="80px" src="/static/img/yuvak.png" >'
        return format_html(s)
    class Meta:
        verbose_name_plural = "પૂ.સંત"
        verbose_name = "પૂ.સંત"


class PurvashramDetails(models.Model):
    name = models.CharField(max_length=100, verbose_name="નામ",blank=True,null=True)
    native_place = models.CharField(max_length=100, verbose_name="વતન")
    study = models.CharField(max_length=100, blank=True, null=None, verbose_name="અભ્યાસ")
    sant = models.OneToOneField(Sant, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "પૂર્વાશ્રમની વિગત"
        verbose_name = "પૂર્વાશ્રમની વિગત"


class DikshaDetails(models.Model):
    type = models.CharField(max_length=10, choices=DikshaType, verbose_name="પ્રકાર")
    name = models.CharField(max_length=50,verbose_name="દીક્ષિત નામ",default='')
    Date = models.CharField(choices=Year, max_length=7, null=True, blank=True, verbose_name="દીક્ષા વર્ષ")
    place = models.CharField(max_length=25, blank=True, null=True, verbose_name="સ્થળ")
    event = models.CharField(max_length=50, blank=True, null=True, verbose_name="સમૈયા/ઉત્સવ")
    sant = models.ForeignKey(Sant, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "દીક્ષા વિગત"
        verbose_name = "દીક્ષા વિગત"


class AnuvrutiDetails(models.Model):
    fromYear = models.CharField(max_length=7, choices=Year, verbose_name="શરૂઆત")
    toYear = models.CharField(max_length=7, choices=Year, verbose_name="અંત")
    place = models.CharField(max_length=20, verbose_name="સ્થળ/મંદિર")
    post = models.CharField(max_length=20, verbose_name="પદ",blank=True,null=True)
    seva = models.CharField(max_length=20, verbose_name="વિભાગ",blank=True,null=True)
    sant = models.ForeignKey(Sant, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "અનુવૃતિ વિગત"
        verbose_name = "અનુવૃતિ વિગત"


class Attachments(models.Model):
    photo = models.ImageField(upload_to='attachments/', verbose_name="ફોટો")
    photolink = models.URLField(max_length=1500, blank=True, null=None, verbose_name="લિંક")
    discripttion = models.CharField(max_length=1500, verbose_name="વર્ણન")
    sant = models.ForeignKey(Sant, on_delete=models.CASCADE)

    @property
    def image_priview(self):
        if self.photo:
            s = '<img src={} height="150px" width="250px" style="border: 1px solid black" alt="{}"/></div>'.format(
                self.photo.url,self.discripttion)
        else:
            s = '<img  height="150px" width="250px" src="/static/img/yuvak.png" >'
        return format_html(s)

    @property
    def imagelink(self):
        if self.photolink:
            s = '<a href={} target="_blank"  alt="{}">{}</a>'.format(
                self.photolink, self.discripttion,self.photolink)
        else:
            s = '<a href="#" target="_blank" ></a>'
        return format_html(s)

    class Meta:
        verbose_name_plural = "ફોટો"
        verbose_name = "ફોટો"
