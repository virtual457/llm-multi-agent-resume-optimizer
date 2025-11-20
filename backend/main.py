"""
Main FastAPI Application for LLM Multi-Agent Resume Optimizer
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="LLM Multi-Agent Resume Optimizer",
    description="Autonomous resume generation and optimization using multi-agent AI",
    version="0.1.0"
)

# CORS configuration for frontend
cors_origins = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import routes
from api import routes

# Include API routes
app.include_router(routes.router, prefix="/api", tags=["api"])


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "online",
        "service": "LLM Multi-Agent Resume Optimizer",
        "version": "0.1.0"
    }


@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "llm_provider": os.getenv("LLM_PROVIDER", "not_configured"),
        "backend": "operational"
    }


if __name__ == "__main__":
    import uvicorn
    
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    debug = os.getenv("DEBUG", "True").lower() == "true"
    
    print(f"🚀 Starting LLM Multi-Agent Resume Optimizer")
    print(f"📍 Server: http://{host}:{port}")
    print(f"🔧 Debug mode: {debug}")
    print(f"🤖 LLM Provider: {os.getenv('LLM_PROVIDER', 'not configured')}")
    
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=debug
    )
