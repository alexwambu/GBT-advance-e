import subprocess

def handle_deployment(repo_url, domain):
    try:
        subprocess.run(["git", "clone", repo_url, "deployed_app"], check=True)
        # Inject logo logic or modify app here
        return {
            "status": "success",
            "url": f"https://{domain}",
            "message": f"App deployed at https://{domain}"
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
