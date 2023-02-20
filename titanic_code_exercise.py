
"""
Created on Sun Nov  7 21:52:29 2021

@author: letizia
"""
# This program takes an unprocessed file with passenger information from the titanic and processes, analyses & visualizes it.

# data preprocessing
def preprocess(records):
    
    my_file = open(records, "r")
    
    csv_list = []
            
    for line in my_file.readlines():
        if len(line) <= 1:
            continue
                    
        else:
            new_line = line.strip("\n")
            new_line = new_line.split(",")
            csv_list.append(tuple(new_line))
                    
            
    # seperate and save header from my csv_list        
    header = csv_list[0]
    del csv_list[0]
    
    
# continue with csv_list: clean data 
    
    # clean attribute: survived
    
    pos_val_survived = ["Yes", "yes", "Alive", "t", "True", "true", "T"]
    invalid_values = ["", "unknown", "undefined"]
    
    for line in csv_list:
        list_of_tuple = list(line)
        index_line = csv_list.index(line)
        if list_of_tuple[0] in invalid_values:
            
            del csv_list[index_line]
        
        elif list_of_tuple[0] in pos_val_survived:
            list_of_tuple[0] = True
        
        else:
            list_of_tuple[0] = False

        csv_list[index_line] = tuple(list_of_tuple) 
       
        
    # clean attribute: Pclass    
    for line in csv_list:
        list_of_tuple = list(line)
        index_line = csv_list.index(line)
        
        
        if list_of_tuple[1] == "1" or list_of_tuple[1] == "2" or list_of_tuple[1] == "3":
            list_of_tuple[1] = int(list_of_tuple[1])
        
            csv_list[index_line] = tuple(list_of_tuple) 

        else: 
            del csv_list[index_line] 
        
        
    # clean attribute: name
        # no action required
        
        
    # clean attribute: gender
    pos_val_female = ["female", "f", "Female", "F"]
    for line in csv_list:
        list_of_tuple = list(line)
        index_line = csv_list.index(line)
        
        if list_of_tuple[3] == "undefined":
            del csv_list[index_line]
            
        elif list_of_tuple[3] in pos_val_female:
            list_of_tuple[3] = "female"
            
        else:
            list_of_tuple[3] = "male"
        
        csv_list[index_line] = tuple(list_of_tuple) 
        
        
    # clean attribute: age
    for line in csv_list:
        list_of_tuple = list(line)
        index_line = csv_list.index(line)
        
        try: 
            list_of_tuple[4] = float(list_of_tuple[4])
            csv_list[index_line] = tuple(list_of_tuple) 
            
            csv_list[index_line] = tuple(list_of_tuple)

        except ValueError: 
            del csv_list[index_line]
            
    
    # clean attribute: fare
    for line in csv_list:
        list_of_tuple = list(line)
        index_line = csv_list.index(line)
        
        try: 
            list_of_tuple[5] = float(list_of_tuple[5]) 

        except ValueError:
            list_of_tuple[5] = 25.0
        
        
        if list_of_tuple[5] <= 0:
            list_of_tuple[5] = 25.0
    
    
        csv_list[index_line] = tuple(list_of_tuple) 
    

    # final file with header adn right format
    preprocessed_file = (header, csv_list)
    
    return preprocessed_file


# Data analysis
def gender_class_rates(dataset):
    male_1 = 0
    male_2 = 0
    male_3 = 0
    
    female_1 = 0
    female_2 = 0
    female_3 = 0
    
    for n in dataset[1]:

        if n[3] == "male" and n[1] == 1:
            male_1 += 1
        
        elif n[3] == "male" and n[1] == 2:
            male_2 += 1
        
        elif n[3] == "male" and n[1] == 3:
            male_3 += 1

        elif n[3] == "female" and n[1] == 1:
            female_1 += 1
        
        elif n[3] == "female" and n[1] == 2:
            female_2 += 1

        elif n[3] == "female" and n[1] == 3:
            female_3 += 1

    num_of_passengers = len(dataset[1])

    perc_male_1 = round(100*(male_1 / num_of_passengers), 1)         
    perc_male_2 = round(100*(male_2 / num_of_passengers), 1) 
    perc_male_3 = round(100*(male_3 / num_of_passengers), 1) 
    
    perc_female_1 = round(100*(female_1 / num_of_passengers), 1) 
    perc_female_2 = round(100*(female_2 / num_of_passengers), 1) 
    perc_female_3 = round(100*(female_3 / num_of_passengers), 1)

    if perc_female_1 == 0.0:
        perc_female_1 = None

    if perc_female_2 == 0.0:
        perc_female_2 = None
    
    if perc_female_3 == 0.0:
        perc_female_3 = None

    if perc_male_1 == 0.0:
        perc_male_1 = None

    if perc_male_2 == 0.0:
        perc_male_2 = None

    if perc_male_3 == 0.0:
        perc_male_3 = None
    
    my_tuple = ((perc_male_1, perc_male_2, perc_male_3), (perc_female_1, perc_female_2, perc_female_3))
    
    return my_tuple

#visulaization
def visualize(records):
    num_pas_1 = 0
    num_pas_1_alive = 0
    
    num_pas_2 = 0
    num_pas_2_alive = 0
    
    num_pas_3 = 0
    num_pas_3_alive = 0
    
    for n in records[1]:
        if n[1] == 1:
            num_pas_1 += 1
            
            if n[0] == True:
                num_pas_1_alive += 1
        
        elif n[1] == 2:
            num_pas_2 += 1
            
            if n[0] == True:
                num_pas_2_alive += 1
                
        elif n[1] == 3:
            num_pas_3 += 1
            
            if n[0] == True:
                num_pas_3_alive += 1
     
        
    num_of_passengers = len(records[1])
    
    
    perc_total_1 = round(100*(num_pas_1 / num_of_passengers), 1)
    vis_total_1 = round(perc_total_1/5)*"*" + (20-round(perc_total_1/5))*" "
    
    perc_alive_1 = round(100*(num_pas_1_alive / num_of_passengers), 1)
    vis_alive_1 = round(perc_alive_1/5)*"*" + (20-round(perc_alive_1/5))*" "
    
    
    perc_total_2 = round(100*(num_pas_2 / num_of_passengers), 1)
    vis_total_2 = round(perc_total_2/5)*"*" + (20-round(perc_total_2/5))*" "
    
    perc_alive_2 = round(100*(num_pas_2_alive / num_of_passengers), 1)
    vis_alive_2 = round(perc_alive_2/5)*"*" + (20-round(perc_alive_2/5))*" "
    
    
    perc_total_3 = round(100*(num_pas_3 / num_of_passengers), 1)
    vis_total_3 = round(perc_total_3/5)*"*" + (20-round(perc_total_3/5))*" "
    
    perc_alive_3 = round(100*(num_pas_3_alive / num_of_passengers), 1)
    vis_alive_3 = round(perc_alive_3/5)*"*" + (20-round(perc_alive_3/5))*" "
    
    
    
    my_string = f"== 1st Class ==\nTotal |{vis_total_1}| {perc_total_1}%\nAlive |{vis_alive_1}| {perc_alive_1}%\n== 2nd Class ==\nTotal |{vis_total_2}| {perc_total_2}%\nAlive |{vis_alive_2}| {perc_alive_2}%\n== 3rd Class ==\nTotal |{vis_total_3}| {perc_total_3}%\nAlive |{vis_alive_3}| {perc_alive_3}%"


    return my_string


preprocessed_file = preprocess("/Users/letizia/Desktop/titanic/cf1f927b-80ec-31c3-8d00-c55aefc59278 3/public/titanic.csv")
#print(preprocessed_file)

analysed_file = gender_class_rates(preprocessed_file)
print(analysed_file)

visualization = visualize(preprocessed_file)
print(visualization)

