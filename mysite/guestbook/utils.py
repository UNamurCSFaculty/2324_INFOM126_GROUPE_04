def is_name_valid(name: str) -> bool:
	""" Checks if name is valid. Valid names are non-empty strings with length <= 100"""
	return len(name) > 0 and len(name) <= 100

def normalize_name(name: str) -> str:
	"""Converts name to lowercase and removes leading and trailing spaces"""
	return name.lower().strip()

def normalize_message(message: str) -> str:
	"""Truncates message to 64 characters if it is longer than 64 characters"""
	result_message = message
	if len(message) > 64:
		result_message = message[:61] + "..."
	return result_message
