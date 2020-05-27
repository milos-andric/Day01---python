import time
import string

def pseudo_rand(modulo):
	t_tel = time.time()
	t_tel = int(t_tel * 100000 % modulo)
	return(t_tel)


def generator(text, sep=" ", option=None):
	text = text.split(sep)
	if option is None:
		for i in text:
			yield i
	elif option == "shuffle":
		le = len(text)
		list2 = []
		for x in range(len(text)):
			mot = text[pseudo_rand(le)]
			list2.append(mot)
			text.remove(mot)
			le -= 1
		text = list2
		for i in text:
			yield i
	elif option == "ordered":
		text.sort()
		for x in text:
			yield x

text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option="ordered"):
	print(word)