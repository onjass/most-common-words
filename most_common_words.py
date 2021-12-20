# About: Creation of XML file with the N most common words from plain text file(s)
# Version: 1.8 - 2021/12/08

import argparse
import os
import re
import time
import sys

def get_text(source_path):
	text = ''
	try:
		if os.path.isfile(source_path):
			with open(source_path) as reader:
				text = reader.read()
		elif os.path.isdir(source_path):
			for filename in os.listdir(source_path):
				with open('{}/{}'.format(source_path,filename)) as reader:
					text = "{} {}".format(text, reader.read())
		else:
			raise OSError('Source_path Error: Provide an existing path.')
			sys.exit()
		return text
	except UnicodeDecodeError as e:
		print('ERROR - Provide a directory with plain text files or a path to a plain text file (UTF-8).')
		sys.exit()

def get_most_common_words(text, N):
	text = re.sub("[^\w\s]", "", text) # Regex expression to remove punctuation from text
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
		xml += "\t<word length=\"{}\">{}</word>\n".format(str(len(word)),word)
	xml += "</topwords>"
	return xml

def get_args():
	description = '''
	************************
	Most Common Words script
	************************
	This script provides a simple and quick way to collect the (N) most common
	words from a plain text file or a directory containing multiple plain text
	files. Note that the encoding of the file(s) should be in UTF-8
	'''
	parser = argparse.ArgumentParser(description=description,
									 formatter_class = argparse.RawDescriptionHelpFormatter)
	parser.add_argument('-s','--source_path',
						help='Provide path of a file or directory',
						type=str,
						metavar='')
	parser.add_argument('-d','--destination_file_path',
						help='Provide a destination path to save the XML file',
						type=str,
						metavar='')
	parser.add_argument('-n','--most_common_count',
						help='(N) most common words to retrieve from source',
						type=int,
						metavar='')
	args = parser.parse_args()
	return args


def main():
	args = get_args()
	# Check params provided by user
	try:
		text = get_text(args.source_path)
		if text == '':
			raise OSError('Source_path Error: File(s) are empty')
			sys.exit()
		most_common_words = get_most_common_words(text, args.most_common_count)
		xml = convert_to_xml(most_common_words)
		try:
			with open("{}".format(args.destination_file_path),'r+') as writer:
				writer.write(xml) # If destination file .XML does not exist - error
		except OSError as e:
			print('Destination_path Error: The path provided does not exist')
			sys.exit()
	except OSError as e:
		print(e)
		sys.exit()


if __name__ == "__main__":
	start_time = time.time()
	main()
	print("--- %s seconds ---" % (time.time() - start_time))
