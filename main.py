import sys

from stats import get_num_words,num_dictionary,sort_dictionary

def get_book_text(file_patch):
	with open(file_patch)as f:
		file_contents = f.read()
	return file_contents

def main():
	print(len(sys.argv))
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>") 
		sys.exit(1)
	else:
		file_patch = sys.argv[1]
	book_text = get_book_text(file_patch) 
	lista = sort_dictionary(num_dictionary(book_text))
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {file_patch}")
	print("----------- Word Count ----------")
	print(f"Found {get_num_words(book_text)} total words")
	print("--------- Character Count -------")
	for i in lista:
		print (f"{i["name"]}: {i["num"]}")
	print("============= END ===============")
main()
