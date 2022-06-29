from ast import keyword
import json
import os




# def names_of_registered_students(input_json_path, course_name):
#     """
#     This function returns a list of the names of the students who registered for
#     the course with the name "course_name".

#     :param input_json_path: Path of the students database json file.
#     :param course_name: The name of the course.
#     :return: List of the names of the students.
#     """
#     pass


# def enrollment_numbers(input_json_path, output_file_path):
#     """
#     This function writes all the course names and the number of enrolled
#     student in ascending order to the output file in the given path.

#     :param input_json_path: Path of the students database json file.
#     :param output_file_path: Path of the output text file.
#     """
#     pass



def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    pass


def names_of_registered_students(input_json_path, course_name):
    with open(input_json_path, 'r') as jsonFile:
        inputFile = json.load(jsonFile)
        jsonFile.close()
    #x= type(inputFile)    
    listName = []
    for studentId , details in inputFile.items():
        for course in details['registered_courses']:
            if course == course_name:
                listName.append(details['student_name'])
                break
    return listName            


def enrollment_numbers(input_json_path, output_file_path):
    with open(input_json_path, 'r') as jsonFile:
        inputFile = json.load(jsonFile)
        jsonFile.close()
    listOfCourses = []
    for studentId , details in inputFile.items():
        for course in details['registered_courses']:
            listOfCourses.append(course)
    listOfCourses.sort()
    outputFile= open(output_file_path, 'w')  
    length = len(listOfCourses)
    i = 0
    while i <length:
        counterOfTypecourse = 1
        while  i<(length-1) and listOfCourses[i]==listOfCourses[i+1]:
            counterOfTypecourse += 1
            i += 1 
        s = '"'+ listOfCourses[i] + '"' + " " + str(counterOfTypecourse) + "\n"
        outputFile.write(s)
        i += 1
    outputFile.close()
    return

    

def courses_for_lecturers(json_directory_path, output_json_path):
    lecturerAndCourses ={}
    for file in os.listdir(json_directory_path):
        filePath = os.path.join(json_directory_path,file)
        fileFormat = os.path.splitext(filePath)
        if os.path.isfile(filePath) and fileFormat[1]=='.json':
            with open(filePath,'r') as dataFile:
                loadedDict=json.load(dataFile)  
                for courseAndLecturersDict in loadedDict.values():
                    for lecturer in courseAndLecturersDict["lecturers"]:
                        if lecturer in lecturerAndCourses and lecturerAndCourses[lecturer].count(courseAndLecturersDict["course_name"])==0:
                            lecturerAndCourses[lecturer].append(courseAndLecturersDict["course_name"])   
                        elif lecturer in lecturerAndCourses and lecturerAndCourses[lecturer].count(courseAndLecturersDict["course_name"])!=0:
                            continue
                        else  :
                            lecturerAndCourses[lecturer]=[courseAndLecturersDict["course_name"]] 
    with open(output_json_path,'w') as f:
        json.dump(lecturerAndCourses,f, indent=4)
    




