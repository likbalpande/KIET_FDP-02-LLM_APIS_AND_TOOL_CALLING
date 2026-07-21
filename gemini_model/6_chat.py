from ai.chat_completion import chat_completion

messages = []

while True:
    print('\n-----------------------\n')
    query = input("You: ")
    messages.append({"role": "user", "content": query})

    reply = chat_completion(messages)
    print("AI:", reply)

    messages.append({"role": "model", "content": reply})


# Help me with maths doubts
# What is that concept of hospital?