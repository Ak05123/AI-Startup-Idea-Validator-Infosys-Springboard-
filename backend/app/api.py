import asyncio
import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pathlib import Path
import traceback

from app.orchestrator import run_startup_validation


class ValidateRequest(BaseModel):
    ideaName: str
    country: str | None = None
    liveLocation: str | None = None
    budget: str | None = None
    industries: list[str] | None = None


class AdvisorRequest(BaseModel):
    question: str
    validationContext: dict


app = FastAPI(title="Startup Validator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
async def health():
    """Simple health check so the frontend / startup script can confirm
    the backend is up and ready to accept requests.
    """
    return {"status": "ok"}


@app.post("/api/validate")
async def validate(req: ValidateRequest):
    """Accept a structured request, build a canonical idea string, and run the
    existing validation pipeline. Returns the `shared_state` produced by the
    pipeline so the frontend can consume real data.
    """
    idea = req.ideaName.strip() if req.ideaName else ""
    # If additional fields are provided, append them to the idea to give agents context
    if req.country:
        idea += f"\nTarget country: {req.country}"
    if req.liveLocation:
        idea += f"\nLive location: {req.liveLocation}"
    if req.budget:
        idea += f"\nEstimated budget: {req.budget}"
    if req.industries:
        idea += f"\nIndustry: {', '.join(req.industries)}"

    try:
        # Run the synchronous pipeline in a thread to avoid blocking the event loop
        loop = asyncio.get_running_loop()
        shared_state = await loop.run_in_executor(None, run_startup_validation, idea)
        return shared_state
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/download-pdf")
async def download_pdf(path: str):
    """Return a generated PDF file given a path. The frontend can call this with
    the `pdf_status.path` returned in `shared_state` to retrieve the file.
    """
    try:
        file_path = Path(path)
        if not file_path.exists():
            raise HTTPException(status_code=404, detail="PDF not found")
        return FileResponse(path=str(file_path), media_type='application/pdf', filename=file_path.name)
    except HTTPException:
        raise
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
