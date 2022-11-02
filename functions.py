def ValidInput(input_str):
	length = len(input_str)
	if (length == 0):
		return False
	else:
		char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

		for item in input_str:
			for stuff in char:
				if (item  == stuff or item == stuff.lower()):
					return True

	return False
