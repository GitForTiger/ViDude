from utils.audioProcessor import process_input
from core.transcriberController import transcribe_all

source = "https://youtu.be/dbIF8h5f87Q?si=lwtafZBeFx8xwvUH"

chunks = process_input(source)

print(transcribe_all(chunks, True))