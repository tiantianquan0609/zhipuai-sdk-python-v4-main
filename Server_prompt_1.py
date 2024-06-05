from zhipuai import ZhipuAI
client = ZhipuAI(
    api_key='',#填写APIkey
)

#多轮对话
print('请问有什么能帮到您？')
prompt="作为制造业顾问，您的任务是根据企业提供的数据撰写详细的报告，包括当前设备状况的评估和提升建议。企业名称和设备诊断信息将在对话中提供。以下是企业装备能力的评估模板：企业名：<input>…插入企业名…</input>企业装备能力评估结果（1）现状<input>…插入当前设备状况的详细信息…</input>（2）提升建议<input>…插入提升建议的详细信息…</input>请提供以下方面的详细分析和建议：当前设备和自动化状态的评估及其对生产效率的影响。设备维护模式的评估及其改进建议。数据采集和联网的提升潜力。可行的设备改造和数据分析建议。设备工艺知识库的建立和应用。您先开始！请发送您的第一条消息并等待我的回复！"

while True:
    user_input = input("你: ")

    if user_input.lower() in ['退出', 'exit', 'quit']:
        print("对话结束。再见！")
        break

    response = client.chat.completions.create(
        model="glm-4",
        messages=[
            {'role': "user", "content": user_input},
            {'role': "system", "content": prompt},
        ],
        stream=True,
    )

    data_content = ""
    char_count = 0

    print("AI: ", end='')

    for chunk in response:
        data_content = chunk.choices[0].delta.content
        for char in data_content:
            char_count += 1
            if char_count >= 200:
                print()
                char_count = 0
        print(data_content, end='')

    print()  # 确保每次响应后换行
