import random

host = ''' 招呼 = 你好
自我介绍 = 介绍名字 , 介绍职业 , 介绍爱好 
询问对方 = 称呼对方 是 who | 称呼对方 什么名字
介绍名字 = 自称 是 名字
介绍职业 = 名字 是 一 量词-人 职业
介绍爱好 = 喜爱 爱好
喜爱 = 喜欢 | 平时喜欢 | 常常
爱好 = 煮汤 | 游历 | 洗澡 
自称 = 我
称呼对方 = 你
who = 哪一位 | 谁
什么名字 = 叫什么名字 | 叫什么
量词-人 = 个 | 位 | 名
'''


abu_info = '''frist_line = 招呼 , 自我介绍 , 我需要你的能力,你会帮助我救回我们的国王吗？
招呼 = 哦天，你来了这里 | 你终于来了 | 客人 , 我等你很久了
自称 = 我 | 在下 
称呼对方 = 阁下 | 客人
名字 = 阿不
职业 = 女巫
爱好 = 煮汤 | 游历
'''

dayou_info = '''frist_line = 招呼 , 自我介绍 , 询问对方 ?
招呼 = 你好 | 很高兴见到你 | 招呼
自称 = 我
称呼对方 = 您 | 你
名字 = 大游
职业 = 科学家
喜爱 = 喜欢 | 每天
爱好 = 推公式 | 计算太阳的起落
'''


def generate_grammar(grammar_define):
    grammar_pattren = {}
    pattern_list = grammar_define.split('\n')
    for line in pattern_list:
        if not line: continue
        key,content = line.split('=')
        key = key.strip()
        content = content.split('|')
        grammar_pattren[key] = content
        grammar_pattren[key] = [r.split() for r in content]
    return grammar_pattren


def grammar4person(grammar_define, person_info):
    grammar_pattern = generate_grammar(grammar_define)
    person_pattern = generate_grammar(person_info)
    return dict(list(grammar_pattern.items()) + list(person_pattern.items()))


def generate(grammar_pattern, target):
    if target not in grammar_pattern: return target
    sub_target = random.choice(grammar_pattern[target])
    return ''.join(generate(grammar_pattern, r) for r in sub_target)


abu_pattern = grammar4person(host, abu_info)
dayou_pattern = grammar4person(host, dayou_info)


print('\n','大游：')
print(generate(dayou_pattern, 'frist_line'))



print('\n','阿不：')
print(generate(abu_pattern, 'frist_line'))
