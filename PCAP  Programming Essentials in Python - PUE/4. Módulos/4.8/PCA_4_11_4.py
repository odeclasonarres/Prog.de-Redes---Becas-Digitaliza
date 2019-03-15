iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')
if not iban.isalnum():
    print("Invalid characters inside IBAN - sorry!")
elif len(iban) < 15:
    print("IBAN too short")
elif len(iban) > 31:
    print("IBAN too long")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    ibann = int(iban2)
    if ibann % 97 == 1:
        print("Seems legit!")
    else:
        print("I don't think it's a valid IBAN, sorry")
    
