import json

# num = []

# keys_set_1 = {0: "Dizzy", 1: "COLD", 2: "MOISTURE", 3: "TEMPRATURE", 4: "BURN",
#              5: "Dizzy", 6: "Dizzy", 7: "Dizzy", 8: "Dizzy", 9: "Dizzy",
# 
#               10: "Dizzy", 11: "Dizzy", 12: "Dizzy", 13: "Dizzy", 14: "Dizzy"}


def rewrite(write): 
    write = write.decode()
    info = write.split("=")
    print(info)
    if info[0] == "Field1_name": 
        num = ''
        # num = info[0].isdigit()
        for letter in info[0]: 
            if letter.isdigit(): 
                num += letter

        open_json(num, info[1])
    
    elif info[0] == "Field2_name":
        num2 = '' 
        # num = info[0].isdigit()
        for letter in info[0]: 
            if letter.isdigit(): 
                num2 += letter
        open_json(num2, info[1])
    
    elif info[0] == "Field3_name": 
        num3 = ''
        # num = info[0].isdigit()
        for letter in info[0]: 
            if letter.isdigit(): 
                num3 += letter
        open_json(num3, info[1])
    
    elif info[0] == "Field4_name": 
        num4 = ''
        # num = info[0].isdigit()
        for letter in info[0]: 
            if letter.isdigit(): 
                num4 += letter
        open_json(num4, info[1])
    
    elif info[0] == "Field5_name":
        num5 = '' 
        # num = info[0].isdigit()
        for letter in info[0]: 
            if letter.isdigit(): 
                num5 += letter
        open_json(num5, info[1])
    
    elif info[0] == "Field6_name":
        num6 = '' 
        # num = info[0].isdigit()
        for letter in info[0]: 
            if letter.isdigit(): 
                num6 += letter
        open_json(num6, info[1])
    
    elif info[0] == "Field7_name": 
        num7 = ''
        # num = info[0].isdigit()
        for letter in info[0]: 
            if letter.isdigit(): 
                num7 += letter
        open_json(num7, info[1])
    
    elif info[0] == "Field8_name":
        num8 = '' 
        # num = info[0].isdigit()
        for letter in info[0]: 
            if letter.isdigit(): 
                num8 += letter
        open_json(num8, info[1])

    elif info[0] == "Field9_name": 
        num9 = ''
        # num = info[0].isdigit()
        for letter in info[0]: 
            if letter.isdigit(): 
                num9 += letter
        open_json(num9, info[1])
    
    elif info[0] == "Field10_name": 
        num10 = ''
        # num = info[0].isdigit()
        for letter in info[0]: 
            if letter.isdigit(): 
                num10 += letter
        open_json(num10, info[1])
    
    elif info[0] == "Field11_name": 
        num11 = ''
        # num = info[0].isdigit()
        for letter in info[0]: 
            if letter.isdigit(): 
                num11 += letter
        open_json(num11, info[1])
    
    elif info[0] == "Field12_name":
        num12 = '' 
        # num = info[0].isdigit()
        for letter in info[0].split(): 
            if letter.isdigit(): 
                num12 += letter
        open_json(num12, info[1])
    
    elif info[0] == "Field13 _name":
        num13 = '' 
        # num = info[0].isdigit()
        for letter in info[0]: 
            print(letter)
            if letter.isdigit():
                print("Here" + letter) 
                num13 += letter
        open_json(num13, info[1])

    elif info[0] == "Field14_name":
        num13 = '' 
        # num = info[0].isdigit()
        for letter in info[0]: 
            if letter.isdigit(): 
                num14 += letter
        open_json(num14, info[1])

def open_json(number, data):
    with open("keyset_nur.json", "r") as x: 
        something = json.load(x)
        print(data)
        print(number)

        something[str(number)] = str(data)
    
    with open ("keyset_nur.json", "w") as x: 
        json.dump(something, x, indent=2)
