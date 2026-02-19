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