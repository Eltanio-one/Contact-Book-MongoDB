from pymongo.mongo_client import MongoClient
from pymongo import ReturnDocument
from dotenv import load_dotenv
from pathlib import Path
import os
import re


def retrieve_database() -> MongoClient:
    load_dotenv(
        dotenv_path=Path(
            "/Users/danielhavers/OneDrive - Anthony Nolan/VSCode/Contact Book MongoDB/mongo.env"
        )
    )

    uri = os.environ.get("MONGO_URI")

    # Create a new client and connect to the server
    client = MongoClient(uri)

    # Send a ping to confirm a successful connection
    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(e)


def get_name() -> str:
    while True:
        try:
            first, last = input("Name: ").split(" ")
        except ValueError:
            continue
        if not first.isalpha() or not last.isalpha():
            print("Invalid name entered")
        else:
            return f"{first} {last}"


def get_address() -> str:
    while True:
        address = input("Home Address: (house name/number, street name, postcode) ")
        if not (
            _ := re.fullmatch(
                r"^([a-zA-z0-9])+, (?:[a-zA-Z]+)? ?([a-zA-Z]+), ([A-Z]{1,2}[0-9][0-9A-Z] [0-9][A-Z]{2})$",
                address,
            )
        ):
            print("Invalid address entered")
            pass
        else:
            return address


def get_mobile() -> str:
    while True:
        mobile = input("Mobile number (with area code and no whitespace): ")
        if not (verif := re.fullmatch(r"^\+(\d{2})(\d{10})$", mobile)):
            print("Invalid mobile entered")
            pass
        if not mobile.startswith("+44"):
            print("Only UK mobile numbers allowed")
            pass
        number = verif.groups(2)
        for numb in number:
            if int(numb) < 0:
                print("Only positive numbers permitted")
                pass
        else:
            return mobile


def get_email() -> str:
    while True:
        email = input("Email: ")
        if not (
            _ := re.fullmatch(
                r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$",
                email,
            )
        ):
            print("Invalid email address entered")
            pass
        else:
            return email


def inp() -> str:
    while True:
        func = input("What action would you like to perform? (CRUD) ")
        if func.upper() not in ["C", "R", "U", "D"]:
            print("Please enter either C (create), R (read), U (update) or D (delete)")
            pass
        else:
            return func.upper()


def main() -> None:
    client = retrieve_database()
    # connect to db and collection
    db = client["contactledger"]
    contacts_collection = db["contacts"]

    # ask if user wants to CRUD
    func = inp()

    # create method
    if func == "C":
        name, address, mobile, email = (
            get_name(),
            get_address(),
            get_mobile(),
            get_email(),
        )
        contact = {"name": name, "address": address, "mobile": mobile, "email": email}
        id = contacts_collection.insert_one(contact)
        print(f"Contact created! The unique ID for this entry is: {id.inserted_id}")

    # read method
    elif func == "R":
        name = get_name()
        contact = contacts_collection.find_one({"name": name})
        for arg in contact:
            print(contact[arg])

    # update method
    elif func == "U":
        name = get_name()
        while True:
            ask = input(
                "What would you like to update? (address, mobile or email) "
            ).lower()
            if ask not in ["address", "mobile", "email"]:
                pass
            else:
                match ask:
                    case "address":
                        address = get_address()
                        contacts_collection.find_one_and_update(
                            {"name": name},
                            {"$set": {"address": address}},
                            return_document=ReturnDocument.AFTER,
                        )
                    case "mobile":
                        mobile = get_mobile()
                        contacts_collection.find_one_and_update(
                            {"name": name},
                            {"$set": {"mobile": mobile}},
                            return_document=ReturnDocument.AFTER,
                        )
                    case "email":
                        email = get_email()
                        contacts_collection.find_one_and_update(
                            {"name": name},
                            {"$set": {"email": email}},
                            return_document=ReturnDocument.AFTER,
                        )
                print("Contact successfully updated")
                break

    elif func == "D":
        name = get_name()
        contacts_collection.find_one_and_delete({"name": name})
        print("Contact successfully deleted")


if __name__ == "__main__":
    main()
