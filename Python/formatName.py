def format_name(f_name, l_name):
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
#title() is a function that capitalizes the first letter of a string.

  return(f"{formatted_f_name} {formatted_l_name}")
formatted_string = format_name("pratyush", "SHarMa")
print(formatted_string)