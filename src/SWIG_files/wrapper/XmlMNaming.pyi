from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.XmlMDF import *
from OCC.Core.Message import *
from OCC.Core.TopTools import *
from OCC.Core.TDF import *
from OCC.Core.XmlObjMgt import *
from OCC.Core.TopAbs import *
from OCC.Core.TopoDS import *


class xmlmnaming:
	@staticmethod
	def AddDrivers(aDriverTable: XmlMDF_ADriverTable, aMessageDriver: Message_Messenger) -> None: ...

class XmlMNaming_NamedShapeDriver(XmlMDF_ADriver):
	def __init__(self, aMessageDriver: Message_Messenger) -> None: ...
	def Clear(self) -> None: ...
	def GetShapesLocations(self) -> TopTools_LocationSet: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	@overload
	def Paste(self, theSource: XmlObjMgt_Persistent, theTarget: TDF_Attribute, theRelocTable: XmlObjMgt_RRelocationTable) -> bool: ...
	@overload
	def Paste(self, theSource: TDF_Attribute, theTarget: XmlObjMgt_Persistent, theRelocTable: XmlObjMgt_SRelocationTable) -> None: ...
	def ReadShapeSection(self, anElement: XmlObjMgt_Element) -> None: ...
	def WriteShapeSection(self, anElement: XmlObjMgt_Element) -> None: ...

class XmlMNaming_NamingDriver(XmlMDF_ADriver):
	def __init__(self, aMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	@overload
	def Paste(self, theSource: XmlObjMgt_Persistent, theTarget: TDF_Attribute, theRelocTable: XmlObjMgt_RRelocationTable) -> bool: ...
	@overload
	def Paste(self, theSource: TDF_Attribute, theTarget: XmlObjMgt_Persistent, theRelocTable: XmlObjMgt_SRelocationTable) -> None: ...

class XmlMNaming_Shape1:
	@overload
	def __init__(self, Doc: XmlObjMgt_Document) -> None: ...
	@overload
	def __init__(self, E: XmlObjMgt_Element) -> None: ...
	@overload
	def Element(self) -> XmlObjMgt_Element: ...
	@overload
	def Element(self) -> XmlObjMgt_Element: ...
	def LocId(self) -> int: ...
	def Orientation(self) -> TopAbs_Orientation: ...
	def SetShape(self, ID: int, LocID: int, Orient: TopAbs_Orientation) -> None: ...
	def SetVertex(self, theVertex: TopoDS_Shape) -> None: ...
	def TShapeId(self) -> int: ...

# harray1 classes
# harray2 classes
# hsequence classes

xmlmnaming_AddDrivers = xmlmnaming.AddDrivers
