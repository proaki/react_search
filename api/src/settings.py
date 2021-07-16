import os
from dotenv import load_dotenv


# Load .ENV file
# After this, you can access to environment like os.environ.get("VAR")
def load_config(env_file_path: str):
    if not os.path.exists(env_file_path):
        assert f".ENV file does not exist on {env_file_path}"
    load_dotenv(dotenv_path=env_file_path)
