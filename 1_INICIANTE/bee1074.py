qtt_values = int(input())
results = []
string_result = ''
for _ in range(qtt_values):
    number = int(input())
    if number == 0:
        string_result+="NULL"
    else:
        if number%2 == 0:
            string_result += "EVEN"
        elif number%2 != 0:
            string_result += "ODD"
        if number > 0:
            string_result += ' POSITIVE'
        if number < 0:
            string_result += ' NEGATIVE'
    results.append(string_result)
    string_result = ''
    
    
for result in results:
    print(result)