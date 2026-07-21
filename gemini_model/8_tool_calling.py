from google.genai import types

from ai.chat_completion_with_tools import chat_completion_with_tools


def send_email(to, subject, body):
    print(f"Sending email to {to} | subject: {subject} | body: {body}")
    print("----------\n✅ Email sent!\n----------")
    return "Email sent"


def read_emails(count=5):
    return [f"Email {i + 1}" for i in range(count)]


def sum(a, b):
    return a + b


def multiple(a, b):
    return a * b


available_functions = {
    "send_email": send_email,
    "read_emails": read_emails,
    "sum": sum,
    "multiple": multiple,
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "send_email",
            "description": "Send an email to someone",
            "parameters": {
                "type": "object",
                "properties": {
                    "to": {"type": "string"},
                    "subject": {"type": "string"},
                    "body": {"type": "string"},
                },
                "required": ["to", "subject", "body"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_emails",
            "description": "Read the latest emails from the inbox",
            "parameters": {
                "type": "object",
                "properties": {"count": {"type": "integer"}},
                "required": [],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "sum",
            "description": "Add two numbers",
            "parameters": {
                "type": "object",
                "properties": {"a": {"type": "number"}, "b": {"type": "number"}},
                "required": ["a", "b"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "multiple",
            "description": "Multiply two numbers",
            "parameters": {
                "type": "object",
                "properties": {"a": {"type": "number"}, "b": {"type": "number"}},
                "required": ["a", "b"],
            },
        },
    },
]


def print_reply(message):
    for part in message.parts:
        if part.text:
            print("AI:", part.text)

messages = []

while True:
    
    query = input("\nYou: ")
    messages.append({"role": "user", "content": query})

    message = chat_completion_with_tools(messages, tools)
    messages.append(message)  # the model's turn, holding its function call(s)

    tool_was_called = False
    for part in message.parts:
        if part.function_call:
            tool_was_called = True
            name = part.function_call.name
            args = part.function_call.args
            result = available_functions[name](**args)
            print(f"\n------ function call ------")
            print(f"{name}({args}) -> {result}")
            print(f"------ ------\n")

            response_part = types.Part.from_function_response(name=name, response={"result": result})
            messages.append(types.Content(role="user", parts=[response_part]))

    if tool_was_called:
        message = chat_completion_with_tools(messages, tools)  # let the ai use the tool output

    print_reply(message)
