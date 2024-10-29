from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/sleep")
def sleep_endpoint():
    time.sleep(5)
    return {"message": "Slept for 5 seconds"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)