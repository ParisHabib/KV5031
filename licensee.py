class Person:
    def __init__(self, name: str, notes: str, personal_id: str = "000"):
        self.name = name
        self.personal_id = personal_id
        self.notes = notes

    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name: str) -> None:
        self.name = name

    def get_id(self) -> str:
        return self.personal_id
    
    def set_id(self, personal_id: str) -> None:
        self.personal_id = personal_id

    def get_notes(self) -> str:
        return self.notes
    
    def set_notes(self, notes: str) -> None:
        self.notes = notes

class Licensee(Person):
    def __init__(self, name: str, notes: str, home_address: str, prisoner_gender: str, release_date: str, end_of_license: str, current_prison: str, personal_id: str = "000"):
        super().__init__(name, notes, personal_id)
        self.sex_offender = False
        self.needed_drug_search = False
        self.home_address = home_address
        self.prisoner_gender = prisoner_gender
        self.release_date = release_date
        self.end_of_license = end_of_license
        self.current_prison = current_prison

    def get_sex_offender(self) -> bool:
        return self.sex_offender
    
    def set_sex_offender(self, status: bool) -> None:
        self.sex_offender = status

    def get_needed_drug_search(self) -> bool:
        return self.needed_drug_search
    
    def set_needed_drug_search(self, status: bool) -> None:
        self.needed_drug_search = status

    def get_home_address(self) -> str:
        return self.home_address
    
    def set_home_address(self, home_address: str) -> None:
        self.home_address = home_address

    def get_prisoner_gender(self) -> str:
        return self.prisoner_gender
    
    def set_prisoner_gender(self, prisoner_gender: str) -> None:
        self.prisoner_gender = prisoner_gender

    def get_release_date(self) -> str:
        return self.release_date
    
    def set_release_date(self, release_date: str) -> None:
        self.release_date = release_date

    def get_end_of_license(self) -> str:
        return self.end_of_license
    
    def set_end_of_license(self, end_of_license: str) -> None:
        self.end_of_license = end_of_license

    def get_current_prison(self) -> str:
        return self.current_prison
    
    def set_current_prison(self, current_prison: str) -> None:
        self.current_prison = current_prison

class Officer(Person):
    def __init__(self, name: str, notes: str, personal_id: str ="000"):
        super().__init__(name, notes, personal_id)

class Rehabilitation_Housing_Unit:
    def __init__(self, RHU_name: str, RHU_notes: str, unit_address: str):
        self.RHU_name = RHU_name
        self.RHU_notes = RHU_notes
        self.unit_address = unit_address
        self.within_school_distance = False

    def get_RHU_name(self) -> str:
        return self.RHU_name
    
    def set_RHU_name(self, RHU_name: str) -> None:
        self.RHU_name = RHU_name

    def get_RHU_notes(self) -> str:
        return self.RHU_notes
    
    def set_RHU_notes(self, RHU_notes: str) -> None:
        self.RHU_notes = RHU_notes

    def get_unit_address(self) -> str:
        return self.unit_address
    
    def set_unit_address(self, unit_address: str) -> None:
        self.unit_address = unit_address
   
    def get_within_school_distance(self) -> bool:
        return self.within_school_distance
    
    def set_within_school_distance(self, status: bool) -> None:
        self.within_school_distance = status

