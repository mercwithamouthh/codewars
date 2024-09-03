def two_sort(array):
    # Step 1: Sort the array alphabetically
    sorted_array = sorted(array)

    # Step 2: Get the first string in the sorted array
    first_string = sorted_array[0]

    # Step 3: Insert "***" between each letter of the string
    result = "***".join(first_string)

    return result
#OR MUCH SIMPLER WAY
def two_sortt(array): #with two tts so it wouldnt mess up the original function
    return '***'.join(sorted(array)[0])