
try:
    from model.rest_api import RESTClient
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[1]))
    from model.rest_api import RESTClient

__all__ = [
    "RESTClient",
]