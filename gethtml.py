from bs4 import BeautifulSoup
import os
import datetime

# 解析 HTML 文件夹
html_folder = "/Users/user/Downloads/公众号罗斯基"  # 修改为你的 HTML 目录
output_file = "testoutput.txt"  # 输出文件

# 打开输出文件
with open(output_file, "w", encoding="utf-8") as out_file:
    for filename in os.listdir(html_folder):
        if filename.endswith(".html"):
            file_path = os.path.join(html_folder, filename)

            # 读取 HTML 内容
            with open(file_path, "r", encoding="utf-8") as f:
                html_content = f.read()

            # 解析 HTML
            soup = BeautifulSoup(html_content, "html.parser")

            # 获取标题
            title_tag = soup.find("title")
            title = title_tag.text.strip() if title_tag else "未找到标题"

            # 提取纯文本内容并处理空格
            content = soup.get_text(separator=' ')  # 使用单个空格作为分隔符
            # 去除多余空格
            content = ' '.join(filter(None, content.split()))

            # 从文件名提取日期
            date_str = filename[:8]
            try:
                date = datetime.datetime.strptime(date_str, "%Y%m%d").date()
            except ValueError:
                date = "未知日期"

            # 写入文件
            out_file.write("=" * 80 + "\n")
            out_file.write(f"文件名: {filename}\n")
            out_file.write(f"日期: {date}\n")
            out_file.write(f"标题: {title}\n")
            out_file.write(f"内容预览: {content}...\n")  # 只显示前 500 字
            out_file.write("=" * 80 + "\n\n")

print("解析完成，结果已保存到 testoutput.txt")