from tkinter import *
from pygame import mixer
from tkinter import filedialog
class MusicPlayer:
    def __init__(self,window):
        window.geometry('320x120')
        window.title('MusicPlayer')
        window.resizable(0,0)
        Load=Button(window,text='Load',width=10,font=('times',10),command=self.load)
        Play=Button(window,text='play',width=10,font=('times',10),command=self.play)
        Pause=Button(window,text='Pause',width=10,font=('times',10),command=self.pause)
        Stop=Button(window,text='Stop',width=10,font=('times',10),command=self.stop)
        Load.place(x=0,y=20)
        Play.place(x=110,y=20)
        Pause.place(x=220,y=20)
        Stop.place(x=110,y=60)
        self.music_file=False
        self.playing_state=False
    def load(self):
        self.music_file=filedialog.askopenfile()
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state=False
    def stop(self):
        mixer.music.stop()
root=Tk()
app=MusicPlayer(root)
root.mainloop()