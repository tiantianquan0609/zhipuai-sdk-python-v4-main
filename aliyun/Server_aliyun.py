from http import HTTPStatus
import dashscope

dashscope.api_key = "sk-6cfb62b1810242bfab7fc893db65fb87"

from dashscope import Generation

def get_response(messages):
    response = Generation.call(model="qwen-turbo",
                               messages=messages,
                               # 将输出设置为"message"格式
                               result_format='message')
    return response


# messages = [{'role': 'system', 'content': '作为制造业顾问，您的任务是根据企业提供的数据撰写详细的报告，包括当前设备状况的评估和提升建议。企业名称和设备诊断信息将在对话中提供。以下是企业装备能力的评估模板：企业名：<input>…插入企业名…</input>企业装备能力评估结果（1）现状<input>…插入当前设备状况的详细信息…</input>（2）提升建议<input>…插入提升建议的详细信息…</input>请提供以下方面的详细分析和建议：当前设备和自动化状态的评估及其对生产效率的影响。设备维护模式的评估及其改进建议。数据采集和联网的提升潜力。可行的设备改造和数据分析建议。设备工艺知识库的建立和应用。您先开始！请发送您的第一条消息并等待我的回复！'}]
messages = [{'role': 'system', 'content': '作为装备领域企业的诊断咨询助手，你需要根据企业对诊断问卷的回答，对企业现状进行总结，并提供提升建议。请注意不能编造未知的企业信息和回答，也不能编造与问卷回答不符的现状。诊断问卷包括以下问题：Q1：生产现场整体的自动化率水平大致是多少？（0%-20%：较差水平，20%-50%：中等水平，50%-100%：良好水平）Q2：生产现场设备数控化率水平大致是多少？（0%-20%：较差水平，20%-50%：中等水平，50%-100%：良好水平）Q3：生产现场数控化设备联网率大致是多少？（0%-20%：较差水平，20%-50%：中等水平，50%-100%：良好水平）Q4：目前设备的国产化率大概有多少？（0%-20%：较差水平，20%-50%：中等水平，50%-100%：良好水平）Q5：目前的设备管理模式如何？出现设备故障如何解决？（A.手动维护模式，B.预测性维护模式，C.智能化维护模式）请参考以下根据企业对问卷回答生成的现状总结和提升建议示例：<example-1><example-input>企业名：贝斯特企业，A1: 20%，A2: 20%，A3: 20%，A4: 20%，A5: A</example-input><example-output>企业名：贝斯特企业企业装备能力评估结果1）现状：企业多数装备已经实现自动化，能够有效地支撑企业产品生产；有着完整的设备改造规划和采购计划，并按照计划每年提升设备的智能化水平；能够基于信息化手段，有效管理设备运行状态，提高设备稳定性。企业目前在锻压机领域已经做到了行业领先地位，客户也都是各行业的领先企业。由于部分事业部的设备都是比较贵重的资产，且在生产过程中起着非常重要的作用，所以对于绝大多数设备都有定期的巡检和维护，设备维护保养情况良好。（2）提升建议：对于关键设备应该进行联网，通过对关键工序设备所建立的数据管理、模拟加工、图形化编程等人机交互功能；应建立关键工序设备的三维模型库；关键工序设备应具有预测性维护功能，而不是已经出现问题在报警提示维修；关键工序设备还应具有远程监测和远程诊断功能，可以实现故障预警。</example-output></example-1><example-2><example-input>企业名：某电子公司，A1: 50%，A2: 50%，A3: 50%，A4: 50%，A5: B</example-input><example-output>企业名：某电子公司企业装备能力评估结果（1）现状：关键工序基本使用了数控装备，数控装备具备联网功能，数控设备具备联网条件，设备面板可对异常进行提醒。部分设备实现了联网，实现了实时数据监控，但联网比例不高，仅占3%。江扬电缆的装备基本为数控设备，一些老旧设备也可以通过改造实现设备联网。但自动化设备及机器人的运用不多，搬运、流转、仓储方面的装备自动化程度较低，仍依靠人工，劳动强度较大。（2）提升建议：建议对搬运、工序流转、仓储等方面提升装备水平，降低员工劳动强度，提高生产效率。</example-output></example-2>以下是需要处理的信息，围绕在 input 标签内：<input>企业名：xxx，A1: ，A2: ，A3: ，A4: ，A5: </input>请一步一步地解决这个问题。'}]

print('您好！我是您的诊断咨询助手。请您输入企业名称以及装备领域诊断问卷的回答，我将为您提供贵公司装备能力的详细评估结果。')

# 您可以自定义设置对话轮数，当前为3
for i in range(10):
    user_input = input("请输入：")
    messages.append({'role': 'user', 'content': user_input})
    assistant_output = get_response(messages).output.choices[0]['message']['content']
    messages.append({'role': 'assistant', 'content': assistant_output})
    print(f'用户输入：{user_input}')
    print(f'模型输出：{assistant_output}')
    print('\n')