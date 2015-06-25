from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin

from .views import homepage
from .profiles.views import ProfileDetailView, ProfileEditView, ProfileListView
from food.views import GrubListView, GrubEditView, GrubCreateView, GrubDetailView

urlpatterns = patterns(
    "",
    url(r"^$", homepage, name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^invites/", include("kaleo.urls")),
    url(r"^grub/$", GrubListView.as_view(), name="grubs_list"),
    url(r"^grub/edit/", GrubEditView.as_view(), name="grubs_edit"),
    url(r"^grub/create/", GrubCreateView.as_view(), name="grubs_create"),


    url(r"^profile/edit/", ProfileEditView.as_view(), name="profiles_edit"),
    url(r"^u/$", ProfileListView.as_view(), name="profiles_list"),
    url(r"^grub/(?P<id>[\w\._-]+)/$", GrubDetailView.as_view(), name="grubs_detail"),

    url(r"^u/(?P<username>[\w\._-]+)/$", ProfileDetailView.as_view(), name="profiles_detail"),
    url(r"^t/", include("teams.urls")),

    url(r"", include("wiki.urls"))
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
