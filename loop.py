#!/usr/bin/env /usr/bin/python3

"""
example code to extract ID & email from data structure
"""

# this is data we're assuming is returned to us
# it is a dictionary with the  following structure
# two keys (Accounts and ResponseMetadata)
#   Accounts is a list of dictionaries with the following keys:
#        ARN
#        Email
#        Id
#        JoinedMethod
#        JoinedTimestamp
#        Name
#        Status
#    Response value is a dictionary

myData = {'Accounts': [{'Arn': 'arn:aws:organizations::111111111111:account/o-exampleorgid/111111111111',
   'Email': 'bill@example.com',
   'Id': '111111111111',
   'JoinedMethod': 'INVITED',
   'JoinedTimestamp': ['2016', '12', '15', '19', '30', '15', '3', '350', '0'],
   'Name': 'Master Account',
   'Status': 'ACTIVE'},
  {'Arn': 'arn:aws:organizations::111111111111:account/o-exampleorgid/222222222222',
   'Email': 'alice@example.com',
   'Id': '222222222222',
   'JoinedMethod': 'INVITED',
   'JoinedTimestamp': ['2016', '12', '15', '19', '30', '15', '3', '350', '0'],
   'Name': 'Developer Account',
   'Status': 'ACTIVE'},
  {'Arn': 'arn:aws:organizations::111111111111:account/o-exampleorgid/333333333333',
   'Email': 'juan@example.com',
   'Id': '333333333333',
   'JoinedMethod': 'INVITED',
   'JoinedTimestamp': ['2016', '12', '15', '19', '30', '15', '3', '350', '0'],
   'Name': 'Test Account',
   'Status': 'ACTIVE'},
  {'Arn': 'arn:aws:organizations::111111111111:account/o-exampleorgid/444444444444',
   'Email': 'anika@example.com',
   'Id': '444444444444',
   'JoinedMethod': 'INVITED',
   'JoinedTimestamp': ['2016', '12', '15', '19', '30', '15', '3', '350', '0'],
   'Name': 'Production Account',
   'Status': 'ACTIVE'}],
 'ResponseMetadata': {'unusedKey': 'unusedVal'}}


def getIDandEmail(inData):
    """
    extract ID & email from data
    :param inData:
    :return: list of dictionaries
    """

    # we'll iterate through the list contained in the dict key 'Accounts'.  We'll use a temporary dictionary (tdict)
    # to contain the Id & Email
    # Then append that dict to a list
    # first, create an empty list and temp dictionary
    myList = []
    tdict = {}
    for item in inData['Accounts']:
        tdict['Id'] = item['Id']
        tdict['Email'] = item['Email']
        myList.append(tdict.copy())

    return myList


def printData(inStuff):
    """
    print the data in a nice format
    :param inStuff:
    :return:
    """
    print("ID\t\tEmail")
    for item in inStuff:
        print("{}\t{}".format(item['Id'], item['Email']))


def main():
    parsedData = getIDandEmail(myData)
    printData(parsedData)


main()

