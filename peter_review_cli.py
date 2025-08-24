import argparse
import os
from code_review import review
from review_audio import test_natural_voice
import simpleaudio as sa  # pip install simpleaudio


def main():
    parser = argparse.ArgumentParser(
        description="Peter Griffin style code reviewer CLI tool"
    )
    parser.add_argument(
        "file",
        type=str,
        help="Path to the code file to review"
    )
    parser.add_argument(
        "--audio",
        action="store_true",
        help="Also generate and play Peter Griffin voice audio of the review"
    )
    args = parser.parse_args()

    # Read file contents
    if not os.path.exists(args.file):
        print(f"❌ File not found: {args.file}")
        return

    with open(args.file, "r", encoding="utf-8") as f:
        code_text = f.read()

    # Get review
    review_text = review(code_text)

    if review_text:
        print("===== 📋 Peter Review =====")
        print(review_text)

        # Optionally generate audio and play it
        if args.audio:
            audio_path = test_natural_voice(review_text)
            if audio_path and os.path.exists(audio_path):
                print("🔊 Playing audio...")
                wave_obj = sa.WaveObject.from_wave_file(audio_path)
                play_obj = wave_obj.play()
                play_obj.wait_done()  # block until playback finishes
    else:
        print("❌ Failed to generate review.")


if __name__ == "__main__":
    main()
