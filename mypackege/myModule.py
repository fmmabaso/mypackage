def top_n (item, n):
    """Return the top n items in an array, in desc order'

    Args:
        items (array): list or array-like object containing numerical values.
        n (int): number of top items to return.

    Returns:
            array: top n items, in descending order.

    Examples:
        >>> top_n([8, 3, 2, 7, 4], 3)
        [8, 7, 3]
    """

for i in range(n): #keep sorting until we have the top n items
    for j in range(len(item)-1-1):

        if items[j] > items[j=1]: # if this item is bigger than next the item..
            items[j], items[j+1] = items[j+1], items[j] # swap the two!

# Get two last items
top_n = items[-n:]

#Return in descending order
return top_n[::-1]
      
