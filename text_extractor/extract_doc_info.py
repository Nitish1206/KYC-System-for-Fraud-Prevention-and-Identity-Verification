import easyocr
from difflib import SequenceMatcher

# def get_card_details(path_):
reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
results = reader.readtext('raw_images/nitish_pancard.jpg')

    # return result
print(results)
# get_card_details

# Utility function to compute similarity
def similar(str1, str2):
    return SequenceMatcher(None, str1, str2).ratio()

# name="Jha Madhushankar"
# DOB="28/10/1968"

for result in results:
    print(result[1])
#     if "dob" in result[1].lower():
#         ddob=result[1].split(" ")[-1].strip() 
#         # if ddob.lower()=="dob":

#         print(ddob)

#         ss=similar(result[1],DOB)
#         print(ss)
#         print(result[1])