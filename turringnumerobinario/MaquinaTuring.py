def turing_M (state = None, #estados de la maquina de turing
              blank = None, #simbolo blanco del alfabeto dela cinta
              rules = [],   #reglas de transicion
              tape = [],    #cinta
              final = None,  #estado valido y/o final
              pos = 0):#posicion siguiente de la maquina de turing

    st = state
    if not tape: tape = [blank]
    if pos <0 : pos += len(tape)
    if pos >= len(tape) or pos < 0 : raise Exception ("Se inicializa mal la posición")

    rules = dict(((s0, v0), (v1, dr, s1)) for (s0, v0, v1, dr, s1) in rules)
    """
Estado	Símbolo leído	Símbolo escrito	       Mov. 	Estado sig.
  p(s0)	       1(v0)	         x(v1)         R(dr)	     p(s1)
"""
    while True:
        print (st, '\t', end=" ")
        for i, v in enumerate(tape):
             if i==pos: print ("[%s]"%(v,),end=" ")
             else: print (v, end=" ")
        print()
        
        if st == final: break #Si ya llegó al estado final, se rompe el ciclo
        if (st, tape[pos]) not in rules: break #Si no encuentra reglas, se rompe el ciclo
        
        (v1,dr,s1) = rules [(st, tape[pos])]
        tape[pos]=v1 #rescribe el simbolo de la cinta
    
    #movimiento del cabezal
        if dr == 'left':
            if pos > 0: pos -= 1
            else: tape.insert(0, blank)
        if dr == 'right':
            pos += 1
            if pos >= len(tape): tape.append(blank)
        st = s1



print("----------------Maquina de turing: Incremento-------------------")
entrada2 = input("Ingrese los simbolos en binario: ")
turing_M (state = 's1', #estado inicial de la maquina de turing
              blank = '0', #simbolo blanco de el alfabeto dela cinta
              tape = list(entrada2),#inserta los elementos en la cinta
              final = 's6',  #estado valido y/o final
              rules = map(tuple,#reglas de transicion
                          [
                          "s1 1 0 right s2".split(),
                          "s2 1 1 right s2".split(),
                          "s2 0 0 right s3".split(),
                          "s3 0 1 left s4".split(),
                          "s3 1 1 right s3".split(),
                          "s4 1 1 left s4".split(),
                          "s4 0 0 left s5".split(),
                          "s5 1 1 left s5".split(),
                          "s5 0 1 right s1".split(),
                          ]   
                         )
             )  
