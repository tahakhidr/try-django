import os
from .base import *

if os.environ.get("CURRENT_ENVIRON") == "DEV":
    from .dev import *
else:
    from .prod import *
