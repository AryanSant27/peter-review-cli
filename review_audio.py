import torch
from TTS.api import TTS
import os

# Simple test script for immediate results

def test_natural_voice(text):
    # Initialize TTS
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")

    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

    reference_audio = "clean.wav"



    output_file = r"output\review.wav"

    try:
        tts.tts_to_file(
            text=text,
            speaker_wav=reference_audio,
            language="en",
            file_path=output_file,
            temperature=0.6,
            length_penalty=1.0,
            repetition_penalty=5.0,
            top_k=50,
            top_p=0.8,
            speed=1.0
            )
        print(f"✅ Generated: {output_file} ")
        return output_file

    except Exception as e:
        print(f"❌ Error: {e}")
        return None


if __name__ == "__main__":
    text = "This is a sample text for review."
    test_natural_voice(text)


