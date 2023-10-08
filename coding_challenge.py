import re

def extract_phone_numbers(string):
    # Phone number: (XXX) XXX-XXXX
    phone_pattern = r'\(\d{3}\) \d{3}-\d{4}'
    return re.findall(phone_pattern, string)

def extract_email_addresses(string):
    # Email
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(email_pattern, string)

def replace_email_addresses(string, replacement):
    # Email
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.sub(email_pattern, replacement, string)

# string to test function
string = "Please contact info@example.com for assistance. Phone: (123) 456-7890 or (111) 222-3333"

print(extract_phone_numbers(string))
# Output IS PHONENUMBERS

print(extract_email_addresses(string))
# Output IS EMAIL

print(replace_email_addresses(string, "REPLACED"))
# Output is REPLACED




