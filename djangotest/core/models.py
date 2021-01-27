from django.utils.translation import ugettext_lazy as _


from django.db import models

class BlogPost(models.Model):

    title = models.CharField(_("Title"), max_length=50)
    date = models.DateTimeField()
    short_description = models.CharField(_("Short Description"), max_length=150, blank=True, null=True)
    content = models.TextField()

    class Meta:
        verbose_name = _("blogpost")
        verbose_name_plural = _("blogposts")

    def __str__(self):
        return f"{self.title} - {self.date}"  