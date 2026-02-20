from datetime import datetime
import tomllib
from typing import List
from DataModels.AppConfigurationModels.ConfigurationFileModel import Host


def config_reader(file_path: str) -> List[Host] | None:
    try:
        with open(file_path, "rb") as f:
            data = tomllib.load(f)
            result = [Host(name=name, **params) for name, params in data.items()]
            return result

    except FileNotFoundError:
        print(f"{datetime.now()} -- File {file_path} is not found")
        return None
    except tomllib.TOMLDecodeError as e:
        print(f"{datetime.now()} -- Error parsing TOML file: {e}")
        return None
    except PermissionError:
        print(f"{datetime.now()} -- Permission denied {file_path}")
        return None
    except Exception as e:
        print(f"{datetime.now()} -- Unexpected error: {e}")
        return None

def get_checkout_interval(interval: str = "600s"):
    h = m = s = 60
    unit = interval[-1].lower()
    sleep_time = interval[:-1]
    print(f"{unit}\n")
    print(f"{sleep_time}")

    if unit == "h": return float(sleep_time*h*m*s)
    elif unit == "m": return float(sleep_time*m*s)
    elif unit == "s": return float(sleep_time*s)