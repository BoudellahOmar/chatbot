# My OpenAI Chatbot

This is a simple AI chatbot built using the OpenAI GPT API. You can run it from your terminal and start chatting right away

## Requirements

- Python 3.6+
- OpenAI account + API key
- Internet connection

## How to Use

1. Clone this repository:

```bash
git clone https://github.com/BoudellahOmar/chatbot.git
cd chatbot
```

2. Install dependencies:

```bash
pip install openai
```

3. Add your OpenAI API key in `chatbot.py`:

```python
openai.api_key = "your-api-key-here"
```

4. Run the chatbot:

```bash
python chatbot.py
```

5. Start chatting! Type `exit` to quit.

## Customize Your Bot

Change the bot’s personality by editing this line:

```python
{"role": "system", "content": "You are a helpful assistant."}
```

Examples:
- `"You are a sarcastic robot."`
- `"You are a coding tutor for Python beginners."`

## License

This project is MIT licensed. Feel free to fork and improve it!
