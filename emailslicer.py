#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      LALIT SHARMA
#
# Created:     23/11/2022
# Copyright:   (c) LALIT SHARMA 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
email_user = input("enter your email id: ")
user_name = email_user[:email_user.index("@")]
domain = email_user[email_user.index("@")+1:]
print("user name = ",user_name)
print("Domain = ",domain)