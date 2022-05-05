#Author: Faith Elledge
#Grithub_username: Elledgef
#Date: 5/4
#Description: returns names that only start with a K

def add_surnames(lst):
    return [x+"Kardashian"for x in lst if x[0].lower()=='k']