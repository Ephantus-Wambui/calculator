import time
time.sleep(1)
print("Hello welcome to simple calculator. Type your inputs and choose the operation you want to do.")
time.sleep(1)
try:
	def calc():
		try:
			input1 = int(input("Please input your first value here: "))
			time.sleep(1)
			input2 = int(input("Please input your second value here: "))
			time.sleep(1)
			print("""
				For addition input +,
				For subtraction input -,
				For multiplication input *,
				For division input /.
			""")
			time.sleep(1)
			input3 = input("Please input your operation: ")
			time.sleep(1)
			if (input3 == "+"):
				sum = input1 + input2
				time.sleep(2)
				print(f"Your answer is {sum}")
			elif (input3 == "-"):
				sub = input1 - input2
				time.sleep(2)
				print(f"Your answer is {sub}")
			elif (input3 == "*"):
				multi = input1 * input2
				time.sleep(2)
				print(f"Your answer is {multi}")
			elif (input3 == "/"):
				div = input1 / input2
				time.sleep(2)
				print(f"Your answer is {div}")
			else:
				print("Something went wrong")
		except:
			time.sleep(2)
			print("Your input must be a number, do you want to try again?")
			time.sleep(2)
			response = input("Type your response here(Y or n): ")
			if (response.lower() == "y" or response.lower() == "yes"):
				time.sleep(2)
				calc()
			else:
				time.sleep(3)
				print("Okay, you can come back anytime")
except:
	time.sleep(3)
	print("Something went wrong, close app and try again")
calc()
