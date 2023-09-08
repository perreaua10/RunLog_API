from fastapi import FastAPI

app = FastAPI()


@app.get("/api/v1/hello")
async def root():
    return {"message": "Hello World what is going on here"}

#hosted simply at https://runlog-api.onrender.com/docs