# The CPLPREPPER
## Disclaimer
This program is intended solely for the modification of strings. Use is only permitted with the prior written consent of the customer and in accordance with all applicable national laws. Any use outside this scope is expressly prohibited.

## Explanation
cplprepper stands for “Custom Payload Prepper”. It is a simple Python tool that helps you to prepare strings.
You have two input fields to add an IP and your custom string. I developed this tool primarily to help me prepare custom XSS payloads for penetration testing.
Apart from pentesting, you can also use it to create custom variations of a string that you can enter yourself.

## Usage
Let's say you have a registration form on a website and you want to test the website for XSS. So you're going to enter different payloads in each of the possible input fields. But to keep track of which of the fields is vulnerable to XSS, you customize each payload with the name of the respective input field. Entering the attacker IP and the respective names can quickly become very extensive. And this is exactly where this tool can help you.

## Operating instructions
The program is self-explanatory and guides you through all the necessary steps. All you have to do is start it.
~~~bash
python3 cplprepper.py
~~~
