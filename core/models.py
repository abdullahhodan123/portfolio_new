from django.db import models


class SiteSetting(models.Model):
    site_title = models.CharField(max_length=100)
    hero_title = models.CharField(max_length=200)
    hero_subtitle = models.TextField()
    hero_image = models.ImageField(upload_to="hero/")
    resume = models.FileField(upload_to="resume/")
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=255)

    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

    def __str__(self):
        return self.site_title


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="projects/")
    description = models.TextField()

    github = models.URLField(blank=True)
    live = models.URLField(blank=True)

    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.name} - {self.subject}"