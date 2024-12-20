from fastapi import FastAPI
from app.routers import auth, summarize
import firebase_admin
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(summarize.router)

@app.get("/")
async def root():
    return {
            "Current App Name:":firebase_admin.get_app().project_id,
            "message": "Welcome to the SimpliLaw Backend API"}