# Filename: interface.py
# Description: Allows the user to input symptoms; outputs possible diseases.
# TODO: ask questions to narrow down disease

import sys
sys.dont_write_bytecode = True

import time
from random import shuffle

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

def some_symptoms(disease_ontology):
    string = ""
    l = []

    diseases = disease_ontology.keys()

    counter = 0

    # calculate limit
    # how i know what the last element of the list is
    # i don't want a comma after that one
    limit = 15
    # for disease in diseases:
    #    for symptom in disease_ontology[disease][0]:
    #        limit += 1

    for disease in diseases:
        for symptom in disease_ontology[disease][0]:
            l.append(symptom)
    
    shuffle(l)

    for s in l:
        string += s
        if counter != limit:
            string += ', '
            counter += 1
        else:
            break

    return string

# # TODO? check if two strings match, but not necessarily exact match
# or if a is contained in b
def inexact_match(a, b):
    return (a in b) or (b in a)

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

    for disease in disease_ontology:
        fits = 0
        for symptom in symptoms:
            if match_found(symptom, disease_ontology[disease][0]):
                fits = 1
            else:
                fits = 0
                break
        if fits == 1:
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

# TODO: Based on the list of diseases left, deduce which with questions
def narrow_down_diseases(disease_list, ontology):
    if len(disease_list) == 1:
        last_disease = disease_list[0]
    else:
        last_disease = "Asthma"

        # get common symptoms
        common = []
        not_in_common = {}

        # do first two
        for symptoma in ontology[disease_list[0]][0]:
            for symptomb in ontology[disease_list[1]][0]:
                if inexact_match(symptoma, symptomb):
                    if symptoma not in common:
                        common.append(symptoma)
                    if symptomb not in common:
                        common.append(symptomb)

        counter = 0 # we've done the first two
        # compare list to rest of diseases
        for disease in disease_list:
            c = []
            if counter > 1 and counter < len(disease_list):
                for symptom in common:
                    for s in ontology[disease_list[counter]][0]:
                        if inexact_match(symptom, s):
                            c.append(s)
                common = c
                counter += 1
            counter += 1


        # to populate not_in_common, compare common with all symptoms of a disease
        for disease in disease_list:
            for symptom in common:
                for symptoma in ontology[disease][0]:
                    if not inexact_match(symptom, symptoma):
                        if disease not in not_in_common:
                            not_in_common[disease] = []
                        not_in_common[disease].append(symptoma)

        for disease in disease_list:
            print disease
            print ontology[disease][0]

        # ask yes no questions about remaining symptoms not in common
        print "common:"
        print common
        print "not_in_common:"
        print not_in_common
        assert(False)
        for disease in not_in_common:
            print disease
            assert(False)

    return last_disease

def main():
    print "Calculating..."
    start = time.time()

    filename = "polished_diseases.txt"

    disease_ontology = process_disease_file(filename)
    # print disease_ontology

    # TODO: Implement ask questions to narrow down disease
    # TODO: Implement user asks about disease, give symptoms and treatment

    print
    print "15 random samples of symptoms in disease ontology:"
    print
    print some_symptoms(disease_ontology)
    print

    prompt = "Input a list of symptoms separated by a comma (type 'e' to exit): "
    
    user_input = raw_input(prompt)

    while(user_input != 'e'):
        # symptom_list = get_symptoms(user_input)
        disease_list = get_diseases(user_input, disease_ontology)
        print
        if not disease_list:
            print "No diseases matching these symptoms found in ontology."
        else:
            print "Here is a list of possible diseases:"
            for disease in disease_list:
                print disease
            last_disease = narrow_down_diseases(disease_list, disease_ontology)
            print
            print "Here are some treatment options for %s:" % last_disease
            for treatment in disease_ontology[last_disease][1]:
                print treatment
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
