import re


def parse_l0g_line(line):
    log_pattern = (
        r"^(?P<timestamp>\S+ \S+) (?P<level>\S+) (?P<service>\S+) (?P<message>.+)$"
    )
    match = re.match(log_pattern, line)
    if match:
        return (
            match.groupdict()
        )  # used to convert raw data into structured data (dictionary)
    else:
        return None
