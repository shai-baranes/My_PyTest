


def add(a: int, b: int) -> int:
	return a+b


def divide(a: int, b: int) -> float:
	if b==0:
		raise ValueError("Cannot Divide by 0") # ValueError is probably our return value overwrite...
		# raise ZeroDivisionError("Cannot Divide by 0")
	return a/b


