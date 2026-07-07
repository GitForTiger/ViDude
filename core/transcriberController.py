import json
import os
import whisper

# Import our isolated engines
from core import whisperEngine
from core import sarvamEngine

def load_config(config_path="core/config.json") -> dict:
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Missing {config_path}!")
    with open(config_path, "r") as file:
        return json.load(file)

def detect_language(chunk_path: str, model_size: str) -> str:
    """Uses Whisper to detect the language of the first 30 seconds."""
    print("🔍 Auto-detecting language...")
    
    # Load the model
    model = whisper.load_model(model_size)
    
    # Load the audio and trim it to 30 seconds
    audio = whisper.load_audio(chunk_path)
    audio = whisper.pad_or_trim(audio)
    
    # Create the spectrogram and detect
    mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)
    _, probs = model.detect_language(mel)
    
    # Get the highest probability language code (e.g., 'en', 'hi')
    detected_lang = max(probs, key=probs.get)
    print(f"🎯 Language detected: '{detected_lang}' (Probability: {probs[detected_lang]:.2f})")
    
    return detected_lang

def process_transcription(chunks: list) -> str:
    if not chunks:
        return ""

    config = load_config()
    whisper_model_size = config.get("whisper_model_size", "small")
    
    # Detect language using the first chunk
    detected_lang = detect_language(chunks[0], whisper_model_size)
    
    # Routing Logic: If Hindi ('hi'), use Sarvam. Else, use Whisper.
    if detected_lang == "hi":
        print("🔀 Routing to Sarvam AI engine...")
        return sarvamEngine.transcribe_all(chunks, config)
    else:
        print("🔀 Routing to local Whisper engine...")
        return whisperEngine.transcribe_all(chunks, config)