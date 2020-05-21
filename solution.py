class ChangeMaker:
    def __init__(self, total_price, user_payment):
        self.total_price = total_price
        self.user_payment = user_payment
        self.need_change = int((user_payment*100)- (total_price)*100)
        self.denomination_dict = {'$100 bill':10000, '$20 bill':2000, '$10 bill':1000,'$5 bill':500, '$1 bill':100,
                 'quarter':25, 'dime':10, 'nickel':5, 'penny':1}

    def optimal_change(self):
        result=""
        if self.need_change < 0:
          return f"The costs are ${self.total_price} and the amount you paid are ${self.user_payment}, please go on the payment."
        if self.need_change == 0:
          return f"The payment equals the price. No changes."

        for key, value in self.denomination_dict.items():
             count_of_change=0
             if self.need_change >= value:
                (largest_num, self.need_change)=divmod(self.need_change, value)
              # largest_num = self.need_change//value
              # self.need_change = self.need_change % value
                
                for i in range(0, largest_num):
                   count_of_change += 1

                if self.need_change == 0 and key =="penny" and count_of_change >1:
                    result += f'{count_of_change} pennies.' 
                elif self.need_change ==0 and key !="penny" and count_of_change >1:
                    result += f'{count_of_change} {key}s.'
                elif self.need_change == 0 and count_of_change ==1:
                    result +=f'{count_of_change} {key}.'
                elif self.need_change > 0 and count_of_change ==1:
                    result += f'{count_of_change} {key}, '
                else:
                    result += f'{count_of_change} {key}s, '


        return f'The optimal change for an item that costs ${self.total_price} with an amount paid of ${self.user_payment} is {result}'

Change_Maker1 = ChangeMaker(62.13, 100)
print(Change_Maker1.optimal_change())
