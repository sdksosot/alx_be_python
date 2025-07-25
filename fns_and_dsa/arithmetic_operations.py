def perform_operation(num1:float , num2:float , operation: str ):
  if operation == '+':
     return num1 + num2
  elif operation == '-':
     return num1 - num2
  elif operation == '/':
     if num2 != 0:
        return num1 / num2
     else:
        return 'cannot devied by zero'
  elif operation == '*':
     return num1 * num2
  else:
     return 'invalid value'
  
