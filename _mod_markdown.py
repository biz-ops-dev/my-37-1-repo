"""
Write about
  how allow for multiple input files
   - list extend (not append)

   main() at end

Future:
  option to remove terms from old file
  # is it ok to have a class without any init methods?
"""


from bs4 import BeautifulSoup
import markdown
from markdown.extensions import def_list
from markdown.extensions import md_in_html
from markdown.extensions import sane_lists
from markdown.extensions.toc import TocExtension
import datetime

class ObtainMarkdownData:
    """ Obtain data from Markdown"""

    @staticmethod
    def obtain_all_infile_data(file_path) -> str :
        """
        Obtain the contents of a markdown file with the markdown extension _def_list
        
        Input: string or list of strings of filenames of markdown file
        Output: String containing all content from inputted files formatted with a def_list parser (happens to be functional well beyond def lists)
        Dependencies: markdown.extensions.def_list
        """

        list_of_content = []
    
        for file_path in file_path:
                with open(file_path, 'r') as file_obj:
                    content = file_obj.read()
                    def_list_content = [markdown.markdown(content, extensions=['markdown.extensions.def_list'])]

                    # first wrong order but now fixed - extend 
                    list_of_content.extend(def_list_content)

        #New: make list into single string to process
        string_list_of_content = ' '.join([str(item) for item in list_of_content])

        return string_list_of_content
    
    def extract_dict_items(def_list_content) -> dict:
        """
        Input:
        Output: dictionary with a key pair of the term (dt) and a list of definitions (dd) """
        soup = BeautifulSoup(def_list_content, "html.parser")
        dl_tags = soup.find_all("dl")  # find all <dl> tags in the document
        dt_dd_pairs = []  # list of tuples to track dt and dd pairs

        for dl_tag in dl_tags:
            current_dt = None  # flag to track current dt
            current_dd_list = []  # list of strings to track multiple definitions

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
        return list_text

    def string_formatted_div(file_path):
        """ Obtain the contents of a "dictionary" div and return results as html
        UNTESTED since moved into class
        """
        with open(file_path, 'r') as file:
            soup = BeautifulSoup(file.read(), "html.parser")
            plain_text_div = soup.find("div", class_="dictionary")
            html_formatted_div = markdown.markdown(plain_text_div.get_text(), extensions=['markdown.extensions.def_list'])
        return html_formatted_div

class WriteMarkdownData:
    """ Write data to Markdown"""
    
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


class WriteNonMarkdown:
    """ Write data to other files not markdown"""

    def flashcard_file(dictionary_text, output_file):
        """ Take the dictionary and write it to a tab deliminated file used for flashcards.  Use the first definition in the list. """

        flashcard_path = '/Users/pr-mbausr/Library/CloudStorage/OneDrive-Personal/Apps/Flashcards Deluxe/'

        with open(flashcard_path + output_file, 'w') as textfile:
            for key, value in dictionary_text.items():
                textfile.write(f"{key}\t {value[0]}\n")
        print(f'Item Count: {len(dictionary_text.keys())}')
        print(f'File written to: {flashcard_path + output_file}')


# add below to classes 
''''''
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

def main():
    file_path = input("Enter the file(s) to pull from: ")
    while not file_path:
        print("No file path provided. Please try again.")
        file_path = input("Enter the file path: ")

    # add intermediary steps to select what options to chose
    print()
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