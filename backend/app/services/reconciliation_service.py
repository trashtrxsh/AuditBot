from typing import Dict, List, Any

def reconcile_invoice_with_po(invoice_data: Dict[str, Any], po_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Compara os dados de uma nota fiscal com um pedido de compra.
    Verifica CNPJ, valor total e data.
    """
    divergencias: List[str] = []
    
    # Validação de CNPJ
    if invoice_data.get("cnpj_emissor") != po_data.get("cnpj_fornecedor"):
        divergencias.append(
            f"CNPJ divergente. NF: {invoice_data.get('cnpj_emissor')} | PO: {po_data.get('cnpj_fornecedor')}"
        )
        
    # Validação de Valor Total
    if float(invoice_data.get("valor_total", 0)) != float(po_data.get("valor_total", 0)):
        divergencias.append(
            f"Valor total divergente. NF: {invoice_data.get('valor_total')} | PO: {po_data.get('valor_total')}"
        )
        
    # Validação de Data
    if invoice_data.get("data_emissao") != po_data.get("data_pedido"):
         divergencias.append(
            f"Data divergente. NF: {invoice_data.get('data_emissao')} | PO: {po_data.get('data_pedido')}"
        )

    # Determinar status
    status = "divergente" if divergencias else "conciliado"

    return {
        "status": status,
        "divergencias": divergencias
    }
