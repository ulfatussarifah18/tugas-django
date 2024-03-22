from django.db import models

class peminjambuku(models.Model):
    nama = models.CharField(max_length=50)
    npm = models.CharField(max_length=50)
    prodi = models.CharField(max_length=50)

    def __str__(self):
        return '{}. {}'.format(self.id,self.nama)


   