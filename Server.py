from zhipuai import ZhipuAI
client = ZhipuAI(
    api_key='',#填写APIkey
)

#单轮对话
# print('请问有什么能帮到您？\n')
# user_input = input()
# reponse = client.chat.completions.create(
#     model="glm-4",
#     messages=[
#         {'role':"user","content":user_input},
#     ],
#     stream = True,
# )
#
# data_content = ""
# char_count = 0
# for  chunk in reponse:
#     data_content = chunk.choices[0].delta.content
#     for char in data_content:
#         char_count +=1
#         if char_count >= 200:
#             print()
#             char_count = 0
#     print(data_content, end='')

#多轮对话
print('请问有什么能帮到您？')

while True:
    user_input = input("你: ")

    if user_input.lower() in ['退出', 'exit', 'quit']:
        print("对话结束。再见！")
        break

    response = client.chat.completions.create(
        model="glm-4",
        messages=[
            {'role': "user", "content": user_input},
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