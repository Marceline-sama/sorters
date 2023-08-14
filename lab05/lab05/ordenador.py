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
        
    def ordene_insertion_recur(lst, n) -> [int]:
        lst = [5, 2, 3, 4, 1]
        n = len(lst)        
        if n is None:
            n = len(lst)
        if n <= 1:
            return lst                        
        ordene_insertion_recur(lst, n - 1)

        ultimo = lst[n-1]

        j = n - 2

        while ( j >= 0 and lst[j]>ultimo):
            lst[j+1] = lst[j]
            j = j -1
        lst[j + 1] = ultimo
        return lst 

    def ordene_selection_recur(lst, comeco_idx = 0):
        if comeco_idx >= len(lst) - 1:
            return lst 
        min_idx = comeco_idx
        for i in range(comeco_idx + 1, len(lst)):
            if lst[i] < lst[min_idx]:
                min_idx = i
        lst[comeco_idx], lst[min_idx] = lst[min_idx], lst[comeco_idx]
        return ordene_selection_recur(lst, comeco_idx + 1)              
