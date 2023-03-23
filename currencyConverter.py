class Currency_Converter:


    def __init__(self):

        self.countries = {1 : "convUSD", 2 : "convEuro", 3 : "convYuan", 4 : "convLira", 5: "convVND", 6: "convBaht"}
        self.convUSD = {1: "1",
                        2: "0.93",
                        3: "6.79",
                        4: "18.83"}


                          
        self.convEuro = {1: "1.07",
                         2: "1",
                         3: "7.26",
                         4: "20.14"}


                          
        self.convYuan = {1: "0.15",
                         2: "0.14",
                         3: "1",
                         4: "2.77"}


                          
        self.convLira = {1: "0.053",
                         2: "0.05",
                         3: "0.36",
                         4: "1"}

                          
        self.convVND = {1: "0.000042",
                        2: "0.000039",
                        3: "0.00029",
                        4: "0.0008",
                        5: "1",
                        6: "0.0014"}


                          
        self.convBaht = {1: "0.03",
                         2: "0.028",
                         3: "0.2",
                         4: "0.56",
                         5: "703.83",
                         6: "1"}

        
    def op(self, ques, moneyin, rate):
        if ques == "1":
            a = self.convUSD.get(rate)
            b = (moneyin * float(a))
            return b
            
        if ques == "2":
            a = self.convEuro.get(rate)
            b = (moneyin *float(a))
            return b
            
        if ques == "3":
            a = self.convYuan.get(rate)
            b = (moneyin * float(a))
            return b
            
        if ques == "4":
            a = self.convLira.get(rate)
            b = (moneyin * float(a))
            return b

        if ques == "5":
            a = self.convVND.get(rate)
            b = (moneyin * float(a))
            return b

        if ques == "6":
            a = self.convBaht.get(rate)
            b = (moneyin * float(a))
            return b



def main():
    cc = Currency_Converter()
    print(cc.op(input("Please enter which type of currency you have. Choose from the list: \n1. United States Dollar \n2. European Euro \n3. Chinese Yuan \n4. Turkish Lira \n5. Vietnam Dong \n6. Thailand Baht\n"),int(input("Enter the amount of money \n")), int(input("Enter money to convert. Choose from the list: \n1. United States Dollar \n2. European Euro \n3. Chinese Yuan \n4. Turkish Lira\n5. Vietnam Dong \n6. Thailand Baht\n")) ))





if __name__=="__main__":
    main()


   
