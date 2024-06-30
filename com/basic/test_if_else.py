def check_score(score):
    if score < 60:
        print("不及格")
    elif score < 70:
        print("刚刚及格")
    elif score < 80:
        print("中等")
    elif score < 90:
        print("良好")
    elif score < 100:
        print("优秀")
    else:
        print("满分")


check_score(59)
