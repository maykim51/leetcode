'''
아이디어는 잘 생각해냈고, 구현도 잘 했음. 스페이스바 처리만 잘 하면 될 것.
'''
dictNum = {
    "0":"",
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine",
    "10":"Ten",
    "11":"Eleven",
    "12":"Twelve",
    "13":"Thirteen",
    "14":"Fourteen",
    "15":"Fifteen",
    "16":"Sixteen",
    "17":"Seventeen",
    "18":"Eighteen",
    "19":"Nineteen"
}

dictTens = {
    "2":"Twenty",
    "3":"Thirty",
    "4":"Forty",
    "5":"Fifty",
    "6":"Sixty",
    "7":"Seventy",
    "8":"Eighty",
    "9":"Ninety"
}

units = [
    "Thousand",
    "Million",
    "Billion",
    "Trillion"
]

class Solution:
    def readThreeDigits(self, num:str) -> str:
        # if one digit
        if len(num) == 1:
            return dictNum[num]
        elif len(num) == 2:
            if num in dictNum:
                return dictNum[num]
            else:
                if num[1] == 0:
                    return dictTens[num[0]]
                return dictTens[num[0]] + " " + dictNum[num[1]]
        elif len(num) == 3:
            return dictNum[num[0]] + " " + "Hundred" + " " + dictTens[num[1]] + " " + dictNum[num[2]]
        
        return "N/A"
            
        
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        numbers = []
        
        #check the size of number
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000

        # slice number by 3 
        num = str(num)
        while(num != ""):
            numbers.insert(0,num[-3:])
            num = num[:-3]
        
        # read each 3 digits
        for i in range(len(numbers)):
            numbers[i] = self.readThreeDigits(numbers[i].strip())
        print(numbers)
        
        ret = ""
        # insert units (hundreds, ten...)
        if billion:
            ret += numbers[0] + " " + "Billion"
            numbers = numbers[1:]
        if million:
            if ret != "":
                ret += " "
            ret += numbers[0] + " " + "Million"
            numbers = numbers[1:]
        if thousand:
            if ret != "":
                ret += " "
            ret += numbers[0] + " " + "Thousand"
            numbers = numbers[1:]
        if rest:
            if ret != "":
                ret += " "
            ret += numbers[0]
        return ret
        
        
        


def main():
    sol = Solution()
    print(sol.numberToWords(20))
    
if __name__ == "__main__":
    main()
