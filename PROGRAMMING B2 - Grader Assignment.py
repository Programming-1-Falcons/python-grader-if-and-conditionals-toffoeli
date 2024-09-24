totalpoint=int(input("Total Points: "))
pointgot=int(input("Points Achieved: "))
grade=(pointgot/totalpoint)*100
if grade<=50:
    answer="F"
elif grade>=51 and grade<=60:
    answer="D"
elif grade>=61 and grade<=75:
    answer="C"
elif grade>=76 and grade<=88:
    answer="B"
else:
    answer="A"
print(f"Student got a(n) '{answer}'.")