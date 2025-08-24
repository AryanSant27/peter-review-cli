from setuptools import setup, find_packages

setup(
    name="peter-review",
    version="0.1",
    packages=find_packages(),
    py_modules=["peter_review_cli", "code_review", "review_audio"],
    install_requires=[
        "simpleaudio==1.0.4",
        "TTS==0.22.0",
        "torch==2.5.1",
        "google-genai==1.31.0",
        "torchvision==0.20.1",
        "torchaudio==2.5.1",
    ],
    entry_points={
        "console_scripts": [
            "peter-review = peter_review_cli:main",
        ],
    },
)
