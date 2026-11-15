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

GuiFILE.SetMode("ACEU")
GuiFILE.Open(r"\\amat.com\Folders\India\SSG\CAECoC_BUs\CPS\from_GTS\To_Dhritiman\IIT-M_Workshop_23Oct25\Tutorials\Plasma-CCP-Etch\Reactor_ACE\Results\ACE_Plasma-CCP_Etch.DTF")
GuiPT.Set("Electr", 0)
GuiPT.Set("Plasma", 0)
GuiPT.Set("Chem", 0)
GuiPT.Set("Flow", 0)
GuiFILE.SaveAs(r"\\amat.com\Folders\India\SSG\CAECoC_BUs\CPS\from_GTS\To_Dhritiman\IIT-M_Workshop_23Oct25\Tutorials\Plasma-CCP-Etch\Reactor_ACE\Results\ACE_Plasma-CCP_Etch_Fresh.DTF")
