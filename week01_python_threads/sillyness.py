import threading
print("****************************************\n* Search The Book of Mormon for a word *\n****************************************")
search_word = str(input("Count occurances of what word? - "))
use_threads = ('y' == str(input("Use threads? (y/n) - ")))
my_threads = [] # will use one thread per line in the file
global_count = 0
total_word_count = 0

def count_word(line_of_text, s_word, thread_no):
	word_array = list(line_of_text.split(" "))
	local_count = 0
	for word in word_array:
		global total_word_count
		total_word_count += 1
		if word == s_word:
			global global_count
			global_count += 1	
			local_count += 1
	print("      Thread # "+str(thread_no+1)+" found the word \'"+str(s_word)+"\' "+str(local_count)+" times.")

print("   Starting Search...")
with open("bom reformatted.txt") as f:
	for i, line in zip(range(100), f):
		if use_threads:
			my_threads.append(threading.Thread(target=count_word, args=(line,search_word,i,)))
			my_threads[-1].start()
		else:
			count_word(line, search_word, 0)


if use_threads:
	#for t in my_threads:
	#	t.start()
	print("   Used "+str(len(my_threads))+" threads.")	
	for t in my_threads:
		t.join()
	
print("   ...Search Done.")
print("   Total words in file: "+str(total_word_count)+".")
print("   The word \'"+str(search_word)+"\' occurs "+str(global_count)+" times in The Book of Mormon.")