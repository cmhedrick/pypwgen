import string
import secrets

def gen_password(length=16, symbols=True):
    """
        desc: generate password based on length and if symbols are allowed
        input: length=int, symbols=bool
        return: string
    """
    # chars :94 include digits, alphas (low + upper), and symbols
    chars = string.printable[:94]
    # some places don't do symbols
    if not symbols:
        # chars :62 as above as below, except symbols
        chars = string.printable[:62]

    # use py3's secrets.choice function to randomly pick char
    return ''.join(secrets.choice(chars) for i in range(length))

if __name__ == "__main__":
    print('Test pass (defaults): ' + gen_password())
    print('Test pass (custom len): ' + gen_password(length=32))
    print('Test pass (no sym): ' + gen_password(symbols=False))
    print('Test pass (cust len + no sym): ' + gen_password(32, False))