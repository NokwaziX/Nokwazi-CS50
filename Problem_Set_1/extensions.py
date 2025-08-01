'''
File Extentions and Media Types:

.gif  - image/gif
.jpg. - image/jpeg
.jpeg - image/jpeg
.png  - image/png
.pdf  - application/pdf
.txt. - text/plain
.zip  - application/zip
.other - application/octet-stream

'''

file_name = input('Insert file name: ')
file_name2 = file_name.lower().strip() #Vary the casing and remove leading whitespace

#Use endswith method
if file_name2.endswith('.gif'):
  print('image/gif')
elif file_name2.endswith('.jpg') or file_name2.endswith('.jpeg'):
  print('image/jpeg')
elif file_name2.endswith('.png'):
  print('image/png')
elif file_name2.endswith('.pdf'):
  print('application/pdf')
elif file_name2.endswith('.txt'):
  print('text/plain')
elif file_name2.endswith('.zip'):
  print('application/zip')
else:
  print('application/octet-stream')
