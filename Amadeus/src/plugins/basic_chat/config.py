from pydantic import BaseSettings


class Config(BaseSettings):
    # Your Config Here
    bc_data_path :str = ""

    class Config:
        extra = "ignore"
        case_sensitive = False