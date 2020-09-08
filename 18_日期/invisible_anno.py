import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# ---------- 数据预处理 ----------
file_path = './test.csv'
df_all = pd.DataFrame(pd.read_csv(file_path, encoding='utf-8'))
df_all = df_all.set_index(pd.DatetimeIndex(pd.to_datetime(df_all.time)))

print(df_all)
x = df_all['time']
y1 = df_all['data']

y2 = df_all["buy"]
y3 = df_all["sell"]
y_condition = list(df_all["操作"])

text1 = []
for i in range(len(x)):
    if (df_all['操作'][i] != 0) and (df_all['操作'][i] == "买"):
        str_info = '价格: ' + str(df_all['价格'][i]) + '\n' + '数量: ' + str(df_all['数量'][i]) + '\n' + '操作: ' + str(df_all['操作'][i])
        text1.append(str_info)
    else:
        text1.append(" ")
text2 = []
for i in range(len(x)):
    if (df_all['操作'][i] != 0) and (df_all['操作'][i] == "卖"):
        str_info = '价格: ' + str(df_all['价格'][i]) + '\n' + '数量: ' + str(df_all['数量'][i]) + '\n' + '操作: ' + str(df_all['操作'][i])
        text2.append(str_info)
    else:
        text2.append(" ")

print(text2)
# ---------- 画图 ----------
fig, ax = plt.subplots()

# 折线图
ax.plot(x, y1, color='royalblue', lw=2.5, label='data')
# 折线图上的散点
ax.scatter(x, y2, marker='o', c='darkgreen', label='买')
ax.scatter(x, y3, marker='o', c='firebrick', label='卖')

# 一些小设置
# 设置 x 轴显示密度
tick_spacing = 8
ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
# 设置 x 坐标轴标签的显示内容和大小
plt.xlabel('时间', fontsize=16)
# 设置 x 坐标轴刻度的旋转方向和大小
plt.xticks(rotation=90, fontsize=16)
# 设置 y 坐标轴刻度大小
plt.yticks(fontsize=18)
# 坐标轴中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
# 调整图的位置
plt.subplots_adjust(top=0.9, bottom=0.22)
# 设置尺寸
fig.set_size_inches(24, 12)

# po_annotation1 为 ‘买’ 时需要显示的标注信息
# 该 list 内部存放多个子 list，每个子 list 为 [标注点的坐标, 标注]
po_annotation1 = []
for i in range(len(x)):
    # 标注点的坐标
    point_x = x[i]
    point_y = y2[i]
    point, = plt.plot(point_x, point_y, 'o', c='darkgreen')
    # 标注框偏移量
    offset1 = 80
    offset2 = 80
    # 标注框
    bbox1 = dict(boxstyle="round", fc='lightgreen', alpha=0.6)
    # 标注箭头
    arrowprops1 = dict(arrowstyle="->", connectionstyle="arc3,rad=0.")
    # 标注
    annotation = plt.annotate(text1[i], xy=(x[i], y2[i]), xytext=(-offset1, offset2), textcoords='offset points',
                              bbox=bbox1, arrowprops=arrowprops1, size=15)
    # 默认鼠标未指向时不显示标注信息
    annotation.set_visible(False)
    po_annotation1.append([point, annotation])

po_annotation2 = []
for i in range(len(x)):
    # 标注点的坐标：
    point_x = x[i]
    point_y = y3[i]
    point, = plt.plot(point_x, point_y, 'o', c='firebrick')
    # 标注框偏移量
    offset1 = 30
    offset2 = 80
    # 标注框
    bbox2 = dict(boxstyle="round", fc='salmon', alpha=0.6)
    # 标注箭头
    arrowprops2 = dict(arrowstyle="->", connectionstyle="arc3,rad=0.")
    # 标注
    annotation = plt.annotate(text2[i], xy=(x[i], y3[i]), xytext=(-offset1, offset2), textcoords='offset points',
                              bbox=bbox2, arrowprops=arrowprops2, size=15)
    # 默认鼠标未指向时不显示标注信息
    annotation.set_visible(False)
    po_annotation2.append([point, annotation])


# 定义鼠标响应函数
def on_move(event):
    visibility_changed = False
    for point, annotation in po_annotation1:
        should_be_visible = (point.contains(event)[0] == True)

        if should_be_visible != annotation.get_visible():
            visibility_changed = True
            annotation.set_visible(should_be_visible)

    for point, annotation in po_annotation2:
        should_be_visible = (point.contains(event)[0] == True)

        if should_be_visible != annotation.get_visible():
            visibility_changed = True
            annotation.set_visible(should_be_visible)

    if visibility_changed:
        plt.draw()


# 鼠标移动事件
on_move_id = fig.canvas.mpl_connect('motion_notify_event', on_move)
plt.show()