from fastapi import FastAPI


app = FastAPI(title="Academic Ops API")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "academic-ops",
    }
