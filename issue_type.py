from django import template

register = template.Library()


@register.simple_tag
def define(the_string):
  print "Hello"	
  return the_string
