# Filename: user_interface.py
# Description: Allows the user to input symptoms; outputs possible diseases.

import sys
sys.dont_write_bytecode = True

import time

def process_disease_file(filename):
    d = {}
    return d

def get_diseases(user_input, disease_ontology):
    l = []
    return l

def all_symptoms(disease_ontology):
    string = ""

    for symptom in disease_ontology:
        string.append(symptom)
        string.append(", ")
        # TODO: how do i know what the last element of the list is?
        #       i don't want a comma after that one
    
    return string


def main():
    print "Calculating..."
    start = time.time()

    filename = "diseases.txt"

    disease_ontology = process_disease_file(filename)

    print all_symptoms(disease_ontology)

    prompt = "Input a list of symptoms separated by a comma (type 'e' to exit): "
    
    #TODO: get user_input

    while(user_input != 'e'):
        symptom_list = get_symptoms(user_input)
        disease_list = get_diseases(user_input)
        print "Here is a list of possible diseases:"
        for disease in disease_list:
            print disease
        # TODO: get user_input again

    end = time.time()
    sumtime = end - start
    print "DONE!"
    print sumtime
#    print t
#    fo = open("results.txt", "wb")
#    fo.write("%d\n%.8f\n" % (t, sumtime))
#    fo.close()


if __name__ == "__main__":
    main()
