from django.db import models
from helper.models import TrackingModel
from account.models import User

class Todo(TrackingModel):
    title = models.CharField(max_length=255)
    desc=models.TextField()
    is_complete = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return self.title



    

