# don't touch this, unless you have a better way to do this

import os
import importlib

async def load_events(bot):
    folder = os.path.dirname(__file__)
    for filename in os.listdir(folder):
        if filename.endswith(".py") and filename not in ("__init__.py", "e_handler.py"):
            module_name = f"{__package__}.{filename[:-3]}"  # e.g., events.on_ready
            module = importlib.import_module(module_name)

            if hasattr(module, "setup"):
                print(f"Loaded: {module_name}")
                await module.setup(bot)
