from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, Response
from rembg import remove, new_session
import uvicorn

app = FastAPI()

# ប្រើម៉ូដែល u2net_human_seg ដែលកាត់សក់មនុស្សបានស្អាត និងលឿនលើ Cloud
my_session = new_session("u2net_human_seg")

@app.get("/")
async def read_index():
    return FileResponse("index.html")

@app.post("/api/cut-image")
async def cut_image(file: UploadFile = File(...)):
    input_image = await file.read()
    output_image = remove(input_image, session=my_session)
    return Response(content=output_image, media_type="image/png")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
