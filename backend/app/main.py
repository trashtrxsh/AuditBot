from fastapi import FastAPI
from app.routes import reconciliation

app = FastAPI(
    title="AuditBot API",
    description="API para o sistema de automação financeira AuditBot (MVP Mock)",
    version="0.1.0"
)

# Inclui as rotas de conciliação
app.include_router(reconciliation.router)

@app.get("/health", tags=["Health"])
def health_check():
    """
    Endpoint simples para verificar se a API está online.
    """
    return {"status": "online", "message": "AuditBot API is running"}
