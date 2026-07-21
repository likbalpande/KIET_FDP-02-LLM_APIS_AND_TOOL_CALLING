from ai.chat_completion import chat_completion

messages = [
    {"role": "user", "content": "Help me with maths doubts"},
    # {"role": "model", "content": "..."},
    # {"role": "user", "content":"What is that concept of hospital?"}
]

reply = chat_completion(messages)

print(reply)
