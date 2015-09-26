import os
import re

os.system("sudo /etc/init.d/tor restart")
os.system("sudo killall tor")
os.system("sudo killall tor")

f=open("/home/kc/.mozilla/firefox/profiles.ini","r")
file = f.read()
profile_list=re.findall(r'Path=[\w.]+',file)
profile = profile_list[0][5:]
f.close()

profile_path="/home/kc/.mozilla/firefox/"+profile
pref_file=profile_path+"/prefs.js"
f=open(pref_file,"r")
pref_js_data=f.read()
f.close()
pref_js_data_list=pref_js_data.split("\n")
present_network_proxy_setting=re.findall(r'''user_pref\(\"network.proxy.type\", \d''',pref_js_data)
if present_network_proxy_setting[0][-1]!=1:
    pref_js_data_list[pref_js_data_list.index('''user_pref("network.proxy.type", 0);''')]='''user_pref("network.proxy.type", 1);'''
    pref_js_data_list[pref_js_data_list.index('''user_pref("network.proxy.type", 1);''')-1]='''user_pref("network.proxy.socks_remote_dns", true);'''
    pref_js_data_list[pref_js_data_list.index('''user_pref("network.proxy.type", 1);''')-2]='''user_pref("network.proxy.socks_port", 9050);'''
    pref_js_data_list[pref_js_data_list.index('''user_pref("network.proxy.type", 1);''')-3]='''user_pref("network.proxy.socks", "127.0.0.1");'''

pref_torred_data='\n'.join(pref_js_data_list)
f=open(pref_file,"w")
f.write(pref_torred_data)
f.close()




