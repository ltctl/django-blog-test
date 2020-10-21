from django.db import models
from django.conf import settings
# Create your models here.


class Tag(models.Model):
    tag_name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.tag_name

    @property
    def display_tag_name(self):
        return self.tag_name

    @property
    def tag_name_with_fallback(self):
        return self.tag_name if self.tag_name else 'hashtag'


class Article(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    date_time = models.DateField(auto_now_add=True)
    content = models.TextField()
    digest = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    view = models.BigIntegerField(default=0)
    comment = models.BigIntegerField(default=0)
    picture = models.ImageField(upload_to="photos/")
    tag = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.title

    def viewed(self):
        """update view count"""
        self.view += 1
        self.save(update_fields=['view'])
        return self.view

    def commented(self):
        """update comment count"""
        self.comment += 1
        self.save(update_fields=['comment'])
        return self.comment

    class Meta:
        ordering = ['-date_time']

    @property
    def display_title(self):
        return self.title

    @property
    def title_with_fallback(self):
        return self.title if self.title else 'Not Really a Title'

    @property
    def display_digest(self):
        return self.digest

    @property
    def digest_with_fallback(self):
        return self.digest if self.digest else 'Digesting.'


class Category(models.Model):
    name = models.CharField(max_length=30)
    created_time = models.DateTimeField(auto_now_add=True)
    last_mod_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "categories"

    def __unicode__(self):
        return self.name

    @property
    def display_name(self):
        return self.name

    @property
    def name_with_fallback(self):
        return self.name if self.name else 'bekind'


class Comment(models.Model):
    title = models.CharField(max_length=50)
    source_id = models.CharField(max_length=25)
    created_time = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=25)
    url = models.URLField(max_length=250)  # comment URL
    comment = models.CharField(max_length=500)

    @property
    def display_title(self):
        return self.title

    @property
    def title_with_fallback(self):
        return self.title if self.title else 'Random comment'

    @property
    def display_comment(self):
        return self.comment

    @property
    def comment_with_fallback(self):
        return self.comment if self.comment else 'oic'

    @property
    def display_url(self):
        return self.url


class Blogger(models.Model):
    info = models.JSONField(null=True, blank=True)
