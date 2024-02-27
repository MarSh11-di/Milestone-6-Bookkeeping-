abetca = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
lenght_abetca = len(abetca)
message = input("введiть повiдомлення: ").lower().strip()
key_user = int(input("введiть змiщенн: "))
length_mes = len(message)
decrypt_text = ""
for letter in message:
  if letter == " ":
    decrypt_text += " "
  else:
    ind= (abetca.index(letter)-key_user)%lenght_abetca
    decrypt_text +=abetca[ind]
print("decrypt_text: ", decrypt_text)