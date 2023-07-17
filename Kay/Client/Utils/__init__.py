
try:
    from utils.font import get_NotoSan_font
    from utils import client_logManager as clmn
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[1]))
    from utils.font import get_NotoSan_font
    from utils import client_logManager as clmn

__all__ = [
    "get_NotoSan_font",
    "clmn",
]