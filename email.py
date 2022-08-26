{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f9708507",
   "metadata": {},
   "outputs": [],
   "source": [
    "#From Outlook\n",
    "import os\n",
    "import win32com.client as win32\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "41193430",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Login Success!!\n",
      "Email has been sent to python271290@gmail.com\n"
     ]
    }
   ],
   "source": [
    "# From gmail\n",
    "# In settings use the App password to generate password and use it in code to log in\n",
    "import smtplib\n",
    "\n",
    "sender_mail=\"python271290@gmail.com\"\n",
    "rec_mail=\"python271290@gmail.com\"\n",
    "listadd=[\"abej90@gmail.com\",\"patianupama2@gmail.com\"] # Send mail to multiple addresses \n",
    "#password=input(str(\"Enter your password: \"))\n",
    "password=\"yswnemxpebhjvooz\" # Generated from App Password due to google settings\n",
    "\n",
    "subject=\"Test Mail via Python!!\"\n",
    "body=\"Python testing from gmail via Anaconda Jupyter\"\n",
    "message=\"subject:{}\\n\\n{}.format(subject,body)\"\n",
    "server=smtplib.SMTP('smtp.gmail.com',587)\n",
    "server.ehlo()\n",
    "server.starttls()\n",
    "server.login(sender_mail,password)\n",
    "print(\"Login Success!!\")\n",
    "server.sendmail(sender_mail,listadd,body)\n",
    "print(\"Email has been sent to\",rec_mail)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "365e9e4a",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'poem' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-16-dc6036032110>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     12\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     13\u001b[0m \u001b[1;31m# Open the plain text file whose name is in textfile for reading.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 14\u001b[1;33m \u001b[1;32mwith\u001b[0m \u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpoem\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mfp\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     15\u001b[0m     \u001b[1;31m# Create a text/plain message\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     16\u001b[0m     \u001b[0mmsg\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mEmailMessage\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'poem' is not defined"
     ]
    }
   ],
   "source": [
    "# Import smtplib for the actual sending function\n",
    "import smtplib\n",
    "\n",
    "# Import the email modules we'll need\n",
    "from email.message import EmailMessage\n",
    "\n",
    "sender_mail=\"python271290@gmail.com\"\n",
    "rec_mail=\"python271290@gmail.com\"\n",
    "listadd=[\"abej90@gmail.com\",\"patianupama2@gmail.com\"] # Send mail to multiple addresses \n",
    "#password=input(str(\"Enter your password: \"))\n",
    "password=\"yswnemxpebhjvooz\" # Generated from App Password due to google settings\n",
    "\n",
    "# Open the plain text file whose name is in textfile for reading.\n",
    "with open(poem) as fp:\n",
    "    # Create a text/plain message\n",
    "    msg = EmailMessage()\n",
    "    msg.set_content(fp.read())\n",
    "\n",
    "# me == the sender's email address\n",
    "# you == the recipient's email address\n",
    "msg['Subject'] = f'The contents of {textfile}'\n",
    "msg['From'] = sender_mail\n",
    "msg['To'] = rec_mail\n",
    "\n",
    "# Send the message via our own SMTP server.\n",
    "s = smtplib.SMTP('smtp.gmail.com',587)\n",
    "s.send_message(msg)\n",
    "s.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0e0405bf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
