from django.test import TestCase
from ..views import PostListView
from django.urls import resolve, reverse
from ..models import Board, Topic, Post
from django.contrib.auth.models import User


class TopicPostsTests(TestCase):
    def setUp(self):
        board = Board.objects.create(name='django', description='pass')
        user = User.objects.create_user(username='john', email='john@doe.com', password='asd123456')
        topic = Topic.objects.create(board=board, starter=user, subject='hello world')
        Post.objects.create(message='Lorem ipsum dolor sit amet', topic=topic, created_by=user)
        url = reverse('topic_posts', kwargs={'pk': board.pk, 'topic_pk': topic.pk})
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/boards/1/topics/1/')
        self.assertEquals(view.func.view_class, PostListView)

