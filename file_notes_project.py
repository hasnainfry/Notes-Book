import os 

path = ("/storage/emulated/0/Download/CodingPython/student.txt")

while True :
	print ("\n==== Notes Manager ====")
	print ("1 Create New Notes")
	print ("2 Read Notes")
	print ("3 Add more Notes (write)")
	print ("4 Search A Word In Notes")
	print ("5 Delete Notes File")
	print ("6   Exit")
	
	
	try:
		choice = int(input("Enter Choice "))
		
		# 1️⃣ Creat New Notes :
		if choice == 1 :
			text = input("Write Your Notes")
			with open(path,"w") as notes :
				notes.write(text)
				print ("✅Your Notes Successfully Added")
				
		#2️⃣ Read Notes
		elif choice == 2 :
			if os.path.exists(path) :
				with open(path,"r") as f :
					notes = f.read()
					print ("\n ---- Your Notes ----")
					print (notes)
			else:
					print ("Notes Not Exist")
					
		# 3️⃣ Append Notes			
		elif choice == 3 :
			append_notes = input("Enter Text To add :\n")
			with open(path,"a") as f :
				f.write("\n" + append_notes)
				print ("✅ Notes Updated")
				
		# 4️⃣ Search word		
		elif choice == 4 :
				if os.path.exists(path) :
					word = input("Enter Word To search")
					with open(path,"r") as f :
						search = f.read()
						if word in search :
							print (f"✅ {word} Found In your notes")
						else:
							print (f"❌ {word} Not Found in your notes")
				else:
					print ("❌ Notes file not found")
			
			
			 # 5️⃣ Delete Notes
		elif choice == 5 :
			if os.path.exists(path) :
				os.remove(path)
				print ("🗑️Notes Successfully Deleted ")
			else :
				print ("❌ Notes File Not Found")
			
			
			# 6️⃣ Program Exit
		elif choice == 6 :
			print ("Now Program Exiting.... Have A Great Day !")
			break	
			
						
	except ValueError :
		print ("Select Choice In Digits ")
		
	