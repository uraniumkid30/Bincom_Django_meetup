# models tut 1
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=30)
    about = models.TextField()
    email = models.EmailField()
    website = models.URLField()
    address = models.CharField(max_length=150)
    owner = models.CharField(max_length=150)
    vacancy = models.BooleanField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name

class Language(models.Model):
    LANG_TYPE = (('C', 'Compiled'),
                    ('I', 'Interpreted'),)
    name = models.CharField(max_length=30)
    language_type = models.CharField(choices=LANG_TYPE, default='C', max_length=50)
    def __str__(self):
        return self.name

class Framework(models.Model):
    name = models.CharField(max_length=30)
    language = models.ForeignKey(Language, on_delete=models.CASCADE) #in sql language id is used

    def __str__(self):
        return self.name
class Programmer(models.Model):
    LANG_PROFICIENCY = (('B','Beginner'),
               ('I','Intermediate'),
               ('A','Advance'),)
    EMPLOYMENT_LEVEL = (('J', 'Junior'),
               ('S', 'Senior'),)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    language = models.ManyToManyField(Language,)
    age = models.IntegerField()
    lang_level = models.CharField(choices=LANG_PROFICIENCY,default='B',max_length=50)
    employment_level = models.CharField(choices=EMPLOYMENT_LEVEL, default='J',max_length=50)
    salary = models.IntegerField()
    bonus = models.FloatField()
    salary_paid = models.BooleanField()
    marital_status = models.BooleanField()
    date_employed = models.DateTimeField()

    @property
    def total_earnings(self):
        return (self.salary + (self.salary*self.bonus))

    @property
    def name(self):
        return (self.first_name + ' ' +self.last_name)


    def __str__(self):
        return self.first_name + ' ' +self.last_name


