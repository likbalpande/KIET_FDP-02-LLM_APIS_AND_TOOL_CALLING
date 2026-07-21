from ai.chat_completion import chat_completion

messages = [
    {"role": "user", "content": "Help me with maths doubts"},
    # {"role": "assistant", "content": "..."},
    # {"role": "user", "content":"What is that concept of hospital?"}
]

reply = chat_completion(messages)

print(reply)
