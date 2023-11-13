def arithmetic_arranger(operations, solve=False):
   if len(operations) > 5:
      return "Error: Too many problems."
   
   fl, sl, dashes = "", "", ""
   results = ""
   for ix, op in enumerate(operations):
      op1, operator, op2 = op.split()

      if operator not in ["+", "-"]:
         return "Error: Operator must be '+' or '-'."
      
      if not op1.isnumeric() or not op2.isnumeric():
         return "Error: Numbers must only contain digits."
      
      if len(op1) > 4 or len(op2) > 4:
         return "Error: Numbers cannot be more than four digits."

      if len(op1) > len(op2):
         fl = fl + " "*2 + op1
         sl = sl + operator + " "*(len(op1)-len(op2)+1) + op2
      else:
         fl = fl + " "*(len(op2)-len(op1)+2) + op1
         sl = sl + f"{operator} {op2}"
      dash = "-"*(max(len(op1), len(op2)) + 2)
      dashes = dashes + dash

      if ix != len(operations) - 1:
         fl, sl, dashes = fl+" "*4, sl+" "*4, dashes+" "*4
      
      if not solve:
         continue

      result = ""
      if operator == "+":
         result = str(int(op1) + int(op2))
      elif operator == "-":
         result = str(int(op1) - int(op2))
      
      results = results + " "*(len(dash)-len(result)) + result
      results = results + " "*4 if ix != len(operations) - 1 else results
   final_string = f"{fl}\n{sl}\n{dashes}"
   if solve:
      final_string = f"{final_string}\n{results}"
   return final_string