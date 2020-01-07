from message import views
from django.conf.urls import url
from django.conf.urls.static import static
from . import settings
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = [
    url(r'^jrhq',views.jrhq),
    url(r'^goldprice',views.goldprice),
    url(r'^lshq_sge',views.lshq_sge),
    url(r'^lshq_ctf',views.lshq_ctf),
    url(r'^lshq_tmall_ctf',views.lshq_ctf_tmall),
    url(r'^lshq_css',views.lshq_css),
    url(r'^lshq_tmall_css',views.lshq_css_tmall),
    url(r'^hqzs_css', views.hqzs_css),
    url(r'^hqzs_ctf',views.hqzs_ctf),
    url(r'^hqzs_sge',views.hqzs_sge),
    url(r'^sge_rec',views.sge_rec),
    url(r'^css_rec',views.css_rec),
    url(r'^ctf_rec',views.ctf_rec),
]