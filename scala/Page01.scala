print("hi scala!")
print(3+2)
print(1==2)


val input = "Enjoying this apple 3.14159 times today"
val pattern = """.* apple ([\d.]+) times .*""".r
val pattern(amoutText) = input
