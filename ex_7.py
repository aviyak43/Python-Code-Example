from my_plot import plot

I = {"firstName": 0, "lastName": 1, "birthDate": None, "height": 5, "weight": 6, "BMI": 7}
DATE_I = {"day": 2, "month": 3, "year": 4}
# The file contains the data of persons: first name, last name, date of birth (day, month, year), height and weight
INPUT_FILE = "persons.txt"

'''
Aviya Keisar
311515415
ass07
'''

'''
Function Name: calcBmi
Input: weight, height
Output: - 
Function Operation: The function gets the weight and height of a person, and calculates its BMI, based on its weight
                    (in kg) and height (in meters).
'''
def calcBmi(weight, height):
    return weight / ((height/100) ** 2)


'''
# Function Name: sortByDate
# Input: persons
# Output: - 
# Function Operation: The function sorts the persons list by their date of birth.
'''
def sortByDate(persons):
    persons.sort(key=lambda d: int(d["birthDate"]["day"]))
    persons.sort(key=lambda d: int(d["birthDate"]["month"]))
    persons.sort(key=lambda d: int(d["birthDate"]["year"]))


'''
# Function Name: load
# Input: file_name, persons
# Output: - 
# Function Operation: The function reads an input from a given file, one line at a time, then inserts values from it 
                      to the keys of a dictionary, and finally adds it to the persons list.
'''
def load(file_name, persons):
    with open(file_name, "r") as input_file:
         #takes one line at a time
        for data in input_file:
            data = data.replace('\n', '')
            dataList = data.split(",")
            PERSON = {}
            PERSON["firstName"] = dataList[I["firstName"]]
            PERSON["lastName"] = dataList[I["lastName"]]
            PERSON["birthDate"] = {}
            PERSON["birthDate"]["day"] = dataList[DATE_I["day"]]
            PERSON["birthDate"]["month"] = dataList[DATE_I["month"]]
            PERSON["birthDate"]["year"] = dataList[DATE_I["year"]]
            PERSON["height"] = dataList[I["height"]]
            PERSON["weight"] = "{:.2f}".format(float(dataList[I["weight"]]))
            PERSON["BMI"] = calcBmi(float(dataList[I["weight"]]), float(dataList[I["height"]]))
            persons.append(PERSON)


'''
Function Name: save
Input: file_name, persons
Output: - 
Function Operation: The function writes all the fields of the persons list, to an output file.
'''
def save(file_name, persons):
    with open(file_name, "w") as output:
        for person_dict in persons:
            details = list(person_dict.values())
            date = list(person_dict["birthDate"].values())
            details = details[:2] + date + details[3:-1]
            output.write(",".join(details) + "\n")


def main():
    plot('Input:', INPUT_FILE)
    persons = []
    load(INPUT_FILE, persons)

    persons.sort(key=lambda d: d["firstName"])
    save("by_first_name.csv", persons)
    plot('By first name:', 'by_first_name.csv')

    persons.sort(key=lambda d: d["lastName"])
    save("by_last_name.csv", persons)
    plot('By last name:', 'by_last_name.csv')

    sortByDate(persons)
    save("by_date.csv", persons)
    plot('By date:', 'by_date.csv')

    persons.sort(key=lambda d: int(d["height"]))
    save("by_height.csv", persons)
    plot('By height:', 'by_height.csv')

    persons.sort(key=lambda d: float(d["weight"]))
    save("by_weight.csv", persons)
    plot('By weight:', 'by_weight.csv')

    persons.sort(key=lambda d: d["BMI"])
    save("by_BMI.csv", persons)
    plot('By bmi:', 'by_BMI.csv')


if __name__ == '__main__':
    main()
