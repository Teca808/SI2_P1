from django.urls import path
from visaAppWSBackend.views import TarjetaView, PagoView, ComercioView

urlpatterns = [
    # check if tarjeta is in "tarjeta"
    path('tarjeta/', TarjetaView.as_view(), name='tarjeta'),
    # create "pago"
    path('pago/', PagoView.as_view(), name='pago'),
    # get list of "pagos" associated with a given idComercio
    path('comercio/<str:idComercio>', ComercioView.as_view(), name='comercio'),
    # delete "pago" with id id_pago
    path('pago/<str:id_pago>', PagoView.as_view(), name='pago'),
]