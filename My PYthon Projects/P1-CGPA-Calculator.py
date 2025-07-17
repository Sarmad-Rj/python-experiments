class CGPA_CALC:
    def __init__(self, sems, GPAs):
        self.sems = sems
        self.GPAs = GPAs

    def calc(self):
        CGPA = sum(self.GPAs) / self.sems
        print(f"Your CGPA is {CGPA:.2f}")

def main():
    print("~" * 50)
    total_semesters = int(input("Enter your total semesters: "))
    GPAs = []
    for i in range(total_semesters):
        gpa = float(input(f"Enter GPA of Semester {i + 1}: "))
        GPAs.append(gpa)
    calc = CGPA_CALC(total_semesters, GPAs)
    calc.calc()
    print("~" * 50)

if __name__ == "__main__":
    main()
