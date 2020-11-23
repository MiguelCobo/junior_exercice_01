
def ask_age() -> None:
    age = int(input('Age: '))
    if age >100:
        return ask_age()
    if age < 18 :print('You are not an adult')
    if age >= 18 :print('You are an adult')

def main() -> None:
    ask_age()
