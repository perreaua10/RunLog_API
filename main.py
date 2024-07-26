from fastapi import FastAPI

app = FastAPI()


@app.get("/api/v1/hello")
async def root():
    return '''<!DOCTYPE html>
            <html>
            <body>

            <h1>My First Heading</h1>
            <p>My first paragraph.</p>

            </body>
            </html>'''

#hosted simply at https://runlog-api.onrender.com/docs