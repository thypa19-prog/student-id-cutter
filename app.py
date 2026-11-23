import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, Response
from rembg import remove, new_session
import uvicorn

app = FastAPI()

# ប្រើម៉ូដែល silueta (43MB) ដើម្បីកុំឱ្យលើស RAM 512MB របស់ Render
my_session = new_session("silueta")

@app.get("/")
async def read_index():
    return FileResponse("index.html")

@app.post("/api/cut-image")
async def cut_image(file: UploadFile = File(...)):
    input_image = await file.read()
    output_image = remove(input_image, session=my_session)
    return Response(content=output_image, media_type="image/png")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
