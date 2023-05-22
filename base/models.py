from django.db import models

# Create your models here.


class Hackathon(models.Model):
    submission_types = [("image", "image"),
                        ("link", "link"),
                        ("file", "file"),]

    # user=
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=600, null=True, blank=True)
    bg_image = models.ImageField(
        upload_to="static/bg_img", null=True, blank=True)
    hk_image = models.ImageField(
        upload_to="static/hk_img", null=True, blank=True)
    type_of_submission = models.CharField(
        max_length=10, choices=submission_types, default="link")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    reward_prize = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title + " " + self.type_of_submission


class Submission(models.Model):
    # submitted_by=
    hackthon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    summary = models.TextField(max_length=500, null=True, blank=True)
    url = models.URLField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to="static/images")
    file = models.FileField(upload_to="static/files")
