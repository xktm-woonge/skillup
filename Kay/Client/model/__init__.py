
try:
    from model.rest_api import RESTClient
    from model.websocket_communication import RealtimeCommunication
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[1]))
    from model.rest_api import RESTClient
    from model.websocket_communication import RealtimeCommunication

__all__ = [
    "RESTClient",
    "RealtimeCommunication",
]