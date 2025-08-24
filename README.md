# peter-review cli

This tool is a cli tool specifically designed to give you a code review in the voice of Peter Griffin himself from Family Guy. It uses TTS under the hood. This is literally the first version so it is heavy in size. The TTS model used is 1.7gb and it uses PyTorch 2.5.1 which is 2.7gb as-well. Without a doubt, it is slow but that is something fixable and something I will work on.


# Flow
The flow of this tool is such that when we call the tool, it scrapes the code file first and with that code and a system prompt, it makes an API call to Gemini which provides a Peter-style code review. The review text is then passed to the audio generation pipeline and we get the audio file saved in the output directory.


## Steps to install

First clone this repository 

```bash
git clone https://github.com/AryanSant27/peter-review-cli
```
Then 
```bash
cd peter-review-cli
```
And
```bash
pip install .
```
**NOTE: This strictly works on Python 3.10.11**

This will install it globally in your system, however I won't recommend that and install this in a virtual environment

So instead create a virtual env first with
```bash
python3.10 -m venv venv
```
then activate the venv and install it using 

```bash
pip install .
```
## Usage

Using it is really easy, even if it is confined in a virtual environment
First activate the virtual environment for this

```bash
venv\Scripts\activate
```
Then,
```bash
peter-review path\to\your\code\file.extension
```

**This will generate a text only review for the provided code**
To get the Audio also

```bash
peter-review path\to\your\code\file.extension --audio
```

**This will play the audio in the terminal itself, although it takes a roughly 40-50 seconds**



