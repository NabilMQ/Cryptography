from tkinter import *
from tkinter import filedialog

window = Tk()

# Vigenere Cipher

def encryptVigenereCipher():

  if ''.join(vigenereCipherTextFieldKeyword.get().split()).upper() == '':
    vigenereCipherOutput.configure(text="ERROR, PLEASE FILL THE KEYWORD")
    return

  strVal = ''.join(vigenereCipherTextField.get().split()).upper()
  keyword = ''.join(vigenereCipherTextFieldKeyword.get().split()).upper()
  keywordLen = len(keyword)
  index = 0

  if keywordLen < 12:
    vigenereCipherOutput.configure(text="ERROR, MINIMUM IS 12 CHARACTERS")
    return

  while len(keyword) < len(strVal):
    if index >= keywordLen:
      index = 0

    keyword += keyword[index]
    index += 1

  index = 0
  ans = ""
  for char in strVal:
    if ord(char) < 65 or (ord(char) > 90 and ord(char) < 97) or ord(char) > 122: 
      vigenereCipherOutput.configure(text="ERROR, ALPHABET ONLY")
      return
    
    asciiNum = ord(char)
    asciiNum += (ord(keyword[index]))
    asciiNum = asciiNum % 26
    asciiNum += 65
    ans += chr(asciiNum + 0)
    index += 1

  vigenereCipherOutput.configure(text="Output: " + ans)

def decryptVigenereCipher():
  if ''.join(vigenereCipherTextFieldKeyword.get().split()).upper() == '':
    vigenereCipherOutput.configure(text="ERROR, PLEASE FILL THE KEYWORD")
    return

  strVal = ''.join(vigenereCipherTextField.get().split()).upper()
  keyword = ''.join(vigenereCipherTextFieldKeyword.get().split()).upper()
  keywordLen = len(keyword)
  index = 0

  if keywordLen < 12:
    vigenereCipherOutput.configure(text="ERROR, MINIMUM IS 12 CHARACTERS")
    return

  while len(keyword) < len(strVal):
    if index >= keywordLen:
      index = 0

    keyword += keyword[index]
    index += 1

  index = 0
  ans = ""
  for char in strVal:
    if ord(char) < 65 or (ord(char) > 90 and ord(char) < 97) or ord(char) > 122: 
      vigenereCipherOutput.configure(text="ERROR, ALPHABET ONLY")
      return
    
    asciiNum = ord(char)
    asciiNum -= (ord(keyword[index]))
    asciiNum = asciiNum % 26
    asciiNum += 65
    ans += chr(asciiNum + 0)
    index += 1

  vigenereCipherOutput.configure(text="Output: " + ans)

def openfileVigenereCipherEncrypt():
  if ''.join(vigenereCipherTextFieldKeyword.get().split()).upper() == '':
    vigenereCipherOutput.configure(text="ERROR, PLEASE FILL THE KEYWORD")
    return

  openedFile = filedialog.askopenfilename(
    initialdir="/",
    title="Select txt file",
    filetypes=(("Text files", "*.txt"), )
  )

  if openedFile:
    with open(openedFile, "r") as file:
      content = ''.join(file.read().split()).upper()
      keyword = ''.join(vigenereCipherTextFieldKeyword.get().split()).upper()
      keywordLen = len(keyword)
      index = 0

      if keywordLen < 12:
        vigenereCipherOutput.configure(text="ERROR, MINIMUM IS 12 CHARACTERS")
        return

      while len(keyword) < len(content):
        if index >= keywordLen:
          index = 0

        keyword += keyword[index]
        index += 1

      index = 0
      ans = ""
      for char in content:
        if ord(char) < 65 or (ord(char) > 90 and ord(char) < 97) or ord(char) > 122: 
          vigenereCipherOutput.configure(text="ERROR, ALPHABET ONLY")
          return
    
        asciiNum = ord(char)
        asciiNum += (ord(keyword[index]))
        asciiNum = asciiNum % 26
        asciiNum += 65
        ans += chr(asciiNum + 0)
        index += 1

      vigenereCipherOutput.configure(text="Output: " + ans)
  
def openfileVigenereCipherDecrypt():
  if ''.join(vigenereCipherTextFieldKeyword.get().split()).upper() == '':
    vigenereCipherOutput.configure(text="ERROR, PLEASE FILL THE KEYWORD")
    return

  openedFile = filedialog.askopenfilename(
    initialdir="/",
    title="Select txt file",
    filetypes=(("Text files", "*.txt"), )
  )

  if openedFile:
    with open(openedFile, "r") as file:
      content = ''.join(file.read().split()).upper()
      keyword = ''.join(vigenereCipherTextFieldKeyword.get().split()).upper()
      keywordLen = len(keyword)
      index = 0

      if keywordLen < 12:
        vigenereCipherOutput.configure(text="ERROR, MINIMUM IS 12 CHARACTERS")
        return

      while len(keyword) < len(content):
        if index >= keywordLen:
          index = 0

        keyword += keyword[index]
        index += 1

      index = 0
      ans = ""
      for char in content:
        if ord(char) < 65 or (ord(char) > 90 and ord(char) < 97) or ord(char) > 122: 
          vigenereCipherOutput.configure(text="ERROR, ALPHABET ONLY")
          return
    
        asciiNum = ord(char)
        asciiNum -= (ord(keyword[index]))
        asciiNum = asciiNum % 26
        asciiNum += 65
        ans += chr(asciiNum + 0)
        index += 1

      vigenereCipherOutput.configure(text="Output: " + ans)


window.title("Kriptografi")
window.geometry("720x480")

vigenereCipher = Label(
  window,
  text="Vigenere Cipher",
)
vigenereCipher.grid(
  column=0,
  row=0,
)

txt = Label(
  window,
  text="Text Input",
)
txt.grid(
  column=0,
  row=1,
)

vigenereCipherTextField = Entry(
  window,
  width=10,
)
vigenereCipherTextField.grid(
  column=1,
  row=1,
)

vigenereCipherEncrypt = Button(
  window,
  text="Encrypt",
  fg="black",
  command=encryptVigenereCipher
)
vigenereCipherEncrypt.grid(
  column=2,
  row=1,
)

vigenereCipherDecrypt = Button(
  window,
  text="Decrypt",
  fg="black",
  command=decryptVigenereCipher,
)
vigenereCipherDecrypt.grid(
  column=3,
  row=1,
)

vigenereCipherOutput = Label(
  window,
  text="Output: ",
)
vigenereCipherOutput.grid(
  column=4,
  row=1,
)

vigenereCipherKeywordText = Label(
  window,
  text="Keyword: ",
)
vigenereCipherKeywordText.grid(
  column=0,
  row=2,
)

vigenereCipherTextFieldKeyword = Entry(
  window,
  width=10,
)
vigenereCipherTextFieldKeyword.grid(
  column=1,
  row=2,
)

vigenereCipherOpenFileEncrypt = Button(
  window,
  text="Open File Encrypt",
  fg="black",
  command=openfileVigenereCipherEncrypt,
)
vigenereCipherOpenFileEncrypt.grid(
  column=0,
  row=3,
)

vigenereCipherOpenFileDecrypt = Button(
  window,
  text="Open File Decrypt",
  fg="black",
  command=openfileVigenereCipherDecrypt,
)
vigenereCipherOpenFileDecrypt.grid(
  column=1,
  row=3,
)

# Playfair Cipher

def find(matrix, toFind):
  for i in range(5):
    for j in range(5):
      if (matrix[i][j] == toFind):
        return [i, j]

def encryptPlayfairCipher():

  if ''.join(playfairCipherTextFieldKeyword.get().split()).upper() == '':
    playfairCipherOutput.configure(text="ERROR, PLEASE FILL THE KEYWORD")
    return

  strVal = ''.join(playfairCipherTextField.get().split()).upper()
  strValCopy = strVal
  strVal = ""
  for char in strValCopy:
    if char == "J":
      strVal += "I"
    else:
      strVal += char

  if len(strVal) % 2 == 1:
    strVal += "Z"
  
  plainText = []
  tempArr = []
  i = 0
  while i < len(strVal):
    if len(tempArr) == 1 and tempArr[0] == strVal[i]:
      if ord(strVal[i]) + 1 == 91:
        tempArr.append("A")
      else:
        if chr(ord(strVal[i]) + 1) == "J":
          tempArr.append("K")
        else:
          tempArr.append(chr(ord(strVal[len(strVal) - 1]) + 1))

      i -= 1

    else:
      tempArr.append(strVal[i])

    if len(tempArr) == 2:
      plainText.append(tempArr)
      tempArr = []
    
    i += 1

  if len(tempArr) == 1:
    if ord(strVal[len(strVal) - 1]) + 1 == 91:
      tempArr.append("A")
    else:
      if chr(ord(strVal[len(strVal) - 1]) + 1) == "J":
        tempArr.append("K")
      else:
        tempArr.append(chr(ord(strVal[len(strVal) - 1]) + 1))
    
    plainText.append(tempArr)

  keyword = ''.join(playfairCipherTextFieldKeyword.get().split()).upper()
  keywordCopy = keyword
  keyword = ""
  for char in keywordCopy:
    if char == "J":
      keyword += "I"
    else:
      keyword += char

  keywordLen = len(keyword)
  mapOfChar = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0,
    "F": 0,
    "G": 0,
    "H": 0,
    "I": 0,
    "K": 0,
    "L": 0,
    "M": 0,
    "N": 0,
    "O": 0,
    "P": 0,
    "Q": 0,
    "R": 0,
    "S": 0,
    "T": 0,
    "U": 0,
    "V": 0,
    "W": 0,
    "X": 0,
    "Y": 0,
    "Z": 0,
  }
  for char in keyword:
    mapOfChar[char] += 1
    if (mapOfChar[char] > 1):
      playfairCipherOutput.configure(text="ERROR, USE UNIQUE CHARACTERS")
      return

  if keywordLen < 12:
    playfairCipherOutput.configure(text="ERROR, MINIMUM IS 12 CHARACTERS")
    return
  
  matrixKey = []
  tempMatrix = []
  for char in keyword:
    tempMatrix.append(char)
    if len(tempMatrix) == 5:
      matrixKey.append(tempMatrix)
      tempMatrix = []
  
  for key, value in mapOfChar.items():
    if value == 0:
      tempMatrix.append(key)
    
    if len(tempMatrix) == 5:
      matrixKey.append(tempMatrix)
      tempMatrix = []
  
  for char in strVal:
    if ord(char) < 65 or (ord(char) > 90 and ord(char) < 97) or ord(char) > 122: 
      playfairCipherOutput.configure(text="ERROR, ALPHABET ONLY")
      return
    
  print(matrixKey)

  ans = ""
  for char in plainText:
    firstCoor = find(matrixKey, char[0])
    secondCoor = find(matrixKey, char[1])
    if firstCoor[0] == secondCoor[0]:
      firstCoor[1] += 1
      if firstCoor[1] > 4:
        firstCoor[1] = 0

      secondCoor[1] += 1
      if secondCoor[1] > 4:
        secondCoor[1] = 0

    elif firstCoor[1] == secondCoor[1]:
      firstCoor[0] += 1
      if firstCoor[0] > 4:
        firstCoor[0] = 0

      secondCoor[0] += 1
      if secondCoor[0] > 4:
        secondCoor[0] = 0
    
    else:
      temp = firstCoor[1]
      firstCoor[1] = secondCoor[1]
      secondCoor[1] = temp

      
    ans += matrixKey[firstCoor[0]][firstCoor[1]]
    ans += matrixKey[secondCoor[0]][secondCoor[1]]
      

  playfairCipherOutput.configure(text="Output: " + ans)

def decryptPlayfairCipher():
  if ''.join(playfairCipherTextFieldKeyword.get().split()).upper() == '':
    playfairCipherOutput.configure(text="ERROR, PLEASE FILL THE KEYWORD")
    return

  strVal = ''.join(playfairCipherTextField.get().split()).upper()
  strValCopy = strVal
  strVal = ""
  for char in strValCopy:
    if char == "J":
      strVal += "I"
    else:
      strVal += char

  if len(strVal) % 2 == 1:
    strVal += "Z"
  
  plainText = []
  tempArr = []
  i = 0
  while i < len(strVal):
    if len(tempArr) == 1 and tempArr[0] == strVal[i]:
      if ord(strVal[i]) + 1 == 91:
        tempArr.append("A")
      else:
        if chr(ord(strVal[i]) + 1) == "J":
          tempArr.append("K")
        else:
          tempArr.append(chr(ord(strVal[len(strVal) - 1]) + 1))

      i -= 1

    else:
      tempArr.append(strVal[i])

    if len(tempArr) == 2:
      plainText.append(tempArr)
      tempArr = []
    
    i += 1

  if len(tempArr) == 1:
    if ord(strVal[len(strVal) - 1]) + 1 == 91:
      tempArr.append("A")
    else:
      if chr(ord(strVal[len(strVal) - 1]) + 1) == "J":
        tempArr.append("K")
      else:
        tempArr.append(chr(ord(strVal[len(strVal) - 1]) + 1))
    
    plainText.append(tempArr)

  keyword = ''.join(playfairCipherTextFieldKeyword.get().split()).upper()
  keywordCopy = keyword
  keyword = ""
  for char in keywordCopy:
    if char == "J":
      keyword += "I"
    else:
      keyword += char

  keywordLen = len(keyword)
  mapOfChar = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0,
    "F": 0,
    "G": 0,
    "H": 0,
    "I": 0,
    "K": 0,
    "L": 0,
    "M": 0,
    "N": 0,
    "O": 0,
    "P": 0,
    "Q": 0,
    "R": 0,
    "S": 0,
    "T": 0,
    "U": 0,
    "V": 0,
    "W": 0,
    "X": 0,
    "Y": 0,
    "Z": 0,
  }
  for char in keyword:
    mapOfChar[char] += 1
    if (mapOfChar[char] > 1):
      playfairCipherOutput.configure(text="ERROR, USE UNIQUE CHARACTERS")
      return

  if keywordLen < 12:
    playfairCipherOutput.configure(text="ERROR, MINIMUM IS 12 CHARACTERS")
    return
  
  matrixKey = []
  tempMatrix = []
  for char in keyword:
    tempMatrix.append(char)
    if len(tempMatrix) == 5:
      matrixKey.append(tempMatrix)
      tempMatrix = []
  
  for key, value in mapOfChar.items():
    if value == 0:
      tempMatrix.append(key)
    
    if len(tempMatrix) == 5:
      matrixKey.append(tempMatrix)
      tempMatrix = []
  
  for char in strVal:
    if ord(char) < 65 or (ord(char) > 90 and ord(char) < 97) or ord(char) > 122: 
      playfairCipherOutput.configure(text="ERROR, ALPHABET ONLY")
      return
    
  print(matrixKey)

  ans = ""
  for char in plainText:
    firstCoor = find(matrixKey, char[0])
    secondCoor = find(matrixKey, char[1])
    if firstCoor[0] == secondCoor[0]:
      firstCoor[1] -= 1
      if firstCoor[1] < 0:
        firstCoor[1] = 4

      secondCoor[1] -= 1
      if secondCoor[1] < 0:
        secondCoor[1] = 4

    elif firstCoor[1] == secondCoor[1]:
      firstCoor[0] -= 1
      if firstCoor[0] < 0:
        firstCoor[0] = 4

      secondCoor[0] -= 1
      if secondCoor[0] < 0:
        secondCoor[0] = 4
    
    else:
      temp = firstCoor[1]
      firstCoor[1] = secondCoor[1]
      secondCoor[1] = temp

      
    ans += matrixKey[firstCoor[0]][firstCoor[1]]
    ans += matrixKey[secondCoor[0]][secondCoor[1]]
      

  playfairCipherOutput.configure(text="Output: " + ans)

def openfilePlayfairCipherEncrypt():
  if ''.join(playfairCipherTextFieldKeyword.get().split()).upper() == '':
    playfairCipherOutput.configure(text="ERROR, PLEASE FILL THE KEYWORD")
    return

  openedFile = filedialog.askopenfilename(
    initialdir="/",
    title="Select txt file",
    filetypes=(("Text files", "*.txt"), )
  )

  if openedFile:
    with open(openedFile, "r") as file:
      strVal = ''.join(file.read().split()).upper()
      if ''.join(playfairCipherTextFieldKeyword.get().split()).upper() == '':
        playfairCipherOutput.configure(text="ERROR, PLEASE FILL THE KEYWORD")
        return

      strValCopy = strVal
      strVal = ""
      for char in strValCopy:
        if char == "J":
          strVal += "I"
        else:
          strVal += char

      if len(strVal) % 2 == 1:
        strVal += "Z"
      
      plainText = []
      tempArr = []
      i = 0
      while i < len(strVal):
        if len(tempArr) == 1 and tempArr[0] == strVal[i]:
          if ord(strVal[i]) + 1 == 91:
            tempArr.append("A")
          else:
            if chr(ord(strVal[i]) + 1) == "J":
              tempArr.append("K")
            else:
              tempArr.append(chr(ord(strVal[len(strVal) - 1]) + 1))

          i -= 1

        else:
          tempArr.append(strVal[i])

        if len(tempArr) == 2:
          plainText.append(tempArr)
          tempArr = []
        
        i += 1

      if len(tempArr) == 1:
        if ord(strVal[len(strVal) - 1]) + 1 == 91:
          tempArr.append("A")
        else:
          if chr(ord(strVal[len(strVal) - 1]) + 1) == "J":
            tempArr.append("K")
          else:
            tempArr.append(chr(ord(strVal[len(strVal) - 1]) + 1))
        
        plainText.append(tempArr)

      keyword = ''.join(playfairCipherTextFieldKeyword.get().split()).upper()
      keywordCopy = keyword
      keyword = ""
      for char in keywordCopy:
        if char == "J":
          keyword += "I"
        else:
          keyword += char

      keywordLen = len(keyword)
      mapOfChar = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        "F": 0,
        "G": 0,
        "H": 0,
        "I": 0,
        "K": 0,
        "L": 0,
        "M": 0,
        "N": 0,
        "O": 0,
        "P": 0,
        "Q": 0,
        "R": 0,
        "S": 0,
        "T": 0,
        "U": 0,
        "V": 0,
        "W": 0,
        "X": 0,
        "Y": 0,
        "Z": 0,
      }
      for char in keyword:
        mapOfChar[char] += 1
        if (mapOfChar[char] > 1):
          playfairCipherOutput.configure(text="ERROR, USE UNIQUE CHARACTERS")
          return

      if keywordLen < 12:
        playfairCipherOutput.configure(text="ERROR, MINIMUM IS 12 CHARACTERS")
        return
      
      matrixKey = []
      tempMatrix = []
      for char in keyword:
        tempMatrix.append(char)
        if len(tempMatrix) == 5:
          matrixKey.append(tempMatrix)
          tempMatrix = []
      
      for key, value in mapOfChar.items():
        if value == 0:
          tempMatrix.append(key)
        
        if len(tempMatrix) == 5:
          matrixKey.append(tempMatrix)
          tempMatrix = []
      
      for char in strVal:
        if ord(char) < 65 or (ord(char) > 90 and ord(char) < 97) or ord(char) > 122: 
          playfairCipherOutput.configure(text="ERROR, ALPHABET ONLY")
          return
        
      print(matrixKey)

      ans = ""
      for char in plainText:
        firstCoor = find(matrixKey, char[0])
        secondCoor = find(matrixKey, char[1])
        if firstCoor[0] == secondCoor[0]:
          firstCoor[1] += 1
          if firstCoor[1] > 4:
            firstCoor[1] = 0

          secondCoor[1] += 1
          if secondCoor[1] > 4:
            secondCoor[1] = 0

        elif firstCoor[1] == secondCoor[1]:
          firstCoor[0] += 1
          if firstCoor[0] > 4:
            firstCoor[0] = 0

          secondCoor[0] += 1
          if secondCoor[0] > 4:
            secondCoor[0] = 0
        
        else:
          temp = firstCoor[1]
          firstCoor[1] = secondCoor[1]
          secondCoor[1] = temp

          
        ans += matrixKey[firstCoor[0]][firstCoor[1]]
        ans += matrixKey[secondCoor[0]][secondCoor[1]]
          

      playfairCipherOutput.configure(text="Output: " + ans)
  
def openfilePlayfairCipherDecrypt():
  if ''.join(playfairCipherTextFieldKeyword.get().split()).upper() == '':
    playfairCipherOutput.configure(text="ERROR, PLEASE FILL THE KEYWORD")
    return

  openedFile = filedialog.askopenfilename(
    initialdir="/",
    title="Select txt file",
    filetypes=(("Text files", "*.txt"), )
  )

  if openedFile:
    with open(openedFile, "r") as file:
      strVal = ''.join(file.read().split()).upper()
      if ''.join(playfairCipherTextFieldKeyword.get().split()).upper() == '':
        playfairCipherOutput.configure(text="ERROR, PLEASE FILL THE KEYWORD")
        return

      strValCopy = strVal
      strVal = ""
      for char in strValCopy:
        if char == "J":
          strVal += "I"
        else:
          strVal += char

      if len(strVal) % 2 == 1:
        strVal += "Z"
      
      plainText = []
      tempArr = []
      i = 0
      while i < len(strVal):
        if len(tempArr) == 1 and tempArr[0] == strVal[i]:
          if ord(strVal[i]) + 1 == 91:
            tempArr.append("A")
          else:
            if chr(ord(strVal[i]) + 1) == "J":
              tempArr.append("K")
            else:
              tempArr.append(chr(ord(strVal[len(strVal) - 1]) + 1))

          i -= 1

        else:
          tempArr.append(strVal[i])

        if len(tempArr) == 2:
          plainText.append(tempArr)
          tempArr = []
        
        i += 1

      if len(tempArr) == 1:
        if ord(strVal[len(strVal) - 1]) + 1 == 91:
          tempArr.append("A")
        else:
          if chr(ord(strVal[len(strVal) - 1]) + 1) == "J":
            tempArr.append("K")
          else:
            tempArr.append(chr(ord(strVal[len(strVal) - 1]) + 1))
        
        plainText.append(tempArr)

      keyword = ''.join(playfairCipherTextFieldKeyword.get().split()).upper()
      keywordCopy = keyword
      keyword = ""
      for char in keywordCopy:
        if char == "J":
          keyword += "I"
        else:
          keyword += char

      keywordLen = len(keyword)
      mapOfChar = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        "F": 0,
        "G": 0,
        "H": 0,
        "I": 0,
        "K": 0,
        "L": 0,
        "M": 0,
        "N": 0,
        "O": 0,
        "P": 0,
        "Q": 0,
        "R": 0,
        "S": 0,
        "T": 0,
        "U": 0,
        "V": 0,
        "W": 0,
        "X": 0,
        "Y": 0,
        "Z": 0,
      }
      for char in keyword:
        mapOfChar[char] += 1
        if (mapOfChar[char] > 1):
          playfairCipherOutput.configure(text="ERROR, USE UNIQUE CHARACTERS")
          return

      if keywordLen < 12:
        playfairCipherOutput.configure(text="ERROR, MINIMUM IS 12 CHARACTERS")
        return
      
      matrixKey = []
      tempMatrix = []
      for char in keyword:
        tempMatrix.append(char)
        if len(tempMatrix) == 5:
          matrixKey.append(tempMatrix)
          tempMatrix = []
      
      for key, value in mapOfChar.items():
        if value == 0:
          tempMatrix.append(key)
        
        if len(tempMatrix) == 5:
          matrixKey.append(tempMatrix)
          tempMatrix = []
      
      for char in strVal:
        if ord(char) < 65 or (ord(char) > 90 and ord(char) < 97) or ord(char) > 122: 
          playfairCipherOutput.configure(text="ERROR, ALPHABET ONLY")
          return
        
      print(matrixKey)

      ans = ""
      for char in plainText:
        firstCoor = find(matrixKey, char[0])
        secondCoor = find(matrixKey, char[1])
        if firstCoor[0] == secondCoor[0]:
          firstCoor[1] -= 1
          if firstCoor[1] < 0:
            firstCoor[1] = 4

          secondCoor[1] -= 1
          if secondCoor[1] < 0:
            secondCoor[1] = 4

        elif firstCoor[1] == secondCoor[1]:
          firstCoor[0] -= 1
          if firstCoor[0] < 0:
            firstCoor[0] = 4

          secondCoor[0] -= 1
          if secondCoor[0] < 0:
            secondCoor[0] = 4
        
        else:
          temp = firstCoor[1]
          firstCoor[1] = secondCoor[1]
          secondCoor[1] = temp

          
        ans += matrixKey[firstCoor[0]][firstCoor[1]]
        ans += matrixKey[secondCoor[0]][secondCoor[1]]
          

      playfairCipherOutput.configure(text="Output: " + ans)

window.title("Kriptografi")
window.geometry("720x480")

playfairCipher = Label(
  window,
  text="Playfair Cipher",
)
playfairCipher.grid(
  column=0,
  row=4,
)

txt = Label(
  window,
  text="Text Input",
)
txt.grid(
  column=0,
  row=5,
)

playfairCipherTextField = Entry(
  window,
  width=10,
)
playfairCipherTextField.grid(
  column=1,
  row=5,
)

playfairCipherEncrypt = Button(
  window,
  text="Encrypt",
  fg="black",
  command=encryptPlayfairCipher
)
playfairCipherEncrypt.grid(
  column=2,
  row=5,
)

playfairCipherDecrypt = Button(
  window,
  text="Decrypt",
  fg="black",
  command=decryptPlayfairCipher,
)
playfairCipherDecrypt.grid(
  column=3,
  row=5,
)

playfairCipherOutput = Label(
  window,
  text="Output: ",
)
playfairCipherOutput.grid(
  column=4,
  row=5,
)

playfairCipherKeywordText = Label(
  window,
  text="Keyword: ",
)
playfairCipherKeywordText.grid(
  column=0,
  row=6,
)

playfairCipherTextFieldKeyword = Entry(
  window,
  width=10,
)
playfairCipherTextFieldKeyword.grid(
  column=1,
  row=6,
)

playfairCipherOpenFileEncrypt = Button(
  window,
  text="Open File Encrypt",
  fg="black",
  command=openfilePlayfairCipherEncrypt,
)
playfairCipherOpenFileEncrypt.grid(
  column=0,
  row=7,
)

playfairCipherOpenFileDecrypt = Button(
  window,
  text="Open File Decrypt",
  fg="black",
  command=openfilePlayfairCipherDecrypt,
)
playfairCipherOpenFileDecrypt.grid(
  column=1,
  row=7,
)

# Hill Cipher

def encryptHillCipher():

  if ''.join(hillCipherTextFieldKeyword.get().split()).upper() == '':
    hillCipherOutput.configure(text="ERROR, PLEASE FILL THE KEYWORD")
    return

  strVal = ''.join(hillCipherTextField.get().split()).upper()
  keyword = ''.join(hillCipherTextFieldKeyword.get().split()).upper()
  keywordLen = len(keyword)

  if keywordLen != 4:
    hillCipherOutput.configure(text="ERROR, MUST HAVE 4 CHARACTERS")
    return
  
  if len(strVal) % 2 != 0:
    hillCipherOutput.configure(text="ERROR, INPUT LENGTH MUST BE DIVISIBLE BY 2")
    return

  keywordNum = [ord(keyword[0]) % 65, ord(keyword[1]) % 65, ord(keyword[2]) % 65, ord(keyword[3]) % 65]  
  
  plainText = []
  temp = []
  for char in strVal:
    temp.append(ord(char) % 65)

    if len(temp) == 2:
      plainText.append(temp)
      temp = []

  ans = ""
  for el in plainText:
    first =  keywordNum[0] * el[0] + keywordNum[1] * el[1]
    first = first % 26

    second = keywordNum[2] * el[0] + keywordNum[3] * el[1]
    second = second % 26

    first += 65
    second += 65

    ans += chr(first)
    ans += chr(second)

  hillCipherOutput.configure(text="Output: " + ans)

def decryptHillCipher():
  if ''.join(hillCipherTextFieldKeyword.get().split()).upper() == '':
    hillCipherOutput.configure(text="ERROR, PLEASE FILL THE KEYWORD")
    return

  strVal = ''.join(hillCipherTextField.get().split()).upper()
  keyword = ''.join(hillCipherTextFieldKeyword.get().split()).upper()
  keywordLen = len(keyword)
  index = 0

  if keywordLen != 4:
    hillCipherOutput.configure(text="ERROR, MUST HAVE 4 CHARACTERS")
    return
  
  if len(strVal) % 2 != 0:
    hillCipherOutput.configure(text="ERROR, INPUT LENGTH MUST BE DIVISIBLE BY 2")
    return

  keywordNum = [ord(keyword[0]) % 64, ord(keyword[1]) % 64, ord(keyword[2]) % 64, ord(keyword[3]) % 64]  
  print(keywordNum)
  det = keywordNum[0] * keywordNum[3] - keywordNum[1] * keywordNum[2]
  det = det % 26

  print(det)
  temp = 0
  while (det * temp) % 26 != 1:
    temp += 1

  keywordNum = [(keywordNum[3] * temp) % 26, (-keywordNum[1] * temp) % 26, (-keywordNum[2] * temp) % 26, (keywordNum[0] * temp) % 26]
  print(keywordNum)

  plainText = []
  temp = []
  for char in strVal:
    temp.append(ord(char) % 64)

    if len(temp) == 2:
      plainText.append(temp)
      temp = []

  ans = ""
  for el in plainText:
    first =  keywordNum[0] * el[0] + keywordNum[1] * el[1]
    first = first % 26

    second = keywordNum[2] * el[0] + keywordNum[3] * el[1]
    second = second % 26

    first += 65
    second += 65

    ans += chr(first)
    ans += chr(second)

  hillCipherOutput.configure(text="Output: " + ans)

def openfileHillCipherEncrypt():
  if ''.join(hillCipherTextFieldKeyword.get().split()).upper() == '':
    hillCipherOutput.configure(text="ERROR, PLEASE FILL THE KEYWORD")
    return

  openedFile = filedialog.askopenfilename(
    initialdir="/",
    title="Select txt file",
    filetypes=(("Text files", "*.txt"), )
  )

  if openedFile:
    with open(openedFile, "r") as file:
      content = ''.join(file.read().split()).upper()
      keyword = ''.join(hillCipherTextFieldKeyword.get().split()).upper()
      keywordLen = len(keyword)
      index = 0

      if keywordLen != 4:
        hillCipherOutput.configure(text="ERROR, MUST HAVE 4 CHARACTERS")
        return
      
      if len(content) % 2 != 0:
        hillCipherOutput.configure(text="ERROR, INPUT LENGTH MUST BE DIVISIBLE BY 2")
        return

      keywordNum = [ord(keyword[0]) % 65, ord(keyword[1]) % 65, ord(keyword[2]) % 65, ord(keyword[3]) % 65]  
  
      plainText = []
      temp = []
      for char in content:
        temp.append(ord(char) % 65)

        if len(temp) == 2:
          plainText.append(temp)
          temp = []

      ans = ""
      for el in plainText:
        first =  keywordNum[0] * el[0] + keywordNum[1] * el[1]
        first = first % 26

        second = keywordNum[2] * el[0] + keywordNum[3] * el[1]
        second = second % 26

        first += 65
        second += 65

        ans += chr(first)
        ans += chr(second)

      hillCipherOutput.configure(text="Output: " + ans)
  
def openfileHillCipherDecrypt():
  if ''.join(hillCipherTextFieldKeyword.get().split()).upper() == '':
    hillCipherOutput.configure(text="ERROR, PLEASE FILL THE KEYWORD")
    return

  openedFile = filedialog.askopenfilename(
    initialdir="/",
    title="Select txt file",
    filetypes=(("Text files", "*.txt"), )
  )

  if openedFile:
    with open(openedFile, "r") as file:
      content = ''.join(file.read().split()).upper()
      keyword = ''.join(hillCipherTextFieldKeyword.get().split()).upper()
      keywordLen = len(keyword)
      index = 0

      if keywordLen != 4:
        hillCipherOutput.configure(text="ERROR, MUST HAVE 4 CHARACTERS")
        return
      
      if len(content) % 2 != 0:
        hillCipherOutput.configure(text="ERROR, INPUT LENGTH MUST BE DIVISIBLE BY 2")
        return

      while len(keyword) < len(content):
        if index >= keywordLen:
          index = 0

        keyword += keyword[index]
        index += 1

      index = 0
      ans = ""
      for char in content:
        if ord(char) < 65 or (ord(char) > 90 and ord(char) < 97) or ord(char) > 122: 
          hillCipherOutput.configure(text="ERROR, ALPHABET ONLY")
          return
    
        asciiNum = ord(char)
        asciiNum -= (ord(keyword[index]))
        asciiNum = asciiNum % 26
        asciiNum += 65
        ans += chr(asciiNum + 0)
        index += 1

      hillCipherOutput.configure(text="Output: " + ans)


window.title("Kriptografi")
window.geometry("720x480")

hillCipher = Label(
  window,
  text="Hill Cipher",
)
hillCipher.grid(
  column=0,
  row=8,
)

txt = Label(
  window,
  text="Text Input",
)
txt.grid(
  column=0,
  row=9,
)

hillCipherTextField = Entry(
  window,
  width=10,
)
hillCipherTextField.grid(
  column=1,
  row=9,
)

hillCipherEncrypt = Button(
  window,
  text="Encrypt",
  fg="black",
  command=encryptHillCipher
)
hillCipherEncrypt.grid(
  column=2,
  row=9,
)

hillCipherDecrypt = Button(
  window,
  text="Decrypt",
  fg="black",
  command=decryptHillCipher,
)
hillCipherDecrypt.grid(
  column=3,
  row=9,
)

hillCipherOutput = Label(
  window,
  text="Output: ",
)
hillCipherOutput.grid(
  column=4,
  row=9,
)

hillCipherKeywordText = Label(
  window,
  text="Keyword: ",
)
hillCipherKeywordText.grid(
  column=0,
  row=10,
)

hillCipherTextFieldKeyword = Entry(
  window,
  width=10,
)
hillCipherTextFieldKeyword.grid(
  column=1,
  row=10,
)

hillCipherOpenFileEncrypt = Button(
  window,
  text="Open File Encrypt",
  fg="black",
  command=openfileHillCipherEncrypt,
)
hillCipherOpenFileEncrypt.grid(
  column=0,
  row=11,
)

hillCipherOpenFileDecrypt = Button(
  window,
  text="Open File Decrypt",
  fg="black",
  command=openfileHillCipherDecrypt,
)
hillCipherOpenFileDecrypt.grid(
  column=1,
  row=11,
) 

window.mainloop()