class Sol:
    def lemonade_change(self,bills):
        fives,tens=0,0
        for x in bills:
            if x==5:
                fives+=1
            elif x==10 and fives==0:
                print(1)
                return False
            elif x == 10:
                tens+=1
                fives-=1
            elif x==20 and (tens==0 or fives==0):
                if fives<3:
                    return False
            elif x == 20 and (tens> 0 and fives> 0):
                fives -= 1
                tens-=1
            elif x == 20 and fives > 2:
                fives-=3
        return True

if __name__ == '__main__':
    p = Sol()
    print(p.lemonade_change(bills = [5,10,20]))
