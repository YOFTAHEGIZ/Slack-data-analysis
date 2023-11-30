from pymongo import MongoClient

def get_message_schema():
    return {
        "client_msg_id": str,
        "type": {"type": str, "required": True},
        "subtype": str,
        "ts": {"type": str, "required": True},
        "user": str,
        "text": str,
        "inviter": str,
        "blocks": [
            {
                "type": str,
                "block_id": str,
                "elements": [
                    {
                        "type": str,
                        "elements": [
                            {
                                "type": str,
                                "text": str,
                                "user_id": str,
                            }
                        ],
                    }
                ],
            }
        ],
        "team": str,
        "user_team": str,
        "source_team": str,
        "user_profile": {
            "avatar_hash": str,
            "image_72": str,
            "first_name": str,
            "real_name": str,
            "display_name": str,
            "team": str,
            "name": str,
            "is_restricted": bool,
            "is_ultra_restricted": bool,
        },
    }