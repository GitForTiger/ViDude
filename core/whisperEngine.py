import whisper
import os

def load_model(model_size):
    print(f"Loading Whisper model: {model_size} ...")
    model = whisper.load_model(model_size)
    print("Whisper model loaded.")
    return model

def transcribe_chunk(chunk_path: str, model) -> str:
    # We strictly use English here
    result = model.transcribe(chunk_path, task="transcribe", language="en")
    return result["text"]

def transcribe_all(chunks: list, config: dict) -> str:
    print("Initializing Whisper Engine...")
    model_size = config.get("whisper_model_size", "small")
    model = load_model(model_size)
    
    full_transcript = ""
    for i, chunk in enumerate(chunks):
        print(f"Transcribing chunk {i + 1}/{len(chunks)} via Whisper...")
        text = transcribe_chunk(chunk, model)
        full_transcript += text + " "
        
    print("Whisper Transcription Complete.")
    return full_transcript.strip()