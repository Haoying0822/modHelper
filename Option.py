option = [ "Alice Lee Centre for Nursing Studies",
"Business School", "College of Design and Engineering",
"College of Humanities and Sciences - FASS",
"College of Humanities and Sciences - FoS",
"Faculty of Dentistry", "Faculty of Law", "School of Computing",
"Yong Loo Lin School of Medicine", "Yong Siew Toh Conservatory of Music",
"MA2001", "MA2002", "PC1101"]

def create_dict(str_list):
    dict = {}
    for str in str_list:
        dict[str] = str_list.index(str)
    return dict

option_dict = create_dict(option)

#print(option_dict)

"""
After getting a full module list, can use the command above to directly create a dictionary.
Copy and paste the result back to this file. 
"""