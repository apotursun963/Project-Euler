
def number_to_words(num):
    digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if 1 <= num < 10:
        return digits[num]
    elif 10 < num < 20:
        return teens[num - 10]
    elif 10 <= num < 100:
        return tens[num // 10] + (digits[num % 10] if num % 10 != 0 else "")
    elif 100 <= num < 1000:
        return digits[num // 100] + "hundred" + ("and" + number_to_words(num % 100) if num % 100 != 0 else "")
    elif num == 1000:
        return "onethousand"
    return ""

def count_letters_in_words(limit):
    total_letters = 0
    for i in range(1, limit + 1):
        word = number_to_words(i)
        total_letters += len(word)
    return total_letters

print(count_letters_in_words(1000))
