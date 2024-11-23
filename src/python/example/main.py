import os
from importlib.resources import _legacy


found_generated_txt = _legacy.is_resource("example", "generated.txt")
print(f"{os.getcwd()=}")
print(f"{found_generated_txt=}")
