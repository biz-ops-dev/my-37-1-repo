from dataclasses import dataclass

"""
Usage
 1. temporary script to create flashcards from items created by _mod_markdown.py
 2. Record intended changes to related module to reduce complexity and improve efficienct

Intended Changes - _mod_markdown.py
 1. file input
    allow string or list of strings vs only one
 2. When obtaining all dictionary
    items include ones in a 'div' class = dictionary
    items include ones in a 'div' class = dict

 3. When writing to flashcard file allow ability to append to what exists
 4. Find way to quickly recall common files and folders
 5. Pull `python` code block from all files

Quiz file
 1. quiz from items in a table - see git file below

 determine better way to do below
     def flashcard_deluxe(dictionary_text, output_file, def_number=1) -> ['file']:
     
learn call functions from method

add below to _mod_markdown_py so can run as script and make flashcards

"""

from _mod_markdown import ObtainMarkdownData
from _mod_markdown import WriteToFile
from _mod_markdown import *

# files
list_earned_value = ['/Users/pr-mbausr/Library/CloudStorage/OneDrive-Personal/notes/Business/Accounting/managerial accounting/earned value analasys.md']
string_earned_value = list_earned_value[0]
accounting_introduction = '/Users/pr-mbausr/Library/CloudStorage/OneDrive-Personal/notes/Business/Accounting/financial accounting/1-Introduction.md'
control_flow = '/Users/pr-mbausr/Library/CloudStorage/OneDrive-Personal/notes/Technology/Python/data types/control-flow/control_flow.md'
git = '/Users/pr-mbausr/Library/CloudStorage/OneDrive-Personal/notes/Technology/other-tools/git.md'

#print('list file\n', ObtainMarkdownData.dictionary_items(list_earned_value))
#print('string file\n', ObtainMarkdownData.dictionary_items(string_earned_value))

"""
print('list file\n', ObtainMarkdownData.dictionary_items_delete_single_file_only(list_earned_value))
print('string file\n', ObtainMarkdownData.dictionary_items_delete_single_file_only(string_earned_value))
"""

#convert_file_path(string_earned_value)

acct_dictionary = ObtainMarkdownData.dictionary_div(accounting_introduction)
WriteToFile.flashcard_deluxe(acct_dictionary, 'fi-acct-from-intro-div.txt')

@dataclass
class SideOneFirst:
   side1: str
   side2: str

   
    
