from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import TransactionViewSet
from core.views.debug import PopulateDBView
from core.views.summary import TransactionSummaryView

# O Router cria as rotas automaticamente,
# fazendo um gerênciamento desses endpoints:
# GET /transactions/ (Listar)
# POST /transactions/ (Criar)
# GET /transactions/1/ (Detalhar)
# PUT /transactions/1/ (Atualizar)
# DELETE /transactions/1/ (Deletar)
router = DefaultRouter()
router.register(r'transactions', TransactionViewSet, basename='transaction')

urlpatterns = [
    path('summary/', TransactionSummaryView.as_view(), name='summary'),
    
    # Rota para gerar dados (pode remover depois se for pra produção)
    path('populate/', PopulateDBView.as_view(), name='populate-db'),

    path('', include(router.urls)),
]