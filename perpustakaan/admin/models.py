from django.db import models

class pinjambuku(models.Model):
    nama = models.CharField(max_lenght=50)
    npm = models.CharField(max_lenght=50)
    prodi = models.CharField(max_lenght=50)



    def __str__(help):
        return "{}. {}".format(self.id,self.nama)


