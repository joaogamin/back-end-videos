import re


def convert_duration(iso_duration):
	match = re.match(r'PT(\d+H)?(\d+M)?(\d+S)?', iso_duration)
	if not match:
		return "Invalid duration format"

	hours = int(match.group(1)[:-1]) if match.group(1) else 0
	minutes = int(match.group(2)[:-1]) if match.group(2) else 0
	seconds = int(match.group(3)[:-1]) if match.group(3) else 0

	return f"{hours:02}:{minutes:02}:{seconds:02}"
