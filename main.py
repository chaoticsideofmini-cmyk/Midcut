from fastapi import FastAPI
from routes import process_route, result_route, feature_route

app = FastAPI(title="MidCut AI V1 Backend")

# Include routers
app.include_router(process_route.router)
app.include_router(result_route.router)
app.include_router(feature_route.router)

@app.get("/")
async def root():
    return {"message": "MidCut AI V1 Backend Running Successfully!"}
