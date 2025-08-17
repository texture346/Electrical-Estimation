[DEPLOY_README.md](https://github.com/user-attachments/files/21822026/DEPLOY_README.md)
# Quick deploy (GitHub → Railway)

1) **Rename Procfile_fastapi → Procfile**.
2) Push to GitHub:
   ```bash
   git init && git add . && git commit -m "Deploy"
   git branch -M main
   git remote add origin https://github.com/USERNAME/REPO.git
   git push -u origin main
   ```
3) Railway → New Project → Deploy from GitHub
   - Build: `pip install -r requirements_fastapi.txt`
   - Start: `gunicorn -k uvicorn.workers.UvicornWorker server_fastapi:app --workers 2 --timeout 120`
4) Open the Railway URL → test `/health`.
5) (Optional) Set CORS origins and your ENV VARS in Railway settings.
