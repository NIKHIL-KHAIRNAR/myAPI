from django.db import models
from django.utils.text import gettext_lazy as _


class TestTable(models.Model):
    name = models.CharField(_('Name'), max_length=254)
    mobile = models.CharField(_('Phone_number'), null=True, max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("API")
        verbose_name_plural = _("API's")


