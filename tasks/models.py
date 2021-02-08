from django.db import models
from django.urls import reverse

# Create your models here.

class Task(models.Model):
    task=models.CharField(max_length=35)

    def delete_url(self):
        return reverse("delete",kwargs={'task_id':self.id})

    def done_url(self):
        return reverse("done",kwargs={'task_id':self.id})

class DoneTask(models.Model):
    task=models.CharField(max_length=35,null=True,blank=True)

    def delete_done_url(self):
        return reverse("delete_done",kwargs={'task_id':self.id})
