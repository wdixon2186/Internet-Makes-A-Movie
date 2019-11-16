from django.db import models

class Script(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    logline = models.CharField(max_length=140)
    upload = models.FileField(upload_to='uploads/', default="default.pdf", blank=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)

class Comment(models.Model):
    script = models.ForeignKey(
        Script, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()

    def __str__(self):
        return self.comment