def main():
    # 用字典存储所有学生信息，键为学号，值为包含姓名和成绩列表的字典
    students = {}

    while True:
        print("\n===== 学生成绩管理系统 =====")
        print("1. 录入学生成绩")
        print("2. 查询学生信息")
        print("3. 统计所有学生各科成绩（平均分、最高分、最低分）")
        print("4. 退出系统")
        choice = input("请选择操作 (1-4): ")

        if choice == '1':
            # 录入学生信息
            sid = input("请输入学号: ").strip()
            if sid in students:
                print("该学号已存在，请使用查询或修改功能。")
                continue
            name = input("请输入姓名: ").strip()
            # 输入各科成绩，用列表存储
            scores = []
            subjects = ["语文", "数学", "英语"]
            for subject in subjects:
                while True:
                    try:
                        score = float(input(f"请输入{subject}成绩: "))
                        if 0 <= score <= 100:
                            scores.append(score)
                            break
                        else:
                            print("成绩应在0-100之间，请重新输入。")
                    except ValueError:
                        print("请输入有效的数字。")
            students[sid] = {"name": name, "scores": scores}
            print(f"学生 {name} 的成绩已录入。")

        elif choice == '2':
            # 查询学生信息
            if not students:
                print("系统中暂无学生信息。")
                continue
            sid = input("请输入要查询的学号: ").strip()
            if sid in students:
                stu = students[sid]
                print(f"学号: {sid}, 姓名: {stu['name']}")
                subjects = ["语文", "数学", "英语"]
                for i, sub in enumerate(subjects):
                    print(f"  {sub}: {stu['scores'][i]}")
            else:
                print("未找到该学号的学生。")

        elif choice == '3':
            # 统计所有学生的各科成绩
            if not students:
                print("系统中暂无学生信息，无法统计。")
                continue

            # 初始化各科成绩列表
            chinese_scores = []
            math_scores = []
            english_scores = []

            # 遍历所有学生，收集各科成绩
            for stu in students.values():
                # 成绩按顺序：索引0语文，1数学，2英语
                chinese_scores.append(stu['scores'][0])
                math_scores.append(stu['scores'][1])
                english_scores.append(stu['scores'][2])

            # 定义一个函数来计算统计值
            def calc_stats(scores, subject_name):
                avg = sum(scores) / len(scores)
                max_score = max(scores)
                min_score = min(scores)
                print(f"{subject_name} - 平均分: {avg:.2f}, 最高分: {max_score}, 最低分: {min_score}")

            print(f"\n共有 {len(students)} 名学生，各科成绩统计如下：")
            calc_stats(chinese_scores, "语文")
            calc_stats(math_scores, "数学")
            calc_stats(english_scores, "英语")

        elif choice == '4':
            print("感谢使用学生成绩管理系统，再见！")
            break

        else:
            print("无效的选择，请输入1-4之间的数字。")

if __name__ == "__main__":
    main()