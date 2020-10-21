# import base64
from django.test import TestCase
from .models import Article, Category, Comment, Tag, Blogger
from django.core.files import File


class TagTestCase(TestCase):

    # CharField
    def test_name_CharField(self):
        tag = Tag()
        self.assertEqual(tag.tag_name_with_fallback, 'hashtag')
        print("< Tag Name Tester Worked >")
        tag.tag_name = 'dash'
        self.assertEqual(tag.tag_name_with_fallback, 'dash')
        print('< Tag Name Custom Test Worked >')


class ArticleTestCase(TestCase):

    # CharField
    def test_title_CharField(self):
        art = Article()
        self.assertEqual(art.title_with_fallback, 'Not Really a Title')
        print("< Article Title Tester Worked >")
        art.title = 'epilogue'
        self.assertEqual(art.title_with_fallback, 'epilogue')
        print('< Article Name Custom Test Worked >')

    # TextField
    def test_digest_TextField(self):
        art = Article()
        self.assertEqual(art.digest_with_fallback, "Digesting.")
        print("< Article Digest Tester Worked >")
        art.digest = "This is the digest of the new article."
        self.assertEqual(art.digest_with_fallback, "This is the digest of the new article.")
        print('< Article Digest Custom Test Worked >')

    # # ImageField
    # def test_display_picture(self):
    #     art = Article()
    #     art.picture = File(open("./photos/Untitled_Artwork_2.png"))
    #     art.save()
    #     print("< Picture Test Worked >")
    #     p = art.objects.get(id=1).photo.path
    #     self.failUnless(open(p), 'file not found')


class CategoryTestCase(TestCase):

    # CharField
    def test_name(self):
        cat = Category()
        self.assertEqual(cat.name_with_fallback, 'bekind')
        print("< Category Name Tester Worked >")
        cat.name = "beadog"
        self.assertEqual(cat.name_with_fallback, 'beadog')
        print('< Category Name Custom Test Worked >')

    # # DateTimeField
    # def test_created_time(self):


class CommentTestCase(TestCase):

    # URLField
    def test_display_url(self):
        com = Comment()
        com.url = 'https://google.com'
        self.assertEqual(com.display_url, 'https://google.com')
        print('< Comment URL Custom Test Worked >')


class BloggerTestCase(TestCase):

    def test_JSONField(self):
        field = Blogger()
        field.info = '{"user 1": "category 1"}'
        self.assertEqual(field.info, '{"user 1": "category 1"}')
        print('< JSON Field Custom Test Worked >')
