from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import TransactionViewSet
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
    path('', include(router.urls)),
    path('summary/', TransactionSummaryView.as_view(), name='summary'),
]