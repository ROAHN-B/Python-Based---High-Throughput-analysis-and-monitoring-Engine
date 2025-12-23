import re
from datetime import datetime

log_pattern = re.compile(
    r"^(?P<timestamp>\S+ \S+) (?P<level>\S+) (?P<service>\S+) (?P<message>.+)$"
)


def parse_log_line(line):
    match = re.match(log_pattern, line)
    if not match:
        return None
    data = match.groupdict()
    data["timestamp"] = datetime.strptime(data["timestamp"], "%Y-%M-%d %H:%M:%S")
    data["raw"] = line.strip()
    return data
