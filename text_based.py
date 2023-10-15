from bs4 import BeautifulSoup
import markdown
from markdown.extensions import def_list
from markdown.extensions import md_in_html
from markdown.extensions import sane_lists
from markdown.extensions.toc import TocExtension
import datetime
import os
from pathlib import Path as P


class FileExtract:

    """Class for extracting data from files"""

    @staticmethod
    def from_markdown(*paths: str) -> dict:
        """
        Extract all data from a path and return dictionary of filename and text
        """
        content_dict = {}

        for p in paths:
            path = P(p)

            if path.is_file() and path.suffix == '.md':
                content_dict[path.name] = path.read_text()

            elif path.is_dir():
                for p in path.rglob('*'):
                    #print(f"\ni: {i}\npath: {path}")
                    if p.is_file() and p.suffix == '.md':
                        content_dict[p.name] = p.read_text()

        return content_dict


class SyntaxApply:
    """
    Pass data amoungst functions in this module
    """
    @staticmethod
    def MD_def_list(d:dict, soup:bool=True) -> dict:
        """Return a dictionary keeping the same keys and formatting the items as indicated below"""
        #:todo:print(type(d.items())) # appears tuple of list of tuples that are string pairs
        d_MD_DL = {}
        for k, v in d.items():
            d_MD_DL[k] = markdown.markdown(v, extensions=['markdown.extensions.def_list'])

        if soup:
            return SyntaxApply.toBeautifulSoup(d_MD_DL)
        else:
            return d_MD_DL
        
    @staticmethod
    def toBeautifulSoup(d:dict) ->dict:
        d_BS = {}
        for k, v in d.items():
            d_BS[k] = BeautifulSoup(v, "html.parser")
        return d_BS

    
class ObtainMarkdownData:
    
    def dictionary_items(file_path: ['string','or list of files']) -> dict:
        """
        Return a dictionary of terms and all associated definitions from a file or list of files
        Note: dependant on 'all_data' function in this class

        Input: filepath or list of filepaths
        Output: dictionary with a key pair of the term (dt) and a list of definitions (dd)

        to update: include div class dictionary if in file passed
        """

        all_data = ObtainMarkdownData.all_data(file_path)        
        soup = BeautifulSoup(all_data, "html.parser")
        
        dl_tags = soup.find_all("dl")  # find all <dl> tags in the document
        dt_dd_pairs = []  # list of tuples to track dt and dd pairs

        for dl_tag in dl_tags:
            current_dt = None  # flag
            current_dd_list = []  # track multiple definitions

            for tag in dl_tag.children:
                if tag.name == "dt":
                    if current_dt is not None and current_dd_list:
                        dt_dd_pairs.append((current_dt, current_dd_list))
                    current_dt = tag.text.strip()
                    current_dd_list = []
                elif tag.name == "dd" and current_dt is not None:
                    current_dd_list.append(tag.text.strip())

            if current_dt is not None and current_dd_list:
                dt_dd_pairs.append((current_dt, current_dd_list))

        dictionary_dt_listof_dd = dict(dt_dd_pairs)
        return dictionary_dt_listof_dd
    
    @staticmethod    
    def dictionary_div(file_path) -> dict:
        """  
        Obtain the contents of a "dictionary" div and return results as
        1. html formatted string
        """

        with open(file_path, 'r') as file:
            soup = BeautifulSoup(file.read(), "html.parser")
            dictionary_div = soup.find("div", class_="dictionary") # type <class 'bs4.element.Tag'>
            dictionary_div_string = str(dictionary_div)

            string_remove_div_header = dictionary_div_string.replace('<div class="dictionary">', '')
            string_remove_div_footer = string_remove_div_header.replace('</div>', '')

            def_list_content = markdown.markdown(string_remove_div_footer, extensions=['markdown.extensions.def_list'])
            another_can_of_soup = BeautifulSoup(def_list_content, 'html.parser')
                
            # merge below object as this is basically duplicated

            dl_tags = another_can_of_soup.find_all("dl")  # find all <dl> tags in the document
            dt_dd_pairs = []  # list of tuples to track dt and dd pairs

            for dl_tag in dl_tags:
                current_dt = None  # flag
                current_dd_list = []  # track multiple definitions

                for tag in dl_tag.children:
                    if tag.name == "dt":
                        if current_dt is not None and current_dd_list:
                            dt_dd_pairs.append((current_dt, current_dd_list))
                        current_dt = tag.text.strip()
                        current_dd_list = []
                    elif tag.name == "dd" and current_dt is not None:
                        current_dd_list.append(tag.text.strip())

                if current_dt is not None and current_dd_list:
                    dt_dd_pairs.append((current_dt, current_dd_list))

            dictionary_dt_listof_dd = dict(dt_dd_pairs)
            return dictionary_dt_listof_dd
        
    @staticmethod
    def get_md_files(directory_list):
        md_files = []
        for root, _, files in os.walk(directory_list):
            for filename in files:
                if filename.endswith('.md'):
                    md_files.append(os.path.join(root, filename))
        return md_files

class formatMarkdownDictionary:
    """ Format the dictionary for specific quiz or flashcards purposes"""

    def format_dictionary(definition_dictionary) ->dict:
        """ Format dictionary per instructions in the definition
        q| {side1}, {keyword}, {optional additional terms - def2, 3, 4
        returns dictionary with term being a list so it can be parsed for flashcards deluxe
        }"""

        dict_instructions = {}

        for key, values in definition_dictionary.items():
            for value in values:
                if value.startswith('q|'):
                    instructions = value.replace('q|', '').strip().split(',')
                                       

                    if len(instructions) < 2:
                        first_side = instructions[0]
                        keywords = 'no keywords'
                    else:
                        first_side = instructions[0]
                        keywords = instructions[1]
                    
                    dict_instructions[key] = {
                        'first-side' : first_side,
                        'keywords' : keywords,
                        #'additional' : additional,
                        }

        print('finstuctions \n', dict_instructions)
                    
        output_dict = {}
        print(definition_dictionary)
                    
        for key, values in dict_instructions.items():
            if values['first-side'] == '1':
                output_dict[key] = {
                    'side-1' : key,
                    'side-2' : definition_dictionary[key][0],
                }
            if values['first-side'] == '2':
                output_dict[key] = {
                    'side-1' : definition_dictionary[key][0],
                    'side-2' : key,
                }
            if values['first-side'] == 'b':
                output_dict[key] = {
                    'side-1' : key,
                    'side-2' : definition_dictionary[key][0],
                }
                
                output_dict[key + '_swapped'] = {
                    'side-1': definition_dictionary[key][0],
                    'side-2': key,
                }

        print('\n\n\n\n\noutput dict \n', output_dict)

        second_output_dictionary = {value['side-1']: [value['side-2']] for value in output_dict.values()}


        print('\n\n\nsecibd output dict \n', second_output_dictionary)

        return second_output_dictionary
     



class WriteToFile:
    """Take data and write it to an output file"""
    
    def flashcard_deluxe(dictionary_text, output_file, def_number=1) -> ['file']:
        """
        input: dictionary of term and list of definition(s)
        output: flashcard file on onedrive
        Take the dictionary and write it to a tab deliminated file used for flashcards
        """

        flashcard_path = '/Users/pr-mbausr/Library/CloudStorage/OneDrive-Personal/Apps/Flashcards Deluxe/'
        def_index = def_number-1

        with open(flashcard_path + output_file, 'w') as textfile:
            for key, value in dictionary_text.items():
                textfile.write(f"{key}\t {value[def_index]}\n")
        print(f'Item Count: {len(dictionary_text.keys())}')
        print(f'File written to: {flashcard_path + output_file}')
    
    def backup_file(file_path):
        """ Create a backup file of the original markdown file before modifications"""
        backup_file_path = f'{file_path}-june-15-1.bak'
        with open(file_path, 'r') as file:
            with open(backup_file_path, 'w') as backup_file:
                backup_file.write(file.read())
                backup_file.close()

    def add_dictionary_to_dictionary_div(output_file_path, sorted_dictionary_text):
        """ Input is the text of the dictionary data sorted in the sort dictionary function"""
        with open(output_file_path, 'r') as file:
            soup = BeautifulSoup(file.read(), "html.parser")
            plain_text_div = soup.find("div", class_="dictionary")
            plain_text_div.string = "\n\n" + sorted_dictionary_text + "\n"
    
        with open(output_file_path, 'w') as file:
            file.write(str(soup))

@staticmethod
def weakly_programmed_methods():

    def sort_dictionary(html_formatted_div):
        """ Input is a div formatted as an html.  Output is a string of formatted text""" 
        soup = BeautifulSoup(html_formatted_div, "html.parser")
        dl_tag = soup.find("dl") # find the first dl tag for what purpose?

        dt_dd_pairs = [] # list of tuples to track dt and dd pairs
        current_dt = None # flag to track current dt
        current_dd_list = [] # list of strings to track multiple definitions


        for tag in dl_tag.children:
            if tag.name == "dt":
                if current_dt is not None and current_dd_list:
                    dt_dd_pairs.append((current_dt, "\n".join(current_dd_list)))
                current_dt = tag.text.strip()
                current_dd_list = []
            elif tag.name == "dd" and current_dt is not None:
                current_dd_list.append(tag.text.strip())
        if current_dt is not None and current_dd_list:
            dt_dd_pairs.append((current_dt, "\n".join(current_dd_list)))

        sorted_dt_dd_pairs = sorted(dt_dd_pairs, key=lambda pair: pair[0].lower())
        sorted_dictionary_text = "\n".join([f"{dt}\n: {dd}\n" for dt, dd in sorted_dt_dd_pairs])
        return(sorted_dictionary_text)

    def extract_list_items(content):
        """Take content from the ?def-list-content? function and extract the list items"""
        soup = BeautifulSoup(content, "html.parser")

        ul_tags = soup.find_all("ul")  # Find all <ul> tags in the document
        ol_tags = soup.find_all("ol")  # Find all <ol> tags in the document
        all_list_tags = ul_tags + ol_tags

        list_item_pairs = []  # List of tuples

        for list_tag in all_list_tags:
            current_li = None
            current_list = []
            paragraph = None

            # Find the previous paragraph tag
            prev_paragraph_tag = None
            for sibling in list_tag.previous_siblings:
                if sibling.name == "p":
                    prev_paragraph_tag = sibling
                    break

            if prev_paragraph_tag:
                paragraph = prev_paragraph_tag.get_text().strip()

            for tag in list_tag.children:
                if tag.name == "li":
                    if current_li is not None:
                        current_list.append(current_li)
                    current_li = tag.get_text().strip()
                elif tag.name in ["ul", "ol"] and current_li is not None:
                    current_list.append(tag.get_text().strip())

            if current_li is not None:
                current_list.append(current_li)
                list_item_pairs.append((paragraph, current_list))

        list_text = dict(list_item_pairs)
        print(list_text)
        return list_text

    def list_items(content):
        """Take content from the ?def-list-content? function and extract the list items"""
        soup = BeautifulSoup(content, "html.parser")

        ul_tags = soup.find_all("ul")  # Find all <ul> tags in the document
        ol_tags = soup.find_all("ol")  # Find all <ol> tags in the document
        all_list_tags = ul_tags + ol_tags

        list_item_pairs = []  # List of tuples

        for list_tag in all_list_tags:
            current_li = None
            current_list = []
            paragraph = None

            # Find the previous paragraph tag
            prev_paragraph_tag = None
            for sibling in list_tag.previous_siblings:
                if sibling.name == "p":
                    prev_paragraph_tag = sibling
                    break

            if prev_paragraph_tag:
                paragraph = prev_paragraph_tag.get_text().strip()

            for tag in list_tag.children:
                if tag.name == "li":
                    if current_li is not None:
                        current_list.append(current_li)
                    current_li = tag.get_text().strip()
                elif tag.name in ["ul", "ol"] and current_li is not None:
                    current_list.append(tag.get_text().strip())

            if current_li is not None:
                current_list.append(current_li)
                list_item_pairs.append((paragraph, current_list))

        list_text = dict(list_item_pairs)
        return list_text

def main():
    # pull from file
    file_path = input("Enter the file(s) to pull from: ")
    while not file_path:
        print("No file path provided. Please try again.")
        file_path = input("Enter the file path: ")

    # add intermediary steps to select what options to chose
    output_flashcard_txtfile = input("Enter output file path for flashcards: ")
    while not output_flashcard_txtfile:
        print("No file path provided. Please try again.")
        output_flashcard_txtfile = input("Enter the file path: ")

    # add option to specify - this was written to return the sorted div text back to a md file in a "dictionary" div
    output_file_path = input("Enter output file path: ")
    if not output_file_path:
        output_file_path = file_path


if __name__ == "__main__":
    main()
