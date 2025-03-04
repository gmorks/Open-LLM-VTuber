from dataclasses import dataclass
from typing import Optional

@dataclass
class TwitchConfig:
    enabled: bool = False
    token: str = ""
    channel: str = ""
    bot_name: str = ""
    client_id: str = ""
    prefix: str = "!"

    @classmethod
    def from_dict(cls, config: dict) -> 'TwitchConfig':
        return cls(
            enabled=config.get('enabled', False),
            token=config.get('token', ''),
            channel=config.get('channel', ''),
            bot_name=config.get('bot_name', ''),
            client_id=config.get('client_id', ''),
            prefix=config.get('prefix', '!')
        )