#Question-2
class Mobile:
 
  countryCodes = {"880": "Bangladesh", "966": "India", "455": "USA"}
 
  def __init__(self, model, simCardStatus):
    self.model = model
    self.__simCardStatus = simCardStatus
    print(f"Model {model} is manufactured.")
 
  def setSimCardStatus(self,status):
    self.__simCardStatus = status
    print("SIM card status updated successfully.")
  
  def getSimCardStatus(self):
    return self.__simCardStatus

  def __str__(self):
    return f"Mobile Phone Detail:\nModel: {self.model}\nSIM Card Status: {self.__simCardStatus}"


class Nokia(Mobile):
  def __init__(self, model, simCardStatus, balance=0):
    super().__init__(model, simCardStatus)
    self.balance = balance
    self.dialCallHistory = []
    print(f"Model {model} is manufactured.")

  def __str__(self):
    return f"{super().__str__()}\nBalance: {self.balance}"

  def rechargeSIMCard(self, amount):
    self.balance += amount
    print("SIM card recharged successfully.")
  
  def dialCall(self, number):
    if self.getSimCardStatus() is False:
      return "SIM card is not inserted."
    if self.balance < 1:
      return "Insufficient balance."
    if number[0:3] not in Mobile.countryCodes:
      return "Dialing is not allowed in this region."
    self.dialCallHistory.append(number)
    return f"Dialing the number {number} to {Mobile.countryCodes[number[0:3]]} region."

  

# Driver Code
N3110 = Nokia("N3110", False)
print(N3110)
print("1=================================")
N1100 = Nokia("N1100", True,100)
print(N1100)
print("2=================================")
print(N3110.dialCall("88017196xxxx"))
print("3=================================")
N3110.setSimCardStatus(True)
print("4=================================")
print(N3110.dialCall("88017196xxxx"))
print("5=================================")
N3110.rechargeSIMCard(200)
print("6=================================")
print(N3110.dialCall("88017196xxxx"))
print("7=================================")
print(N1100.dialCall("45617196xxxx"))
print("8=================================")
print(N1100.dialCall("45517196xxxx"))
print(N1100.dialCall("96617196xxxx"))
print("9=================================")
print(f"Dial call history for {N1100.model}: {N1100.dialCallHistory}")
print(f"Dial call history for {N3110.model}: {N3110.dialCallHistory}")