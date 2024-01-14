from linkedin_api import Linkedin
api = Linkedin('rahulxsharma00@gmail.com','pitbull2000')
username = input("enter the username: ")
print(api.get_profile(username))



