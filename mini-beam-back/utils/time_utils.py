from datetime import datetime as dt

import pytz

local_tz = pytz.timezone("Asia/Singapore")


def get_now_time() -> dt:
    return dt.now(local_tz)
