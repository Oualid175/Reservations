from django.urls import path
from .views import Reserver, Annuler, Consulter, Proposer

urlpatterns = [
    path('reserver/', Reserver.as_view(), name='reserver'),
    path('annuler/', Annuler.as_view(), name='annuler'),
    path('consulter/', Consulter.as_view(), name='consulter'),
    path('proposer/', Proposer.as_view(), name='proposer'),
]
