global Patient_record
Patient_record = {
    'first_name': [],
    'last_name': [],
    'Age': [],
    'Weight_KG': [],
    'Height': [],
    'cholesterol': [],
    'Age_Category': [],
    'BMI': [],
    'cholesterol_level': []
}

def new_red():
    # Prompting the user for his/her details
    Firstname = input('Enter the patient\'s first name: ')
    Lastname = input('Enter the patient\'s last name: ')
    
    # Handling Year of birth input and calculating age
    while True:
        try:
            Year = int(input('Enter the patient\'s year of birth: '))
            break
        except ValueError:
            print("Please enter a valid year.")
    
    Age = 2024 - Year
    
    # Handling weight input
    while True:
        try:
            weight = float(input('Enter the Patient\'s weight (in Kg): '))
            break
        except ValueError:
            print("Please enter a valid weight in Kg.")
    
    # Handling height input
    while True:
        try:
            Height = float(input('Enter the Patient\'s Height (in meters): '))
            break
        except ValueError:
            print("Please enter a valid height in meters.")
    
    # Handling cholesterol input
    while True:
        try:
            cholesterol = int(input('Enter the Patient\'s cholesterol level (mg/dl): '))
            break
        except ValueError:
            print("Please enter a valid cholesterol level in mg/dl.")
    
    # Add user information to the dictionary
    Patient_record['first_name'].append(Firstname)
    Patient_record['last_name'].append(Lastname)
    Patient_record['Age'].append(Age)
    Patient_record['Weight_KG'].append(weight)
    Patient_record['Height'].append(Height)
    Patient_record['cholesterol'].append(cholesterol)
    print('Patient record has been added successfully')

    # Determine the Age Category
    if Age >= 18:
        Patient_record['Age_Category'].append('Adult')
    else:
        Patient_record['Age_Category'].append('Minor')
    
    # Calculate BMI
    BMI_value = weight / (Height * Height)
    if BMI_value < 18.5:
        Patient_record['BMI'].append('Underweight')
    elif BMI_value > 29.9:
        Patient_record['BMI'].append('Obese')
    elif 18.5 <= BMI_value <= 24.9:
        Patient_record['BMI'].append('Normal')
    else:
        Patient_record['BMI'].append('Overweight')
    
    # Determine cholesterol level
    if cholesterol < 200:
        Patient_record['cholesterol_level'].append('Normal')
    elif cholesterol > 240:
        Patient_record['cholesterol_level'].append('High')
    else:
        Patient_record['cholesterol_level'].append('Borderline')

    # Print the patient record
    current_index = len(Patient_record['cholesterol_level']) - 1
    print(f"-----Health Summary {Patient_record['first_name'][current_index]} {Patient_record['last_name'][current_index]} -----")
    print(f"Age Category: {Patient_record['Age_Category'][current_index]}")
    print(f"BMI Category: {Patient_record['BMI'][current_index]}")
    print(f"Cholesterol Category: {Patient_record['cholesterol_level'][current_index]}")

def search_red():
    if not Patient_record['last_name']:
        print('Patient Record is empty')
    else:
        search_name = input('Enter the patient name to search: ')
        if search_name in Patient_record['last_name']:
            for i in range(len(Patient_record['last_name'])):
                if search_name == Patient_record['last_name'][i]:
                    print(f"-----Health Summary {Patient_record['first_name'][i]} {Patient_record['last_name'][i]} -----")
                    print(f"Age Category: {Patient_record['Age_Category'][i]}")
                    print(f"BMI Category: {Patient_record['BMI'][i]}")
                    print(f"Cholesterol Category: {Patient_record['cholesterol_level'][i]}")
        else:
            print(f"{search_name} cannot be found")

def edit_red():
    if not Patient_record['last_name']:
        print('Patient Record is empty')
    else:
        print("Which record do you want to edit?")
        for i in range(len(Patient_record['first_name'])):
            print(f"{i + 1}. {Patient_record['first_name'][i]} {Patient_record['last_name'][i]}")
        
        edit_person = input('Enter the person\'s first name: ')
        if edit_person in Patient_record['first_name']:
            for i in range(len(Patient_record['first_name'])):
                if edit_person == Patient_record['first_name'][i]:
                    print(f"First Name: {Patient_record['first_name'][i]}")
                    print(f"Last Name: {Patient_record['last_name'][i]}")
                    print(f"Year of Birth: {2024 - Patient_record['Age'][i]}")
                    print(f"Weight: {Patient_record['Weight_KG'][i]} kg")
                    print(f"Height: {Patient_record['Height'][i]} meters")
                    print(f"Cholesterol: {Patient_record['cholesterol'][i]} mg/dl")
                    
                    edit_choice = input('Which field do you want to edit? ').lower()
                    if edit_choice == 'first name':
                        Patient_record['first_name'][i] = input('Enter the new first name: ')
                    elif edit_choice == 'last name':
                        Patient_record['last_name'][i] = input('Enter the new last name: ')
                    elif edit_choice == 'year of birth':
                        while True:
                            try:
                                new_year = int(input('Enter the new year of birth: '))
                                break
                            except ValueError:
                                print("Please enter a valid year.")
                        Patient_record['Age'][i] = 2024 - new_year
                    elif edit_choice == 'weight':
                        while True:
                            try:
                                Patient_record['Weight_KG'][i] = float(input('Enter the new weight (in Kg): '))
                                break
                            except ValueError:
                                print("Please enter a valid weight.")
                    elif edit_choice == 'height':
                        while True:
                            try:
                                Patient_record['Height'][i] = float(input('Enter the new height (in meters): '))
                                break
                            except ValueError:
                                print("Please enter a valid height.")
                    elif edit_choice == 'cholesterol':
                        while True:
                            try:
                                Patient_record['cholesterol'][i] = int(input('Enter the new cholesterol level (mg/dl): '))
                                break
                            except ValueError:
                                print("Please enter a valid cholesterol level.")
                    else:
                        print('Invalid choice')
        else:
            print(f"{edit_person} cannot be found")

# Display the menu
while True:
    print('Welcome to Patient Health Record')
    menu_nos = input('1) Enter New records\n2) Search Patient\n3) Edit or update Patient Detail\n4) Exit\nEnter your number: ')

    if menu_nos == '1':
        new_red()
        while True:
            con = input('Would you like to enter another patient\'s details (Yes or No): ')
            if con.lower() == 'no':
                break
            elif con.lower() == 'yes':
                new_red()
            else:
                print('Please enter Yes or No')

    elif menu_nos == '2':
        search_red()

    elif menu_nos == '3':
        edit_red()

    elif menu_nos == '4':
        break

    else:
        print('Invalid number. Please enter a valid number.')
