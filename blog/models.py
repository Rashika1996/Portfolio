from django.db import models

class Blog(models.Model):
        title = models.CharField(max_length=255,null=True)
        pub_date = models.DateTimeField()
        body = models.TextField()
        image = models.ImageField(upload_to='images/')

        def dateTimeView(self):
            return self.pub_date.strftime('%b %e %Y')

        def __str__(self):
            return self.title

        
    # body 
    # image
"""class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class BlogTable(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

class Entry(models.Model):
    blog = models.ForeignKey(BlogTable, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline"""


