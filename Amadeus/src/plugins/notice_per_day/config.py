from pydantic import BaseSettings, Extra, Field


class Config(BaseSettings):
    # plugin custom config
    plugin_setting: str = "default"

    npd_qq_friends: list = []
    npd_qq_groups: list = []


    class Config:
        extra = Extra.allow
        case_sensitive = False