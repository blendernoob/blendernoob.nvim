
'''
Stub class file for:
OpenMayaAnim

Maya2024 Python API stub file
Pycharm Version
Generated from original Maya documentation.
Autodesk Maya2024  c1997-2023 Autodesk, Inc. All rights reserved. 
'''


from typing import overload




class MAnimControl:
    '''Control over animation playback and values.
This class provide access to the values that control how an
animation is played. This includes the minimum and maximum frames
included in the playback, whether the playback loops, and whether
the animation runs in all views, or only the active view, etc.
Methods also exist that mirror the functionality of the controls
found on the time slider in the UI to start and stop the
playback.
'''
    def __init__(self):
        pass


    def isValid(self): 
        '''
        isValid(self) -> bool

        Synopsis
        -----
        Introduced in 2020.0 Return if the AnimControl is valid.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def playbackMode(self): 
        '''
        playbackMode(self) -> MAnimControl.MAnimControl

        Synopsis
        -----
        Return the playback mode currently in effect.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setPlaybackMode(self, newMode: MAnimControl.PlaybackMode): 
        '''
        setPlaybackMode(self, newMode: MAnimControl.PlaybackMode)

        Synopsis
        -----
        Set the current playback mode.

        Returns:
        -----
        None

        Parameters:
        -----
        newMode: MAnimControl.PlaybackMode
        	[in] -> an element of 


        '''
        pass

    def viewMode(self): 
        '''
        viewMode(self) -> MAnimControl.MAnimControl

        Synopsis
        -----
        Return the viewing mode currently in effect.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setViewMode(self, newMode: MAnimControl.PlaybackViewMode): 
        '''
        setViewMode(self, newMode: MAnimControl.PlaybackViewMode)

        Synopsis
        -----
        Set the current viewing mode. Controls whether the animation is
        run in only the active view, or simultaneously in all views.

        Returns:
        -----
        None

        Parameters:
        -----
        newMode: MAnimControl.PlaybackViewMode
        	[in] -> an element of 


        '''
        pass

    def playbackBy(self): 
        '''
        playbackBy(self) -> double

        Synopsis
        -----
        Return a double specifying the increment between times viewed
        during the playing of the animation.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setPlaybackBy(self, newTime: double): 
        '''
        setPlaybackBy(self, newTime: double)

        Synopsis
        -----
        Specify the increment between times viewed during the playing of
        the animation.

        Returns:
        -----
        None

        Parameters:
        -----
        newTime: double
        	[in] -> a double containing the new increment


        '''
        pass

    def minTime(self): 
        '''
        minTime(self) -> MTime

        Synopsis
        -----
        Return an MTime specifying the first frame of the current
        playback time range. This corresponds to the minTime which can
        also be set and queried using the playbackOptions mel command. It
        does not represent the first frame of the total animation time
        unless the two coincide.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def maxTime(self): 
        '''
        maxTime(self) -> MTime

        Synopsis
        -----
        Return an MTime specifying the last frame of the current playback
        time range. This corresponds to the maxTime which can also be set
        and queried using the playbackOptions mel command. It does not
        represent the final frame of the total animation time unless the
        two coincide.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setMinTime(self, newMinTime: MTime): 
        '''
        setMinTime(self, newMinTime: MTime)

        Synopsis
        -----
        Set the first frame of the current playback time range.

        Returns:
        -----
        None

        Parameters:
        -----
        newMinTime: MTime
        	[in] -> an 


        '''
        pass

    def setMaxTime(self, newMaxTime: MTime): 
        '''
        setMaxTime(self, newMaxTime: MTime)

        Synopsis
        -----
        Set the value of the last frame of the current playback time
        range.

        Returns:
        -----
        None

        Parameters:
        -----
        newMaxTime: MTime
        	[in] -> an 


        '''
        pass

    def setMinMaxTime(self, min: MTime,
                        max: MTime): 
        '''
        setMinMaxTime(self, min: MTime,
                        max: MTime)

        Synopsis
        -----
        Set the values of the first and last frames of the playback time
        range.

        Returns:
        -----
        None

        Parameters:
        -----
        min: MTime
        	[in] -> an 

        max: MTime
        	[in] -> an 


        '''
        pass

    def animationStartTime(self): 
        '''
        animationStartTime(self) -> MTime

        Synopsis
        -----
        Return an MTime specifying the first frame of the animation, as
        specified by the Maya user in the Range Slider UI. This
        corresponds to the animationStartTime which can also be set and
        queried using the playbackOptions mel command.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def animationEndTime(self): 
        '''
        animationEndTime(self) -> MTime

        Synopsis
        -----
        Return an MTime specifying the last frame of the animation, as
        specified by the Maya user in the Range Slider UI. This
        corresponds to the animationEndTime which can also be set and
        queried using the playbackOptions mel command.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setAnimationStartTime(self, newStartTime: MTime): 
        '''
        setAnimationStartTime(self, newStartTime: MTime)

        Synopsis
        -----
        Set the value of the first frame in the animation.

        Returns:
        -----
        None

        Parameters:
        -----
        newStartTime: MTime
        	[in] -> an 


        '''
        pass

    def setAnimationEndTime(self, newEndTime: MTime): 
        '''
        setAnimationEndTime(self, newEndTime: MTime)

        Synopsis
        -----
        Set the value of the last frame in the animation.

        Returns:
        -----
        None

        Parameters:
        -----
        newEndTime: MTime
        	[in] -> an 


        '''
        pass

    def setAnimationStartEndTime(self, newStartTime: MTime,
                        newEndTime: MTime): 
        '''
        setAnimationStartEndTime(self, newStartTime: MTime,
                        newEndTime: MTime)

        Synopsis
        -----
        Set the values of the first and last frames in the animation.

        Returns:
        -----
        None

        Parameters:
        -----
        newStartTime: MTime
        	[in] -> an 

        newEndTime: MTime
        	[in] -> an 


        '''
        pass

    def currentTime(self): 
        '''
        currentTime(self) -> MTime

        Synopsis
        -----
        Return an MTime instance containing the current animation frame.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setCurrentTime(self, newTime: MTime): 
        '''
        setCurrentTime(self, newTime: MTime)

        Synopsis
        -----
        Set the current animation frame.

        Returns:
        -----
        None

        Parameters:
        -----
        newTime: MTime
        	[in] -> an 


        '''
        pass

    def playbackSpeed(self): 
        '''
        playbackSpeed(self) -> double

        Synopsis
        -----
        Return the speed with with to play the animation.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setPlaybackSpeed(self, newSpeed: double): 
        '''
        setPlaybackSpeed(self, newSpeed: double)

        Synopsis
        -----
        Set the desired speed factor at which the animation will play
        back.

        Returns:
        -----
        None

        Parameters:
        -----
        newSpeed: double
        	[in] -> the new speed factor


        '''
        pass

    def playForward(self): 
        '''
        playForward(self)

        Synopsis
        -----
        Start playing the current animation forwards.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def playBackward(self): 
        '''
        playBackward(self)

        Synopsis
        -----
        Start playing the current animation backwards.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def isPlaying(self): 
        '''
        isPlaying(self) -> bool

        Synopsis
        -----
        Return a value indicating whether Maya is currently playing the
        animation.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def isScrubbing(self): 
        '''
        isScrubbing(self) -> bool

        Synopsis
        -----
        Return a value indicating whether interactive scrubbing is
        occuring while Maya is not currently playing an animation.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def stop(self): 
        '''
        stop(self)

        Synopsis
        -----
        Stop playing the current animation.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def autoKeyMode(self): 
        '''
        autoKeyMode(self) -> bool

        Synopsis
        -----
        Return the autoKeyMode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setAutoKeyMode(self, mode: bool): 
        '''
        setAutoKeyMode(self, mode: bool)

        Synopsis
        -----
        Set the autoKeyMode.

        Returns:
        -----
        None

        Parameters:
        -----
        mode: bool
        	[in] -> a boolean specifying the new mode


        '''
        pass

    def globalInTangentType(self, ReturnStatus: MAnimControl.MStatus): 
        '''
        globalInTangentType(self, ReturnStatus: MAnimControl.MStatus) -> MFnAnimCurve.MFnAnimCurve

        Synopsis
        -----
        Return the current global in tangent type.

        Returns: 
        ----- 
        MFnAnimCurve::TangentType the current global in tangent type

        Parameters:
        -----
        ReturnStatus: MAnimControl.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def setGlobalInTangentType(self, tangentType: MFnAnimCurve.MFnAnimCurve): 
        '''
        setGlobalInTangentType(self, tangentType: MFnAnimCurve.MFnAnimCurve)

        Synopsis
        -----
        Set the current global in tangent type.

        Returns:
        -----
        None

        Parameters:
        -----
        tangentType: MFnAnimCurve.MFnAnimCurve
        	[in] -> the global in tangent type to set [Note: 


        '''
        pass

    def globalOutTangentType(self, ReturnStatus: MAnimControl.MStatus): 
        '''
        globalOutTangentType(self, ReturnStatus: MAnimControl.MStatus) -> MFnAnimCurve.MFnAnimCurve

        Synopsis
        -----
        Return the current global out tangent type.

        Returns: 
        ----- 
        The current global out tangent type

        Parameters:
        -----
        ReturnStatus: MAnimControl.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def setGlobalOutTangentType(self, tangentType: MFnAnimCurve.MFnAnimCurve): 
        '''
        setGlobalOutTangentType(self, tangentType: MFnAnimCurve.MFnAnimCurve)

        Synopsis
        -----
        Set the current global out tangent type.

        Returns:
        -----
        None

        Parameters:
        -----
        tangentType: MFnAnimCurve.MFnAnimCurve
        	[in] -> the global out tangent type to set [Note: 


        '''
        pass

    def weightedTangents(self, ReturnStatus: MAnimControl.MStatus): 
        '''
        weightedTangents(self, ReturnStatus: MAnimControl.MStatus) -> bool

        Synopsis
        -----
        Determine whether or not the tangents on the Anim Curve are
        weighted.

        Returns: 
        ----- 
        true the tangents on the Anim Curve are weighted  false the
        tangents on the Anim Curve are not weighted

        Parameters:
        -----
        ReturnStatus: MAnimControl.MStatus
        	[out] -> Status Code


        '''
        pass

    def setWeightedTangents(self, weightState: bool): 
        '''
        setWeightedTangents(self, weightState: bool)

        Synopsis
        -----
        Sets whether or not the tangents on the Anim Curve are weighted.
        Note: switching a curve from weightedTangents true to false and
        back to true again will not preserve fixed tangents properly. Use
        undo instead.

        Returns:
        -----
        None

        Parameters:
        -----
        weightState: bool
        	[in] -> a boolean specifying whether tangents should be weighted or not


        '''
        pass

class PlaybackMode:
    '''Animation playback modes. 
    Non-functional class.  Values for this enum:
    kPlaybackOnce
    kPlaybackLoop
    kPlaybackOscillate
    '''

    def __init__(self):
        pass

    def kPlaybackOnce(self):
        '''This is an enum of PlaybackMode.
        - Description: Play once then stop. 
        - Value: 0
        '''
        pass

    def kPlaybackLoop(self):
        '''This is an enum of PlaybackMode.
        - Description: Play continuously. 
        - Value: 1
        '''
        pass

    def kPlaybackOscillate(self):
        '''This is an enum of PlaybackMode.
        - Description: Play forwards, then backwards continuously. 
        - Value: 2
        '''
        pass

class PlaybackViewMode:
    '''Animation playback viewing modes. 
    Non-functional class.  Values for this enum:
    kPlaybackViewAll
    kPlaybackViewActive
    '''

    def __init__(self):
        pass

    def kPlaybackViewAll(self):
        '''This is an enum of PlaybackViewMode.
        - Description: Playback in all views. 
        - Value: 0
        '''
        pass

    def kPlaybackViewActive(self):
        '''This is an enum of PlaybackViewMode.
        - Description: Playback in only the active view. 
        - Value: 1
        '''
        pass

class MAnimCurveChange:
    '''Anim Curve Change Cache.
Adding, removing and changing keyframes on an anim curve cannot
be done simply by setting attribute values on the corresponding
node. This makes it impossible to capture such changes in an
MDGModifier for undo/redo purposes.
The
MAnimCurveChange class provides persistent storage for information concerning
changes to anim curve nodes, along with methods to undo and redo
those changes.
MFnAnimCurve methods which add, remove or change keyframes take an optional
MAnimCurveChange instance in which to store information about the changes being
made.
If the same
MAnimCurveChange instance is used for multiple anim curve edit operations, then
the cache maintains an undo/redo queue which allows all changes
in the series to be undone or redone. If selective undo/redo is
required, then a different MAnimCurveCache instance must be used
for each edit.
'''
    def __init__(self):
        pass


    def undoIt(self): 
        '''
        undoIt(self)

        Synopsis
        -----
        Undoes all of the Anim Curve edits that have been given to this
        cache.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def redoIt(self): 
        '''
        redoIt(self)

        Synopsis
        -----
        Redoes all of the Anim Curve edits that this cache previously
        undid. It is only valid to invoke this method after an undo on
        this cache.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def isInteractive(self): 
        '''
        isInteractive(self) -> bool

        Synopsis
        -----
        Return the performance hint flag value.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setInteractive(self, value: bool): 
        '''
        setInteractive(self, value: bool)

        Synopsis
        -----
        The interactive flag is a performance hint. If the flag is set to
        true new edits will be merged with the key from previous edit.
        For example if you are dragging the key each drag will be merged
        so only the last edit of the drag is safed. If the curves have a
        lot of scattered edit this merge will not scale well, so it is
        best to to it to false in this case.

        Returns:
        -----
        None

        Parameters:
        -----
        value: bool
        	[in] -> the value to set the flag. 


        '''
        pass

    def className(self): 
        '''
        className(self) -> char*

        Synopsis
        -----
        Returns the name of this class.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MAnimCurveClipboard:
    '''Control over the animation clipboard.
The clipboard is a list of MAnimCurveClipboardItems (i.e. an
MAnimCurveClipboardItemArray). All of the data stored on a clipboard remains static; that is,
it will persist as long as the application remains running.
The items on the clipboard must be ordered. In the case where the
clipboard info represents animation of a hierarchy, the order in
which items appear in the clipboard is reliant on a depth-first-
iteration from the root or the hierarchy. This ordering, is
essential to properly match up hierarchies of objects
As an example, consider that animation from the following
hierarchy is placed into the clipboard. Slanted Dag Objects are
animated.
In this example, the object labelled "C" has translate{X,Y,Z}
animated, while all the others only have one animated attribute
(excluding objects B and F, which have no animated attributes).
Using notation where A(r,c,a) represents the animCurve driving
object "A", which is at row "r" in its subhierarchy, has "c"
children, and "a" animated attributes these items would appear in
the clipboard in this order (i.e. depth-first with each object's
attributes explicitly indexed before continuing down the
hierarchy):
For example C(2,1,2) would mean that the object C resides on the
second level of the subhierarchy and has one child. The last "2"
is simply used as an index to count the number of animated
attributes on this object.
Multiple objects can be represented on the clipboard in this
manner. In the example above, if we had a separate second object
with no children, "J", it would appear at the end of the array as
J(0,0,0).
Note that although B and F contain no animation data themselves,
they must still be placed on the clipboard as placeholders to
preserve the hierarchy information. A placeholder object is
defined by a NULL value for the
MAnimCurveClipboardItem's animCurve.
There is a special clipboard that remains static. It can be
accessed by
MAnimCurveClipboard::theAPIClipboard().
'''
    def __init__(self):
        pass


    @overload
    def set(self, cb: MAnimCurveClipboard): 
        '''
        set(self, cb: MAnimCurveClipboard)

        Synopsis
        -----
        Replaces the contents of the clipboard.

        Returns:
        -----
        None

        Parameters:
        -----
        cb: MAnimCurveClipboard
        	[in] -> the clipboard to copy


        '''
        pass

    @overload
    def set(self, clipboardItemArray: MAnimCurveClipboardItemArray): 
        '''
        set(self, clipboardItemArray: MAnimCurveClipboardItemArray)

        Synopsis
        -----
        Sets the contents of the clipboard. The leading offset
        information is not preserved if this method is used. For example,
        if the keys on the animCurve you wish to cut fall within the
        range of 10 to 20 frames, and a startTime of 3 is specified, the
        leading offset of 7 frames is not preserved.

        Returns:
        -----
        None

        Parameters:
        -----
        clipboardItemArray: MAnimCurveClipboardItemArray
        	[in] -> the array of clipboard items to load on to the current clipboard


        '''
        pass

    @overload
    def set(self, clipboardItemArray: MAnimCurveClipboardItemArray,
                        startTime: MTime,
                        endTime: MTime,
                        startUnitlessInput: float,
                        endUnitlessInput: float,
                        strictValidation: bool): 
        '''
        set(self, clipboardItemArray: MAnimCurveClipboardItemArray,
                        startTime: MTime,
                        endTime: MTime,
                        startUnitlessInput: float,
                        endUnitlessInput: float,
                        strictValidation: bool)

        Synopsis
        -----
        Sets the contents of the clipboard. The start and end arguments
        are used to preserve offset information. For example, if the keys
        on the animCurve you wish to cut fall within the range of 10 to
        20 frames, and a startTime of 3 is specified, the offset of 7
        frames is preserved.The arguments startTime and endTime are used
        to specify the range for animCurves of type kAnimCurveT*, while
        startUnitlessInput and endUnitlessInput are used to specify the
        range for animCurves of type kAnimCurveU*.If the values of the
        MTime and float arguments are reversed (i.e. startTime > endTime
        or startUnitlessInput > endUnitlessInput ) then the range to be
        placed on the clipboard will be determined by the first and last
        key on the animCurves (i.e. leading offset information will not
        be preserved).The start and end values must also bound the
        animation (i.e. the first and last key respectively), otherwise
        this method will fail. If there is no animation on any of the
        items being placed on the clipboard, the range is ignored.The
        strictValidation argument exists to provide backwards
        compatibility with former workflows where certain clipboard
        hierarchy orders were strictly enforced, preventing setting of
        the clipboard contents unless the selection and hierarchy order
        met the validation criteria, such as the first element must have
        a depth of zero. When true, the validation is done and the
        clipboard will not be set unless the hierarchy restrictions are
        met. When false, pasting by name can work even if the
        hierarchy/selection order is different during the paste.

        Returns:
        -----
        None

        Parameters:
        -----
        clipboardItemArray: MAnimCurveClipboardItemArray
        	[in] -> the array of clipboard items to load on to the current clipboard 

        startTime: MTime
        	[in] -> the start time for the clipboard 

        endTime: MTime
        	[in] -> the end time for the clipboard 

        startUnitlessInput: float
        	[out] -> the start unitless input for the clipboard 

        endUnitlessInput: float
        	[out] -> the end unitless input for the clipboard 

        strictValidation: bool
        	[in] -> if true, do the validation check, if false, then don't do the check. 


        '''
        pass

    def clear(self): 
        '''
        clear(self)

        Synopsis
        -----
        This method empties the clipboard.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def isEmpty(self, ReturnStatus: MAnimCurveClipboard.MStatus): 
        '''
        isEmpty(self, ReturnStatus: MAnimCurveClipboard.MStatus) -> bool

        Synopsis
        -----
        Determines if the clipboard is empty.

        Returns: 
        ----- 
        true the current clipboard is empty  false the current clipboard
        is not empty  Status Code

        Parameters:
        -----
        ReturnStatus: MAnimCurveClipboard.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def clipboardItems(self, ReturnStatus: MAnimCurveClipboard.MStatus): 
        '''
        clipboardItems(self, ReturnStatus: MAnimCurveClipboard.MStatus) -> const MAnimCurveClipboardItemArray

        Synopsis
        -----
        Returns the contents of the clipboard.

        Returns: 
        ----- 
        The item array currently on this clipboard.

        Parameters:
        -----
        ReturnStatus: MAnimCurveClipboard.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def startTime(self, ReturnStatus: MAnimCurveClipboard.MStatus): 
        '''
        startTime(self, ReturnStatus: MAnimCurveClipboard.MStatus) -> MTime

        Synopsis
        -----
        Returns the start time of the clipboard.

        Returns: 
        ----- 
        The start time of the clipboard.

        Parameters:
        -----
        ReturnStatus: MAnimCurveClipboard.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def endTime(self, ReturnStatus: MAnimCurveClipboard.MStatus): 
        '''
        endTime(self, ReturnStatus: MAnimCurveClipboard.MStatus) -> MTime

        Synopsis
        -----
        Returns the end time of the clipboard.

        Returns: 
        ----- 
        The end time of the clipboard.

        Parameters:
        -----
        ReturnStatus: MAnimCurveClipboard.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def startUnitlessInput(self, ReturnStatus: MAnimCurveClipboard.MStatus): 
        '''
        startUnitlessInput(self, ReturnStatus: MAnimCurveClipboard.MStatus) -> float

        Synopsis
        -----
        Returns the start unitless input of the clipboard.

        Returns: 
        ----- 
        The start unitless input of the clipboard.

        Parameters:
        -----
        ReturnStatus: MAnimCurveClipboard.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def endUnitlessInput(self, ReturnStatus: MAnimCurveClipboard.MStatus): 
        '''
        endUnitlessInput(self, ReturnStatus: MAnimCurveClipboard.MStatus) -> float

        Synopsis
        -----
        Returns the end unitless input of the clipboard.

        Returns: 
        ----- 
        The end unitless input of the clipboard.

        Parameters:
        -----
        ReturnStatus: MAnimCurveClipboard.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

class MAnimCurveClipboardItem:
    '''Wrapper for a clipboard item.
This class provides a wrapper for a clipboard item. Common
convenience functions are available, and the implementation is
compatible with the internal Maya implementation so that it can
be passed efficiently between plugins and internal maya data
structures.
'''
    def __init__(self):
        pass


    def animCurve(self, ReturnStatus: MAnimCurveClipboardItem.MStatus): 
        '''
        animCurve(self, ReturnStatus: MAnimCurveClipboardItem.MStatus) -> const MObject

        Synopsis
        -----
        Returns the animCurve held by this clipboard item as an MObject.
        Note that the returned MObject is const because you must not
        modify the animCurve referenced by this MObject.

        Returns: 
        ----- 
        An MObject for the animCurve. On failure, the MObject will be
        NULL. Be aware that the clipboard may be holding onto NULL
        animCurves (which are placeholder objects).

        Parameters:
        -----
        ReturnStatus: MAnimCurveClipboardItem.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def getAddressingInfo(self, rowCount: int,
                        childCount: int,
                        attributeCount: int): 
        '''
        getAddressingInfo(self, rowCount: int,
                        childCount: int,
                        attributeCount: int)

        Synopsis
        -----
        Returns the addressing information for this clipboard item,.

        Returns:
        -----
        None

        Parameters:
        -----
        rowCount: int
        	[out] -> The clipboard item's row count 

        childCount: int
        	[out] -> The clipboard item's child count 

        attributeCount: int
        	[out] -> The clipboard item's attribute count


        '''
        pass

    def fullAttributeName(self, ReturnStatus: MAnimCurveClipboardItem.MStatus): 
        '''
        fullAttributeName(self, ReturnStatus: MAnimCurveClipboardItem.MStatus) -> const MString&

        Synopsis
        -----
        Returns the attribute's full name.

        Returns: 
        ----- 
        The attribute's full name

        Parameters:
        -----
        ReturnStatus: MAnimCurveClipboardItem.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def leafAttributeName(self, ReturnStatus: MAnimCurveClipboardItem.MStatus): 
        '''
        leafAttributeName(self, ReturnStatus: MAnimCurveClipboardItem.MStatus) -> const MString&

        Synopsis
        -----
        Returns the attribute's leaf name.

        Returns: 
        ----- 
        The attribute's leaf name.

        Parameters:
        -----
        ReturnStatus: MAnimCurveClipboardItem.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def nodeName(self, ReturnStatus: MAnimCurveClipboardItem.MStatus): 
        '''
        nodeName(self, ReturnStatus: MAnimCurveClipboardItem.MStatus) -> const MString&

        Synopsis
        -----
        Returns the node name.

        Returns: 
        ----- 
        The node name.

        Parameters:
        -----
        ReturnStatus: MAnimCurveClipboardItem.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def animCurveType(self, ReturnStatus: MAnimCurveClipboardItem.MStatus): 
        '''
        animCurveType(self, ReturnStatus: MAnimCurveClipboardItem.MStatus) -> MFnAnimCurve.MFnAnimCurve

        Synopsis
        -----
        Returns the animCurve type.

        Returns: 
        ----- 
        The animCurve type.

        Parameters:
        -----
        ReturnStatus: MAnimCurveClipboardItem.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def setAnimCurve(self, curve: MObject): 
        '''
        setAnimCurve(self, curve: MObject)

        Synopsis
        -----
        Sets the clipboard item's animCurve.

        Returns:
        -----
        None

        Parameters:
        -----
        curve: MObject
        	[in] -> The animCurve


        '''
        pass

    def setAddressingInfo(self, rowCount: int,
                        childCount: int,
                        attributeCount: int): 
        '''
        setAddressingInfo(self, rowCount: int,
                        childCount: int,
                        attributeCount: int)

        Synopsis
        -----
        Sets the clipboard item's addressing info.

        Returns:
        -----
        None

        Parameters:
        -----
        rowCount: int
        	[in] -> The clipboard item's row count 

        childCount: int
        	[in] -> The clipboard item's child count 

        attributeCount: int
        	[in] -> The clipboard item's attribute count


        '''
        pass

    def setNameInfo(self, nodeName: MString,
                        fullName: MString,
                        leafName: MString): 
        '''
        setNameInfo(self, nodeName: MString,
                        fullName: MString,
                        leafName: MString)

        Synopsis
        -----
        Sets the clipboard item's name info.

        Returns:
        -----
        None

        Parameters:
        -----
        nodeName: MString
        	[in] -> The clipboard item's node name 

        fullName: MString
        	[in] -> The clipboard item's full attribute name 

        leafName: MString
        	[in] -> The clipboard item's leaf attribute name


        '''
        pass

    def __eq__(self, rhs: MAnimCurveClipboardItem): 
        '''
        __eq__(self, rhs: MAnimCurveClipboardItem) -> bool

        Synopsis
        -----
        Compare the individual members for equality.

        Returns: 
        ----- 
        true the MAnimCurveClipboard items are equal  false the
        MAnimCurveClipboard items are not equal

        Parameters:
        -----
        rhs: MAnimCurveClipboardItem
        	[in] -> The 


        '''
        pass

    def className(self): 
        '''
        className(self) -> char*

        Synopsis
        -----
        Returns the name of this class.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MAnimCurveClipboardItemArray:
    '''Array of
MAnimCurveClipboardItem data type.
This class implements an array of MAnimCurveClipboardItems.
Common convenience functions are available, and the
implementation is compatible with the internal Maya
implementation so that it can be passed efficiently between
plugins and internal maya data structures.
'''
    def __init__(self):
        pass


    def __getitem__(self, index: int): 
        '''
        __getitem__(self, index: int) -> const MAnimCurveClipboardItem&

        Synopsis
        -----
        Index operator. Returns the value of the element at the given
        index. No range checking is done - valid indices are 0 to
        length()-1.

        Returns: 
        ----- 
        A reference to the indicated element

        Parameters:
        -----
        index: int
        	[in] -> the index of the desired element


        '''
        pass

    def set(self, element: MAnimCurveClipboardItem,
                        index: int): 
        '''
        set(self, element: MAnimCurveClipboardItem,
                        index: int)

        Synopsis
        -----
        Sets the value of the indicated element to the indicated
        MAnimCurveClipboardItem value.

        Returns:
        -----
        None

        Parameters:
        -----
        element: MAnimCurveClipboardItem
        	[in] -> the new value for the indicated element 

        index: int
        	[in] -> the index of the element that is to be set to the the new value


        '''
        pass

    def setLength(self, length: int): 
        '''
        setLength(self, length: int)

        Synopsis
        -----
        Set the length of the array. This will grow and shrink the array
        as desired. Elements that are grown have uninitialized values,
        while those which are shrunk will lose the data contained in the
        deleted elements (ie. it will release the memory).

        Returns:
        -----
        None

        Parameters:
        -----
        length: int
        	[in] -> the new size of the array 


        '''
        pass

    def length(self): 
        '''
        length(self) -> int

        Synopsis
        -----
        Returns the number of elements in the instance.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def remove(self, index: int): 
        '''
        remove(self, index: int)

        Synopsis
        -----
        Remove the array element at the given index. All array elements
        following the removed element are shifted toward the first
        element.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> index of the element to be removed


        '''
        pass

    def insert(self, element: MAnimCurveClipboardItem,
                        index: int): 
        '''
        insert(self, element: MAnimCurveClipboardItem,
                        index: int)

        Synopsis
        -----
        Inserts a new value into the array at the given index. The
        initial element at that index, and all following elements, are
        shifted towards the last. If the array cannot be expanded in size
        by 1 element, then the insert will fail and the existing array
        will remain unchanged.

        Returns:
        -----
        None

        Parameters:
        -----
        element: MAnimCurveClipboardItem
        	[in] -> the new value to insert into the array 

        index: int
        	[in] -> the index of the element to set to the the new value


        '''
        pass

    def append(self, element: MAnimCurveClipboardItem): 
        '''
        append(self, element: MAnimCurveClipboardItem)

        Synopsis
        -----
        Adds a new element to the end of the array. If the array cannot
        be expanded in size by 1 element, then the append will fail and
        the existing array will remain unchanged.

        Returns:
        -----
        None

        Parameters:
        -----
        element: MAnimCurveClipboardItem
        	[in] -> the value for the new last element


        '''
        pass

    def clear(self): 
        '''
        clear(self)

        Synopsis
        -----
        Clear the contents of the array. After this operation the length
        method will return 0. This does not change the amount of memory
        allocated to the array, only the number of valid elements in it.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setSizeIncrement(self, newIncrement: int): 
        '''
        setSizeIncrement(self, newIncrement: int)

        Synopsis
        -----
        Set the size by which the array will be expanded whenever
        expansion is necessary.

        Returns:
        -----
        None

        Parameters:
        -----
        newIncrement: int
        	[in] -> the new increment 


        '''
        pass

    def sizeIncrement(self): 
        '''
        sizeIncrement(self) -> int

        Synopsis
        -----
        Return the size by which the array will be expanded whenever
        expansion is necessary.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def isValid(self, failedIndex: int): 
        '''
        isValid(self, failedIndex: int) -> bool

        Synopsis
        -----
        Ensures that the MAnimCurveClipboard items in the array make
        sense.

        Returns: 
        ----- 
        true if the clipboard item array is valid, and false otherwise

        Parameters:
        -----
        failedIndex: int
        	[out] -> The failed index value


        '''
        pass

    def copy(self, source: MAnimCurveClipboardItemArray): 
        '''
        copy(self, source: MAnimCurveClipboardItemArray)

        Synopsis
        -----
        Copy the contents of the source array to this array.

        Returns:
        -----
        None

        Parameters:
        -----
        source: MAnimCurveClipboardItemArray
        	[in] -> array to copy from


        '''
        pass

    def className(self): 
        '''
        className(self) -> char*

        Synopsis
        -----
        Returns the name of this class.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MAnimMessage:
    '''Animation messages.
This class is used to register callbacks for animation messages.
To remove a callback use
MMessage::removeCallback. All callbacks that are registered by a plug-in must be removed
by that plug-in when it is unloaded. Failure to do so will result
in a fatal error.
'''
    def __init__(self):
        pass


    def addAnimCurveEditedCallback(self, func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MAnimMessage.MStatus): 
        '''
        addAnimCurveEditedCallback(self, func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MAnimMessage.MStatus) -> MAnimMessage.OPENMAYA_MAJOR_NAMESPACE_OPENMCallbackId

        Synopsis
        -----
        AnimCurve edited callback. This method registers a callback that
        is called whenever an AnimCurve is edited.

        Returns: 
        ----- 
        Identifier used for removing the callback.

        Parameters:
        -----
        func: MMessage.MMessage
        	[in] -> The callback function.

        clientData: void
        	[in] -> User defined data passed to the callback function. 

        ReturnStatus: MAnimMessage.MStatus
        	[out] -> Status code.


        '''
        pass

    def addAnimKeyframeEditedCallback(self, func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MAnimMessage.MStatus): 
        '''
        addAnimKeyframeEditedCallback(self, func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MAnimMessage.MStatus) -> MCallbackId

        Synopsis
        -----
        AnimCurve keyframe edited callback. This method registers a
        callback that is called whenever an a group of keys are
        modified.The callback is invoked once per atomic change to single
        or group of keyframes. For example, if a user selects a group 5
        of keys and moves them 5 units in the value axis, then a single
        callback event will be invoked with a MObject for each of the 5
        keyframes. The MObjects can then be used in the MFnKeyframeDelta
        function set. Refer to MFnKeyframeDelta function set
        documentation for more info.

        Returns: 
        ----- 
        Identifier used for removing the callback.

        Parameters:
        -----
        func: MMessage.MMessage
        	[in] -> the callback function

        clientData: void
        	[in] -> User defined data. 

        ReturnStatus: MAnimMessage.MStatus
        	[out] -> status code


        '''
        pass

    def addNodeAnimKeyframeEditedCallback(self, animNode: MObject,
                        func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MAnimMessage.MStatus): 
        '''
        addNodeAnimKeyframeEditedCallback(self, animNode: MObject,
                        func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MAnimMessage.MStatus) -> MCallbackId

        Synopsis
        -----
        AnimCurve keyframe edited callback. This method registers a
        callback that is called whenever an a group of keys are
        modified.The callback is invoked once per atomic change to single
        or group of keyframes on the specified animation curve node. For
        example, if a user selects a group 5 of keys and moves them 5
        units in the value axis, then a single callback event will be
        invoked with a MObject for each of the 5 keyframes. The MObjects
        can then be used in the MFnKeyframeDelta function set. Refer to
        MFnKeyframeDelta function set documentation for more info.

        Returns: 
        ----- 
        Identifier used for removing the callback.

        Parameters:
        -----
        animNode: MObject
        	[in] -> the param curve node you want to watch. 

        func: MMessage.MMessage
        	[in] -> the callback function

        clientData: void
        	[in] -> User defined data. 

        ReturnStatus: MAnimMessage.MStatus
        	[out] -> status code


        '''
        pass

    def addAnimKeyframeEditCheckCallback(self, func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MAnimMessage.MStatus): 
        '''
        addAnimKeyframeEditCheckCallback(self, func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MAnimMessage.MStatus) -> MCallbackId

        Synopsis
        -----
        AnimCurve keyframe edit check callback. This method registers a
        callback that is used by the setKeyframe command to allow a user
        to consider the set keyframe request and cancel it if needed.The
        callback method should return false to abort the keyframe
        setting.This example callback will reject any changes to plugs
        including 'translate' in their name.

        Returns: 
        ----- 
        Identifier used for removing the callback.

        Parameters:
        -----
        func: MMessage.MMessage
        	[in] -> the callback function 

        clientData: void
        	[in] -> User defined data. 

        ReturnStatus: MAnimMessage.MStatus
        	[out] -> status code


        '''
        pass

    def addPreBakeResultsCallback(self, func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MAnimMessage.MStatus): 
        '''
        addPreBakeResultsCallback(self, func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MAnimMessage.MStatus) -> MCallbackId

        Synopsis
        -----
        Pre Bake Simulation callback. This method registers a callback
        that is called from bakeResults command before the simulation.One
        example usage is handle the runup to the first frame in a dynamic
        system. If plugArray is set to zero length in the callback, the
        baking will be aborted.

        Returns: 
        ----- 
        Identifier used for removing the callback.

        Parameters:
        -----
        func: MMessage.MMessage
        	[in] -> the callback function 

        clientData: void
        	[in] -> User defined data. 

        ReturnStatus: MAnimMessage.MStatus
        	[out] -> status code


        '''
        pass

    def addPostBakeResultsCallback(self, func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MAnimMessage.MStatus): 
        '''
        addPostBakeResultsCallback(self, func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MAnimMessage.MStatus) -> MCallbackId

        Synopsis
        -----
        Post Bake Simulation callback. This method registers a callback
        that is called from bakeResults command after the simulation.If
        the plugArray is replaced, then the anim curves created from
        baking will be connected to the new plugs.

        Returns: 
        ----- 
        Identifier used for removing the callback.

        Parameters:
        -----
        func: MMessage.MMessage
        	[in] -> the callback function 

        clientData: void
        	[in] -> User defined data. 

        ReturnStatus: MAnimMessage.MStatus
        	[out] -> status code


        '''
        pass

    def addDisableImplicitControlCallback(self, func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MAnimMessage.MStatus): 
        '''
        addDisableImplicitControlCallback(self, func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MAnimMessage.MStatus) -> MCallbackId

        Synopsis
        -----
        Disable Implicit Control callback. This method registers a
        callback that is called from bakeResults command after baking
        operation is completed, if disableImplicitControl is enabled.One
        example usage of this callback is to create the anim curve that
        is used to drive Maya rigidbody's bakeSimulationIndex, which
        defines if the rigid body should take its input from anim curve
        or rigid body simulation.

        Returns: 
        ----- 
        Identifier used for removing the callback.

        Parameters:
        -----
        func: MMessage.MMessage
        	[in] -> the callback function 

        clientData: void
        	[in] -> User defined data. 

        ReturnStatus: MAnimMessage.MStatus
        	[out] -> status code


        '''
        pass

    def flushAnimKeyframeEditedCallbacks(self): 
        '''
        flushAnimKeyframeEditedCallbacks(self)

        Synopsis
        -----
        AnimCurve keyframe edited callback flush. Animation keyframe
        edited callbacks are queued to only be issued on an idle
        event.There may be times when it is desired to issue the callback
        at a specific time. This method provides this functionality. It
        will flush all animation keyframe edited callbacks and force them
        to issue their callbacks with the data contained within.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> char*

        Synopsis
        -----
        Returns the name of this class.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MAnimUtil:
    '''Static class providing common animation helper methods.
MAnimUtil is a static class which provides methods which determine if an
object is being animated, which attributes are animated for a
given object and which animation curves are used to animate a
given attribute.
Note: for purposes of this helper class, "animation" refers to
attributes animated by animCurves (i.e. by setting keys). It does
not include any animation through expressions or dynamics or
timer node connections.
Some helper methods may examine different types of objects.
Depending upon how the object is represented, the same object may
be examined differently.
If the object is specified as an
, then all of its attributes are examined. If the
MObject is a hierarchical object (such as a dag node) and you specify
that the objects parents should be examined, then all the parents
of an instanced object will be examined.
If the object is specified as an
, then all of its attributes are examined. If you specify that
the objects parents should be examined, then only the specified
path of the instanced object will be examined.
If the object is specifed as an
 and no attribute has been set, then the method will behave as if
it was called with an
MObject. Otherwise only the specified attribute will be examined. For
example, a compound attribute will not have its child attributes
examined (i.e. if you specify node.translate, node.translateX
will not be examined).
If the object is specified through an
, it can also have multiple representations. If the object was
added to the
MSelectionList as an
MObject, then it will be examined as an
MObject. If the object was added to the
MSelectionList as an
MDagPath, then it will be examined as an
MDagPath. If the object was added to the
MSelectionList as either a component or an
MPlug, it will be examined as an
MPlug with additional expansion of compound attributes into their
child attributes (for example, if specify node.translate is
specified, node.translateX will be examined. More importantly, if
you specify poly.f[4] then xValue, yValue and zValue will be
examined for each vertex).
Below is a summary of how the same object will be examined by
MAnimUtil::isAnimated depending upon how it has been represented. If we have the
following hierarchical layout:
 (translateX is animated)
The
MAnimUtil::isAnimated will respond as follows:
 => false
 => true
 => false
 => false
 => false
 => true
 => false
 => true
 => false
 => true
The following list assumes that
MAnimUtil is called with an
MSelectionList named list, and shows the response depending upon how the object
has been added to list:
 => false
 => true
 => false
 => false
 => false
 => true
 => true
 => true
 => true
 => true
'''
    def __init__(self):
        pass


    @overload
    def isAnimated(self, node: MObject,
                        checkParent: bool,
                        ReturnStatus: MAnimUtil.MStatus): 
        '''
        isAnimated(self, node: MObject,
                        checkParent: bool,
                        ReturnStatus: MAnimUtil.MStatus) -> MAnimUtil.OPENMAYA_MAJOR_NAMESPACE_OPENbool

        Synopsis
        -----
        Determine whether or not an MObject is animated. If the MObject
        is a hierarchical object (such as a dag node) then you may also
        specify whether or not the MObject's parents are examined. In the
        case of instanced MObjects, all of the MObject's parents are
        examined.

        Returns: 
        ----- 
        true The MObject is animated.  false The MObject is not animated.

        Parameters:
        -----
        node: MObject
        	[in] -> the 

        checkParent: bool
        	[in] -> whether or not to examine if the node's parent is animated 

        ReturnStatus: MAnimUtil.MStatus
        	[out] -> the return status


        '''
        pass

    @overload
    def isAnimated(self, path: MDagPath,
                        checkParent: bool,
                        ReturnStatus: MAnimUtil.MStatus): 
        '''
        isAnimated(self, path: MDagPath,
                        checkParent: bool,
                        ReturnStatus: MAnimUtil.MStatus) -> bool

        Synopsis
        -----
        Determine whether or not an MDagPath is animated. You may also
        specify whether or not the MDagPath's parent is examined. In the
        case of instanced MDagPath only the specified path is examined.

        Returns: 
        ----- 
        true The MDagPath is animated.  false The MDagPath is not
        animated.

        Parameters:
        -----
        path: MDagPath
        	[in] -> the 

        checkParent: bool
        	[in] -> whether or not to examine if the path's parent is animated 

        ReturnStatus: MAnimUtil.MStatus
        	[out] -> the return status


        '''
        pass

    @overload
    def isAnimated(self, plug: MPlug,
                        checkParent: bool,
                        ReturnStatus: MAnimUtil.MStatus): 
        '''
        isAnimated(self, plug: MPlug,
                        checkParent: bool,
                        ReturnStatus: MAnimUtil.MStatus) -> bool

        Synopsis
        -----
        Determine whether or not an MPlug is animated. If the MPlug does
        not have an attribute specified, then the entire node is
        examined. You may also specify whether or not the node's parents
        are examined. In the case of instanced nodes, all of the node's
        parents are examined. If an attribute has been specified, the
        node's parents are not examined.

        Returns: 
        ----- 
        true The MPlug is animated.  false The MPlug is not animated.

        Parameters:
        -----
        plug: MPlug
        	[in] -> the 

        checkParent: bool
        	[in] -> whether or not to examine if the node's parent is animated 

        ReturnStatus: MAnimUtil.MStatus
        	[out] -> the return status


        '''
        pass

    @overload
    def isAnimated(self, selectionList: MSelectionList,
                        checkParent: bool,
                        ReturnStatus: MAnimUtil.MStatus): 
        '''
        isAnimated(self, selectionList: MSelectionList,
                        checkParent: bool,
                        ReturnStatus: MAnimUtil.MStatus) -> bool

        Synopsis
        -----
        Determine whether or not any member of an MSelectionList is
        animated. This is intended to work with an MSelectionList with a
        single entry since that provides the most useful information.In
        addition to normal objects, components such as mesh vertices or
        faces can be easily described on an MSelectionList, making this a
        good way to determine if parts of a shape are animated or not.If
        a member represents an MDagPath you may also specify whether or
        not the MDagPath's parent is examined. In the case of instanced
        MDagPath only the specified path is examined.If a member
        represents a hierarchical MObject (such as a dag node) then you
        may also specify whether or not the MObject's parents are
        examined. In the case of instanced MObjects, all of the MObject's
        parents are examined.

        Returns: 
        ----- 
        true The MSelectionList has at least one animated member.  false
        No member of the MSelectionList is animated.

        Parameters:
        -----
        selectionList: MSelectionList
        	[in] -> the 

        checkParent: bool
        	[in] -> whether or not to examine if the node's parent is animated 

        ReturnStatus: MAnimUtil.MStatus
        	[out] -> the return status


        '''
        pass

    @overload
    def findAnimatedPlugs(self, node: MObject,
                        animatedPlugs: MPlugArray,
                        checkParent: bool,
                        ReturnStatus: MAnimUtil.MStatus): 
        '''
        findAnimatedPlugs(self, node: MObject,
                        animatedPlugs: MPlugArray,
                        checkParent: bool,
                        ReturnStatus: MAnimUtil.MStatus) -> bool

        Synopsis
        -----
        Find the list of attributes (MPlugs) on an MObject that is
        animated. If the MObject is a hierarchical object (such as a dag
        node) then you may also specify whether or not the MObject's
        parents are examined. In the case of instanced MObjects, all of
        the MObject's parents are examined.

        Returns: 
        ----- 
        true The MObject is animated.  false The MObject is not animated.

        Parameters:
        -----
        node: MObject
        	[in] -> the 

        animatedPlugs: MPlugArray
        	[in] -> the list of attributes which are animated the array is not cleared 

        checkParent: bool
        	[in] -> whether or not to examine if the node's parent is animated 

        ReturnStatus: MAnimUtil.MStatus
        	[out] -> the return status


        '''
        pass

    @overload
    def findAnimatedPlugs(self, path: MDagPath,
                        animatedPlugs: MPlugArray,
                        checkParent: bool,
                        ReturnStatus: MAnimUtil.MStatus): 
        '''
        findAnimatedPlugs(self, path: MDagPath,
                        animatedPlugs: MPlugArray,
                        checkParent: bool,
                        ReturnStatus: MAnimUtil.MStatus) -> bool

        Synopsis
        -----
        Find the list of attributes (MPlugs) on an MDagPath object that
        is animated. You may also specify whether or not the MDagPath's
        parent is examined. In the case of instanced MDagPath only the
        specified path is examined.

        Returns: 
        ----- 
        true The MDagPath is animated.  false The MDagPath is not
        animated.

        Parameters:
        -----
        path: MDagPath
        	[in] -> the 

        animatedPlugs: MPlugArray
        	[in] -> the list of attributes which are animated the array is not cleared 

        checkParent: bool
        	[in] -> whether or not to examine if the path's parent is animated 

        ReturnStatus: MAnimUtil.MStatus
        	[out] -> the return status


        '''
        pass

    @overload
    def findAnimatedPlugs(self, selectionList: MSelectionList,
                        animatedPlugs: MPlugArray,
                        checkParent: bool,
                        ReturnStatus: MAnimUtil.MStatus): 
        '''
        findAnimatedPlugs(self, selectionList: MSelectionList,
                        animatedPlugs: MPlugArray,
                        checkParent: bool,
                        ReturnStatus: MAnimUtil.MStatus) -> bool

        Synopsis
        -----
        Find the list of attributes (MPlugs) on any member of an
        MSelectionList that is animated. In addition to normal objects,
        components such as mesh vertices or faces can be easily described
        on an MSelectionList, making this a good way to determine if
        parts of a shape are animated or not.If a member represents an
        MDagPath you may also specify whether or not the MDagPath's
        parent is examined. In the case of instanced MDagPath only the
        specified path is examined.If a member represents a hierarchical
        MObject (such as a dag node) then you may also specify whether or
        not the MObject's parents are examined. In the case of instanced
        MObjects, all of the MObject's parents are examined.

        Returns: 
        ----- 
        true The MSelectionList has at least one animated member.  false
        No member of the MSelectionList is animated.

        Parameters:
        -----
        selectionList: MSelectionList
        	[in] -> the 

        animatedPlugs: MPlugArray
        	[in] -> the list of attributes which are animated the array is not cleared 

        checkParent: bool
        	[in] -> whether or not to examine if the node's parent is animated 

        ReturnStatus: MAnimUtil.MStatus
        	[out] -> the return status


        '''
        pass

    def findAnimation(self, plug: MPlug,
                        animation: MObjectArray,
                        ReturnStatus: MAnimUtil.MStatus): 
        '''
        findAnimation(self, plug: MPlug,
                        animation: MObjectArray,
                        ReturnStatus: MAnimUtil.MStatus) -> bool

        Synopsis
        -----
        Find the animCurve(s) that are animating a given attribute
        (MPlug). In most cases an attribute is animated by a single
        animCurve and so just that animCurve will be returned. It is
        possible to setup a series of connections where an attribute is
        animated by more than one animCurve, although Maya does not
        currently offer a UI to do so. Compound attributes are not
        expanded to include any child attributes.

        Returns: 
        ----- 
        true The MPlug is animated.  false The MPlug is not animated.

        Parameters:
        -----
        plug: MPlug
        	[in] -> the plug to examine for animCurve(s) 

        animation: MObjectArray
        	[in] -> the list of animCurves which animate `plug'. The array is not cleared 

        ReturnStatus: MAnimUtil.MStatus
        	[out] -> the return status


        '''
        pass

    def findSetDrivenKeyAnimation(self, plug: MPlug,
                        animationNodes: MObjectArray,
                        drivers: MPlugArray,
                        ReturnStatus: MAnimUtil.MStatus): 
        '''
        findSetDrivenKeyAnimation(self, plug: MPlug,
                        animationNodes: MObjectArray,
                        drivers: MPlugArray,
                        ReturnStatus: MAnimUtil.MStatus) -> bool

        Synopsis
        -----
        Find any driven keyframe animCurves, the blendWeighted node and
        the driver attribute(s) that are animating a given attribute
        (MPlug). Or return false if no driven keyframe exists on the
        attribute.A driven keyframe is similar to a regular keyframe.
        However, while a standard keyframe always has an x-axis of time
        in the graph editor, for a drivenkeyframe the user may choose any
        attribute as the x-axis of the graph editor. This attribute is
        called the driver.In the case where there is only one driver, the
        animation curve will be connected directly to the driven
        attribute. When there are multiple drivers, the driven keyframe
        animCurves feed into a blendWeighted node which drives the
        attribute.Compound attributes are not expanded to include any
        child attributes.

        Returns: 
        ----- 
        true The MPlug is animated by a setDrivenKey.  false The MPlug is
        not animated by a setDrivenKey.

        Parameters:
        -----
        plug: MPlug
        	[in] -> the plug to examine for animCurve(s) 

        animationNodes: MObjectArray
        	[out] -> the list of sdk animation curves and a blendWeighted node that drive the `plug'. The array is not cleared 

        drivers: MPlugArray
        	[out] -> the list of driver attribute(s). The array is not cleared. 

        ReturnStatus: MAnimUtil.MStatus
        	[out] -> the return status


        '''
        pass

    def findConstraint(self, plug: MPlug,
                        constraint: MObject,
                        targets: MObjectArray,
                        ReturnStatus: MAnimUtil.MStatus): 
        '''
        findConstraint(self, plug: MPlug,
                        constraint: MObject,
                        targets: MObjectArray,
                        ReturnStatus: MAnimUtil.MStatus) -> bool

        Synopsis
        -----
        Find any constraint that is directly driving the specified
        attribute. If a constraint is found, this method will also find
        the constraint targets. Return false if no constraint exists on
        the attribute.Compound attributes are not expanded to include any
        child attributes.

        Returns: 
        ----- 
        true The MPlug is controlled by a constraint  false The MPlug is
        not animated by a constraint

        Parameters:
        -----
        plug: MPlug
        	[in] -> the plug to examine for a constraint 

        constraint: MObject
        	[out] -> the constraint 

        targets: MObjectArray
        	[out] -> the list of constraint targets The array is not cleared. 

        ReturnStatus: MAnimUtil.MStatus
        	[out] -> the return status


        '''
        pass

    def findAnimatablePlugs(self, selectionList: MSelectionList,
                        animatablePlugs: MPlugArray): 
        '''
        findAnimatablePlugs(self, selectionList: MSelectionList,
                        animatablePlugs: MPlugArray) -> bool

        Synopsis
        -----
        Find the list of attributes (MPlugs) on any member of an
        MSelectionList that is animatable. In addition to normal objects,
        components such as mesh vertices or faces can be easily described
        on an MSelectionList, making this a good way to determine if
        parts of a shape are animatable or not.

        Returns: 
        ----- 
        true The MSelectionList has at least one animatable member. false
        No member of the MSelectionList is animatable.

        Parameters:
        -----
        selectionList: MSelectionList
        	[in] -> the 

        animatablePlugs: MPlugArray
        	[in] -> the list of attributes which are animatable the array is not cleared


        '''
        pass

    def className(self): 
        '''
        className(self) -> char*

        Synopsis
        -----
        Returns the name of this class.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MFnAnimCurve:
    '''Anim Curve Function Set.
Create, query and edit Anim Curve Nodes and the keys internal to
those Nodes.
Create an Anim Curve Node and connect its output to any
animatable attribute on another Node.
Evaluate an Anim Curve at a particular time.
Determine the number of keys held by an Anim Curve.
Determine the time and value of individual keys, as well as the
(angle,weight) or (x,y) values and type of key tangents. The in-
tangent refers to the tangent entering the key. The out-tangent
refers to the tangent leaving the key.
Find the index of the key at, or closest to a particular time.
Set the time and value of individual keys, as well as the type of
the tangent to the curve entering (in-tangent) and leaving (out-
tangent) the key, specify the tangent as either (angle,weight) or
(x,y).
Add and remove keys from an Anim Curve. Anim Curves are
implemented as Dependency Graph (DG) Nodes. Each Node can have
indexed keys.
There are eight different types of Anim Curve nodes:
Specifying the correct AnimCurveType during creation will avoid
implicit unit conversion nodes.
Use the Anim Curve Function Set to create Anim Curve Nodes and
connect them to animatable attributes on DG Nodes, as well as to
query and edit an Anim Curve Node and its keys.
On creation, an Anim Curve Function Set may be attached to a
given Anim Curve or it may be unattached. The Function Set may be
attached to a different Anim Curve Node using the
setObject() methods inherited from the Base Function Set (
MFnBase) or with the
create() methods.
Use the
create() methods of an Anim Curve Function Set to create a new Anim Curve
Node, attach the Function Set to the new Node and connect the
output of the Node to a specific animatable Attribute or Plug of
another Node. Additionally, the output of an Anim Curve Node may
be attached to an Attribute or Plug of another DG Node using the
DG Modifier method
MDGModifier::connect().
Use the
evaluate() methods to determine the value of an Anim Curve at a particular
time or a given unitless input.
Use the
addKey() and
remove() methods to add and remove keys to and from an Anim Curve.
The query and edit methods of the Anim Curve Function Set act on
keys at a specific 0-based index. [Note that the
numKeys() method returns a 1-based value]. Keys can be accessed either
randomly (via a 0-based index) or serially (using the
find() and
findClosest() methods).
Use the
find() or
findClosest() methods to determine the index of a key at or closest to a
specific time respectively.
Use the specific query methods to determine the time, value and
tangent information for a key at a given index.
Use the specific edit methods to set the time, value and tangent
information for a key at a given index.
There are methods for setting the x,y values for the in- and out-
tangents, as well as setting their angles and weights.
Setting the time of a key will fail if the new time would require
a re-ordering of the keys. Use the
remove() and
addKey() methods to re-order the keys. Or use the keyframe command from
mel.
The Maya developer's kit ships with example code (animDemo) which
demonstrates how to evaluate a Maya animation curve independent
from Maya. The animation parameter curves in Maya are defined by
a restricted set of cubic two-dimensional Bezier curves. It is
defined by four points. P1 = (x1, y1) is the (key,value) pair for
the first key. P2 = (x2, y2) is a point which defines the
outgoing tangent direction at P1. P4 = (x4, y4) defines the
second key and P3 = (x3, y3) is a point which defines the
incoming tangent direction at P4. There are some basic
restrictions for the x coordinates of these points: x1 <= x2 <=
x3 <= x4.
The 2-dimensional Bezier curve is defined as
F(u) yields a vector of two cubic polynomials [ Fx(u) Fy(u) ]
which define an (x, y) position on the parameter curve for some u
in the range [0,1].
For an animation parameter curve, we are given the x position and
want to know its corresponding y position. To do this we use x =
Fx(u) and solve for u. Fx(u) is cubic and the restrictions on
valid values for x2 and x3 guarantee there will be only one real
root value for u. Once we know u, we can plug it into Fy(u) to
get the y value.
One important note is how the outgoing and incoming tangents
directions for a key are saved internally and in the Maya Ascii
file format. Instead of being specified as points, the tangent
directions are specified as vectors. The outgoing tangent
direction at P1 is specified and saved as the vector 3*(P2 - P1)
and the incoming tangent direction is specified and saved as the
vector 3*(P4 - P3).
An animation curve is basically a restricted form of a bezier
curve for which the keys serve as the control points and have
tangent information embedded within them. There are two different
methods for converting tangent information into the control
points of the bezier hull and we have taken to calling the two
methods weighted and non-weighted tangents.
The animation curve is evaluated in a piecewise manner, which
means that each segment between two keys is evaluated on its own,
without regards to any other segment. The only time keys outside
of a segment are considered is when tangent values are calculated
for the spline, clamped, plateau or auto tangent types.
When evaluating an animation curve, a two stage process is used:
Animation curves may have either weighted or non-weighted
tangents. With non-weighted tangents, tangents are implemented as
vectors and P2 and P3 are internally adjusted to account for the
time difference between P1 and P4.
When evaluating a time within a segment, the following
algortithms are used:
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kAnimCurve.Reimplemented from MFnDependencyNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> MFnAnimCurve.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnAnimCurve".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def create(self, node: MObject,
                        attribute: MObject,
                        modifier: MDGModifier,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        create(self, node: MObject,
                        attribute: MObject,
                        modifier: MDGModifier,
                        ReturnStatus: MFnAnimCurve.MStatus) -> MObject

        Synopsis
        -----
        Creates a new Anim Curve Node, attaches the Function Set to the
        new Node (detaching from the current Node) and connects the
        output of the new Anim Curve Node to an animatable Attribute on
        another DG Node. This method will fail if the target Attribute is
        not animatable, or if a connection to the target Attribute
        already exists.Once the new Anim Curve Node has been created, the
        create() method finds the Plug associated with the target
        Attribute, makes sure the Attribute is animatable and then makes
        the connection.The creation and connection of DG Nodes are DG
        operations. Operations on the DG are performed by DG Modifiers
        (MDGModifier). A DG Modifier provides methods for editing the DG,
        however, the operations are not performed immediately. DG
        operations must be undoable, therefore, the DG Modifier maintains
        a queue of pending DG operations which are performed when the
        MDGModifer::doIt() method is invoked. Subsequently, the queue of
        DG operations becomes the undo queue. When the
        MDGModifier::undoIt() method is invoked all of the operations on
        the queue are undone. DG operations on the queue can be done and
        undone as often as required as long as the Modifier exists and no
        other changes to the DG make the operations invalid. Once the
        Modifier holding the queue is destroyed, the queue is lost.If a
        DG Modifier is passed as a parameter to this create() method,
        then that Modifier will be invoked to perform the creation and
        connection operations. At the completion of the create() method,
        the Modifier holds the necessary information to undo the
        operations, therefore, the caller of the create() method can undo
        the creation and connection if necessary.If no Modifier is passed
        in, the create() method instantiates its own Modifier, uses it to
        perform the DG operations and then destroys the Modifier. The
        creation and connection, in this case, are not undoable by the
        caller.

        Returns: 
        ----- 
        The new Anim Curve Node

        Parameters:
        -----
        node: MObject
        	[in] -> DG Node to which the output of the new Anim Curve Node is to be connected 

        attribute: MObject
        	[in] -> Attribute on the given node to which the output of the new Anim Curve Node is to be connected 

        modifier: MDGModifier
        	[in] -> Modifier to be used so undo capability is retained by caller 

        ReturnStatus: MFnAnimCurve.MStatus
        	[in] -> Status Code


        '''
        pass

    @overload
    def create(self, node: MObject,
                        attribute: MObject,
                        animCurveType: MFnAnimCurve.AnimCurveType,
                        modifier: MDGModifier,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        create(self, node: MObject,
                        attribute: MObject,
                        animCurveType: MFnAnimCurve.AnimCurveType,
                        modifier: MDGModifier,
                        ReturnStatus: MFnAnimCurve.MStatus) -> MObject

        Synopsis
        -----
        Creates a new Anim Curve Node, attaches the Function Set to the
        new Node (detaching from the current Node) and connects the
        output of the new Anim Curve Node to an animatable Attribute on
        another DG Node. This method will fail if the target Attribute is
        not animatable, or if a connection to the target Attribute
        already exists.Once the new Anim Curve Node has been created, the
        create() method finds the Plug associated with the target
        Attribute, makes sure the Attribute is animatable and then makes
        the connection.The creation and connection of DG Nodes are DG
        operations. Operations on the DG are performed by DG Modifiers
        (MDGModifier). A DG Modifier provides methods for editing the DG,
        however, the operations are not performed immediately. DG
        operations must be undoable, therefore, the DG Modifier maintains
        a queue of pending DG operations which are performed when the
        MDGModifer::doIt() method is invoked. Subsequently, the queue of
        DG operations becomes the undo queue. When the
        MDGModifier::undoIt() method is invoked all of the operations on
        the queue are undone. DG operations on the queue can be done and
        undone as often as required as long as the Modifier exists and no
        other changes to the DG make the operations invalid. Once the
        Modifier holding the queue is destroyed, the queue is lost.If a
        DG Modifier is passed as a parameter to this create() method,
        then that Modifier will be invoked to perform the creation and
        connection operations. At the completion of the create() method,
        the Modifier holds the necessary information to undo the
        operations, therefore, the caller of the create() method can undo
        the creation and connection if necessary.If no Modifier is passed
        in, the create() method instantiates its own Modifier, uses it to
        perform the DG operations and then destroys the Modifier. The
        creation and connection, in this case, are not undoable by the
        caller.

        Returns: 
        ----- 
        The new Anim Curve Node

        Parameters:
        -----
        node: MObject
        	[in] -> DG Node to which the output of the new Anim Curve Node is to be connected 

        attribute: MObject
        	[in] -> Attribute on the given node to which the output of the new Anim Curve Node is to be connected 

        animCurveType: MFnAnimCurve.AnimCurveType
        	[in] -> The animCurve Type to be created 

        modifier: MDGModifier
        	[in] -> Modifier to be used so undo capability is retained by caller 

        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code


        '''
        pass

    @overload
    def create(self, plug: MPlug,
                        modifier: MDGModifier,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        create(self, plug: MPlug,
                        modifier: MDGModifier,
                        ReturnStatus: MFnAnimCurve.MStatus) -> MObject

        Synopsis
        -----
        Creates a new Anim Curve Node, attaches the Function Set to the
        new Node (detaching from the current Node) and connects the
        output of the new Anim Curve Node to the Plug on an animatable
        Attribute on another DG Node. This method will fail if the target
        Attribute is not animatable, or if a connection to the target
        Attribute already exists.If a DG Modifier is passed as a
        parameter to this create() method, then that Modifier will be
        invoked to perform the creation and connection operations. At the
        completion of the create() method, the Modifier holds the
        necessary information to undo the operations, therefore, the
        caller of the create() method can undo the creation and
        connection if necessary.If no Modifier is passed in, the create()
        method instantiates its own Modifier, uses it to perform the DG
        operations and then destroys the Modifier. The creation and
        connection, in this case, are not undoable by the caller.

        Returns: 
        ----- 
        The new Anim Curve Node

        Parameters:
        -----
        plug: MPlug
        	[in] -> Plug to which the output of the new Anim Curve Node is to be connected 

        modifier: MDGModifier
        	[in] -> Modifier to be used so undo capability is retained by caller 

        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code


        '''
        pass

    @overload
    def create(self, plug: MPlug,
                        animCurveType: MFnAnimCurve.AnimCurveType,
                        modifier: MDGModifier,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        create(self, plug: MPlug,
                        animCurveType: MFnAnimCurve.AnimCurveType,
                        modifier: MDGModifier,
                        ReturnStatus: MFnAnimCurve.MStatus) -> MObject

        Synopsis
        -----
        Creates a new Anim Curve Node, attaches the Function Set to the
        new Node (detaching from the current Node) and connects the
        output of the new Anim Curve Node to the Plug on an animatable
        Attribute on another DG Node. This method will fail if the target
        Attribute is not animatable, or if a connection to the target
        Attribute already exists.If a DG Modifier is passed as a
        parameter to this create() method, then that Modifier will be
        invoked to perform the creation and connection operations. At the
        completion of the create() method, the Modifier holds the
        necessary information to undo the operations, therefore, the
        caller of the create() method can undo the creation and
        connection if necessary.If no Modifier is passed in, the create()
        method instantiates its own Modifier, uses it to perform the DG
        operations and then destroys the Modifier. The creation and
        connection, in this case, are not undoable by the caller.

        Returns: 
        ----- 
        The new Anim Curve Node

        Parameters:
        -----
        plug: MPlug
        	[in] -> Plug to which the output of the new Anim Curve Node is to be connected 

        animCurveType: MFnAnimCurve.AnimCurveType
        	[in] -> The animCurve type to be created 

        modifier: MDGModifier
        	[in] -> Modifier to be used so undo capability is retained by caller 

        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code


        '''
        pass

    @overload
    def create(self, animCurveType: MFnAnimCurve.AnimCurveType,
                        modifier: MDGModifier,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        create(self, animCurveType: MFnAnimCurve.AnimCurveType,
                        modifier: MDGModifier,
                        ReturnStatus: MFnAnimCurve.MStatus) -> MObject

        Synopsis
        -----
        Creates a new Anim Curve Node, attaches the Function Set to the
        new Node (detaching from the current Node) but does not attempt
        to connect the new Anim Curve Node. If a DG Modifier is passed as
        a parameter to this create() method, then that Modifier will be
        invoked to perform the creation and connection operations. At the
        completion of the create() method, the Modifier holds the
        necessary information to undo the operations, therefore, the
        caller of the create() method can undo the creation and
        connection if necessary.If no Modifier is passed in, the create()
        method instantiates its own Modifier, uses it to perform the DG
        operations and then destroys the Modifier. The creation and
        connection, in this case, are not undoable by the caller.

        Returns: 
        ----- 
        The new Anim Curve Node

        Parameters:
        -----
        animCurveType: MFnAnimCurve.AnimCurveType
        	[in] -> The type of Anim Curve to be created 

        modifier: MDGModifier
        	[in] -> Modifier to be used so undo capability is retained by caller 

        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code


        '''
        pass

    def animCurveType(self, ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        animCurveType(self, ReturnStatus: MFnAnimCurve.MStatus) -> MFnAnimCurve.MFnAnimCurve

        Synopsis
        -----
        Returns the animCurve type.

        Returns: 
        ----- 
        The animCurve type.

        Parameters:
        -----
        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code


        '''
        pass

    def timedAnimCurveTypeForPlug(self, plug: MPlug,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        timedAnimCurveTypeForPlug(self, plug: MPlug,
                        ReturnStatus: MFnAnimCurve.MStatus) -> MFnAnimCurve.MFnAnimCurve

        Synopsis
        -----
        Returns the timed animCurve type appropriate for the specified
        plug.

        Returns: 
        ----- 
        The animCurve type.

        Parameters:
        -----
        plug: MPlug
        	[in] -> plug 

        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code


        '''
        pass

    def unitlessAnimCurveTypeForPlug(self, plug: MPlug,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        unitlessAnimCurveTypeForPlug(self, plug: MPlug,
                        ReturnStatus: MFnAnimCurve.MStatus) -> MFnAnimCurve.MFnAnimCurve

        Synopsis
        -----
        Returns the unitless animCurve type appropriate for the specified
        plug.

        Returns: 
        ----- 
        The animCurve type.

        Parameters:
        -----
        plug: MPlug
        	[in] -> plug 

        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code


        '''
        pass

    @overload
    def evaluate(self, atTime: MTime,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        evaluate(self, atTime: MTime,
                        ReturnStatus: MFnAnimCurve.MStatus) -> double

        Synopsis
        -----
        Determines the interpolated output value of Anim Curves of type
        kAnimCurveTA, kAnimCurveTL and kAnimCurveTU at the specified
        time.

        Returns: 
        ----- 
        Interpolated value of Anim Curve at specified time

        Parameters:
        -----
        atTime: MTime
        	[in] -> Time at which the Anim Curve is to be evaluated 

        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code .


        '''
        pass

    @overload
    def evaluate(self, atTime: MTime,
                        value: double): 
        '''
        evaluate(self, atTime: MTime,
                        value: double)

        Synopsis
        -----
        Determines the interpolated output value of Anim Curves of type
        kAnimCurveTA, kAnimCurveTL and kAnimCurveTU at the specified
        time.

        Returns:
        -----
        None

        Parameters:
        -----
        atTime: MTime
        	[in] -> Time at which the Anim Curve is to be evaluated 

        value: double
        	[out] -> Interpolated value of Anim Curve at specified time


        '''
        pass

    @overload
    def evaluate(self, atTime: MTime,
                        timeValue: MTime): 
        '''
        evaluate(self, atTime: MTime,
                        timeValue: MTime)

        Synopsis
        -----
        Determines the interpolated output value of Anim Curves of type
        kAnimCurveTT at the specified time.

        Returns:
        -----
        None

        Parameters:
        -----
        atTime: MTime
        	[in] -> Time at which the Anim Curve is to be evaluated 

        timeValue: MTime
        	[out] -> Interpolated output time of Anim Curve at specified time


        '''
        pass

    @overload
    def evaluate(self, atUnitlessInput: double,
                        value: double): 
        '''
        evaluate(self, atUnitlessInput: double,
                        value: double)

        Synopsis
        -----
        Determines the interpolated output value of Anim Curves of type
        kAnimCurveUA, kAnimCurveUL and kAnimCurveUU at the specified
        unitless input.

        Returns:
        -----
        None

        Parameters:
        -----
        atUnitlessInput: double
        	[out] -> Input value at which the Anim Curve is to be evaluated 

        value: double
        	[out] -> Interpolated output value of Anim Curve at specified input value


        '''
        pass

    @overload
    def evaluate(self, atUnitlessInput: double,
                        timeValue: MTime): 
        '''
        evaluate(self, atUnitlessInput: double,
                        timeValue: MTime)

        Synopsis
        -----
        Determines the interpolated output value of Anim Curves of type
        kAnimCurveUT at the specified unitless input.

        Returns:
        -----
        None

        Parameters:
        -----
        atUnitlessInput: double
        	[out] -> Input value at which the Anim Curve is to be evaluated 

        timeValue: MTime
        	[out] -> Interpolated output time of Anim Curve at specified time


        '''
        pass

    def isStatic(self, ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        isStatic(self, ReturnStatus: MFnAnimCurve.MStatus) -> bool

        Synopsis
        -----
        Determines whether or not the animCurve is static. The animCurve
        is considered to be static if it would return the same value
        regardless of the evaluation time. This basically means that the
        values of all the keys are the same and the y component of all
        the tangents is 0.For efficiency reasons, the isStatic flag is
        conservative. If the flag is true, the curve is guaranteed to be
        static. Since Maya assumes a recently edited curve may be edited
        again, the application defers certain analysis of the curve to
        determine if it's static. Therefore, isStatic may return false
        when edit operations convert the curve from non-static to static.
        It is possible to manually trigger curve analysis operations
        using the dgValidateCurve command.

        Returns: 
        ----- 
        Boolean value: true if the curve is static, false otherwise

        Parameters:
        -----
        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code .


        '''
        pass

    def numKeys(self, ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        numKeys(self, ReturnStatus: MFnAnimCurve.MStatus) -> int

        Synopsis
        -----
        Determines the number of keys on the Anim Curve Node.

        Returns: 
        ----- 
        Number of keys on the Anim Curve Node

        Parameters:
        -----
        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code


        '''
        pass

    def remove(self, index: int,
                        change: MAnimCurveChange): 
        '''
        remove(self, index: int,
                        change: MAnimCurveChange)

        Synopsis
        -----
        Removes the key at the specified index. If this method is called
        from within an MItKeyframe iterator, the results are undefined
        (i.e., it is likely that the incorrect key will be removed). This
        is because keys are automatically sorted (i.e., assigned new
        index values) everytime time they are modified in such a manner
        that could cause them to change order (e.g., they are moved, keys
        are inserted or removed, etc.).

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> Index of the key to be removed 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information.


        '''
        pass

    @overload
    def addKeyframe(self, time: MTime,
                        value: double,
                        change: MAnimCurveChange): 
        '''
        addKeyframe(self, time: MTime,
                        value: double,
                        change: MAnimCurveChange)

        Synopsis
        -----
        Adds a new key with the given value at the specified time.
        Tangent types are set to kTangentGlobal. If you immediately query
        this key for its tangent type (after it is added), it will not be
        kTangentGlobal, rather it will be the specific type referred to
        by kTangentGlobal.

        Returns:
        -----
        None

        Parameters:
        -----
        time: MTime
        	[in] -> Time at which the key is to be added 

        value: double
        	[in] -> Value to which the key is to be set 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information.


        '''
        pass

    @overload
    def addKeyframe(self, time: MTime,
                        value: double,
                        tangentInType: MFnAnimCurve.TangentType,
                        tangentOutType: MFnAnimCurve.TangentType,
                        change: MAnimCurveChange): 
        '''
        addKeyframe(self, time: MTime,
                        value: double,
                        tangentInType: MFnAnimCurve.TangentType,
                        tangentOutType: MFnAnimCurve.TangentType,
                        change: MAnimCurveChange)

        Synopsis
        -----
        Adds a new key with the given value and tangent types at the
        specified time.

        Returns:
        -----
        None

        Parameters:
        -----
        time: MTime
        	[in] -> Time at which the key is to be added 

        value: double
        	[in] -> Value to which the key is to be set 

        tangentInType: MFnAnimCurve.TangentType
        	[in] -> In tangent type for the key 

        tangentOutType: MFnAnimCurve.TangentType
        	[in] -> Out tangent type for the key 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information.


        '''
        pass

    @overload
    def addKey(self, time: MTime,
                        value: double,
                        tangentInType: MFnAnimCurve.TangentType,
                        tangentOutType: MFnAnimCurve.TangentType,
                        change: MAnimCurveChange,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        addKey(self, time: MTime,
                        value: double,
                        tangentInType: MFnAnimCurve.TangentType,
                        tangentOutType: MFnAnimCurve.TangentType,
                        change: MAnimCurveChange,
                        ReturnStatus: MFnAnimCurve.MStatus) -> int

        Synopsis
        -----
        Adds a new key with the given value and tangent types at the
        specified time for curves of type kAnimCurveTA, kAnimCurveTL and
        kAnimCurveTU.

        Returns: 
        ----- 
        Index of the added key

        Parameters:
        -----
        time: MTime
        	[in] -> Time at which the key is to be added 

        value: double
        	[in] -> Value to which the key is to be set 

        tangentInType: MFnAnimCurve.TangentType
        	[in] -> In tangent type for the key 

        tangentOutType: MFnAnimCurve.TangentType
        	[in] -> Out tangent type for the key 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information. 

        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code


        '''
        pass

    @overload
    def addKey(self, timeInput: MTime,
                        timeValue: MTime,
                        tangentInType: MFnAnimCurve.TangentType,
                        tangentOutType: MFnAnimCurve.TangentType,
                        change: MAnimCurveChange,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        addKey(self, timeInput: MTime,
                        timeValue: MTime,
                        tangentInType: MFnAnimCurve.TangentType,
                        tangentOutType: MFnAnimCurve.TangentType,
                        change: MAnimCurveChange,
                        ReturnStatus: MFnAnimCurve.MStatus) -> int

        Synopsis
        -----
        Adds a new key with the given output time value and tangent types
        at the specified input time for curves of type kAnimCurveTT.

        Returns: 
        ----- 
        Index of the added key

        Parameters:
        -----
        timeInput: MTime
        	[in] -> Time at which the key is to be added 

        timeValue: MTime
        	[in] -> Value to which the key is to be set 

        tangentInType: MFnAnimCurve.TangentType
        	[in] -> In tangent type for the key 

        tangentOutType: MFnAnimCurve.TangentType
        	[in] -> Out tangent type for the key 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information. 

        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code


        '''
        pass

    @overload
    def addKey(self, unitlessInput: double,
                        value: double,
                        tangentInType: MFnAnimCurve.TangentType,
                        tangentOutType: MFnAnimCurve.TangentType,
                        change: MAnimCurveChange,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        addKey(self, unitlessInput: double,
                        value: double,
                        tangentInType: MFnAnimCurve.TangentType,
                        tangentOutType: MFnAnimCurve.TangentType,
                        change: MAnimCurveChange,
                        ReturnStatus: MFnAnimCurve.MStatus) -> int

        Synopsis
        -----
        Adds a new key with the given value and tangent types at the
        specified unitless input for curves of type kAnimCurveUA,
        kAnimCurveUL and kAnimCurveUU.

        Returns: 
        ----- 
        Index of added key

        Parameters:
        -----
        unitlessInput: double
        	[in] -> Unitless input at which the key is to be added 

        value: double
        	[in] -> Value to which the key is to be set 

        tangentInType: MFnAnimCurve.TangentType
        	[in] -> In tangent type for the key 

        tangentOutType: MFnAnimCurve.TangentType
        	[in] -> Out tangent type for the key 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information. 

        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code


        '''
        pass

    @overload
    def addKey(self, unitlessInput: double,
                        timeValue: MTime,
                        tangentInType: MFnAnimCurve.TangentType,
                        tangentOutType: MFnAnimCurve.TangentType,
                        change: MAnimCurveChange,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        addKey(self, unitlessInput: double,
                        timeValue: MTime,
                        tangentInType: MFnAnimCurve.TangentType,
                        tangentOutType: MFnAnimCurve.TangentType,
                        change: MAnimCurveChange,
                        ReturnStatus: MFnAnimCurve.MStatus) -> int

        Synopsis
        -----
        Adds a new key with the given output time value and tangent types
        at the specified unitless input for curves of type kAnimCurveUT.

        Returns: 
        ----- 
        Index of added key

        Parameters:
        -----
        unitlessInput: double
        	[in] -> Unitless input at which the key is to be added 

        timeValue: MTime
        	[in] -> Value to which the key is to be set 

        tangentInType: MFnAnimCurve.TangentType
        	[in] -> In tangent type for the key 

        tangentOutType: MFnAnimCurve.TangentType
        	[in] -> Out tangent type for the key 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information. 

        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code


        '''
        pass

    def addKeys(self, timeArray: MTimeArray,
                        valueArray: MDoubleArray,
                        tangentInType: MFnAnimCurve.TangentType,
                        tangentOutType: MFnAnimCurve.TangentType,
                        keepExistingKeys: bool,
                        change: MAnimCurveChange): 
        '''
        addKeys(self, timeArray: MTimeArray,
                        valueArray: MDoubleArray,
                        tangentInType: MFnAnimCurve.TangentType,
                        tangentOutType: MFnAnimCurve.TangentType,
                        keepExistingKeys: bool,
                        change: MAnimCurveChange)

        Synopsis
        -----
        Add a set of new keys with the given corresponding values and
        tangent types at the specified times. This method only works for
        Anim Curves of type kAnimCurveTA, kAnimCurveTL and
        kAnimCurveTU.This method is tuned to provide best performance
        when:These optimisations are geared towards motion capture plug-
        ins where a large numbers of keys must be added to a curve in a
        single operation.Note: The timeArray and valueArray arrays are
        owned by the calling function. This method will copy those arrays
        to internal structures for use. As such, It is up to the caller
        to ensure that the memory allocated for the above arrays are
        deallocated appropriately.

        Returns:
        -----
        None

        Parameters:
        -----
        timeArray: MTimeArray
        	[in] -> Times at which keys are to be added 

        valueArray: MDoubleArray
        	[in] -> Values to which the keys is to be set 

        tangentInType: MFnAnimCurve.TangentType
        	[in] -> In tangent type for all the added keys 

        tangentOutType: MFnAnimCurve.TangentType
        	[in] -> Out tangent type for all the added keys 

        keepExistingKeys: bool
        	[in] -> Specifies whether the new keys should be merged with existing keys, or if they should be cut prior to adding the new keys 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information.


        '''
        pass

    def addKeysWithTangents(self, timeArray: MTimeArray,
                        valueArray: MDoubleArray,
                        tangentInType: MFnAnimCurve.TangentType,
                        tangentOutType: MFnAnimCurve.TangentType,
                        tangentInTypeArray: MIntArray,
                        tangentOutTypeArray: MIntArray,
                        tangentInXArray: MDoubleArray,
                        tangentInYArray: MDoubleArray,
                        tangentOutXArray: MDoubleArray,
                        tangentOutYArray: MDoubleArray,
                        tangentsLockedArray: MIntArray,
                        weightsLockedArray: MIntArray,
                        convertUnits: bool,
                        keepExistingKeys: bool,
                        change: MAnimCurveChange): 
        '''
        addKeysWithTangents(self, timeArray: MTimeArray,
                        valueArray: MDoubleArray,
                        tangentInType: MFnAnimCurve.TangentType,
                        tangentOutType: MFnAnimCurve.TangentType,
                        tangentInTypeArray: MIntArray,
                        tangentOutTypeArray: MIntArray,
                        tangentInXArray: MDoubleArray,
                        tangentInYArray: MDoubleArray,
                        tangentOutXArray: MDoubleArray,
                        tangentOutYArray: MDoubleArray,
                        tangentsLockedArray: MIntArray,
                        weightsLockedArray: MIntArray,
                        convertUnits: bool,
                        keepExistingKeys: bool,
                        change: MAnimCurveChange)

        Synopsis
        -----
        Add a set of new keys with the given corresponding values and
        tangent types at the specified times. This method only works for
        Anim Curves of type kAnimCurveTA, kAnimCurveTL and
        kAnimCurveTU.(Optional) Specify the tangent types for keys in
        tangentInTypeArray and tangentOutTypeArray. When an INT_MAX is
        found, the method will use the tangent types from tangentInType
        and tangentOutType parameters.(Optional) Specify the tangents for
        keys in tangentInXArray, tangentInYArray, tangentOutXArray and
        tangentOutYArray. When a DBL_MAX is found, the method will leave
        tangents unchanged.(Optional) Specify whether the tangents should
        be locked before the method returns in tangentsLockedArray. When
        an INT_MAX is found, the tangent lock is unchanged.(Optional)
        Specify whether the weights should be locked before the method
        returns in weightsLockedArray. When an INT_MAX is found, the
        weight lock is unchanged.This method is tuned to provide best
        performance when:These optimisations are geared towards motion
        capture plug-ins where a large numbers of keys must be added to a
        curve in a single operation.Note: All arrays are owned by the
        calling function. This method will copy those arrays to internal
        structures for use. As such, It is up to the caller to ensure
        that the memory allocated for the above arrays are deallocated
        appropriately.

        Returns:
        -----
        None

        Parameters:
        -----
        timeArray: MTimeArray
        	[in] -> Times at which keys are to be added 

        valueArray: MDoubleArray
        	[in] -> Values to which the keys is to be set 

        tangentInType: MFnAnimCurve.TangentType
        	[in] -> In tangent type for all the added keys 

        tangentOutType: MFnAnimCurve.TangentType
        	[in] -> Out tangent type for all the added keys 

        tangentInTypeArray: MIntArray
        	[in] -> In tangent types for individual added keys 

        tangentOutTypeArray: MIntArray
        	[in] -> Out tangent types for individual added keys 

        tangentInXArray: MDoubleArray
        	[in] -> Absolute x value of the slope of in tangent 

        tangentInYArray: MDoubleArray
        	[in] -> Absolute y value of the slope of in tangent 

        tangentOutXArray: MDoubleArray
        	[in] -> Absolute x value of the slope of out tangent 

        tangentOutYArray: MDoubleArray
        	[in] -> Absolute y value of the slope of out tangent 

        tangentsLockedArray: MIntArray
        	[in] -> Lock or unlock the tangents 

        weightsLockedArray: MIntArray
        	[in] -> Lock or unlock the weights 

        convertUnits: bool
        	[in] -> Whether to convert to UI units before setting 

        keepExistingKeys: bool
        	[in] -> Specifies whether the new keys should be merged with existing keys, or if they should be cut prior to adding the new keys 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information.


        '''
        pass

    def insertKey(self, time: MTime,
                        breakdown: bool,
                        change: MAnimCurveChange,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        insertKey(self, time: MTime,
                        breakdown: bool,
                        change: MAnimCurveChange,
                        ReturnStatus: MFnAnimCurve.MStatus) -> int

        Synopsis
        -----
        Introduced in 2019.0 Inserts a key at the specified time
        adjusting neighboring tangents to maintain curve shape.This
        method is the API equivalent to setKeyframe -insert.

        Returns:
        -----
        None

        Parameters:
        -----
        time: MTime
        	[in] -> Time to insert the key 

        breakdown: bool
        	[in] -> Whether the new key is a breakdown key 

        change: MAnimCurveChange
        	[in] -> Optional cache to store undo/redo information. 

        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code 


        '''
        pass

    @overload
    def find(self, time: MTime,
                        index: int,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        find(self, time: MTime,
                        index: int,
                        ReturnStatus: MFnAnimCurve.MStatus) -> bool

        Synopsis
        -----
        Determines the index of the key which is set at the specified
        time.

        Returns: 
        ----- 
        Boolean value: true if the index is found false otherwise

        Parameters:
        -----
        time: MTime
        	[in] -> Time for which a key index is required 

        index: int
        	[out] -> Key index at the specified time (implicit return) 

        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code


        '''
        pass

    @overload
    def find(self, unitlessInput: double,
                        index: int,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        find(self, unitlessInput: double,
                        index: int,
                        ReturnStatus: MFnAnimCurve.MStatus) -> bool

        Synopsis
        -----
        Determines the index of the key which is set at the specified
        unitless input value.

        Returns: 
        ----- 
        Boolean value: true if the index is found false otherwise

        Parameters:
        -----
        unitlessInput: double
        	[in] -> Value for which a key index is required 

        index: int
        	[out] -> Key index at the specified time (implicit return) 

        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code


        '''
        pass

    @overload
    def findClosest(self, time: MTime,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        findClosest(self, time: MTime,
                        ReturnStatus: MFnAnimCurve.MStatus) -> int

        Synopsis
        -----
        Determines the index of the key which is set at the time closest
        to the specified time.

        Returns: 
        ----- 
        Key index closest to the specified time

        Parameters:
        -----
        time: MTime
        	[in] -> Time for which a key index is required 

        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code .


        '''
        pass

    @overload
    def findClosest(self, unitlessInput: double,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        findClosest(self, unitlessInput: double,
                        ReturnStatus: MFnAnimCurve.MStatus) -> int

        Synopsis
        -----
        Determines the index of the key which is set at the time closest
        to the specified unitless input value.

        Returns: 
        ----- 
        Key index closest to the specified time

        Parameters:
        -----
        unitlessInput: double
        	[in] -> Input value for which a key index is required 

        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code .


        '''
        pass

    def time(self, index: int,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        time(self, index: int,
                        ReturnStatus: MFnAnimCurve.MStatus) -> MTime

        Synopsis
        -----
        Determines the time of the key at the specified index.

        Returns: 
        ----- 
        Time of the key at the given index. The unit defaults to
        MTime::kFilm (i.e., 24 frames/second)

        Parameters:
        -----
        index: int
        	[in] -> Index of the key for which the time is required 

        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code .


        '''
        pass

    def value(self, index: int,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        value(self, index: int,
                        ReturnStatus: MFnAnimCurve.MStatus) -> double

        Synopsis
        -----
        Determines the value of the key at the specified index. This
        method should only be used on Anim Curves of type kAnimCurve*A,
        kAnimCurve*L or kAnimCurve*U.

        Returns: 
        ----- 
        Value of the key

        Parameters:
        -----
        index: int
        	[in] -> Index of the key for which the value is required 

        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code .


        '''
        pass

    def quaternionW(self, index: int,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        quaternionW(self, index: int,
                        ReturnStatus: MFnAnimCurve.MStatus) -> double

        Synopsis
        -----
        Introduced in 2024.0 Returns the quaternionW of the key at the
        specified index.This method should only be used on Anim Curves of
        type kAnimCurveTA.

        Returns: 
        ----- 
        Value of the key

        Parameters:
        -----
        index: int
        	[in] -> Index of the key for which the value is required 

        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code .


        '''
        pass

    def unitlessInput(self, index: int,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        unitlessInput(self, index: int,
                        ReturnStatus: MFnAnimCurve.MStatus) -> double

        Synopsis
        -----
        Determines the unitless input value of the key at the specified
        index. This method should only be used on Anim Curves of type
        kAnimCurveU*.

        Returns: 
        ----- 
        Input value at which the key is set

        Parameters:
        -----
        index: int
        	[in] -> Index of the key for which the input value is required 

        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code .


        '''
        pass

    def setValue(self, index: int,
                        value: double,
                        change: MAnimCurveChange): 
        '''
        setValue(self, index: int,
                        value: double,
                        change: MAnimCurveChange)

        Synopsis
        -----
        Sets the value of the key at the specified index. This method
        should only be used on Anim Curves of type kAnimCurve*A,
        kAnimCurve*L or kAnimCurve*U.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> Index of the key for which the value is to be set 

        value: double
        	[in] -> Value to which the key is to be set 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information.


        '''
        pass

    def setQuaternionW(self, index: int,
                        quaternionW: double,
                        change: MAnimCurveChange): 
        '''
        setQuaternionW(self, index: int,
                        quaternionW: double,
                        change: MAnimCurveChange)

        Synopsis
        -----
        Introduced in 2024.0 Sets the quaternionW of the key at the
        specified index.This method should only be used on Anim Curves of
        type kAnimCurve*A.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> Index of the key for which the value is to be set 

        quaternionW: double
        	[in] -> Quaternion W component to which the key is to be set 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information.


        '''
        pass

    def setTime(self, index: int,
                        time: MTime,
                        change: MAnimCurveChange): 
        '''
        setTime(self, index: int,
                        time: MTime,
                        change: MAnimCurveChange)

        Synopsis
        -----
        Sets the time of the key at the specified index. This will fail
        if setting the time would require re-ordering of the keys. This
        method should only be used on Anim Curves of type
        kAnimCurveT*.Tangents may be changed so that the curve remains
        monotonic with respect to time.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> Index of the key for which the time is to be set 

        time: MTime
        	[in] -> Time to which the indexed key time is to be set 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information.


        '''
        pass

    def setUnitlessInput(self, index: int,
                        unitlessInput: double,
                        change: MAnimCurveChange): 
        '''
        setUnitlessInput(self, index: int,
                        unitlessInput: double,
                        change: MAnimCurveChange)

        Synopsis
        -----
        Sets the value of the unitless input of the key at the specified
        index. This will fail if setting the value would require re-
        ordering of the keys. This method should only be used on Anim
        Curves of type kAnimCurveU*.Tangents may be changed so that the
        curve remains monotonic with respect to the unitless input.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> Index of the key for which the unitless input value is to be set 

        unitlessInput: double
        	[in] -> Value to which the indexed key unitless input value is to be set 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information.


        '''
        pass

    def isTimeInput(self, ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        isTimeInput(self, ReturnStatus: MFnAnimCurve.MStatus) -> bool

        Synopsis
        -----
        Determines the input type of the animCurve.

        Returns: 
        ----- 
        Boolean value: true if the curve takes time as input false
        otherwise.

        Parameters:
        -----
        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code .


        '''
        pass

    def isUnitlessInput(self, ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        isUnitlessInput(self, ReturnStatus: MFnAnimCurve.MStatus) -> bool

        Synopsis
        -----
        Determines the input type of the animCurve.

        Returns: 
        ----- 
        Boolean value: true if the curve takes a unitless value as input,
        false otherwise.

        Parameters:
        -----
        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code .


        '''
        pass

    def inTangentType(self, index: int,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        inTangentType(self, index: int,
                        ReturnStatus: MFnAnimCurve.MStatus) -> MFnAnimCurve.MFnAnimCurve

        Synopsis
        -----
        Determines the type of the tangent to the curve entering the
        current key.

        Returns: 
        ----- 
        Type of the tangent

        Parameters:
        -----
        index: int
        	[in] -> Index of the key for which the tangent type is required 

        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code .


        '''
        pass

    def outTangentType(self, index: int,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        outTangentType(self, index: int,
                        ReturnStatus: MFnAnimCurve.MStatus) -> MFnAnimCurve.MFnAnimCurve

        Synopsis
        -----
        Determines the type of the tangent to the curve leaving the
        current key.

        Returns: 
        ----- 
        Type of the tangent

        Parameters:
        -----
        index: int
        	[in] -> Index of the key for which the tangent type is required 

        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code .


        '''
        pass

    def setInTangentType(self, index: int,
                        tangentType: MFnAnimCurve.TangentType,
                        change: MAnimCurveChange): 
        '''
        setInTangentType(self, index: int,
                        tangentType: MFnAnimCurve.TangentType,
                        change: MAnimCurveChange)

        Synopsis
        -----
        Sets the type of the tangent to the curve entering the key at the
        specified index.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> Index of the key for which the tangent type is to be set 

        tangentType: MFnAnimCurve.TangentType
        	[in] -> Type to which the tangent is to be set 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information.


        '''
        pass

    def setOutTangentType(self, index: int,
                        tangentType: MFnAnimCurve.TangentType,
                        change: MAnimCurveChange): 
        '''
        setOutTangentType(self, index: int,
                        tangentType: MFnAnimCurve.TangentType,
                        change: MAnimCurveChange)

        Synopsis
        -----
        Sets the type of the tangent to the curve leaving the key at the
        specified index.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> Index of the key for which the tangent type is to be set 

        tangentType: MFnAnimCurve.TangentType
        	[in] -> Type to which the tangent is to be set 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information.


        '''
        pass

    def setTangentTypes(self, indexArray: MIntArray,
                        inTangentType: MFnAnimCurve.TangentType,
                        outTangentType: MFnAnimCurve.TangentType,
                        change: MAnimCurveChange): 
        '''
        setTangentTypes(self, indexArray: MIntArray,
                        inTangentType: MFnAnimCurve.TangentType,
                        outTangentType: MFnAnimCurve.TangentType,
                        change: MAnimCurveChange)

        Synopsis
        -----
        Sets the tangent types for multiple keys.

        Returns:
        -----
        None

        Parameters:
        -----
        indexArray: MIntArray
        	[in] -> Indices of the key for which the tangent type is to be set 

        inTangentType: MFnAnimCurve.TangentType
        	[in] -> Type to which the in tangent is to be set 

        outTangentType: MFnAnimCurve.TangentType
        	[in] -> Type to which the out tangent is to be set 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information.


        '''
        pass

    @overload
    def getTangent(self, index: int,
                        x: MFnAnimCurve.TangentValue,
                        y: MFnAnimCurve.TangentValue,
                        inTangent: bool): 
        '''
        getTangent(self, index: int,
                        x: MFnAnimCurve.TangentValue,
                        y: MFnAnimCurve.TangentValue,
                        inTangent: bool)

        Synopsis
        -----
        Determines the x,y value representing the vector of the in- or
        out-tangent (depending on the value of the inTangent parameter)
        to the curve for the key at the specified index. The values
        returned will be in Maya's internal units (seconds for time,
        centimeters for linear, radians for angles). The following
        examples demonstrates how to convert from internal units of
        seconds into the current user time unit.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> Index of the key for which the tangent x,y value is required 

        x: MFnAnimCurve.TangentValue
        	[out] -> The x value of the slope of the tangent in seconds 

        y: MFnAnimCurve.TangentValue
        	[out] -> Absolute y value of the slope of the tangent 

        inTangent: bool
        	[in] -> If true, the in-tangent is returned, else, the out-tangent is returned


        '''
        pass

    @overload
    def getTangent(self, index: int,
                        angle: MAngle,
                        weight: double,
                        inTangent: bool): 
        '''
        getTangent(self, index: int,
                        angle: MAngle,
                        weight: double,
                        inTangent: bool)

        Synopsis
        -----
        Determines the angle and weight of the in- or out-tangent to the
        curve for the key at the specified index. Recall that tangents
        are stored as vectors internally and in the Maya Ascii file
        format. This means that the returned angle and weight will be
        converted from an (x,y) pair to represent the vector according to
        the following formula:where x is in seconds and y is in
        centimeters for linear units and radians for angular units.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> Index of the key for which the tangent x,y value is required 

        angle: MAngle
        	[out] -> The tangent angle 

        weight: double
        	[out] -> The tangent weight 

        inTangent: bool
        	[in] -> If true, the inTangent is returned, else, the outTangent is returned


        '''
        pass

    @overload
    def setTangent(self, index: int,
                        x: MFnAnimCurve.TangentValue,
                        y: MFnAnimCurve.TangentValue,
                        inTangent: bool,
                        change: MAnimCurveChange,
                        convertUnits: bool): 
        '''
        setTangent(self, index: int,
                        x: MFnAnimCurve.TangentValue,
                        y: MFnAnimCurve.TangentValue,
                        inTangent: bool,
                        change: MAnimCurveChange,
                        convertUnits: bool)

        Synopsis
        -----
        Sets the tangent for the key at the specified index. If
        convertUnits is true (the default) the x value will be scaled by
        the current UI time units and the y value will be scaled by the
        relevant UI units for the output type of the animation curve
        (i.e. linear units for a curve that outputs linear data, and so
        on).Note that if this method is called on a locked tangent (which
        they are by default), the corresponding out- or in-tangent will
        be modified as well (i.e., they will both be set to fixed). To
        prevent this from occurring, you must first unlock the tangent,
        make your modifications and then restore the lock setting for the
        tangent afterwards.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> Index of the key for which the tangent type is to be set 

        x: MFnAnimCurve.TangentValue
        	[in] -> Absolute x value of the slope of the tangent 

        y: MFnAnimCurve.TangentValue
        	[in] -> Absolute y value of the slope of the tangent 

        inTangent: bool
        	[in] -> If true, the inTangent is modified, else, the outTangent is modified 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information. 

        convertUnits: bool
        	[in] -> Whether to convert to UI units before setting


        '''
        pass

    @overload
    def setTangent(self, index: int,
                        angle: MAngle,
                        weight: double,
                        inTangent: bool,
                        change: MAnimCurveChange,
                        convertUnits: bool): 
        '''
        setTangent(self, index: int,
                        angle: MAngle,
                        weight: double,
                        inTangent: bool,
                        change: MAnimCurveChange,
                        convertUnits: bool)

        Synopsis
        -----
        Sets the tangent for the key at the specified index. If
        convertUnits is true (the default) the x value will be scaled by
        the current UI time units and the y value will be scaled by the
        relevant UI units for the output type of the animation curve
        (i.e. linear units for a curve that outputs linear data, and so
        on).Recall that tangents are stored as vectors internally and in
        the Maya Ascii file format. This means that the provided angle
        and weight will be converted into an (x,y) pair to represent the
        vector according to the following formula:Note that if this
        method is called on a locked tangent (which they are by default),
        the corresponding out- or in-tangent will be modified as well
        (i.e., they will both be set to fixed). To prevent this from
        occurring, you must first unlock the tangent, make your
        modifications and then restore the lock setting for the tangent
        afterwards.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> Index of the key for which the tangent type is to be set 

        angle: MAngle
        	[in] -> The angle to set the tangent 

        weight: double
        	[in] -> The weight to set the tangent 

        inTangent: bool
        	[in] -> If true, the inTangent is modified, else, the outTangent is modified 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information. 

        convertUnits: bool
        	[in] -> Whether to convert to UI units before setting


        '''
        pass

    def setAngle(self, index: int,
                        angle: MAngle,
                        inTangent: bool,
                        change: MAnimCurveChange): 
        '''
        setAngle(self, index: int,
                        angle: MAngle,
                        inTangent: bool,
                        change: MAnimCurveChange)

        Synopsis
        -----
        Set the in- or out-angle of the tangent for the key at the given
        index. Note that if this method is called on a locked tangent
        (which they are by default), the corresponding out- or in-tangent
        will be modified as well (i.e., they will both be set to fixed).
        To prevent this from occurring, you must first unlock the
        tangent, make your modifications and then restore the lock
        setting for the tangent afterwards.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> Index of the key 

        angle: MAngle
        	[in] -> The new in- or out-angle for the key's tangent 

        inTangent: bool
        	[in] -> If true, set the in-tangent, else out-tangent 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information.


        '''
        pass

    def setWeight(self, index: int,
                        weight: double,
                        inTangent: bool,
                        change: MAnimCurveChange): 
        '''
        setWeight(self, index: int,
                        weight: double,
                        inTangent: bool,
                        change: MAnimCurveChange)

        Synopsis
        -----
        Set the in- or out-weight of the tangent for the key at the given
        index. Note that if this method is called on a locked weight
        (which they are by default), the corresponding out- or in-weight
        will be modified as well. To prevent this from occurring, you
        must first unlock the weight, make your modifications and then
        restore the lock setting for the weight afterwards.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> Index of the key 

        weight: double
        	[in] -> The new in- or out-weight for the key's tangent 

        inTangent: bool
        	[in] -> If true, set the in-tangent, else set out-tangent 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information.


        '''
        pass

    def weightsLocked(self, index: int,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        weightsLocked(self, index: int,
                        ReturnStatus: MFnAnimCurve.MStatus) -> bool

        Synopsis
        -----
        Determines whether the weights are locked at the given key.

        Returns: 
        ----- 
        Boolean value: true if the weights are locked, false otherwise.

        Parameters:
        -----
        index: int
        	[in] -> Index of the key to check for locked weights 

        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code .


        '''
        pass

    def tangentsLocked(self, index: int,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        tangentsLocked(self, index: int,
                        ReturnStatus: MFnAnimCurve.MStatus) -> bool

        Synopsis
        -----
        Determines whether the tangents are locked at the given key.

        Returns: 
        ----- 
        Boolean value: true if the tangents are locked, false otherwise.

        Parameters:
        -----
        index: int
        	[in] -> Index of the key to check for locked tangents 

        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code .


        '''
        pass

    def setWeightsLocked(self, index: int,
                        locked: bool,
                        change: MAnimCurveChange): 
        '''
        setWeightsLocked(self, index: int,
                        locked: bool,
                        change: MAnimCurveChange)

        Synopsis
        -----
        Lock or unlock the weights at the given key.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> Index of the key at which to set/unset the locks 

        locked: bool
        	[in] -> true if the weights are to be locked, false otherwise 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information.


        '''
        pass

    def setTangentsLocked(self, index: int,
                        locked: bool,
                        change: MAnimCurveChange): 
        '''
        setTangentsLocked(self, index: int,
                        locked: bool,
                        change: MAnimCurveChange)

        Synopsis
        -----
        Lock or unlock the tangents at the given key.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> Index of the key at which to set/unset the locks 

        locked: bool
        	[in] -> true if the tangents are to be locked, false otherwise 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information.


        '''
        pass

    def preInfinityType(self, ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        preInfinityType(self, ReturnStatus: MFnAnimCurve.MStatus) -> MFnAnimCurve.MFnAnimCurve

        Synopsis
        -----
        Determines the behaviour of the curve for the range occurring
        before the first key.

        Returns: 
        ----- 
        The current preInfinityType for the curve

        Parameters:
        -----
        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code .


        '''
        pass

    def postInfinityType(self, ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        postInfinityType(self, ReturnStatus: MFnAnimCurve.MStatus) -> MFnAnimCurve.MFnAnimCurve

        Synopsis
        -----
        Determines the behaviour of the curve for the range occurring
        after the last key.

        Returns: 
        ----- 
        The current postInfinityType for the curve

        Parameters:
        -----
        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code .


        '''
        pass

    def setPreInfinityType(self, infinityType: MFnAnimCurve.MFnAnimCurve,
                        change: MAnimCurveChange): 
        '''
        setPreInfinityType(self, infinityType: MFnAnimCurve.MFnAnimCurve,
                        change: MAnimCurveChange)

        Synopsis
        -----
        Set the behaviour of the curve for the range occurring before the
        first key.

        Returns:
        -----
        None

        Parameters:
        -----
        infinityType: MFnAnimCurve.MFnAnimCurve
        	[in] -> The infinity type to be set. 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information.


        '''
        pass

    def setPostInfinityType(self, infinityType: MFnAnimCurve.MFnAnimCurve,
                        change: MAnimCurveChange): 
        '''
        setPostInfinityType(self, infinityType: MFnAnimCurve.MFnAnimCurve,
                        change: MAnimCurveChange)

        Synopsis
        -----
        Set the behaviour of the curve for the range occurring after the
        last key.

        Returns:
        -----
        None

        Parameters:
        -----
        infinityType: MFnAnimCurve.MFnAnimCurve
        	[in] -> The infinity type to be set. 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information.


        '''
        pass

    def isWeighted(self, ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        isWeighted(self, ReturnStatus: MFnAnimCurve.MStatus) -> bool

        Synopsis
        -----
        Determines whether or not the curve has weighted tangents.

        Returns: 
        ----- 
        Boolean value: true if the curve has weighted tangents, false
        otherwise.

        Parameters:
        -----
        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code .


        '''
        pass

    def setIsWeighted(self, isWeighted: bool,
                        change: MAnimCurveChange): 
        '''
        setIsWeighted(self, isWeighted: bool,
                        change: MAnimCurveChange)

        Synopsis
        -----
        Sets whether or not the curve has weighted tangents.

        Returns:
        -----
        None

        Parameters:
        -----
        isWeighted: bool
        	[in] -> Whether or not the curve should have weighted tangents 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information.


        '''
        pass

    def isBreakdown(self, index: int,
                        ReturnStatus: MFnAnimCurve.MStatus): 
        '''
        isBreakdown(self, index: int,
                        ReturnStatus: MFnAnimCurve.MStatus) -> bool

        Synopsis
        -----
        Determines whether or not a key is a breakdown.

        Returns: 
        ----- 
        Boolean value: true if the key is a breakdown, false otherwise.

        Parameters:
        -----
        index: int
        	[in] -> The key's index 

        ReturnStatus: MFnAnimCurve.MStatus
        	[out] -> Status Code .


        '''
        pass

    def setIsBreakdown(self, index: int,
                        isBreakdown: bool,
                        change: MAnimCurveChange): 
        '''
        setIsBreakdown(self, index: int,
                        isBreakdown: bool,
                        change: MAnimCurveChange)

        Synopsis
        -----
        Sets the breakdown state of a key at a given index.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> Index of the key whose breakdown state is to be modified 

        isBreakdown: bool
        	[in] -> The new breakdown state for the key. 

        change: MAnimCurveChange
        	[out] -> Optional cache to store undo/redo information.


        '''
        pass

class AnimCurveType:
    '''Defines the input and output type of the animation curve. 
    Non-functional class.  Values for this enum:
    kAnimCurveTA
    kAnimCurveTL
    kAnimCurveTT
    kAnimCurveTU
    kAnimCurveUA
    kAnimCurveUL
    kAnimCurveUT
    kAnimCurveUU
    kAnimCurveUnknown
    '''

    def __init__(self):
        pass

    def kAnimCurveTA(self):
        '''This is an enum of AnimCurveType.
        - Description: Time to Angular. 
        - Value: 0
        '''
        pass

    def kAnimCurveTL(self):
        '''This is an enum of AnimCurveType.
        - Description: Time to Linear. 
        - Value: 1
        '''
        pass

    def kAnimCurveTT(self):
        '''This is an enum of AnimCurveType.
        - Description: Time to Time. 
        - Value: 2
        '''
        pass

    def kAnimCurveTU(self):
        '''This is an enum of AnimCurveType.
        - Description: Time to Unitless. 
        - Value: 3
        '''
        pass

    def kAnimCurveUA(self):
        '''This is an enum of AnimCurveType.
        - Description: Unitless to Angular. 
        - Value: 4
        '''
        pass

    def kAnimCurveUL(self):
        '''This is an enum of AnimCurveType.
        - Description: Unitless to Linear. 
        - Value: 5
        '''
        pass

    def kAnimCurveUT(self):
        '''This is an enum of AnimCurveType.
        - Description: Unitless to Time. 
        - Value: 6
        '''
        pass

    def kAnimCurveUU(self):
        '''This is an enum of AnimCurveType.
        - Description: Unitless to Unitless. 
        - Value: 7
        '''
        pass

    def kAnimCurveUnknown(self):
        '''This is an enum of AnimCurveType.
        - Description: Unknown type. 
        - Value: 8
        '''
        pass

class TangentType:
    '''Defines the type of the tangent. 
    Non-functional class.  Values for this enum:
    kTangentGlobal
    kTangentFixed
    kTangentLinear
    kTangentFlat
    kTangentSmooth
    kTangentStep
    kTangentSlow
    kTangentFast
    kTangentClamped
    kTangentPlateau
    kTangentStepNext
    kTangentAuto
    kTangentAutoMix
    kTangentAutoEase
    kTangentAutoCustom
    '''

    def __init__(self):
        pass

    def kTangentGlobal(self):
        '''This is an enum of TangentType.
        - Description: Global. 
        - Value: 0
        '''
        pass

    def kTangentFixed(self):
        '''This is an enum of TangentType.
        - Description: Fixed. 
        - Value: 1
        '''
        pass

    def kTangentLinear(self):
        '''This is an enum of TangentType.
        - Description: Linear. 
        - Value: 2
        '''
        pass

    def kTangentFlat(self):
        '''This is an enum of TangentType.
        - Description: Flag. 
        - Value: 3
        '''
        pass

    def kTangentSmooth(self):
        '''This is an enum of TangentType.
        - Description: Smooth. 
        - Value: 4
        '''
        pass

    def kTangentStep(self):
        '''This is an enum of TangentType.
        - Description: Step. 
        - Value: 5
        '''
        pass

    def kTangentSlow(self):
        '''This is an enum of TangentType.
        - Description: OBSOLETE kTangentSlow should not be used. Using this tangent type may produce unwanted and unexpected results. 
        - Value: 6
        '''
        pass

    def kTangentFast(self):
        '''This is an enum of TangentType.
        - Description: OBSOLETE kTangentFast should not be used. Using this tangent type may produce unwanted and unexpected results. 
        - Value: 7
        '''
        pass

    def kTangentClamped(self):
        '''This is an enum of TangentType.
        - Description: Clamped. 
        - Value: 8
        '''
        pass

    def kTangentPlateau(self):
        '''This is an enum of TangentType.
        - Description: Plateau. 
        - Value: 9
        '''
        pass

    def kTangentStepNext(self):
        '''This is an enum of TangentType.
        - Description: StepNext. 
        - Value: 10
        '''
        pass

    def kTangentAuto(self):
        '''This is an enum of TangentType.
        - Description: Auto. 
        - Value: 11
        '''
        pass

    def kTangentAutoMix(self):
        '''This is an enum of TangentType.
        - Description: Introduced in 2022.0 2022.0:Introduced in this version. AutoMix 
        - Value: 27
        '''
        pass

    def kTangentAutoEase(self):
        '''This is an enum of TangentType.
        - Description: Introduced in 2022.0 2022.0:Introduced in this version. AutoEase 
        - Value: 28
        '''
        pass

    def kTangentAutoCustom(self):
        '''This is an enum of TangentType.
        - Description: Introduced in 2022.0 2022.0:Introduced in this version. AutoCustom 
        - Value: 29
        '''
        pass

class InfinityType:
    '''Defines the type of the infinity. 
    Non-functional class.  Values for this enum:
    kConstant
    kLinear
    kCycle
    kCycleRelative
    kOscillate
    '''

    def __init__(self):
        pass

    def kConstant(self):
        '''This is an enum of InfinityType.
        - Description: Constant. 
        - Value: 0
        '''
        pass

    def kLinear(self):
        '''This is an enum of InfinityType.
        - Description: Linear. 
        - Value: 1
        '''
        pass

    def kCycle(self):
        '''This is an enum of InfinityType.
        - Description: Cycle. 
        - Value: 3
        '''
        pass

    def kCycleRelative(self):
        '''This is an enum of InfinityType.
        - Description: Cycle relative. 
        - Value: 4
        '''
        pass

    def kOscillate(self):
        '''This is an enum of InfinityType.
        - Description: Oscillate. 
        - Value: 5
        '''
        pass

class MFnBlendShapeDeformer:
    '''blend shape deformer function set
MFnBlendShapeDeformer is the function set for blend shape deformers. A blend shape
deformer takes a base shape (polygonal surface, curve, surface,
or lattice) and blends it with other target shapes based on
weight values.
The blend shape deformer is actually a small network of
dependency nodes in the dependency graph. This function set is
provided to make manipulation of the network easier. The main
deformer node should be given to this function set as its object.
There are three parts to a blend shape deformer. There are the
base objects, the target objects, and the weight values.
The base objects are the shapes that are to be deformed. There
must be at least one base object. The base objects will change
form as the targets and deformation parameters are modified.
Each base object has a list of target objects that affect its
shape. Each target is associated with one of the the deformer's
weight values. When the weight value increases, the target has
more influence on the base shape.
There is just one array of weight values between all of the base
objects and targets. So, it is possible for targets of different
base objects to share the same weight index. When the weight
value changes, it will affect all of the base objects that have
targets using that weight value.
It is also possible to chain together target shapes so that a
base object will deform through each shape one at a time as the
weight value increases. This is done by adding multiple targets
to a base shape using the same weight index for all of them. When
each target is added, a weight value is specified at which that
target will be in full effect. Give each target a different full
weight value.
For example, one could take a sphere and make it blend into a
cone and then into a cylinder. One way to do this is to make
sphere the base shape. Then, add the cone as a target for the
sphere at weight index 0 with a full effect weight of 0.5. Next,
add the cylinder as a second target for the sphere also at weight
index 0, but with a full effect weight of 1.0. Now, as the weight
goes from 0 to 1, the base shape will start as a sphere, morph
into a cone, and then into a cylinder.
It is not necessary for the base shape and its targets to have
identical vertex/CV counts, but the blend will be more effective
if they do.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kBlendShape.Reimplemented from MFnDependencyNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> staticchar*

        Synopsis
        -----
        Returns the name of this class.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def create(self, baseObject: MObject,
                        originSpace: MFnBlendShapeDeformer.Origin,
                        ReturnStatus: MFnBlendShapeDeformer.MStatus): 
        '''
        create(self, baseObject: MObject,
                        originSpace: MFnBlendShapeDeformer.Origin,
                        ReturnStatus: MFnBlendShapeDeformer.MStatus) -> MObject

        Synopsis
        -----
        Creates a new blend shape deformer in the dependency graph with
        the specified shape as the baseObject.

        Returns: 
        ----- 
        A handle to the new deformer

        Parameters:
        -----
        baseObject: MObject
        	[in] -> a base object for the deformer 

        originSpace: MFnBlendShapeDeformer.Origin
        	[in] -> origin about which to deform 

        ReturnStatus: MFnBlendShapeDeformer.MStatus
        	[out] -> return status


        '''
        pass

    @overload
    def create(self, baseObjects: MObjectArray,
                        originSpace: MFnBlendShapeDeformer.Origin,
                        historyLoc: MFnBlendShapeDeformer.HistoryLocation,
                        ReturnStatus: MFnBlendShapeDeformer.MStatus): 
        '''
        create(self, baseObjects: MObjectArray,
                        originSpace: MFnBlendShapeDeformer.Origin,
                        historyLoc: MFnBlendShapeDeformer.HistoryLocation,
                        ReturnStatus: MFnBlendShapeDeformer.MStatus) -> MObject

        Synopsis
        -----
        Creates a new blend shape deformer in the dependency graph. This
        method differs from the other MFnBlendShapeDeformer::create in
        that it allows multiple base shapes to be supplied at create time
        and it allows the use of the front-of-chain history location,
        which puts the blendShape ahead of other deformers such as
        skinning deformers.

        Returns: 
        ----- 
        A handle to the new deformer

        Parameters:
        -----
        baseObjects: MObjectArray
        	[in] -> base object(s) for the deformer 

        originSpace: MFnBlendShapeDeformer.Origin
        	[in] -> origin about which to deform 

        historyLoc: MFnBlendShapeDeformer.HistoryLocation
        	[in] -> where in the shape's history to place the deformer 

        ReturnStatus: MFnBlendShapeDeformer.MStatus
        	[out] -> return status


        '''
        pass

    def addBaseObject(self, object: MObject): 
        '''
        addBaseObject(self, object: MObject)

        Synopsis
        -----
        Adds a new base object to the deformer. This object will be
        deformed as targets are added for it and the deformation
        parameters change.

        Returns:
        -----
        None

        Parameters:
        -----
        object: MObject
        	[in] -> new base object


        '''
        pass

    def getBaseObjects(self, objects: MObjectArray): 
        '''
        getBaseObjects(self, objects: MObjectArray)

        Synopsis
        -----
        Get a list of all of the base objects for this deformer. The
        objects returned will be the deformed versions of the base
        objects.

        Returns:
        -----
        None

        Parameters:
        -----
        objects: MObjectArray
        	[out] -> storage for the array of base objects


        '''
        pass

    @overload
    def addTarget(self, baseObject: MObject,
                        weightIndex: int,
                        newTarget: MObject,
                        fullWeight: double,
                        targetType: MFnBlendShapeDeformer.TargetType): 
        '''
        addTarget(self, baseObject: MObject,
                        weightIndex: int,
                        newTarget: MObject,
                        fullWeight: double,
                        targetType: MFnBlendShapeDeformer.TargetType)

        Synopsis
        -----
        Adds a new target object for the given base object. The weight
        index says which of the deformer's weight values will control
        this target's affects on the base object. The full weight
        argument determines at what weight the target is in full effect.
        If a base object has no other targets and the weight is set to
        the 'full weight', then the base object will look just like the
        target object.

        Returns:
        -----
        None

        Parameters:
        -----
        baseObject: MObject
        	[in] -> base object for the target 

        weightIndex: int
        	[in] -> weight index to use for target's effect 

        newTarget: MObject
        	[in] -> new target object for the given base 

        fullWeight: double
        	[in] -> weight value at which the target is in full effect 

        targetType: MFnBlendShapeDeformer.TargetType
        	[in] -> target type for the target


        '''
        pass

    @overload
    def addTarget(self, baseObject: MObject,
                        weightIndex: int,
                        fullWeight: double,
                        targetType: MFnBlendShapeDeformer.TargetType): 
        '''
        addTarget(self, baseObject: MObject,
                        weightIndex: int,
                        fullWeight: double,
                        targetType: MFnBlendShapeDeformer.TargetType)

        Synopsis
        -----
        Adds a new delta target object for the given base object. The
        weight index says which of the deformer's weight values will
        control this target's affects on the base object. The full weight
        argument determines at what weight the target is in full effect.
        If a base object has no other targets and the weight is set to
        the 'full weight', then the base object will look just like the
        target object.

        Returns:
        -----
        None

        Parameters:
        -----
        baseObject: MObject
        	[in] -> base object for the target 

        weightIndex: int
        	[in] -> weight index to use for target's effect 

        fullWeight: double
        	[in] -> weight value at which the target is in full effect 

        targetType: MFnBlendShapeDeformer.TargetType
        	[in] -> target type for the target


        '''
        pass

    def removeTarget(self, baseObject: MObject,
                        weightIndex: int,
                        target: MObject,
                        fullWeight: double): 
        '''
        removeTarget(self, baseObject: MObject,
                        weightIndex: int,
                        target: MObject,
                        fullWeight: double)

        Synopsis
        -----
        Remove a target object for the given base object. The weight
        index specifies the index at which target is connected. The full
        weight argument specifies at what weight the target is in full
        effect.

        Returns:
        -----
        None

        Parameters:
        -----
        baseObject: MObject
        	[in] -> base object for the target 

        weightIndex: int
        	[in] -> weight index corresponding to the target 

        target: MObject
        	[in] -> target object for the given base to be removed 

        fullWeight: double
        	[in] -> weight value at which the target is in full effect


        '''
        pass

    def getTargets(self, baseObject: MObject,
                        weightIndex: int,
                        targetObjects: MObjectArray): 
        '''
        getTargets(self, baseObject: MObject,
                        weightIndex: int,
                        targetObjects: MObjectArray)

        Synopsis
        -----
        Get a list of all of the target objects for the given base object
        that affect it based on the given weight index.

        Returns:
        -----
        None

        Parameters:
        -----
        baseObject: MObject
        	[in] -> The base shape of interest. 

        weightIndex: int
        	[in] -> The index of the weight attribute. Since the weight indices may be sparse, the weightIndexList method should be used to find the weight indices used by a given blendShape. 

        targetObjects: MObjectArray
        	[out] -> Storage for the returned array of target objects.


        '''
        pass

    def numWeights(self, ReturnStatus: MFnBlendShapeDeformer.MStatus): 
        '''
        numWeights(self, ReturnStatus: MFnBlendShapeDeformer.MStatus) -> int

        Synopsis
        -----
        Return the number of weight values that this blend shape deformer
        has. The number of weight values is equal to the number of
        targets. Targets are either shapes in the dag or baked data on
        the blendShape node (when a target shape is deleted).

        Returns: 
        ----- 
        The number of weight indices

        Parameters:
        -----
        ReturnStatus: MFnBlendShapeDeformer.MStatus
        	[out] -> return status


        '''
        pass

    def weightIndexList(self, indexList: MIntArray): 
        '''
        weightIndexList(self, indexList: MIntArray)

        Synopsis
        -----
        Return the array index numbers corresponding to the targets. The
        resulting index list will be the length of
        MFnBlendShape::numWeights. This method exists because the indices
        of the targets can be sparse. For example, if a target has been
        removed using Deform -> Edit BlendShape -> Remove.

        Returns:
        -----
        None

        Parameters:
        -----
        indexList: MIntArray
        	[out] -> the array index numbers for the blendShape targets


        '''
        pass

    def targetItemIndexList(self, weightIndex: int,
                        baseObject: MObject,
                        targetItemIndices: MIntArray): 
        '''
        targetItemIndexList(self, weightIndex: int,
                        baseObject: MObject,
                        targetItemIndices: MIntArray)

        Synopsis
        -----
        A base object may have more than one target using the same
        element of the blendShape's 'weights' array. We refer to these as
        the base object's "target items" for that weight index.Each
        target item should have a different 'fullWeight' value at which
        it takes full effect. As the value of the weights array element
        approaches the lowest of those 'fullWeight' values the associated
        target item has an increasing effect on the shape of the base
        object. As the value of the weights array element passes that
        first 'fullWeight' value and starts to approach the next higher
        'fullWeight' value, the next target item starts to gain influence
        and the influence of the previous one drops off.In this way, as
        the weight value increases, influence passes from one target item
        to another, allowing the target object to morph through a
        sequence of different target shapes.Each target item is connected
        to an element of the blendShape deformer's 'inputTargetItem'
        array for that base object and weights array index. The
        inputTargetItem array index is calculated as follows: index =
        fullWeight * 1000 + 5000.For example, if a base object has three
        different targetItems for a given weights array element, having
        fullWeight values of 0.5, 1.0 and 2.0, they will be connected to
        inputTargetItem array indices 5500, 6000 and 7000,
        respectively.This method returns an array containing the
        inputTargetItem array indices of all the target items of a given
        base object which use the specified weight index.

        Returns:
        -----
        None

        Parameters:
        -----
        weightIndex: int
        	[in] -> 'weights' array index. 

        baseObject: MObject
        	[in] -> The deformed object of interest 

        targetItemIndices: MIntArray
        	[out] -> 'inputTargetItem' array indices of the requested target items.


        '''
        pass

    def weight(self, index: int,
                        ReturnStatus: MFnBlendShapeDeformer.MStatus): 
        '''
        weight(self, index: int,
                        ReturnStatus: MFnBlendShapeDeformer.MStatus) -> float

        Synopsis
        -----
        Get the weight value at the given index. To be valid, a weight
        value should only be requested at index values returned by
        MFnBlendShapeDeformer::weightIndexList.

        Returns: 
        ----- 
        The weight value

        Parameters:
        -----
        index: int
        	[in] -> index of weight value 

        ReturnStatus: MFnBlendShapeDeformer.MStatus
        	[out] -> return status


        '''
        pass

    def setWeight(self, index: int,
                        weight: float): 
        '''
        setWeight(self, index: int,
                        weight: float)

        Synopsis
        -----
        Set the weight value at the given index.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> index of weight value 

        weight: float
        	[in] -> new weight value


        '''
        pass

    def envelope(self, ReturnStatus: MFnBlendShapeDeformer.MStatus): 
        '''
        envelope(self, ReturnStatus: MFnBlendShapeDeformer.MStatus) -> float

        Synopsis
        -----
        Gets the envelope value of the deformer. The envelope is a global
        scale factor that is applied to all of the weight values in the
        deformer. The envelope can be used increase or decrease the
        effects of all of the targets at the same time.

        Returns: 
        ----- 
        Envelope value

        Parameters:
        -----
        ReturnStatus: MFnBlendShapeDeformer.MStatus
        	[out] -> return status


        '''
        pass

    def setEnvelope(self, envelope: float): 
        '''
        setEnvelope(self, envelope: float)

        Synopsis
        -----
        Sets the envelope value of the deformer. The envelope is a global
        scale factor that is applied to all of the weight values in the
        deformer. The envelope can be used increase or decrease the
        effects of all of the targets at the same time.

        Returns:
        -----
        None

        Parameters:
        -----
        envelope: float
        	[in] -> envelope value


        '''
        pass

    def origin(self, ReturnStatus: MFnBlendShapeDeformer.MStatus): 
        '''
        origin(self, ReturnStatus: MFnBlendShapeDeformer.MStatus) -> MFnBlendShapeDeformer.MFnBlendShapeDeformer

        Synopsis
        -----
        Gets the origin space. It defines the point around which the
        differences in the geometry are calculated.

        Returns: 
        ----- 
        The origin space

        Parameters:
        -----
        ReturnStatus: MFnBlendShapeDeformer.MStatus
        	[out] -> return status


        '''
        pass

    def setOrigin(self, space: MFnBlendShapeDeformer.Origin): 
        '''
        setOrigin(self, space: MFnBlendShapeDeformer.Origin)

        Synopsis
        -----
        Sets the origin space. It defines the point around which the
        differences in the geometry are calculated.

        Returns:
        -----
        None

        Parameters:
        -----
        space: MFnBlendShapeDeformer.Origin
        	[in] -> origin space


        '''
        pass

    def historyLocation(self, ReturnStatus: MFnBlendShapeDeformer.MStatus): 
        '''
        historyLocation(self, ReturnStatus: MFnBlendShapeDeformer.MStatus) -> MFnBlendShapeDeformer.MFnBlendShapeDeformer

        Synopsis
        -----
        Gets the history location (deformation order). It defines where
        to place the deformer node in the chain.

        Returns: 
        ----- 
        The history location (deformation order)

        Parameters:
        -----
        ReturnStatus: MFnBlendShapeDeformer.MStatus
        	[out] -> return status


        '''
        pass

class Origin:
    '''Specifies the space to use for the deformation origin. 
    Non-functional class.  Values for this enum:
    kLocalOrigin
    kWorldOrigin
    '''

    def __init__(self):
        pass

    def kLocalOrigin(self):
        '''This is an enum of Origin.
        - Description:  
        - Value: 0
        '''
        pass

    def kWorldOrigin(self):
        '''This is an enum of Origin.
        - Description:  
        - Value: 1
        '''
        pass

class HistoryLocation:
    '''Specifies where in the shape's history to place the deformer (deformation order). 
    Non-functional class.  Values for this enum:
    kFrontOfChain
    kNormal
    kPost
    kOther
    '''

    def __init__(self):
        pass

    def kFrontOfChain(self):
        '''This is an enum of HistoryLocation.
        - Description: Pre-Defromation. 
        - Value: 0
        '''
        pass

    def kNormal(self):
        '''This is an enum of HistoryLocation.
        - Description: Automatic deformation order. 
        - Value: 1
        '''
        pass

    def kPost(self):
        '''This is an enum of HistoryLocation.
        - Description: Post-Deformation. 
        - Value: 2
        '''
        pass

    def kOther(self):
        '''This is an enum of HistoryLocation.
        - Description: Other deformation order. 
        - Value: 3
        '''
        pass

class TargetType:
    '''TODO. 
    Non-functional class.  Values for this enum:
    kObject
    kTangent
    '''

    def __init__(self):
        pass

    def kObject(self):
        '''This is an enum of TargetType.
        - Description:  
        - Value: 0
        '''
        pass

    def kTangent(self):
        '''This is an enum of TargetType.
        - Description:  
        - Value: 1
        '''
        pass

class MFnCharacter:
    '''Function Set for Characters.
Maya offers "character" nodes to simplify the setting of
keyframes on collections of attributes. The implementation of the
"character" is a sub-class of
MFnSet taking advantage of the fact that attributes can be represented
as MObjects and can be made members of a set. The fact that sets
also derive from
MObject means that characters may have other character sets as members
thus establishing a hierarchy. Only attributes and characters can
be members of a character set. The character node will disallow
the addition of other objects to its set.
Character sets are also part of a partition, meaning that
membership of character sets cannot overlap with other character
sets. Thus, when an attribute already in a character is added to
another character it must be removed from the original character.
Characters are integral to Maya's nonlinear animation system,
"Trax". Trax allows the user to create "animation clips", which
bundle a set of animation curves so that they can be reused
multiple times, with different timing then the original clip.
When a clip is created, Maya finds the the animation curves that
are attached to the attributes in the character set and moves
those animation curves into the newly created clip. The
MFnClip function set is the Maya function set for clips.
Clips in maya can be of two types: source clips and scheduled
clips. In the Maya UI, source clips are visible in the Visor
while scheduled clips are visible in Trax. A source clip contains
the animation curves for the clip. An scheduled clip contains
data about the placement of an instance of a source clip in the
Maya timeline. In this context, an "instance" means that the
animation curves from the source clip are shared by the scheduled
clip. Scheduled clips never contain their own animation curves,
they always refer to a source clip's curves.
For example, if you create a clip called "run" in maya that lasts
from frames 1-20, a source clip node will be created with a start
of 1, a duration of 19, and dependency graph connections to all
of the animation curves that make up the "run". If you then place
an instance of the run clip at frame 5 and another instance of
the run clip at frame 20, you have 2 scheduled clips: one with a
start frame of 5 and one with a start frame of 20. As mentioned
in the previous paragraph, only a single set of animation curves
exist for the run regardless of the number of times the run is
scheduled.
Trax also allows you to create "blends" between clips, which
enable you to control the transition between the clips. A blend
is represented in the dependency graph by an "animBlendInOut"
node, which uses an animation curve to determine the transition
type.
In the dependency graph, when a character has animation clips,
the character node will always be connected to a "clipLibrary"
node and a "clipScheduler" node. The clipLibrary node is
connected to all of the source clips and their animation curves.
The clipScheduler node is connected to the scheduled clips and
blends. It is the clipScheduler that computes the final animation
by looking at the placement and overlap of the clips and feeding
the attribute data back into the character set.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kCharacter.Reimplemented from MFnSet.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> MFnCharacter.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnCharacter".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def attachSourceToCharacter(self, sourceClip: MObject,
                        dgMod: MDGModifier): 
        '''
        attachSourceToCharacter(self, sourceClip: MObject,
                        dgMod: MDGModifier)

        Synopsis
        -----
        Attaches a given source clip node (created using
        MFnClip::createSourceClip) to the character's clipLibrary.
        Attaches a clipLibrary and clipScheduler to the character if they
        are not attached already.

        Returns:
        -----
        None

        Parameters:
        -----
        sourceClip: MObject
        	[in] -> source clip to be attached 

        dgMod: MDGModifier
        	[in] -> command modifier used for undo and redo


        '''
        pass

    def attachInstanceToCharacter(self, instanceClip: MObject,
                        dgMod: MDGModifier): 
        '''
        attachInstanceToCharacter(self, instanceClip: MObject,
                        dgMod: MDGModifier)

        Synopsis
        -----
        Attaches an instance of a clip to the character. If the source
        clip related to the clip instance is not already attached to the
        character, it will be attached as well.This command will fail if
        the instanced clip passed in is not associated with a source
        clip. The best way to associate an instanced clip with a source
        clip is to create the instanced clip using
        MFnClip::createInstancedClip.

        Returns:
        -----
        None

        Parameters:
        -----
        instanceClip: MObject
        	[in] -> the animClip node representing the clipInstance 

        dgMod: MDGModifier
        	[in] -> command modifier used for undo and redo


        '''
        pass

    def addCurveToClip(self, curve: MObject,
                        sourceClip: MObject,
                        plug: MPlug,
                        dgMod: MDGModifier): 
        '''
        addCurveToClip(self, curve: MObject,
                        sourceClip: MObject,
                        plug: MPlug,
                        dgMod: MDGModifier)

        Synopsis
        -----
        Adds an animation curve to a clip. The user must provide the
        animation curve, and the related source clip node (typically
        created using MFnCharacter::createSourceClip). The user must also
        specify the plug that the clip will drive. The plug must be a
        member of the character managed by this MFnCharacter.

        Returns:
        -----
        None

        Parameters:
        -----
        curve: MObject
        	[in] -> the animation curve to be added to the clip 

        sourceClip: MObject
        	[in] -> a source clip specifying the start and duratiohn of the clip 

        plug: MPlug
        	[in] -> plug that this animCurve will drive 

        dgMod: MDGModifier
        	[in] -> command modifier used for undo and redo


        '''
        pass

    def createBlend(self, instancedClip1: MObject,
                        instancedClip2: MObject,
                        blendAnimCurve: MObject,
                        dgMod: MDGModifier,
                        ReturnStatus: MFnCharacter.MStatus): 
        '''
        createBlend(self, instancedClip1: MObject,
                        instancedClip2: MObject,
                        blendAnimCurve: MObject,
                        dgMod: MDGModifier,
                        ReturnStatus: MFnCharacter.MStatus) -> MObject

        Synopsis
        -----
        Creates a blend between two instanced clips on the character. The
        blend is defined by a specified paramCurve, which should be keyed
        between times of 0 and 1. Time 0 corresponds to the start time of
        the blend. Time 1 corresponds to the end time of the blend. The
        blend will be performed on the clips according to the keyed value
        of the blend curve, using the equation: (value)*clip1 +
        (1-value)*clip2. For example, let's say the blend curve goes from
        a value of (0,0) to (1,1). At the start of the blend you will
        have 100% of clip1, and 0% of clip2. At the end of the blend you
        will have 0% of clip1, and 100% of clip2.

        Returns: 
        ----- 
        The resulting animBlend node

        Parameters:
        -----
        instancedClip1: MObject
        	[in] -> clip to be blended 

        instancedClip2: MObject
        	[in] -> another clip to be blended 

        blendAnimCurve: MObject
        	[in] -> animCurve defining the type of the blend 

        dgMod: MDGModifier
        	[in] -> command modifier used for undo and redo 

        ReturnStatus: MFnCharacter.MStatus
        	[out] -> return status


        '''
        pass

    def blendExists(self, instancedClip1: MObject,
                        instancedClip2: MObject,
                        blendResult: MObject): 
        '''
        blendExists(self, instancedClip1: MObject,
                        instancedClip2: MObject,
                        blendResult: MObject) -> bool

        Synopsis
        -----
        Return true if a blend exists between the two instanced clips on
        the character. If a blend exists, the animBlend node related to
        the blend is also returned.

        Returns: 
        ----- 
        true, if a blend was found between the two clips

        Parameters:
        -----
        instancedClip1: MObject
        	[in] -> clip 

        instancedClip2: MObject
        	[in] -> another clip 

        blendResult: MObject
        	[in] -> the blend, if a blend is found


        '''
        pass

    def removeBlend(self, instancedClip1: MObject,
                        instancedClip2: MObject,
                        dgMod: MDGModifier,
                        ReturnStatus: MFnCharacter.MStatus): 
        '''
        removeBlend(self, instancedClip1: MObject,
                        instancedClip2: MObject,
                        dgMod: MDGModifier,
                        ReturnStatus: MFnCharacter.MStatus) -> bool

        Synopsis
        -----
        Remove the blend between the two instanced clips on the
        character. If a blend exists and was deleted, returns true. If a
        blend did not exist, returns false.

        Returns: 
        ----- 
        true, if a blend was found and deleted

        Parameters:
        -----
        instancedClip1: MObject
        	[in] -> clip 

        instancedClip2: MObject
        	[in] -> another clip 

        dgMod: MDGModifier
        	[in] -> command modifier used for undo and redo 

        ReturnStatus: MFnCharacter.MStatus
        	[out] -> the return status


        '''
        pass

    def getCharacterThatOwnsPlug(self, plug: MPlug,
                        result: MObject): 
        '''
        getCharacterThatOwnsPlug(self, plug: MPlug,
                        result: MObject) -> bool

        Synopsis
        -----
        Given a plug, test the plug to see if it is owned by a character.
        If a character controls this plug, the character will be returned

        Returns: 
        ----- 
        true, if the plug is in a character

        Parameters:
        -----
        plug: MPlug
        	[in] -> MPlug

        result: MObject
        	[in] -> Mobject containing a character if the plug is in a character, else an empty 


        '''
        pass

    def getMemberPlugs(self, result: MPlugArray): 
        '''
        getMemberPlugs(self, result: MPlugArray)

        Synopsis
        -----
        Get the members of the character set that are attributes. Return
        them as a plug array. A character set can contain only attributes
        and subcharacters. To get all of the members of the character,
        use MFnSet::getMembers. To get the subcharacters, use
        MFnCharacter::getSubcharacters.

        Returns:
        -----
        None

        Parameters:
        -----
        result: MPlugArray
        	[out] -> storage for the returned list of members


        '''
        pass

    def getSubCharacters(self, result: MSelectionList): 
        '''
        getSubCharacters(self, result: MSelectionList)

        Synopsis
        -----
        Get a list of the subcharacters that are members of the character
        set.

        Returns:
        -----
        None

        Parameters:
        -----
        result: MSelectionList
        	[out] -> storage for the returned list of members


        '''
        pass

    def getClipScheduler(self, ReturnStatus: MFnCharacter.MStatus): 
        '''
        getClipScheduler(self, ReturnStatus: MFnCharacter.MStatus) -> MObject

        Synopsis
        -----
        Get the clipScheduler node that manages the playback of clips on
        this character. If no clips have been created for this character,
        this method will return an empty MObject.

        Returns: 
        ----- 
        MObject containing a clipScheduler node

        Parameters:
        -----
        ReturnStatus: MFnCharacter.MStatus
        	[out] -> return status


        '''
        pass

    def getScheduledClipCount(self, ReturnStatus: MFnCharacter.MStatus): 
        '''
        getScheduledClipCount(self, ReturnStatus: MFnCharacter.MStatus) -> int

        Synopsis
        -----
        Return the number of clips that have been scheduled on this
        character.

        Returns: 
        ----- 
        Number of clips scheduled on this character

        Parameters:
        -----
        ReturnStatus: MFnCharacter.MStatus
        	[out] -> return status


        '''
        pass

    def getScheduledClip(self, index: int,
                        ReturnStatus: MFnCharacter.MStatus): 
        '''
        getScheduledClip(self, index: int,
                        ReturnStatus: MFnCharacter.MStatus) -> MObject

        Synopsis
        -----
        Return the scheduled animClip node corresponding to the specified
        index. The specified index should range from 0 to clipCount-1
        where clipCount is the value returned by
        MFnCharacter::getScheduledClipCount.

        Returns: 
        ----- 
        MObject containing an animClip node

        Parameters:
        -----
        index: int
        	[in] -> Clip index. 

        ReturnStatus: MFnCharacter.MStatus
        	[out] -> return status


        '''
        pass

    def getSourceClipCount(self, ReturnStatus: MFnCharacter.MStatus): 
        '''
        getSourceClipCount(self, ReturnStatus: MFnCharacter.MStatus) -> int

        Synopsis
        -----
        Return the number of source clips managed by the clipLibrary node
        of this character. For more information on source clips, refer to
        the description of the MFnCharacter node.

        Returns: 
        ----- 
        Number of source clips owned by the library on this character

        Parameters:
        -----
        ReturnStatus: MFnCharacter.MStatus
        	[out] -> return status


        '''
        pass

    def getSourceClip(self, index: int,
                        ReturnStatus: MFnCharacter.MStatus): 
        '''
        getSourceClip(self, index: int,
                        ReturnStatus: MFnCharacter.MStatus) -> MObject

        Synopsis
        -----
        Return the animClip node corresponding to the specified index.
        The animClip node will be a source clip node. The specified index
        should range from 0 to clipCount-1 where clipCount is the value
        returned by MFnCharacter::getSourceClipCount.

        Returns: 
        ----- 
        MObject containing an animClip node

        Parameters:
        -----
        index: int
        	[in] -> Clip index. 

        ReturnStatus: MFnCharacter.MStatus
        	[out] -> Return status.


        '''
        pass

    def getBlendCount(self, ReturnStatus: MFnCharacter.MStatus): 
        '''
        getBlendCount(self, ReturnStatus: MFnCharacter.MStatus) -> int

        Synopsis
        -----
        Return the number of blends that have been added to clips on this
        character.

        Returns: 
        ----- 
        Number of blends on clips in this character

        Parameters:
        -----
        ReturnStatus: MFnCharacter.MStatus
        	[out] -> return status


        '''
        pass

    def getBlend(self, index: int,
                        ReturnStatus: MFnCharacter.MStatus): 
        '''
        getBlend(self, index: int,
                        ReturnStatus: MFnCharacter.MStatus) -> MObject

        Synopsis
        -----
        Return the animBlendInOut node corresponding to the specified
        index.

        Returns: 
        ----- 
        MObject containing an animBlendInOut node

        Parameters:
        -----
        index: int
        	[in] -> Index of the desired node. 

        ReturnStatus: MFnCharacter.MStatus
        	[out] -> return status


        '''
        pass

    def getBlendClips(self, index: int,
                        clip1: MObject,
                        clip2: MObject): 
        '''
        getBlendClips(self, index: int,
                        clip1: MObject,
                        clip2: MObject)

        Synopsis
        -----
        Returns the clip nodes that are blended by the blend node
        corresponding to the specified index.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> the index of the blend 

        clip1: MObject
        	[out] -> the first of the clips being blended 

        clip2: MObject
        	[out] -> the second of the clips being blended


        '''
        pass

class MFnClip:
    '''clip function set
Maya uses animation clips as the building block of its nonlinear
animation system, "Trax". An animation clip allows the user to
bundle a set of animation curves independent of time so that they
can be reused multiple times, with different timing then the
original clip.
Character sets (
MFnCharacter) are integral to Maya's clip architecture, since a clip contains
whatever attributes of the character were animated when the clip
was created. For more information on character sets, refer to the
MFnCharacter documentation.
Clips in maya can be of two types: source clips and scheduled
clips. In the Maya UI, source clips are visible in the Visor
while scheduled clips are visible in Trax. A source clip contains
the animation curves for the clip. A scheduled clip contains data
about the placement of an instance of a source clip in the Maya
timeline. In this context, an "instance" means that the animation
curves from the source clip are shared by the scheduled clip.
Scheduled clips never contain their own animation curves, they
always refer to a source clip's curves.
For example, if you create a clip called "run" in maya that lasts
from frames 1-20, a source clip node will be created with a start
of 1, a duration of 19, and dependency graph connections to all
of the animation curves that make up the "run". If you then place
an instance of the run clip at frame 5 and another instance of
the run clip at frame 20, you have 2 scheduled clips: one with a
start frame of 5 and one with a start frame of 20. As mentioned
in the previous paragraph, only a single set of animation curves
exist for the run regardless of the number of times the run is
scheduled.
Trax also allows you to create "blends" between clips, which
enable you to control the transition between the clips. A blend
is represented in the dependency graph by an "animBlendInOut"
node, which uses an animation curve to determine the transition
type.
In the dependency graph, when a character has animation clips,
the character node will always be connected to a "clipLibrary"
node and a "clipScheduler" node. The clipLibrary node is
connected to all of the source clips and their animation curves.
The clipScheduler node is connected to the scheduled clips and
blends. It is the clipScheduler that computes the final animation
by looking at the placement and overlap of the clips and feeding
the attribute data back into the character set.
To create a source clip, the typical steps are:
To create a scheduled clip so that it appears in the Trax Editor,
the typical steps are:
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kClip.Reimplemented from MFnDependencyNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> MFnClip.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnClip".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def createSourceClip(self, sourceStart: MTime,
                        sourceDuration: MTime,
                        dgMod: MDGModifier,
                        ReturnStatus: MFnClip.MStatus): 
        '''
        createSourceClip(self, sourceStart: MTime,
                        sourceDuration: MTime,
                        dgMod: MDGModifier,
                        ReturnStatus: MFnClip.MStatus) -> MObject

        Synopsis
        -----
        Creates a source clip node and associates it with this function
        set. Each animation clip has a single source clip, which defines
        the startFrame and duration of the clip's animation curves. The
        startFrame and duration act as a window onto the animation
        curves, defining the range of animation that is considered part
        of the clip. After a source clip node is created, it can be
        passed to a MFnCharacter along with the clip animCurves in order
        to associate the clip with the character.

        Returns: 
        ----- 
        The newly created clip.

        Parameters:
        -----
        sourceStart: MTime
        	[in] -> time on clip animCurves that represents clip start 

        sourceDuration: MTime
        	[in] -> time extent of the clip 

        dgMod: MDGModifier
        	[in] -> command modifier used for undo and redo 

        ReturnStatus: MFnClip.MStatus
        	[out] -> return status


        '''
        pass

    def createInstancedClip(self, sourceClip: MObject,
                        start: MTime,
                        dgMod: MDGModifier,
                        ReturnStatus: MFnClip.MStatus,
                        absolute: bool,
                        postCycle: double,
                        weight: double,
                        scale: double,
                        preCycle: double): 
        '''
        createInstancedClip(self, sourceClip: MObject,
                        start: MTime,
                        dgMod: MDGModifier,
                        ReturnStatus: MFnClip.MStatus,
                        absolute: bool,
                        postCycle: double,
                        weight: double,
                        scale: double,
                        preCycle: double) -> MObject

        Synopsis
        -----
        Creates an instance of a clip that will be viewable in the Trax
        editor.

        Returns: 
        ----- 
        The newly created clip.

        Parameters:
        -----
        sourceClip: MObject
        	[in] -> the source clip node 

        start: MTime
        	[in] -> start frame where the instance will be scheduled 

        dgMod: MDGModifier
        	[in] -> command modifier used for undo and redo 

        ReturnStatus: MFnClip.MStatus
        	[in] -> return status 

        absolute: bool
        	[in] -> whether the clip is absolute (1) or relative (0) 

        postCycle: double
        	[in] -> post cycle for the clip 

        weight: double
        	[in] -> weight for the clip 

        scale: double
        	[in] -> scale for the clip

        preCycle: double
        	[in] -> pre cycle for the clip 


        '''
        pass

    def isInstancedClip(self, ReturnStatus: MFnClip.MStatus): 
        '''
        isInstancedClip(self, ReturnStatus: MFnClip.MStatus) -> bool

        Synopsis
        -----
        Return true or false as to whether the clip node represents the
        source clip or an instanced clip. All clips maintained by the
        clipScheduler node and visible in the TraX editor are instanced
        clips. All clips maintained by the clipLibrary node and visible
        in the Visor are non-instanced clips, also called "Source Clips".
        Each instanced clip has a corresponding source clip.

        Returns: 
        ----- 
        True or false as to whether the clip is an instanced clip.

        Parameters:
        -----
        ReturnStatus: MFnClip.MStatus
        	[out] -> return status


        '''
        pass

    def isPose(self, ReturnStatus: MFnClip.MStatus): 
        '''
        isPose(self, ReturnStatus: MFnClip.MStatus) -> bool

        Synopsis
        -----
        Return true or false as to whether the clip node represents a
        pose.

        Returns: 
        ----- 
        True or false as to whether the clip is a pose.

        Parameters:
        -----
        ReturnStatus: MFnClip.MStatus
        	[out] -> return status


        '''
        pass

    def sourceClip(self, ReturnStatus: MFnClip.MStatus): 
        '''
        sourceClip(self, ReturnStatus: MFnClip.MStatus) -> MObject

        Synopsis
        -----
        Return the source clip associated with the MFnClip's clip.

        Returns: 
        ----- 
        MObject containing the associated source clip.

        Parameters:
        -----
        ReturnStatus: MFnClip.MStatus
        	[out] -> return status


        '''
        pass

    def getPreCycle(self, ReturnStatus: MFnClip.MStatus): 
        '''
        getPreCycle(self, ReturnStatus: MFnClip.MStatus) -> double

        Synopsis
        -----
        Return the value of this clip's pre cycle attribute.

        Returns: 
        ----- 
        The value of this clip's pre cycle attribute.

        Parameters:
        -----
        ReturnStatus: MFnClip.MStatus
        	[out] -> return status


        '''
        pass

    def getPostCycle(self, ReturnStatus: MFnClip.MStatus): 
        '''
        getPostCycle(self, ReturnStatus: MFnClip.MStatus) -> double

        Synopsis
        -----
        Return the value of this clip's post cycle attribute.

        Returns: 
        ----- 
        The value of this clip's post cycle attribute.

        Parameters:
        -----
        ReturnStatus: MFnClip.MStatus
        	[out] -> return status


        '''
        pass

    def getWeight(self, ReturnStatus: MFnClip.MStatus): 
        '''
        getWeight(self, ReturnStatus: MFnClip.MStatus) -> double

        Synopsis
        -----
        Return the value of this clip's weight attribute.

        Returns: 
        ----- 
        The value of this clip's weight attribute.

        Parameters:
        -----
        ReturnStatus: MFnClip.MStatus
        	[out] -> return status


        '''
        pass

    def getScale(self, ReturnStatus: MFnClip.MStatus): 
        '''
        getScale(self, ReturnStatus: MFnClip.MStatus) -> double

        Synopsis
        -----
        Return the value of this clip's scale attribute.

        Returns: 
        ----- 
        The value of this clip's scale attribute.

        Parameters:
        -----
        ReturnStatus: MFnClip.MStatus
        	[out] -> return status


        '''
        pass

    def getEnabled(self, ReturnStatus: MFnClip.MStatus): 
        '''
        getEnabled(self, ReturnStatus: MFnClip.MStatus) -> bool

        Synopsis
        -----
        Return the value of this clip's enable attribute.

        Returns: 
        ----- 
        The value of this clip's enable attribute.

        Parameters:
        -----
        ReturnStatus: MFnClip.MStatus
        	[out] -> return status


        '''
        pass

    def getStartFrame(self, ReturnStatus: MFnClip.MStatus): 
        '''
        getStartFrame(self, ReturnStatus: MFnClip.MStatus) -> MTime

        Synopsis
        -----
        Return the value of this clip's start frame.

        Returns: 
        ----- 
        The value of this clip's start frame.

        Parameters:
        -----
        ReturnStatus: MFnClip.MStatus
        	[out] -> return status


        '''
        pass

    def getSourceStart(self, ReturnStatus: MFnClip.MStatus): 
        '''
        getSourceStart(self, ReturnStatus: MFnClip.MStatus) -> MTime

        Synopsis
        -----
        Return the value of the start frame of this clip's source clip.
        The sourceStart and sourceDuration define the region of the
        animCurve that is treated as the clip.

        Returns: 
        ----- 
        The value of this clip's source start frame.

        Parameters:
        -----
        ReturnStatus: MFnClip.MStatus
        	[out] -> return status


        '''
        pass

    def getSourceDuration(self, ReturnStatus: MFnClip.MStatus): 
        '''
        getSourceDuration(self, ReturnStatus: MFnClip.MStatus) -> MTime

        Synopsis
        -----
        Return the value of the start frame of this clip's source
        duration. The sourceStart and sourceDuration define the region of
        the animCurve that is treated as the clip.

        Returns: 
        ----- 
        The value of this clip's source duration.

        Parameters:
        -----
        ReturnStatus: MFnClip.MStatus
        	[out] -> return status


        '''
        pass

    def getMemberAnimCurves(self, curves: MObjectArray,
                        associatedAttrs: MPlugArray): 
        '''
        getMemberAnimCurves(self, curves: MObjectArray,
                        associatedAttrs: MPlugArray)

        Synopsis
        -----
        Return two arrays: the first contains the animCurves associated
        with this clip. The second contains the character member that is
        driven by this animCurve.

        Returns:
        -----
        None

        Parameters:
        -----
        curves: MObjectArray
        	[out] -> array to store the result curves 

        associatedAttrs: MPlugArray
        	[out] -> array to store the character members


        '''
        pass

    def getAbsoluteChannelSettings(self, absoluteChannels: MIntArray): 
        '''
        getAbsoluteChannelSettings(self, absoluteChannels: MIntArray)

        Synopsis
        -----
        Return an array indicating which channels of the clip are
        absolute and which are relative. The length of the array is equal
        to the members in the character. A value of one in the array
        indicates absolute and a value of 0 indicates relative.

        Returns:
        -----
        None

        Parameters:
        -----
        absoluteChannels: MIntArray
        	[out] -> array to store the result


        '''
        pass

    def getTrack(self, ReturnStatus: MFnClip.MStatus): 
        '''
        getTrack(self, ReturnStatus: MFnClip.MStatus) -> int

        Synopsis
        -----
        Return the track number for the clip. Track indices are one-
        based. If a track index of zero is returned, it indicates that a
        track has not yet been assigned to the clip.

        Returns: 
        ----- 
        The index of this clip's track

        Parameters:
        -----
        ReturnStatus: MFnClip.MStatus
        	[out] -> return status


        '''
        pass

    def setPoseClip(self, state: bool,
                        mod: MDGModifier): 
        '''
        setPoseClip(self, state: bool,
                        mod: MDGModifier)

        Synopsis
        -----
        Specify whether or not this clip node should be tagged as a pose
        rather than a clip. By default, clip nodes are not poses.

        Returns:
        -----
        None

        Parameters:
        -----
        state: bool
        	[in] -> true, to tag the clip as a pose 

        mod: MDGModifier
        	[in] -> modifier to use when calling this method from commands that support undo


        '''
        pass

    def setPreCycle(self, cycle: double,
                        mod: MDGModifier): 
        '''
        setPreCycle(self, cycle: double,
                        mod: MDGModifier)

        Synopsis
        -----
        Specify the pre cycle value for the clip.

        Returns:
        -----
        None

        Parameters:
        -----
        cycle: double
        	[in] -> cycle value 

        mod: MDGModifier
        	[in] -> modifier to use when calling this method from commands that support undo


        '''
        pass

    def setPostCycle(self, cycle: double,
                        mod: MDGModifier): 
        '''
        setPostCycle(self, cycle: double,
                        mod: MDGModifier)

        Synopsis
        -----
        Specify the post cycle value for the clip.

        Returns:
        -----
        None

        Parameters:
        -----
        cycle: double
        	[in] -> cycle value 

        mod: MDGModifier
        	[in] -> modifier to use when calling this method from commands that support undo


        '''
        pass

    def setWeight(self, wt: double,
                        mod: MDGModifier): 
        '''
        setWeight(self, wt: double,
                        mod: MDGModifier)

        Synopsis
        -----
        Specify a weight value for the clip.

        Returns:
        -----
        None

        Parameters:
        -----
        wt: double
        	[in] -> weight value 

        mod: MDGModifier
        	[in] -> modifier to use when calling this method from commands that support undo


        '''
        pass

    def setScale(self, scale: double,
                        mod: MDGModifier): 
        '''
        setScale(self, scale: double,
                        mod: MDGModifier)

        Synopsis
        -----
        Specify a scale value for the clip.

        Returns:
        -----
        None

        Parameters:
        -----
        scale: double
        	[in] -> scale value 

        mod: MDGModifier
        	[in] -> modifier to use when calling this method from commands that support undo


        '''
        pass

    def setEnabled(self, val: bool,
                        mod: MDGModifier): 
        '''
        setEnabled(self, val: bool,
                        mod: MDGModifier)

        Synopsis
        -----
        Specify whether or not the clip is enabled. Note: should not be
        called for source clips since the enabled attribute is ignored on
        source clips.

        Returns:
        -----
        None

        Parameters:
        -----
        val: bool
        	[in] -> enable value 

        mod: MDGModifier
        	[in] -> modifier to use when calling this method from commands that support undo


        '''
        pass

    def setStartFrame(self, start: MTime,
                        mod: MDGModifier): 
        '''
        setStartFrame(self, start: MTime,
                        mod: MDGModifier)

        Synopsis
        -----
        Specify the start frame for the instanced clip. Note: should not
        be called for source clips since the start frame attribute is
        ignored on source clips.

        Returns:
        -----
        None

        Parameters:
        -----
        start: MTime
        	[in] -> start frame value 

        mod: MDGModifier
        	[in] -> modifier to use when calling this method from commands that support undo


        '''
        pass

    def setSourceData(self, start: MTime,
                        duration: MTime,
                        mod: MDGModifier): 
        '''
        setSourceData(self, start: MTime,
                        duration: MTime,
                        mod: MDGModifier)

        Synopsis
        -----
        Specify the start frame and duration for the source clip
        associated with this clip.

        Returns:
        -----
        None

        Parameters:
        -----
        start: MTime
        	[in] -> source start frame value 

        duration: MTime
        	[in] -> source duration value 

        mod: MDGModifier
        	[in] -> modifier to use when calling this method from commands that support undo


        '''
        pass

    def setTrack(self, trackIndex: int,
                        mod: MDGModifier): 
        '''
        setTrack(self, trackIndex: int,
                        mod: MDGModifier)

        Synopsis
        -----
        Specify the one-based track number for the clip.

        Returns:
        -----
        None

        Parameters:
        -----
        trackIndex: int
        	[in] -> the track number for the clip 

        mod: MDGModifier
        	[in] -> modifier to use when calling this method from commands that support undo


        '''
        pass

    def setAbsoluteChannelSettings(self, absoluteChannels: MIntArray,
                        mod: MDGModifier): 
        '''
        setAbsoluteChannelSettings(self, absoluteChannels: MIntArray,
                        mod: MDGModifier)

        Synopsis
        -----
        Set which channels of the clip are absolute and which are
        relative. The length of the specified array should be equal to
        the number of members in the character. A value of one in the
        array indicates absolute and a value of 0 indicates relative.

        Returns:
        -----
        None

        Parameters:
        -----
        absoluteChannels: MIntArray
        	[in] -> array containing the absolute channels to be set 

        mod: MDGModifier
        	[in] -> modifier to use when calling this method from commands that support undo


        '''
        pass

class MFnGeometryFilter:
    '''geometry filter function set
MFnGeometryFilter is the function set for geometry filters, the node that is the
base class for deformers. Geometry filter nodes include clusters,
ffds, nonlinears, user-defined deformers, sculpts, wires and
blendShapes. The purpose of the geometry filter is to connect to
the geometry that is deformed. The geometry filter is independent
of any algorithm that calculates the deformation.
This function set provides methods for finding out which
geometries are connected to geometry filter nodes.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kGeometryFilt.Reimplemented from
        MFnDependencyNode.Reimplemented in MFnWeightGeometryFilter, and
        MFnSkinCluster.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> staticchar*

        Synopsis
        -----
        Returns the name of this class.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getInputGeometry(self, geomList: MObjectArray): 
        '''
        getInputGeometry(self, geomList: MObjectArray)

        Synopsis
        -----
        This method returns the input geometry for the deformer by
        traversing the graph to find upstream shape nodes. It is possible
        for there to be nodes in between the shape and the deformer so
        that the returned shape may have a different topology or tweaks
        then the input data to the deformer. If the actual input geometry
        data for the deformer is required, this information can be
        accessed by using MPlug::getValue() to query the inputGeometry
        attribute on the deformer.The input geometry is packed into the
        provided list of MObjects. Each of the MObjects will be a DAG
        node.

        Returns:
        -----
        None

        Parameters:
        -----
        geomList: MObjectArray
        	[out] -> storage for the returned array


        '''
        pass

    def getOutputGeometry(self, geomList: MObjectArray): 
        '''
        getOutputGeometry(self, geomList: MObjectArray)

        Synopsis
        -----
        The output geometry is packed into the provided list of MObjects.
        Each of the MObjects will be a DAG node.

        Returns:
        -----
        None

        Parameters:
        -----
        geomList: MObjectArray
        	[out] -> storage for the returned array


        '''
        pass

    def inputShapeAtIndex(self, index: int,
                        ReturnStatus: MFnGeometryFilter.MStatus): 
        '''
        inputShapeAtIndex(self, index: int,
                        ReturnStatus: MFnGeometryFilter.MStatus) -> MObject

        Synopsis
        -----
        Returns the input shape corresponding to the plug index.

        Returns: 
        ----- 
        The input shape corresponding to the plug index

        Parameters:
        -----
        index: int
        	[in] -> the plug index for the input shape 

        ReturnStatus: MFnGeometryFilter.MStatus
        	[out] -> return status


        '''
        pass

    def outputShapeAtIndex(self, index: int,
                        ReturnStatus: MFnGeometryFilter.MStatus): 
        '''
        outputShapeAtIndex(self, index: int,
                        ReturnStatus: MFnGeometryFilter.MStatus) -> MObject

        Synopsis
        -----
        Returns the output shape corresponding to the plug index.

        Returns: 
        ----- 
        The output shape corresponding to the plug index

        Parameters:
        -----
        index: int
        	[in] -> the plug index for the output shape 

        ReturnStatus: MFnGeometryFilter.MStatus
        	[out] -> return status


        '''
        pass

    def indexForOutputShape(self, shape: MObject,
                        ReturnStatus: MFnGeometryFilter.MStatus): 
        '''
        indexForOutputShape(self, shape: MObject,
                        ReturnStatus: MFnGeometryFilter.MStatus) -> int

        Synopsis
        -----
        Returns the plug index for the specified output shape.

        Returns: 
        ----- 
        The plug index leading to the specified shape

        Parameters:
        -----
        shape: MObject
        	[in] -> the shape for which the plug index is requested 

        ReturnStatus: MFnGeometryFilter.MStatus
        	[out] -> return status


        '''
        pass

    def getPathAtIndex(self, index: int,
                        dagPath: MDagPath): 
        '''
        getPathAtIndex(self, index: int,
                        dagPath: MDagPath)

        Synopsis
        -----
        The DAG path of the output geometry at the specified plug index
        is put in the dagPath argument.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> the plug index 

        dagPath: MDagPath
        	[out] -> the DAG path whose index is requested


        '''
        pass

    def indexForGroupId(self, groupId: int,
                        ReturnStatus: MFnGeometryFilter.MStatus): 
        '''
        indexForGroupId(self, groupId: int,
                        ReturnStatus: MFnGeometryFilter.MStatus) -> int

        Synopsis
        -----
        Returns the plug index corresponding to the groupId. This ID can
        change from one Maya session to another, but it is unique for
        each Maya session.

        Returns: 
        ----- 
        The plug index corresponding to the groupId

        Parameters:
        -----
        groupId: int
        	[in] -> the groupId for the plug index 

        ReturnStatus: MFnGeometryFilter.MStatus
        	[out] -> return status


        '''
        pass

    def groupIdAtIndex(self, index: int,
                        ReturnStatus: MFnGeometryFilter.MStatus): 
        '''
        groupIdAtIndex(self, index: int,
                        ReturnStatus: MFnGeometryFilter.MStatus) -> int

        Synopsis
        -----
        Returns the groupId at the specified plug index.

        Returns: 
        ----- 
        The groupId at the specified index

        Parameters:
        -----
        index: int
        	[in] -> the plug index for which the groupId is requested 

        ReturnStatus: MFnGeometryFilter.MStatus
        	[out] -> return status


        '''
        pass

    def numOutputConnections(self, ReturnStatus: MFnGeometryFilter.MStatus): 
        '''
        numOutputConnections(self, ReturnStatus: MFnGeometryFilter.MStatus) -> int

        Synopsis
        -----
        Returns the number of output geometries connected to this node.
        This is typically equal to the number of input geometries unless
        an input or output geometry has been deleted, or a connection to
        an input or output geometry has been broken.This method is useful
        in conjunction with indexForOutputConnection to iterate through
        the affected objects.For example:

        Returns: 
        ----- 
        The number of outputs

        Parameters:
        -----
        ReturnStatus: MFnGeometryFilter.MStatus
        	[out] -> return status


        '''
        pass

    def indexForOutputConnection(self, connectionIndex: int,
                        ReturnStatus: MFnGeometryFilter.MStatus): 
        '''
        indexForOutputConnection(self, connectionIndex: int,
                        ReturnStatus: MFnGeometryFilter.MStatus) -> int

        Synopsis
        -----
        Returns the plug index corresponding to the connection index. The
        connection index is the index specifying the nth output
        connection. The plug index (logical index) is the sparse array
        index used by many of MFnGeometryFilter's methods and in MEL
        scripts. The connection index is 0-based, hence, the maximum
        value of the connection index is numOutputs - 1.

        Returns: 
        ----- 
        The plug index corresponding to the connection index

        Parameters:
        -----
        connectionIndex: int
        	[in] -> the connection index 

        ReturnStatus: MFnGeometryFilter.MStatus
        	[out] -> return status


        '''
        pass

    def deformerSet(self, ReturnStatus: MFnGeometryFilter.MStatus): 
        '''
        deformerSet(self, ReturnStatus: MFnGeometryFilter.MStatus) -> MObject

        Synopsis
        -----
        Returns the set containing the objects that are deformed. Adding
        new components to the deformer set will cause them to be
        deformed. Removing components from the deformer set will prevent
        them from being influenced by the deformer.Note that the wrap
        deformer and the skinCluster deformers are special cases. They
        allow only a single object to be deformed per wrap/skinCluster,
        so adding additional geometries to a wrap or skinCluster node
        will have no effect.

        Returns: 
        ----- 
        The set containing the objects that are deformed

        Parameters:
        -----
        ReturnStatus: MFnGeometryFilter.MStatus
        	[out] -> return status


        '''
        pass

    def envelope(self, ReturnStatus: MFnGeometryFilter.MStatus): 
        '''
        envelope(self, ReturnStatus: MFnGeometryFilter.MStatus) -> float

        Synopsis
        -----
        Returns the envelope value. The envelope is a global scale factor
        that is applied to all the values.

        Returns: 
        ----- 
        The envelope value

        Parameters:
        -----
        ReturnStatus: MFnGeometryFilter.MStatus
        	[out] -> return status


        '''
        pass

    def setEnvelope(self, envelope: float): 
        '''
        setEnvelope(self, envelope: float)

        Synopsis
        -----
        Sets the envelope value. The envelope is a global scale factor
        that is applied to all the values.

        Returns:
        -----
        None

        Parameters:
        -----
        envelope: float
        	[in] -> envelope value


        '''
        pass

    def getComponentAtIndex(self, index: int,
                        ReturnStatus: MFnGeometryFilter.MStatus): 
        '''
        getComponentAtIndex(self, index: int,
                        ReturnStatus: MFnGeometryFilter.MStatus) -> MObject

        Synopsis
        -----
        Introduced in 2022.0 Get the component used for the ith deformed
        geometry.

        Returns: 
        ----- 
        MObject representing the component, if successfull and returned
        nullObj, it would mean complete component

        Parameters:
        -----
        index: int
        	[in] -> the plug index for which the component is requested 

        ReturnStatus: MFnGeometryFilter.MStatus
        	[out] -> return status


        '''
        pass

    def getIndexMapper(self, index: int,
                        indexMapper: MFnGeometryFilter.MIndexMapper): 
        '''
        getIndexMapper(self, index: int,
                        indexMapper: MFnGeometryFilter.MIndexMapper)

        Synopsis
        -----
        Introduced in 2024.1 This method retrieves the indexMapper of the
        deformer.The indexMapper defines the subset on which the deformer
        operates.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> the plug index for which the component is requested 

        indexMapper: MFnGeometryFilter.MIndexMapper
        	[out] -> storage for the returned array


        '''
        pass

class MFnHikEffector:
    '''Full Body IK end effector function set.
MFnHikEffector is the function set for full body ik effectors. An Full Body IK
(FBIK/HIK) effector is a special transform that allows users to
manipulate a Full Body IK system.
The methods of the parent class
MFnTransform used to position the end effector.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kHikEffector.Reimplemented from MFnTransform.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> MFnHikEffector.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnHikEffector".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def create(self, parent: MObject,
                        ReturnStatus: MFnHikEffector.MStatus): 
        '''
        create(self, parent: MObject,
                        ReturnStatus: MFnHikEffector.MStatus) -> MObject

        Synopsis
        -----
        Creates a new fbik effector.

        Returns: 
        ----- 
        A handle to the new object

        Parameters:
        -----
        parent: MObject
        	[in] -> parent DAG node (usually none) 

        ReturnStatus: MFnHikEffector.MStatus
        	[out] -> return status


        '''
        pass

    def getPivotOffset(self, ReturnStatus: MFnHikEffector.MStatus): 
        '''
        getPivotOffset(self, ReturnStatus: MFnHikEffector.MStatus) -> MVector

        Synopsis
        -----
        Retrieve the pivot offset of this effector.

        Returns: 
        ----- 
        Pivot offset vector.

        Parameters:
        -----
        ReturnStatus: MFnHikEffector.MStatus
        	[out] -> return status


        '''
        pass

    def setPivotOffset(self, vector: MVector): 
        '''
        setPivotOffset(self, vector: MVector)

        Synopsis
        -----
        Set the pivot offset for this effector.

        Returns:
        -----
        None

        Parameters:
        -----
        vector: MVector
        	[in] -> the new pivot offset


        '''
        pass

    def getEffColor(self, ReturnStatus: MFnHikEffector.MStatus): 
        '''
        getEffColor(self, ReturnStatus: MFnHikEffector.MStatus) -> MColor

        Synopsis
        -----
        Retrieve the cached humanIK color of this effector.

        Returns: 
        ----- 
        Pivot offset vector.

        Parameters:
        -----
        ReturnStatus: MFnHikEffector.MStatus
        	[out] -> return status


        '''
        pass

    def setEffColor(self, color: MColor): 
        '''
        setEffColor(self, color: MColor)

        Synopsis
        -----
        Set the humanIK color for this effector.

        Returns:
        -----
        None

        Parameters:
        -----
        color: MColor
        	[in] -> the new color


        '''
        pass

    def getAuxiliaryEffectors(self, effs: MObjectArray): 
        '''
        getAuxiliaryEffectors(self, effs: MObjectArray)

        Synopsis
        -----
        Returns an array of the auxiliary effectors associated with this
        effector. Auxiliary effectors are used by humanIK to act as
        additional pivots.

        Returns:
        -----
        None

        Parameters:
        -----
        effs: MObjectArray
        	[out] -> the auxiliary effectors for this effector


        '''
        pass

class MFnIkEffector:
    '''Inverse kinematics end effector function set.
MFnIkEffector is the function set for inverse kinematic end effectors. An end
effector is a point on the skeleton, usually the last bone. When
an IK system solves, it is trying to calculate the rotations on
the joints necessary to get the end effector to the target point.
The methods of the parent class
MFnTransform used to position the end effector.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kIkEffector.Reimplemented from MFnTransform.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> MFnIkEffector.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnIkEffector".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def create(self, parent: MObject,
                        ReturnStatus: MFnIkEffector.MStatus): 
        '''
        create(self, parent: MObject,
                        ReturnStatus: MFnIkEffector.MStatus) -> MObject

        Synopsis
        -----
        Creates a new end effector. For the effector to work properly, it
        should be given a joint as the parent. It should be given the
        joint before the last bone.

        Returns: 
        ----- 
        A handle to the new object

        Parameters:
        -----
        parent: MObject
        	[in] -> parent DAG node (should be a joint) 

        ReturnStatus: MFnIkEffector.MStatus
        	[out] -> return status


        '''
        pass

class MFnIkHandle:
    '''Function set for inverse kinematics (IK) handles.
This is the function set for inverse kinematics (IK) handles. An
ik handle specifies the joints in a skeleton that are effected by
an attached ik solver.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kIkHandle.Reimplemented from MFnTransform.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> MFnIkHandle.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnIkHandle".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def create(self, startJoint: MDagPath,
                        effector: MDagPath,
                        ReturnStatus: MFnIkHandle.MStatus): 
        '''
        create(self, startJoint: MDagPath,
                        effector: MDagPath,
                        ReturnStatus: MFnIkHandle.MStatus) -> MObject

        Synopsis
        -----
        Creates a new ik handle. The effector and startJoint specify the
        joint chain controlled by this handle. The effector is the joint
        that is moved by the handle forcing the solver to recalculate the
        joint chain.

        Returns:
        -----
        None

        Parameters:
        -----
        startJoint: MDagPath
        	[in] -> a path to the start joint in the joint chain 

        effector: MDagPath
        	[in] -> a path to the end-effector (last joint) in the chain 

        ReturnStatus: MFnIkHandle.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def getStartJoint(self, jointPath: MDagPath): 
        '''
        getStartJoint(self, jointPath: MDagPath)

        Synopsis
        -----
        This method will get a dag path to the starting joint of the
        handle's joint chain.

        Returns:
        -----
        None

        Parameters:
        -----
        jointPath: MDagPath
        	[out] -> storage for the dag path to the joint


        '''
        pass

    def setStartJoint(self, jointPath: MDagPath): 
        '''
        setStartJoint(self, jointPath: MDagPath)

        Synopsis
        -----
        This method will set the dag path for the starting joint of the
        handle's joint chain. The start joint must be on the same
        skeletal chain as the end effector or this method will fail.

        Returns:
        -----
        None

        Parameters:
        -----
        jointPath: MDagPath
        	[in] -> The dag path to the joint that will be set


        '''
        pass

    def getEffector(self, effectorPath: MDagPath): 
        '''
        getEffector(self, effectorPath: MDagPath)

        Synopsis
        -----
        Get a dag path to the end-effector of the handle's joint chain.

        Returns:
        -----
        None

        Parameters:
        -----
        effectorPath: MDagPath
        	[out] -> Storage for the effector path


        '''
        pass

    def setEffector(self, effectorPath: MDagPath): 
        '''
        setEffector(self, effectorPath: MDagPath)

        Synopsis
        -----
        Set the dag path to the end-effector of the handle's joint chain.
        The end-effector/joint must be on the same skeletal chain as the
        start joint or this method will fail.The end effector may be
        specified with a joint or an end-effector. If a joint is used, an
        end-effector will be created at the same position as the joint
        and this new end-effector will be used as the end effector.

        Returns:
        -----
        None

        Parameters:
        -----
        effectorPath: MDagPath
        	[in] -> The path for the effector


        '''
        pass

    def setStartJointAndEffector(self, jointPath: MDagPath,
                        effectorPath: MDagPath): 
        '''
        setStartJointAndEffector(self, jointPath: MDagPath,
                        effectorPath: MDagPath)

        Synopsis
        -----
        This method will set the dag path for the starting joint and the
        end-effector of the handle's joint chain. This method must be
        used when setting the joints for a handle that are in a different
        skeletal chain then the current one.The end effector may be
        specified with a joint or an end-effector. If a joint is used, an
        end-effector will be created at the same position as the joint
        and this new end-effector will be used as the end effector.

        Returns:
        -----
        None

        Parameters:
        -----
        jointPath: MDagPath
        	[in] -> The dag path to the joint that will be set 

        effectorPath: MDagPath
        	[in] -> The path for the effector


        '''
        pass

    def priority(self, ReturnStatus: MFnIkHandle.MStatus): 
        '''
        priority(self, ReturnStatus: MFnIkHandle.MStatus) -> int

        Synopsis
        -----
        Get the priority of this handle in case a solution is affected by
        more than one handle. Logically, all handles with a lower number
        priority are solved before any handles with a higher numbered
        priority. (All handles of priority 1 are solved before any
        handles of priority 2 and so on.) Handle priorities must be > 0.

        Returns: 
        ----- 
        The priority of this handle

        Parameters:
        -----
        ReturnStatus: MFnIkHandle.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def setPriority(self, priority: int): 
        '''
        setPriority(self, priority: int)

        Synopsis
        -----
        Set the priority of this handle in case a solution is affected by
        more than one handle. Logically, all handles with a lower number
        priority are solved before any handles with a higher numbered
        priority. (All handles of priority 1 are solved before any
        handles of priority 2 and so on.) Handle priorities must be > 0.

        Returns:
        -----
        None

        Parameters:
        -----
        priority: int
        	[in] -> The priority to set for this handle


        '''
        pass

    def stickiness(self, ReturnStatus: MFnIkHandle.MStatus): 
        '''
        stickiness(self, ReturnStatus: MFnIkHandle.MStatus) -> MFnIkHandle.MFnIkHandle

        Synopsis
        -----
        Get the stickiness of this handle. Sticky handles are solved when
        the skeleton is being manipulated interactively. If a character
        has sticky feet, the solver will attempt to keep them in the same
        position as the user moves the character's root. If they were not
        sticky, they would move along with the root.

        Returns: 
        ----- 
        The stickiness value for this handle.

        Parameters:
        -----
        ReturnStatus: MFnIkHandle.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def setStickiness(self, stickiness: MFnIkHandle.Stickiness): 
        '''
        setStickiness(self, stickiness: MFnIkHandle.Stickiness)

        Synopsis
        -----
        Set the stickiness of this handle. Sticky handles are solved when
        the skeleton is being manipulated interactively. If a character
        has sticky feet, the solver will attempt to keep them in the same
        position as the user moves the character's root. If they were not
        sticky, they would move along with the root.

        Returns:
        -----
        None

        Parameters:
        -----
        stickiness: MFnIkHandle.Stickiness
        	[in] -> The stickiness value to be set.


        '''
        pass

    def weight(self, ReturnStatus: MFnIkHandle.MStatus): 
        '''
        weight(self, ReturnStatus: MFnIkHandle.MStatus) -> double

        Synopsis
        -----
        Get the handles weight in error calculations. The weight only
        applies when handle goals are in conflict and cannot be solved
        simultaneously. When this happens, a solution is computed that
        weights the "distance" from each goal to the solution by the
        handle's weight and attempts to minimize this value. The weight
        must be >= 0.

        Returns: 
        ----- 
        The weight value for this handle

        Parameters:
        -----
        ReturnStatus: MFnIkHandle.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def setWeight(self, weight: double): 
        '''
        setWeight(self, weight: double)

        Synopsis
        -----
        Specifies the handles weight in error calculations. The weight
        only applies when handle goals are in conflict and cannot be
        solved simultaneously. When this happens, a solution is computed
        that weights the "distance" from each goal to the solution by the
        handle's weight and attempts to minimize this value. The weight
        must be >= 0.

        Returns:
        -----
        None

        Parameters:
        -----
        weight: double
        	[in] -> The weight value to be set


        '''
        pass

    def poWeight(self, ReturnStatus: MFnIkHandle.MStatus): 
        '''
        poWeight(self, ReturnStatus: MFnIkHandle.MStatus) -> double

        Synopsis
        -----
        Gets the position/orientation weight of a handle. This is used to
        compute the "distance" between the goal position and the end-
        effector position.A positionWeight of 1.0 computes the distance
        as the distance between positions only and ignores the
        orientations.A positionWeight of 0.0 computes the distance as the
        distance between the orientations only and ignores the
        positions.A positionWeight of 0.5 attempts to weight the
        distances equally but cannot actually compute this due to units
        differences. Because there is no way to add linear units and
        angular units.

        Returns: 
        ----- 
        The position/orientation weight

        Parameters:
        -----
        ReturnStatus: MFnIkHandle.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def setPOWeight(self, poWeight: double): 
        '''
        setPOWeight(self, poWeight: double)

        Synopsis
        -----
        Sets the position/orientation weight of a handle. This is used to
        compute the "distance" between the goal position and the end-
        effector position.A positionWeight of 1.0 computes the distance
        as the distance between positions only and ignores the
        orientations.A positionWeight of 0.0 computes the distance as the
        distance between the orientations only and ignores the
        positions.A positionWeight of 0.5 attempts to weight the
        distances equally but cannot actually compute this due to units
        differences. Because there is no way to add linear units and
        angular units.

        Returns:
        -----
        None

        Parameters:
        -----
        poWeight: double
        	[in] -> The position/orientation weight to be set


        '''
        pass

    def solver(self, ReturnStatus: MFnIkHandle.MStatus): 
        '''
        solver(self, ReturnStatus: MFnIkHandle.MStatus) -> MObject

        Synopsis
        -----
        Returns the solver attached to this handle.

        Returns: 
        ----- 
        The solver associated with this handle

        Parameters:
        -----
        ReturnStatus: MFnIkHandle.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    @overload
    def setSolver(self, solver: MObject): 
        '''
        setSolver(self, solver: MObject)

        Synopsis
        -----
        Set the solver for this handle.

        Returns:
        -----
        None

        Parameters:
        -----
        solver: MObject
        	[in] -> The solver for this handle


        '''
        pass

    @overload
    def setSolver(self, solverName: MString): 
        '''
        setSolver(self, solverName: MString)

        Synopsis
        -----
        Set the solver associated with this handle by name.

        Returns:
        -----
        None

        Parameters:
        -----
        solverName: MString
        	[in] -> The type name of the solver to be set


        '''
        pass

class Stickiness:
    '''Specifies a handle's stickiness when the skeleton is being manipulated interactively. 
    Non-functional class.  Values for this enum:
    kStickyOff
    kStickyOn
    kSuperSticky
    '''

    def __init__(self):
        pass

    def kStickyOff(self):
        '''This is an enum of Stickiness.
        - Description: Handle will move with skeleton's root. 
        - Value: 0
        '''
        pass

    def kStickyOn(self):
        '''This is an enum of Stickiness.
        - Description: Handle will try to stay where it is. 
        - Value: 1
        '''
        pass

    def kSuperSticky(self):
        '''This is an enum of Stickiness.
        - Description: Not used. 
        - Value: 2
        '''
        pass

class MFnIkJoint:
    '''Function set for joints.
This is the function set for joints.
The transformation matrix for a joint node is below.
(where '*' denotes matrix multiplication).
These matrices are defined as follows:
The methods to get the value of these matrices are:
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kJoint.Reimplemented from MFnTransform.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> MFnIkJoint.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnIkJoint".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def create(self, parent: MObject,
                        ReturnStatus: MFnIkJoint.MStatus): 
        '''
        create(self, parent: MObject,
                        ReturnStatus: MFnIkJoint.MStatus) -> MObject

        Synopsis
        -----
        Create a new joint in a skeleton. In maya, skeletons are defined
        entirely by DAG hierarchy. So, giving the joint you want to
        attach to as a parent will add this joint to that skeleton.

        Returns: 
        ----- 
        The parent transform of the new joint

        Parameters:
        -----
        parent: MObject
        	[in] -> the parent object for this in the dag. A value of NULL specifies the world dag node as parent. 

        ReturnStatus: MFnIkJoint.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    @overload
    def getOrientation(self, quaternion: MQuaternion): 
        '''
        getOrientation(self, quaternion: MQuaternion)

        Synopsis
        -----
        Get the joint orientation. This corresponds to the jointOrient
        attribute on the joint, which is stored internally as a
        quaternion. It is different from the rotation orientation defined
        in the transform node. Modifying the jointOrient changes the
        coordinate axes, which affects how scaling a joint behaves.The
        matrix equations used to combine the jointOrient with the other
        transformation attributes of the joint are described in the
        description for the MFnIkJoint class.

        Returns:
        -----
        None

        Parameters:
        -----
        quaternion: MQuaternion
        	[out] -> the quaternion representing the jointOrient


        '''
        pass

    @overload
    def setOrientation(self, quaternion: MQuaternion): 
        '''
        setOrientation(self, quaternion: MQuaternion)

        Synopsis
        -----
        Set the jointOrient value. This corresponds to the jointOrient
        attribute on the joint, which is stored internally as a
        quaternion. It is different from the rotation orientation defined
        in the transform node. Modifying the jointOrient changes the
        coordinate axes, which affects how scaling a joint behaves.The
        matrix equations used to combine the jointOrient with the other
        transformation attributes of the joint are described in the
        description for the MFnIkJoint class.

        Returns:
        -----
        None

        Parameters:
        -----
        quaternion: MQuaternion
        	[in] -> the joint orientation


        '''
        pass

    @overload
    def getOrientation(self, rotation: MEulerRotation): 
        '''
        getOrientation(self, rotation: MEulerRotation)

        Synopsis
        -----
        Get the orientation of the coordinate axes.

        Returns:
        -----
        None

        Parameters:
        -----
        rotation: MEulerRotation
        	[out] -> the euler rotation into which we will store the orientation


        '''
        pass

    @overload
    def setOrientation(self, rotation: MEulerRotation): 
        '''
        setOrientation(self, rotation: MEulerRotation)

        Synopsis
        -----
        Set the orientation of the coordinate axes.

        Returns:
        -----
        None

        Parameters:
        -----
        rotation: MEulerRotation
        	[in] -> the orientation


        '''
        pass

    @overload
    def getOrientation(self, rotation: double3,
                        order: MTransformationMatrix.MTransformationMatrix): 
        '''
        getOrientation(self, rotation: double3,
                        order: MTransformationMatrix.MTransformationMatrix)

        Synopsis
        -----
        Get the orientation of the coordinate axes.

        Returns:
        -----
        None

        Parameters:
        -----
        rotation: double3
        	[out] -> the array into which we will store the angles 

        order: MTransformationMatrix.MTransformationMatrix
        	[out] -> storage for the order to do the rotation in


        '''
        pass

    @overload
    def setOrientation(self, rotation: double3,
                        order: MTransformationMatrix.MTransformationMatrix): 
        '''
        setOrientation(self, rotation: double3,
                        order: MTransformationMatrix.MTransformationMatrix)

        Synopsis
        -----
        Set the orientation of the coordinate axes.

        Returns:
        -----
        None

        Parameters:
        -----
        rotation: double3
        	[in] -> the orientation 

        order: MTransformationMatrix.MTransformationMatrix
        	[in] -> the order to do the rotation in


        '''
        pass

    @overload
    def getScaleOrientation(self, quaternion: MQuaternion): 
        '''
        getScaleOrientation(self, quaternion: MQuaternion)

        Synopsis
        -----
        Get the orientation of the coordinate axes for rotation. This is
        equivalent to calling the MFnTransform::rotateOrientation method,
        and corresponds to the rotateAxis attribute on the joint node.

        Returns:
        -----
        None

        Parameters:
        -----
        quaternion: MQuaternion
        	[out] -> the quaternion into which we will store the rotate orientation


        '''
        pass

    @overload
    def setScaleOrientation(self, quaternion: MQuaternion): 
        '''
        setScaleOrientation(self, quaternion: MQuaternion)

        Synopsis
        -----
        Set the orientation of the coordinate axes for rotation. This is
        equivalent to calling the MFnTransform::setRotateOrientation
        method, and corresponds to the rotateAxis attribute on the joint
        node. The matrix equations used to combine the rotateAxis with
        the other transformation attributes of the joint are described in
        the description for the MFnIkJoint class.

        Returns:
        -----
        None

        Parameters:
        -----
        quaternion: MQuaternion
        	[out] -> the rotate orientation


        '''
        pass

    @overload
    def getScaleOrientation(self, rotation: double3,
                        order: MTransformationMatrix.MTransformationMatrix): 
        '''
        getScaleOrientation(self, rotation: double3,
                        order: MTransformationMatrix.MTransformationMatrix)

        Synopsis
        -----
        Get the orientation of the coordinate axes for rotation. This is
        equivalent to calling the MFnTransform::rotateOrientation method
        but returns the Euler rotation rather than the quaternion
        rotation. The matrix equations used to combine the rotateAxis
        with the other transformation attributes of the joint are
        described in the description for the MFnIkJoint class.

        Returns:
        -----
        None

        Parameters:
        -----
        rotation: double3
        	[out] -> the array into which we will store the angles 

        order: MTransformationMatrix.MTransformationMatrix
        	[out] -> storage for the order to do the rotation in


        '''
        pass

    @overload
    def setScaleOrientation(self, rotation: double3,
                        order: MTransformationMatrix.MTransformationMatrix): 
        '''
        setScaleOrientation(self, rotation: double3,
                        order: MTransformationMatrix.MTransformationMatrix)

        Synopsis
        -----
        Set the orientation of the coordinate axes for rotation. This is
        equivalent to calling the MFnTransform::setRotateOrientation
        method, and corresponds to the rotateAxis attribute on the joint
        node. The matrix equations used to combine the rotateAxis with
        the other transformation attributes of the joint are described in
        the description for the MFnIkJoint class.

        Returns:
        -----
        None

        Parameters:
        -----
        rotation: double3
        	[in] -> the rotate orientation 

        order: MTransformationMatrix.MTransformationMatrix
        	[in] -> the order to do the rotation in


        '''
        pass

    def getSegmentScale(self, scale: double3): 
        '''
        getSegmentScale(self, scale: double3)

        Synopsis
        -----
        Get the local space scale values for the joint segment (bone).
        This is equivalent to calling MFnTransform::getScale.

        Returns:
        -----
        None

        Parameters:
        -----
        scale: double3
        	[out] -> Storage for the scale values


        '''
        pass

    def setSegmentScale(self, scale: double3): 
        '''
        setSegmentScale(self, scale: double3)

        Synopsis
        -----
        Set the local space scale values for the joint segment (bone).
        This is equivalent to calling Ttransform::setScale.

        Returns:
        -----
        None

        Parameters:
        -----
        scale: double3
        	[in] -> the new scale values to set


        '''
        pass

    def getStiffness(self, stiffness: double3): 
        '''
        getStiffness(self, stiffness: double3)

        Synopsis
        -----
        Get the stiffness (from 0 to 100.0) for the joint. The stiffness
        attribute is used by ik solvers to generate a resistance to a
        joint motion. The higher the stiffness the less it will rotate.
        Stiffness works in relative sense: it determines the willingness
        of this joint to rotate with respect to the other joint in the ik
        chain.

        Returns:
        -----
        None

        Parameters:
        -----
        stiffness: double3
        	[out] -> storage for the stiffness values


        '''
        pass

    def setStiffness(self, stiffness: double3): 
        '''
        setStiffness(self, stiffness: double3)

        Synopsis
        -----
        Set the stiffness (from 0 to 100.0) for the joint. The stiffness
        attribute is used by ik solvers to generate a resistance to a
        joint motion. The higher the stiffness the less it will rotate.
        Stiffness works in relative sense: it determines the willingness
        of this joint to rotate with respect to the other joint in the ik
        chain.

        Returns:
        -----
        None

        Parameters:
        -----
        stiffness: double3
        	[in] -> the X, Y, and Z stiffness values


        '''
        pass

    def getPreferredAngle(self, rotation: double3): 
        '''
        getPreferredAngle(self, rotation: double3)

        Synopsis
        -----
        Get the preferred orientation for this joint (in XYZ order)

        Returns:
        -----
        None

        Parameters:
        -----
        rotation: double3
        	[out] -> the array into which we will store the angles


        '''
        pass

    def setPreferredAngle(self, rotation: double3): 
        '''
        setPreferredAngle(self, rotation: double3)

        Synopsis
        -----
        Set the preferred orientation for this joint (in XYZ order)

        Returns:
        -----
        None

        Parameters:
        -----
        rotation: double3
        	[in] -> the array into which we will store the angles


        '''
        pass

    def getDegreesOfFreedom(self, freeInX: bool,
                        freeInY: bool,
                        freeInZ: bool): 
        '''
        getDegreesOfFreedom(self, freeInX: bool,
                        freeInY: bool,
                        freeInZ: bool)

        Synopsis
        -----
        Get degrees of freedom of this joint.

        Returns:
        -----
        None

        Parameters:
        -----
        freeInX: bool
        	[out] -> the first degree of freedom 

        freeInY: bool
        	[out] -> the second degree of freedom 

        freeInZ: bool
        	[out] -> the third degree of freedom


        '''
        pass

    def setDegreesOfFreedom(self, freeInX: bool,
                        freeInY: bool,
                        freeInZ: bool): 
        '''
        setDegreesOfFreedom(self, freeInX: bool,
                        freeInY: bool,
                        freeInZ: bool)

        Synopsis
        -----
        Set the degrees of freedom of this joint by specifying which axes
        are allowed to rotate.

        Returns:
        -----
        None

        Parameters:
        -----
        freeInX: bool
        	[in] -> the first degree of freedom 

        freeInY: bool
        	[in] -> the second degree of freedom 

        freeInZ: bool
        	[in] -> the third degree of freedom


        '''
        pass

    def minRotateDampXRange(self, ReturnStatus: MFnIkJoint.MStatus): 
        '''
        minRotateDampXRange(self, ReturnStatus: MFnIkJoint.MStatus) -> double

        Synopsis
        -----
        Get the minimum of the damping range in X. This corresponds to
        the minRotateDampXRange attribute on the joint.The
        minRotateDampRange and minRotateDampStrength are attributes used
        by ik to apply resistance to a joint rotation as it approaches
        the lower boundary of its rotation limits. This functionality
        allows joint motion to slow down smoothly until the joint reaches
        its rotation limits instead of stopping abruptly. The
        minRotateDampRange specifies when the deceleration should start,
        and the minRotateDampStrength defines the rate of deceleration.

        Returns: 
        ----- 
        The minimum damping range in X

        Parameters:
        -----
        ReturnStatus: MFnIkJoint.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def minRotateDampYRange(self, ReturnStatus: MFnIkJoint.MStatus): 
        '''
        minRotateDampYRange(self, ReturnStatus: MFnIkJoint.MStatus) -> double

        Synopsis
        -----
        Get the minimum of the damping range in Y. This corresponds to
        the minRotateDampYRange attribute on the joint.The
        minRotateDampRange and minRotateDampStrength are attributes used
        by ik to apply resistance to a joint rotation as it approaches
        the lower boundary of its rotation limits. This functionality
        allows joint motion to slow down smoothly until the joint reaches
        its rotation limits instead of stopping abruptly. The
        minRotateDampRange specifies when the deceleration should start,
        and the minRotateDampStrength defines the rate of deceleration.

        Returns: 
        ----- 
        The minimum damping range in Y

        Parameters:
        -----
        ReturnStatus: MFnIkJoint.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def minRotateDampZRange(self, ReturnStatus: MFnIkJoint.MStatus): 
        '''
        minRotateDampZRange(self, ReturnStatus: MFnIkJoint.MStatus) -> double

        Synopsis
        -----
        Get the minimum of the damping range in Z. This corresponds to
        the minRotateDampZRange attribute on the joint.The
        minRotateDampRange and minRotateDampStrength are attributes used
        by ik to apply resistance to a joint rotation as it approaches
        the lower boundary of its rotation limits. This functionality
        allows joint motion to slow down smoothly until the joint reaches
        its rotation limits instead of stopping abruptly. The
        minRotateDampRange specifies when the deceleration should start,
        and the minRotateDampStrength defines the rate of deceleration.

        Returns: 
        ----- 
        The minimum damping range in Z

        Parameters:
        -----
        ReturnStatus: MFnIkJoint.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def maxRotateDampXRange(self, ReturnStatus: MFnIkJoint.MStatus): 
        '''
        maxRotateDampXRange(self, ReturnStatus: MFnIkJoint.MStatus) -> double

        Synopsis
        -----
        Get the maximum of the damping range in X. This corresponds to
        the maxRotateDampXRange attribute on the joint.The
        minRotateDampRange and minRotateDampStrength are attributes used
        by ik to apply resistance to a joint rotation as it approaches
        the upper boundary of its rotation limits. This functionality
        allows joint motion to slow down smoothly until the joint reaches
        its rotation limits instead of stopping abruptly. The
        maxRotateDampRange specifies when the deceleration should start,
        and the maxRotateDampStrength defines the rate of deceleration.

        Returns: 
        ----- 
        The maximum of the damping range in X

        Parameters:
        -----
        ReturnStatus: MFnIkJoint.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def maxRotateDampYRange(self, ReturnStatus: MFnIkJoint.MStatus): 
        '''
        maxRotateDampYRange(self, ReturnStatus: MFnIkJoint.MStatus) -> double

        Synopsis
        -----
        Get the maximum of the damping range in Y. This corresponds to
        the maxRotateDampYRange attribute on the joint.The
        minRotateDampRange and minRotateDampStrength are attributes used
        by ik to apply resistance to a joint rotation as it approaches
        the upper boundary of its rotation limits. This functionality
        allows joint motion to slow down smoothly until the joint reaches
        its rotation limits instead of stopping abruptly. The
        maxRotateDampRange specifies when the deceleration should start,
        and the maxRotateDampStrength defines the rate of deceleration.

        Returns: 
        ----- 
        The maximum of the damping range in Y

        Parameters:
        -----
        ReturnStatus: MFnIkJoint.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def maxRotateDampZRange(self, ReturnStatus: MFnIkJoint.MStatus): 
        '''
        maxRotateDampZRange(self, ReturnStatus: MFnIkJoint.MStatus) -> double

        Synopsis
        -----
        Get the maximum of the damping range in Z. This corresponds to
        the maxRotateDampZRange attribute on the joint.The
        minRotateDampRange and minRotateDampStrength are attributes used
        by ik to apply resistance to a joint rotation as it approaches
        the upper boundary of its rotation limits. This functionality
        allows joint motion to slow down smoothly until the joint reaches
        its rotation limits instead of stopping abruptly. The
        maxRotateDampRange specifies when the deceleration should start,
        and the maxRotateDampStrength defines the rate of deceleration.

        Returns: 
        ----- 
        The maximum of the damping range in Z

        Parameters:
        -----
        ReturnStatus: MFnIkJoint.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def setMinRotateDampXRange(self, angle: double): 
        '''
        setMinRotateDampXRange(self, angle: double)

        Synopsis
        -----
        Set the minimum of the damping range in X.

        Returns:
        -----
        None

        Parameters:
        -----
        angle: double
        	[in] -> The damping range to set


        '''
        pass

    def setMinRotateDampYRange(self, angle: double): 
        '''
        setMinRotateDampYRange(self, angle: double)

        Synopsis
        -----
        Set the minimum of the damping range in Y.

        Returns:
        -----
        None

        Parameters:
        -----
        angle: double
        	[in] -> the damping range to set


        '''
        pass

    def setMinRotateDampZRange(self, angle: double): 
        '''
        setMinRotateDampZRange(self, angle: double)

        Synopsis
        -----
        Set the minimum of the damping range in Z.

        Returns:
        -----
        None

        Parameters:
        -----
        angle: double
        	[in] -> the damping range to set


        '''
        pass

    def setMaxRotateDampXRange(self, angle: double): 
        '''
        setMaxRotateDampXRange(self, angle: double)

        Synopsis
        -----
        Set the maximum of the damping range in X.

        Returns:
        -----
        None

        Parameters:
        -----
        angle: double
        	[in] -> the damping range to set


        '''
        pass

    def setMaxRotateDampYRange(self, angle: double): 
        '''
        setMaxRotateDampYRange(self, angle: double)

        Synopsis
        -----
        Set the maximum of the damping range in Y.

        Returns:
        -----
        None

        Parameters:
        -----
        angle: double
        	[in] -> the damping range to set


        '''
        pass

    def setMaxRotateDampZRange(self, angle: double): 
        '''
        setMaxRotateDampZRange(self, angle: double)

        Synopsis
        -----
        Set the maximum of the damping range in Z.

        Returns:
        -----
        None

        Parameters:
        -----
        angle: double
        	[in] -> the damping range to set


        '''
        pass

    def minRotateDampXStrength(self, ReturnStatus: MFnIkJoint.MStatus): 
        '''
        minRotateDampXStrength(self, ReturnStatus: MFnIkJoint.MStatus) -> double

        Synopsis
        -----
        Get the minimum of the damping strength in X.

        Returns: 
        ----- 
        Status code (see below)

        Parameters:
        -----
        ReturnStatus: MFnIkJoint.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def minRotateDampYStrength(self, ReturnStatus: MFnIkJoint.MStatus): 
        '''
        minRotateDampYStrength(self, ReturnStatus: MFnIkJoint.MStatus) -> double

        Synopsis
        -----
        Get the minimum of the damping strength in X.

        Returns: 
        ----- 
        Status code (see below)

        Parameters:
        -----
        ReturnStatus: MFnIkJoint.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def minRotateDampZStrength(self, ReturnStatus: MFnIkJoint.MStatus): 
        '''
        minRotateDampZStrength(self, ReturnStatus: MFnIkJoint.MStatus) -> double

        Synopsis
        -----
        Get the minimum of the damping strength in X.

        Returns: 
        ----- 
        Status code (see below)

        Parameters:
        -----
        ReturnStatus: MFnIkJoint.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def maxRotateDampXStrength(self, ReturnStatus: MFnIkJoint.MStatus): 
        '''
        maxRotateDampXStrength(self, ReturnStatus: MFnIkJoint.MStatus) -> double

        Synopsis
        -----
        Get the minimum of the damping strength in X.

        Returns: 
        ----- 
        Status code (see below)

        Parameters:
        -----
        ReturnStatus: MFnIkJoint.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def maxRotateDampYStrength(self, ReturnStatus: MFnIkJoint.MStatus): 
        '''
        maxRotateDampYStrength(self, ReturnStatus: MFnIkJoint.MStatus) -> double

        Synopsis
        -----
        Get the minimum of the damping strength in X.

        Returns: 
        ----- 
        Status code (see below)

        Parameters:
        -----
        ReturnStatus: MFnIkJoint.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def maxRotateDampZStrength(self, ReturnStatus: MFnIkJoint.MStatus): 
        '''
        maxRotateDampZStrength(self, ReturnStatus: MFnIkJoint.MStatus) -> double

        Synopsis
        -----
        Get the minimum of the damping strength in X.

        Returns: 
        ----- 
        Status code (see below)

        Parameters:
        -----
        ReturnStatus: MFnIkJoint.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def setMinRotateDampXStrength(self, angle: double): 
        '''
        setMinRotateDampXStrength(self, angle: double)

        Synopsis
        -----
        Set the maximum of the damping strength in Z.

        Returns:
        -----
        None

        Parameters:
        -----
        angle: double
        	[in] -> The new damping strength value


        '''
        pass

    def setMinRotateDampYStrength(self, angle: double): 
        '''
        setMinRotateDampYStrength(self, angle: double)

        Synopsis
        -----
        Set the maximum of the damping strength in Y.

        Returns:
        -----
        None

        Parameters:
        -----
        angle: double
        	[in] -> The new damping strength value


        '''
        pass

    def setMinRotateDampZStrength(self, angle: double): 
        '''
        setMinRotateDampZStrength(self, angle: double)

        Synopsis
        -----
        Set the minimum of the damping strength in Z.

        Returns:
        -----
        None

        Parameters:
        -----
        angle: double
        	[in] -> The new damping strength value


        '''
        pass

    def setMaxRotateDampXStrength(self, angle: double): 
        '''
        setMaxRotateDampXStrength(self, angle: double)

        Synopsis
        -----
        Set the maximum of the damping strength in X.

        Returns:
        -----
        None

        Parameters:
        -----
        angle: double
        	[in] -> The new damping strength value


        '''
        pass

    def setMaxRotateDampYStrength(self, angle: double): 
        '''
        setMaxRotateDampYStrength(self, angle: double)

        Synopsis
        -----
        Set the maximum of the damping strength in Y.

        Returns:
        -----
        None

        Parameters:
        -----
        angle: double
        	[in] -> The new damping strength value


        '''
        pass

    def setMaxRotateDampZStrength(self, angle: double): 
        '''
        setMaxRotateDampZStrength(self, angle: double)

        Synopsis
        -----
        Set the maximum of the damping strength in Z.

        Returns:
        -----
        None

        Parameters:
        -----
        angle: double
        	[in] -> The new damping strength value


        '''
        pass

    def hikJointName(self, ReturnStatus: MFnIkJoint.MStatus): 
        '''
        hikJointName(self, ReturnStatus: MFnIkJoint.MStatus) -> MString

        Synopsis
        -----
        Get the name that the HumanIK solver uses to identify this joint.

        Returns: 
        ----- 
        The name used to identify this joint for HumanIK

        Parameters:
        -----
        ReturnStatus: MFnIkJoint.MStatus
        	[out] -> Status code (see below)


        '''
        pass

class MFnIkSolver:
    '''Function set for inverse kinematics (IK) solvers.
This is the function set for inverse kinematics (IK) solvers.
This function set is used for setting and querying attached ik
solvers.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kIkSolver.Reimplemented from MFnDependencyNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> MFnIkSolver.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnIkSolver".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def maxIterations(self, ReturnStatus: MFnIkSolver.MStatus): 
        '''
        maxIterations(self, ReturnStatus: MFnIkSolver.MStatus) -> int

        Synopsis
        -----
        Returns the maximum number of iterations used when solving.

        Returns: 
        ----- 
        The maximum number of iterations used by this solver when solving

        Parameters:
        -----
        ReturnStatus: MFnIkSolver.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def setMaxIterations(self, maxIters: int): 
        '''
        setMaxIterations(self, maxIters: int)

        Synopsis
        -----
        Sets the maximum number of iterations used when solving.

        Returns:
        -----
        None

        Parameters:
        -----
        maxIters: int
        	[in] -> the new value for the maximum number of iterations for the solver


        '''
        pass

    def tolerance(self, ReturnStatus: MFnIkSolver.MStatus): 
        '''
        tolerance(self, ReturnStatus: MFnIkSolver.MStatus) -> double

        Synopsis
        -----
        Returns the tolerance used when solving.

        Returns: 
        ----- 
        The tolerance value for this solver

        Parameters:
        -----
        ReturnStatus: MFnIkSolver.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def setTolerance(self, tolerance: double): 
        '''
        setTolerance(self, tolerance: double)

        Synopsis
        -----
        Sets the tolerance used when solving.

        Returns:
        -----
        None

        Parameters:
        -----
        tolerance: double
        	[in] -> The tolerance value to be set


        '''
        pass

class MFnKeyframeDelta:
    '''Base function set for keyframe deltas.
Keyframe delta objects are returned via the
MAnimMessage::animKeyframeEditedCallback( ... ). They describe
atomic changes to keyframes as a result of a curve edit
operation. Refer to the documentation in
MAnimMessage class for further information.
Base function set for all keyframe delta objects. A keyframe
delta object is generated from the
MAnimMessage::addAnimKeyframeEditedCallback.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kKeyframeDelta.Reimplemented from MFnBase.Reimplemented in
        MFnKeyframeDeltaTangent, MFnKeyframeDeltaBlockAddRemove,
        MFnKeyframeDeltaInfType, MFnKeyframeDeltaMove,
        MFnKeyframeDeltaAddRemove, MFnKeyframeDeltaScale,
        MFnKeyframeDeltaBreakdown, and MFnKeyframeDeltaWeighted.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> staticchar*

        Synopsis
        -----
        Returns the name of this class.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def paramCurve(self, ReturnStatus: MFnKeyframeDelta.MStatus): 
        '''
        paramCurve(self, ReturnStatus: MFnKeyframeDelta.MStatus) -> MObject

        Synopsis
        -----
        Return the Animation Curve MObject that this key belongs to.

        Returns: 
        ----- 
        A MObject, readable by MFnAnimCurve.

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDelta.MStatus
        	[out] -> Return code.


        '''
        pass

    def keyIndex(self, ReturnStatus: MFnKeyframeDelta.MStatus): 
        '''
        keyIndex(self, ReturnStatus: MFnKeyframeDelta.MStatus) -> int

        Synopsis
        -----
        The index of this key on the animation curve. Note that when keys
        are added and then moved in a single action, the delta for the
        added key may refer to a key that no longer exists. In this case,
        the index returned related to the add operation will be the index
        where the key would be if it still existed on the curve. For
        example, if an animation curve has keys at frames 1 and 10, and a
        key is added at frame 12 and then moved to frame 11 in a single
        action, when the callback for the addition is received, the key
        at frame 12 will no longer exist. In this case, the keyIndex
        returned will be 3, to indicate that the key would be at index 3
        if it existed. Reimplemented in MFnKeyframeDeltaAddRemove, and
        MFnKeyframeDeltaMove.

        Returns: 
        ----- 
        An unsigned int representing the position of the key on the
        curve.

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDelta.MStatus
        	[out] -> Return code.


        '''
        pass

class MFnKeyframeDeltaAddRemove:
    '''Function set for the addition or removal keys on a curve.
Captures the addition or removal of key on a curve. keyIndex(...)
will return the index of the key that was added or removed.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kKeyframeDeltaAddRemove.Reimplemented from MFnKeyframeDelta.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> MFnKeyframeDeltaAddRemove.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnKeyframeDeltaAddRemove".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def deltaType(self, ReturnStatus: MFnKeyframeDeltaAddRemove.MStatus): 
        '''
        deltaType(self, ReturnStatus: MFnKeyframeDeltaAddRemove.MStatus) -> MFnKeyframeDeltaAddRemove.MFnKeyframeDeltaAddRemove

        Synopsis
        -----
        Indicates the type of change that this class instance represents.

        Returns: 
        ----- 
        kAdded - a key has been added.  kRemoved - a key has been
        removed.

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaAddRemove.MStatus
        	[out] -> 


        '''
        pass

    def value(self, ReturnStatus: MFnKeyframeDeltaAddRemove.MStatus): 
        '''
        value(self, ReturnStatus: MFnKeyframeDeltaAddRemove.MStatus) -> double

        Synopsis
        -----
        The value of the key that was added or removed.

        Returns: 
        ----- 
        A double value

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaAddRemove.MStatus
        	[out] -> Return code.


        '''
        pass

    def time(self, ReturnStatus: MFnKeyframeDeltaAddRemove.MStatus): 
        '''
        time(self, ReturnStatus: MFnKeyframeDeltaAddRemove.MStatus) -> MTime

        Synopsis
        -----
        The time value of the key that was added or removed.

        Returns: 
        ----- 
        A MTime value of the added/removed key.

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaAddRemove.MStatus
        	[out] -> Return code.


        '''
        pass

    def keyIndex(self, ReturnStatus: MFnKeyframeDeltaAddRemove.MStatus): 
        '''
        keyIndex(self, ReturnStatus: MFnKeyframeDeltaAddRemove.MStatus) -> int

        Synopsis
        -----
        The index of this key on the animation curve. Note that when keys
        are added and then moved in a single action, the delta for the
        added key may refer to a key that no longer exists. In this case,
        the index returned related to the add operation will be the index
        where the key would be if it still existed on the curve. For
        example, if an animation curve has keys at frames 1 and 10, and a
        key is added at frame 12 and then moved to frame 11 in a single
        action, when the callback for the addition is received, the key
        at frame 12 will no longer exist. In this case, the keyIndex
        returned will be 3, to indicate that the key would be at index 3
        if it existed. Reimplemented from MFnKeyframeDelta.

        Returns: 
        ----- 
        An unsigned int representing the position of the key on the
        curve.

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaAddRemove.MStatus
        	[out] -> Return code.


        '''
        pass

    def replacedValue(self, ReturnStatus: MFnKeyframeDeltaAddRemove.MStatus): 
        '''
        replacedValue(self, ReturnStatus: MFnKeyframeDeltaAddRemove.MStatus) -> double

        Synopsis
        -----
        The value of the key that was replaced. This method is only
        applicable to the kReplaced operation. Otherwise it will return
        0.

        Returns: 
        ----- 
        A double value

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaAddRemove.MStatus
        	[out] -> Return code.


        '''
        pass

class DeltaType:
    '''Type of change. 
    Non-functional class.  Values for this enum:
    kAdded
    kRemoved
    kReplaced
    '''

    def __init__(self):
        pass

    def kAdded(self):
        '''This is an enum of DeltaType.
        - Description: Key added. 
        - Value: 0
        '''
        pass

    def kRemoved(self):
        '''This is an enum of DeltaType.
        - Description: Key removed. 
        - Value: 1
        '''
        pass

    def kReplaced(self):
        '''This is an enum of DeltaType.
        - Description: Key replaced. 
        - Value: 2
        '''
        pass

class MFnKeyframeDeltaBlockAddRemove:
    '''Function set for block add or removal of keys.
Certain keyframe editing operations work on group of keys rather
than an single key. These operations require this function set to
retrieve changes.
Function set for reading a block of keyframe changes. They are
used internally to set a large group of keys quickly. Because
changes occur in groups using base class keyframe methods on this
derived class do not make sense. Therefore, methods describing
where the block of keys were added or removed are available
though methods on this class.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kKeyframeDeltaBlockAddRemove.Reimplemented from
        MFnKeyframeDelta.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> MFnKeyframeDeltaBlockAddRemove.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnKeyframeDeltaBlockAddRemove".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def deltaType(self, ReturnStatus: MFnKeyframeDeltaBlockAddRemove.MStatus): 
        '''
        deltaType(self, ReturnStatus: MFnKeyframeDeltaBlockAddRemove.MStatus) -> MFnKeyframeDeltaBlockAddRemove.MFnKeyframeDeltaBlockAddRemove

        Synopsis
        -----
        Indicates the type of change, i.e. keys added or removed, that
        this class instance represents.

        Returns: 
        ----- 
        kAdded - a block of keys were added.  kRemoved - a block of keys
        were removed.

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaBlockAddRemove.MStatus
        	[out] -> Return code.


        '''
        pass

    def startTime(self, ReturnStatus: MFnKeyframeDeltaBlockAddRemove.MStatus): 
        '''
        startTime(self, ReturnStatus: MFnKeyframeDeltaBlockAddRemove.MStatus) -> MTime

        Synopsis
        -----
        An MTime value indicating the start time of the add/remove.

        Returns: 
        ----- 
        An MTime value.

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaBlockAddRemove.MStatus
        	[out] -> Return code.


        '''
        pass

    def endTime(self, ReturnStatus: MFnKeyframeDeltaBlockAddRemove.MStatus): 
        '''
        endTime(self, ReturnStatus: MFnKeyframeDeltaBlockAddRemove.MStatus) -> MTime

        Synopsis
        -----
        Returns an MTime value indicating the endTime of the add/remove.

        Returns: 
        ----- 
        An MTime value indicating the end of the add/remove.

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaBlockAddRemove.MStatus
        	[out] -> Return code.


        '''
        pass

    def numKeys(self, ReturnStatus: MFnKeyframeDeltaBlockAddRemove.MStatus): 
        '''
        numKeys(self, ReturnStatus: MFnKeyframeDeltaBlockAddRemove.MStatus) -> int

        Synopsis
        -----
        Total number of keys involved in this add or remove operation.

        Returns:
        -----
        None

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaBlockAddRemove.MStatus
        	[out] -> Return code.


        '''
        pass

    def getValues(self, values: MDoubleArray,
                        ReturnStatus: MFnKeyframeDeltaBlockAddRemove.MStatus): 
        '''
        getValues(self, values: MDoubleArray,
                        ReturnStatus: MFnKeyframeDeltaBlockAddRemove.MStatus)

        Synopsis
        -----
        Returns the values of all keys involved in the group add or
        remove.

        Returns:
        -----
        None

        Parameters:
        -----
        values: MDoubleArray
        	[in] -> MDoubleArray

        ReturnStatus: MFnKeyframeDeltaBlockAddRemove.MStatus
        	[out] -> Status code.


        '''
        pass

    def getTimes(self, times: MTimeArray,
                        ReturnStatus: MFnKeyframeDeltaBlockAddRemove.MStatus): 
        '''
        getTimes(self, times: MTimeArray,
                        ReturnStatus: MFnKeyframeDeltaBlockAddRemove.MStatus)

        Synopsis
        -----
        Returns the times of all keys involved in the group add or
        remove.

        Returns:
        -----
        None

        Parameters:
        -----
        times: MTimeArray
        	[in] -> MTimeArray

        ReturnStatus: MFnKeyframeDeltaBlockAddRemove.MStatus
        	[out] -> Return code.


        '''
        pass

class DeltaType:
    '''Type of change. 
    Non-functional class.  Values for this enum:
    kAdded
    kRemoved
    '''

    def __init__(self):
        pass

    def kAdded(self):
        '''This is an enum of DeltaType.
        - Description: Keys were added. 
        - Value: 0
        '''
        pass

    def kRemoved(self):
        '''This is an enum of DeltaType.
        - Description: Keys were removed. 
        - Value: 1
        '''
        pass

class MFnKeyframeDeltaBreakdown:
    '''Function set for changes in a key's breakdown state.
Delta keyframe object for changes in breakdown state of a key.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kKeyframeDeltaBreakdown.Reimplemented from MFnKeyframeDelta.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> MFnKeyframeDeltaBreakdown.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnKeyframeDeltaBreakdown".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def wasBreakdown(self, ReturnStatus: MFnKeyframeDeltaBreakdown.MStatus): 
        '''
        wasBreakdown(self, ReturnStatus: MFnKeyframeDeltaBreakdown.MStatus) -> bool

        Synopsis
        -----
        Returns the previous breakdown state of the key. It will return
        false if the key was converted to a breakdown key.

        Returns: 
        ----- 
        true or false depending on the key's breakdown state.

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaBreakdown.MStatus
        	[out] -> Return code.


        '''
        pass

    def isBreakdown(self, ReturnStatus: MFnKeyframeDeltaBreakdown.MStatus): 
        '''
        isBreakdown(self, ReturnStatus: MFnKeyframeDeltaBreakdown.MStatus) -> bool

        Synopsis
        -----
        Returns the current breakdown state of the key. It will return
        true if the key was converted to a breakdown key.

        Returns: 
        ----- 
        true or false depending on the key's breakdown state.

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaBreakdown.MStatus
        	[out] -> Return code.


        '''
        pass

class MFnKeyframeDeltaInfType:
    '''Function set for changes in pre or post infinity type.
This delta object represents changes in the pre-infinity or post-
infinity type of the animation curve. Pre-infinity and post-
infinity types are specific to animation curves and do not have a
corresponding key associated with them. It is, therefore, invalid
to have a keyframe associated with a
MFnKeyframeDeltaInfType. To determine if this class represents a change to pre or post
infinity use the method isPreInfinity on this class.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kKeyframeDeltaInfType.Reimplemented from MFnKeyframeDelta.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> MFnKeyframeDeltaInfType.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnKeyframeDeltaInfType".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def previousInfinityType(self, ReturnStatus: MFnKeyframeDeltaInfType.MStatus): 
        '''
        previousInfinityType(self, ReturnStatus: MFnKeyframeDeltaInfType.MStatus) -> MFnAnimCurve.MFnAnimCurve

        Synopsis
        -----
        The previous infinity type.

        Returns: 
        ----- 
        The previous infinityType for the curve.

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaInfType.MStatus
        	[out] -> Return code.


        '''
        pass

    def currentInfinityType(self, ReturnStatus: MFnKeyframeDeltaInfType.MStatus): 
        '''
        currentInfinityType(self, ReturnStatus: MFnKeyframeDeltaInfType.MStatus) -> MFnAnimCurve.MFnAnimCurve

        Synopsis
        -----
        The current infinity type.

        Returns: 
        ----- 
        The current InfinityType for the curve

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaInfType.MStatus
        	[out] -> Return code.


        '''
        pass

    def isPreInfinity(self, ReturnStatus: MFnKeyframeDeltaInfType.MStatus): 
        '''
        isPreInfinity(self, ReturnStatus: MFnKeyframeDeltaInfType.MStatus) -> bool

        Synopsis
        -----
        This class can describe changes to both the pre-infinity and
        post-infinity this method allows the API user to figure out which
        type this class represents.

        Returns: 
        ----- 
        true if this class encapsulates changes to the pre-infinity type.

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaInfType.MStatus
        	[out] -> Return code.


        '''
        pass

class MFnKeyframeDeltaMove:
    '''Function set for change in keyframe value or time.
This function set is used for keyframe deltas of type
MFn::kKeyframeDeltaMove. These keyframe deltas are generated from 'move' events. For
example, the user drags or scales a key from one position to
another.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kKeyframeDeltaMove.Reimplemented from MFnKeyframeDelta.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> MFnKeyframeDeltaMove.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnKeyframeDeltaMove".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def previousTime(self, ReturnStatus: MFnKeyframeDeltaMove.MStatus): 
        '''
        previousTime(self, ReturnStatus: MFnKeyframeDeltaMove.MStatus) -> MTime

        Synopsis
        -----
        The previous time value of this key.

        Returns: 
        ----- 
        A MTime containing the previous time of this key.

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaMove.MStatus
        	[out] -> Return Code


        '''
        pass

    def currentTime(self, ReturnStatus: MFnKeyframeDeltaMove.MStatus): 
        '''
        currentTime(self, ReturnStatus: MFnKeyframeDeltaMove.MStatus) -> MTime

        Synopsis
        -----
        The current/current time value.

        Returns: 
        ----- 
        A MTime containing the current time of this key.

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaMove.MStatus
        	[out] -> Status code.


        '''
        pass

    def previousValue(self, ReturnStatus: MFnKeyframeDeltaMove.MStatus): 
        '''
        previousValue(self, ReturnStatus: MFnKeyframeDeltaMove.MStatus) -> double

        Synopsis
        -----
        The previous value of the key prior to the change. The value
        corresponds to the units of the animation curve.

        Returns: 
        ----- 
        A double representing the previous value of the key.

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaMove.MStatus
        	[out] -> Return code.


        '''
        pass

    def currentValue(self, ReturnStatus: MFnKeyframeDeltaMove.MStatus): 
        '''
        currentValue(self, ReturnStatus: MFnKeyframeDeltaMove.MStatus) -> double

        Synopsis
        -----
        The current value of the key. The value corresponds to the units
        of the animation curve.

        Returns: 
        ----- 
        A double representing the current value of the key.

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaMove.MStatus
        	[out] -> Return code.


        '''
        pass

    def previousIndex(self, ReturnStatus: MFnKeyframeDeltaMove.MStatus): 
        '''
        previousIndex(self, ReturnStatus: MFnKeyframeDeltaMove.MStatus) -> int

        Synopsis
        -----
        The previous index value of this key. If a key has been moved
        over another key then you can use this previous index to figure
        out where the key was moved from.

        Returns: 
        ----- 
        An unsigned value representing the previous index of this key on
        the curve.

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaMove.MStatus
        	[out] -> Return code.


        '''
        pass

    def keyIndex(self, ReturnStatus: MFnKeyframeDeltaMove.MStatus): 
        '''
        keyIndex(self, ReturnStatus: MFnKeyframeDeltaMove.MStatus) -> int

        Synopsis
        -----
        The current index value of this key. Reimplemented from
        MFnKeyframeDelta.

        Returns: 
        ----- 
        An unsigned value representing the current index of this key on
        the curve.

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaMove.MStatus
        	[out] -> Return code.


        '''
        pass

class MFnKeyframeDeltaScale:
    ''''''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kKeyframeDeltaScale.Reimplemented from MFnKeyframeDelta.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> char*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnKeyframeDeltaScale".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def startTime(self, ReturnStatus: MFnKeyframeDeltaScale.MStatus): 
        '''
        startTime(self, ReturnStatus: MFnKeyframeDeltaScale.MStatus) -> MTime

        Synopsis
        -----
        The start time of the scaling block.

        Returns: 
        ----- 
        An MTime value

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaScale.MStatus
        	[out] -> return code.


        '''
        pass

    def endTime(self, ReturnStatus: MFnKeyframeDeltaScale.MStatus): 
        '''
        endTime(self, ReturnStatus: MFnKeyframeDeltaScale.MStatus) -> MTime

        Synopsis
        -----
        The end time of the scaling block.

        Returns: 
        ----- 
        An MTime value

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaScale.MStatus
        	[out] -> return code.


        '''
        pass

    def currentStartTime(self, ReturnStatus: MFnKeyframeDeltaScale.MStatus): 
        '''
        currentStartTime(self, ReturnStatus: MFnKeyframeDeltaScale.MStatus) -> MTime

        Synopsis
        -----
        The current scale time (after scaling has been performed).

        Returns: 
        ----- 
        An MTime value

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaScale.MStatus
        	[out] -> return code.


        '''
        pass

    def currentEndTime(self, ReturnStatus: MFnKeyframeDeltaScale.MStatus): 
        '''
        currentEndTime(self, ReturnStatus: MFnKeyframeDeltaScale.MStatus) -> MTime

        Synopsis
        -----
        The current end time.

        Returns: 
        ----- 
        An MTime value

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaScale.MStatus
        	[out] -> return code.


        '''
        pass

    def pivotTime(self, ReturnStatus: MFnKeyframeDeltaScale.MStatus): 
        '''
        pivotTime(self, ReturnStatus: MFnKeyframeDeltaScale.MStatus) -> MTime

        Synopsis
        -----
        The pivot point of the scale (in time).

        Returns: 
        ----- 
        An MTime value

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaScale.MStatus
        	[out] -> return code.


        '''
        pass

class MFnKeyframeDeltaTangent:
    '''Function set for changes to a key's tangent.
A
MFnKeyframeDeltaTangent function allows API programmers to read changes in keyframe
tangent values. It captures changes in tangent type, as well as,
changes in tangent time/value pair.
MFnKeyframeDeltaTangents are generated by a
MAnimMessage::addAnimKeyframeEditedCallback. Because a key's tangent may be unbroken. It is possible to
receive to
MFnKeyframeDeltaTangent values per key – one for the incoming tangent and one for the
outgoing tangent. The API programmer should use the isInTangent
method to determine if the tangent change affects the in-bound
tangent or out-bound tangent.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kKeyframeDeltaTangent.Reimplemented from MFnKeyframeDelta.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> MFnKeyframeDeltaTangent.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnKeyframeDeltaTangent".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def previousTangentType(self, ReturnStatus: MFnKeyframeDeltaTangent.MStatus): 
        '''
        previousTangentType(self, ReturnStatus: MFnKeyframeDeltaTangent.MStatus) -> MFnAnimCurve.MFnAnimCurve

        Synopsis
        -----
        Returns the previous tangent type.

        Returns: 
        ----- 
        The previous tangent type.

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaTangent.MStatus
        	[out] -> Return code.


        '''
        pass

    def currentTangentType(self, ReturnStatus: MFnKeyframeDeltaTangent.MStatus): 
        '''
        currentTangentType(self, ReturnStatus: MFnKeyframeDeltaTangent.MStatus) -> MFnAnimCurve.MFnAnimCurve

        Synopsis
        -----
        Returns the current tangent type that the key represents.

        Returns: 
        ----- 
        The current tangent type.

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaTangent.MStatus
        	[out] -> Return code.


        '''
        pass

    def getPreviousPosition(self, x: MFnAnimCurve.MFnAnimCurve,
                        y: MFnAnimCurve.MFnAnimCurve): 
        '''
        getPreviousPosition(self, x: MFnAnimCurve.MFnAnimCurve,
                        y: MFnAnimCurve.MFnAnimCurve)

        Synopsis
        -----
        Get the values of the previous time/value position of the tangent
        for this key.

        Returns:
        -----
        None

        Parameters:
        -----
        x: MFnAnimCurve.MFnAnimCurve
        	[out] -> The x component of the position. 

        y: MFnAnimCurve.MFnAnimCurve
        	[out] -> The y component of the position.


        '''
        pass

    def getCurrentPosition(self, x: MFnAnimCurve.MFnAnimCurve,
                        y: MFnAnimCurve.MFnAnimCurve): 
        '''
        getCurrentPosition(self, x: MFnAnimCurve.MFnAnimCurve,
                        y: MFnAnimCurve.MFnAnimCurve)

        Synopsis
        -----
        Get the values of the current time/value position of the tangent
        for this key.

        Returns:
        -----
        None

        Parameters:
        -----
        x: MFnAnimCurve.MFnAnimCurve
        	[out] -> The x component of the position. 

        y: MFnAnimCurve.MFnAnimCurve
        	[out] -> The y component of the position.


        '''
        pass

    def isInTangent(self, ReturnStatus: MFnKeyframeDeltaTangent.MStatus): 
        '''
        isInTangent(self, ReturnStatus: MFnKeyframeDeltaTangent.MStatus) -> bool

        Synopsis
        -----
        Key's have two tangents, in-bound and out-bound. A
        MFnKeyframeTangent object can created once for each tangent. Use
        this method to determine which tangent was modified.

        Returns: 
        ----- 
        true if the incoming tangent was modified.  false if the outgoing
        tangent was modified.

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaTangent.MStatus
        	[out] -> Return code.


        '''
        pass

class MFnKeyframeDeltaWeighted:
    '''Function set for changes in a key's weighted state.
Delta keyframe object for changes in weighted state of a key.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kKeyframeDeltaWeighted.Reimplemented from MFnKeyframeDelta.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> MFnKeyframeDeltaWeighted.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnKeyframeDeltaWeighted".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def wasWeighted(self, ReturnStatus: MFnKeyframeDeltaWeighted.MStatus): 
        '''
        wasWeighted(self, ReturnStatus: MFnKeyframeDeltaWeighted.MStatus) -> bool

        Synopsis
        -----
        Returns true if the key had weighted tangent, but it is not
        currently.

        Returns: 
        ----- 
        true or false depending on the key's weight status.

        Parameters:
        -----
        ReturnStatus: MFnKeyframeDeltaWeighted.MStatus
        	[out] -> Return code.


        '''
        pass

class MFnLattice:
    '''Lattice function set.
MFnLattice is the function set for lattice shapes and lattice geometry. It
can be used on lattices in the DAG or on lattice geometry from a
dependency node attribute.
Lattices are most commonly used for specifying FFDs (free-form
deformations). See
MFnLatticeDeformer for more information on those.
MFnLatticeData can be used to create new lattice data objects for use with
dependency node attributes.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kLattice.Reimplemented from MFnDagNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> MFnLattice.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnLattice".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def create(self, xDiv: int,
                        yDiv: int,
                        zDiv: int,
                        parentOrOwner: MObject,
                        ReturnStatus: MFnLattice.MStatus): 
        '''
        create(self, xDiv: int,
                        yDiv: int,
                        zDiv: int,
                        parentOrOwner: MObject,
                        ReturnStatus: MFnLattice.MStatus) -> MObject

        Synopsis
        -----
        Create a new lattice. This can be used to create either a new
        lattice shape in the DAG, or to place new lattice geometry into a
        dependency graph lattice data object. Lattice data objects can be
        created with MFnLatticeData or can be obtained from an
        MDataHandle in the compute method of a dependency node.The
        parentOrOwner argument is used to specify the owner of the new
        lattice.If parentOrOwner is a kLatticeData data wrapper (e.g. as
        returned by MFnLatticeData::create) then a new kLattice object
        will be created and placed inside the wrapper. No nodes will be
        created and the method will return the kLattice object.If
        parentOrOwner is NULL then new lattice and transform nodes will
        be created and added to the DAG, with the lattice parented under
        the transform. The method will return the transform node.If
        parentOrOwner is a DAG node then a new lattice node will be
        created and parented under that DAG node. The method will return
        the lattice node.

        Returns: 
        ----- 
        A handle to the new lattice data, lattice node or transform node.
        See the discussion of the parentOrOwner parameter above for more
        details.

        Parameters:
        -----
        xDiv: int
        	[in] -> Lattice divisions in x (must be at least 2). 

        yDiv: int
        	[in] -> Lattice divisions in y (must be at least 2). 

        zDiv: int
        	[in] -> Lattice divisions in z (must be at least 2). 

        parentOrOwner: MObject
        	[in] -> Parent node or data wrapper. See discussion above. 

        ReturnStatus: MFnLattice.MStatus
        	[out] -> Status code.


        '''
        pass

    def reset(self, sSize: double,
                        tSize: double,
                        uSize: double): 
        '''
        reset(self, sSize: double,
                        tSize: double,
                        uSize: double)

        Synopsis
        -----
        Reset the lattice points to a uniform parallelipiped shape with
        the specified dimensions: sSize x tSize x uSize.

        Returns:
        -----
        None

        Parameters:
        -----
        sSize: double
        	[in] -> size in s dimension 

        tSize: double
        	[in] -> size in t dimension 

        uSize: double
        	[in] -> size in u dimension


        '''
        pass

    def getDivisions(self, s: int,
                        t: int,
                        u: int): 
        '''
        getDivisions(self, s: int,
                        t: int,
                        u: int)

        Synopsis
        -----
        Get the number of divisions in the lattice.

        Returns:
        -----
        None

        Parameters:
        -----
        s: int
        	[out] -> divisions in s dimension 

        t: int
        	[out] -> divisions in t dimension 

        u: int
        	[out] -> divisions in u dimension


        '''
        pass

    def setDivisions(self, s: int,
                        t: int,
                        u: int): 
        '''
        setDivisions(self, s: int,
                        t: int,
                        u: int)

        Synopsis
        -----
        Set the number of divisions in the lattice.

        Returns:
        -----
        None

        Parameters:
        -----
        s: int
        	[in] -> divisions in s dimension 

        t: int
        	[in] -> divisions in t dimension 

        u: int
        	[in] -> divisions in u dimension


        '''
        pass

    def point(self, s: int,
                        t: int,
                        u: int,
                        ReturnStatus: MFnLattice.MStatus): 
        '''
        point(self, s: int,
                        t: int,
                        u: int,
                        ReturnStatus: MFnLattice.MStatus) -> MPoint

        Synopsis
        -----
        Returns the point in the lattice that is at the given indices.

        Returns: 
        ----- 
        The point

        Parameters:
        -----
        s: int
        	[in] -> s index 

        t: int
        	[in] -> t index 

        u: int
        	[in] -> u index 

        ReturnStatus: MFnLattice.MStatus
        	[out] -> return status


        '''
        pass

class MFnLatticeDeformer:
    '''FFD lattice deformer function set.
MFnLatticeDeformer is the function set for lattice deformers. Lattice deformers use
FFDs to deform geometry.
The lattice deformer is actually a small network of dependency
nodes in the dependency graph. This function set is provided to
make manipulation of the network easier. The main deformer node
should be given to this function set as its object.
There are two lattices associated with a lattice deformer. There
is a base lattice that defines the start position for the
lattice. The second lattice is the version that is modified to
deform the geometry. The difference between the two lattices
defines the deformation that is applied to the geometry.
The base lattice is a very simple shape that only defines a box
in space. The base lattice should be modified by using the
standard DAG transformation support. The second deformable
lattice has geometry that can be modified using the
MFnLattice function set.
For a piece of geometry to be modified by this deformer, the
geometry must be attached to the deformer (use addGeometry
method) and the geometry must be contained within the base
lattice. The resetLattice method can be used to make the lattice
resize to the bounding box of the attached geometry.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kFFD.Reimplemented from MFnDependencyNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> MFnLatticeDeformer.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnLatticeDeformer".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def create(self, xDiv: int,
                        yDiv: int,
                        zDiv: int,
                        ReturnStatus: MFnLatticeDeformer.MStatus): 
        '''
        create(self, xDiv: int,
                        yDiv: int,
                        zDiv: int,
                        ReturnStatus: MFnLatticeDeformer.MStatus) -> MObject

        Synopsis
        -----
        Creates a new lattice deformer with the given number of
        divisions. This function set's object is set to be the new
        lattice node.

        Returns: 
        ----- 
        Returns a handle to the new deformer

        Parameters:
        -----
        xDiv: int
        	[in] -> number of divisions in x (must be at least 2) 

        yDiv: int
        	[in] -> number of divisions in y (must be at least 2) 

        zDiv: int
        	[in] -> number of divisions in z (must be at least 2) 

        ReturnStatus: MFnLatticeDeformer.MStatus
        	[out] -> return status


        '''
        pass

    def addGeometry(self, object: MObject): 
        '''
        addGeometry(self, object: MObject)

        Synopsis
        -----
        Adds a piece of geometry to the deformation. After adding new
        geometry to the deformation, one must make sure that the new
        geometry is contained within the base lattice for the deformation
        to affect it. The easiest way to do this is to reset the
        deformation with the flag that causes it to expand the base
        lattice to the bounding box of all of the contained geometry.

        Returns:
        -----
        None

        Parameters:
        -----
        object: MObject
        	[in] -> the geometry


        '''
        pass

    def removeGeometry(self, object: MObject): 
        '''
        removeGeometry(self, object: MObject)

        Synopsis
        -----
        Removes a piece of geometry from the deformation.

        Returns:
        -----
        None

        Parameters:
        -----
        object: MObject
        	[in] -> the geometry


        '''
        pass

    def getAffectedGeometry(self, objects: MObjectArray): 
        '''
        getAffectedGeometry(self, objects: MObjectArray)

        Synopsis
        -----
        The geometry affected by this deformer is packed into the
        provided list of MObjects. Each of the MObjects will be a DAG
        node that has geometry.

        Returns:
        -----
        None

        Parameters:
        -----
        objects: MObjectArray
        	[out] -> storage for the returned array


        '''
        pass

    def getDivisions(self, x: int,
                        y: int,
                        z: int): 
        '''
        getDivisions(self, x: int,
                        y: int,
                        z: int)

        Synopsis
        -----
        Retrieve the number of divisions in each of the X, Y, and Z
        directions. The number of divisions specifies the resolution of
        the lattice.

        Returns:
        -----
        None

        Parameters:
        -----
        x: int
        	[out] -> a reference parameter that on return contains the number of divisions in the X direction 

        y: int
        	[out] -> a reference parameter that on return contains the number of divisions in the Y direction 

        z: int
        	[out] -> a reference parameter that on return contains the number of divisions in the Z direction


        '''
        pass

    def setDivisions(self, x: int,
                        y: int,
                        z: int): 
        '''
        setDivisions(self, x: int,
                        y: int,
                        z: int)

        Synopsis
        -----
        Set the number of divisions in each of the X, Y, and Z
        directions. The number of divisions specifies the resolution of
        the lattice.

        Returns:
        -----
        None

        Parameters:
        -----
        x: int
        	[in] -> number of divisions in the X direction 

        y: int
        	[in] -> number of divisions in the Y direction 

        z: int
        	[in] -> number of divisions in the Z direction


        '''
        pass

    def resetLattice(self, centerLattice: bool): 
        '''
        resetLattice(self, centerLattice: bool)

        Synopsis
        -----
        This method resets the deformed lattice to match the base
        lattice. The center option will resize the lattice to be the
        bounding box of all contained geometry. If instanced objects are
        being deformed, then then centering option will take the first
        instance found. So, it is possible to get unexpected results when
        centering around instanced objects.

        Returns:
        -----
        None

        Parameters:
        -----
        centerLattice: bool
        	[in] -> whether to center the lattice


        '''
        pass

    def deformLattice(self, ReturnStatus: MFnLatticeDeformer.MStatus): 
        '''
        deformLattice(self, ReturnStatus: MFnLatticeDeformer.MStatus) -> MObject

        Synopsis
        -----
        This returns the deformed version of the lattice. The deformed
        lattice is a shape in the DAG and should be modified using the
        MFnLattice function set.

        Returns: 
        ----- 
        Handle for the deformed lattice shape

        Parameters:
        -----
        ReturnStatus: MFnLatticeDeformer.MStatus
        	[out] -> return status


        '''
        pass

    def baseLattice(self, ReturnStatus: MFnLatticeDeformer.MStatus): 
        '''
        baseLattice(self, ReturnStatus: MFnLatticeDeformer.MStatus) -> MObject

        Synopsis
        -----
        This returns the base version of the lattice that describes the
        region of space deformed by the lattice. The returned base
        lattice is a shape in the DAG and can be accessed using the
        MFnDagNode function set.

        Returns: 
        ----- 
        Handle for the base lattice shape

        Parameters:
        -----
        ReturnStatus: MFnLatticeDeformer.MStatus
        	[out] -> return status


        '''
        pass

class MFnMotionPath:
    '''Motion path animation function set.
This class is used for constructing and manipulating motion path
animation.
Motion path animation requires a curve (or surface) and one or
more other objects. During the animation, the objects will be
moved along the curve.
Setting "follow" for the motion path aligns the object(s) local
axis to the tangent of the motion path. Banking can also be
applied to objects.
Motion path markers are points along the path where the
orientation and position for the object(s) travelling along the
path can be specified.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kMotionPath.Reimplemented from MFnDependencyNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> MFnMotionPath.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnMotionPath".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def create(self, pathObject: MDagPath,
                        objectToAnimate: MDagPath,
                        timeStart: MTime,
                        timeEnd: MTime,
                        modifier: MDGModifier,
                        ReturnStatus: MFnMotionPath.MStatus): 
        '''
        create(self, pathObject: MDagPath,
                        objectToAnimate: MDagPath,
                        timeStart: MTime,
                        timeEnd: MTime,
                        modifier: MDGModifier,
                        ReturnStatus: MFnMotionPath.MStatus) -> MObject

        Synopsis
        -----
        Create a new motion path dependency node. When a motion path node
        is created, the following defaults are set:

        Returns: 
        ----- 
        The new motion path node

        Parameters:
        -----
        pathObject: MDagPath
        	[in] -> the curve, surface, or curve-on-surface to use as the object path 

        objectToAnimate: MDagPath
        	[in] -> the object that will follow the motion path 

        timeStart: MTime
        	[in] -> the time at which to start the animation 

        timeEnd: MTime
        	[in] -> the time at which to end the animation 

        modifier: MDGModifier
        	[in] -> this object will hold the undo information 

        ReturnStatus: MFnMotionPath.MStatus
        	[out] -> Status Code


        '''
        pass

    def setPathObject(self, pathObject: MDagPath,
                        modifier: MDGModifier): 
        '''
        setPathObject(self, pathObject: MDagPath,
                        modifier: MDGModifier)

        Synopsis
        -----
        Set the curve or surface for this motion path. All animated
        objects for this motion path will follow the new path that is
        specified.

        Returns:
        -----
        None

        Parameters:
        -----
        pathObject: MDagPath
        	[in] -> The curve (or surface) that will be the motion path 

        modifier: MDGModifier
        	[in] -> The object that will hold the undo information


        '''
        pass

    def pathObject(self, ReturnStatus: MFnMotionPath.MStatus): 
        '''
        pathObject(self, ReturnStatus: MFnMotionPath.MStatus) -> MDagPath

        Synopsis
        -----
        Return a dag path to the motion path object. The motion path
        object is the curve/surface that animated objects of this node
        will move along.

        Returns: 
        ----- 
        The dag path of the motion path object

        Parameters:
        -----
        ReturnStatus: MFnMotionPath.MStatus
        	[out] -> Status Code


        '''
        pass

    def addAnimatedObject(self, objectToAnimate: MDagPath,
                        modifier: MDGModifier): 
        '''
        addAnimatedObject(self, objectToAnimate: MDagPath,
                        modifier: MDGModifier)

        Synopsis
        -----
        Add an object to be animated along this motion path.

        Returns:
        -----
        None

        Parameters:
        -----
        objectToAnimate: MDagPath
        	[in] -> A DAG path to the animated object 

        modifier: MDGModifier
        	[in] -> The object that will hold the undo information


        '''
        pass

    def getAnimatedObjects(self, array: MDagPathArray): 
        '''
        getAnimatedObjects(self, array: MDagPathArray)

        Synopsis
        -----
        Returns an array of dag paths to the animated objects for this
        motion path.

        Returns:
        -----
        None

        Parameters:
        -----
        array: MDagPathArray
        	[out] -> Storage for the dag paths.


        '''
        pass

    def setFollow(self, on: bool,
                        modifier: MDGModifier): 
        '''
        setFollow(self, on: bool,
                        modifier: MDGModifier)

        Synopsis
        -----
        Setting follow on will cause the animated object(s) local axis to
        be aligned with the tangent of the motion path. The default
        alignment axis is Y.

        Returns:
        -----
        None

        Parameters:
        -----
        on: bool
        	[in] -> Specifies whether follow is activated for this motion path 

        modifier: MDGModifier
        	[in] -> The object that will hold the undo information


        '''
        pass

    def follow(self, ReturnStatus: MFnMotionPath.MStatus): 
        '''
        follow(self, ReturnStatus: MFnMotionPath.MStatus) -> bool

        Synopsis
        -----
        Determines whether follow is set for this motion path node.

        Returns: 
        ----- 
        true Follow is turned on  false Follow is turned off

        Parameters:
        -----
        ReturnStatus: MFnMotionPath.MStatus
        	[out] -> Status Code


        '''
        pass

    def setFollowAxis(self, axis: MFnMotionPath.MFnMotionPath): 
        '''
        setFollowAxis(self, axis: MFnMotionPath.MFnMotionPath)

        Synopsis
        -----
        Sets the axis of the animated object that will follow the motion
        path. Possible alignment parameters are kXaxis, kYaxiz, or
        kZaxis.

        Returns:
        -----
        None

        Parameters:
        -----
        axis: MFnMotionPath.MFnMotionPath
        	[in] -> Object axis to align with motion path tangent


        '''
        pass

    def followAxis(self, ReturnStatus: MFnMotionPath.MStatus): 
        '''
        followAxis(self, ReturnStatus: MFnMotionPath.MStatus) -> MFnMotionPath.MFnMotionPath

        Synopsis
        -----
        Return the follow axis for this motion path.

        Returns: 
        ----- 
        The follow axis.

        Parameters:
        -----
        ReturnStatus: MFnMotionPath.MStatus
        	[out] -> Status Code


        '''
        pass

    def setUpAxis(self, axis: MFnMotionPath.MFnMotionPath): 
        '''
        setUpAxis(self, axis: MFnMotionPath.MFnMotionPath)

        Synopsis
        -----
        Set the up-axis for this motion path.

        Returns:
        -----
        None

        Parameters:
        -----
        axis: MFnMotionPath.MFnMotionPath
        	[in] -> Axis to be set


        '''
        pass

    def upAxis(self, ReturnStatus: MFnMotionPath.MStatus): 
        '''
        upAxis(self, ReturnStatus: MFnMotionPath.MStatus) -> MFnMotionPath.MFnMotionPath

        Synopsis
        -----
        Return the up-axis for this motion path.

        Returns: 
        ----- 
        The up-axis for this motion path

        Parameters:
        -----
        ReturnStatus: MFnMotionPath.MStatus
        	[out] -> Status Code


        '''
        pass

    def setBank(self, bank: bool): 
        '''
        setBank(self, bank: bool)

        Synopsis
        -----

        Returns:
        -----
        None

        Parameters:
        -----
        bank: bool
        	[in] -> Specifies whether bank is turned on


        '''
        pass

    def bank(self, ReturnStatus: MFnMotionPath.MStatus): 
        '''
        bank(self, ReturnStatus: MFnMotionPath.MStatus) -> bool

        Synopsis
        -----
        Determines whether bank has been enabled for this motion path.

        Returns: 
        ----- 
        true Bank is enabled  false Bank is disabled

        Parameters:
        -----
        ReturnStatus: MFnMotionPath.MStatus
        	[out] -> Status Code


        '''
        pass

    def setBankScale(self, bankScale: double): 
        '''
        setBankScale(self, bankScale: double)

        Synopsis
        -----
        Set the bank scale for this motion path. If the computed bank
        angles are not large enough, the user can specify the bankScale
        to amplify them. The default value is 1.Positive bankScale
        produces inward bank angle, negative bankScale produces outward
        bank angle.

        Returns:
        -----
        None

        Parameters:
        -----
        bankScale: double
        	[in] -> The new bank scale value


        '''
        pass

    def bankScale(self, ReturnStatus: MFnMotionPath.MStatus): 
        '''
        bankScale(self, ReturnStatus: MFnMotionPath.MStatus) -> double

        Synopsis
        -----
        Return the bank scale for this motion path.

        Returns: 
        ----- 
        The bank scale.

        Parameters:
        -----
        ReturnStatus: MFnMotionPath.MStatus
        	[out] -> Status Code


        '''
        pass

    def setBankThreshold(self, bankThreshold: double): 
        '''
        setBankThreshold(self, bankThreshold: double)

        Synopsis
        -----
        Set the bank threshold for this motion path. The bank threshold
        is used to specify the maximum bank angle. The default value is
        90 degrees.

        Returns:
        -----
        None

        Parameters:
        -----
        bankThreshold: double
        	[in] -> The new bank threshold value


        '''
        pass

    def bankThreshold(self, ReturnStatus: MFnMotionPath.MStatus): 
        '''
        bankThreshold(self, ReturnStatus: MFnMotionPath.MStatus) -> double

        Synopsis
        -----
        Return the bank threshold for this motion path. The bank
        threshold is used to specify the maximum bank angle. The default
        value is 90 degrees.

        Returns: 
        ----- 
        The bank threshold.

        Parameters:
        -----
        ReturnStatus: MFnMotionPath.MStatus
        	[out] -> Status Code


        '''
        pass

    def setUseNormal(self, use: bool): 
        '''
        setUseNormal(self, use: bool)

        Synopsis
        -----
        If true, enables alignment of the up axis of the animated object
        to the normal vector of the path geometry.

        Returns:
        -----
        None

        Parameters:
        -----
        use: bool
        	[in] -> Specifies if normal is used


        '''
        pass

    def useNormal(self, ReturnStatus: MFnMotionPath.MStatus): 
        '''
        useNormal(self, ReturnStatus: MFnMotionPath.MStatus) -> bool

        Synopsis
        -----
        Determines whether the up-axis of the animated object for this
        motion path is aligned with the normal vector of the path
        geometry.

        Returns: 
        ----- 
        true Normal vector is used for object alignment.  false Normal
        vector is not used for object alignment.

        Parameters:
        -----
        ReturnStatus: MFnMotionPath.MStatus
        	[out] -> Status Code


        '''
        pass

    def setInverseNormal(self, invert: bool): 
        '''
        setInverseNormal(self, invert: bool)

        Synopsis
        -----
        If true, enable alignment of the up axis of the moving object(s)
        to the opposite direction of the normal vector of the path
        geometry.

        Returns:
        -----
        None

        Parameters:
        -----
        invert: bool
        	[in] -> Specifies if inverse normal is used


        '''
        pass

    def inverseNormal(self, ReturnStatus: MFnMotionPath.MStatus): 
        '''
        inverseNormal(self, ReturnStatus: MFnMotionPath.MStatus) -> bool

        Synopsis
        -----
        Determines whether the up-axis of the animated object for this
        motion path is aligned to the opposite direction of the normal
        vector of the path geometry.

        Returns: 
        ----- 
        true Inverse normal vector is used for object alignment.  false
        Inverse normal vector is not used for object alignment.

        Parameters:
        -----
        ReturnStatus: MFnMotionPath.MStatus
        	[out] -> Status Code


        '''
        pass

    def setUStart(self, start: double): 
        '''
        setUStart(self, start: double)

        Synopsis
        -----
        Sets the starting value of the u parameterization for the
        animation.

        Returns:
        -----
        None

        Parameters:
        -----
        start: double
        	[in] -> the new start value


        '''
        pass

    def setUEnd(self, end: double): 
        '''
        setUEnd(self, end: double)

        Synopsis
        -----
        Sets the end value of the u parameterization for the animation.

        Returns:
        -----
        None

        Parameters:
        -----
        end: double
        	[in] -> the new end value


        '''
        pass

    def uStart(self, ReturnStatus: MFnMotionPath.MStatus): 
        '''
        uStart(self, ReturnStatus: MFnMotionPath.MStatus) -> double

        Synopsis
        -----
        Returns the starting value of the u parameterization for the
        animation.

        Returns: 
        ----- 
        The starting value

        Parameters:
        -----
        ReturnStatus: MFnMotionPath.MStatus
        	[out] -> Status Code


        '''
        pass

    def uEnd(self, ReturnStatus: MFnMotionPath.MStatus): 
        '''
        uEnd(self, ReturnStatus: MFnMotionPath.MStatus) -> double

        Synopsis
        -----
        Returns the end value of the u parameterization for the
        animation.

        Returns: 
        ----- 
        The end value

        Parameters:
        -----
        ReturnStatus: MFnMotionPath.MStatus
        	[out] -> Status Code


        '''
        pass

    def setUTimeStart(self, start: MTime): 
        '''
        setUTimeStart(self, start: MTime)

        Synopsis
        -----
        Sets the starting time of the animation for the u parameter.

        Returns:
        -----
        None

        Parameters:
        -----
        start: MTime
        	[in] -> the new start time


        '''
        pass

    def setUTimeEnd(self, end: MTime): 
        '''
        setUTimeEnd(self, end: MTime)

        Synopsis
        -----
        Sets the end time of the animation for the u parameter.

        Returns:
        -----
        None

        Parameters:
        -----
        end: MTime
        	[in] -> the new end time


        '''
        pass

    def uTimeStart(self, ReturnStatus: MFnMotionPath.MStatus): 
        '''
        uTimeStart(self, ReturnStatus: MFnMotionPath.MStatus) -> MTime

        Synopsis
        -----
        Returns the start time of the animation for the u parameter.

        Returns: 
        ----- 
        The starting time

        Parameters:
        -----
        ReturnStatus: MFnMotionPath.MStatus
        	[out] -> Status Code


        '''
        pass

    def uTimeEnd(self, ReturnStatus: MFnMotionPath.MStatus): 
        '''
        uTimeEnd(self, ReturnStatus: MFnMotionPath.MStatus) -> MTime

        Synopsis
        -----
        Returns the end time of the animation for the u parameter.

        Returns: 
        ----- 
        The end time

        Parameters:
        -----
        ReturnStatus: MFnMotionPath.MStatus
        	[out] -> Status Code


        '''
        pass

    def numPositionMarkers(self, ReturnStatus: MFnMotionPath.MStatus): 
        '''
        numPositionMarkers(self, ReturnStatus: MFnMotionPath.MStatus) -> int

        Synopsis
        -----
        Returns the number of position markers on this motion path.

        Returns: 
        ----- 
        The number of markers

        Parameters:
        -----
        ReturnStatus: MFnMotionPath.MStatus
        	[out] -> Status Code


        '''
        pass

    def getPositionMarker(self, markerNum: int,
                        ReturnStatus: MFnMotionPath.MStatus): 
        '''
        getPositionMarker(self, markerNum: int,
                        ReturnStatus: MFnMotionPath.MStatus) -> MObject

        Synopsis
        -----
        Gets the position marker where markerNum is the order in which
        the marker was created.

        Returns: 
        ----- 
        The position marker

        Parameters:
        -----
        markerNum: int
        	[in] -> The number of the marker 

        ReturnStatus: MFnMotionPath.MStatus
        	[out] -> Status Code


        '''
        pass

    def numOrientationMarkers(self, ReturnStatus: MFnMotionPath.MStatus): 
        '''
        numOrientationMarkers(self, ReturnStatus: MFnMotionPath.MStatus) -> int

        Synopsis
        -----
        Returns the number of orientation markers on this motion path.

        Returns: 
        ----- 
        The number of markers

        Parameters:
        -----
        ReturnStatus: MFnMotionPath.MStatus
        	[out] -> Status Code


        '''
        pass

    def getOrientationMarker(self, markerNum: int,
                        ReturnStatus: MFnMotionPath.MStatus): 
        '''
        getOrientationMarker(self, markerNum: int,
                        ReturnStatus: MFnMotionPath.MStatus) -> MObject

        Synopsis
        -----
        Gets the orientation marker where markerNum is the order in which
        the marker was created.

        Returns: 
        ----- 
        The orientation marker

        Parameters:
        -----
        markerNum: int
        	[in] -> The number of the marker 

        ReturnStatus: MFnMotionPath.MStatus
        	[out] -> Status Code


        '''
        pass

class Axis:
    '''Available axes. 
    Non-functional class.  Values for this enum:
    kXaxis
    kYaxis
    kZaxis
    '''

    def __init__(self):
        pass

    def kXaxis(self):
        '''This is an enum of Axis.
        - Description:  
        - Value: 0
        '''
        pass

    def kYaxis(self):
        '''This is an enum of Axis.
        - Description:  
        - Value: 1
        '''
        pass

    def kZaxis(self):
        '''This is an enum of Axis.
        - Description:  
        - Value: 2
        '''
        pass

class MFnSkinCluster:
    '''skinCluster function set
MFnSkinCluster is the function set for skinClusters. SkinCluster nodes are
created during a smooth bindSkin. The purpose of the skinCluster
is to store a weight per influence object for each component of
each geometry that is deformed. Influence objects can be joints
or any transform.
Note that unlike most deformers, a skinCluster node can deform
only a single geometry. Therefore, if additional geometries are
added to the skinCluster set, they will be ignored.
This function set provides methods for getting and setting
weights on skin cluster nodes. It parent class,
MFnGeometryFilter provides methods for accessing the skin cluster's input and
output geometry.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kSkinClusterFilter.Reimplemented from MFnGeometryFilter.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> staticchar*

        Synopsis
        -----
        Returns the name of this class.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def getWeights(self, path: MDagPath,
                        components: MObject,
                        influenceIndex: int,
                        weights: MDoubleArray): 
        '''
        getWeights(self, path: MDagPath,
                        components: MObject,
                        influenceIndex: int,
                        weights: MDoubleArray)

        Synopsis
        -----
        Gets the skinCluster weights for the influence object for the
        specified components of the object whose dagPath is specified.
        Note that if some of components are not deformed by the
        skinCluster, zeros will be returned as the weights. For example,
        on periodic nurbs surfaces, some of the cvs enforce the
        periodicity of the surface. There is no weight data for these
        components. They do not get deformed since their position is
        automatically maintained by the nurb so that the periodicity of
        the surface will not be lost. Zeros will be returned for such
        components.The influence object is specified using the physical
        (non-sparse) index of the influence object. This corresponds to
        the order the influences are returned by the influenceObjects
        method.The length of the returned array will be equal to the
        number of specified components. The values in the returned array
        will be ordered in the same order as the input components.

        Returns:
        -----
        None

        Parameters:
        -----
        path: MDagPath
        	[in] -> path to object deformed by the skinCluster 

        components: MObject
        	[in] -> components to return weights for 

        influenceIndex: int
        	[in] -> physical index of influence object 

        weights: MDoubleArray
        	[out] -> weight values


        '''
        pass

    @overload
    def getWeights(self, path: MDagPath,
                        components: MObject,
                        weights: MDoubleArray,
                        influenceCount: int): 
        '''
        getWeights(self, path: MDagPath,
                        components: MObject,
                        weights: MDoubleArray,
                        influenceCount: int)

        Synopsis
        -----
        Gets the skinCluster weights for all influenceObjects for the
        specified components of the object whose dagPath is specified.
        Returns the weights in an array of size number of components x
        number of influenceObjects. The array elements are ordered by
        components: i.e. all of the weight values for the first component
        first, followed by all the weight values for the next component,
        and so on. For the first component, the weights are ordered by
        influence object in the same order that is returned by the
        MFnSkinCluster::influenceObjects method.The number of influence
        objects is returned in influenceCount.

        Returns:
        -----
        None

        Parameters:
        -----
        path: MDagPath
        	[in] -> path to object deformed by the skinCluster 

        components: MObject
        	[in] -> components to return weights for 

        weights: MDoubleArray
        	[out] -> weight values returned (one per component, per influence) 

        influenceCount: int
        	[out] -> count of influence objects


        '''
        pass

    @overload
    def getWeights(self, path: MDagPath,
                        components: MObject,
                        influenceIndices: MIntArray,
                        weights: MDoubleArray): 
        '''
        getWeights(self, path: MDagPath,
                        components: MObject,
                        influenceIndices: MIntArray,
                        weights: MDoubleArray)

        Synopsis
        -----
        Gets the skinCluster weights for the influence objects for the
        specified components of the object whose dagPath is specified.
        Returns the weights in an array of size number of components x
        number of influence objects. The array elements are ordered by
        components: i.e. all of the weight values for the first component
        first, followed by all the weight values for the next component,
        and so on. For the first component, the weights are ordered by
        influence object in the same order as in influenceIndices.

        Returns:
        -----
        None

        Parameters:
        -----
        path: MDagPath
        	[in] -> path to object deformed by the skinCluster 

        components: MObject
        	[in] -> components to return weights for 

        influenceIndices: MIntArray
        	[in] -> indices of influence objects to get 

        weights: MDoubleArray
        	[out] -> weight values returned (one per component, per influence)


        '''
        pass

    @overload
    def setWeights(self, path: MDagPath,
                        components: MObject,
                        influenceIndex: int,
                        value: double,
                        normalize: bool,
                        oldValues: MDoubleArray): 
        '''
        setWeights(self, path: MDagPath,
                        components: MObject,
                        influenceIndex: int,
                        value: double,
                        normalize: bool,
                        oldValues: MDoubleArray)

        Synopsis
        -----
        Sets the skinCluster weight for the influence object on the
        specified components of the object whose dagPath is specified.
        The influence is specified using the physical (non-sparse) index
        of the influence object. This corresponds to the order the
        influences are returned by the influenceObjects method.In order
        to undo the setWeight operation, it is necessary to save the
        oldValues array and call setWeight with the oldValues array at
        the time of undo. The number of oldValues returned will be of
        size number of specified components x the total number of
        influence objects. The values in the oldValues array will be
        ordered with first the all the values for the first component,
        then all the values for the next, and so on.Note that unlike most
        deformers, a skinCluster node can deform only a single geometry.
        Therefore, if additional geometries are added to the skinCluster
        set, they will be ignored, and weights cannot be set for the
        additional geometry.

        Returns:
        -----
        None

        Parameters:
        -----
        path: MDagPath
        	[in] -> path to object deformed by the skinCluster 

        components: MObject
        	[in] -> components to be weighted 

        influenceIndex: int
        	[in] -> physical index of influence object for the weight 

        value: double
        	[in] -> weight value 

        normalize: bool
        	[in] -> whether or not to normalize weights on other influence objects 

        oldValues: MDoubleArray
        	[in] -> previous weight values, for undo


        '''
        pass

    @overload
    def setWeights(self, path: MDagPath,
                        components: MObject,
                        influenceIndices: MIntArray,
                        values: MDoubleArray,
                        normalize: bool,
                        oldValues: MDoubleArray): 
        '''
        setWeights(self, path: MDagPath,
                        components: MObject,
                        influenceIndices: MIntArray,
                        values: MDoubleArray,
                        normalize: bool,
                        oldValues: MDoubleArray)

        Synopsis
        -----
        Sets the skinCluster weight on the specified components of the
        object whose dagPath is specified for the influence objects
        corresponding to the specified influence indices. The influence
        is specified using the physical (non-sparse) index of the
        influence object. This corresponds to the order the influences
        are returned by the influenceObjects method.If you want to set
        the same values on all of the specified components, the number of
        values in the values array should equal the number of indices in
        the influence indices array. If you want to specify a unique
        value for each component, the number of values in the values
        array should equal the number of components x the number of
        indices in the influence indices array. The ordering of the
        values array should be such that first all the values for the
        first component are listed, then the second, and so on. For
        example, if you want to set the weights for three components for
        influences 7 and 10, the influence array would contain [7,10],
        and the values array would contain: [component#1 weight for
        influence 7, component #1 weight for influence 10, component#2
        weight for influence 7, component#2 weight for influence 10,
        ...].In order to undo the setWeights operation, it is necessary
        to save the oldValues array and call setWeights with the
        oldValues array at the time of undo. The number of oldValues
        returned will be of size number of components x total number of
        influence objects. The values in the oldValues array will be
        ordered with first the all the values for the first component,
        then all the values for the next, and so on.Note that unlike most
        deformers, a skinCluster node can deform only a single geometry.
        Therefore, if additional geometries are added to the skinCluster
        set, they will be ignored, and weights cannot be set for the
        additional geometry.

        Returns:
        -----
        None

        Parameters:
        -----
        path: MDagPath
        	[in] -> path to object deformed by the skinCluster 

        components: MObject
        	[in] -> components to be weighted 

        influenceIndices: MIntArray
        	[in] -> physical indices of influence objects to set 

        values: MDoubleArray
        	[in] -> weight values 

        normalize: bool
        	[in] -> whether or not to normalize weights on other influence objects 

        oldValues: MDoubleArray
        	[in] -> previous weight values, for undo


        '''
        pass

    @overload
    def getPointsAffectedByInfluence(self, path: MDagPath,
                        result: MSelectionList,
                        weights: MDoubleArray): 
        '''
        getPointsAffectedByInfluence(self, path: MDagPath,
                        result: MSelectionList,
                        weights: MDoubleArray)

        Synopsis
        -----
        During deformation, the skinCluster algorithm is applied for a
        given influence object on all points in the deformer's set whose
        weights are non-zero. This method allows the user to query the
        non-zero weights for a particular influence object.Returns a
        selection list containing the dag path and the components that
        are affected by the specified influence object. To retrieve the
        components from the returned MSelectionList, use
        MSelectionList::getDagPath. Also returns the corresponding
        weights for the components. If no components are weighted for a
        specified influence, the resulting selection list will be empty.

        Returns:
        -----
        None

        Parameters:
        -----
        path: MDagPath
        	[in] -> path of the influence object 

        result: MSelectionList
        	[out] -> selection list of components affected by the influence object for this skinCluster (return) 

        weights: MDoubleArray
        	[out] -> weights for the affected components (return)


        '''
        pass

    def indexForInfluenceObject(self, mpath: MDagPath,
                        ReturnStatus: MFnSkinCluster.MStatus): 
        '''
        indexForInfluenceObject(self, mpath: MDagPath,
                        ReturnStatus: MFnSkinCluster.MStatus) -> int

        Synopsis
        -----
        Returns the logical index of the matrix array attribute where the
        specified influence object is attached.

        Returns: 
        ----- 
        The logical index of the influence object

        Parameters:
        -----
        mpath: MDagPath
        	[in] -> path of the influence object 

        ReturnStatus: MFnSkinCluster.MStatus
        	[out] -> return status


        '''
        pass

    def influenceObjects(self, paths: MDagPathArray,
                        ReturnStatus: MFnSkinCluster.MStatus): 
        '''
        influenceObjects(self, paths: MDagPathArray,
                        ReturnStatus: MFnSkinCluster.MStatus) -> int

        Synopsis
        -----
        Returns an array of paths to the influence objects for the
        skinCluster.

        Returns: 
        ----- 
        The number of influence objects

        Parameters:
        -----
        paths: MDagPathArray
        	[in] -> influence objects 

        ReturnStatus: MFnSkinCluster.MStatus
        	[out] -> return status


        '''
        pass

    @overload
    def getWeights(self, path: MDagPath,
                        components: MObject,
                        influenceIndex: int,
                        weights: MFloatArray): 
        '''
        getWeights(self, path: MDagPath,
                        components: MObject,
                        influenceIndex: int,
                        weights: MFloatArray)

        Synopsis
        -----
        This method is obsolete. Maya's skinCluster nodes store their
        weights as doubles. This method has been replaced by one which
        uses doubles instead of floats. This method only exists for
        backwards-compilability of old plug-in code.

        Returns:
        -----
        None

        Parameters:
        -----
        path: MDagPath
        	[in] -> path to object deformed by the skinCluster 

        components: MObject
        	[in] -> components to return weights for 

        influenceIndex: int
        	[in] -> index of influence object 

        weights: MFloatArray
        	[out] -> weight values


        '''
        pass

    @overload
    def getWeights(self, path: MDagPath,
                        components: MObject,
                        weights: MFloatArray,
                        influenceCount: int): 
        '''
        getWeights(self, path: MDagPath,
                        components: MObject,
                        weights: MFloatArray,
                        influenceCount: int)

        Synopsis
        -----
        This method is obsolete. Maya's skinCluster nodes store their
        weights as doubles. This method has been replaced by one which
        uses doubles instead of floats. This method only exists for
        backwards-compilability of old plug-in code.

        Returns:
        -----
        None

        Parameters:
        -----
        path: MDagPath
        	[in] -> path to object deformed by the skinCluster 

        components: MObject
        	[in] -> components to return weights for 

        weights: MFloatArray
        	[out] -> weight values returned (one per component, per influence) 

        influenceCount: int
        	[out] -> count of influence objects


        '''
        pass

    @overload
    def setWeights(self, path: MDagPath,
                        components: MObject,
                        influenceIndex: int,
                        value: float,
                        normalize: bool,
                        oldValues: MFloatArray): 
        '''
        setWeights(self, path: MDagPath,
                        components: MObject,
                        influenceIndex: int,
                        value: float,
                        normalize: bool,
                        oldValues: MFloatArray)

        Synopsis
        -----
        This method is obsolete. Maya's skinCluster nodes store their
        weights as doubles. This method has been replaced by one which
        uses doubles instead of floats. This method only exists for
        backwards-compilability of old plug-in code.

        Returns:
        -----
        None

        Parameters:
        -----
        path: MDagPath
        	[in] -> path to object deformed by the skinCluster 

        components: MObject
        	[in] -> components to be weighted 

        influenceIndex: int
        	[in] -> index of influence object for the weight 

        value: float
        	[in] -> weight value 

        normalize: bool
        	[in] -> whether or not to normalize weights on other influence objects 

        oldValues: MFloatArray
        	[in] -> previous weight values, for undo


        '''
        pass

    @overload
    def setWeights(self, path: MDagPath,
                        components: MObject,
                        influenceIndices: MIntArray,
                        values: MFloatArray,
                        normalize: bool,
                        oldValues: MFloatArray): 
        '''
        setWeights(self, path: MDagPath,
                        components: MObject,
                        influenceIndices: MIntArray,
                        values: MFloatArray,
                        normalize: bool,
                        oldValues: MFloatArray)

        Synopsis
        -----
        This method is obsolete. Maya's skinCluster nodes store their
        weights as doubles. This method has been replaced by one which
        uses doubles instead of floats. This method only exists for
        backwards-compilability of old plug-in code.

        Returns:
        -----
        None

        Parameters:
        -----
        path: MDagPath
        	[in] -> path to object deformed by the skinCluster 

        components: MObject
        	[in] -> components to be weighted 

        influenceIndices: MIntArray
        	[in] -> indices of influence objects to set 

        values: MFloatArray
        	[in] -> weight values 

        normalize: bool
        	[in] -> whether or not to normalize weights on other influence objects 

        oldValues: MFloatArray
        	[in] -> previous weight values, for undo


        '''
        pass

    @overload
    def getPointsAffectedByInfluence(self, path: MDagPath,
                        result: MSelectionList,
                        weights: MFloatArray): 
        '''
        getPointsAffectedByInfluence(self, path: MDagPath,
                        result: MSelectionList,
                        weights: MFloatArray)

        Synopsis
        -----
        This method is obsolete. Maya's skinCluster nodes store their
        weights as doubles. This method has been replaced by one which
        uses doubles instead of floats. This method only exists for
        backwards-compilability of old plug-in code.

        Returns:
        -----
        None

        Parameters:
        -----
        path: MDagPath
        	[in] -> path of the influence object 

        result: MSelectionList
        	[out] -> selection list of components affected by the influence object for this skinCluster (return) 

        weights: MFloatArray
        	[out] -> weights for the affected components (return)


        '''
        pass

    def getBlendWeights(self, path: MDagPath,
                        components: MObject,
                        weights: MDoubleArray): 
        '''
        getBlendWeights(self, path: MDagPath,
                        components: MObject,
                        weights: MDoubleArray)

        Synopsis
        -----
        This method returns weights from skinCluster's blend weight
        array. These weights are used to determine the blending between
        classical linear skinning and dual quaternion bases skinning on a
        per vertex basis. The function returns the weights associated
        with the components passed. The components are defined on the
        object whose dagPath is specified.

        Returns:
        -----
        None

        Parameters:
        -----
        path: MDagPath
        	[in] -> path to object deformed by the skinCluster 

        components: MObject
        	[in] -> the components to return weights for 

        weights: MDoubleArray
        	[out] -> the weight values returned (one per component in the order given)


        '''
        pass

    def setBlendWeights(self, path: MDagPath,
                        components: MObject,
                        weights: MDoubleArray): 
        '''
        setBlendWeights(self, path: MDagPath,
                        components: MObject,
                        weights: MDoubleArray)

        Synopsis
        -----
        This method sets weights in skinCluster's blend weight array.
        These weights are used to determine the blending between
        classical linear skinning and dual quaternion bases skinning on a
        per vertex basis. The function sets the weights for the given
        components of the object whose dagPath is specified. The array
        size should match the number of components passed. Failing this,
        it will set the smaller of the two.

        Returns:
        -----
        None

        Parameters:
        -----
        path: MDagPath
        	[in] -> path to object deformed by the skinCluster 

        components: MObject
        	[in] -> the components list for the new weight values 

        weights: MDoubleArray
        	[out] -> the weight values (one per component in the order given)


        '''
        pass

class MFnWeightGeometryFilter:
    '''Weight geometry filter function set.
MFnWeightGeometryFilter is the function set for weight geometry filters. Weight geometry
filter nodes include clusters, cluster flexors, and user-defined
deformers derived from
MPxDeformerNode. The purpose of the weight geometry filter is to store the
weights for each component of each geometry that is deformed. The
weight geometry filter is independent of any algorithm that
calculates a deformation based on the component weight values.
Clusters, cluster flexors, and user-defined deformers each have
their own algorithm to determine the deformation based on the
component weights.
This function set provides methods for getting and setting
weights on weight geometry filter nodes. In addition to getting
and settings weights on components, this class provides methods
for accessing the weight geometry filter's input and output
geometry through its parent class,
MFnGeometryFilter.
When getting and setting weights on components, it is more
efficient to use the methods that take a plug index. The plug
index is a sparse array index, and is the same index used in MEL
scripts to index into an array of plugs.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kWeightGeometryFilt.Reimplemented from MFnGeometryFilter.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> staticchar*

        Synopsis
        -----
        Returns the name of this class.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def getWeights(self, index: int,
                        components: MObject,
                        weights: MFloatArray): 
        '''
        getWeights(self, index: int,
                        components: MObject,
                        weights: MFloatArray)

        Synopsis
        -----
        Gets the weights of the components that correspond to the
        geometry at the specified plug index. The relationship between
        the weights and the components can be determined by iterating
        through the components using the MItGeometry iterator. The
        iterator iterates through the components in the same order as the
        weights array.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> the plug index corresponding to the shape that has the components 

        components: MObject
        	[out] -> the components whose weights are requested 

        weights: MFloatArray
        	[out] -> the weight values of the components


        '''
        pass

    @overload
    def getWeights(self, path: MDagPath,
                        components: MObject,
                        weights: MFloatArray): 
        '''
        getWeights(self, path: MDagPath,
                        components: MObject,
                        weights: MFloatArray)

        Synopsis
        -----
        Gets the weights of the components that correspond to the
        geometry whose DAG path is specified. If the plug index is
        already known, it is more efficient to call the other getWeights
        method than this one. This getWeights method calls
        indexForOutputShape internally to find the plug index.The
        relationship between the weights and the components can be
        determined by iterating through the components using the
        MItGeometry iterator. The iterator iterates through the
        components in the same order as the weights array.

        Returns:
        -----
        None

        Parameters:
        -----
        path: MDagPath
        	[in] -> the path of the DAG object that has the components 

        components: MObject
        	[in] -> the components whose weights are requested 

        weights: MFloatArray
        	[out] -> the weight values of the components


        '''
        pass

    @overload
    def setWeight(self, path: MDagPath,
                        index: int,
                        components: MObject,
                        weight: float,
                        oldValues: MFloatArray): 
        '''
        setWeight(self, path: MDagPath,
                        index: int,
                        components: MObject,
                        weight: float,
                        oldValues: MFloatArray)

        Synopsis
        -----
        Sets the weights of the specified components of the object whose
        DAG path is specified. In order to undo the setWeight operation,
        it is necessary to save the oldValues array and call setWeight
        with the oldValues array at the time of undo.

        Returns:
        -----
        None

        Parameters:
        -----
        path: MDagPath
        	[in] -> the DAG path for the object whose components' weights are being set 

        index: int
        	[in] -> the plug index for the specified shape 

        components: MObject
        	[in] -> the components of the object 

        weight: float
        	[in] -> weight value for the components 

        oldValues: MFloatArray
        	[in] -> an array of old values for the components


        '''
        pass

    @overload
    def setWeight(self, path: MDagPath,
                        components: MObject,
                        weight: float,
                        oldValues: MFloatArray): 
        '''
        setWeight(self, path: MDagPath,
                        components: MObject,
                        weight: float,
                        oldValues: MFloatArray)

        Synopsis
        -----
        Sets the weights of the specified components of the object whose
        DAG path is specified. If the plug index is already known, it is
        more efficient to call the corresponding setWeight method that
        takes a plugIndex. This setWeight method is a convenience method
        which calls indexForOutputShape internally to find the plug
        index.In order to undo the setWeight operation, it is necessary
        to save the oldValues array and call setWeight with the oldValues
        array at the time of undo.

        Returns:
        -----
        None

        Parameters:
        -----
        path: MDagPath
        	[in] -> the DAG path for the object whose components' weights are being set 

        components: MObject
        	[in] -> the components of the object 

        weight: float
        	[in] -> weight value for the components 

        oldValues: MFloatArray
        	[in] -> an array of old values for the components


        '''
        pass

    @overload
    def setWeight(self, path: MDagPath,
                        index: int,
                        components: MObject,
                        values: MFloatArray): 
        '''
        setWeight(self, path: MDagPath,
                        index: int,
                        components: MObject,
                        values: MFloatArray)

        Synopsis
        -----
        Sets the weights of the specified components of the object whose
        DAG path is specified. This method is useful in conjunction with
        the setWeight methods that return an oldValues array. This method
        can be called with those oldValues to restore the weights to the
        previous values.

        Returns:
        -----
        None

        Parameters:
        -----
        path: MDagPath
        	[in] -> the DAG path for the object whose components' weights are being set 

        index: int
        	[in] -> the plug index for the specified shape 

        components: MObject
        	[in] -> the components of the object 

        values: MFloatArray
        	[in] -> the value array of the components


        '''
        pass

    @overload
    def setWeight(self, path: MDagPath,
                        components: MObject,
                        values: MFloatArray): 
        '''
        setWeight(self, path: MDagPath,
                        components: MObject,
                        values: MFloatArray)

        Synopsis
        -----
        Sets the weights of the specified components of the object whose
        DAG path is specified. This method is useful in conjunction with
        the setWeight methods that return an oldValues array. This method
        can be called with those oldValues to restore the weights to the
        previous values.If the plug index is already known, it is more
        efficient to call the corresponding setWeight method that takes a
        plugIndex. This setWeight method is a convenience method which
        calls indexForOutputShape internally to find the plug index.

        Returns:
        -----
        None

        Parameters:
        -----
        path: MDagPath
        	[in] -> the DAG path for the object whose components' weights are being set 

        components: MObject
        	[in] -> the components of the object 

        values: MFloatArray
        	[in] -> the value array of the components


        '''
        pass

    def weightPlugStrings(self, list: MSelectionList,
                        ReturnStatus: MFnWeightGeometryFilter.MStatus): 
        '''
        weightPlugStrings(self, list: MSelectionList,
                        ReturnStatus: MFnWeightGeometryFilter.MStatus) -> MString

        Synopsis
        -----
        Sets the plugStrings argument to be a string (separated by
        spaces) containing the names of the plugs on this node that
        correspond to the components in the selection list. The method
        can be useful in conjunction with setting keys on a number of
        plugs. The operation will fail if none of the items in the
        selection list correspond to components weighted by this cluster.

        Returns: 
        ----- 
        A string containing the names of the plugs on this node that
        correspond to the components in the selection list

        Parameters:
        -----
        list: MSelectionList
        	[in] -> selection list that contains components 

        ReturnStatus: MFnWeightGeometryFilter.MStatus
        	[out] -> Status code


        '''
        pass

    def getWeightPlugStrings(self, list: MSelectionList,
                        plugStringArray: MStringArray): 
        '''
        getWeightPlugStrings(self, list: MSelectionList,
                        plugStringArray: MStringArray)

        Synopsis
        -----
        Set the plugStringArray argument to contain the names of the
        plugs on this node that correspond to the components in the
        selection list. The operation will fail if none of the items in
        the selection list correspond to components weighted by this
        cluster.

        Returns:
        -----
        None

        Parameters:
        -----
        list: MSelectionList
        	[in] -> selection list that contains components 

        plugStringArray: MStringArray
        	[out] -> string array containing the names of the plugs on this node that correspond to the components in the selection list; each of the plugs is put in a separate string


        '''
        pass

    def getEnvelopeWeights(self, multiIndex: int,
                        weights: MFloatArray): 
        '''
        getEnvelopeWeights(self, multiIndex: int,
                        weights: MFloatArray)

        Synopsis
        -----
        Introduced in 2024.1 Gets the weights the deformer uses for the
        geometry at the specified plug index.The weights are the
        combination of painted weights and falloff weights. The number of
        weights is equal to the number of affected verts of the
        indexMapper of the deformer. (The indexMapper can be retrieved
        with the MFnGeometryFilter::getIndexMapper function)

        Returns:
        -----
        None

        Parameters:
        -----
        multiIndex: int
        	[in] -> 

        weights: MFloatArray
        	[out] -> 


        '''
        pass

class MFnWireDeformer:
    '''wire deformer function set
MFnWireDeformer is the function set for wire deformers. Wire deformers modify
geometry based on its proximity to controlling wire curves. As
the wire curves are modified, the parts of the geometry close to
the curve will follow.
The wire deformer is actually a small network of dependency nodes
in the dependency graph. This function set is provided to make
manipulation of the network easier. The main deformer node should
be given to this function set as its object.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kWire.Reimplemented from MFnDependencyNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def className(self): 
        '''
        className(self) -> char*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnWireDeformer".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def create(self, ReturnStatus: MFnWireDeformer.MStatus): 
        '''
        create(self, ReturnStatus: MFnWireDeformer.MStatus) -> MObject

        Synopsis
        -----
        Creates a new wire deformer. This function set's object is set to
        be the new wire deformer node.

        Returns: 
        ----- 
        Returns a handle to the new deformer

        Parameters:
        -----
        ReturnStatus: MFnWireDeformer.MStatus
        	[out] -> return status


        '''
        pass

    def addGeometry(self, object: MObject): 
        '''
        addGeometry(self, object: MObject)

        Synopsis
        -----
        Adds a piece of geometry to the deformation. After adding new
        geometry to the deformation. The new geometry will then be
        deformed by the existing wires.

        Returns:
        -----
        None

        Parameters:
        -----
        object: MObject
        	[in] -> the geometry


        '''
        pass

    def removeGeometry(self, object: MObject): 
        '''
        removeGeometry(self, object: MObject)

        Synopsis
        -----
        Removes a piece of geometry from the deformation.

        Returns:
        -----
        None

        Parameters:
        -----
        object: MObject
        	[in] -> the geometry


        '''
        pass

    def getAffectedGeometry(self, objects: MObjectArray): 
        '''
        getAffectedGeometry(self, objects: MObjectArray)

        Synopsis
        -----
        The geometry affected by this deformer is packed into the
        provided list of MObjects. Each of the MObjects will be a DAG
        node that has geometry.

        Returns:
        -----
        None

        Parameters:
        -----
        objects: MObjectArray
        	[out] -> storage for the returned array


        '''
        pass

    def numWires(self, ReturnStatus: MFnWireDeformer.MStatus): 
        '''
        numWires(self, ReturnStatus: MFnWireDeformer.MStatus) -> int

        Synopsis
        -----
        returns the number of wire curves connected to this deformer.

        Returns: 
        ----- 
        The number of wires

        Parameters:
        -----
        ReturnStatus: MFnWireDeformer.MStatus
        	[out] -> return status


        '''
        pass

    def addWire(self, object: MObject): 
        '''
        addWire(self, object: MObject)

        Synopsis
        -----
        Adds a new wire curve to the deformation.

        Returns:
        -----
        None

        Parameters:
        -----
        object: MObject
        	[in] -> the new wire


        '''
        pass

    def wire(self, wireIndex: int,
                        ReturnStatus: MFnWireDeformer.MStatus): 
        '''
        wire(self, wireIndex: int,
                        ReturnStatus: MFnWireDeformer.MStatus) -> MObject

        Synopsis
        -----
        Return the wire at the given index. The returned object will be a
        nurbs curve shape suitable for use with the MFnNurbsCurve
        function set.

        Returns: 
        ----- 
        A handle to the given wire curve

        Parameters:
        -----
        wireIndex: int
        	[in] -> index of wire to return 

        ReturnStatus: MFnWireDeformer.MStatus
        	[out] -> return status


        '''
        pass

    def wireDropOffDistance(self, wireIndex: int,
                        ReturnStatus: MFnWireDeformer.MStatus): 
        '''
        wireDropOffDistance(self, wireIndex: int,
                        ReturnStatus: MFnWireDeformer.MStatus) -> float

        Synopsis
        -----
        Return the drop off distance of the wire at the given index.
        Increasing this value will give the wire a greater area of
        influence.

        Returns: 
        ----- 
        The drop off distance

        Parameters:
        -----
        wireIndex: int
        	[in] -> index of wire to return the drop off distance for 

        ReturnStatus: MFnWireDeformer.MStatus
        	[out] -> return status


        '''
        pass

    def setWireDropOffDistance(self, wireIndex: int,
                        dropOff: float): 
        '''
        setWireDropOffDistance(self, wireIndex: int,
                        dropOff: float)

        Synopsis
        -----
        Sets the drop off distance of the wire at the given index.
        Increasing this value will give the wire a greater area of
        influence.

        Returns:
        -----
        None

        Parameters:
        -----
        wireIndex: int
        	[in] -> index of wire to set the drop off distance for 

        dropOff: float
        	[in] -> new drop off value


        '''
        pass

    def wireScale(self, wireIndex: int,
                        ReturnStatus: MFnWireDeformer.MStatus): 
        '''
        wireScale(self, wireIndex: int,
                        ReturnStatus: MFnWireDeformer.MStatus) -> float

        Synopsis
        -----
        Return the radial scale of the wire at the given index. The scale
        value affects how the wire modifies the geometry in its area of
        influence. A value of between 0.0 and 1.0 causes the wire to pull
        the surrounding geometry points towards itself. A value of
        greater than one causes the wire to repulse the geometry points
        around it. A value of exactly 1.0 causes the wire to neither pull
        nor push the points around it.The surrounding points will always
        deform with the wire, The scale factor just allows the points
        around the wire to be radially scaled closer to or further from
        the wire.

        Returns: 
        ----- 
        The radial scale value

        Parameters:
        -----
        wireIndex: int
        	[in] -> index of wire to return the scale value for 

        ReturnStatus: MFnWireDeformer.MStatus
        	[out] -> return status


        '''
        pass

    def setWireScale(self, wireIndex: int,
                        scale: float): 
        '''
        setWireScale(self, wireIndex: int,
                        scale: float)

        Synopsis
        -----
        Sets the radial scale value of the wire at the given index. The
        scale value affects how the wire modifies the geometry in its
        area of influence. A value of between 0.0 and 1.0 causes the wire
        to pull the surrounding geometry points towards itself. A value
        of greater than one causes the wire to repulse the geometry
        points around it. A value of exactly 1.0 causes the wire to
        neither pull nor push the points around it.The surrounding points
        will always deform with the wire, The scale factor just allows
        the points around the wire to be radially scaled closer to or
        further from the wire.

        Returns:
        -----
        None

        Parameters:
        -----
        wireIndex: int
        	[in] -> index of wire to set the drop off distance for 

        scale: float
        	[in] -> new scale value


        '''
        pass

    def holdingShape(self, wireIndex: int,
                        ReturnStatus: MFnWireDeformer.MStatus): 
        '''
        holdingShape(self, wireIndex: int,
                        ReturnStatus: MFnWireDeformer.MStatus) -> MObject

        Synopsis
        -----
        Returns the holding shape for the given wire. The holding shape
        may be a nurbs curve or a nurbs surface. If the given wire does
        not have a holding shape, then a null MObject handle will be
        returned.A holding shape pins down the deforming shapes when the
        associated wire is moved. One possible application is to use a
        curve to limit the area that a wire affects.

        Returns: 
        ----- 
        Return status

        Parameters:
        -----
        wireIndex: int
        	[in] -> index of wire to get the holding shape for 

        ReturnStatus: MFnWireDeformer.MStatus
        	[out] -> return status


        '''
        pass

    def setHoldingShape(self, wireIndex: int,
                        holdingShape: MObject): 
        '''
        setHoldingShape(self, wireIndex: int,
                        holdingShape: MObject)

        Synopsis
        -----
        Sets the holding shape for the given wire. The holding shape may
        be a nurbs curve or a nurbs surface.A holding shape pins down the
        deforming shapes when the associated wire is moved. One possible
        application is to use a curve to limit the area that a wire
        affects.

        Returns:
        -----
        None

        Parameters:
        -----
        wireIndex: int
        	[in] -> index of wire to set the holding shape for 

        holdingShape: MObject
        	[in] -> nurbs curve or surface to use as holding shape


        '''
        pass

    def envelope(self, ReturnStatus: MFnWireDeformer.MStatus): 
        '''
        envelope(self, ReturnStatus: MFnWireDeformer.MStatus) -> float

        Synopsis
        -----
        Returns the envelope for this deformer. The envelope is a scale
        factor that affects the dropoff distances of all wires that
        belong to this deformer.

        Returns: 
        ----- 
        The envelope value

        Parameters:
        -----
        ReturnStatus: MFnWireDeformer.MStatus
        	[in] -> return status


        '''
        pass

    def setEnvelope(self, envelope: float): 
        '''
        setEnvelope(self, envelope: float)

        Synopsis
        -----
        Sets the envelope for this deformer. The envelope is a scale
        factor that affects the dropoff distances of all wires that
        belong to this deformer.

        Returns:
        -----
        None

        Parameters:
        -----
        envelope: float
        	[in] -> envelope value


        '''
        pass

    def rotation(self, ReturnStatus: MFnWireDeformer.MStatus): 
        '''
        rotation(self, ReturnStatus: MFnWireDeformer.MStatus) -> float

        Synopsis
        -----
        Returns the rotation value for this deformer. The rotation value
        determines how much the tangency of the wire curve affects the
        deformation. When the rotation value is 0.0, the deformation will
        be linear. The geometry will pull straight towards the wire. When
        the rotation value is 1.0, the tangency of the wire curve is
        taken into effect. This will provide more natural deformations
        when the wire curve is twisted with respect to its original
        position. The surface will pull towards the wire in an arc rather
        than in a straight line.

        Returns: 
        ----- 
        The rotation value

        Parameters:
        -----
        ReturnStatus: MFnWireDeformer.MStatus
        	[out] -> return status


        '''
        pass

    def setRotation(self, rotation: float): 
        '''
        setRotation(self, rotation: float)

        Synopsis
        -----
        Sets the rotation value for this deformer. The rotation value
        determines how much the tangency of the wire curve affects the
        deformation. When the rotation value is 0.0, the deformation will
        be linear. The geometry will pull straight towards the wire. When
        the rotation value is 1.0, the tangency of the wire curve is
        taken into effect. This will provide more natural deformations
        when the wire curve is twisted with respect to its original
        position. The surface will pull towards the wire in an arc rather
        than in a straight line.

        Returns:
        -----
        None

        Parameters:
        -----
        rotation: float
        	[in] -> new rotation value


        '''
        pass

    def localIntensity(self, ReturnStatus: MFnWireDeformer.MStatus): 
        '''
        localIntensity(self, ReturnStatus: MFnWireDeformer.MStatus) -> float

        Synopsis
        -----
        Returns the local intensity for this wire deformer. The local
        intensity has an effect when two wire curves are positioned close
        to each other. Normally, only the most deformed of the two curves
        will affect the surface. When the local intensity is increased,
        the less deformed curve will start to pull the surface back
        towards itself.

        Returns: 
        ----- 
        The local intensity value

        Parameters:
        -----
        ReturnStatus: MFnWireDeformer.MStatus
        	[out] -> return status


        '''
        pass

    def setLocalIntensity(self, localIntensity: float): 
        '''
        setLocalIntensity(self, localIntensity: float)

        Synopsis
        -----
        Sets the local intensity for this wire deformer. The local
        intensity has an effect when two wire curves are positioned close
        to each other. Normally, only the most deformed of the two curves
        will affect the surface. When the local intensity is increased,
        the less deformed curve will start to pull the surface back
        towards itself.

        Returns:
        -----
        None

        Parameters:
        -----
        localIntensity: float
        	[in] -> New local intensity value


        '''
        pass

    def crossingEffect(self, ReturnStatus: MFnWireDeformer.MStatus): 
        '''
        crossingEffect(self, ReturnStatus: MFnWireDeformer.MStatus) -> float

        Synopsis
        -----
        Returns the crossing effect for this wire deformer. The crossing
        effect applies when two wire curves cross each other. Normally,
        the deformation is dampened so that the surface is only affected
        by the most deformed curve at the intersection point. When the
        crossing effect is increased, the effect of the wires becomes
        additive. So, the object will be deform more near crossing wires.

        Returns: 
        ----- 
        The crossing effect value

        Parameters:
        -----
        ReturnStatus: MFnWireDeformer.MStatus
        	[out] -> return status


        '''
        pass

    def setCrossingEffect(self, crossingEffect: float): 
        '''
        setCrossingEffect(self, crossingEffect: float)

        Synopsis
        -----
        Sets the crossing effect for this wire deformer. The crossing
        effect applies when two wire curves cross each other. Normally,
        the deformation is dampened so that the surface is only affected
        by the most deformed curve at the intersection point. When the
        crossing effect is increased, the effect of the wires becomes
        additive. So, the object will be deform more near crossing wires.

        Returns:
        -----
        None

        Parameters:
        -----
        crossingEffect: float
        	[in] -> New crossing effect value


        '''
        pass

    def numDropoffLocators(self, wireIndex: int,
                        ReturnStatus: MFnWireDeformer.MStatus): 
        '''
        numDropoffLocators(self, wireIndex: int,
                        ReturnStatus: MFnWireDeformer.MStatus) -> int

        Synopsis
        -----
        Returns the number of drop off locators. A drop off locator
        allows the modification the wire curve drop off distance at a
        specific point on the wire curve.

        Returns: 
        ----- 
        The number of drop off locators for the given curve

        Parameters:
        -----
        wireIndex: int
        	[in] -> the index of the wire curve to query 

        ReturnStatus: MFnWireDeformer.MStatus
        	[out] -> return status


        '''
        pass

    def setDropoffLocator(self, wireIndex: int,
                        locatorIndex: int,
                        param: float,
                        percentage: float): 
        '''
        setDropoffLocator(self, wireIndex: int,
                        locatorIndex: int,
                        param: float,
                        percentage: float)

        Synopsis
        -----
        Sets the parameters of a drop off locator. A drop off locator
        allows the modification the wire curve drop off distance at a
        specific point on the wire curve.

        Returns:
        -----
        None

        Parameters:
        -----
        wireIndex: int
        	[in] -> index of the wire curve 

        locatorIndex: int
        	[in] -> index of the locator on the given wire 

        param: float
        	[in] -> new param value along the curve at which to position the locator 

        percentage: float
        	[in] -> percentage of the drop off distance applied


        '''
        pass

    def getDropoffLocator(self, wireIndex: int,
                        locatorIndex: int,
                        param: float,
                        percentage: float): 
        '''
        getDropoffLocator(self, wireIndex: int,
                        locatorIndex: int,
                        param: float,
                        percentage: float)

        Synopsis
        -----
        Gets the parameters of a drop off locator. A drop off locator
        allows the modification the wire curve drop off distance at a
        specific point on the wire curve.

        Returns:
        -----
        None

        Parameters:
        -----
        wireIndex: int
        	[in] -> index of the wire curve 

        locatorIndex: int
        	[in] -> index of the locator on the given wire 

        param: float
        	[out] -> storage for the param value along the curve that the locator is positioned at 

        percentage: float
        	[out] -> storage for the percentage value of the locator


        '''
        pass

class MIkHandleGroup:
    '''IK handle groups.
Group class for ik handles. Each group has an associated solver
and priority. A single chain solver handle group has only one
handle in its group.
'''
    def __init__(self):
        pass


    def priority(self, ReturnStatus: MIkHandleGroup.MStatus): 
        '''
        priority(self, ReturnStatus: MIkHandleGroup.MStatus) -> int

        Synopsis
        -----
        Return the priority value of this handle group.

        Returns: 
        ----- 
        The priority

        Parameters:
        -----
        ReturnStatus: MIkHandleGroup.MStatus
        	[out] -> Status code


        '''
        pass

    def solverID(self, ReturnStatus: MIkHandleGroup.MStatus): 
        '''
        solverID(self, ReturnStatus: MIkHandleGroup.MStatus) -> int

        Synopsis
        -----
        Return the solver id used by this handle group.

        Returns: 
        ----- 
        The solver id for this group

        Parameters:
        -----
        ReturnStatus: MIkHandleGroup.MStatus
        	[out] -> Status code


        '''
        pass

    def solverPriority(self, ReturnStatus: MIkHandleGroup.MStatus): 
        '''
        solverPriority(self, ReturnStatus: MIkHandleGroup.MStatus) -> int

        Synopsis
        -----
        return the priority of the solver used by this handle group.

        Returns: 
        ----- 
        The solver priority

        Parameters:
        -----
        ReturnStatus: MIkHandleGroup.MStatus
        	[out] -> Status code


        '''
        pass

    def setPriority(self, priority: int): 
        '''
        setPriority(self, priority: int)

        Synopsis
        -----
        Set the priority of this handle group.

        Returns:
        -----
        None

        Parameters:
        -----
        priority: int
        	[in] -> the priority value to set


        '''
        pass

    def setSolverID(self, id: int): 
        '''
        setSolverID(self, id: int)

        Synopsis
        -----
        Set the solver id for this handle group.

        Returns:
        -----
        None

        Parameters:
        -----
        id: int
        	[in] -> the id value to set


        '''
        pass

    def checkEffectorAtGoal(self, ReturnStatus: MIkHandleGroup.MStatus): 
        '''
        checkEffectorAtGoal(self, ReturnStatus: MIkHandleGroup.MStatus) -> bool

        Synopsis
        -----
        Determines whether the end-effector at the handle(goal) location.

        Returns: 
        ----- 
        true The end-effector is at the goal location  false The end-
        effector is not at the goal location

        Parameters:
        -----
        ReturnStatus: MIkHandleGroup.MStatus
        	[out] -> Status code


        '''
        pass

    def solve(self): 
        '''
        solve(self)

        Synopsis
        -----
        Do all ik solving steps for this group.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def dofCount(self, ReturnStatus: MIkHandleGroup.MStatus): 
        '''
        dofCount(self, ReturnStatus: MIkHandleGroup.MStatus) -> int

        Synopsis
        -----
        Return the total number of degrees of freedom of this handle
        group.

        Returns: 
        ----- 
        The total number of dofs

        Parameters:
        -----
        ReturnStatus: MIkHandleGroup.MStatus
        	[out] -> Status code


        '''
        pass

    def handleCount(self, ReturnStatus: MIkHandleGroup.MStatus): 
        '''
        handleCount(self, ReturnStatus: MIkHandleGroup.MStatus) -> int

        Synopsis
        -----
        Return the number of handles in the handle list for this group.

        Returns: 
        ----- 
        The number of handles

        Parameters:
        -----
        ReturnStatus: MIkHandleGroup.MStatus
        	[out] -> Status code


        '''
        pass

    def handle(self, ith: int,
                        ReturnStatus: MIkHandleGroup.MStatus): 
        '''
        handle(self, ith: int,
                        ReturnStatus: MIkHandleGroup.MStatus) -> MObject

        Synopsis
        -----
        Return the ith handle in the handle list for this group.

        Returns: 
        ----- 
        An MObject for the handle

        Parameters:
        -----
        ith: int
        	[in] -> the index of the handle 

        ReturnStatus: MIkHandleGroup.MStatus
        	[out] -> Status code


        '''
        pass

    def className(self): 
        '''
        className(self) -> char*

        Synopsis
        -----
        Returns the name of this class.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MIkSystem:
    '''Inverse kinematics (IK) system class.
This class provides an interface to the inverse kinematics (IK)
system. The ik system is used to set/query the global snapping
flag for handles, set/query the global solve flag for solvers,
and to find the ik solvers available in maya.
'''
    def __init__(self):
        pass


    def findSolver(self, name: MString,
                        ReturnStatus: MIkSystem.MStatus): 
        '''
        findSolver(self, name: MString,
                        ReturnStatus: MIkSystem.MStatus) -> MIkSystem.OPENMAYA_MAJOR_NAMESPACE_OPEN MObject

        Synopsis
        -----
        Returns the ik solver with the given name. If the solver cannot
        be found then a a null MObject and an error is returned.

        Returns: 
        ----- 
        The ik solver matching the given name

        Parameters:
        -----
        name: MString
        	[in] -> the name of the solver to find 

        ReturnStatus: MIkSystem.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def getSolvers(self, names: MStringArray): 
        '''
        getSolvers(self, names: MStringArray)

        Synopsis
        -----
        Get a list of the names for the solvers that are available in the
        system.

        Returns:
        -----
        None

        Parameters:
        -----
        names: MStringArray
        	[out] -> storage for the solver names


        '''
        pass

    def isGlobalSnap(self, ReturnStatus: MIkSystem.MStatus): 
        '''
        isGlobalSnap(self, ReturnStatus: MIkSystem.MStatus) -> bool

        Synopsis
        -----
        Determines whether global snapping is on. Turning on global
        snapping will turn on snapping for all ik handles.

        Returns: 
        ----- 
        true global snapping is on  false global snapping is off

        Parameters:
        -----
        ReturnStatus: MIkSystem.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def setGlobalSnap(self, isSnap: bool): 
        '''
        setGlobalSnap(self, isSnap: bool)

        Synopsis
        -----
        Turns global snapping on or off. Turning on global snapping will
        turn on snapping for all ik handles.

        Returns:
        -----
        None

        Parameters:
        -----
        isSnap: bool
        	[in] -> true turns global snapping on, false turns it off


        '''
        pass

    def isGlobalSolve(self, ReturnStatus: MIkSystem.MStatus): 
        '''
        isGlobalSolve(self, ReturnStatus: MIkSystem.MStatus) -> bool

        Synopsis
        -----
        Determines whether global solving is on.

        Returns:
        -----
        None

        Parameters:
        -----
        ReturnStatus: MIkSystem.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def setGlobalSolve(self, isSolve: bool): 
        '''
        setGlobalSolve(self, isSolve: bool)

        Synopsis
        -----
        Turns global solving on or off.

        Returns:
        -----
        None

        Parameters:
        -----
        isSolve: bool
        	[in] -> true turns global solving on, false turns it off


        '''
        pass

    def className(self): 
        '''
        className(self) -> char*

        Synopsis
        -----
        Returns the name of this class.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MItKeyframe:
    '''Keyframe Iterator.
Iterate over the keyframes of a particular Anim Curve Node, and
query and edit the keyframe to which the iterator points.
Determine the time and value of the keyframe, as well as the x,y
values and type of the tangent to the curve entering (in tangent)
and leaving (out tangent) the keyframe.
Set the time and value of the keyframe, and the type of the
tangents.
Anim Curves are implemented as Dependency Graph (DG) Nodes. Each
Node has multiple ordered and indexed keyframes.
Use the Keyframe Iterator to systematically visit, and query
and/or edit the keyframes of a Anim Curve Node.
Use the Keyframe Iterator in conjunction with the Anim Curve
Function Set (
MFnAnimCurve) to edit Anim Curve Nodes.
On creation the iterator is attached to a Anim Curve Node. The
iterator may be detached from its current Node and attached to
another Anim Curve Node using the
reset() method.
Though keyframes within a Node are ordered and indexed, the
iterator maintains the index of the current Node internally and
does not export it. Use the Anim Curve Function Set to access the
index for a keyframe. The index is zero-based. When an iterator
is first attached to a Node, either on creation or reset, the
index is set to zero. There is an overloaded version of the
reset() method which does not cause the iterator to change Nodes, but
merely resets the index.
Use the
next(),
reset() and
isDone() methods to perform iterations.
Use the specific query methods to determine the time, value and
tangent information for the keyframe under the iterator.
Use specific edit methods to set the time and value , as well as
the incoming and outgoing tangent type (
MItKeyframe::TangentType) of the keyframe under the iterator.
There is no method for setting the x,y value of either of the
tangents.
Setting the time of a keyframe will fail if the new time would
require a re-ordering of the keyframes. Use the Anim Curve
Functiion Set methods
MFnAnimCurve::remove() and MFnAnimCurve::addKeyFrame() to re-order the keyframes.
'''
    def __init__(self):
        pass


    @overload
    def reset(self, animCurveNode: MObject): 
        '''
        reset(self, animCurveNode: MObject)

        Synopsis
        -----
        Detaches the iterator from the current Anim Curve Node and
        attaches it to the given Node. Resets to the first keyframe
        (index = 0).

        Returns:
        -----
        None

        Parameters:
        -----
        animCurveNode: MObject
        	[in] -> New target Node for attachment to iterator


        '''
        pass

    @overload
    def reset(self): 
        '''
        reset(self)

        Synopsis
        -----
        Resets the keyframe index to 0 (first keyframe) on the Anim Curve
        Node to which the iterator is attached.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def next(self): 
        '''
        next(self)

        Synopsis
        -----
        Moves to the next keyframe on the Anim Curve Node to which the
        iterator is attached. Attempting to move beyond the last keyframe
        has no effect (and returns success).

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def isDone(self, ReturnStatus: MItKeyframe.MStatus): 
        '''
        isDone(self, ReturnStatus: MItKeyframe.MStatus) -> bool

        Synopsis
        -----
        Indicates that the iterator has moved beyond the last keyframe on
        the Anim Curve Node to which the iterator is attached. If
        isDone() returns true, attempting to access the curve via the
        iterator's time(), value() etc. methods will return an 'index out
        of range' error.

        Returns: 
        ----- 
        true Done  false Not done

        Parameters:
        -----
        ReturnStatus: MItKeyframe.MStatus
        	[out] -> Status Code (see below)


        '''
        pass

    def time(self, ReturnStatus: MItKeyframe.MStatus): 
        '''
        time(self, ReturnStatus: MItKeyframe.MStatus) -> MTime

        Synopsis
        -----
        Determines the time of the current keyframe.

        Returns: 
        ----- 
        Time (in seconds) of the current keyframe

        Parameters:
        -----
        ReturnStatus: MItKeyframe.MStatus
        	[out] -> Status Code (see below).


        '''
        pass

    def setTime(self, time: MTime): 
        '''
        setTime(self, time: MTime)

        Synopsis
        -----
        Sets the time of the current keyframe. This will fail if setting
        the time would require re-ordering of the keyframes.Tangents may
        be changed so that the curve remains monotonic with respect to
        time.

        Returns:
        -----
        None

        Parameters:
        -----
        time: MTime
        	[in] -> Time to which the current keyframe time is to be set.


        '''
        pass

    def value(self, ReturnStatus: MItKeyframe.MStatus): 
        '''
        value(self, ReturnStatus: MItKeyframe.MStatus) -> double

        Synopsis
        -----
        Determines the value of the current keyframe.

        Returns: 
        ----- 
        Value of the current keyframe

        Parameters:
        -----
        ReturnStatus: MItKeyframe.MStatus
        	[out] -> Status Code (see below).


        '''
        pass

    def setValue(self, value: double): 
        '''
        setValue(self, value: double)

        Synopsis
        -----
        Sets the value of the current keyframe.

        Returns:
        -----
        None

        Parameters:
        -----
        value: double
        	[in] -> Value to which the current keyframe time is to be set.


        '''
        pass

    def inTangentType(self, ReturnStatus: MItKeyframe.MStatus): 
        '''
        inTangentType(self, ReturnStatus: MItKeyframe.MStatus) -> MItKeyframe.MItKeyframe

        Synopsis
        -----
        Determines the type of the tangent to the curve entering the
        current keyframe.

        Returns: 
        ----- 
        Type of the tangent

        Parameters:
        -----
        ReturnStatus: MItKeyframe.MStatus
        	[out] -> Status Code (see below).


        '''
        pass

    def outTangentType(self, ReturnStatus: MItKeyframe.MStatus): 
        '''
        outTangentType(self, ReturnStatus: MItKeyframe.MStatus) -> MItKeyframe.MItKeyframe

        Synopsis
        -----
        Determines the type of the tangent to the curve leaving the
        current keyframe.

        Returns: 
        ----- 
        Type of the tangent

        Parameters:
        -----
        ReturnStatus: MItKeyframe.MStatus
        	[out] -> Status Code (see below).


        '''
        pass

    def setInTangentType(self, tangentType: MItKeyframe.TangentType): 
        '''
        setInTangentType(self, tangentType: MItKeyframe.TangentType)

        Synopsis
        -----
        Sets the type of the tangent to the curve entering the current
        keyframe.

        Returns:
        -----
        None

        Parameters:
        -----
        tangentType: MItKeyframe.TangentType
        	[in] -> Type to which the tangent is to be set


        '''
        pass

    def setOutTangentType(self, tangentType: MItKeyframe.TangentType): 
        '''
        setOutTangentType(self, tangentType: MItKeyframe.TangentType)

        Synopsis
        -----
        Sets the type of the tangent to the curve entering the current
        keyframe.

        Returns:
        -----
        None

        Parameters:
        -----
        tangentType: MItKeyframe.TangentType
        	[in] -> Type to which the tangent is to be set


        '''
        pass

    def getTangentOut(self, x: MItKeyframe.TangentValue,
                        y: MItKeyframe.TangentValue): 
        '''
        getTangentOut(self, x: MItKeyframe.TangentValue,
                        y: MItKeyframe.TangentValue)

        Synopsis
        -----
        Determines the x,y value of the tangent to the curve leaving the
        current keyframe.

        Returns:
        -----
        None

        Parameters:
        -----
        x: MItKeyframe.TangentValue
        	[out] -> Delta x of the slope of the tangent 

        y: MItKeyframe.TangentValue
        	[out] -> Delta y of the slope of the tangent


        '''
        pass

    def getTangentIn(self, x: MItKeyframe.TangentValue,
                        y: MItKeyframe.TangentValue): 
        '''
        getTangentIn(self, x: MItKeyframe.TangentValue,
                        y: MItKeyframe.TangentValue)

        Synopsis
        -----
        Determines the x,y value of the tangent to the curve entering the
        current keyframe.

        Returns:
        -----
        None

        Parameters:
        -----
        x: MItKeyframe.TangentValue
        	[out] -> Delta x of the slope of the tangent 

        y: MItKeyframe.TangentValue
        	[out] -> Delta y of the slope of the tangent


        '''
        pass

    def tangentsLocked(self, ReturnStatus: MItKeyframe.MStatus): 
        '''
        tangentsLocked(self, ReturnStatus: MItKeyframe.MStatus) -> bool

        Synopsis
        -----
        Determines whether the tangents are locked at this keyframe.

        Returns: 
        ----- 
        true if the tangents are locked  false if the tangents are not
        locked

        Parameters:
        -----
        ReturnStatus: MItKeyframe.MStatus
        	[out] -> Status Code (see below).


        '''
        pass

    def setTangentsLocked(self, locked: bool): 
        '''
        setTangentsLocked(self, locked: bool)

        Synopsis
        -----
        Lock or unlock the tangents at this keyframe.

        Returns:
        -----
        None

        Parameters:
        -----
        locked: bool
        	[in] -> true if the tangents are to be locked, false otherwise


        '''
        pass

    def className(self): 
        '''
        className(self) -> char*

        Synopsis
        -----
        Returns the name of this class.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class TangentType:
    '''Tangent types. 
    Non-functional class.  Values for this enum:
    kTangentGlobal
    kTangentFixed
    kTangentLinear
    kTangentFlat
    kTangentSmooth
    kTangentStep
    kTangentSlow
    kTangentFast
    kTangentClamped
    kTangentPlateau
    kTangentStepNext
    kTangentAuto
    kTangentAutoMix
    kTangentAutoEase
    kTangentAutoCustom
    '''

    def __init__(self):
        pass

    def kTangentGlobal(self):
        '''This is an enum of TangentType.
        - Description: Use the global tangent settings in Maya's 'Animation Preferences'. 
        - Value: 0
        '''
        pass

    def kTangentFixed(self):
        '''This is an enum of TangentType.
        - Description: Normally, if a key is moved tangent values will be adjusted to maintain their relationships to the surrounding keys (linear, smooth, etc). If a tangent is set to be fixed then it will not change when keys are moved but will retain its current value. 
        - Value: 1
        '''
        pass

    def kTangentLinear(self):
        '''This is an enum of TangentType.
        - Description: For an in tangent this sets it to point directly at the previous key. For an out tangent it points directly to the next key. This is used to create straight lines between keys. 
        - Value: 2
        '''
        pass

    def kTangentFlat(self):
        '''This is an enum of TangentType.
        - Description: The tangent is horizontal. 
        - Value: 3
        '''
        pass

    def kTangentSmooth(self):
        '''This is an enum of TangentType.
        - Description: The in and out tangents are colinear and set to provide a smooth transition from the key before to the key after. 
        - Value: 4
        '''
        pass

    def kTangentStep(self):
        '''This is an enum of TangentType.
        - Description: The key's value is maintained until the next key is reached whereupon it immediately jumps to the new key's value. 
        - Value: 5
        '''
        pass

    def kTangentSlow(self):
        '''This is an enum of TangentType.
        - Description: Slow tangent. 
        - Value: 6
        '''
        pass

    def kTangentFast(self):
        '''This is an enum of TangentType.
        - Description: Fast tangent. 
        - Value: 7
        '''
        pass

    def kTangentClamped(self):
        '''This is an enum of TangentType.
        - Description: Same as smooth except when two keys are very close together in which case the tangents between them are treated as linear. This corrects for slippage which is sometimes seen when spline tangents are used on keyframes which are close together. 
        - Value: 8
        '''
        pass

    def kTangentPlateau(self):
        '''This is an enum of TangentType.
        - Description: Similar to smooth except that minima and maxima between keyframes are flattened, if necessary, to prevent them overshooting their keys. 
        - Value: 9
        '''
        pass

    def kTangentStepNext(self):
        '''This is an enum of TangentType.
        - Description: Upon leaving the keyframe the value immediately jumps to that of the next keyframe and stays there. 
        - Value: 10
        '''
        pass

    def kTangentAuto(self):
        '''This is an enum of TangentType.
        - Description: The first and last keyframes will have flat tangents. Between, inner keyframes, the animation curve will not over shoot the keyframe values. 
        - Value: 11
        '''
        pass

    def kTangentAutoMix(self):
        '''This is an enum of TangentType.
        - Description: Introduced in 2022.0 2022.0:Introduced in this version. The first and last keyframes will have flat tangents. Between, inner keyframes, the animation curve will not over shoot the keyframe values, and use a linear interpolation to calculate the auto tangent. 
        - Value: 12
        '''
        pass

    def kTangentAutoEase(self):
        '''This is an enum of TangentType.
        - Description: Introduced in 2022.0 2022.0:Introduced in this version. The first and last keyframes will have flat tangents. Between, inner keyframes, the animation curve will not over shoot the keyframe values, and use a cubic interpolation to calculate the auto tangent. 
        - Value: 13
        '''
        pass

    def kTangentAutoCustom(self):
        '''This is an enum of TangentType.
        - Description: Introduced in 2022.0 2022.0:Introduced in this version. The first and last keyframes will have flat tangents. Between, inner keyframes, the animation curve will not over shoot the keyframe values, and use a custom cubic interpolation to calculate the auto tangent. 
        - Value: 14
        '''
        pass

