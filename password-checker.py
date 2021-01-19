import requests
import hashlib
import sys


def request_api_data(char):
    res = requests.get("https://api.pwnedpasswords.com/range/" + f"{char}")
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching data: {res.status_code}")
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    print(hashes)
    for h, count, in hashes:
        if h == hash_to_check:
            print(h, count)
            return count
    return 0


def pawned_password(passcode):
    sha1_passcode = hashlib.sha1(passcode.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1_passcode[:5], sha1_passcode[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pawned_password(password)
        if count:
            print("")
            print(
                f'Your password "{password}" was found {count} times... please change your password')
        else:
            print(f"{password} was not found. Carry on!")
    print("")
    print(80 * "-")
    print("Finished script execution successfully!")


# enables us to enter options after running a file in the terminal
if __name__ == '__main__':
    main(sys.argv[1:])
