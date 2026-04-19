import csv
def save_emails():
    while True:
        emails = input("enter an email id or type 'done' to finish ")
        if emails == "done":
            break
        with open("saved_emails.csv","a",newline="") as file:
            csv.writer(file).writerow([emails])
save_emails()

def open_emails():
    with open("saved_emails.csv","r",newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0])
open_emails()