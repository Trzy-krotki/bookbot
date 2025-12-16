def get_num_words(text):
	return len(text.split()) 

def num_dictionary(text):
	text = text.lower()
	text = text.replace(" ","")
	num_dictionary = {
	"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"x":0,"y":0,"z":0,"æ":0,"â": 0,"ê":0,"ë":0,"ô":0}
	for leter in text:
		if leter in num_dictionary:
			num_dictionary[leter] += 1
	return num_dictionary

def sort_dictionary(dic):
	list = []
	def sort_num(item):
		return item["num"]

	for leter in dic:
		new_dic = {}
		new_dic["name"] = leter
		new_dic["num"] = dic[leter]
		list.append(new_dic)
	list.sort(key=sort_num,reverse=True)
	return list
