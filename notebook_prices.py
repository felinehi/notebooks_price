
class notebook():
    def __init__(self,name='',pages=None,count=None,price=None,wgt=None,ppu=None,uw=None,ppw=None,pf=None):
        self.price = price
        self.pages = pages
        self.wgt = wgt
        self.count = count
        self.name = name
        self.ppu = ppu
        self.uw = uw
        self.ppw = ppw
        self.pf = pf
        if self.pages != None and self.count != None and self.price != None and self.wgt != None:
            self.perform_funcs()
        
        return
    
    def __print__(self):
         print(self.__str__())
         return
        
    def __str__(self):
        a = str(self.ppu)
        b = str(self.uw)
        c = str(self.ppw)
        d = str(self.pf)
        return str(a+b+c+d)
    def price_per_unit(self):
        self.ppu = self.price/self.count
        return
        
    def wgt_for_unit(self):
        self.uw = self.wgt/self.count
        return
        
    def price_per_wgt(self):
        self.ppw = self.ppu/self.uw
        return

    def price_per_page(self):
        self.pf = self.price/self.pages
        return
        
    def perform_funcs(self):
        self.price_per_unit()
        self.wgt_for_unit()
        self.price_per_wgt()
        self.price_per_page()
        return
    

def compare_notebooks(*bk):
    for unit in bk:
        for unit2 in bk:
            if unit == unit2: continue
            
    
if __name__ == "__main__":
    '''
    Notebook data sourced from 
    
    https://www.amazon.com/Spiral-Notebook-Subject-Assorted-48-Pack/

    https://www.amazon.com/Five-Star-Notebooks-Subject-38052/

    https://www.amazon.com/Oxford-Spiral-Notebook-College-Ruled/

    https://www.amazon.com/ViVin-Notebooks-Subject-College-Assorted/

    https://www.amazon.com/Five-Star-Notebook-Customizable-820045-ECM
    
    on 8-16-2024.
    '''
    print(notebook('Five-Star-Customizable',100,6,26.11,6.58))
    print(notebook('ViVin',100,12,35.99,11.36))
    print(notebook('Oxford',70,24,39.97,13.48))
    print(notebook('Five-Star-Subject',100,6,19.99,2.8))
    print(notebook('Spiral Notebook Assorted',70,48,69.79,None))
