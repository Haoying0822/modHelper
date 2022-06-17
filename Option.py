option = [ "Alice Lee Centre for Nursing Studies",
"Business School", "College of Design and Engineering",
"College of Humanities and Sciences - FASS",
"College of Humanities and Sciences - FoS",
"Faculty of Dentistry", "Faculty of Law", "School of Computing",
"Yong Loo Lin School of Medicine", "Yong Siew Toh Conservatory of Music",
"MA2001", "MA2002", "PC1101", "PC1201", "PC1421", 
"PC2020", "PC2031", "PC2032", "PC2130", "PC2135", "PC2174A", "PC2193", 
"PC2267", "PC2411", "PC2412", "PC2421", "PC2422", "PC2423",
"PC3130", "PC3193", "PC3231", "PC3232", "PC3233", "PC3235", "PC3235B", "PC3236",
"PC3238", "PC3242", "PC3243", "PC3246", "PC3247", "PC3251", "PC3261", "PC3267",
"PC3274", "PC3274A", "PC3288", "PC3294", "PC3295", "PC2411", "PC3412", "PC3413",
"PC3421", "PC3422", "PC3441", "PC3442",
"PC4228", "PC4230", "PC4236", "PC4240", "PC4241", "PC4242", "PC4243", "PC4245",
"PC4246", "PC4248", "PC4249", "PC4253", "PC4259", "PC4262", "PC4264", "PC4267",
"PC4268", "PC4274", "PC4274A", "PC4288", "PC4441",
"PC5101", "PC5102", "PC5198", "PC5201", "PC5202", "PC5203", "PC5204", "PC5204B", "PC5205",
"PC5206", "PC5207", "PC5209", "PC5210", "PC5212", "PC5213", "PC5214", "PC5215", "PC5228",
"PC5239B", "PC5247", "PC5274", "PC5251", "PC5252", "PC5253"]


def create_dict(str_list):
    dict = {}
    n = 0
    for str in str_list:
        dict[str] = n
        n += 1
    return dict

option_dict = create_dict(option)

#print(option_dict)

"""
After getting a full module list, can use the command above to directly create a dictionary.
Copy and paste the result back to this file. 
"""
