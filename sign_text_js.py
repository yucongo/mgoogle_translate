__all__ = ['sign_text_js']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['hash', 'C', 'a'])
@Js
def PyJsHoisted_a_(r, o, this, arguments, var=var):
    var = Scope({'r':r, 'o':o, 'this':this, 'arguments':arguments}, var)
    var.registers(['t', 'o', 'r', 'a'])
    #for JS loop
    var.put('t', Js(0.0))
    while (var.get('t')<(var.get('o').get('length')-Js(2.0))):
        try:
            var.put('a', var.get('o').callprop('charAt', (var.get('t')+Js(2.0))))
            def PyJs_LONG_0_(var=var):
                return PyJsComma(PyJsComma(var.put('a', ((var.get('a').callprop('charCodeAt', Js(0.0))-Js(87.0)) if (var.get('a')>=Js('a')) else var.get('Number')(var.get('a')))),var.put('a', (PyJsBshift(var.get('r'),var.get('a')) if PyJsStrictEq(Js('+'),var.get('o').callprop('charAt', (var.get('t')+Js(1.0)))) else (var.get('r')<<var.get('a'))))),var.put('r', (((var.get('r')+var.get('a'))&Js(4294967295.0)) if PyJsStrictEq(Js('+'),var.get('o').callprop('charAt', var.get('t'))) else (var.get('r')^var.get('a')))))
            PyJs_LONG_0_()
        finally:
                var.put('t', Js(3.0), '+')
    return var.get('r')
PyJsHoisted_a_.func_name = 'a'
var.put('a', PyJsHoisted_a_)
pass
var.put('C', var.get(u"null"))
@Js
def PyJs_anonymous_1_(r, _gtk, this, arguments, var=var):
    var = Scope({'r':r, '_gtk':_gtk, 'this':this, 'arguments':arguments}, var)
    var.registers(['t', 'l', 'r', 'S', 'h', 'm', 'd', 'u', 's', '_gtk', 'g', 'e', 'o', 'f', 'i'])
    var.put('o', var.get('r').get('length'))
    ((var.get('o')>Js(30.0)) and var.put('r', (((Js('')+var.get('r').callprop('substr', Js(0.0), Js(10.0)))+var.get('r').callprop('substr', (var.get('Math').callprop('floor', (var.get('o')/Js(2.0)))-Js(5.0)), Js(10.0)))+var.get('r').callprop('substr', (-Js(10.0)), Js(10.0)))))
    var.put('t', PyJsComma(Js(0.0), Js(None)))
    var.put('t', (var.get('C') if PyJsStrictNeq(var.get(u"null"),var.get('C')) else (var.put('C', (var.get('_gtk') or Js(''))) or Js(''))))
    #for JS loop
    var.put('e', var.get('t').callprop('split', Js('.')))
    var.put('h', (var.get('Number')(var.get('e').get('0')) or Js(0.0)))
    var.put('i', (var.get('Number')(var.get('e').get('1')) or Js(0.0)))
    var.put('d', Js([]))
    var.put('f', Js(0.0))
    var.put('g', Js(0.0))
    while (var.get('g')<var.get('r').get('length')):
        try:
            var.put('m', var.get('r').callprop('charCodeAt', var.get('g')))
            def PyJs_LONG_4_(var=var):
                def PyJs_LONG_3_(var=var):
                    def PyJs_LONG_2_(var=var):
                        return PyJsComma(PyJsComma(var.put('m', ((Js(65536.0)+((Js(1023.0)&var.get('m'))<<Js(10.0)))+(Js(1023.0)&var.get('r').callprop('charCodeAt', var.put('g',Js(var.get('g').to_number())+Js(1)))))),var.get('d').put((var.put('f',Js(var.get('f').to_number())+Js(1))-Js(1)), ((var.get('m')>>Js(18.0))|Js(240.0)))),var.get('d').put((var.put('f',Js(var.get('f').to_number())+Js(1))-Js(1)), (((var.get('m')>>Js(12.0))&Js(63.0))|Js(128.0))))
                    return PyJsComma((PyJs_LONG_2_() if ((PyJsStrictEq(Js(55296.0),(Js(64512.0)&var.get('m'))) and ((var.get('g')+Js(1.0))<var.get('r').get('length'))) and PyJsStrictEq(Js(56320.0),(Js(64512.0)&var.get('r').callprop('charCodeAt', (var.get('g')+Js(1.0)))))) else var.get('d').put((var.put('f',Js(var.get('f').to_number())+Js(1))-Js(1)), ((var.get('m')>>Js(12.0))|Js(224.0)))),var.get('d').put((var.put('f',Js(var.get('f').to_number())+Js(1))-Js(1)), (((var.get('m')>>Js(6.0))&Js(63.0))|Js(128.0))))
                return (var.get('d').put((var.put('f',Js(var.get('f').to_number())+Js(1))-Js(1)), var.get('m')) if (Js(128.0)>var.get('m')) else PyJsComma((var.get('d').put((var.put('f',Js(var.get('f').to_number())+Js(1))-Js(1)), ((var.get('m')>>Js(6.0))|Js(192.0))) if (Js(2048.0)>var.get('m')) else PyJs_LONG_3_()),var.get('d').put((var.put('f',Js(var.get('f').to_number())+Js(1))-Js(1)), ((Js(63.0)&var.get('m'))|Js(128.0)))))
            PyJs_LONG_4_()
        finally:
                (var.put('g',Js(var.get('g').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('S', var.get('h'))
    var.put('u', Js('+-a^+6'))
    var.put('l', Js('+-3^+b+-f'))
    var.put('s', Js(0.0))
    while (var.get('s')<var.get('d').get('length')):
        try:
            PyJsComma(var.put('S', var.get('d').get(var.get('s')), '+'),var.put('S', var.get('a')(var.get('S'), var.get('u'))))
        finally:
                (var.put('s',Js(var.get('s').to_number())+Js(1))-Js(1))
    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('S', var.get('a')(var.get('S'), var.get('l'))),var.put('S', var.get('i'), '^')),((Js(0.0)>var.get('S')) and var.put('S', ((Js(2147483647.0)&var.get('S'))+Js(2147483648.0))))),var.put('S', Js(1000000.0), '%')),((var.get('S').callprop('toString')+Js('.'))+(var.get('S')^var.get('h'))))
PyJs_anonymous_1_._set_name('anonymous')
var.put('hash', PyJs_anonymous_1_)


# Add lib to the module scope
sign_text_js = var.to_python()