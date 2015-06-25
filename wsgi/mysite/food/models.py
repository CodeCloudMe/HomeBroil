from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

def food_upload(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("foods", filename)


class Grub(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date added')
    exp_date = models.DateTimeField('date expires')
    description = models.CharField(max_length=500)
    photo = models.ImageField(upload_to=food_upload, blank=True)
    userId = models.IntegerField()


    def save(self, *args, **kwargs):
        self.pub_date = timezone.now()
        return super(Grub, self).save(*args, **kwargs)

    



    #


     


