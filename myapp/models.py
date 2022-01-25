from django.db import models
class QA(models.Model):
    question = models.CharField(("question"), max_length=255)
    answer = models.CharField(("answer"), max_length=255)

    def __str__(self):
        return {self.answer} , {self.question}

class ExcelFile(models.Model):
    file = models.FileField(upload_to="excel")