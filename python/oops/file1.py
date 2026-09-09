class Emp:
    def __init__(self:Emp,emp_name:str,emp_id:int,salary:float) -> None:
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.salary = salary

    def display_data(self:Emp) -> None :
        print(f'Employee ID : {self.emp_id}\nEmployee Name : {self.emp_name}\nEmployee Salary : {self.salary}')

def main() -> None:
    obj = Emp('Mukesh',511,100000.00)
    obj.display_data()

if __name__ == "__main__":
    main()
