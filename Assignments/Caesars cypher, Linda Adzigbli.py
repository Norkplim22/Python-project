plain_text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    
text = input("Enter plaintext message: ").upper()
#s defines the shift count
S = int(input("Choose the shift code: "))

encrypted = str()

# transverse the plain text
for i in text:
    updated_position = (plain_text.find(i)-S) % 26
    encrypted += plain_text[updated_position]

print(encrypted)

