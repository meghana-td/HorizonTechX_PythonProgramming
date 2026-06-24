import re
with open("c:/Users/admin/.vscode/programs/python/internship tasks/doc.txt","r") as file:
    text= file.read()
emails= re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",text)
with open("emails.txt","w") as file:
    for email in emails:
        file.write(email+"\n")
    print("\nEmails are saved as emails.txt")
if emails:
    print("Extracted emails: \n")
    for email in emails:
        print(email)
else:
    print("No email addresses are found.")
