from django.db import models
import datetime as dt 

class Editor(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank = True)

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()

    @classmethod
    def delete_editor(cls,name):
        cls.delete(name)    
    class Meta:
        ordering = ['first_name']
    @classmethod
    def retrieve_all(cls):
        all_editors=Editor.objects.all()
        for editor in all_editors:
            return editor
    @classmethod
    def filter_editor(cls,name):
        updates_editor = Editor.objects.filter(first_name=name).update(first_name='Nick')
        return updates_editor
    

class tags(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length = 60)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/')

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news

    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
