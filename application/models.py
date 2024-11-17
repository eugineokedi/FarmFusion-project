from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    
    
    def __str__(self):
        return f'name={self.name}, email_address={self.email}, title={self.subject}, message={self.message}'