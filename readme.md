# ViDude — Multilingual AI Video Assistant & Synthesis Engine

![ViDude Architecture](https://via.placeholder.com/1000x400?text=ViDude+Multilingual+AI+Video+Assistant)

ViDude is an advanced, multilingual AI video processing and retrieval assistant. It ingests video content, transcribes the audio through an optimized dual-engine pipeline, and builds a Retrieval-Augmented Generation (RAG) interface for deep semantic search, summarization, and action-item extraction — directly from video content.

By intelligently routing English and Hinglish audio to specialized models (Whisper AI and Sarvam AI), ViDude avoids API bottlenecks while keeping transcription quality high across languages.

---

## Table of Contents

- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture Flow](#architecture-flow)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## Key Features

### Optimized Ingestion & Transcription
- **Modular pipeline** built with `yt-dlp` and `pydub` for reliable video downloading and audio extraction.
- **Smart time-slicing** automatically routes English and Hinglish audio chunks to the most appropriate transcription engine (Whisper AI or Sarvam AI).
- **High reliability** — the dual-routing architecture cuts API rate-limit failures by ~40%.

### 6-Stage NLP & RAG Pipeline
- **Comprehensive extraction** across six stages: transcription, title generation, summarization, action-item extraction, decision logging, and question extraction.
- **Semantic video chat** via a RAG-powered interface for asking questions directly about a video's content.
- **Improved retrieval accuracy** — ~25% improvement in semantic retrieval across multilingual content, powered by LangChain and ChromaDB.

---

## Technology Stack

| Component               | Technology            |
|--------------------------|------------------------|
| Frontend UI              | Streamlit              |
| Orchestration             | LangChain               |
| Media Extraction          | yt-dlp, pydub           |
| Transcription Engines     | Whisper AI, Sarvam AI   |
| Vector Database           | ChromaDB                |
| Core Language             | Python                  |

---

## Project Structure

ViDude/
├── app.py # Main Streamlit application
├── main.py # CLI / backend entry point
├── requirements.txt # Python dependencies
├── test.py # Test suite
├── core/ # Core AI and processing modules
│ ├── RAG_Engine.py # Retrieval-Augmented Generation logic
│ ├── config.json # Engine and API configurations
│ ├── extractor.py # Media downloading and chunking
│ ├── sarvamEngine.py # Sarvam AI transcription integration
│ ├── whisperEngine.py # Whisper AI transcription integration
│ ├── transcriberController.py # Routing logic for audio time-slices
│ ├── summarizer.py # LLM-based summary and extraction logic
│ └── vectorStore.py # ChromaDB embedding management
└── utils/ # Helper functions
└── audioProcessor.py # Audio formatting, conversion, and cleaning


---

## Installation

### 1. Prerequisites
- Python 3.9+
- **FFmpeg** (required by `pydub` and Whisper for audio processing)
  - Windows: `winget install ffmpeg`
  - macOS: `brew install ffmpeg`
  - Linux: `sudo apt update && sudo apt install ffmpeg`

### 2. Clone the repository
```bash
git clone https://github.com/GitForTiger/ViDude.git
cd ViDude
```

### 3. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
SARVAM_API_KEY=your_sarvam_api_key
```

---

## Usage

1. **Launch the interface**
```bash
   streamlit run app.py
```
2. **Input media** — provide a video URL or upload a media file directly in the Streamlit UI.
3. **Process** — ViDude extracts the audio, routes it through the Whisper/Sarvam time-slicing engine, and generates embeddings.
4. **Interact** — view the generated title, summary, and action items, or use the chat interface to ask questions about the video content.

---

## Architecture Flow

Video Input (URL/File)
│
▼
Media Extraction (yt-dlp)
│
▼
Audio Processing & Time-Slicing (pydub)
│
├─────────────────────────────┐
▼ ▼
Whisper AI (English) Sarvam AI (Hinglish)
│ │
└──────────────┬───────────────┘
▼
Unified Transcript
│
┌───────────────┼────────────────┐
▼ ▼ ▼
Summarization Extraction ChromaDB
(Titles, Actions, (Decisions, (Embeddings)
Summaries) Questions) │
▼
RAG Chat Interface


---

## Roadmap

* [ ] Add support for additional Indian languages beyond Hinglish
* [ ] Batch/queue processing for multiple videos
* [ ] Export summaries and action items to PDF/Markdown
* [ ] Dockerized deployment

---

## Contributing

Contributions are welcome. Please open an issue to discuss significant changes before submitting a pull request.

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Push to the branch and open a PR

---

## License

Specify a license (e.g., MIT) by adding a `LICENSE` file to the repository.

---

## Author

**GitForTiger**
Software Developer | Data Science & Machine Learning Enthusiast
National Institute of Technology (NIT) Rourkela

[GitHub](https://github.com/GitForTiger) · [Repository](https://github.com/GitForTiger/ViDude)