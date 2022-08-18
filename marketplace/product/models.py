from django.db import models


class ProductModel(models.Model):
    """
        Model for product
    """
    name = models.CharField(max_length=128)
    description = models.TextField()
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    price = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    edited_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return str(self.id)


class ProductChangesModel(models.Model):
    """
        Model to see all changes in Product
    """
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