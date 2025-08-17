from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

# TODO: import your routers here when ready
# from dashboard_routes import router as dashboard_router
# app.include_router(dashboard_router, prefix="/dashboard")
# from boq_routes import router as boq_router
# app.include_router(boq_router, prefix="/boq")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("server_fastapi:app", host="0.0.0.0", port=port)
