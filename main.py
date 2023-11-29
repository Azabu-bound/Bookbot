def count_words(text: str) -> int:
 words = text.split()
 return len(words)

def count_letters(text: str) -> dict:
  char_count = {}
  text = text.lower()
  for char in text:
    if char.isalpha():
        if char in char_count:
          char_count[char] += 1
        else:
          char_count[char] = 1
  return char_count

def create_report(text, file_path) -> str:
  char_counts = count_letters(text)
  sorted_char_list = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
  
  print (f"--- Begin report of {file_path} ---")
  print (f"{count_words(text)} words found in the document.")

  for char in sorted_char_list:
    print (f"The {char[0]} character was found {char[1]} times.")
  
  print ("--- End report ---")

with open("books/frankenstein.txt") as f: 
  file_contents = f.read()
  create_report(file_contents, "books/frankenstein.txt")