#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import re

def rule_single(tree):
	r1 = re.findall("\(S[\n ]",tree,re.DOTALL)
	if len(r1)==1:									#1s
		r1=re.findall("\(CC(.*)\(PP \((TO|IN) (.*?)\)",tree,re.DOTALL)
		if	r1:										#1s + (CC then (PP (TO/(IN
			return [r1[0][2]]
		else:										#no dm
			return 0
	elif len(r1)>=2:								#2s
		r1=re.findall("\(ADVP \(RB (.*?)\)", tree, re.DOTALL)
		if len(r1)==0:								#2s + no advp ()
			r1=re.findall("SBAR", tree, re.DOTALL)	
			if len(r1)==0:							#2s + no sbar (())
				r1=re.findall("\(CC", tree, re.DOTALL)
				if len(r1)==0:						#2s + no cc   ((()))
					r1 = re.findall("\(IN", tree, re.DOTALL)
					if len(r1)==0:					#2s + no in   ((((-)))) no dm
						return 0
					else:							#2s + in      (((\())))
						r1 = re.findall("\(IN (.*?)\)", tree, re.DOTALL)
						return r1
				else:								#2s +cc 	  ((\()))
					r1 = re.findall("\(CC (.*?)\)", tree, re.DOTALL)
					return r1		
			else:
				r1 = re.findall("\(SBAR(.*)\(IN (.*?)\)", tree, re.DOTALL)
				return [r1[0][1]] 					#2s + sbar    (\())
		else:
			return r1								#2s + advp	  \()
	else:											#no dm
		return 0

def rule_multiple(tree):
	r1=''
	r1=re.findall("\(S", tree, re.DOTALL)
	if len(r1)>=2:									#2s
		r1 = re.findall("\(PP \(IN (.*?)\)(.*?)\)\)", tree, re.DOTALL)
		if r1:										#2s + (S (PP (IN
			r2 = r1[0][1]	
			r2 = r2+')'
			r2 = re.findall("([a-z]+)\)", r2, re.DOTALL)
			r1 = r1[0][0]		#1st half of dm
			r1 = r1+' '+' '.join(map(str, r2))
			return [r1]
		r1=re.findall("\(S[\s]+\(SBAR\s+\(IN (.*?)\)", tree, re.DOTALL)
		if r1:										#2s + (S (SBAR (IN
			return r1
		r1 = re.findall("\(S[\s]+\(IN (.*?)\)", tree, re.DOTALL)
		if r1:										#2s + (S (IN
			return r1
		else:
			return 0
	else:											#no dm
		return 0

def rule(tree):
	r1=re.findall("ROOT", tree, re.DOTALL)
	if (len(r1)==1):
		return rule_single(tree)
	else:
		return rule_multiple(tree)


def main():
	f = open('rules', 'r')							#input file with the parse tree
	l = f.readlines()
	string=''
	for i in l:
		string+=i
	f.close()
	trees = string.split('|||')
	trees = trees[:-1]
	for tree in trees:
		tree = tree.split('<<')
		print tree[0], "\n"
		print "#Discourse marker: ", rule(tree[0])
		print "---------------------------------------------------\n"


if __name__ == "__main__":
    main()