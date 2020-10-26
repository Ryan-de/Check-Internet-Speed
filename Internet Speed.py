# pip install speedtest-cli 

import speedtest

st = speedtest,Speedtest()
print("Your Download speed is",st.download()//10**6, "Mbps")
print("Your upload speed is",st.upload()//10**6, "Mbps")
print("Your ping is",int(st.results.ping),"MS")
