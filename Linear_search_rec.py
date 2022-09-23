# function for finding position of element using recursive approach 

def linear_search(arr, length, ele):
  
    if (length == 0):
        return -1
    elif (length == 1 and arr[0] != ele):
        return -1
    elif (arr[length] == ele):
        return length
    else:
        return(linear_search(arr, length-1, ele))

      
# driver code 

if __name__ == "__main__":
  
    arr = [ 20, 15, 5, 30, 50, 45]
    ele = 50
    length = len(arr)-1
    
# calling the function and assigning a variable name to it 

    output = linear_search(arr, length, ele)
    
    if (output == -1):
        print(f'{ele} is not included in array.')
    else:
        print(f'{ele} is on {output} position.')
    
