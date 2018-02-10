#!/usr/bin/env python
# encoding: UTF-8

import logicmin

t = logicmin.TT(4,6);

t.addRow("0000","--11-1")
t.addRow("0001","100110")
t.addRow("0010","101101")
t.addRow("0011","000010")
t.addRow("0100","110110")
t.addRow("0101","000101")
t.addRow("0110","1-11-1")
t.addRow("0111","1-10-1")
t.addRow("1000","1-11-1")
t.addRow("1001","110110")
t.addRow("1010","111111")
t.addRow("1011","110110")
t.addRow("1100","101111")
t.addRow("1101","101101")
t.addRow("1110","101110")
t.addRow("1111","011111")

sols = t.solve()
print sols.printN()


