from pydantic import BaseSettings


class Config(BaseSettings):
    # Your Config Here
    bs_uids: dict

    class Config:
        extra = "ignore"
        case_sensitive = False