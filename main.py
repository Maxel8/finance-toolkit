import json

print("Chose language:")
print("en - English")
print("de - Deutsch")

language = input("Language: ").lower()
if language not in ["en", "de"]:
    print("Invalid language, defaulting to English.")
    language = "en"

with open(f"locales/{language}.json", "r", encoding="utf-8") as f:
        lang = json.load(f)

print()
print(lang["menu_title"])
print()

while True:

    print(lang["menu_option"])
    print(lang["menu_option_1"])
    print(lang["menu_option_2"])
    print(lang["menu_option_3"])
    print(lang["menu_option_4"])
    print(lang["menu_option_end"])

    option = int(input(lang["menu_option_choose"]))

    if option == 1:
        print(lang["option_1_title"])
        print()

        def interest_once():
            P = float(input(lang["option_1_principal"]))
            r = float(input(lang["option_1_rate"]))
            t = float(input(lang["option_1_time"]))

            A = P * (1 + (r/100) * (t/12))
            A = round(A, 2)
            interest = round(A - P, 2)
            print(lang["option_1_result"], A)
            print(lang["option_1_interest"], interest)

        interest_once()


    elif option == 2:
        print(lang["option_2_title"])
        

    elif option == 3:
        print(lang["option_3_title"])

    elif option == 4:
        print(lang["option_4_title"])
        print()

        def annuity_loan():
            K = float(input(lang["option_4_loan-amount"]))
            i = float(input(lang["option_4_interest-rate"]))
            n = int(input(lang["option_4_months"]))

            R = K * (((i/100/12)*(1+(i/100/12)**n)) / ((1+i/100/12)**n - 1))
            print(lang["option_4_result"], R)
        
        annuity_loan()

    elif option == 0:
        print(lang["option_end_title"])
        break
    else:
        print(lang["invalid_message"])

print()
print(lang["exit_message"])