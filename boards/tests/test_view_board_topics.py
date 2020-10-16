from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Board
from ..views import TopicListView


class BoardTopicsTests(TestCase):
    def setUp(self):
        Board.objects.create(name='123', description='456')
        url = reverse('board_topics', kwargs={'pk': 1})
        self.response = self.client.get(url)

    def test_board_topics_view_success_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func.view_class, TopicListView)

    def test_board_topics_view_contains_navigation_link(self):
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})
        home_url = reverse('home')
        self.assertContains(self.response, 'href="{0}"'.format(home_url))
        self.assertContains(self.response, 'href="{0}"'.format(new_topic_url))
