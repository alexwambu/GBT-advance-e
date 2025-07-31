from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import shutil
from deploy_logic import handle_deployment

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="backend/static"), name="static")

@app.post("/deploy/")
async def deploy_app(repo_url: str = Form(...), domain: str = Form(...), logo: UploadFile = None):
    logo_path = "backend/static/logo/logo.png"
    if logo:
        with open(logo_path, "wb") as f:
            shutil.copyfileobj(logo.file, f)
    return handle_deployment(repo_url, domain)
