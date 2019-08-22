from django.db import models

class Comanda(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=False)


    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name
