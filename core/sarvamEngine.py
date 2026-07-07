import os
import requests
from pydub import AudioSegment

SARVAM_PIECE_SECONDS = 25
SARVAM_STT_TRANSLATE_URL = "https://api.sarvam.ai/speech-to-text-translate"
SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")

def _send_to_sarvam(piece_path: str, model_name: str) -> str:
    headers = {"api-subscription-key": SARVAM_API_KEY}
    with open(piece_path, "rb") as f:
        files = {"file": (os.path.basename(piece_path), f, "audio/wav")}
        data = {"model": model_name, "with_diarization": "false"}
        response = requests.post(
            SARVAM_STT_TRANSLATE_URL,
            headers=headers,
            files=files,
            data=data,
            timeout=120,
        )

    if not response.ok:
        print(f"\n❌ Sarvam returned {response.status_code}")
        response.raise_for_status()

    return response.json().get("transcript", "")

def transcribe_chunk(chunk_path: str, model_name: str) -> str:
    if not SARVAM_API_KEY:
        raise RuntimeError("SARVAM_API_KEY is not set in environment variables.")

    audio = AudioSegment.from_wav(chunk_path)
    piece_ms = SARVAM_PIECE_SECONDS * 1000
    full_text = ""
    total_pieces = (len(audio) + piece_ms - 1) // piece_ms

    for i, start in enumerate(range(0, len(audio), piece_ms)):
        piece = audio[start: start + piece_ms]
        piece_path = f"{chunk_path}_sv_{i}.wav"
        piece.export(piece_path, format="wav")

        try:
            print(f"  → Sarvam processing piece {i + 1}/{total_pieces} ...")
            full_text += _send_to_sarvam(piece_path, model_name) + " "
        finally:
            if os.path.exists(piece_path):
                os.remove(piece_path)

    return full_text.strip()

def transcribe_all(chunks: list, config: dict) -> str:
    print("Initializing Sarvam AI Engine...")
    model_name = config.get("sarvam_model", "saaras:v2.5")
    
    full_transcript = ""
    for i, chunk in enumerate(chunks):
        print(f"Transcribing chunk {i + 1}/{len(chunks)} via Sarvam...")
        text = transcribe_chunk(chunk, model_name)
        full_transcript += text + " "
        
    print("Sarvam Transcription Complete.")
    return full_transcript.strip()