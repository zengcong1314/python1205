

from app.project.data import  choose_topic
from app.project.pages.topic import TopicPage


def test_topic(login):
    driver = login
    TopicPage(driver).topic()
    assert TopicPage(driver).get_class(choose_topic.topic)
