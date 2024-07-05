from django.db import models
from django.contrib.auth.models import AbstractBaseUser



class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=50,unique=True)
    first_name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null = True)
    last_name = models.CharField(max_length=50,null = True)
    role = models.CharField(max_length=20, null = True)
    email = models.EmailField(max_length=50, unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['first_name','last_name','surname']
    
    
    class Meta:
        db_table = "CustomUser"
        
    
    
        def __str__(self):
            return f"{self.user_name} {self.first_name} {self.surname} {self.last_name} {self.role}"
    
    def __repr__(self):
            
        
        return f"{self.user_name} {self.first_name} {self.surname} {self.last_name} {self.role}"
    
    