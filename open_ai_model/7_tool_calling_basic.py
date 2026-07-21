import json

from ai.chat_completion_with_tools import chat_completion_with_tools


def send_email(to, subject, body):
    print(f"Sending email to {to} | subject: {subject} | body: {body}")
    return "----------\n✅ Email sent!\n----------"


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

query = input("You: ")
messages = [{"role": "user", "content": query}]

message = chat_completion_with_tools(messages, tools)

if message.tool_calls:
    for tool_call in message.tool_calls:
        name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)
        result = available_functions[name](**args)
        print(f"--- function call ---")
        print(f"{name}({args}) -> {result}")
        print(f"--- ---")
else:
    print("AI: ", message.content)
