from BlochSphere import *
import tkinter as tk
from  tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Qubita Class Inherits all the Sphere and Vector State attributes and plots on MatPlotlib Figure 
class Qubita(BlochSphere, StateVector):
    def __init__(self, QubitaRadius, x=float, y=float, z=float):
        # pass initial parameters to Super classes
        BlochSphere.__init__(self, QubitaRadius)
        StateVector.__init__(self, x, y, z)

        # Plot State and Qubit Sphere
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection="3d")
        self.ax.scatter([0], [0], [0], color='r', s=50) 
        self.QubitSphere = self.ax.plot_wireframe(self.x, self.y, self.z, color="b", alpha=0.3) # Sphere plot
        self.Vector = self.ax.quiver(self.VECTORTAIL[0], self.VECTORTAIL[1], self.VECTORTAIL[2], 
              self.vectorState[0], self.vectorState[0], self.vectorState[2],
              color = 'r', length=1, normalize=True, arrow_length_ratio = 0.20)
        self.ax.axis('off')
        
    def RotateVector(self, theta, phi):
        StateVector.RotateVector(self, theta, phi)
        self.Vector.remove()
        self.fig.canvas.draw_idle()
        self.Vector = self.ax.quiver(self.VECTORTAIL[0], self.VECTORTAIL[1], self.VECTORTAIL[2], 
              self.vectorState[0], self.vectorState[1], self.vectorState[2],
              color = 'r', length=1, normalize=True, arrow_length_ratio = 0.20)

    def Measure(self):
        StateVector.Measure(self)
        self.Vector.remove()
        self.fig.canvas.draw_idle()
        self.Vector = self.ax.quiver(self.VECTORTAIL[0], self.VECTORTAIL[1], self.VECTORTAIL[2], 
              self.vectorState[0], self.vectorState[1], self.vectorState[2],
              color = 'r', arrow_length_ratio = 0.20)

    def InitSuperposition(self):
        if type(StateVector.InitSuperposition(self)) == str:
            # return the message to be used by error message box later
          return StateVector.InitSuperposition(self)
        StateVector.InitSuperposition(self)
        self.Vector.remove()
        self.fig.canvas.draw_idle()
        self.Vector = self.ax.quiver(self.VECTORTAIL[0], self.VECTORTAIL[1], self.VECTORTAIL[2], 
              self.vectorState[0], self.vectorState[1], self.vectorState[2],
              color = 'r', length=1, normalize=True, arrow_length_ratio = 0.20)    

    def PauliX(self):
        StateVector.PauliX(self)
        self.Vector.remove()
        self.fig.canvas.draw_idle()
        self.Vector = self.ax.quiver(self.VECTORTAIL[0], self.VECTORTAIL[1], self.VECTORTAIL[2], 
              self.vectorState[0], self.vectorState[1], self.vectorState[2],
              color = 'r', length=1, normalize=True, arrow_length_ratio = 0.20)
    
    def PauliY(self):
        StateVector.PauliY(self)
        self.Vector.remove()
        self.fig.canvas.draw_idle()
        self.Vector = self.ax.quiver(self.VECTORTAIL[0], self.VECTORTAIL[1], self.VECTORTAIL[2], 
              self.vectorState[0], self.vectorState[1], self.vectorState[2],
              color = 'r', length=1, normalize=True, arrow_length_ratio = 0.20)
    
    def PauliZ(self):
        StateVector.PauliZ(self)
        self.Vector.remove()
        self.fig.canvas.draw_idle()
        self.Vector = self.ax.quiver(self.VECTORTAIL[0], self.VECTORTAIL[1], self.VECTORTAIL[2], 
              self.vectorState[0], self.vectorState[1], self.vectorState[2],
              color = 'r', length=1, normalize=True, arrow_length_ratio = 0.20)
        
    def PhaseGate(self):
        StateVector.PhaseGate(self)
        self.Vector.remove()
        self.fig.canvas.draw_idle()
        self.Vector = self.ax.quiver(self.VECTORTAIL[0], self.VECTORTAIL[1], self.VECTORTAIL[2], 
              self.vectorState[0], self.vectorState[1], self.vectorState[2],
              color = 'r', length=1, normalize=True, arrow_length_ratio = 0.20)
    
    def TGate(self):
        StateVector.TGate(self)
        self.Vector.remove()
        self.fig.canvas.draw_idle()
        self.Vector = self.ax.quiver(self.VECTORTAIL[0], self.VECTORTAIL[1], self.VECTORTAIL[2], 
              self.vectorState[0], self.vectorState[1], self.vectorState[2],
              color = 'r', length=1, normalize=True, arrow_length_ratio = 0.20)
    
    def HadamardGate(self):
        StateVector.HadamardGate(self)
        self.Vector.remove()
        self.fig.canvas.draw_idle()
        self.Vector = self.ax.quiver(self.VECTORTAIL[0], self.VECTORTAIL[1], self.VECTORTAIL[2], 
              self.vectorState[0], self.vectorState[1], self.vectorState[2],
              color = 'r', length=1, normalize=True, arrow_length_ratio = 0.20)
        
     
def main():
    # Run Functions
    def RunTransform():
        # ensure that entry is not empty
        if thetaEntry.get() == '' or phiEntry.get() == '':
            messagebox.showerror('Input Error', 'Some Values are missing')
            return
        # store entry values in variable
        thetaValue = float(thetaEntry.get())
        phiValue = float(phiEntry.get())
        # pass variables as argument to Qubit RotateVector method
        Qubit.RotateVector(thetaValue, phiValue)
        # Update current state display
        currentState = f"Current State: x = {Qubit.vectorState[0]}, y = {Qubit.vectorState[1]}, z = {Qubit.vectorState[2]}"
        currentStateLabel.config(text=currentState)
    
    def RunMeasure():
        # Qubit Measure method
        Qubit.Measure()
        # display 1 or 0 depending on what measure does
        if Qubit.vectorState[2] == 1:
            measureLabel.config(text='Last Measure: 0')
        elif Qubit.vectorState[2] ==  -1:
            measureLabel.config(text='Last Measure: 1')
        
        # Update current state display
        currentState = f"Current State: x = {Qubit.vectorState[0]}, y = {Qubit.vectorState[1]}, z = {Qubit.vectorState[2]}"
        currentStateLabel.config(text=currentState)

    def RunSuperpostion():
        # Check if there is an error in running superposition and display
        if type(Qubit.InitSuperposition()) == str:
            error =  Qubit.InitSuperposition()
            messagebox.showerror('Superpostion Error', error)
            return
        else:
            # if no errors run the method
            Qubit.InitSuperposition()
        # Updare current state display
        currentState = f"Current State: x = {Qubit.vectorState[0]}, y = {Qubit.vectorState[1]}, z = {Qubit.vectorState[2]}"
        currentStateLabel.config(text=currentState)
    
    # All gates run appropriate methd and update state
    def RunPauliXGate():
        Qubit.PauliX()
        currentState = f"Current State: x = {Qubit.vectorState[0]}, y = {Qubit.vectorState[1]}, z = {Qubit.vectorState[2]}"
        currentStateLabel.config(text=currentState)

    def RunPauliYGate():
        Qubit.PauliY()
        currentState = f"Current State: x = {Qubit.vectorState[0]}, y = {Qubit.vectorState[1]}, z = {Qubit.vectorState[2]}"
        currentStateLabel.config(text=currentState)
    
    def RunPauliZGate():
        Qubit.PauliZ()
        currentState = f"Current State: x = {Qubit.vectorState[0]}, y = {Qubit.vectorState[1]}, z = {Qubit.vectorState[2]}"
        currentStateLabel.config(text=currentState)
    
    def RunPhaseGate():
        Qubit.PhaseGate()
        currentState = f"Current State: x = {Qubit.vectorState[0]}, y = {Qubit.vectorState[1]}, z = {Qubit.vectorState[2]}"
        currentStateLabel.config(text=currentState)
    
    def RunTGate():
        Qubit.TGate()
        currentState = f"Current State: x = {Qubit.vectorState[0]}, y = {Qubit.vectorState[1]}, z = {Qubit.vectorState[2]}"
        currentStateLabel.config(text=currentState)

    def RunHadamardGate():
        Qubit.HadamardGate()
        currentState = f"Current State: x = {Qubit.vectorState[0]}, y = {Qubit.vectorState[1]}, z = {Qubit.vectorState[2]}"
        currentStateLabel.config(text=currentState)
    
    # validation functions
    def ValidateTheta(thetaEntry):
        # make sure it takes empty string values
        if thetaEntry == "":
            errorLabel.config(text='')
            return True
        try:
            floatValue = float(thetaEntry)
            # check if float and ensure it is within range
            if 0 <= floatValue <= 180:
                errorLabel.config(text='')
                return True
            else:
                errorLabel.config(text='Theta must be between 0 and 180')
                return False
        # return error message and reject value if number is not entered
        except ValueError:
            errorLabel.config(text='Invalid Entry')
            return False
    def ValidatePhi(phiEntry):
        if phiEntry == "":
            errorLabel.config(text='')
            return True
        try:
            floatValue = float(phiEntry)
            if 0 <= floatValue <= 360:
                error_msg.set("")
                return True
            else:
                errorLabel.config(text='Phi must be between 0 and 360')
                return False
        except ValueError:
            errorLabel.config(text='Invalid Entry')
            return False
        
    # Create Qubita Window and Qubit object by instatiating Qubita Class
    Qubit = Qubita(1, 0, 0, 1)
    QubitaWindow = tk.Tk()
    QubitaWindow.title("Qubita")
    QubitaWindow.iconbitmap('QUBITA ICON.ico')
    QubitaWindow.rowconfigure(0, weight=1)
    QubitaWindow.rowconfigure(1, weight=2)
    QubitaWindow.columnconfigure(0, weight=1)
    
    # Qubit in Qubita Window
    qubitObjectFrame = tk.Frame(master=QubitaWindow)
    canvas = FigureCanvasTkAgg(Qubit.fig, master=qubitObjectFrame)
    canvas.draw()
    # canvas widget
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(expand=True, fill='both')
    qubitObjectFrame.grid(row=0, column=0, sticky='nsew')
    
    # create validation variables for user inputs using the functions
    validatetheta = (QubitaWindow.register(ValidateTheta), '%P')
    validatephi = (QubitaWindow.register(ValidatePhi), '%P')
    error_msg = tk.StringVar()

    # User Interface Frame
    userInterfaceMasterFrame = ttk.Frame(master=QubitaWindow)
    userInterfaceFrame = tk.Frame(master=userInterfaceMasterFrame, borderwidth=2, relief='solid')
    userInterfaceFrame.rowconfigure(0, weight=1)
    userInterfaceFrame.rowconfigure(1, weight=1)
    userInterfaceFrame.rowconfigure(2, weight=1)
    userInterfaceFrame.rowconfigure(3, weight=1)
    #userInterfaceFrame.rowconfigure(4, weight=1)
    userInterfaceFrame.columnconfigure(0, weight=1)
    

    # Current state and Last measure label
    currentState = f"Current State: x = {Qubit.vectorState[0]}, y = {Qubit.vectorState[1]}, z = {Qubit.vectorState[2]}" # string to pass
    currentStateAndMeasureResultFrame = ttk.Frame(master=userInterfaceFrame)
    measureLabel = ttk.Label(master=currentStateAndMeasureResultFrame,
                             font = 'Calibri 12',
                             text = "Last Measure: "
                             )
    currentStateLabel = ttk.Label(master=currentStateAndMeasureResultFrame, font='Calibri 12', text=currentState)
    currentStateLabel.pack()
    measureLabel.pack()
    currentStateAndMeasureResultFrame.grid(row=0, column = 0)

    # Transform Frame
    transformFrame = ttk.Frame(master=userInterfaceFrame) 
    thetaLabel = ttk.Label(master=transformFrame, text="θ = ")
    thetaEntry = ttk.Entry(master=transformFrame,
                           validate="key", 
                           validatecommand=validatetheta)
    phiLabel = ttk.Label(master=transformFrame, text="φ = ")
    phiEntry = ttk.Entry(master=transformFrame, 
                         validate="key", 
                         validatecommand=validatephi)

    transformButton = ttk.Button(master=transformFrame, 
                                 text="Transform", width=20, 
                                 command=RunTransform)
    errorLabel = tk.Label(master = transformFrame, text='')
    transformButton.pack(side='left')
    thetaLabel.pack(side='left')
    thetaEntry.pack(side='left')
    phiLabel.pack(side='left')
    phiEntry.pack(side='left')
    errorLabel.pack(side='top')
    transformFrame.grid(row=1, column=0)
    
    
    # Measure and superposition button
    measureSuperpositionFrame = ttk.Frame(master=userInterfaceFrame)
    measureButton = ttk.Button(master=measureSuperpositionFrame, 
                              text="Measure", 
                              width=20,
                              command=RunMeasure)
    superpositionButton = ttk.Button(master=measureSuperpositionFrame, 
                                     text="Initiate Superposition",
                                     width=20,
                                     command=RunSuperpostion)
    measureButton.pack(side='left')
    superpositionButton.pack(side='right')
    measureSuperpositionFrame.grid(row=2, column=0)

    # Gates Frame
    gatesFrame = ttk.Frame(master=userInterfaceFrame)
    pauliXButton = ttk.Button(master=gatesFrame, 
                              text='Apply PauliX Gate', 
                              width=20, 
                              command=RunPauliXGate)
    pauliYButton = ttk.Button(master=gatesFrame, 
                              text='Apply PauliY Gate', 
                              width=20, 
                              command=RunPauliYGate)
    pauliZButton = ttk.Button(master=gatesFrame, 
                              text='Apply PauliZ Gate', 
                              width=20, 
                              command=RunPauliZGate)
    
    phaseGateButton = ttk.Button(master=gatesFrame, 
                                 text='Apply Phase Gate', 
                                 width=20, 
                                 command=RunPhaseGate)
    
    TGateButtonButton = ttk.Button(master=gatesFrame,
                             text='Apply T Gate',
                             width=20,
                             command=RunTGate)
    
    hadamardGateButton = ttk.Button(master=gatesFrame, 
                                    text='Apply Hadamard Gate', 
                                    width=20, 
                                    command=RunHadamardGate)
    
    pauliXButton.pack(side='left')
    pauliYButton.pack(side='left')
    pauliZButton.pack(side='left')
    phaseGateButton.pack(side='left')
    TGateButtonButton.pack(side='left')
    hadamardGateButton.pack(side='left')
    gatesFrame.grid(row=3, column=0)
    


    userInterfaceFrame.pack(expand=True, fill='both')
    userInterfaceMasterFrame.grid(row=1, column=0, sticky='nsew')

    QubitaWindow.mainloop()

if __name__ == "__main__":
    main()

