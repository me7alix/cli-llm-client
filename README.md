# CLI LLM client
A CLI LLM client based on the openai library written in python


## Installation
Download repository
```
git clone https://github.com/me7alix/cli-llm-client
```
Then add this line to startup file (~/.bashrc, ~/.zshrc, etc) to have access to the program everywhere
```
alias ast="python ~/cli-llm-client/main.py"
```

## Usage
The second argument specifies the name of the system script (they can be added to config.json). The third argument is specified in order to immediately execute the request (without starting a chat)
```
# running using system prompt
ast
# running using specific system prompt
ast tr
# running without starting a chat
ast n "the longest river in the world"
# you can also do it like this
ast n the longest river in the world
```

## Commands
Use `!clear` to clear the chat and context. Use `!exit` to exit the chat.

## Adding system prompts
To add a new system prompt, open the project directory
```
cd ~/cli-llm-client
```
Then open `config.json` file in some text editor (I'm using nano as an example)
```
nano config.json
```
Add a new system prompt in a similar way
```
"[prompt name]-prompt":"[your prompt]"
```
