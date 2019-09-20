from django.conf.urls import url
from .views.order import OrderListCreateView, OrderDetailModifyDeleteView, OrderStatusView
from .views.customer import CustomerCreateView
#from .views.customer import somethinghere

urlpatterns = [
    url('^order/(?P<id>\d+)$', OrderDetailModifyDeleteView.as_view(), name='modify-order'),
    url('^order/(?P<id>\d+)/status$', OrderStatusView.as_view(), name='get-order-status'),
    url('^order/', OrderListCreateView.as_view(), name='get-all-orders'),
    url('^customer/', CustomerCreateView.as_view(), name='create-customer')
]