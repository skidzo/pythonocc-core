from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Geom import *
from OCC.Core.GeomAbs import *
from OCC.Core.Geom2d import *
from OCC.Core.GeomLProp import *


class LocalAnalysis_StatusErrorType(IntEnum):
	LocalAnalysis_NullFirstDerivative: int = ...
	LocalAnalysis_NullSecondDerivative: int = ...
	LocalAnalysis_TangentNotDefined: int = ...
	LocalAnalysis_NormalNotDefined: int = ...
	LocalAnalysis_CurvatureNotDefined: int = ...
LocalAnalysis_NullFirstDerivative = LocalAnalysis_StatusErrorType.LocalAnalysis_NullFirstDerivative
LocalAnalysis_NullSecondDerivative = LocalAnalysis_StatusErrorType.LocalAnalysis_NullSecondDerivative
LocalAnalysis_TangentNotDefined = LocalAnalysis_StatusErrorType.LocalAnalysis_TangentNotDefined
LocalAnalysis_NormalNotDefined = LocalAnalysis_StatusErrorType.LocalAnalysis_NormalNotDefined
LocalAnalysis_CurvatureNotDefined = LocalAnalysis_StatusErrorType.LocalAnalysis_CurvatureNotDefined

class localanalysis:
	pass

class LocalAnalysis_CurveContinuity:
	def __init__(self, Curv1: Geom_Curve, u1: float, Curv2: Geom_Curve, u2: float, Order: GeomAbs_Shape, EpsNul: Optional[float] = 0.001, EpsC0: Optional[float] = 0.001, EpsC1: Optional[float] = 0.001, EpsC2: Optional[float] = 0.001, EpsG1: Optional[float] = 0.001, EpsG2: Optional[float] = 0.001, Percent: Optional[float] = 0.01, Maxlen: Optional[float] = 10000) -> None: ...
	def C0Value(self) -> float: ...
	def C1Angle(self) -> float: ...
	def C1Ratio(self) -> float: ...
	def C2Angle(self) -> float: ...
	def C2Ratio(self) -> float: ...
	def ContinuityStatus(self) -> GeomAbs_Shape: ...
	def G1Angle(self) -> float: ...
	def G2Angle(self) -> float: ...
	def G2CurvatureVariation(self) -> float: ...
	def IsC0(self) -> bool: ...
	def IsC1(self) -> bool: ...
	def IsC2(self) -> bool: ...
	def IsDone(self) -> bool: ...
	def IsG1(self) -> bool: ...
	def IsG2(self) -> bool: ...
	def StatusError(self) -> LocalAnalysis_StatusErrorType: ...

class LocalAnalysis_SurfaceContinuity:
	@overload
	def __init__(self, Surf1: Geom_Surface, u1: float, v1: float, Surf2: Geom_Surface, u2: float, v2: float, Order: GeomAbs_Shape, EpsNul: Optional[float] = 0.001, EpsC0: Optional[float] = 0.001, EpsC1: Optional[float] = 0.001, EpsC2: Optional[float] = 0.001, EpsG1: Optional[float] = 0.001, Percent: Optional[float] = 0.01, Maxlen: Optional[float] = 10000) -> None: ...
	@overload
	def __init__(self, curv1: Geom2d_Curve, curv2: Geom2d_Curve, U: float, Surf1: Geom_Surface, Surf2: Geom_Surface, Order: GeomAbs_Shape, EpsNul: Optional[float] = 0.001, EpsC0: Optional[float] = 0.001, EpsC1: Optional[float] = 0.001, EpsC2: Optional[float] = 0.001, EpsG1: Optional[float] = 0.001, Percent: Optional[float] = 0.01, Maxlen: Optional[float] = 10000) -> None: ...
	@overload
	def __init__(self, EpsNul: Optional[float] = 0.001, EpsC0: Optional[float] = 0.001, EpsC1: Optional[float] = 0.001, EpsC2: Optional[float] = 0.001, EpsG1: Optional[float] = 0.001, Percent: Optional[float] = 0.01, Maxlen: Optional[float] = 10000) -> None: ...
	def C0Value(self) -> float: ...
	def C1UAngle(self) -> float: ...
	def C1URatio(self) -> float: ...
	def C1VAngle(self) -> float: ...
	def C1VRatio(self) -> float: ...
	def C2UAngle(self) -> float: ...
	def C2URatio(self) -> float: ...
	def C2VAngle(self) -> float: ...
	def C2VRatio(self) -> float: ...
	def ComputeAnalysis(self, Surf1: GeomLProp_SLProps, Surf2: GeomLProp_SLProps, Order: GeomAbs_Shape) -> None: ...
	def ContinuityStatus(self) -> GeomAbs_Shape: ...
	def G1Angle(self) -> float: ...
	def G2CurvatureGap(self) -> float: ...
	def IsC0(self) -> bool: ...
	def IsC1(self) -> bool: ...
	def IsC2(self) -> bool: ...
	def IsDone(self) -> bool: ...
	def IsG1(self) -> bool: ...
	def IsG2(self) -> bool: ...
	def StatusError(self) -> LocalAnalysis_StatusErrorType: ...

# harray1 classes
# harray2 classes
# hsequence classes

localanalysis_Dump = localanalysis.Dump
localanalysis_Dump = localanalysis.Dump
