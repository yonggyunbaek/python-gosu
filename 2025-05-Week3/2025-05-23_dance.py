# https://www.acmicpc.net/problem/4836

import sys
input = sys.stdin.readline


while True:
    err = { i: False for i in range(1,6) }
    dance = input().split()
    if not dance:
         break
    th = set()
    dip_position = []
    for i in range(len(dance)):
        if dance[i] == 'dip':
            err[5] = True
            if ((i >= 1 and dance[i - 1] == 'jiggle') or
                (i >= 2 and dance[i - 2] == 'jiggle') or
                (i < len(dance) - 1 and dance[i + 1] == 'twirl')):
                err[1] = True
            else:
                dip_position.append(i)
                
        elif dance[i] == 'twirl' or dance[i] == 'hop':
             th.add(dance[i])
    if 'dip' not in dance:
         err[1] = True
    if len(dance) >= 3 and dance[-3:] == ['clap', 'stomp', 'clap']:
            err[2] = True
    if dance[0] != 'jiggle':
         err[4] = True
    if th != {'twirl'}:
         err[3] = True
    if dip_position:
         err[1] = False

    err_list = [ str(k) for k, v in err.items() if not v ]
    # print(err_list)
    if len(err_list) == 1:
         errnum = str(err_list[0])
         answer = f"form error {errnum}: "
    elif len(err_list) == 2:
         answer = f"form errors {err_list[0]} and {err_list[1]}: "
    elif len(err_list) > 2:
         temp = ', '.join(err_list[:-1])
         answer = f"form errors {temp} and {str(err_list[-1])}: "
    elif len(err_list) == 0:
         answer = "form ok: "
    
    if dip_position:
         for i in dip_position:
              dance[i] = "DIP"
    
    print(answer, end='')
    print(*dance)
             
    




