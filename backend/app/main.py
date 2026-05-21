# pyrefly: ignore [missing-import]
from fastapi import FastAPI
# pyrefly: ignore [missing-import]
from fastapi.middleware.cors import CORSMiddleware
from app.routes import reconciliation

app = FastAPI(
    title="AuditBot API",
    description="API para o sistema de automação financeira AuditBot (MVP Mock)",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui as rotas de conciliação
app.include_router(reconciliation.router)

@app.get("/health", tags=["Health"])
def health_check():
    """
    Endpoint simples para verificar se a API está online.
    """
    return {"status": "online", "message": "AuditBot API is running"}
