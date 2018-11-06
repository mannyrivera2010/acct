from django.db import models


class Account(models.Model):
    ASSET = 'ASSET'
    LIABILITY = 'LIABILITY'
    EQUITY = 'EQUITY'
    ACCOUNT_TYPE_CHOICES = (
        (ASSET, 'ASSET'),
        (LIABILITY, 'LIABILITY'),
        (EQUITY, 'EQUITY'),
    )
    account_type = models.CharField(
        max_length=200,
        choices=ACCOUNT_TYPE_CHOICES,
        default=ASSET,
    )


class Transaction(models.Model):
    transaction_date = models.DateField(auto_now=False, auto_now_add=True)
    description = models.CharField(max_length=200)

    first_entry_account = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='first_entry')
    second_entry_account = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='second_entry')

    amount = models.DecimalField(max_digits=32, decimal_places=2)
