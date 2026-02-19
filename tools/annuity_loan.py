import json

print("Chose language:")
print("en - English")
print("de - Deutsch")

language = input("Language: ").lower()
if language not in ["en", "de"]:
    print("Invalid language, defaulting to English.")
    language = "en"

with open(f"../locales/{language}.json", "r", encoding="utf-8") as f:
        lang = json.load(f)

print(lang["option_4_title"])
print()

def annuity_loan():
    K = float(input(lang["option_4_loan-amount"]))
    i = float(input(lang["option_4_interest-rate"]))
    n = int(input(lang["option_4_months"]))
    R = K * (((i/100/12)*(1+(i/100/12)**n)) / ((1+i/100/12)**n - 1))
    print(lang["option_4_result"], R)
        
annuity_loan()