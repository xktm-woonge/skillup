try:
    from utils.security import hash_password
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[1]))
    from utils.security import hash_password

__all__ = [
    "hash_password",
]