#-------------------------------
#!/usr/bin/python
#-----------------------EasyPHPMYSQL-------------------------------
#Copyrighted by Matthew Grant on 09.09.2013
#
#EasyPHPMYSQL is a command-line python script that is used to 
#write a PHP class files that connect and manipulate data in a
#MYSQL database just by answering a couple question about the
#database.  Also, it writes an optional login script for an
#administrator backend and an optional example script that shows
#a person how to use the php class.
#
#Free to use as you wish (MIT license)
#
#Proud member of the Zeitgest-Movement
#-----------------------------------------------------------------
import sys, getopt, MySQLdb, os
#----------Global Variable List---------------
host=''
user=''
password=''
filename=''
login=0
database=''
example=0
name=''
logintable=''
loginuser=''
loginpass=''

#----------Functions---------------------------
def usage():
# This is the function that handles the help flag
		print '------------Easyphpsql Help------------------------------------------------'
		print "-h  --help  Display help for easyphpsql"
		print "-u  --user  The user for the database"
		print "-s  --server  The host of the database"
		print "-p  --password  The password for the user of the database"
		print "-d  --database  The name of the database"
		print "-l  --login  Adds login function to the php class <table:username:password>"
		print "-e  --example  Add example of the usage of the php class"
		print "-n  --name The name of the php class that will be created"
		print "-x  --table  The name of the table that has the login information
		print "-y  --username  The name of the column that holds the login username
		print "-z  --password  The name of the column that holds the login password  
		print "---------------------------------------------------------------------------"
		return

def checkarg():
	global host
	global user
	global password
	global filename
	global login
	global database
	global example
	global name
	c1=0
	if host=='':
		host=raw_input("What is the host name for the database (ie - localhost)\n ")
		c1+=1
	if user=='':
		user=raw_input("What is the userename for the database \n")
		c1+=1
	if password=='':
		password=raw_input("What is the password for the database \n")
		c1+=1
	if database=='':
		database=raw_input("What is the name of the database \n")
		c1+=1
	if filename=='':
		filename=raw_input("What is the filename for the php class \n")
		c1+=1
	if name=='':
		name=raw_input("What is the name of the php class \n")
		c1+=1
	if (c1>3):
		flag1=0
		while (flag1==0):
			login1=raw_input("Do you want login script in the php class (y)es or (n)o\n")
			if (login1=="yes" or login1=="y" or login1=='Y' or login1=="YES" or login1=="Yes"):
				login=1
				flag1=1
				logintable=raw_input("What is the name of the table with the login information\n")
				loginuser=raw_input("What is the column name that holds the username\n")
				loginpass=raw_input("What is the column name that holds the password\n")
			elif (login1=="no" or login1=="n" or login1=='N' or login1=="NO" or login1=="No"):
				login=0	
				flag1=1
			else:
				print "[warning] Did not recognized the input you entered\n"
	if (c1>3):
		flag1=0
		while (flag1==0):
			example1=raw_input("Do you want example php files to be wrote to demostrate the php class (y)es or (n)o\n")
			if (example1=="yes" or example1=="y" or example1=='Y' or example1=="YES" or example1=="Yes"):
				example=1
				flag1=1
			elif (example1=="no" or example1=="n" or example1=='N' or example1=="NO" or example1=="No"):
				example=0
				flag1=1	
			else:
				print "[warning] Did not recognized the input you entered\n"
	return

def main(argv):
		try:
			opts, args = getopt.getopt(argv, 'hs:u:p:o:ld:en:x:y:z:',['help=''server=','user=','password=','output=','login=','database=','example=','name=','table=','username=', 'password='])
		except getopt.GetoptError:
			print 'There was an error in the format of FileCreator option'
                        print 'Enter filecreator.py -h for help'
			sys.exit(2)
		for opt, arg in opts:
			if opt in ('-h', '--help'):
		        	usage()
			        sys.exit()
			elif opt in ('-s','--server='):
				global host
				host=arg
				# replace with a call to a function to handle this flag
			elif opt in ('-u','--user='):
				global user
				user=arg
				# replace with a call to a function to handle this flag
			elif opt in ('-p','--password='):
				global password
				password=arg
				# replace with a call to a function to handle this flag
			elif opt in ('-o','--output='):
				global filename
				filename=arg
				# replace with a call to a function to handle this flag
			elif opt in ('-l','--login='):
				# replace with a call to a function to handle this flag
				global login
				login=1
			elif opt in ('-e','--example='):
				# replace with a call to a function to handle this flag
				global example
				example=1
			elif opt in ('-d','--database='):
				# replace with a call to a function to handle this flag
				global database
				database=arg
			elif opt in ('-n','--name='):
				# replace with a call to a function to handle this flag
				global name
				name=arg
#------------------Classes--------------------------------

class easyphpsql:

	tablelist=[]
	colnamelist=[]
	colid=0

	def __init__(self, host, user, password, database):
        	self.host = host
        	self.user = user
      		self.password = password
		self.database = database

	def connectdb(self): 
		db = MySQLdb.connect(self.host,self.user,self.password,self.database)
		cursor = db.cursor()
		return (db, cursor)

	def gettables(self):
		db,cursor=self.connectdb()
		cursor.execute('SHOW TABLES')
		results = cursor.fetchall()
		print "------------Tables for "+database+"------------"
		c=0
		for tblist in results:
			self.tablelist.append(str(results[c][0]))
			#print str(results[c][0])
			print self.tablelist[c]
			c+=1
		print "-----------------------------------------------"
		return

	def getcolumns(self,table):
		del self.colnamelist[:]
		db,cursor=self.connectdb()
		cursor.execute('DESCRIBE '+table)
		results = cursor.fetchall()
		print "------------Columns for "+table+"------------"
		for clist in results:
			#tablelist.append(str(results[c][0]))
			#print str(results[c][0])
			print clist
		print "-----------------------------------------------"
		numrows = len(results)    # 3 rows in your example
		numcols = len(results[0]) # 2 columns in your example
		print "-----------column names-----------------------"
		c1=0
		for num in range(0,numrows):
			self.colnamelist.append(results[num][0])
			print results[num][0]
		print "-----------------------------------------------"
		return

	def phpconstruct(self,host,user,password,database):
		str1 = "function __construct(){\n"
		str1+= "		$this->host=\""+host+"\";\n"
		str1+= "		$this->user=\""+user+"\";\n"
		str1+= "		$this->password=\""+password+"\";\n"
		str1+= "		$this->database=\""+database+"\";\n"
		str1+= "}\n"
		return str1

	def phpconnect(self):
		str1 = "public function connectdb(){\n"
		str1+= "		$mysqli = new mysqli($this->host, $this->user, $this->password, $this->database);\n"
		str1+= "		if ($mysqli->connect_errno) {\n"
    		str1+= "  			$strerror=\"Connect failed: $mysqli->connect_error\";\n"
		str1+= "			$this->writeerror($strerror);\n"
    		str1+= "			exit();\n"
		str1+= "		}\n"
		str1+= "		return $mysqli;\n"
		str1+= "}\n"
		return str1

	def phpclassintro(self):
		str1 = "<?php\n"
		str1+= "class "+name+" {\n"
		str1+= "public $host;\n"
		str1+= "public $user;\n"
		str1+= "public $password;\n"
		str1+= "public $database;\n"
		str1+= "public $tables = array();\n"
		str1+= "public $columns = array();\n"
		str1+= "public $colid;\n"
		return str1

	def phpclassclose(self):
		str1 = "}\n"
		str1+= "?>\n"
		return str1

	def phpadd(self,table):
		str1="public function "+table+"add ("
		for list1 in self.colnamelist:
			str1+="$"+list1+","
		str1=str1[:-1]
		str1+="){\n"
		for list1 in self.colnamelist:
			str1+= "		$"+list1+" = stripslashes($"+list1+");\n"
			str1+= "		$"+list1+" = $mysqli->real_escape_string($"+list1+");\n"
		str1+= "		$query=\"INSERT INTO "+table+" ("
		for list2 in self.colnamelist:
			str1+=list2+","
		str1=str1[:-1]
		str1+=") VALUES (" 
		for list2 in self.colnamelist:
			str1+="$"+list2+","
		str1=str1[:-1]
		str1+=")\";\n"
		str1+= "		$result=$this->doquery($query);\n"
		str1+= "		$result->close();\n"
		str1+= "		return $result;\n"
		str1+= "}\n"
		return str1

	def phpadd1(self):
		str1 = "public function addtotable($table,$col,$mysqli){\n"
		str1+= "		$str1 = '';\n"
		str1+= "		$str2 = '';\n"
		str1+= "		$this->getcolumns($table,$mysqli);\n"
		str1+= "		$columnid1=$this->getid($mysqli,$table);\n"
		str1+= "		$query=\"Insert into $table (\";\n"
		str1+= "		$count2=0;\n"
		str1+= "		foreach ($this->columns as $value){\n"
		str1+= "			if ($count2!=$this->colid){
		str1+= "				$str1.=\"$value,\";\n"
		str1+= "			}\n"
		str1+= "			$count2++;\n"		
		str1+= "		}\n"
		str1+= "		$str1 = substr($str1, 0, -1);\n"
		str1+= "		$str1.=\") VALUES (\";\n"
		str1+= "     		foreach ($col as $value){\n"
		str1+= "			$str2.=\"'$value',\";\n"
		str1+= "		}\n"
		str1+= "		$str2 = substr($str2, 0, -1);\n"
		str1+= "		$str2 .=\")\";\n"
		str1+= "		$query = $query.$str1.$str2;\n"
		str1+= "		$result=$this->doquery($query,$mysqli);\n"
		str1+= "		return $result;\n"
		str1+= "}\n"
		return str1

	def phpedit(self,table):
		self.findid(table)
		str1="public function "+table+"edit ("
		for list1 in self.colnamelist:
			str1+="$"+list1+","
		str1=str1[:-1]
		str1+="){\n"
		for list1 in self.colnamelist:
			str1+= "		$"+list1+" = stripslashes($"+list1+");\n"
			str1+= "		$"+list1+" = $mysqli->real_escape_string($"+list1+");\n"
		str1+= "		$query=\"UPDATE "+table+" SET "
		for list2 in self.colnamelist:
			str1+=list2+"=$"+list2+","
		str1=str1[:-1]
		str1+=" WHERE "+self.colnamelist[self.colid]+"='$"+self.colnamelist[self.colid]+"'\";\n"
		str1+= "		$result=$this->doquery($query);\n"
		str1+= "		$result->close();\n"
		str1+= "		return $result;\n"
		str1+= "}\n"
		return str1

	def phpedit1(self):
		str1 = "public function edittable($table,$coldata,$id,$mysqli){\n"
		str1+= "		$this->getcolumns($table,$mysqli);\n"
		str1+= "		$columnid1=$this->getid($mysqli,$table);\n"
		str1+= "		$col1=$this->columns[$this->colid];\n"
		str1+= "		$query=\"UPDATE $table SET \";\n"
		str1+= "		$count2=0;\n"
		str1+= "		foreach ($this->$columns as $value){\n"
		str1+= "			if ($count2!=$this->colid){
		str1+= "				$str1+=\"$value='$coldata[$count2]',\";\n"
		str1+= "				$count2++;\n"
		str1+= "			}
		str1+= "		}\n"
		str1+= "		$str1 = substr(str1, 0, -1);\n"
		str1+= "		$query .=\" where id='$id'\""
		str1+= "		$result=$this->doquery($query,$mysqli);\n"
		str1+= "		$result->close();\n"
		str1+= "		return $result;\n"
		str1+= "}\n"
		return str1

	def phpdelete(self,table):
		str1="public function "+table+"delete ("
		str1+="$"+self.colnamelist[0]+"){\n"
		str1+= "		$"+self.colnamelist[0]+" = stripslashes($"+self.colnamelist[0]+");\n"
		str1+= "		$"+self.colnamelist[0]+" = $mysqli->real_escape_string($"+self.colnamelist[0]+");\n"
		str1+="		$query=\"DELETE FROM "+table+" WHERE "+self.colnamelist[0]+"='$"+self.colnamelist[0]+"'\";\n"
		str1+= "		$result=$this->doquery($query);\n"
		str1+= "		$result->close();\n"
		str1+= "		return $result;\n"
		str1+= "}\n"
		return str1

	def phpdelete1(self):
		str1 = "public function deletefromtable($table,$id,$mysqli){\n"
		str1+= "		$table = stripslashes($table);\n"
		str1+= "		$table = $mysqli->real_escape_string($table);\n"
		str1+= "		$id = stripslashes($id);\n"
		str1+= "		$id = $mysqli->real_escape_string($id);\n"
		str1+= "		$this->getcolumns($table,$mysqli);\n"
		str1+= "		$columnid1=$this->getid($mysqli,$table);\n"
		str1+= "		$col1=$this->columns[$this->colid];\n"
		str1+= "		$query=\"DELETE FROM $table WHERE $col1='$id'\";\n"
		str1+= "		$result=$this->doquery($query,$mysqli);\n"
		str1+= "		return $result;\n"
		str1+= "}\n"
		return str1

	def phpgetone(self,table):
		str1="public function "+table+"getone ("
		str1+="$"+self.colnamelist[0]+"){\n"
		str1+="		$query=\"SELECT * FROM "+table+" WHERE "+self.colnamelist[0]+"='$"+self.colnamelist[0]+"'\";\n"
		str1+= "		$result=$this->doquery($query);\n"
		str1+= "		$row = $result->fetch_array(MYSQLI_BOTH);\n"
		str1+= "		$result->close();\n"
		str1+= "		return $row;\n"
		str1+= "}\n"
		return str1

	def phpgetone1(self):
		str1 = "public function rowfromtable($table,$id,$mysqli){\n"
		str1+= "		$table = stripslashes($table);\n"
		str1+= "		$table = $mysqli->real_escape_string($table);\n"
		str1+= "		$id = stripslashes($id);\n"
		str1+= "		$id = $mysqli->real_escape_string($id);\n"
		str1+= "		$query=\"SELECT * FROM $table where $column[0]='$id'\";\n"
		str1+= "		$result=$this->doquery($query,$mysqli);\n"
		str1+= "		$row = $result->fetch_array(MYSQLI_BOTH);\n"
		str1+= "		$result->close();\n"
		str1+= "		return $row;\n"
		str1+= "}\n"
		return str1

	def phpget(self,table):
		str1="public function "+table+"getall ("
		str1+="$"+self.colnamelist[0]+"){\n"
		str1+="		$query=\"SELECT * FROM "+table+"\";\n"
		str1+= "		$result=$this->doquery($query);\n"
		str1+= "		return $result;\n"
		str1+= "}\n"
		return str1

	def phpget1(self):
		str1 = "public function getall ($table,$mysqli){\n"
		str1+= "		$query=\"SELECT * FROM $table\";\n"
		str1+= "		$result=$this->doquery($query,$mysqli);\n"
		str1+= "		return $result;\n"
		str1+= "		$result->close();\n"
		str1+= "		return 1;\n"
		str1+= "}\n"
		return str1

	def phpchecklogin(self,logintable,loginuser,loginpass):
		str1 = "public function checklogin($username,$password,$mysqli){\n"
		str1+= "		$username = stripslashes($username);\n"
		str1+= "		$username = $mysqli->real_escape_string($username);\n"
		str1+= "		$password = stripslashes($password);\n"
		str1+= "		$password = $mysqli->real_escape_string($password);\n"
		str1+= "		$query=\"SELECT "+loginpass+" FROM "+logintable+" where "+loginuser+"='$username'\";\n"
		str1+= "		$result=$this->doquery($query,$mysqli);\n"
		str1+= "		$row = $result->fetch_array(MYSQLI_BOTH);\n"
		str1+= "		$password1=$row['password'];\n"
		str1+= "		if ($password==$password1){\n"
		str1+= "			return 1;\n"
		str1+= "		}\n"
		str1+= "		else{\n"
		str1+= "			return 0;\n"
		str1+= "		}\n"
		str1+= "}\n"		
		return str1

	def javascript1(self):
		print "<script>"
		print "		delete (id){"
		print "			res=confirm('Are you sure you want to delete this data');"
		print "			if (res==true){"
		print "				location.href = 'admin.php?method=delete&id='+id"
		print "			}"		
		print "		}"
		print "</script>"
		return

	def phpprinttable(self, table):
		return

	def phpprinttable1(self):
		str1 = "public function printtable($table,$mode){\n"
		str1+= "// Mode can be 0 -> just table no buttons\n"
		str1+= "//             1 -> table + change and delete button\n"
		str1+= "		$this->getcolumns($table,$mysqli);\n"
		str1+= "		$colnum=count($this->columns);\n"
		str1+= "		$columnid1=$this->getid($mysqli,$table);\n"
		str1+= "		$columnid=$this->colid;\n"
		str1+= "		echo \"<table border='1'>\";\n"
		str1+= "		echo '<tr>';\n"
		str1+= "		$count2=0;
		str1+= "         	foreach ($this->columns as $value){\n"
		str1+= "			if ($count2!=$this->colid){\n"		
		str1+= "				echo \"<td>$values</td>\";\n"
		str1+= "			}\n"
		str1+= "			$count2++;\n"
		str1+= "		}\n"
		str1+= "		if ($mode==1){\n"
		str1+= "			echo '<td></td>';\n"
		str1+= "         	}\n"
		str1+= "		echo '</tr>';\n"
		str1+= "		$result=$this->getall($table);\n"
		str1+= "		while($row = $result->fetch_array(MYSQLI_BOTH)){\n"
		str1+= "			if ($mode==1){\n"
		str1+= "				echo \"<form method='GET'>\";\n"
		str1+= "			}\n"
		str1+= "			echo '<tr>';\n"
		str1+= "         		for ($c1=0;$c1<$colnum;$c1++){\n"
		str1+= "				if ($c1!=$this->colid){\n"
		str1+= "					if ($mode==1){\n"
		str1+= "						echo \"<td><input type='text' name='$col1[$c1]' id='$col1[$c1]' value='$row[$c1]'></td>\";\n"		
		str1+= "					}\n"
		str1+= "					else{\n"
		str1+= "						echo '<td>$row[$c1]</td>';\n"
		str1+= "					}\n"
		str1+= "				}\n"
		str1+= "			}\n"
		str1+= "			if ($mode==1){\n"
		str1+= "				echo '<td>';\n"
		str1+= "				echo \"<input type='submit' value='Edit' id='method' name='method'> <input type='button' value='Delete' id='delete' name='delete' onclick='delete1($row[$columnid]);'>\";\n"
		str1+= "				echo \"<input type='hidden' name='table' id='table' value='$table'>\";\n"
		str1+= "				echo \"<input type='hidden' name='id' id='id' value='$row[$columnid]'>\";\n"
		str1+= "				echo '</form>';\n"
		str1+= "				echo '</td>';\n"
		str1+= "			}\n"
		str1+= "			echo '</tr>';\n"
		str1+= "		}\n"
		str1+= "		echo '</table>';\n"
		str1+= "		return 1;\n"
		str1+= "}\n"
		return str1

	def phpquery(self):
		str1 = "public function doquery($query,$mysqli){\n"
		str1+= "		$result = $mysqli->query($query);\n"
		str1+= "		if (!$result){\n" 
		str1+= "			$strerror=\"Error in query: $mysqli->error\";\n"
		str1+= "			$this->writeerror($strerror);\n"
		str1+= "			return 0;\n"
		str1+= "		}\n"
		str1+= " 		return $result;\n"
		str1+= "}\n"
		return str1

	def phpgettables(self):
		str1 = "public function gettables($mysqli){\n"
		str1+= "		$query = 'show tables';\n"
		str1+= "		$result=$this->doquery($query,$mysqli);\n"
		str1+= "		while ($row = $result->fetch_array(MYSQLI_BOTH)){\n"
		str1+= "			$this->tables[]=$row[0];\n"
		str1+= "		}\n"
		str1+= "		$result->close();\n"
		str1+= "		return 1;\n"
		str1+= "}\n"
		return str1

	def phpgetcolumns(self):
		str1 = "public function getcolumns($table,$mysqli){\n"
		str1+= "		$query = \"describe $table\";\n"
		str1+= "		$result=$this->doquery($query,$mysqli);\n"
		str1+= "		unset ($this->columns);\n"
		str1+= "		while ($row = $result->fetch_array(MYSQLI_BOTH)){\n"
		str1+= "			$this->columns[]=$row[0];\n"
		str1+= "		}\n"
		str1+= "		$result->close();\n"
		str1+= "		return 1;\n"
		str1+= "}\n"
		return str1

	def phperror(self):
		str1 = "private function writeerror($strerror){\n"
		str1+= "		$filename = './logs/errorlog.txt';\n"
		str1+= "		$tstamp1 = new DateTime('NOW');\n"
		str1+= "		$tstamp=$tstamp1->format('Y-m-d H:i:s');\n"
		str1+= "		$remoteadd = $_SERVER['REMOTE_ADDR'];\n"
		str1+= "		$str1=\"$tstamp  -  $remoteadd  -  $strerror\\n\";\n"
		str1+= "		if (is_writable($filename)) {\n"
		str1+= "			if (!$handle = fopen($filename, 'a')) {\n"
		str1+= "				//echo \"Cannot open file ($filename)\";\n"
		str1+= "				exit;\n"
		str1+= "			}\n"
		str1+= "			if (fwrite($handle, $str1) === FALSE) {\n"
		str1+= "				//echo \"Cannot write to file ($filename)\";\n"
		str1+= "				exit;\n"
		str1+= "			}\n"
		str1+= "			//echo \"Success, wrote ($somecontent) to file ($filename)\";\n"
		str1+= "		}\n"
		str1+= "		else {\n"
		str1+= "			//echo \"The file $filename is not writable\";\n"
		str1+= "		}\n"
		str1+= "		fclose($handle);\n"
		str1+= "		return 1;\n"
		str1+= "}\n"
		return str1
	
	def findid(self,table):
		db,cursor=self.connectdb()
		cursor.execute('DESCRIBE '+table)
		results = cursor.fetchall()
		numrows = len(results)    # 3 rows in your example"
		for num in range(0,numrows):
			#self.colnamelist.append(results[num][3])
			print results[num][3]
			if results[num][3]=="PRI":
				self.colid=num
		return

	def phpfindid(self):
		str1 = "public function getid($table){\n"
		str1+= "		$c=0;\n"
		str1+= "		$query = \"describe $tables\";\n"
		str1+= "		$result=$this->doquery($query);\n"
		str1+= "		while ($row = $result->fetch_array(MYSQLI_BOTH)){\n"
		str1+= "			if ($row[3]=='PRI'){\n"
		str1+= "				$this->colid=$c;\n"
		str1+= "				$c++;\n"
		str1+= "			}\n"
		str1+= "		}\n"
		str1+= "		$result->close();\n"
		str1+= "		return 1;\n"	
		str1+= "}\n"		
		return str1

	def phplogin(self,name,filename):
		str1="<?php\n"
		str1+="include '"+filename+".php';\n"
		str1+="$"+name+"= new "+name+"(self.host,self.user,self.password,self.database)\n;"
		str1+="$link=$"+name+"->connectdb();\n"
		str1+="$e1=\"<p></p>\";"
		str1+="if (isset($_POST['Login'])){\n"
		str1+="		if (isset($_POST['username']) && isset($_POST['password']) && $_POST['username']!='' && $_POST['password']!=''){\n"
		str1+="			$username = $_POST['username'];\n"
        	str1+="			$password = $_POST['password'];\n"
		str1+="			$username = stripslashes($username);\n"
		str1+="			$username = $link->real_escape_string($username);\n"
		str1+="			$password = stripslashes($password);\n"
		str1+="			$password = $link->real_escape_string($password);\n"
    		str1+="			$password = md5($password);\n"
		str1+="			$result=$"+name+"->checklogin($username, $password, $link);\n"
		str1+="		}\n"
		str1+="		else{\n"
		str1+="			$result=0;\n"
		str1+="		}\n"
		str1+="		if( $result == 1 ) {\n"
        	str1+="			header ('location: http://localhost/admin.php');\n"
    		str1+="		} else {\n"
        	str1+="			$e1 = \"<p><font color='red'>Username and/or password incorrect.</font></p>\";\n"
		str1+="			callhtml($e1);\n"
    		str1+="		}\n" 
		str1+="}\n"
		str1+="else{\n"
		str1+="		callhtml($e1);\n"
		str1+="}\n" 
		str1+="function callhtml(){\n"
		str1+="		echo '<html>';\n"
		str1+="		echo '<head>';\n"
		str1+="		echo '</head>';\n"
		str1+="		echo '<body>';\n"
		str1+="		echo '<center>';\n"
		str1+="		echo '<h1>Login Sc0ript</h1>';\n"
		str1+="		echo \"<form action='login.php' method='POST'>\";\n"
		str1+="		echo $e1;\n"
		str1+="		echo '<table>';\n"
		str1+="		echo '<tr>';\n"
		str1+="		echo '<td>Username</td>';\n"
		str1+="		echo \"<td><input type='text' id='username' name='username'></td>\";\n"
		str1+="		echo '</tr>';\n"
		str1+="		echo '<tr>';\n"
		str1+="		echo '<td>Password</td>';\n"
		str1+="		echo \"<td><input type='password' id='password' name='password'></td>\";\n"
		str1+="		echo '</tr>';\n"
		str1+="		echo '<tr>';\n"
		str1+="		echo \"<td colspan='2' align='center'><input type='submit' value='Login' id='Login' name='Login'></td>\";\n"
		str1+="		echo '</tr>';\n"
		str1+="		echo '</table>';\n"
		str1+="		echo '</form>';\n"
		str1+="		echo '</center>';\n"
		str1+="		echo '</body>';\n"
		str1+="		echo '</html>';\n"
 		str1+="}\n"
		str1+="?>\n"
		return str1

	def phplogout(self):
		str1 ="<?php\n"
		str1+="session_start();\n"
		str1+="session_destroy();\n"
		str1+="header ('location: http://localhost/rain/admin/login.php');\n"
		str1+="?>\n"		
		return str1

	def phpexample(self):
		str1 = "<?php\n"
		str1+= "include \""+filename+".php\";\n"
		str1+= "session_start();\n"
		str1+= "$r1='';\n"
		str1+= "$"+name+" = new "+name+";\n"
		str1+= "$link=$"+name+"->connectdb();\n"
		str1+= "$int1=$"+name+"->gettables($link);\n"
		str1+= "if (isset($_GET['table'])){\n"
		str1+= "		$table=$_GET['table'];\n"
		str1+= "}\n"
		str1+= "else{\n"
		str1+= "		$table=$"+name+"->tables[0];\n"
		str1+= "}\n"
		str1+= "$t1=$"+name+"->tables;\n"
		str1+= "$columnid1=$test->getid($mysqli,$table);\n"
		str1+= "$int1=$"+name+"->getcolumns($table,$link);\n"
		str1+= "$c1=$"+name+"->columns;\n"
		str1+= "$colnum=$count($"+name+"->columns);\n"
		str1+= "if (isset($_GET['method'])){\n"
		str1+= "		$method=$_GET['method'];\n"
		str1+= "		$id=$_GET['id'];\n"
		str1+= "		if ($method=='Delete'){\n"
		str1+= "			$r1=$"+name+"->deletefromtable($table,$id);\n"
		str1+= "		}\n"
		str1+= "		elseif ($method=='Edit'){\n"
		str1+= "			//$c1=0;\n"
		str1+= "			$count2=0;\n"
		str1+= "			foreach($"+name+"->columns as $value){\n"
		str1+= "				if ($count2!=$test->colid){\n"
		str1+= "					$coldata[]=$_GET[$value];\n"
		str1+= "				}\n"
		str1+= "				$count2++;\n"
		str1+= "			}\n"
		str1+= "			$r1=$"+name+"->edittable($mysqli,$table,$id,$coldata);\n"
		str1+= "		}\n"
		str1+= "		elseif ($method=='Add'){\n"
		str1+= "			//$c1=0;\n"
		str1+= "			$count2=0;\n"
		str1+= "			foreach($"+name+"->columns as $value){\n"
		str1+= "				if ($count2!=$test->colid){\n"
		str1+= "					$coldata[]=$_GET[$value];\n"
		str1+= "				}\n"
		str1+= "				$count2++;\n"
		str1+= "			}\n"
		str1+= "			$r1=$"+name+"->addtotable($table,$coldata);\n"
		str1+= "		}\n"
		str1+= "}\n"
		str1+= "?>\n"
		str1+= "<html>\n"
		str1+= "<head>\n"
		str1+= "<script>\n"
		str1+= "		function delete1(id){\n"
		str1+= "			res=confirm(\"Are you sure you want to delete this data\");\n"
		str1+= "			if (res==true){\n"
		str1+= "				location.href = \"admin.php?method=delete&id=\"+id+\"&table=<?=$table ?>\";\n"
		str1+= "			}\n"		
		str1+= "		}\n"
		str1+= "</script>\n"
		str1+= "</head>\n"
		str1+= "<body>\n"
		str1+= "<center>\n"
		str1+= "<h1>Administrator Script</h1>\n"
		str1+= "<table>\n"
		str1+= "<tr>\n"
		str1+= "<?php\n"
		str1+= "foreach($t1 as $value){\n"
		str1+= "		echo \"<td><a href='admin.php?table=$value'>$value</a></td>\";\n"
		str1+= "}\n"
		str1+= "?>\n"
		str1+= "<td><a href=\"logoff.php\">Logoff</a></td>\n"
		str1+= "</tr>\n"
		str1+= "</table>\n"
		str1+= "<h2>Add to Database</h2>\n"
		str1+= "<form method='GET' action='admin.php'>\n"
		str1+= "<input type='hidden' name='table' id='table' value='<?=$table ?>'>\n"
		str1+= "<table border='1'>\n"
		str1+= "<tr>\n"
		str1+= "<?php\n"
		str1+= "$count2=0\n";
		str1+= "foreach($c1 as $value){\n"
		str1+= "		if ($count2!=$"+name+"->colid){\n"
		str1+= "			echo '<td>$value</td>';\n"
		str1+= "		}\n"
		str1+= "		$count2++\n"
		str1+= "}\n"
		str1+= "?>\n"
		str1+= "<td></td>\n"
		str1+= "</tr>\n"
		str1+= "<tr>\n"
		str1+= "<?php\n"
		str1+= "$count2=0\n";
		str1+= "foreach($c1 as $value){\n"
		str1+= "		if ($count2!=$"+name+"->colid){\n"
		str1+= "			echo \"<td><input type='text' name='$value' id='$value'></td>\";\n"
		str1+= "		}\n"
		str1+= "		$count2++\n"		
		str1+= "}\n"
		str1+= "?>\n"
		str1+= "<td><input type='submit' value=' Add ' id='method' name='method'></td>\n"
		str1+= "</tr>\n"
		str1+= "</table>\n"
		str1+= "</form>\n"
		str1+= "<h2>Edit/Delete Database</h2>\n"
		str1+= "<?php\n"
		str1+= "$int1=$"+name+"->printtable($table, 1);\n"
		str1+= "?>\n"
		str1+= "</center>\n"
		str1+= "</body>\n"
		str1+= "</html>\n"
		return str1

	def writefile(self,file1, str1):
		# Open a file
		f = open("./"+file1, "w")
		f.write(str1);
		# Close opend file
		f.close()
		return

			
#-------------Main Body of the Program--------
if __name__ == "__main__":
		main(sys.argv[1:])
#---------------------------------------------
checkarg()
easyphpsql = easyphpsql(host,user,password,database)
easyphpsql.gettables()
content=easyphpsql.phpclassintro()
content+=easyphpsql.phpconstruct(host,user,password,database)
content+=easyphpsql.phpconnect()
for table in easyphpsql.tablelist:
	easyphpsql.getcolumns(table)
	content+=easyphpsql.phpadd(table)
	content+=easyphpsql.phpedit(table)
	content+=easyphpsql.phpdelete(table)
	content+=easyphpsql.phpgetone(table)
	content+=easyphpsql.phpget(table)
content+=easyphpsql.phpadd1()
content+=easyphpsql.phpedit1()
content+=easyphpsql.phpdelete1()
content+=easyphpsql.phpgetone1()
content+=easyphpsql.phpget1()
content+=easyphpsql.phpquery()
content+=easyphpsql.phpgettables()
content+=easyphpsql.phpgetcolumns()
content+=easyphpsql.phperror()
content+=easyphpsql.phpfindid()
content+=easyphpsql. phpprinttable1()
if login==1:
	content+=easyphpsql.phpchecklogin()
content+=easyphpsql.phpclassclose()
easyphpsql.writefile(filename+".php",content)
if login==1:
	content=easyphpsql.phplogin(name,filename)
	easyphpsql.writefile("login.php",content)
	content=easyphpsql.phplogout()
	easyphpsql.writefile("logoff.php",content)
if example==1:
	content=easyphpsql.phpexample()
	easyphpsql.writefile("admin.php",content)
print "The files has been written. Finished!!"
sys.exit(0)

