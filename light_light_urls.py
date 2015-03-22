from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',

    url(r'^$', 'django.contrib.auth.views.login', {'template_name':'admin/login.html'}, name='login'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^user/password/reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/user/password/reset/done/'}, name="password_reset"),
    url(r'^user/password/reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : '/user/password/done/'}),
    url(r'^user/password/done/$', 'django.contrib.auth.views.password_reset_complete'),

    url(r'^authenticated/', include('authenticated.urls')),
    url(r'^design/', include('design.urls')),
    url(r'^infographic/', include('financials.urls')),
    url(r'^data/', include('data.urls')),
    url(r'^imports/', include('imports.urls')),
    url(r'^actions/', include('actions.urls')),
    url(r'^masters/', include('master.urls')),
    url(r'^chat/', include('chat.urls')),

    (r'static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

)
