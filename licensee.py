class Person:
    def __init__(self, name: str, personal_id: str = "000"):
        self.name = name
        self.personal_id = personal_id

    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name: str) -> None:
        self.name = name

    def get_id(self) -> str:
        return self.personal_id

class Licensee(Person):
    def __init__(self, name: str, personal_id: str = "000"):
        super().__init__(name, personal_id)
        self.sex_offender = False

    def get_sex_offender(self) -> bool:
        return self.sex_offender
    
    def set_sex_offender(self, status: bool) -> None:
        self.sex_offender = status

#class Licensee:
    #def __init__(self, name: str, licensee_id: str) -> None:
        #self.__name = name
        #self.__licensee_id = licensee_id
        #self.__sex_offender = False

    #def get_name(self) -> str:
        #return self.__name
    
    #def set_name(self, name: str) -> None:
        #self.__name = name
    
    #def get_licensee_id(self) -> str:
        #return self.__licensee_id
    
    #def set_licensee_id(self, licensee_id: str) -> None:
        #self.__licensee_id = licensee_id

    #def get_sex_offender(self) -> bool:
        #return self.__sex_offender
    
    #def set_sex_offender(self, status: bool) -> None:
        #self.__sex_offender = status


