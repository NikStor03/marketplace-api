from django.db import models

"""
{
"name": "Test",
"description": "test",
"start_date": "2022-08-17 19:56:35.584154",
"end_date": "2022-08-17 19:56:35.584154",
"price": 20.00
}
"""
"""
{
"name": "Test Updated",
"description": "test updated",
"start_date": "2022-08-17 19:56:35.584154",
"end_date": "2022-08-17 19:56:35.584154",
"price": 0.00
}
{
"start_date": "2022-01-20",
"end_date": "2022-09-10"
}
"""


class ProductModel(models.Model):

    name = models.CharField(max_length=128)
    description = models.TextField()
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    price = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    edited_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return str(self.id)


class ProductChangesModel(models.Model):

    product = models.ForeignKey('product.ProductModel', on_delete=models.SET_NULL, null=True)
    name_was = models.CharField(max_length=128)
    name_new = models.CharField(max_length=128)

    description_was = models.TextField()
    description_new = models.TextField()

    start_date_was = models.DateField(null=True)
    start_date_new = models.DateField(null=True)

    end_date_was = models.DateField(null=True)
    end_date_new = models.DateField(null=True)

    price_was = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    price_new = models.DecimalField(null=True, max_digits=5, decimal_places=2)

    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.id)