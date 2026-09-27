from datetime import datetime


def now_time() -> datetime:
    return datetime.now()

def spend_time_str(start_time: datetime, end_time: datetime) -> str:
    total_seconds = int((end_time - start_time).total_seconds())

    if total_seconds < 0:
        return "0s"

    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    parts: list[str] = []
    if hours > 0:
        parts.append(f"{hours}h")
    if minutes > 0:
        parts.append(f"{minutes}m")
    if seconds > 0 or not parts:
        parts.append(f"{seconds}s")

    return " ".join(parts)
