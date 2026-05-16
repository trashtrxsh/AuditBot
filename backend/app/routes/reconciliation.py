from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from app.services.reconciliation_service import reconcile_invoice_with_po
from app.mock.mock_data import MOCK_PURCHASE_ORDERS

router = APIRouter()

# Modelos Pydantic para validação da requisição
class InvoiceData(BaseModel):
    numero_nota: str
    cnpj_emissor: str
    valor_total: float
    data_emissao: str

class ReconciliationRequest(BaseModel):
    nota_fiscal: InvoiceData
    po_number: str

class ReconciliationResponse(BaseModel):
    status: str
    divergencias: List[str]

@router.post("/api/reconcile", response_model=ReconciliationResponse, tags=["Reconciliação"])
def reconcile(request: ReconciliationRequest):
    """
    Recebe os dados extraídos de uma nota fiscal (mock OCR) 
    e realiza a conciliação com o pedido de compra correspondente.
    """
    po_number = request.po_number
    
    # Busca o pedido de compra no banco mockado
    po_data = MOCK_PURCHASE_ORDERS.get(po_number)
    
    # Se o pedido não existir, retorna status de não encontrado sem realizar conciliação
    if not po_data:
        return ReconciliationResponse(
            status="pedido_nao_encontrado",
            divergencias=[f"Pedido de compra '{po_number}' não encontrado no sistema."]
        )
    
    # Chama o serviço de conciliação para validar as regras
    result = reconcile_invoice_with_po(request.nota_fiscal.model_dump(), po_data)
    
    return ReconciliationResponse(
        status=result["status"],
        divergencias=result["divergencias"]
    )
