# PART: A
## Programming Challenge
The attached dataset contains two columns. First column is the topic of a post. Second column is the
text from the post. Using the given dataset, please write a native implementation for an algorithm to
discover the frequent text item-sets from the second column. Do not use any existing function or
library to achieve this objective (develop the algorithm code for frequent itemset mining and apply on
the dataset - do not use any brute force technique).

Hint: You can implement one of the Apriori, Eclat, or FP-growth techniques to achieve this (or a better
method)

## Solution
Implementation of Apriori algorithm to identify frequent text item-sets with minimum support. 
Algorithm only outputs the sets which is higher than minimum support and buit as a percentage.


##### Data preprocessing
Assuming that each raw represent a independent post, posts are splitted into the words.
Next find the unique words in each post and running the Apriori algorithm.
