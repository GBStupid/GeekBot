#same w/ the event handler, don't touch this (though its essentially the same)

import os
import importlib
import inspect

async def load_commands(bot):
    folder = os.path.dirname(__file__)
    for filename in os.listdir(folder):
        if filename.endswith(".py") and filename not in ("__init__.py", "c_handler.py"):
            module_name = f"{__package__}.{filename[:-3]}"
            module = importlib.import_module(module_name)

            setup_func = getattr(module, "setup", None)
            if setup_func:
                if inspect.iscoroutinefunction(setup_func):
                    print(f"Loaded: {module_name}")
                    await setup_func(bot)
                else:
                    setup_func(bot)
