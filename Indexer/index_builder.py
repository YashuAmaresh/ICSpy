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

def crawl_files:
    ''' Crawl the Files domain and retrieve the information from each file.
        Classify the file type and call the Read_file
        Call the Inverted_Indexer
    '''
    for pathname in os.listdir(path):
        for filename in os.listdir(path+"/"+pathname):    
          with open(path+'/'+pathname+'/'+filename) as files:
              read_file(files)
    
def read_files(file_name):
    
    ''' Read the files based on the file type .
        Parse and Process the HTML files here
        Call the Key_Indexer to Index key content
        Call the Base_Indexer to Index Text content
        Tag the Key Dictionary with the Key List
        Tag the Base Dictionary with the Base List
    '''
     try:
                root = html.fromstring(htmlStr)

            except Exception as e:
                print "Parse Error occured"
                continue

            try:
                
                ignore = html.tostring(root, encoding='unicode')

            except UnicodeDecodeError:
                root = html.soupparser.fromstring(htmlStr)
     

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
def Statistics:

    '''
    For Analytics
    '''
