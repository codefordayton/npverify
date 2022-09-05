from django.db import models

class NTEECategory(models.Model):
    category = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class NTEECode(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(NTEECategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Nonprofit(models.Model):
    ein = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    ntee = models.ForeignKey(NTEECode, null=True, on_delete=models.CASCADE)
    altname = models.CharField(max_length=200, null=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=5)
    zip = models.CharField(max_length=12)
    county = models.CharField(max_length=20)
    has_contact = models.BooleanField(null=True)
    needs_volunteers = models.BooleanField(null=True)
    needs_review = models.BooleanField(null=True)
    review_comment = models.TextField(null=True)
    complete = models.BooleanField(default=False)
    website_url = models.CharField(max_length=200, null=True)
    facebook_url = models.CharField(max_length=200, null=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
