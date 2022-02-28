from django.db import models
from django.utils.translation import gettext_lazy as _


class BannerModel(models.Model):
    collection = models.CharField(max_length=100, verbose_name=_('collection'))
    title = models.CharField(max_length=100, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'))
    banner = models.ImageField(upload_to='banners', verbose_name=_('banner'))
    is_active = models.BooleanField(verbose_name=_('is_active'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('banner')
        verbose_name_plural = _('banners')


class ContactModel(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    message = models.TextField(verbose_name=_('message'))
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created_at')
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
