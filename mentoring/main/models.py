from django.db import models

class users(models.Model):
    u_name = models.CharField(max_length=20)
    press_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.u_name}, {self.press_count}"
    

class user_data(models.Model):
    login = models.CharField(max_length=20)
    u_password = models.CharField(max_length=20)
    u_email = models.EmailField(max_length=50)
    press_count = models.IntegerField()
    

    def __str__(self):
        return f"{self.login}, {self.u_password}, {self.u_emal}, {self.press_count}"
    
    class Meta:
        db_table = 'user_data'