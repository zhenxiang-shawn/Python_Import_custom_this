"""
This is my custom import this. This statement has been used ROT13 to encode.

Author: Zhenxiang Jin (zhenxiang.shawn@zohomail.com)
"""
import codecs

my_state = (
    "Guvf vf zl phfgbz vzcbeg guvf. Lbh pna hfr vg gb fubj lbhe fgngrzrag sbe "
    "lbhe yvoenel. Nhgube: Murakvnat Wva. Vs lbh yvxr guvf, cyrnfr fgne guvf "
    "ercb.")


def print_my_state():
    print(codecs.decode(my_state, 'rot_13'))


print_my_state()
