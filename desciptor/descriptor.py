# -*- coding:utf-8 -*- 
# 2017/3/23
# mail:yangnianqiu@gmail.com


class NameDescriptor(object):
    def __init__(self):
        self._name = ''

    def __get__(self, instance, owner):
        return self._name

    def __set__(self, instance, value):
        if not isinstance(value, basestring):
            raise TypeError, 'str must be'
        self._name = value

    def __delete__(self, instance):
        self._name = ''
        print 'delete name'


class Student(object):
    name = NameDescriptor()


if __name__ == '__main__':
    st = Student()
    print 'nothing' if not st.name else st.name, type(st.name)
    try:
        st.name = 1
    except TypeError, e:
        print e
    st.name = 'json'
    del st.name
