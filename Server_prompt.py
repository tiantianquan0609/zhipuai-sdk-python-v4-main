import zhipuai

client = zhipuai.ZhipuAI(api_key='')

print('您好！我是您的诊断咨询助手。请您输入企业名称以及装备领域诊断问卷的回答，我将为您提供贵公司装备能力的详细评估结果。')

# 初始化对话历史
# conversation_history = [
#     {'role': "system", "content": "请记住以下信息：我是陆星辰，是一个男性，是一位知名导演，也是苏梦远的合作导演。我擅长拍摄音乐题材的电影。苏梦远对我的态度是尊敬的，并视我为良师益友。苏梦远，本名苏远心，是一位当红的国内女歌手及演员。在参加选秀节目后，凭借独特的嗓音及出众的舞台魅力迅速成名，进入娱乐圈。她外表美丽动人，但真正的魅力在于她的才华和勤奋。"}
# ]
# conversation_history = [
#     {'role': "system", "content": "你是一个装备领域企业的诊断咨询助手，你需要根据企业对装备领域诊断问题的回答，来对企业装备现状形成一段总结，并针对企业现状精炼出一段提升建议。企业在装备领域诊断问题的答案会在下面的对话中输入。如下是装备领域诊断问题的问卷，共5个问题：Q1：生产现场整体的自动化率水平大致是多少？0-20--等级差 20-50--等级中 50-100--等级好 Q2：生产现场设备数控化率水平大致是多少？ 0-20--等级差 20-50--等级中 50-100--等级好 Q3：生产现场数控化设备联网率大致是多少？0-20--等级差 20-50--等级中 50-100--等级好 Q4：目前设备的国产化率大概有多少？ 0-20--等级差 20-50--等级中 50-100--等级好 Q5：目前的设备管理模式如何？出现设备故障如何解决？ A.手动维护模式 (小型或刚起步的制造业企业可能采用手动维护模式，设备管理主要依靠人工巡检和维护);设备故障出现时，通常由现场操作人员或维修工程师进行处理。维修可能需要暂停生产，并根据现场情况进行修复或更换故障部件。B.预测性维护模式 (利用数据分析和监控技术对设备进行实时监测和预测，以预测设备故障并提前进行维护);在预测性维护模式下，企业会利用设备数据和监控系统实时监测设备状态，一旦发现异常，会立即采取预防性维护措施，以避免设备故障造成的生产中断。C.智能化维护模式 (部分大型制造业企业采用智能化维护模式，结合物联网、大数据和人工智能等技术，实现设备的智能监测、预测和维护);在智能化维护模式下，企业通过设备数据分析和预测模型实时监测设备状态，并自动化地进行维护决策和控制。一旦发现异常，系统会自动触发维护流程，甚至自动下发维护指令给相关人员或系统。如下是某企业在装备能力方面的现状总结和提升建议，可供参考：1. 装备能力评估结果 （1）现状 贝昂车间内有三条自动化装配线和 12 套生产设备，8台设备有 PLC 和数据接口，基本具备进行设备联网数据采集条件，目前还未进行设备联网采集操作。企业设备维护过程缺少记录和跟踪，没有形成规律性维护模式。设备通过固定的巡查和定期的维修进行维护管理，并以故障发生作为维修的主要驱动。设备维护主要通过坏了再修的方式进行。2）提升建议建议条件允许的情况下对设备进行改造，加装传感器，采集必要数据，建议加强设备的数据分析处理能力，建立规范设备工艺知识库，为后续的工艺改进提供充分的参考和借鉴。"}
# ]
# conversation_history = [
#     {'role': "system", "content": "作为装备领域企业的诊断咨询助手，你的任务是根据企业对诊断问卷的问题回答，总结企业的装备现状，并提供提升建议。以下是诊断问卷及其选项：Q1:生产现场整体的自动化率水平大致是多少？0-20：等级差 20-50：等级中 50-100：等级好 Q2:生产现场设备数控化率水平大致是多少？0-20：等级差 20-50：等级中 50-100：等级好 Q3:生产现场数控化设备联网率大致是多少？0-20：等级差 20-50：等级中 50-100：等级好 Q4:目前设备的国产化率大概有多少？0-20：等级差 20-50：等级中 50-100：等级好 Q5:目前的设备管理模式如何？出现设备故障如何解决？A.手动维护模式 B.预测性维护模式 C.智能化维护模式 请根据以下格式回答总结和建议：<example-1><example-input>企业名：未提供具体回答 Q1:未提供具体回答 Q2:未提供具体回答 Q3:未提供具体回答 Q4:未提供具体回答 Q5:未提供具体回答</example-input><example-output>企业名：xxx 企业装备能力评估结果（1）现状 贝昂车间内有三条自动化装配线和12套生产设备，8台设备有PLC和数据接口，基本具备进行设备联网数据采集条件，目前还未进行设备联网采集操作。企业设备维护过程缺少记录和跟踪，没有形成规律性维护模式。设备通过固定的巡查和定期的维修进行维护管理，并以故障发生作为维修的主要驱动。设备维护主要通过坏了再修的方式进行。（2）提升建议 建议条件允许的情况下对设备进行改造，加装传感器，采集必要数据，建议加强设备的数据分析处理能力，建立规范设备工艺知识库，为后续的工艺改进提供充分的参考和借鉴。</example-output></example-1>"}
# ]
conversation_history = [
    {'role': "system", "content": "作为制造业顾问，您的任务是根据企业提供的数据撰写详细的报告，包括当前设备状况的评估和提升建议。企业名称和设备诊断信息将在对话中提供。以下是企业装备能力的评估模板：企业名：<input>…插入企业名…</input>企业装备能力评估结果（1）现状<input>…插入当前设备状况的详细信息…</input>（2）提升建议<input>…插入提升建议的详细信息…</input>请提供以下方面的详细分析和建议：当前设备和自动化状态的评估及其对生产效率的影响。设备维护模式的评估及其改进建议。数据采集和联网的提升潜力。可行的设备改造和数据分析建议。设备工艺知识库的建立和应用。您先开始！请发送您的第一条消息并等待我的回复！"}
]
# while True:
#     user_input = input("你: ")
#
#     if user_input.lower() in ['退出', 'exit', 'quit']:
#         print("对话结束。再见！")
#         break
#
#     # 将用户输入添加到对话历史
#     conversation_history.append({'role': "user", "content": user_input})
#
#     try:
#         # 调用 API 生成响应
#         response = client.chat.completions.create(
#             model="glm-4",
#             messages=conversation_history,
#             stream=True,
#         )
#
#         data_content = ""
#         char_count = 0
#
#         print("AI: ", end='')
#
#         for chunk in response:
#             if hasattr(chunk.choices[0], 'delta') and hasattr(chunk.choices[0].delta, 'content'):
#                 data_content += chunk.choices[0].delta.content
#                 for char in chunk.choices[0].delta.content:
#                     char_count += 1
#                     if char_count >= 200:
#                         print()
#                         char_count = 0
#                 print(chunk.choices[0].delta.content, end='')
#
#         # 将 AI 的回复添加到对话历史
#         conversation_history.append({'role': "assistant", "content": data_content})
#
#     except Exception as e:
#         print(f"API 请求失败: {e}")
#
#     print()  # 确保每次响应后换行

while True:
    user_input = input("你: ")

    if user_input.lower() in ['退出', 'exit', 'quit']:
        print("对话结束。再见！")
        break

    if not user_input.strip():
        print("输入为空，请重新输入。")
        continue

    # 将用户输入添加到对话历史
    conversation_history.append({'role': "user", "content": user_input})

    try:
        # 调用 API 生成响应
        response = client.chat.completions.create(
            model="glm-4",
            messages=conversation_history,
            stream=True,
        )

        data_content = ""
        char_count = 0

        print("AI: ", end='')

        for chunk in response:
            if hasattr(chunk.choices[0], 'delta') and hasattr(chunk.choices[0].delta, 'content'):
                content = chunk.choices[0].delta.content
                data_content += content
                for char in content:
                    char_count += 1
                    if char_count >= 200:
                        print()
                        char_count = 0
                print(content, end='')

        # 将 AI 的回复添加到对话历史
        conversation_history.append({'role': "assistant", "content": data_content})

    except Exception as e:
        print(f"API 请求失败: {e}")

    print()  # 确保每次响应后换行