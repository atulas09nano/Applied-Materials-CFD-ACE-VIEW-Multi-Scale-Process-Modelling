import GuiVersion
import GuiDBM
import GuiFILE
import GuiML
import GuiPT
import GuiMO
import GuiVC
import GuiRC
import GuiBC
import GuiIC
import GuiPC
import GuiFan
import GuiMacP
import GuiMR
import GuiMRF
import GuiViz
import GuiSC
import GuiOut
import GuiRun

#The following line is for backwards-compatibility, DO NOT DELETE IT.
GuiVersion.RecordVersion("2025.0.0.14081")

GuiFILE.SetMode("TOPO")
GuiFILE.Open(r"D:\IDM Download\Compressed\AMAT Software\Tutorials\test ccp etch\TOPO-Plasma-CCP-etch.DTF")
GuiMO.Set("Shared/NSteps", 100)
GuiMO.Set("Shared/NSteps", 1000)
GuiMO.Set("Shared/EndTime", 50)
GuiMO.Set("Shared/Title", "Si Etch by CF4")
GuiMO.Set("Shared/ReadFromACEModel", 1)
GuiMO.Set("Shared/ModelFileName", "D:\IDM Download\Compressed\AMAT Software\Tutorials\Solved\Plasma-CCP-Etch\Feature_TOPO\Results\ACE_Plasma-CCP_Etch_MC_1.001.FSC")
GuiFILE.Save()
