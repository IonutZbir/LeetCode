import math

class Solution:
    def fractionAddition(self, expression: str) -> str:
            i = 0
            nums = []
            dens = []
            
            # se l'espressione inizia con un numero positivo, aggiungo un "+"
            if expression[0] != '-':
                expression = '+' + expression
            
            n = len(expression)
            
            while i < len(expression):
                
                sign = 1
                if expression[i] == '+':
                    sign = 1
                elif expression[i] == '-':
                    sign = -1
                i += 1
                
                # trovo il numeratore    
                num = 0
                while i < n and expression[i].isdigit():
                    num = num * 10 + int(expression[i])
                    i += 1
                
                i += 1 # slash
                
                # trovo il denominatore
                den = 0
                while i < n and expression[i].isdigit():
                    den = den * 10 + int(expression[i])
                    i += 1

                nums.append(num * sign)
                dens.append(den)

            mcm = math.prod(dens) # minimo comune multiplo
            
            # ricalcolo i numeratori
            nums = [int((mcm / dens[i]) * nums[i]) for i in range(len(dens))] 
            
            numerator = sum(nums)
            mcd = math.gcd(numerator, mcm) # massimo comun divisore per poter semplificare poi la frazione
            
            numerator = numerator // mcd
            mcm = mcm // mcd
            
            return f"{numerator}/1" if numerator == 0 else f"{numerator}/{mcm}"
