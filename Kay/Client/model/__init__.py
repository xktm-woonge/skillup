
try:
    from model.rest_api import RESTClient
    from model.realtime_communication import RealTimeClient
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[1]))
    from model.rest_api import RESTClient
    from model.realtime_communication import RealTimeClient

__all__ = [
    "RESTClient",
    "RealTimeClient",
]