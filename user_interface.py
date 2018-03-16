# Filename: user_interface.py
# Description: Allows the user to input symptoms; outputs possible diseases.

import sys
sys.dont_write_bytecode = True

import time

def process_disease_file(filename):
    d = {}
    with open(filename) as f:
        content= f.readlines()
    content = [x.strip() for x in content]
   
    # empty list containing two empty lists
    lol = []
    lol.append([])
    lol.append([])
 
    counter = 0
    curr_key = ''

    for line in content:
        if counter == 0:
            curr_key = line
            d[line] = lol
            counter += 1
        elif counter == 1:
            # do nothing to d, because line says symptom
            # add one to counter, should be 2 now
            counter +=1
        elif line == ';':
            # do nothing to d, because next line begins treatments
            # add one to counter, should be 3 now
            counter += 1
        elif line == ':':
            # end of treatments, the next one will be a disease
            counter = 0
        elif counter == 2:
            # we are adding symptoms
            d[curr_key][0].append(line)
        elif counter == 3:
            # we are adding treatments
            d[curr_key][1].append(line)
        else:
            print "Error, should not be able to get here"
            assert(False)
            
    return d

def get_diseases(user_input, disease_ontology):
    l = []
    return l

def all_symptoms(disease_ontology):
    string = ""

    diseases = disease_ontology.keys()

    counter = 0

    # calculate limit
    # how i know what the last element of the list is
    # i don't want a comma after that one
    limit = 0
    for disease in diseases:
        for symptom in disease_ontology[disease][0]:
            limit += 1

    for disease in diseases:
        for symptom in disease_ontology[disease][0]:
            string += symptom
            counter += 1
            if counter != limit:
                string += ', '
                
    return string


def main():
    print "Calculating..."
    start = time.time()

    filename = "polished_diseases.txt"

    disease_ontology = process_disease_file(filename)
    print disease_ontology

    print all_symptoms(disease_ontology)
    assert(False)

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
