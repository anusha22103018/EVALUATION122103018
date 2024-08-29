#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Student:
    def __init__(self, name, student_class, height, weight, sport, calorie_intake):
        self.name = name
        self.student_class = student_class
        self.height = height
        self.weight = weight
        self.sport = sport
        self.calorie_intake = calorie_intake

    def calculate_bmi(self):
     
        height_m = self.height / 100  
        bmi = self.weight / (height_m ** 2)
        return bmi

    def determine_diet_status(self):
        bmi = self.calculate_bmi()
        calorie_requirement = 25 * self.weight 
        
 
        if bmi < 18.5:
            bmi_status = "Red: Underweight"
        elif 18.5 <= bmi < 24.9:
            bmi_status = "Green: Normal weight"
        else:
            bmi_status = "Orange: Overweight"
        
       
        if self.calorie_intake < calorie_requirement:
            intake_status = "Red: Needs more intake"
        elif self.calorie_intake >= calorie_requirement:
            intake_status = "Green: Sufficient consumption"
        
        return bmi_status, intake_status

    def display_student_info(self):
        bmi_status, intake_status = self.determine_diet_status()
        print(f"Student Name: {self.name}")
        print(f"Class: {self.student_class}")
        print(f"Height: {self.height} cm")
        print(f"Weight: {self.weight} kg")
        print(f"Sport Interested: {self.sport}")
        print(f"Calorie Intake: {self.calorie_intake} kcal")
        print(f"BMI Status: {bmi_status}")
        print(f"Diet Status: {intake_status}")

def main():
    students = {}
    

    students["01"] = Student("Anusha", "A", 160, 50, "Basketball", 2000)
    students["02"] = Student("Brijesh", "B", 175, 70, "Soccer", 2500)
    students["03"] = Student("Chandan", "C", 180, 90, "Swimming", 3000)
    

    for student_id, student in students.items():
        print(f"\nStudent ID: {student_id}")
        student.display_student_info()

if __name__ == "__main__":
    main()


# In[ ]:




