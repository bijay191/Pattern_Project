from django.db import models   

class FileName(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class RegexPattern(models.Model):
    file = models.ForeignKey(FileName, on_delete=models.CASCADE)
    pattern = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} -> {self.pattern}"