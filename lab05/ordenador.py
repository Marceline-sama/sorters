class Sorter:
    def __init__(self):
        pass

    def ordene_selection(self, valores) -> [int]:
        lst = [5, 2, 3, 4, 1]
        n = len(lst)
        for i in range (n - 1):
            min_index = i
            for j in range (i + 1, n):
                if lst[j] < lst[min_index]:
                    min_index = j
            lst[i], lst[min_index] = lst[min_index], lst[i]
            return lst
    
            

    def ordene_insertion(self, valores) -> [int]:
        lst = [5, 2, 3, 4, 1]
        n = len(lst)
        for i in range(1, n):
            current_element = lst[i]
            j = i - 1
            while j >= 0 and current_element < lst[j]:
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = current_element
            return lst    
        
