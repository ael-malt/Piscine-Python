def NULL_not_found(object: any) -> int:
	object_type = type(object)
	if object is None:
		print(f"Nothing : None {object_type}")
	if object_type is float:
		print(f"Cheese : nan {object_type}")
	elif object_type is int and object == 0:
		print(f"Zero : 0 {object_type}")
	elif object_type is str and object == '':
		print(f"Empty : {object_type}")
	elif not object and object_type is bool:
		print(f"Fake : False {object_type}")
	else:
		print("Type not found")
		return 1
	# print(object)
	# always return 0
	return 0
