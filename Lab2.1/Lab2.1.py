import paramiko, time, re
BUF_SIZE = 20000
TIMEOUT = 1

list = []

# Создаем объект — соединение по ssh
ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Инициируем соединение по ssh
ssh_connection.connect("10.31.70.209", username="restapi", password="j0sg1280-7@", look_for_keys=False, allow_agent=False)
session = ssh_connection.invoke_shell()

session.send("\n")
session.recv(BUF_SIZE)
session.send("terminal length 0\n")
time.sleep(TIMEOUT)
session.send("\n")
session.recv(BUF_SIZE)
session.send("show interface\n")
time.sleep(TIMEOUT*2)
s = session.recv(BUF_SIZE).decode()
session.close()
so = s.splitlines()


for row in so:
    m = re.search(r"GigabitEthernet", row )
    if m:
        list.append(m.group(0))
print(list)





#list = []
# #3for row in s:
  #  m = re.search('bytes',row )
  #  if m:
  #print(f"Найдено первое число: {m.group()}")

        #eth = re.search("[0-9]+ (packets input), +[0-9]+ bytes|[0-9]+ (packets output), +[0-9]+ bytes",row )
         #   #inout= re.finditer('[0-9]+ (packets input), +[0-9]+ bytes|[0-9]+ (packets output), +[0-9]+ bytes',row )
        #if eth:
        #    result.append(eth)
    #print (result)

#print(result)