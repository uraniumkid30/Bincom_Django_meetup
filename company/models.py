# models tut 1
from django.db import models
from django.urls import reverse
# relatedname lists out all the children in a parent
# related_query_name is used to filter in queries
# null = True should never be used for text base field (None  and empty str)
# blank is a form validation notion, form.is_valid()

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True


class Company(CommonInfo):
    about = models.TextField()
    email = models.EmailField()
    website = models.URLField()
    address = models.CharField(max_length=150)
    owner = models.CharField(max_length=150)
    vacancy = models.BooleanField()
    created_at = models.DateTimeField()
    companies = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company_details', kwargs={'pk':self.id})

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'

class Language(CommonInfo):
    LANG_TYPE = (('C', 'Compiled'),
                    ('I', 'Interpreted'),)
    language_type = models.CharField(choices=LANG_TYPE, default='C', max_length=50)
    languages = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('language_details', kwargs={'pk': self.id})

class Framework(CommonInfo):
    language = models.ForeignKey(Language, on_delete=models.CASCADE ,related_name='Frameworks',related_query_name='framework')
    #in sql language id is used
    frameworks = models.Manager()

    def get_absolute_url(self):
        return reverse('framework_details', kwargs={'pk': self.id})

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
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='Programmers')
    language = models.ManyToManyField(Language,related_name='Programmers',related_query_name='programmer')
    age = models.IntegerField()
    lang_level = models.CharField(choices=LANG_PROFICIENCY,default='B',max_length=50)
    employment_level = models.CharField(choices=EMPLOYMENT_LEVEL, default='J',max_length=50)
    salary = models.IntegerField()
    bonus = models.FloatField()
    salary_paid = models.BooleanField()
    marital_status = models.BooleanField()
    date_employed = models.DateTimeField()
    programmers = models.Manager()

    @property
    def total_earnings(self):
        return (self.salary + (self.salary*self.bonus))

    @property
    def name(self):
        return (self.first_name + ' ' +self.last_name)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('programmer_details', kwargs={'pk': self.id})



