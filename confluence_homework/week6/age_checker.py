age = input('Enter your age: ')

def check_age(age):
    try:
        if age.strip() == "":
            raise ValueError("Empty string")

        age_int = int(age) 

        if age_int < 0 or age_int > 120:
            raise ValueError("Invalid age")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except TypeError as te:
        print(f"TypeError: {te}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    else:
        print(f"Age {age_int} is valid.")
    finally:
        print("Validation complete")

