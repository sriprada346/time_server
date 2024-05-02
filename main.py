from fastapi import FastAPI
from typing import List
import time
import uvicorn

app = FastAPI()
current_time = time.time()

def update_time():
    global current_time
    while True:
        current_time = time.time()
        time.sleep(1)  # Sleep for 1 second

@app.get("/time")
async def get_current_time():
    global current_time
    formatted_time = time.strftime("%H:%M:%S", time.localtime(current_time))
    milliseconds = int((current_time - int(current_time)) * 1000)
    formatted_time_with_ms = f"{formatted_time}:{milliseconds:03d}"
    return formatted_time_with_ms


    
