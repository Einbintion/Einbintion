import re

def reg_search(text, regex_list):
    results = []
    for regex_dict in regex_list:
        temp_result = {}
        for key, pattern in regex_dict.items():
            matches = re.findall(pattern, text)
            if matches:
                if len(matches) == 1:
                    temp_result[key] = matches[0]
                else:
                    temp_result[key] = matches
        results.append(temp_result)
    return results


text = '''
标的证券：本期发行的证券为可交换为发行人所持中国长江电力股份
有限公司股票（股票代码：600900.SH，股票简称：长江电力）的可交换公司债券。
换股期限：本期可交换公司债券换股期限自可交换公司债券发行结束
之日满 12 个月后的第一个交易日起至可交换债券到期日止，即 2023 年 6 月 2
日至 2027 年 6 月 1 日止。
'''

regex_list = [
    {
        '标的证券': r'股票代码：(\S+?)，',
        '换股期限': r'\b(\d{4} 年 \d{1,2} 月 \d{1,2} 日)'
    }
]

result = reg_search(text, regex_list)
print(result)
