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

class RawNonprofit(models.Model):
    ein = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    ico = models.CharField(max_length=200, null=True)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=3)
    zip = models.CharField(max_length=15)
    group = models.IntegerField(null=True)
    subsection = models.IntegerField(null=True)
    affiliation = models.IntegerField(null=True)
    classification = models.IntegerField(null=True)
    ruling = models.IntegerField(null=True)
    deductibility = models.IntegerField(null=True)
    foundation = models.IntegerField(null=True)
    activity = models.CharField(max_length=20, null=True)
    organization = models.IntegerField(null=True)
    status = models.IntegerField(null=True)
    tax_period = models.IntegerField(null=True)
    asset_cd = models.IntegerField(null=True)
    income_cd = models.IntegerField(null=True)
    filing_req_cd = models.IntegerField(null=True)
    pf_filing_req_cd = models.IntegerField(null=True)
    acct_pd = models.IntegerField(null=True)
    asset_amt = models.IntegerField(null=True)
    income_amt = models.IntegerField(null=True)
    revenue_amt = models.IntegerField(null=True)
    ntee_cd = models.CharField(max_length=15, null=True)
    sort_name = models.CharField(max_length=200, null=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    geo_accuracy_score = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    geo_accuracy_type = models.CharField(max_length=25)
    geo_number = models.CharField(max_length=20, null=True)
    geo_street = models.CharField(max_length=100)
    geo_city = models.CharField(max_length=40)
    geo_state = models.CharField(max_length=3)
    geo_county = models.CharField(max_length=25)
    geo_zip = models.IntegerField()
    geo_country = models.CharField(max_length=3)
    geo_source = models.CharField(max_length=100)

    def __str__(self):
        return self.name
