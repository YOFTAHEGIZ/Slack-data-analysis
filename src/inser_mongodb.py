import os
import sys

rpath = os.path.abspath('..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

import mongo_connection as mc
from src.loader import SlackDataLoader
from message_schema import get_message_schema
from channel_schema import get_channel_schema

def insert_messages_into_channel(channel_name, date, messages):
    db = mc.get_database()
    channels_collection = db["channels_data"]
    
    channel_data = {
        "name": channel_name,
        "date": date,
        "messages": messages,
    }
    
    channels_collection.insert_one(channel_data)

def read_files():
    sl = SlackDataLoader()
    js_files = sl.read_json_files()

    for file in js_files:
        for channel_name in file:
            for d in file[channel_name]:
                for json_data in d['msg']:
                    client_msg_id = json_data.get('client_msg_id')
                    type_ = json_data.get('type')
                    subtype = json_data.get('subtype')
                    ts = json_data.get('ts')
                    user = json_data.get('user')
                    text = json_data.get('text')
                    blocks = json_data.get('blocks', [])
                    team = json_data.get('team')
                    user_team = json_data.get('user_team')
                    source_team = json_data.get('source_team')
                    user_profile = json_data.get('user_profile', {})

                    message_schema = get_message_schema()
                    mapped_message = {
                        "client_msg_id": client_msg_id,
                        "type": type_,
                        "subtype": subtype,
                        "ts": ts,
                        "user": user,
                        "text": text,
                        "blocks": blocks,
                        "team": team,
                        "user_team": user_team,
                        "source_team": source_team,
                        "user_profile": user_profile,
                    }

                    insert_messages_into_channel(channel_name, d['sent_date'], [mapped_message])

if __name__ == "__main__":
    read_files()