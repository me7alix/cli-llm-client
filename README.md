# CLI LLM client
A CLI LLM client based on the openai library written in python

## Installation
Download repository
```
git clone https://github.com/Proger-3301/cli-llm-client
```
Then add this line to startup file (~/.bashrc, ~/.zshrc, etc) to have access to the program everywhere
```
alias ast="python ~/cli-llm-client/main.py"
```

## Usage
The second argument specifies the name of the system script (they can be added to config.json). The third argument is specified in order to immediately execute the request (without starting a chat)
```
// running using system prompt
ast
// running using specific system prompt
ast tr
// running without starting a chat
ast n "the longest river in the world"
```


