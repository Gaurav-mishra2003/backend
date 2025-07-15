
from django.db import models

class Resume(models.Model):
    tittle = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to='resumes/')
    created_at = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.tittle or f"Resume {self.id}"



