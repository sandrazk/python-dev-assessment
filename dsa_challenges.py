def filter_and_Sort_evens(numbers):
    evens=[]
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    evens.sort()
    return evens



list=[3, 1, 4, 7, 1, 5, 9, 2, 6, 8]

result=filter_and_Sort_evens(list)
print(result)

def count_character_frequency(text):
    frequency={}

    text_lowercase=text.lower()

    for char in text_lowercase:
        if char in frequency:
            frequency[char] +=1
        else:
            frequency[char]=1
        return frequency
    
click=("This my task for Basic Data Structures & Algorithms")

result=count_character_frequency(click)
print(result)