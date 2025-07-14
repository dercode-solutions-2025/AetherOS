import json

print("""Welcome to AetherTerminal v0.6. Below is the command list:
			1. Mirror - Mirrors your text with a playful remark.
			2. Lense - Tells you how many characters are in your text.
			3. Calculator - Basic math tool.
			4. Text Editor - Create, open, list, and delete files. (UPDATED)
			""")

# Load file data
try:
	with open("data.json", "r") as f:
		file_data = json.load(f)
except FileNotFoundError:
	file_data = {"files": {}}

def save_file():
	with open("data.json", "w") as f:
		json.dump(file_data, f, indent=4)

def list():
	print("""
			1. Mirror - Mirrors your text with a playful remark.
			2. Lense - Tells you how many characters are in your text.
			3. Calculator - Basic math tool.
			4. Text Editor - Create, open, list, and delete files.""")

while True:
	command = input(">>> ").lower()

	if command in ["1", "mirror"]:
		mirror = input("Enter your text: ")
		print(f"{mirror}? Wow, you really have a lot to say!")
		list()

	elif command in ["2", "lense"]:
		lense = input("Enter your text: ")
		print(str(len(lense)) + " characters")
		list()

	elif command in ["3", "calc", "calculator"]:
		operator = input("What is the operator? (+ - * /): ")
		num1 = float(input("What is the first number?: "))
		num2 = float(input("What is the second number?: "))
		if operator == "+":
			result = num1 + num2
		elif operator == "-":
			result = num1 - num2
		elif operator == "*":
			result = num1 * num2
		elif operator == "/":
			result = num1 / num2
		print(round(result, 3))
		list()

	elif command in ["4", "editor", "text"]:
		print("TEXT EDITOR OPTIONS:\n1. New file\n2. Open file\n3. List files\n4. Delete file")
		option = input("Choose: ")

		if option == "1":
			name = input("File name: ") + ".txt"
			content = []
			print("Type your content. Type '/end' to finish.")
			while True:
				line = input()
				if line == "/end":
					break
				content.append(line)
			file_data["files"][name] = "\n".join(content)
			save_file()
			print(f"{name} saved.")
			list()

		elif option == "2":
			name = input("File name to open: ") + ".txt"
			if name in file_data["files"]:
				print("-----")
				print(file_data["files"][name])
				print("-----")
			else:
				print("File not found.")
			list()

		elif option == "3":
			if file_data["files"]:
				print("Saved files:")
				for fname in file_data["files"]:
					print(" -", fname)
			else:
				print("No files found.")
			list()

		elif option == "4":
			name = input("File name to delete: ") + ".txt"
			if name in file_data["files"]:
				del file_data["files"][name]
				save_file()
				print(f"{name} deleted.")
			else:
				print("File not found.")
			list()

	else:
		print("Unknown command. Type 1-4 or 'mirror', 'lense', 'calc', 'editor'.")
