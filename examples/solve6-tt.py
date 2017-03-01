#!/usr/bin/env python
# encoding: UTF-8

from logicmin.tt import TT
from timeit import default_timer as timer

def main():
	t = TT(6,8);

	t.addRow("000000","--11-111")
	t.addRow("000001","10011011")
	t.addRow("000010","10110111")
	t.addRow("000011","00001000")
	t.addRow("000100","11011001")
	t.addRow("000101","00010110")
	t.addRow("000110","1-11-111")
	t.addRow("000111","1-10-111")
	t.addRow("001000","1-11-111")
	t.addRow("001001","11011011")
	t.addRow("001010","11111101")
	t.addRow("001011","11011011")
	t.addRow("001100","10101011")
	t.addRow("001101","10110110")
	t.addRow("001110","10111010")
	t.addRow("001111","011111-1")
	t.addRow("010000","--11-111")
	t.addRow("010001","10011010")
	t.addRow("010010","10110110")
	t.addRow("010011","00001001")
	t.addRow("010100","11011011")
	t.addRow("010101","00010100")
	t.addRow("010110","1-11----")
	t.addRow("010111","1-10----")
	t.addRow("011000","1-11-11-")
	t.addRow("011001","11011011")
	t.addRow("011010","11111111")
	t.addRow("011011","11011011")
	t.addRow("011100","10111110")
	t.addRow("011101","10110111")
	t.addRow("011110","10111011")
	t.addRow("011111","01111101")
	t.addRow("100000","--11-111")
	t.addRow("100001","10011011")
	t.addRow("100010","10110111")
	t.addRow("100011","00001000")
	t.addRow("100100","11011001")
	t.addRow("100101","00010100")
	t.addRow("100110","1-11-11-")
	t.addRow("100111","1-10-11-")
	t.addRow("101000","1-11-11-")
	t.addRow("101001","11011011")
	t.addRow("101010","11111101")
	t.addRow("101011","11011011")
	t.addRow("101100","10111111")
	t.addRow("101101","10110110")
	t.addRow("101110","10111010")
	t.addRow("101111","011111-1")
	t.addRow("110000","--11-111")
	t.addRow("110001","10011010")
	t.addRow("110010","10110110")
	t.addRow("110011","00001001")
	t.addRow("110100","11011011")
	t.addRow("110101","00010100")
	t.addRow("110110","1-11----")
	t.addRow("110111","1-10----")
	t.addRow("111000","1-11-11-")
	t.addRow("111001","11011011")
	t.addRow("111010","00111111")
	t.addRow("111011","010---11")
	t.addRow("111100","10111110")
	t.addRow("111101","10110111")
	t.addRow("111110","10111111")
	t.addRow("111111","01111101")

	start = timer()
	sols = t.solve()
	end = timer()

	sols.printN()

	print "Solved in %f s." % (end-start)


if __name__ == "__main__":
    main()
