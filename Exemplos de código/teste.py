import pygtk
pygtk.require('2.0')
import gtk
import gtk.glade 
class Editar():
    def __init__(self):
        
        self.xml = gtk.glade.XML('ImobSystem.glade')
        self.windowFuncionario = self.xml.get_widget('EditarFuncionario')
        self.windowFuncionario.show_all()
            
m = Editar()
gtk.main()
