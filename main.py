from openai import OpenAI
import json                                          import sys
import os

cfg_path = os.path.join(os.path.dirname(__file__), 'config.json')
cfg = json.loads(open(cfg_path, 'r').read())

client = OpenAI(
  base_url = cfg["base-url"],
  api_key = cfg["api-key"]
)
                                                     sys_prompt = cfg["main-prompt"]
if len(sys.argv) > 1:                                   sys_prompt = cfg[sys.argv[1]+"-prompt"]
                                                     msgs = []

def get_msg(content):                                  return client.chat.completions.create(
    model=cfg["model"],
    messages=[{"role":"system","content":sys_prompt}]+content,
    temperature=0.2,
    top_p=0.7,
    max_tokens=4096,
    stream=True
  )

if len(sys.argv) > 2:
  msg = {"role":"user","content":sys.argv[2]}
  completion = get_msg([msg])
  print("answer: ", end="")
  for chunk in completion:
    ch = chunk.choices[0].delta.content
    if ch is not None:
      print(ch, end="")
  print('\n')
  exit()

os.system("clear")

while True:
  tx = input(">>> ")
  if tx == "!clear":
    os.system("clear")
    msgs = []
    continue

  if tx == "!exit":
    exit()

  msg = {"role":"user","content":tx}
  msgs.append(msg)
  completion = get_msg(msgs)
  print("answer: ", end="")
  assis_tx = ""

  for chunk in completion:
    ch = chunk.choices[0].delta.content
    if ch is not None:
      assis_tx += ch
      print(ch, end="")
  assis_msg = {"role":"assistant","content":assis_tx}

  msgs.append(assis_msg)
  if len(msgs) > 12: msgs = msgs[-12:]
  print("\n")
