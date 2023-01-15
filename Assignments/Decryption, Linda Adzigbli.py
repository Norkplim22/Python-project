Cipher = "XYZABCDEFGHIJKLMNOPQRSTUVW"
text = input("Enter encrypted text message: ").upper()
#s defines the shift count
S = int(input("Choose the shift code: "))

plain_text = str()

# transverse the plain text
for i in text:
    updated_position = (Cipher.find(i)+S) % 26
    plain_text += Cipher[updated_position]

print(plain_text)