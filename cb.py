class cB:
    def __init__(self, balance, created_at,currency, cid, name,primary, native_balance ,resource,resource_path,ctype,updated_at): # initialize   
        self.Balance = balance
        self.CreatedAt = created_at # by declaring self.var makes this global 
        self.Currency = currency
        self.Id = cid
        self.Name = name
        self.Primary = primary
        self.NativeBalance = native_balance
        self.Resource = resource
        self.ResourcePath = resource_path
        self.Type = ctype
        self.UpdatedAt = updated_at
        
    # RETURN VARIABLES ONLY
    def returnBalance(self):
        return self.Balance
    def returnCurrency(self):
        return self.Currency
    def returnId(self):
        return self.Id
    def returnName(self):
        return self.Name
    def returnNativeBalance(self):
        return self.NativeBalance
    def returnType(self):
        return self.Type




    def printBalance(self):
        return self.Balance + "\n"
    def printGBPBalance(self):
        return self.Balance + " " + self.NativeBalance + "\n"
    def printID(self):
        return self.Id + " " + self.Currency + "\n"
    def printAll(self):
        return self.Balance + " " + self.CreatedAt + " " + self.Currency + " " + self.Id + " " + self.Name + " " + self.Primary + " " + self.NativeBalance + " " + self.Resource + " " + self.ResourcePath + " " + self.Type + " " + self.UpdatedAt + " " +  "\n"
    
