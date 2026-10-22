"""Inspect one ASCII teaching word with a named tokenizer; no model API call."""
import sys
import tiktoken
text=sys.argv[1]
enc=tiktoken.get_encoding('cl100k_base')
ids=enc.encode(text)
assert enc.decode(ids)==text
pieces=[enc.decode_single_token_bytes(i).decode('utf-8') for i in ids]
print('pieces: '+' | '.join(pieces))
print('tokens: '+str(len(ids)))
