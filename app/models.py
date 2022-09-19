from datetime import date
from xml.dom.minicompat import defproperty
from django.db import models


class About(models.Model):
    """About me"""
    my_name = models.CharField("Name", max_length=20)
    excerpt = models.CharField("Excerpt", max_length=150, default='')
    description = models.TextField("Description")

    def __str__(self):
        return self.my_name
    
    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"  


class Contact(models.Model):
    my_name = models.ForeignKey(About, verbose_name="My Name", on_delete=models.CASCADE)
    address = models.CharField("Address", max_length=150)
    phone_number = models.CharField("Phone Number", max_length=20)
    gmail = models.CharField("Gmail", max_length=50)

    def __str__(self):
        return str(self.my_name)
        
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"  


class Career(models.Model):
    title = models.CharField("Title", max_length=150)
    role = models.CharField('Role', max_length=50)
    start = models.DateField("Starts From Date")
    end = models.DateField("Finish date")
    description = models.TextField("Description")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Career"
        verbose_name_plural = "Careers"  


class Education(models.Model):
    title = models.CharField("Title", max_length=150)
    role = models.CharField('Role', max_length=50)
    start = models.DateField("Starts From Date")
    end = models.DateField("Finish date")
    description = models.TextField("Description")

    def __str__(self):
        return self.title
 
    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Educations"       
    

class ProgrammingSkills(models.Model):
    title = models.CharField("Title", max_length=50, default='')
    level = models.PositiveIntegerField("Level", default=0,
        help_text="set your level")

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "ProgSkill"
        verbose_name_plural = "ProgSkills"


class Skills(models.Model):
    description = models.TextField("Description")
    my_skills = models.ManyToManyField(ProgrammingSkills, verbose_name="skills", related_name="my_skills")

    def __str__(self):
        return str(self.description)
    
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"


class Feedbacks(models.Model):
    image = models.ImageField("Client Images", upload_to="clients")
    name = models.CharField("Name", max_length=50)
    role = models.CharField("Role", max_length=50)
    description = models.TextField("Description")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"       


# class SayHello(models.Model):
#     description = models.TextField("Description")
#     gmail = models.ForeignKey(Contact, verbose_name="Gmail", on_delete=models.CASCADE)
#     phone_number = models.ForeignKey(Contact, verbose_name="Phone Number", on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.gmail
        