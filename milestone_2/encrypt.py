abetca = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
lenght_abetca = len(abetca)
message = input("введiть повiдомлення: ").lower().strip()
key_user = int(input("введiть змiщенн: "))
length_mes = len(message)
encrypt_text =""
for letter in message:
  if letter == " ":
    encrypt_text += " "
  else:
    ind= (abetca.index(letter)+key_user)%lenght_abetca
    encrypt_text +=abetca[ind]
print("encrypt_text: ", encrypt_text)