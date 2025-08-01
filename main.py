from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import shutil
from deploy_logic import handle_deployment  # ✅ correct spelling

app = FastAPI()

# Allow frontend requests (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve uploaded logos statically
app.mount("/static", StaticFiles(directory="backend/static"), name="static")

@app.post("/deploy/")
async def deploy_app(
    repo_url: str = Form(...),
    domain: str = Form(...),
    logo: UploadFile = None
):
    logo_path = "backend/static/logo/logo.png"
    
    # Save uploaded logo if provided
    if logo:
        with open(logo_path, "wb") as f:
            shutil.copyfileobj(logo.file, f)

    # Run deployment logic
    return handle_deployment(repo_url, domain)
