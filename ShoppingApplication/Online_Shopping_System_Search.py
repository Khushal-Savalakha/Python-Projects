import difflib
import os

def get_closest_match(word, all_words):
    matches = difflib.get_close_matches(word, all_words, n=3, cutoff=0.6)
    return matches[0] if matches else word

def suggest_words(user_input, all_words):
    return [get_closest_match(word, all_words) for word in user_input]


def search_user_input(search_data, file_path):
    user_input = search_data.split()
    # product_file_names = ['Baby Care.txt', 'Beverages.txt', 'Cleaning Supplies.txt', 'Dairy.txt', 'Grains.txt', 'Washing_Machine.txt']
    product_file_names=os.listdir("D:\\Online_Shopping_System_data")
    searching_present = []

    for file_name in product_file_names:
        flag=0
        file=open(f"{file_path}{file_name}", 'r')
        for line in file:
            line_split=line.lower().split(' ')
            if(flag==0):
                if all(user_search_data in line_split for user_search_data in user_input):
                    searching_present.append(file_name)
                    break
                    flag=1
        file.close()
    return searching_present

def search():    
    # Example usage
    file_path = 'D:\\Online_Shopping_System_data\\'
    user_search = input("Enter your search: ")


    # Search user input in product files
    search_result = search_user_input(user_search.lower(), file_path)
    if search_result:
        print("Matching products found in the following categories:")
        for category in search_result:
            print(category)
        print(user_search)
        return user_search.lower().split(),search_result
    else:
        # Get suggested words
        all_words = set()
        for file_name in ['Baby Care.txt', 'Beverages.txt', 'Cleaning Supplies.txt', 'Dairy.txt', 'Grains.txt', 'Washing_Machine.txt']:
            with open(f"{file_path}{file_name}", 'r') as file:
                words = file.read().lower().split()
                all_words.update(words)
        
        suggestions = suggest_words(user_search.lower().split(), all_words)
        # Display suggestions
        if any(suggestions):
            search_result = search_user_input(' '.join(suggestions), file_path)
            if search_result:
                print("Did you mean these?")
                print(' '.join(suggestions))
                # print(search_result)
                # Fetching.fetch_data(suggestions,search_result)
                return suggestions,search_result
            else:
                print("No matching products found.")
        else:
            print("No suggestions found.")
    

