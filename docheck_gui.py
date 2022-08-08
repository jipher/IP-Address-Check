import PySimpleGUI as sg
from IPy import IP
import os


if os.path.exists('whitelist.txt'):
    wf = open('whitelist.txt','r+')
    wls = wf.readlines()
    wf.close()
else:
    wf = open('whitelist.txt','w')
    wls = []
    wf.close()

if os.path.exists('checklist.txt'):
    cf = open('checklist.txt','r+')
    cls=cf.readlines()
    cf.close()
else:
    cf = open('checklist.txt','w')
    cls = []
    cf.close()

rf=open('result.txt','w+')
ef=open('exclude.txt','w+')
rls=[]
els=[]

sg.theme('DarkAmber')
addlist_text = sg.Text('检查的地址:',size=16)
addlist_list = sg.Multiline("".join(cls[:]),key='-cl-',size=(32,8))
whitelist_text = sg.Text('白名单:',size=16)
whitelist_list = sg.Multiline("".join(wls[:]),key='-wl-',size=(32,8))
result_text = sg.Text('对比结果:',size=16)
result_list = sg.Multiline("".join(rls[:]),key='-rl-',size=(32,8))
exclude_text = sg.Text('被排除地址:',size=16)
exclude_list = sg.Multiline("".join(els[:]),key='-el-',size=(32,8))
check_bt = sg.Button('check')
c_bt = sg.Button('Cancel')

layout = [ [addlist_text,addlist_list],
            [whitelist_text,whitelist_list],
            [result_text,result_list],
            [exclude_text,exclude_list],
            [check_bt,c_bt] ]

window = sg.Window('Checking BlockList Address from WhiteList',layout)

while True:
    rls=[]
    els=[]
    event, values = window.read()
    if event == sg.WIN_CLOSED or event =='Cancel':
        break
    if event == 'check':
        print('checking')
        cf = open('checklist.txt','w')
        cf.write(values['-cl-'])
        cf.close()
        wf =open('whitelist.txt','w')        
        wf.write(values['-wl-'])
        wf.close()
        cls = values['-cl-'].split('\n')
        wls = values['-wl-'].split('\n')
        print(cls)
        for c  in cls:
            notin = True
            for w in wls:
                if IP(c) in IP(w):
                    notin = False
            if notin:
                rf.writelines(c+'\n')
                rls.append(c)
            else:
                ef.writelines(c+'\n')
                els.append(c)
        print(rls)
        print(els)      
        window['-rl-'].update("\n".join(rls[:]))
        window['-el-'].update("\n".join(els[:]))

print('closing')
#wf.close()
rf.close()
ef.close()
#cf.close()


window.close()
