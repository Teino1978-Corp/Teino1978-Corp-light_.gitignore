from django.conf.urls import patterns, url
from .views import IndexView, ChatView

urlpatterns = patterns('',
    url(r'^chatroom/$', view=IndexView.as_view(), name='index_chat'),
    url(r'^chat/$', view=ChatView.as_view(), name='chat'),
    url(r'^crear_comentario/$', view='chat.views.create_comment', name='create_comment'),

)

