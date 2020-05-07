from django.db import models


class Config(models.Model):
    APP_NAME = 'app_name'

    CONFIG_OPTIONS = [
        (APP_NAME, APP_NAME.upper()),
    ]

    key = models.CharField(unique=True, null=False, choices=CONFIG_OPTIONS, max_length=100)
    value = models.CharField(unique=False, null=False, max_length=200)

    def __str__(self) -> str:
        return self.key.upper()

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
