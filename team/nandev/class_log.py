################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

import logging
import os
import sys


class ConnectionHandler(logging.Handler):
    def emit(self, record):
        # Mendeteksi error tertentu untuk reboot
        critical_errors = ["OSError", "socket"]
        if any(err in record.getMessage() for err in critical_errors):
            # Simpan log ke file sebelum reboot
            with open("critical_error.log", "a") as error_file:
                error_file.write(self.format(record) + "\n")
            os.execl(sys.executable, sys.executable, "-m", "Mix")  # Reboot


# Fungsi untuk membuat logger tambahan
def LOGG(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        formatter = logging.Formatter(
            "[%(levelname)s] - %(name)s - %(message)s", "%d-%b %H:%M"
        )
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        file_handler = logging.FileHandler(f"{name}.log")
        file_handler.setFormatter(formatter)

        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)

    return logger


# Logger utama
logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter("[%(levelname)s] - %(name)s - %(message)s", "%d-%b %H:%M")
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

connection_handler = ConnectionHandler()
connection_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(connection_handler)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("asyncio").setLevel(logging.INFO)

LOGS = logging.getLogger("𝐁𝘭𝘶𝘦𝘧𝘭𝘺𝘰𝘥-Userbot v2")
LOGGER = LOGG("𝐁𝘭𝘶𝘦𝘧𝘭𝘺𝘰𝘥-Userbot v2")
