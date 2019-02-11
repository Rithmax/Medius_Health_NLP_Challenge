# Sarith Fernando
# 11/02/2019
# Medius NLP Challenge


import pandas as pd


#  Creates the first candidate set using the dataset
def gen_C1(dataset):
    post_dict = {}
    total_set = []
    for data in dataset:
        for post in data:
            if post not in post_dict:
               post_dict[post] = 1
            else:
                 post_dict[post] = post_dict[post] + 1
    for key in post_dict:
        temp = []
        temp.append(key)
        total_set.append(temp)
        total_set.append(post_dict[key])

    return total_set


# Creates the frequent item sets. Format: [['item_set'],no. of occurrences]
def gen_freq_item_set(candidate_list, no_of_posts, min_sup_percent, dataset, freq_array):
    freq_items = []
    for i in range(len(candidate_list)):
        if i%2 != 0:
            # Finding supports which is higer than minimum support
            support = (candidate_list[i] * 1.0 / no_of_posts) * 100
            if support >= min_sup_percent:
                freq_items.append(candidate_list[i-1])
                freq_items.append(candidate_list[i])

    # Copy array, np.copy
    for k in freq_items:
        freq_array.append(k)

    if len(freq_items) == 2 or len(freq_items) == 0:
        return freq_array

    else:
        gen_candidate_sets(dataset, freq_items, no_of_posts, min_sup_percent)
        return freq_array


# Creates the candidate sets
def gen_candidate_sets(dataset,  freq_items, no_of_posts, min_sup_percent):
    elems = []
    combinations = []
    candidate_set = []
    for i in range(len(freq_items)):
        if i%2 == 0:
            elems.append(freq_items[i])
    for item in elems:
        temp_combi = []
        k = elems.index(item)
        for i in range(k + 1, len(elems)):
            for j in item:
                if j not in temp_combi:
                    temp_combi.append(j)
            for m in elems[i]:
                if m not in temp_combi:
                    temp_combi.append(m)
            combinations.append(temp_combi)
            temp_combi = []
    sorted_combi = []
    unique_combi = []
    for i in combinations:
        sorted_combi.append(sorted(i))
    for i in sorted_combi:
        if i not in unique_combi:
            unique_combi.append(i)
    combinations = unique_combi
    for item in combinations:
        cnt = 0
        for post in dataset:
            if set(item).issubset(set(post)):
                cnt = cnt + 1
        if cnt != 0:
            candidate_set.append(item)
            candidate_set.append(cnt)
    gen_freq_item_set(candidate_set, no_of_posts, min_sup_percent, dataset, freq_array)


def read_data(filename):
    dataset = []
    #  Reading data file line by line
    with open(filename, 'r') as fp:
        lines = fp.readlines()

    for line in lines:
        line = line.rstrip()
        dataset.append(line.split(","))

    return dataset

def load_csv(fname):
    """Load data from *.cvs
    """
    data = []
    with open(fname, 'r') as f:
        for line in f.readlines():
            items = line.strip('\n').split(',')
            data.append(items)
    return data


def load_data_from_cvs_file(fname):
    """Load data from *.cvs
    """
    dat = pd.read_excel(fname, sheet_name=None)
    dat=dat.columns

    return dat


if __name__ == '__main__':

    # Defining the input file name
    filename = "food.txt"

    # Getting the frequency set which is higher than minimum support percentage.
    # ex: Let total posts=40, and min_sup_percent = 50. Then gen_freq_item_set outputs frequency sets with
    # number of occurrences where occurrences are greater than 20.

    min_sup_percent = 50
    freq_array = []
    dataset = read_data(filename)
    print(dataset)

    dataset1 = load_data_from_cvs_file('machine_learning_challenge.xlsx')

    print(dataset1)

    no_of_posts = len(dataset)

    first_set = gen_C1(dataset)
    print(first_set)

    freq_item_set = gen_freq_item_set(first_set, no_of_posts, min_sup_percent, dataset, freq_array)
    print(freq_item_set)

