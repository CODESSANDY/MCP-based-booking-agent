from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.crew_runner import run_booking_agent
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Log every request
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    logger.info("Root endpoint called")
    return {"message": "API is working!", "status": "healthy"}

@app.post("/search")
async def search(request: Request):
    logger.info("=" * 50)
    logger.info("SEARCH ENDPOINT CALLED")
    print("=" * 50)
    print("SEARCH ENDPOINT CALLED")
    try:
        data = await request.json()
        logger.info(f"Received data: {data}")
        print(f"Received data: {data}")
        result = run_booking_agent(data)
        logger.info(f"Result: {result}")
        print(f"Result: {result}")
        return {"result": result}
    except Exception as e:
        logger.error(f"ERROR: {type(e).__name__}: {e}")
        print(f"ERROR: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        raise