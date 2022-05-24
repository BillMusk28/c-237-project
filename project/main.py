import pywhatkit
print("WELCOME TO AUTOMATIC WHATSAPP")
a = int(input("Please enter hour of sending the message(in 24-hour clock): "))
b = int(input("Please enter minute of sending the message: "))
num = int(input("Please enter number of the person to send the message: "))

pywhatkit.sendwhatmsg(num, 'Hello World', a, b)