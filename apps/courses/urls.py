from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course_path$', views.add_course_path),
    url(r'^remove_(?P<course_id>\d+)$', views.remove),
    url(r'^comments_for_(?P<course_id>\d+)$', views.comments_for),
    url(r'^add_comment_path_(?P<course_id>\d+)$', views.add_comment_path),
    url(r'^delete_check_(?P<course_id>\d+)$', views.delete_check),
]
