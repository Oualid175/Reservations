from django.urls import path
from .views import Gerer, Confirmer, Annuler, Fixer

urlpatterns = [
    path('gerer/', Gerer.as_view(), name='gerer'),
    path('confirmer/', Confirmer.as_view(), name='confirmer'),
    path('annuler_admin/', Annuler.as_view(), name='annuler_admin'),
    path('fixer/', Fixer.as_view(), name='fixer'),
]
