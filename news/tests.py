from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()
   
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))
     # Testing Save Method
    def test_save_method(self):
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
    #  # Testing for Deleting Method
    def test_delete_method(self):
        fetch_editor = Editor.objects.get(first_name='James')
        Editor.delete_editor(fetch_editor)
        editors = Editor.objects.all()
        self.assertTrue(len(editors) == 0)
    
    def test_display_method(self):
        all_editors =Editor.retrieve_all()
        self.assertEqual(all_editors.first_name,'James')

    def test_update_method(self):
        editor = Editor.filter_editor('James')
        fetch_editor = Editor.objects.get(first_name='Nick')
        self.assertEqual(fetch_editor.first_name,'Nick')


class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()
    
    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
