from message_schema import get_message_schema
def get_channel_schema():
    return {
        "name": str,
        "date": str,
        "messages": [get_message_schema()],
    }