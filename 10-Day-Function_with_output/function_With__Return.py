def format_name(f_name,l_name):
  if(f_name == " " or l_name == " "):
    return "you didn't provide valid inputs"
  formatted_fname = f_name.title()
  formatted_lname = l_name.title()
  return f"Result: {formatted_fname} {formatted_lname}"

print(format_name(input("What is your frist name?"), input("What is your last name? ")))
