import logging
import config_func
from datetime import datetime

def get_logger():
    config = config_func.load_config()

    logger = logging.getLogger("blog_manager")
    logger.setLevel(level=logging.DEBUG)

    user_id = config.get("ACCOUNTS","USER_ID", fallback="UNKNOWN")
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s %(name)s " + user_id + "[%(thread)d] [%(funcName)s : line %(lineno)d] - %(message)s")
    
    # 콘솔 출력
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)

    # 파일에 출력
    log_file_dir = config.get("FILE_PATH", "LOGFILE_PATH", fallback="UNKNOWN")
    log_file_path = f"{log_file_dir}" + datetime.today().strftime("%Y%m%d_%H%M%S") + ".log"

    file_handler = logging.FileHandler(log_file_path,'w', encoding="utf-8")
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # 중복 핸들러 추가 방지
    if logger.handlers:
        logger.handlers.clear()

    # 핸들러 추가
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    return logger

log  = get_logger()
log.info("hitstt")

