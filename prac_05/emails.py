def main():
    email_to_name = {}
    email = input("Email: ").strip()

    while email != "":
        name = get_name_from_email(email)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm == "n" or confirm == "no":
            name = input("Name: ").strip().title()
        email_to_name[email] = name
        email = input("Email: ").strip()
    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.replace('_', '.').split('.')
    name = ' '.join(part.title() for part in parts)
    return name

main()
