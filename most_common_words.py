# About: Provides most common words from a directory with *.txt files or a single file
# Author: mike.wigger17@gmail.com
# Version: 1.6 - 29/11/2021

import argparse
import os
import re
import time

def is_xml_file(destination_path):
	if destination_path.endswith('.xml'):
		if os.path.isdir(destination_path.rsplit('/',1)[0]):
			return True
		else:
			return False
	else:
		return False

def get_text_single_file(source_path):
	if(source_path.endswith('.txt')):
		with open(source_path,'r') as reader:
			return reader.read()

def get_text_multiple_files(source_path):
	combined_text = ""
	for filename in os.listdir(source_path):
		if(filename.endswith('.txt')):
			with open('{}/{}'.format(source_path,filename)) as reader:
				combined_text = "{} {}".format(combined_text, reader.read())
	return combined_text

def get_most_common_words(text, N):
	# Regex expression to remove punctuation from text
	text = re.sub("[^\w\s]", "", text)
	common_words = {}
	for word in text.split():
		if word in common_words:
			common_words[word] += 1
		else:
			common_words[word] = 1
	return dict(sorted(common_words.items(),
				key=lambda item:item[1],
				reverse=True)[:N])

def convert_to_xml(word_dict):
	xml = "<topwords>\n"
	for word in word_dict:
		xml += "<word length=\"{}\">{}</word>\n".format(str(len(word)),word)
	xml += "</topwords>"
	return xml

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-s','--source_path',
						help='Provide path of a file or directory',
						type=str,
						metavar='')
	parser.add_argument('-d','--destination_path',
						help='Provide a destination path to save the XML file',
						type=str,
						metavar='')
	parser.add_argument('-n','--most_common_count',
						help='(N) most common words to retrieve from source',
						type=int,
						metavar='')
	args = parser.parse_args()
	if os.path.isdir(args.destination_path):
		if not args.destination_path.endswith('/'):
			args.destination_path = '{}/'.format(args.destination_path)
		args.destination_path = '{}most_common_words.xml'.format(args.destination_path)
	return args

def main():
	args = get_args()
	# Check params provided by user
	try:
		if os.path.isdir(args.destination_path) or is_xml_file(args.destination_path):
			if os.path.isdir(args.source_path):
				text = get_text_multiple_files(args.source_path)
				if text.isspace():
					raise OSError('Source_path Error: The .txt files in folder are all empty.')
			elif os.path.isfile(args.source_path):
				if os.stat(args.source_path).st_size != 0: # Check if file is empty
					text = get_text_single_file(args.source_path)
				else:
					raise OSError('Source_path Error: File .txt is empty.')
			else:
				raise OSError('Source_path Error: Provide existing directory or file path.')
			most_common_words = get_most_common_words(text, args.most_common_count)
			xml = convert_to_xml(most_common_words)
			# Save XML file
			with open("{}".format(args.destination_path),'w') as writer:
				writer.write(xml)
		else:
			raise OSError('Destination_path Error: Provide existing directory path or .xml file path.')
	except OSError as e:
		print(e)


if __name__ == "__main__":
	start_time = time.time()
	main()
	print("--- %s seconds ---" % (time.time() - start_time))
