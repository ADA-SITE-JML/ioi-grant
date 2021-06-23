from django.db import models
from django.utils import timezone
from .utils import generate_dataframe_and_graph_as_base64


class SiteSetting(models.Model):
    title = models.CharField(max_length=150)

    category = models.OneToOneField('Category',
                                    null=True,
                                    on_delete=models.SET_NULL)

    class Meta:
        verbose_name = ('Site Setting')
        verbose_name_plural = ('Site Setting')

    def __str__(self):
        return '{0}'.format(self.title)


class Logos(models.Model):
    side_text = models.CharField(null=True,
                                 blank=True,
                                 max_length=150)

    image = models.ImageField(null=True,
                              blank=True,
                              upload_to='Logos')

    width = models.CharField(default='100%',
                             max_length=10)

    height = models.CharField(default='100%',
                              max_length=10)

    alt = models.CharField(blank=True,
                                null=True,
                                max_length=150)

    site_setting = models.OneToOneField(SiteSetting,
                                     on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Logo')
        verbose_name_plural = ('Logo')

    def __str__(self):
        return '{0}'.format(self.alt)


class Navbar(models.Model):
    bg_color = models.CharField(default='#343a40',
                                max_length=30)

    font_color = models.CharField(default='rgb(255, 255, 255, .5)',
                                max_length=30)

    site_setting    = models.OneToOneField(SiteSetting,
                                        on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Navbar')
        verbose_name_plural = ('Navbar')

    def __str__(self):
        return '{0} {1}'.format('Navigation Bar Version', self.pk)


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')

    def __str__(self):
        return self.name


class Body(models.Model):
    bg_color = models.CharField(default='#fff',
                                max_length=30)

    site_setting    = models.OneToOneField(SiteSetting,
                                        on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Body')
        verbose_name_plural = ('Body')

    def __str__(self):
        return '{0} {1}'.format('Body Version', self.pk)


class AboutPage(models.Model):
    name     = models.CharField(max_length=600)

    html     = models.TextField()

    css      = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = ('About Page')
        verbose_name_plural = ('About Page')

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.name = "%s %s" % ('About Page', self.pk)
        super(AboutPage, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ExternalDatabaseConnectionCredentials(models.Model):
    host        = models.CharField(max_length=18)

    dbname      = models.CharField(max_length=150)

    user        = models.CharField(max_length=150)

    password    = models.CharField(max_length=150)

    created_at      = models.DateTimeField()

    updated_at      = models.DateTimeField(blank=True,
                                           null=True)

    deleted_at      = models.DateTimeField(blank=True,
                                           null=True)

    class Meta:
        verbose_name = ('External DB Connection Credential')
        verbose_name_plural = ('External DB Connection Credentials')

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.created_at = timezone.now()
        else:
            self.updated_at = timezone.now()
        super(ExternalDatabaseConnectionCredentials, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.dbname} at {self.host}"


class Graphs(models.Model):
    title           = models.CharField(max_length=300)

    query           = models.TextField(help_text='Note: inserted query must be a valid sql one.')

    table        = models.TextField(blank=True,
                                    null=True)

    code            = models.TextField(default='df.plot(ax=ax)',
                                       help_text='Note: there are 3 global variables to be used: df (pandas dataframe), fig (matplotlib figure) and ax (matplotlib axes). Naming has been given logical equivalent of the general use. They can be overriden accourding to the further manipulation of the data')
    img_base64      = models.TextField()

    description     = models.TextField(blank=True,
                                       null=True,
                                       help_text='This will help you to fastly identify graph settings')

    active          = models.BooleanField(default=True)

    top             = models.CharField(default="0px",
                                       max_length=50)

    left             = models.CharField(default="0px",
                                       max_length=50)

    snap_tolerance   = models.IntegerField(default=20,
                                           help_text='The distance after which the grahps will be magnetised to each other.')

    card_width       = models.CharField(default='22rem',
                                       max_length=50)

    card_height      = models.CharField(default='20rem',
                                       max_length=50)

    connection      = models.ForeignKey(ExternalDatabaseConnectionCredentials,
                                        on_delete=models.CASCADE)

    category        = models.OneToOneField(Category,
                                           null=True,
                                           on_delete=models.SET_NULL)

    class Meta:
        verbose_name = ('Graph')

    def save(self, *args, **kwargs):
        connection = ExternalDatabaseConnectionCredentials.objects.values('host', 'dbname', 'user', 'password')[self.connection.pk - 1]

        if self._state.adding:
            df, base64      = generate_dataframe_and_graph_as_base64(connection, self.query, self.code)
            self.table      = df.to_html()
            self.img_base64 = base64
        else:
            df, base64      = generate_dataframe_and_graph_as_base64(connection, self.query, self.code)
            self.table      = df.to_html()
            self.img_base64 = base64

        super(Graphs, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"


