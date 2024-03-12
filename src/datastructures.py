
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
 
class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
         handler_member = {
         "id": self._generateId(),
         "first_name": member["first_name"],
         "last_name": member["last_name"],
         "age": member["age"],
         "lucky_numbers": list(member["lucky_numbers"])
         }
         if int(handler_member["age"]) > 0:
            self._members.append(handler_member)
            return self._members
         else: "Age must be more than 0"

    

    def delete_member(self, id):
        # fill this method and update the return
        def member_borrado(member):
            return member["id"]!= id
        member = list(filter(member_borrado,self._members))
        if member == self._members:
            return "Member Not Found"
        else:
            self._members = member
            return self._members


    def get_member(self, id):
        # fill this method and update the return
        def filter_list(member):
            return member["id"] == id
        member = list(filter(filter_list,self._members))
        if member != []:
            return member[0]
        else:
            return "member not Found"
    
    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
