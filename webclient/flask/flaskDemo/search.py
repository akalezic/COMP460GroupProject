from collections import Counter
import os
import glob
import math

root = "../webcrawler/crawledPages/*.txt"

path = "flaskDemo/crawledPages/"


def read_file(file_name):
    # reading the review files
    text_file = open(file_name, 'r')
    page_text = text_file.read()
    text_file.close()

    # returning lower case of  as it will be easier to compare with search query
    return page_text.lower()


def calculate_score(word, word_list, files):
    count = word_list[word]
    tf = (count + 1) / (2 * len(word_list))
    calculate_idf(files, word)
    # returning probability with laplace smoothing
    #return tf * calculate_idf(files, word)
    return tf * calculate_idf(files, word)


def calculate_idf(all_files, word):
    document_containing_word = 0
    total_document = len(all_files)
    for item in all_files:
        page_text_all = read_file(path + item)
        page_text_all = Counter(page_text_all.split())
        if page_text_all[word] != 0:
            document_containing_word = document_containing_word + 1
    return math.log((total_document+1)/(document_containing_word+1))



def sort_results(dict):
    # python sorted function uses Timsort algorithm which is a hybrid sorting algorithm, derived from
    # merge sort and insertion sort.
    sorted_dict = {k: v for k, v in sorted(dict.items(), reverse=True, key=lambda item: item[1])}
    return sorted_dict


def display_results(dict):
    rank = 0
    print("Result for the search query sorted according to score \n")
    for items in dict:
        rank += 1
        print(str(rank) + ") " + items + '                      score: ' + str(dict[items]))

def do_search(search_string):
    root = "../webclient/flask/flaskDemo/crawledPages/*.txt"

    file_url_components = []
    file_dict = {}
    no_of_files = 0

    search_string = search_string.lower()
    query_words = search_string.split(" ")
    # scanning the crawledPages Directory for files and creating a list of text files
    #files = glob.glob(root)

    files = os.listdir(path)

    for file in files:
        
        score = 0
        page_text = read_file(path + file)
        page_words = Counter(page_text.split())
        print(page_words)
        # adding score for each word in search query
        for i in range(len(query_words)):
            individual_word_score = calculate_score(query_words[i], page_words, files)
            score = score + individual_word_score
            print(score)
        # converting the file name into url
        file_url = file[27:]
        file_url = file_url.replace('.txt', '')
        file_url_components = file_url.split("-")
        if len(file_url_components) > 1:
            file_url_final = file_url_components[0] + "/" + file_url_components[1]
        else:
            file_url_final = file_url_components[0]

        # adding file url and score to key-value pair
        file_dict[file_url_final] = score
        page_text = ''
        # sorting the results according to score (highest score first)
    print(file_dict)
    sorted_result = sort_results(file_dict)
    #display_results(sorted_result)
    results = list()

    for result_sorted in sorted_result:
        result = dict()
        print(result_sorted)
        result['title'] = result_sorted
        result['description'] = ""
        results.append(result)
    return results
        

if __name__ == '__main__':
    file_url_components = []
    file_dict = {}
    no_of_files = 0
    search_string = input('\nEnter a search term:-')
    search_string = search_string.lower()
    query_words = search_string.split(" ")
    # scanning the crawledPages Directory for files and creating a list of text files
    files = glob.glob(root)
    for file in files:
        score = 0
        page_text = read_file(file)
        page_words = Counter(page_text.split())

        # adding score for each word in search query
        for i in range(len(query_words)):
            individual_word_score = calculate_score(query_words[i], page_words, files)
            score = score + individual_word_score

        # converting the file name into url
        file_url = file[27:]
        file_url = file_url.replace('.txt', '')
        file_url_components = file_url.split("-")
        if len(file_url_components) > 1:
            file_url_final = file_url_components[0] + "/" + file_url_components[1]
        else:
            file_url_final = file_url_components[0]

        # adding file url and score to key-value pair
        file_dict[file_url_final] = score
        page_text = ''
        # sorting the results according to score (highest score first)
    sorted_result = sort_results(file_dict)
    display_results(sorted_result)

