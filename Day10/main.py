#Function with return statement


def formatted_name(first_name, last_name):
    fomatte_fname = first_name.title()
    fomatte_lname = last_name.title()
    return f"{fomatte_fname} {fomatte_lname}"


print(formatted_name("SHiv", "lALL"))