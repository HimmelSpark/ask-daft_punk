from django.conf.urls import url
from questions import views

urlpatterns = [
    url(r'^daft-quest/(?P<qnum>(\d+))$', views.question, name="question"),
    url(r'^load-data', views.load_data, name='load'),
    url(r'^daft-set', views.settings, name="settings"),
    url(r'^daft-reg', views.register, name="register"),
    url(r'^daft-out', views.logOut, name="logout"),
    url(r'^daft-log', views.logIn, name="login"),
    url(r'^daft-test', views.test, name="test"),
    url(r'^daft-hot', views.hot, name="hot"),
    url(r'^daft-ask', views.ask, name="ask"),
    url(r'^daft-tag', views.tag, name="tag"),
    url(r'^like', views.like, name='like'),
    url(r'^$', views.index, name="index"),
]