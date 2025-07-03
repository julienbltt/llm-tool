# llm-tool

This tool provides an API for the Commpanion integration system to interact with LLM models loaded into LM Studio. A simple voice-enabled chatbot powered by [LM Studio](https://lmstudio.ai/), with streaming language model responses and real-time text-to-speech (TTS) synthesis using `pyttsx3`.

## Features

* Sentence-by-sentence streaming response with LM Studio
* Real-time text-to-speech using `pyttsx3`
* Easy model and system prompt selection
* Command-line interaction loop
* API integration for the Commpanion system

## Installation

Install dependencies:
```bash
pip install lmstudio pyttsx3
```

Follow the [LM Studio installation guide](https://lmstudio.ai/). Then you can install any LLM and run your server with your model loaded.

## System Requirements

* Only tested on Python 3.10
* LM Studio installed with the local server running and a model loaded on it
* Supported OS: Windows, Linux, macOS

## Demo

Start the assistant:
```bash
python main.py
```

You'll be prompted to:
* Choose a model ID (e.g., `mistral-7b-instruct-v0.1`, `phi-3-mini-4k-instruct`). The chosen model has to be download on the computer.
* Enter a system prompt (e.g., `"Answer in one sentence"`)

Then, begin chatting! The assistant will speak the response aloud.

### Example

```text
Enter a model id:
mistral-7b-instruct-v0.1
Enter a system prompt:
Answer concisely.
Enter your message: What is the capital of Japan?
🎤 Vocal synthesis:: The capital of Japan is Tokyo.
Response time: 4.831 seconds
```

## Using the Class Directly

You can also use the LMStudioResponder class directly in your own scripts.

```python
from lmsClass import LMStudioResponder

# Create an instance
llm = LMStudioResponder(model_name="mistral-7b-instruct-v0.1", system_prompt="Answer concisely.")

# Get and speak a response
prompt = "What is the capital of Japan?"
response = llm.respond_and_speak(prompt)
```

## Repository

The latest version of this project is available at: https://github.com/julienbltt/llm-tool

## Authors

* **MattDff** – initial development
* **Commpanion Team** – integration and optimization

For more info on pyttsx3 or LM Studio, visit [https://pypi.org/project/pyttsx3/](https://pypi.org/project/pyttsx3/) and [https://lmstudio.ai](https://lmstudio.ai).