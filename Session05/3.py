# Write a function that extracts the even items in a given integer list, 
# named get_even_list, takes 1 parameter: l, where l is the given integer list ([1, 4, 5, -1, 10] for example),
# returns a new list contains only even numbers ([4, 10] if the given list is [1,4,5,-1,10])
def get_even_list(l):
    ls=[]
    for i in l:
        if i % 2==0:
            ls.append(i)
    return ls
print(get_even_list([1,4,5,-1,10]))