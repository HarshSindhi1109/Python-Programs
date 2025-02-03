def logic(num, values, words):
    ans = ""

    for i in range(0, len(values)):
        value = values[i]
        word = words[i]

        if num >= value:
            if num >= 100:
                ans += logic(num // value, values, words) + " "
            
            ans += word

            if num % value > 0:
                ans += " " + logic(num%value, values, words)
            
            return ans.strip()
    return ans

def convertToWord(num):
    if num == 0:
        return "Zero"
    
    values = [1000000000, 1000000, 1000, 100, 90, 80, 70, 60, 50, 40, 30, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    words = [ "Billion", "Million", "Thousand", "Hundred", "Ninety", "Eighty", "Seventy", "Sixty", "Fifty", "Forty", "Thirty", "Twenty", "Nineteen", "Eighteen", "Seventeen", "Sixteen", "Fifteen", "Fourteen", "Thirteen", "Twelve", "Eleven", "Ten", "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]

    return logic(num, values, words)

num = int(input("Enter a number="))
print("Number: ",convertToWord(num))