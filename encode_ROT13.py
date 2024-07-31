"""
This file helps you to encode your statement.

Author: Zhenxiang Jin (zhenxiang.shawn@zohomail.com)
"""

import codecs

# 原始字符串
original_text = ("This is my custom import this. You can use it to show your "
                 "statement for your library. Author: Zhenxiang Jin. "
                 "If you like this, please star this repo.")

# 使用 ROT13 编码
encoded_text = codecs.encode(original_text, 'rot_13')

# 打印编码后的字符串
print("Encoded with ROT13:", encoded_text)
print("Decoded with ROT13:", codecs.decode(encoded_text, 'rot_13'))
