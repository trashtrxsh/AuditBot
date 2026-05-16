from typing import Dict, List, Any

def reconcile_invoice_with_po(invoice_data: Dict[str, Any], po_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Compara os dados de uma nota fiscal com um pedido de compra.
    Verifica CNPJ, valor total e data.
    """
    divergencias: List[str] = []
    
    # Mapeamento explícito dos campos
    nf_cnpj = invoice_data.get("cnpj_emissor")
    po_cnpj = po_data.get("cnpj_fornecedor")
    
    nf_valor = float(invoice_data.get("valor_total", 0))
    po_valor = float(po_data.get("valor_total", 0))
    
    nf_data = invoice_data.get("data_emissao")
    po_data_pedido = po_data.get("data_pedido")

    # Comparação: cnpj_emissor da nota com cnpj_fornecedor do pedido
    if nf_cnpj != po_cnpj:
        divergencias.append(
            f"CNPJ divergente. NF (emissor): {nf_cnpj} | PO (fornecedor): {po_cnpj}"
        )
        
    # Comparação: valor_total da nota com valor_total do pedido
    if nf_valor != po_valor:
        divergencias.append(
            f"Valor total divergente. NF: {nf_valor} | PO: {po_valor}"
        )
        
    # Comparação: data_emissao da nota com data_pedido do pedido
    if nf_data != po_data_pedido:
         divergencias.append(
            f"Data divergente. NF (emissão): {nf_data} | PO (pedido): {po_data_pedido}"
        )

    # Determinar status
    status = "divergente" if divergencias else "conciliado"

    return {
        "status": status,
        "divergencias": divergencias
    }
