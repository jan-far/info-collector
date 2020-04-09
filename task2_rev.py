import string
import random
import itertools

id = itertools.count(1)
users = []
Another_user = True
saved = []
dic = {}


def another_user():
    another = input("Another User? y/n: ").lower()
    if another == "y":
        details()
    elif another == "n":
        print(saved)
    else:
        print("Wrong command! Try again")


def details():
    while Another_user:
        ID = next(id)
        user = ('User{}'.format(ID))
        first_name = input(f"Please enter your first name, {user}: ")
        last_name = input(f"Please enter your last name, {user} : ")
        email = input(f"Please enter your email address, {user}: ")
        length = 5
        keys = "".join(random.choice(string.ascii_lowercase) for i in range(length))
        password = first_name[:2] + last_name[-2:] + keys
        print(f"{user}, Generated password: " + password)

        def pass_key():
            okay_with_pass = input(f"Are you okay with the password? {password} [y/n]: ").lower()

            if okay_with_pass == "y":
                save = {"Name": first_name + " " + last_name,
                        "Email": email,
                        "Password": password
                        }
                received = f"{user} details are: {save}"
                saved.append(received)
                print(received)
                another_user()

            elif okay_with_pass == "n":
                new_pass = input("Enter desired password: ")
                if len(new_pass) < 7:
                    print("Sorry! input password of 7 characters or more")
                    new_pass = input("Enter desired password: ")
                    print("Password: " + new_pass + "has been saved!")
                    save = ({"Name": first_name + " " + last_name,
                             "Email": email,
                             "Password": new_pass
                             })
                    received = f"{user} details are: {save}"
                    saved.append(received)
                    print(received)

                    other_user = input("Register another User? [y/n]: ").lower()
                    if other_user == "y":
                        details()
                        # anotherUser()
                    elif other_user == "n":
                        print(saved)
                    else:
                        print("Not a command! Try again")
                        # for item in saved:
                        # for key, value in item:
                        #   print('{}:{}'.format(key, value))

                else:
                    save = ({"Name": first_name + " " + last_name,
                             "Email": email,
                             "Password": new_pass
                             })
                    print("password has been saved!")
                    received = f"{user} details are: {save}"
                    saved.append(received)
                    print(received)

            else:
                print("Wrong input! please try again")
                pass_key()

        pass_key()
        break


details()
# another = input("Another User? y/n: ").lower()
# if another == "y":
#     details()
# elif another == "n":
#     print(saved)
# else:
#     print("Wrong command! Try again")
