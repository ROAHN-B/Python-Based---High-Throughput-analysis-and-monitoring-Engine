import re
from datetime import datetime

log_pattern = re.compile(
    r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),(?P<level>\w+),(?P<service_level>\w+),(?P<message>.+)$"
)


def parse_log_line(line):
    match = re.match(log_pattern, line)
    if not match:
        return None
    data = match.groupdict()
    data["timestamp"] = datetime.strptime(data["timestamp"], "%Y-%m-%d %H:%M:%S")
    data["raw"] = line.strip()
    return data
