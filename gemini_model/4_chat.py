from ai.chat_completion import chat_completion

while True:
    print('\n-----------------------\n')
    query = input("You: ")
    messages = [{"role": "user", "content": query}]

    reply = chat_completion(messages)
    print("AI:", reply) 


# Help me with maths doubts
# What is that concept of hospital?
