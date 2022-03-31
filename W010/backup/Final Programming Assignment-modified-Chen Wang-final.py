'''
File Name: Final Programming Assignment-modified-Chen Wang.py
Extension:
Function:
    # 0.2: Define a function that can replace its relative link from the https://www.dictionary.com
Content:
    # 1e: Search for the word meaning from the dictionary website, and store the first definition.
            # 1e.1: Open dictionary website from dictionary.com ex: 'https://www.dictionary.com/browse/bazaar'
            # 1e.2: Find the definition and store it in a dictionary only
    # 1f: Create a sheet to store an example (sentence) from the article which is relative to the new word
            # 1f.1: Store all sentences from the article
            # 1f.2: Compared to the vocabulary list, store them in a new create dictionary
    # 2b: Ask the user if want to replace the old one
            # 2b.1: Give a warning when vocabulary's definitions are not empty
            # 2b.2: Request a definition
            # 2b.3: Store it in a defined dictionary

Agenda
Function:
    # 0.1: Define a function that can replace its relative link from the http://classicshorts.com
Content:
    # 1~3 read a relative link, storage vocabulary, and give its definition, then save it
        1: Open a relative link from a complete URL then return how many vocabularies in the relative link
            1a: Give a word and return its relative link
            1b: Use Beautifulsoup,  parser and decode defined URL
            1c: Get vocabularies from this relative link
            1d : 1d: Feedback to the user how many vocabularies was found in these relative links
        2: check if want to store a definition or not, storage a vocabulary (from relative links) and its definition (user-defined)
            2a: Request to key-in a word and store its definition when the user feedback 'Y'
                2a.1: Give a warning when vocabulary's definitions are not empty
                2a.2: Request a definition
                2a.3: Store it in a defined dictionary
        3: After completing to storage vocabulary and its definitions, save file and print vocabulary and its definition to a file
            3a: check  the longest characters in the storage dictionary
            3b: Request a filename from the user
            3c: follow the order to store the term(vocabularies/definitions to the file)
'''

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin
import re

# 0.1: Define a function that can replace its relative link from the http://classicshorts.com
def combine(file):
    website = urljoin ('http://classicshorts.com/stories/aos.html', file) + '.html'
    return website
# 0.2: Define a function that can replace its relative link from the https://www.dictionary.com
def CheckDict(SearchWord):
    Dict_word = 'https://www.dictionary.com/browse/' + SearchWord
    return Dict_word

# 1~3 read a relative link, storage vocabulary, and give its definition, then save it
# If fine error, keep doing, others follow the order to complete
dictionary = {}
example = {}
FileCheck = True
while FileCheck :
    try:
        # 1: Open a relative link from a complete URL then return how many vocabularies in the relative link
        # 1a: Give a word and return its relative link
        askfile = input ('What\'s the short story path? ')
        response = urlopen(combine(askfile))
        # 1b: Use Beautifulsoup,  parser and decode defined URL
        soup = BeautifulSoup(response, 'html.parser')
        # 1c: Get vocabularies from this relative link
        # hint: <a href='http://dictionary.reference.com/browse/Sedan' target=0>Sedan</a> get ''Sedan''
        atag = soup.find_all('a')
        for i in atag:
            # only get vocabulary from dictionay website, others regret!
            if i.get('href')[:17] == 'http://dictionary':
                dictionary[i.get('href').replace("http://dictionary.reference.com/browse/", "")]= ''
                example[i.get('href').replace("http://dictionary.reference.com/browse/", "")] = ''
        # 1d: Feedback to the user how many vocabularies was found in these relative links
        if len(dictionary) > 1:
            print('Short story found. There are {} unique vocabulary words.'.format(len(dictionary)))
        elif len(dictionary) == 1:
            print('Short story found. There are only 1 unique vocabulary word.')
        # Stop when pycharm found no vocabulary (no need saved, directly stop)
        else:
            print('Short story \033[94m\033[1mfound\033[0m. \033[91m\033[1mBut there are no vocabulary word.\033[0m')
            break

        # 1e: Search for the word meaning from the dictionary website, and store the first definition.
        # 1e.1: Open dictionary website from dictionary.com ex: 'https://www.dictionary.com/browse/bazaar'
        for i in list(dictionary.keys()):
            result = urlopen(CheckDict(i))
            soup_Dict = BeautifulSoup(result, 'html.parser')
            a_tags = soup_Dict.find_all('meta')
            Word_Temp = []
            # Store all the information into a temp list
            for tag in a_tags:
                dreamstring = "definition"
                Content_Temp = tag.get('content')
                Word_Temp.append(Content_Temp)

            # 1e.2: Find the definition and store it in a dictionary only
            # Find the word 'definition' in a specified position: Word_Temp[1]
            dreamstring = "definition"

            # Located where the definition start and end
            startindex = 0
            startindex = Word_Temp[1].index("definition", startindex)
            startindex = Word_Temp[1].index(",", startindex)
            endindex = Word_Temp[1].index('.', startindex)
            # Store them!
            dictionary[i] = Word_Temp[1][startindex+2: endindex + 1]

        # 1f: Create a sheet to store example (sentence) from the article which is relative to the new word
        # 1f.1: Store all sentence from the article.
        new_string =[]
        story = soup.findAll('div', attrs={'class': 'StoryPara'})
        for para in story:
            detail = re.split(r'[.;!?\t|]', para.text)
            for additem in detail:
                if len(additem) > 0:
                    if additem[0] == ' ':
                        new_string.append(additem[1:])
                    else:
                        new_string.append(additem)


        # 1f.2: Compared to the vocabulary list, store them in a new create dictionary
        for key in list(example.keys()):
            for sentence in new_string:
                if key in sentence:
                    example[key] = sentence
                    break


        # 2. check if want to store a definition or not, storage a vocabulary (from relative links) and its definition (user-defined)
        # Allow users to key-in vocabulary's definition, until he/she stops
        YesorNoCheck = True
        while YesorNoCheck:
            addask = input ('Would you like to update a definition (Y/N)? ')
            # only allow to go when user key-in Yes or No
            try:
                # 2a: Request to key-in a word and store its definition when the user feedback 'Y'
                if addask == 'Y' or addask == 'Yes' or addask == 'yes' or addask == 'y':
                    term = input('Term: ')
                    if term in dictionary.keys():
                        # 2a.1: Give a warning when vocabulary's definitions are not empty
                        if dictionary[term] != '':
                            print("\033[91m\033[1mWARNING!\033[0m {} is currently defined as \033[91m\033[1m'{}'.\033[0m".format(
                                    term, dictionary[term]))
                            # 2b: Ask the user if want to replace the old one
                            Warningcheck = True
                            while Warningcheck:
                                Warningask = input(
                                    'Would you \033[94m\033[1mSTILL\033[0m like to update a definition (Y/N)? ')
                                # 2b.1: Replace when user say 'Yes'
                                if Warningask == 'Y' or Warningask == 'Yes' or Warningask == 'yes' or Warningask == 'y':
                                    definition = input('Definition: ')
                                    dictionary[term] = definition
                                    Warningcheck = False
                                # 2b.2: No store when user say 'No'
                                elif Warningask == 'N' or Warningask == 'No' or Warningask == 'no' or Warningask == 'n':
                                    Warningcheck = False
                                # 2b.3: Keep asking when use neither say 'Yes' or 'No
                                else:
                                    print('Please enter Y/N again.')

                        else:
                            # 2a.2: Request a definition
                            definition = input('Definition: ')
                            # 2a.3: Store it in a defined dictionary
                            dictionary [term] = definition
                    else:
                        print('\033[91m\033[1mERROR! Term not found.\033[0m')

                # 3. After completing to storage vocabulary and its definitions, save file and print vocabulary and its definition to a file
                elif addask == 'N' or addask == 'No' or addask == 'no' or addask == 'n':
                    # 3a: check  the longest characters in the storage dictionary
                    keyscount = 0
                    for i in dictionary.keys():
                        if len(i) > keyscount:
                            keyscount = len(i)
                    valuescount = len('Definition')
                    for i in dictionary.values():
                        if len(i) > valuescount:
                            valuescount = len(i)
                    # 3b: Request a filename from the user
                    filename = input('What would you like to save the file as? ')
                    VocFile = open(filename, 'w', encoding ='utf-8')
                    # 3c: follow the order to store the term(vocabularies/definitions to the file)

                    VocFile.write('{:{var1}} - {:<{var2}} : {}\n'.format('Term',
                                                                          'Definition', 'Example in the article', var1=keyscount,
                                                                          var2=valuescount))

                    for j in range(len(dictionary)):
                        VocFile.write('{:<{var1}} - {:<{var2}} : {}\n'.format(list(dictionary.keys())[j], list(dictionary.values())[j],
                                                                            list(example.values())[j], var1=keyscount, var2 = valuescount))


                    VocFile.close()
                    print('File saved!')
                    YesorNoCheck = False
                else:
                    print('\033[91m\033[1mPlease key in Y/N again.\033[0m')
            except:
                pass
        FileCheck = False
    except:
        print('Short story \033[91m\033[1mnot found\033[0m.')
        break
