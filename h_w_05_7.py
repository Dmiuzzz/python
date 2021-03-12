import json
with open("firm_base.txt", "r") as firm_base:
    content = firm_base.readlines()
    profit = 0
    av_profit = 0
    num_f = 0
    dic_ap = {}
    dic_fp = {}
    dic_fl = {}
    final_l = []
    for el in content:
        el = el.split()
        profit = int(el[2]) - int(el[3])
        if profit >= 0:
            dic_fp[el[0]] = profit
            av_profit += profit
            num_f += 1
        else: dic_fl[el[0]] = profit
    final_l.append(dic_fp)
    dic_ap["average_profit"] = av_profit/num_f
    final_l.append(dic_ap)
    final_l.append(dic_fl)



print(final_l)

with open("firm_base.json", "w") as write_f:
    json.dump(final_l, write_f)

