This repository contains the submission for DecodeLabs Project 4. The project goal is to create a checklist that identifies basic system security vulnerabilities, with a focus on weak passwords, software update status, and unsafe user practices.

Project Overview
Project 4 is a practical system security audit exercise. The project slides show a four-step checklist covering identity security, patch management, human-factor risks, and endpoint hygiene, and they state that the final deliverable is a professional one-page vulnerability report based on findings from the user's own machine audit.

Features
Checks for weak or short passwords and weak multi-factor authentication choices.

Checks whether operating system updates are enabled and whether key software is outdated.

Identifies unsafe practices such as guest accounts, privilege creep, poor screen-lock habits, and insecure storage of sensitive data.

Checks firewall status and full-disk encryption as part of endpoint hygiene.

Produces a risk score, findings list, and remediation recommendations based on checklist answers.

Technologies Used
Python

Terminal / CLI

How It Works
The program asks the user a series of yes/no audit questions. Each risky answer increases the total score, and the final score is used to classify the machine's overall risk level as Low, Medium, or High. The output includes findings and practical remediation advice.

How to Run
bash
python system_vulnerability_checklist.py
Example Areas Covered
Identity front door: passwords and MFA choices.

Software decay and patch management: OS updates, outdated browser versions, antivirus status, and Shadow IT.

Human perimeter: guest accounts, excessive admin rights, physical security, and unsafe user behavior.

Network and endpoint hygiene: firewall status and local disk encryption.

Learning Outcome
This project develops practical risk assessment skills and reinforces the idea that security is a continuous process rather than a one-time product deployment, which is a theme highlighted in the project slides.

Notes
This project was built as part of the DecodeLabs Cyber Security internship training kit.
