import string

print("Word Length Filter from File")

file_path = "sample.txt"

try:
    length =int(input("Enter the word length to filter: "))
    with open(file_path, 'r') as file:
      content = file.read()

    words= content.split()
    filtered_words = []
    for word in words:

# Remove punctuation and normalize case
      clean_word = word.strip(string.punctuation).lower()

    if len(clean_word) == length:

       filtered_words.append(clean_word)
    print (f"\nWords of length {length}:")

    if filtered_words:
        print(", ".join(filtered_words))
    else:
        print("No matching words found.")

except FileNotFoundError:
    print("Error: sample.txt file not found.")

except ValueError:
     print("Error: Please enter a valid number.")