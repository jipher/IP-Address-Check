import PySimpleGUI as sg

wf=open('whitelist.txt','r')
cf=open('checklist.txt','r')
bf=open('result.txt','w')
ef=open('exclude.txt','w')
wls=wf.readlines()
cls=cf.readlines()
rls=[]
els=[]


sg.theme('DarkAmber')
addlist_text = sg.Text('需要检查的地址:')
addlist_list = sg.Listbox([])
whitelist_text = sg.Text('白名单:')
whitelist_list = sg.Listbox(wls)
result_text = sg.Text('对比结果:')
result_list = sg.Listbox(rls)
exclude_text = sg.Text('被排除地址:')
exclude_list = sg.Listbox(els)
check_bt = sg.Button('对比')
c_bt = sg.Button('Cancel')

layout = [ [addlist_text,addlist_list],
            [whitelist_text,whitelist_list],
            [result_text,result_list],
            [exclude_text,exclude_list],
            [check_bt,c_bt] ]

window = sg.Window('Checking BlockList Address from WhiteList',layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event =='Cancel':
        break
    print('Checking now...',values[0])

wf.close()
cf.close()
bf.close()
ef.close()

window.close()
