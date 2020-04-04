def is_palindrome(input)
  
  if input <= 1:
    return True
  else:
    first_l = input[0]
    last_l = input[-1]
    sub_string = input[1:-1]
    
    return (first_l == last_l) and (is_palindrome(sub_string)
                                    
                                   
if __name__ == __main__:
  print(is_palindrome('madam'))
  print(is_palindrome('tattarrattat'))
  print(is_palindrome('mongoose'))
                                   
