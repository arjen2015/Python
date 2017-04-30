# -*- coding:utf-8 -*-
x = "there are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s." % (binary, do_not)

print x
print y

print "i said: %r." % x
print "i also said:'%s'." % y

hiliarious = False
joke_evalution = "isn't that joke so funny?! %r"

print joke_evalution % hiliarious

w = "this is he left side of..."
e = "a string with a right side."

print w + e