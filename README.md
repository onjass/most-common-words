# Most Common Words
A simple Python script that provides a XML file with the N-most common words from a .txt file or a directory containing multiple .txt files.

## Goal
The aim of this small project is to provide the possibility to any user to execute this script to get the most common words of :
- Either a directory containing multiple .txt files
- Or a single .txt file

It finally saves the N most common words from your source path as a XML in the destination path provided.

## Example
Suppose you have a directory with three .txt files in it :

<img width="148" alt="image" src="https://user-images.githubusercontent.com/61325001/143904945-22825eb1-f633-4ca3-8381-d24bade2c9bc.png">

Here's a sample of the first file :

<img width="678" alt="image" src="https://user-images.githubusercontent.com/61325001/143905058-e7ddea0d-3ca0-45ec-ae33-0ebfff04ba70.png">

_Note : You can create sample .txt files using this dummy text generator_ : https://www.blindtextgenerator.com/lorem-ipsum

Before executing the script, you can have a look at the parameters needed :

```
python3 most_common_words.py --help
```

<img width="435" alt="image" src="https://user-images.githubusercontent.com/61325001/143906157-45e24f72-94e3-4ec0-968c-79766256c3e5.png">

Then, simply run the following command that gives you the 10 most common words :

```
python3 most_common_words.py -s /your-path-to-directory/or-single-file.txt/ -d /destination-folder/or-file.xml/ -n 10
```
## Results

<img width="259" alt="image" src="https://user-images.githubusercontent.com/61325001/143907027-721f6160-b21a-4faf-8547-78512b8a114a.png">
