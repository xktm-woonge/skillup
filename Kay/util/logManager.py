import os
import sys
import logging
from pathlib import Path
from datetime import datetime

def Init():
    __init_timestamp()
    __init_logger()
    HLOG.debug("LogManager Init function called !!!")

def __init_timestamp():
    """ 타임스탬프 초기화
    """
    global _TIMESTAMP

    _TIMESTAMP = datetime.now().strftime(f"%Y%m%d-%H%M%S")

def getTimeStamp() -> str:
    """ 시작 타임스탬프 반환

    Returns:
        str: 타임스탬프
    """
    return _TIMESTAMP

def __init_logger():
    """ 로거 초기화
    """
    
    global HLOG
    # 创建 logger 对象
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # 创建控制台处理器并设置级别为 WARNING
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(logging.Formatter('[%(asctime)s.%(msecs)03d][%(levelname).1s][%(filename)s(%(funcName)s):%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'))

    logfile = f"{getTimeStamp()}_{os.path.basename(sys.argv[0])}.log"
    logpath = f"{Path(__file__).parents[1]}\\Log"

    if os.path.isdir(logpath) != True:
        os.makedirs(logpath)

    # 创建文件处理器并设置级别为 DEBUG
    file_handler = logging.FileHandler(logpath + '\\' + logfile, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter('[%(asctime)s.%(msecs)03d][%(levelname).1s][%(filename)s(%(funcName)s):%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'))

    # 将处理器添加到 logger 对象中
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    HLOG = logger

    # # 输出日志
    # logger.debug('This is a debug message')
    # logger.info('This is an info message')
    # logger.warning('This is a warning message')
    # logger.error('This is an error message')
    # logger.critical('This is a critical message')
