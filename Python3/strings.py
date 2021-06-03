string=string.replace('a','$')

# remove nth index from the string
def remove(string, n):  
      first = string[:n]   
      last = string[n+1:]  
      return first + last
      
