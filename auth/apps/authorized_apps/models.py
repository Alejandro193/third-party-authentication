from django.db import models


class AuthorizedApps(models.Model):
    name = models.CharField(max_length=254)
    identification = models.CharField(max_length=254)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'authorized_apps'
