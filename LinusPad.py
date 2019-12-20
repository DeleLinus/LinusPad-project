from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import *
from tkinter.messagebox import *
import os

class LinusPad:
	def __init__(self):
		self.root=Tk()
		self.root.geometry("300x400+0+0")
		self.root.title("Untitled - LinusPad")
		self.text_field=ScrolledText(self.root, width="167", height="41", wrap="word", padx=6)#, sticky="s")
		self.text_field.grid(row=0,column=0)
		self.xscroll=Scrollbar(self.root, orient="horizontal", command=self.text_field.xview)
		self.text_field.configure(xscrollcommand=self.xscroll.set)
		self.xscroll.grid(row=1, column=0, sticky="ew")
		self.menubars_func()
		self.file_path=""
		self.root.mainloop()
		
	def NewFile(self):
		screen_content=self.text_field.get("1.0", "end-1c")
		if self.file_path !="":
			file_before_new=open(self.file_path,"r")
			saved_file_content=file_before_new.read()
			file_before_new.close()
			if screen_content!=saved_file_content:
				file_name=(self.file_path.split("/")[-1]).split(".")[0]
				do_you_want_to_save=askyesnocancel(title="LinusPad", message="Do yo want to save changes to %s?"%(file_name))
				if do_you_want_to_save:
					current_file=open(self.file_path,"w")
					current_file.write(screen_content)
					current_file.close()
					self.Blank_Page()
				elif (do_you_want_to_save) == None:
					pass
				else:
					self.Blank_Page()
			else:
				self.Blank_Page()
		elif self.file_path=="" and len(screen_content)>0:
			do_you_want_to_save=askyesnocancel(title="LinusPad", message="Do yo want to save changes to Untitled?")
			if do_you_want_to_save:
				file_object=asksaveasfile('w', initialfile='Untitled.txt', defaultextension="txt", parent=self.root, title="Save As", filetypes=(("Text Documents","*.txt"),("All Files","*.*")))
				if file_object!=None:
					content=self.text_field.get("1.0","end-1c")
					file_object.write(screen_content)		
					file_object.close()
					self.Blank_Page()
				else:
					file_object=None
					pass
			elif (do_you_want_to_save)==None:
				pass
			else:
				self.Blank_Page()
		else:
			self.Blank_Page()
	def Blank_Page(self):
		self.text_field.delete("1.0",END)
		self.file_path=""
		self.root.title("Untitled - LinusPad")


	def OpenFile(self):
		file_object=askopenfile('r',parent=self.root,title='Open', filetypes=(("Text Documents","*.txt"),("All Files","*.*")))
		if file_object != None:
			contents=file_object.read()
			self.text_field.delete("1.0", END)
			self.text_field.insert("1.0", contents)
			self.file_path=file_object.name
		#-------------------------------------------------------
			#First way to get and set my title
			# filetitle=str(file_object)
			# filetitle=re.split(r"/|'",filetitle)
			# for i in filetitle:
			# 	if ".txt" in i:
			# 		filetitle=i+" - LinusPad"
			# self.root.title(filetitle)
			#self.file.close()
		#-------------------------------------------------------
			#second way to get and set my title
			#filetitle=os.path.basename(str(file_object))
			#self.root.title(filetitle.split("'")[0]+" - LinusPad" )
			#file_object.close()
		#--------------------------------------------------------
			#Third way to get and set my title. [self.file.name] returns the path of the file
			self.root.title(self.file_path.split("/")[-1] +" - LinusPad" )			
			file_object.close()
		else:
			file_object=None
			pass
		
	def SaveFile(self):
		#my name is Ayandele Linus. I happen to be the brain behind the robotics Association in Nigeria
		if self.file_path=="":
			self.SaveFile_as()
		else:
			current_file=open(self.file_path,"w")
			content=self.text_field.get("1.0","end-1c")
			current_file.write(content)
			current_file.close()
		
	def SaveFile_as(self):
		file_object=asksaveasfile('w', initialfile='Untitled.txt', defaultextension="txt", parent=self.root, title="Save As", filetypes=(("Text Documents","*.txt"),("All Files","*.*")))
		if file_object!=None:
			content=self.text_field.get("1.0","end-1c")
			file_object.write(content)
			self.file_path=file_object.name
			self.root.title(self.file_path.split("/")[-1] +" - LinusPad" )			
			file_object.close()
		else:
			file_object=None
			pass
	def ExitLinusPad(self):
		screen_content=self.text_field.get("1.0", "end-1c")
		if self.file_path !="":
			file_before_new=open(self.file_path,"r")
			saved_file_content=file_before_new.read()
			file_before_new.close()
			if screen_content!=saved_file_content:
				do_you_want_to_save=askyesnocancel(title="LinusPad", message="Do yo want to save changes to\n %s?"%(self.file_path))
				if do_you_want_to_save:
					current_file=open(self.file_path,"w")
					current_file.write(screen_content)
					current_file.close()
					self.root.destroy()
				elif (do_you_want_to_save) == None:
					pass
				else:
					self.root.destroy()
			else:
				self.root.destroy()
		elif self.file_path=="" and len(screen_content)>0:
			do_you_want_to_save=askyesnocancel(title="LinusPad", message="Do yo want to save changes to Untitled?")
			if do_you_want_to_save:
				file_object=asksaveasfile('w', initialfile='Untitled.txt', defaultextension="txt", parent=self.root, title="Save As", filetypes=(("Text Documents","*.txt"),("All Files","*.*")))
				if file_object!=None:
					content=self.text_field.get("1.0","end-1c")
					file_object.write(screen_content)		
					file_object.close()
					self.root.destroy()
				else:
					file_object=None
					pass
			elif (do_you_want_to_save)==None:
				pass
			else:
				self.root.destroy()
		else:
			self.root.destroy()
		


	

	def menubars_func(self):
		menubar=Menu(self.root)
		self.root.config(menu=menubar)
		#------------------------------------------------------------------------------------------------
		filemenu=Menu(menubar, tearoff=0)
		filemenu.add_command(label="New", command=self.NewFile,accelerator="Ctrl+N")
		filemenu.add_command(label="Open...", command=self.OpenFile, accelerator="Ctrl+O")
		filemenu.add_command(label="Save", command=self.SaveFile,accelerator="Ctrl+S")
		filemenu.add_command(label="Save As...",command=self.SaveFile_as)
		filemenu.add_separator()
		filemenu.add_command(label="Page Setup...")
		filemenu.add_separator()
		filemenu.add_command(label='Print', accelerator="Ctrl+P")
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=self.ExitLinusPad)
		menubar.add_cascade(label="File", menu=filemenu, underline=1)
		#------------------------------------------------------------------------------------------------
		editmenu=Menu(menubar, tearoff=0)
		editmenu.add_command(label="Undo", accelerator="Ctrl+Z")
		editmenu.add_command(label="Cut", accelerator="Ctrl+X")
		editmenu.add_command(label="Copy", accelerator="Ctrl+C")
		editmenu.add_command(label="Paste", accelerator="Ctrl+V")
		editmenu.add_command(label="Delete", accelerator="Del")
		editmenu.add_separator()
		editmenu.add_command(label="Find...", accelerator="Ctrl+F")
		editmenu.add_command(label="Find Next", accelerator="F3")
		editmenu.add_command(label="Replace...", accelerator="Ctrl+H")
		editmenu.add_command(label="GoTo...", accelerator="Ctrl+G")
		editmenu.add_separator()
		editmenu.add_command(label="Select All", accelerator="Ctrl+A")
		editmenu.add_command(label="Time/Date", accelerator="F5")
		menubar.add_cascade(label="Edit",menu=editmenu, underline=1)
		#------------------------------------------------------------------------------------------------
		formatmenu=Menu(menubar, tearoff=0)
		formatmenu.add_checkbutton(label="Word Wrap")
		formatmenu.add_command(label="Font...")
		menubar.add_cascade(label="Format", menu=formatmenu, underline=1)
		#------------------------------------------------------------------------------------------------
		viewmenu=Menu(menubar, tearoff=0)
		viewmenu.add_checkbutton(label="Status Bar")
		menubar.add_cascade(label="View", menu=viewmenu,  underline=1)
		#------------------------------------------------------------------------------------------------
		helpmenu=Menu(menubar, tearoff=0)
		helpmenu.add_command(label="View Help")
		helpmenu.add_separator()
		helpmenu.add_command(label="About LinusPad")
		menubar.add_cascade(label="Help",  menu=helpmenu)

		
		
		

cd=LinusPad()

