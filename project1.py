operator = {'+' : 1 , '-' : 1 , '*' : 2 , '/': 2  , '**' : 3}
infix_expression = input('Enter an infix expression:  ')
operation_type = input('prefix or postfix or both ? ')

loop_number = 0
while loop_number <=1:
    stack = []
    x = 3
    for i in infix_expression:
        stack.append(i)
    if loop_number == 0:#postfix
        while x != 0:
            r = 0
            le = len(stack)
            number = 0
            while number != le:
                if stack[number] in operator and operator[stack[number]]==x:
                    ch = stack[r-1]+ stack[r+1] + stack[r]
                    stack.pop(r)
                    stack.pop(r)
                    stack.pop(r-1)
                    stack.insert(r-1 , ch)
                    r-=1
                    number-=1

                elif stack[number] == ')':
                    sta = []
                    j = number
                    for i in stack[number::-1]:
                        sta.append(i)
                        j-=1
                        if i == '(':
                            break
                    j+=1
                    k = stack[j]
                    while k !=')':
                        stack.pop(j)
                        k = stack[j]
                    stack.pop(j)
                    char = []
                    for ck in sta[::-1]:
                        char.append(ck)

                    loop = 3
                    while loop !=0:
                        no = 0
                        len_list = len(char)
                        while no != len_list:
                            if char[no] in operator and operator[char[no]] == loop:
                                ch = char[no-1] + char[no+1] + char[no]
                                char.pop(no-1)
                                char.pop(no-1)
                                char.pop(no-1)
                                char.insert(no-1 , ch)
                                no-=2
                            no+=1
                            len_list = len(char)
                        loop-=1
                    eb = ''
                    char.pop(0)
                    char.pop(-1)
                    for ck in char:
                        eb+=ck
                    stack.insert(j , eb)
                    number = j
                r+=1
                number+=1
                le = len(stack)
            x-=1
        postfix = stack
    elif loop_number == 1: # prefix
        while x !=0:
            r = 0
            le = len(stack)
            number =0
            while number!= le:
                if stack[number] in operator and operator[stack[number]] == x:
                    
                    ch = stack[r] + stack[r-1] + stack[r+1]
                    stack.pop(r)
                    stack.pop(r)
                    stack.pop(r-1)
                    stack.insert(r-1 , ch)
                    r-=1
                    number-=1
                    
                elif stack[number] == ')':
                    sta = []
                    j = number
                    for i in stack[number::-1]:
                        sta.append(i)
                        
                        j-=1
                        if i == '(':
                            break
                    j+=1
                    k = stack[j]
                    while k != ')':
                        stack.pop(j)
                        k=stack[j]
                    stack.pop(j)
                    char = []
                    for ck in sta[::-1]:
                        char.append(ck)
                    
                    loop = 3
                    while loop!=0:
                        no = 0
                        len_list = len(char)
                        while no != len_list:
                            if char[no] in operator and operator[char[no]] == loop:
                                ch = char[no] + char[no-1] + char[no+1]
                                char.pop(no-1)
                                char.pop(no-1)
                                char.pop(no-1)
                                char.insert(no-1 , ch)
                                no-=2
                            no+=1
                            len_list = len(char)
                        loop-=1
                    eb = ''
                    char.pop(0)
                    char.pop(-1)
                    for ck in char:
                            eb+=ck
                    stack.insert(j , eb)
                    number = j
                    

                r+=1
                number+=1
                le = len(stack)

            x-=1
        prefix = stack
    loop_number+=1

if operation_type == 'postfix':
    print('postfix :' , postfix[0])

elif operation_type == 'prefix':
    print('prefix :' , prefix[0])

elif operation_type == 'both':
    print('postfix :' , postfix[0])
    print('prefix :' , prefix[0])

