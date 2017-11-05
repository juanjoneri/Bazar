import sys

class SearchItem(object):

    def __init__(self, host_ID, listing_ID, score, city):
        self.host_ID = int(host_ID)
        self.listing_ID = int(listing_ID)
        self.score = float(score)
        self.city = city

    def __str__(self):
        # for printing results
        return '{},{},{},{}'.format(self.host_ID, self.listing_ID, self.score, self.city)

    def __eq__(self, other):
        # for checking if in page
        return self.host_ID == other.host_ID

def uniques(list1, list2):
    # returns the index of the next element from list2 that is not in list1
    for i in range(len(list2)):
        if list2[i] not in list1:
            yield i

def paginate(num, results):
    items = [SearchItem(*result.split(',')) for result in results] # assuming input has correct format

    leftovers = [] # used as a queue
    pages = [[] for _ in range(len(results) // num + 1)] # 2D list representing pages

    while any(items):
        current_item = leftovers.pop(0) if any(leftovers) else items.pop(0) # try to follow score order
        current_page = next(page for page in pages if len(page) < num)

        if current_item not in current_page:
            current_page.append(current_item)
        else:
            try:
                next_unique_index = next(uniques(current_page, items))
                current_page.append(items.pop(next_unique_index))
            except StopIteration:
                if any(leftovers):
                    current_page.append(leftovers.pop(0))
                else:
                    current_page.append(current_item)
                    continue
            leftovers.append(current_item)

    paginated_results = []
    separator = ''
    for page in pages:
        paginated_results.extend(map(str, page))
        paginated_results.append(separator)
    paginated_results.pop() # there is an extra separator

    return paginated_results

if __name__ == '__main__':
    results = [
    "1,28,300.6,San Francisco",
    "4,5,209.1,San Francisco",
    "20,7,203.4,Oakland",
    "6,8,202.9,San Francisco",
    "6,10,199.8,San Francisco",
    "1,16,190.5,San Francisco",
    "6,29,185.3,San Francisco",
    "7,20,180.0,Oakland",
    "6,21,162.2,San Francisco",
    "2,18,161.7,San Jose",
    "2,30,149.8,San Jose",
    "3,76,146.7,San Francisco",
    "2,14,141.8,San Jose"
    ]
    num = 5
    print(paginate(num, results))