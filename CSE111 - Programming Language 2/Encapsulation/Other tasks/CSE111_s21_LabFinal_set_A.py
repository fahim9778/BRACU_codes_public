class CodeVault:
  submission_count=0
  project_list=[]
  def __init__(self,name,id,code_info,lang,standard,submission_date):
    self._name=name
    self._id=id
    self._code_info=code_info
    self._language=lang
    self._submission_date=submission_date
    CodeVault.submission_count+=1
    self.project_id="projectid_0000"+str(CodeVault.submission_count)
    self.__standard=standard
    CodeVault.project_list.append(self)

  def change_codeinfo(self,new_info):
    self._code_info = new_info
    print("project info changed!!")

  def change_id(self,new_id):
    self._id=new_id
    print("ALERT! YOUR ID IS CHANGED!!")
  def calculate_project_payment(self, obj): 
    if obj.__standard=="A":
      return 10000
    elif obj.__standard=="B":
      return 5000
    else:
      return 3000
 
  def get_standard(self):
    return self.__standard

  def set_standard(self,val):
    self.__standard=val
  def __str__(self):
    return f"the user's name is : {self._name}\nthe project stored is called: {self._code_info}\nit's written in : {self._language} Language\nSubmitted on : {self._submission_date}"


##WRITE YOUR CODE HERE

class Coder(CodeVault):
    def __init__(self,name,id,password,code_info,lang,standard,submission_date):
        super().__init__(name,id,code_info,lang,standard,submission_date)
        self.__password = password
        print(f"hello {self._name}, thanks for signing in with us!")

    def show_user_info(self, id, password):
        if self._id == id and self.__password == password:
            print(f"hello username: {self._id}, here's your info:\nyour rank is: {self.get_standard()},\n{super().__str__()}")
        else:
            print("sorry you are not the owner of this account")

    def apply_for_promotion(self):
        if self.get_standard() == "A":
            print("you are already the highest coder, no promotion needed")
        elif self.get_standard() == "B":
            self.set_standard("A")
            print("congratulations you are a A grade coder now")

    def get_payment(self):
        if self.get_standard() == "A":
            print(f"hello {self._name} you've stored total of 50000tk worth of payment")
        elif self.get_standard() == "B":
            print(f"hello {self._name} you've stored total of 45000tk worth of payment")
        else:
            print(f"hello {self._name} you've stored total of 3000tk worth of payment")

    @classmethod
    def show_total_users(cls):
        return(f"total users so far: {cls.submission_count}")

##DRIVER CODE
c1= Coder("araf", "araf12", "xyz123", "project_111Lab_cheat", "python 3.0", "B", "20/09/2022")
print("----------------ui----------------------------------------")
c1.show_user_info("araf12","xz23")
print("------------------ui--------------------------------------")
c1.show_user_info("araf12","xyz123")
print("---------------------------------------------------------")
c1.get_payment()
c1.apply_for_promotion()
print("---------------------------------------------------------")
c1.get_payment()
print("---------------------------------------------------------")
c1.change_codeinfo("project_370Lab_cheat")
print("------------------ui--------------------------------------")
c1.show_user_info("araf12","xyz123")
print("---------------------------------------------------------")
c2= Coder("fahim", "fahim12", "abc123", "project_422Lab_cheat", "JAVA", "A", "20/10/2022")
c2.apply_for_promotion()
c2.get_payment()
print("----------------ui----------------------------------------")
c2.show_user_info("fahim12","abc123")
print("----------------------------------------------------------")
c2.change_id("fahim_NEW_ID")
print("----------------ui----------------------------------------")
c2.show_user_info("fahim12","abc123")
print("----------------ui----------------------------------------")
c2.show_user_info("fahim_NEW_ID","abc123")
print(Coder.show_total_users())
