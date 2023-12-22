def is_name_valid(name: str) -> bool:
	return len(name) > 0 and len(name) <= 100

def normalize_name(name: str) -> str:
	return name.lower().strip()

def normalize_message(message: str) -> str:
	result_message = message
	if len(message) > 64:
		result_message = message[:61] + "..."
	return result_message