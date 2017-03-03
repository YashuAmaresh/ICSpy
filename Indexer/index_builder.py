from __future__ import division
import os
import feedparser
import string
from bs4 import BeautifulSoup
from lxml.html import soupparser
import nltk, re, pprint
from bs4 import BeautifulSoup
import magic
from nltk import word_tokenize          
from nltk.stem.porter import PorterStemmer

path = "WEBPAGES_RAW"
bad_count=0
file_handle_list = list()
curr_file_count = 0
index_dict = dict()
curr_url_count = 0

def isValid(url):
    global bad_count 
    parsed = urlparse(url)
    try:
        return_val=False
        return_val = ".ics.uci.edu" in parsed.hostname \
        and not re.match(".*\.(css|js|pdf|bmp|gif|jpe?g|ico" + "|png|tiff?|mid|mp2|mp3|mp4"\
        + "|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf" \
        + "|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso|epub|dll|cnf|tgz|sha1" \
        + "|thmx|mso|arff|rtf|jar|csv"\
        + "|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())
                      
        if return_val: #Only if the url is valid check for the traps
        # 1. Repeating directories
            url_str = parsed.path.lower().rstrip("/") + "/"
            if re.match("^.*?(/.+?/).*?(.*\\1){3,}.*$|^.*?/(.+?/)(.*/?\\1){3,}.*$", url_str):
                return_val = False        
            if "cgvw.ics.uci.edu" in parsed.hostname:
                return_val=True
            if not return_val:
                bad_count+=1     #For Logistics          
            return return_val
        else:
            return return_val
    except TypeError:
        print "Error"

def crawl_files():
    ''' Crawl the Files domain and retrieve the information from each file.
        Classify the file type and call the Read_file
        Call the Inverted_Indexer
    '''
    with open("bookkeeping.json") as json_data:        
        data=json.load(json_data)
        for pathname in os.listdir(path):
            for filename in os.listdir(path+"/"+pathname):
                url ="//"+ data[pathname+'/'+filename]
                if(isValid(url)):
                    process_files(path+'/'+pathname+'/'+filename)

def process_files(file_name):
    
    ''' Read the files based on the file type .
        Parse and Process the HTML files here
        Call the Key_Indexer to Index key content
        Call the Base_Indexer to Index Text content
        Tag the Key Dictionary with the Key List
        Tag the Base Dictionary with the Base List
    '''

    fileName = file_name
    fileName = fileName.strip()

    f = open(fileName)
    type_of_content = magic.from_file(fileName)
    content = f.read()

    # if fileName.endswith([".html", ".htm", "xhtml", "jhtml", "txt"]):
    if type_of_content.strip().startswith('ASCII text'):	#Text Data
    	tokens = tokenizeText(content)

    else: #HTML data	
    	try:
        	root = BeautifulSoup(content)

		except (Exception, UnicodeDecodeError) as e:
			print e
			return

		for script in root(["script", "style"]):
    		script.extract()    #extract these unnecessary tags

    	text = root.get_text()

		# break into lines and remove leading and trailing space on each
		lines = (line.strip() for line in text.splitlines())
		# break multi-headlines into a line each
		chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
		# drop blank lines
		text = '\n'.join(chunk for chunk in chunks if chunk)

		print(text)


		#If no exception occured:
		tokens = tokenizeText(text)
		fancyTokens = tokenizeHTML(root)

	index_tokens(tokens, docID)

	f.close()






def tokenizeText(content):
	'''Tokenize text by removing punctuations '''
	stemmer = PorterStemmer()

	processed_tokens = list()
	if content and content.strip():
		content = content.strip()
		lines = content.split('\n')
		lines = [line.strip() for line in lines]

		for line in lines:
			text = "".join([ch for ch in text if ch not in string.punctuation])
			tokens = nltk.word_tokenize(text)
			stems = stem_tokens(tokens, stemmer)
			processed_tokens.extend(stems)

	return processed_tokens


def tokenizeHTML(root):
	pass
                



            
     

def Key_Indexer(content):
    
    '''
    Remove stopwords  with caution . If the stop words have a frequency of more than 2/5 of total word count.
    Stem the words.
    Call the Tokenizer function
    Index the content in this field as very important and given a higher priority
    Return a dictionary of Word,Frequency
    '''
    
def Base_Indexer(content):
    
    '''
    Index the general text content here
    Remove Stopwords and Stem words
    Return a dictionary of Word,Frequency
    '''
    
def Tokenizer(words):
    
    '''
    Implement the Tokenizer and tokenize the content.
    Sort the tokens as per the frequency and return the dictionary of words-frequency
    '''
    
def Inverted_Indexer(Key_List,Base_List):
    
    '''
    Form the Inverted Index for the Key_List and the Base_List
    '''
def Statistics():

    '''
    For Analytics
    '''


def create_Index():
	file_name = "index_head"
	try:
    	os.remove(filename)
	except OSError:
    	pass
	f = open(filename, 'a')

	create_letter_index()

	crawl_files(f)



def create_letter_index():
	letters = string.ascii_uppercase
	letter_file_map = map(lambda x: "index_" + x, list(letters))

	for name in letter_file_map:
		try:
    		os.remove(filename)
		except OSError:
    		pass
		f = open(filename, 'a').close()

	f = open("index_NUM", 'a').close()


def open_letter_index():
	global file_handle_list

	letters = string.ascii_uppercase
	letter_file_map = map(lambda x: "index_" + x, list(letters))

	
	for name in letter_file_map:
		file_handle = open(name, 'a')
		file_handle_list.append(file_handle)

	file_handle_list.append(open("index_NUM", 'a')) #Index File for numbers


def close_letter_index():
	global file_handle_list

	for handle in file_handle_list:
		handle.close()



def index_tokens(tokens, doc_ID):
'''Index Token list by adding them to the dictionary. Also, write the tokens to file when each set of 5000 files are processed.'''
	global curr_file_count
	global index_dict
	global curr_url_count 

	curr_url_count += 1

	if curr_url_count % 5000 == 0:
		#close curr_file by writing contents of the dict to the file and open new file
		#add values to the dictionary

		curr_file_count += 1
		fileName = "index_file_" + str(curr_file_count)

		f = open(fileName, 'w')
		# f.write(str(len(index_dict)) + '\n') #1st line of the file is the number of entries in the file
		for word in sorted(index_dict): 
			json.dump([word, len(word), index_dict[word]], f)
			f.write("\n")

		f.close()

		index_dict = dict()


	for token in tokens:
		word_chain = index_dict.get(token, dict())
		word_chain[doc_ID] = word_chain.get(doc_ID, 0) + 1





def write_index_to_file():
	pass

def merge_indexes():
	pass




