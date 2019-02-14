#define functions and udfs here 
def convert_lpad_number(value, NumOfDigits=2):
  if value is not None :
    return str(value).zfill(NumOfDigits)
  else:
    return ""
