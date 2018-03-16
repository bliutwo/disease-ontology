# Filename: interface.py
# Description: Allows the user to input symptoms; outputs possible diseases.
# TODO: ask questions to narrow down disease

import sys
sys.dont_write_bytecode = True

import time

def process_disease_file(filename):
    d = {}
    with open(filename) as f:
        content= f.readlines()
    content = [x.strip() for x in content]

    # empty list containing two empty lists
    # lol = []
    # lol.append([])
    # lol.append([])
 
    counter = 0
    curr_key = ''

    for line in content:
        if counter == 0:
            curr_key = line
            # original: d[curr_key] = lol
            # can't because pointer to lol
            d[curr_key] = []
            d[curr_key].append([])
            d[curr_key].append([])
            counter += 1
        elif counter == 1:
            # do nothing to d, because line says symptom
            # add one to counter, should be 2 now
            counter +=1
        elif line == 'treatment':
            # do nothing to d, because next line begins treatments
            # add one to counter, should be 3 now
            counter += 1
        elif line == ':':
            # end of treatments, the next one will be a disease
            counter = 0
            curr_key = ''
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

# # TODO? check if two strings match, but not necessarily exact match
# or if a is contained in b
def inexact_match(a, b):
    if a in b:
        return True

# symptom, list of symptoms
# check if symptom in list of symptoms
def match_found(s, l):
    for symptom in l:
        if inexact_match(s, symptom):
            return True
    return False

def get_diseases(user_input, disease_ontology):
    l = []

    symptoms = user_input.split(',')

    for symptom in symptoms:
        for disease in disease_ontology:
            if match_found(symptom, disease_ontology[disease][0]):
                l.append(disease)

    return l

def nice_format(do):
    for disease in do:
        print disease
        print
        for s in do[disease][0]:
            print s
        print
        for t in do[disease][1]:
            print t
        print

def main():
    print "Calculating..."
    start = time.time()

    filename = "polished_diseases.txt"

    disease_ontology = process_disease_file(filename)
    # print disease_ontology

    nice_format(disease_ontology)
    assert(False)

    # TODO: Implement ask questions to narrow down disease

    print "List of symptoms in ontology:"
    print all_symptoms(disease_ontology)
    print

    prompt = "Input a list of symptoms separated by a comma (type 'e' to exit): "
    
    user_input = raw_input(prompt)

    while(user_input != 'e'):
        # symptom_list = get_symptoms(user_input)
        disease_list = get_diseases(user_input, disease_ontology)
        if not disease_list:
            print "No diseases matching these symptoms found in ontology."
        else:
            print "Here is a list of possible diseases:"
            for disease in disease_list:
                print disease
        print
        user_input = raw_input(prompt)

    end = time.time()
    sumtime = end - start
    print
    print "DONE!"
    print "Time to run program: %r seconds" % sumtime
#    print t
#    fo = open("results.txt", "wb")
#    fo.write("%d\n%.8f\n" % (t, sumtime))
#    fo.close()


if __name__ == "__main__":
    main()
