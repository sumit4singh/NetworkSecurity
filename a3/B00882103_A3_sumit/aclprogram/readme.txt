Hi,
directory overview
standard.py is for standard ACL
main.py is for extended ACL
File named acl1, acl2 acl3 are sample ACL for standard.py validation
File named acl1_input and soo on are sample input for respective ACL's
file named e_acl_1, e_acl_2, and e_acl_3 are sample Exteneded ACL for main.py program validation
file named e_acl_1_input and so on are input for respective extened ACL's


Running

to run the prgram pass sample acl and input as command line arguments while running the code

example:
python main.py e_acl_1 e_acl_1_input for extened ACL program
python standard.py acl1 acl1_input for standard ACL program

limitations:
Insterd of any we have to gice 0.0.0.0 255.255.255.255 in ACLs
it does not support range 21-22 insterd we have to split it into two different statements.
 