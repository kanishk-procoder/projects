from tkinter.constants import HIDDEN

card_number = input("Enter the card number : ")
amount = input("Entre to amount to pay : ")

lastdigits = card_number[len(card_number)-4:]
hidden_cardnum = "XXXX "*3 + lastdigits
#message of payment
print(f"An amount of ${amount} has been debited from your account with card number {hidden_cardnum}")