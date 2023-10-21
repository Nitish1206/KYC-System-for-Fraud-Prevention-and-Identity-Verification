from dateutil.parser import parse
from difflib import SequenceMatcher

def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try: 
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False

# Utility function to compute similarity
def similar(str1, str2):
    return SequenceMatcher(None, str1, str2).ratio()

def match_data(extracted_data,input_data):
    res={}
    for key in input_data.keys():
        current_data=input_data[key]
        current_data=current_data.lower().replace(" ","").replace("/","")
        
        print("+++",current_data)
        for result in extracted_data:

            ex_text=result[1].lower().replace(" ","").replace("/","")
            print("---",ex_text)


            # if ex_text
            if "dob" in ex_text:

                dob_data=ex_text.split("b")[-1].strip().replace(":","")
                current_data_=current_data.replace("/","")
                ss=similar(dob_data,current_data_)
                print("$$$$$$",dob_data)
                print(ss)
                if ss > 0.8:
                    res[key]=ss
                    break

            # if result[1].replace(" ", "").isnumeric():
            #     if len(result[1].replace(" ", "")) == 12:
            #         a_num=result[1].replace(" ", "")
            #         key=card
            #         current_data=input_data[key]
            #         current_data=current_data.replace(" ", "")
            #         ss=similar(a_num,current_data)
            #         if ss == 1:
            #             res[key]=ss

            else:
                if is_date(ex_text):
                    key_="dob"
                    current_data_=input_data[key_].replace("/","")
                    date_=ex_text.replace("/","")
                    ss=similar(date_,current_data_)
                    print(ss)
                    if ss > 0.8:
                        res[key_]=ss
                
                        break
        

                else:
                    print("str check")
                    print("ext data",ex_text,"curr data",current_data)
                    ss=similar(ex_text,current_data)
                    print(key)
                    print(ss)
                    if ss > 0.8:
                        res[key]=ss
                        break
            
    
    return res