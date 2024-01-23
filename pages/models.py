from django.db import models


class OurWorkModel(models.Model):
    project_name = models.CharField(max_length=255)
    cotegory = models.CharField(max_length=50)
    img = models.ImageField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = 'our work'
        verbose_name_plural = 'our works'
