#! /usr/bin/python
# -*- coding: utf-8 -*-

# サブプロセスを起動して、パイプでつなぐサンプル
# Kunimtsu Aran

import os
import sys
import signal
import subprocess

if __name__ == "__main__":
	print u"子プロセス起動"
	# $ cat - をサブプロセスとして起動
	# cat の stdin, stdout がそれぞれ SubPro.stdout, SubPro.stdin とつながる
	SubPro = subprocess.Popen( ["cat", "-"],
								stdout     = subprocess.PIPE,
								stdin      = subprocess.PIPE,
								shell      = True,
								preexec_fn = os.setsid )
	
	# 試しに、子プロセスに文字列を書き込んでみる
	for count in [1,2,3,4,5,6,7,8,9]:
		SubPro.stdin.write( "%d\n" % (count,) )
		while(1):
			data = SubPro.stdout.read(1)
			if data=='\n':
				sys.stdout.write(data)
				break
			else:
				sys.stdout.write('cat : ')
				sys.stdout.write(data)
	# 使い終わったら、サブプロセスを殺す
	else:
		os.killpg(SubPro.pid, signal.SIGTERM)
	
	print u"子プロセス終了"
