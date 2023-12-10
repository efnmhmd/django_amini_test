from django.db import models


class Person(models.Model):
    lname = models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.lname + " " + self.fname


class Phone(models.Model):
    phone = models.CharField(max_length=10,unique=True)
    person = models.ForeignKey("Person", on_delete=models.CASCADE ,related_name="phones",null=True , blank=True)
    def __str__(self):
        if self.person != None:
            return self.person.lname + " " + self.person.fname
        else : 
            return self.phone
        
class Address(models.Model):
    address = models.TextField(null=True , blank=True)
    person = models.ManyToManyField("Person")
    def __str__(self):
        if self.person.first():
            return self.person.first().lname + " " + self.person.first().fname
        else :
            return " no person" + str(self.id)
