from fastapi import FastAPI

app = FastAPI(title="MCP AI Dashboard API")


@app.get("/health")
async def health():
    return {"status": "ok"}
