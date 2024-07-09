# 가변인자
# def profile(name, age, lang1, lang2, lang3 ,lang4, lang5):
#     print("이름 : {}\t나이: {}\t".format(name,age), end="")
#     print(lang1, lang2, lang3,lang4,lang5)

def profile(name, age, *language):
    print("이름 : {}\t나이: {}\t".format(name, age), end="")
    for lang in language:
        print(lang, end="")
    print()
    

print("유재석", 25, "python", "java", "c", "c++", "C#","javascript")
print("김태호", 20, "kotlin", "swift")
