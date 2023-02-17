from django.db import models

class Me(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    age = models.DateField()
    photo = models.ImageField(upload_to='static/img', null=True, blank=True)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=30)
    about = models.CharField(max_length=100)


# email
# about
# phone


# for statisic - 1) work 2) projects 3) year experience 4) work time
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "My_info"
        verbose_name_plural = "My infos"