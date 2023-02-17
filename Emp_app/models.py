from django.db import models

# Create your models here.


class department(models.Model):
    dept_name = models.CharField(max_length= 100, null=False)  #Primary Key 
    location = models.CharField(max_length= 100)
    
    def __str__(self):
        return "%s %s" %(self.dept_name, self.location)
     
class role(models.Model):
    role = models.CharField(max_length= 100)
    # experience = models.PositiveIntegerField()
    
    def __str__(self):
        return self.role

class employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(department, on_delete=models.CASCADE)  
    salary = models.IntegerField(default=0)
    role = models.ForeignKey(role, on_delete= models.CASCADE)
    phone = models.PositiveBigIntegerField()
    hire_date = models.DateField()
    
    
    def __str__(self):
        return "%s %s %s %s %s %s %s" %(self.first_name, self.last_name, self.dept, self.role, self.salary, self.hire_date, self.phone)
