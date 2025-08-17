web: gunicorn -k uvicorn.workers.UvicornWorker server_fastapi:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120
