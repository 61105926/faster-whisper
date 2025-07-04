from fastapi import FastAPI, File, UploadFile
from faster_whisper import WhisperModel
import tempfile

app = FastAPI()

# Carga el modelo una vez al iniciar
model = WhisperModel("small", device="cpu", compute_type="int8")

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    # Guarda el archivo temporalmente
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name

    segments, info = model.transcribe(tmp_path, language="es")
    text = " ".join([seg.text for seg in segments])
    
    return {
        "language": info.language,
        "text": text
    }

# Agregamos esto para correr directamente con python main.py si quieres probar local
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001)
