身高=float(input("請輸入身高(公尺)"))
體重=float(input("請輸入體重(公斤)"))
BMI=體重/身高**2
print(BMI)
if BMI<18.5:
    print("體重過輕")
if 18.5<=BMI<24:
    print("健康體位")
if BMI>=24:
    print("體位異常")


# 身高=float(input("請輸入身高(公尺)"))
# 體重=float(input("請輸入體重(公斤)"))
# BMI=體重/身高**2
# print(BMI)
# if BMI<18.5:
#     print("體重過輕")
# elif 18.5<=BMI<24:
#     print("健康體位")
# else:
#     print("體位異常")

