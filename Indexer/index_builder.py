from __future__ import division
import os
import feedparser
import string
from bs4 import BeautifulSoup
from lxml.html import soupparser
import nltk, re, pprint
from bs4 import BeautifulSoup
from nltk import word_tokenize
path = "WEBPAGES_RAW"
bad_count=0

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

def crawl_files:
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
                    read_files(path+'/'+pathname+'/'+filename)

def read_files(file_name):
    
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
    content = f.read()

    # if fileName.endswith([".html", ".htm", "xhtml", "jhtml"]):
    	try:
        	root = html.fromstring(content)

            except Exception as e:
                print "Parse Error occured"


            try:
                
                ignore = html.tostring(root, encoding='unicode')

            except (Exception, UnicodeDecodeError) as e:
                root = html.soupparser.fromstring(content)

            
     

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
