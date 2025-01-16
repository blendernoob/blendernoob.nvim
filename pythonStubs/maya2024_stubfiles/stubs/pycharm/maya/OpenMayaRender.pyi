
'''
Stub class file for:
OpenMayaRender

Maya2024 Python API stub file
Pycharm Version
Generated from original Maya documentation.
Autodesk Maya2024  c1997-2023 Autodesk, Inc. All rights reserved. 
'''


from typing import overload




class MColorMixingSpaceHelper:
    '''Helper class for implementing correct color pickers that use
widgets such as sliders and color wheels to mix colors
Create an instance and set the mixing color space to transform a
color or evaluate sliders.
'''
    def __init__(self):
        pass


    def refresh(self): 
        '''
        refresh(self)

        Synopsis
        -----
        Re-initializes the color mixing helper, for example after a
        configuration change.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getMixingSpaceNames(self, returnedStatus: MColorMixingSpaceHelper.MStatus): 
        '''
        getMixingSpaceNames(self, returnedStatus: MColorMixingSpaceHelper.MStatus) -> MStringArray

        Synopsis
        -----
        Returns the list of available mixing spaces for the current color
        management configuration.

        Returns: 
        ----- 
        List of avaialble mixing spaces

        Parameters:
        -----
        returnedStatus: MColorMixingSpaceHelper.MStatus
        	[out] -> Status code 


        '''
        pass

    def setMixingSpace(self, name: MString): 
        '''
        setMixingSpace(self, name: MString)

        Synopsis
        -----
        Sets the mixing space to be used by
        MColorPickerUtilities::applyMixingTransform() and the slider
        methods.

        Returns:
        -----
        None

        Parameters:
        -----
        name: MString
        	[in] -> The color space name as one of the values by 


        '''
        pass

    def getViewNames(self, returnedStatus: MColorMixingSpaceHelper.MStatus): 
        '''
        getViewNames(self, returnedStatus: MColorMixingSpaceHelper.MStatus) -> MStringArray

        Synopsis
        -----
        Returns the list of available views for the current color
        management configuration.

        Returns: 
        ----- 
        List of avaialble views

        Parameters:
        -----
        returnedStatus: MColorMixingSpaceHelper.MStatus
        	[out] -> Status code 


        '''
        pass

    def setView(self, name: MString): 
        '''
        setView(self, name: MString)

        Synopsis
        -----
        Sets the view to be used by
        MColorPickerUtilities::applyMixingTransform() and the slider
        methods.

        Returns:
        -----
        None

        Parameters:
        -----
        name: MString
        	[in] -> The view name as one of the values by 


        '''
        pass

    def applyMixingTransform(self, inputColor: MColor,
                        direction: MColorMixingSpaceHelper.Direction,
                        returnedStatus: MColorMixingSpaceHelper.MStatus): 
        '''
        applyMixingTransform(self, inputColor: MColor,
                        direction: MColorMixingSpaceHelper.Direction,
                        returnedStatus: MColorMixingSpaceHelper.MStatus) -> MColor

        Synopsis
        -----
        Applies the mixing transform to an input color. The mixing space
        must have been previously set.

        Returns: 
        ----- 
        Returns the transformed color, or the input color if color
        management is turned off

        Parameters:
        -----
        inputColor: MColor
        	[in] -> The input color to transform 

        direction: MColorMixingSpaceHelper.Direction
        	[in] -> The direction of the transform, 

        returnedStatus: MColorMixingSpaceHelper.MStatus
        	[out] -> Status code. 


        '''
        pass

    def mixingToSlider(self, mixingPosition: float,
                        minPos: float,
                        maxPos: float): 
        '''
        mixingToSlider(self, mixingPosition: float,
                        minPos: float,
                        maxPos: float) -> float

        Synopsis
        -----
        Converts a mixing space component value to its normalized color
        slider position.

        Returns: 
        ----- 
        The slider position to display

        Parameters:
        -----
        mixingPosition: float
        	[in] -> The mixing color value to convert 

        minPos: float
        	[in] -> Left edge mixing value for the slider 

        maxPos: float
        	[in] -> Right edge mixing value for the slider 


        '''
        pass

    def sliderToMixing(self, sliderPosition: float,
                        minPos: float,
                        maxPos: float): 
        '''
        sliderToMixing(self, sliderPosition: float,
                        minPos: float,
                        maxPos: float) -> float

        Synopsis
        -----
        Converts normalized slider position to mixing space value.

        Returns: 
        ----- 
        The color component value for the given slider position

        Parameters:
        -----
        sliderPosition: float
        	[in] -> The position of the slider within minPos and maxPos 

        minPos: float
        	[in] -> Left edge mixing value for the slider 

        maxPos: float
        	[in] -> Right edge mixing value for the slider 


        '''
        pass

class Direction:
    '''Color transform direction. 
    Non-functional class.  Values for this enum:
    kForward
    kInverse
    '''

    def __init__(self):
        pass

    def kForward(self):
        '''This is an enum of Direction.
        - Description: apply the color transform 
        - Value: 0
        '''
        pass

    def kInverse(self):
        '''This is an enum of Direction.
        - Description: invert the color transform 
        - Value: 1
        '''
        pass

class MColorPickerCallback:
    '''Helper class for the color picking mechanism.
When using the Color Picking mechanism one should create a
callback class inhereting from
MColorPickerCallback in order to implement the pure virtual method getcolor(). By
having a class (instead of a plain function callback), some
custom data could be added to the callback instance.
'''
    def __init__(self):
        pass


    def getColor(self): 
        '''
        getColor(self) -> virtual MColor

        Synopsis
        -----

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getKey(self): 
        '''
        getKey(self) -> MColorPickerCallback.QWidget*

        Synopsis
        -----
        Returns the widget used for the registration.

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

class MColorPickerUtilities:
    '''Utilities for implementing Color Pickers. See also
MColorMixingSpaceHelper'''
    def __init__(self):
        pass


    def isRegisteredToColorPicking(self, widget: MColorPickerUtilities.QWidget): 
        '''
        isRegisteredToColorPicking(self, widget: MColorPickerUtilities.QWidget) -> bool

        Synopsis
        -----
        Returns whether the widget registered to the Color Picking
        mechanism.

        Returns: 
        ----- 
        true if widget is registered

        Parameters:
        -----
        widget: MColorPickerUtilities.QWidget
        	[in] -> The widget to test


        '''
        pass

    def doRegisterToColorPicking(self, widget: MColorPickerUtilities.QWidget,
                        callback: MColorPickerCallback): 
        '''
        doRegisterToColorPicking(self, widget: MColorPickerUtilities.QWidget,
                        callback: MColorPickerCallback)

        Synopsis
        -----
        Registers a widget that can be used to pick a color with an eye
        dropper.

        Returns:
        -----
        None

        Parameters:
        -----
        widget: MColorPickerUtilities.QWidget
        	[in] -> The widget to register 

        callback: MColorPickerCallback
        	[in] -> The callback to get a color at a specifc position


        '''
        pass

    def unregisterFromColorPicking(self, widget: MColorPickerUtilities.QWidget): 
        '''
        unregisterFromColorPicking(self, widget: MColorPickerUtilities.QWidget)

        Synopsis
        -----
        Unregisters a widget that was registed with
        doRegisterToColorPicking.

        Returns:
        -----
        None

        Parameters:
        -----
        widget: MColorPickerUtilities.QWidget
        	[in] -> The widget to unregister


        '''
        pass

    def applyViewTransform(self, inputColor: MColor,
                        direction: MColorPickerUtilities.Direction): 
        '''
        applyViewTransform(self, inputColor: MColor,
                        direction: MColorPickerUtilities.Direction) -> MColor

        Synopsis
        -----
        Introduced in 2023.0 Applies a colour transform from the
        rendering colour space to the (display, view) space using the
        color management settings from Maya.

        Returns: 
        ----- 
        Returns the transformed color, or the input color unmodified if
        color management is turned off

        Parameters:
        -----
        inputColor: MColor
        	[in] -> The input color to transform 

        direction: MColorPickerUtilities.Direction
        	[in] -> The direction of the transform, 


        '''
        pass

    def grabColor(self, returnedStatus: MColorPickerUtilities.MStatus): 
        '''
        grabColor(self, returnedStatus: MColorPickerUtilities.MStatus) -> MColor

        Synopsis
        -----
        Introduced in 2023.0 Run the eye dropper tool to pick a color on
        screen with the mouse.

        Returns: 
        ----- 
        Returns the picked color. If cancelled, the color returned will
        have all components set to zero and returnedStatus will be set to
        MS::kFailure

        Parameters:
        -----
        returnedStatus: MColorPickerUtilities.MStatus
        	[out] -> MS::kFailure


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

class Direction:
    '''Color transform direction. 
    Non-functional class.  Values for this enum:
    kForward
    kInverse
    '''

    def __init__(self):
        pass

    def kForward(self):
        '''This is an enum of Direction.
        - Description: apply the color transform 
        - Value: 0
        '''
        pass

    def kInverse(self):
        '''This is an enum of Direction.
        - Description: invert the color transform 
        - Value: 1
        '''
        pass

class MCommonRenderSettingsData:
    '''Data container for common rendering settings.
This class is a container that encapsulates the data for common
rendering globals. The data is intended to be accessed using the
following method:
'''
    def __init__(self):
        pass


    def isAnimated(self): 
        '''
        isAnimated(self) -> bool

        Synopsis
        -----
        Determines if there is animation.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def isMovieFormat(self): 
        '''
        isMovieFormat(self) -> bool

        Synopsis
        -----
        Determines if the output format is a single movie file.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setPassName(self, passArg: MString): 
        '''
        setPassName(self, passArg: MString)

        Synopsis
        -----
        Used with getImageName. Sets the pass name for later use. Adds a
        pass subdirectory to the path for the image.

        Returns:
        -----
        None

        Parameters:
        -----
        passArg: MString
        	[in] -> 


        '''
        pass

    def setFieldName(self, field: MString): 
        '''
        setFieldName(self, field: MString)

        Synopsis
        -----
        Used with getImageName. Sets the field name for later use. Adds a
        field subdirectory to the path for the image.

        Returns:
        -----
        None

        Parameters:
        -----
        field: MString
        	[in] -> The name of the field. 


        '''
        pass

    @overload
    def getImageName(self, pathType: MCommonRenderSettingsData.MpathType,
                        frameNumber: double,
                        sceneName: MString,
                        cameraName: MString,
                        fileFormat: MString,
                        layer: MObject,
                        createDirectory: bool,
                        ReturnStatus: MCommonRenderSettingsData.MStatus): 
        '''
        getImageName(self, pathType: MCommonRenderSettingsData.MpathType,
                        frameNumber: double,
                        sceneName: MString,
                        cameraName: MString,
                        fileFormat: MString,
                        layer: MObject,
                        createDirectory: bool,
                        ReturnStatus: MCommonRenderSettingsData.MStatus) -> const MString

        Synopsis
        -----
        Obtains the image name with the proper subdirectory structure.
        Compute the path for the image.The path type returned depends on
        which option has been specified by pathType:

        Returns: 
        ----- 
        The image path as a string.

        Parameters:
        -----
        pathType: MCommonRenderSettingsData.MpathType
        	[in] -> decides file path format of the returned string. See above. 

        frameNumber: double
        	[in] -> the frame number to be used. 

        sceneName: MString
        	[in] -> the scene name. 

        cameraName: MString
        	[in] -> the name of the camera rendering this image. 

        fileFormat: MString
        	[in] -> if not an empty string, use this file format instead of the one selected in the render settings to decide the final file name. 

        layer: MObject
        	[in] -> render layer object from which this image is rendered. 

        createDirectory: bool
        	[in] -> if true, the image path directory will be created. 

        ReturnStatus: MCommonRenderSettingsData.MStatus
        	[out] -> Status code


        '''
        pass

    @overload
    def getImageName(self, pathType: MCommonRenderSettingsData.MpathType,
                        frameNumber: double,
                        sceneName: MString,
                        cameraName: MString,
                        fileFormat: MString,
                        layer: MObject,
                        customTokenString: MString,
                        createDirectory: bool,
                        ReturnStatus: MCommonRenderSettingsData.MStatus): 
        '''
        getImageName(self, pathType: MCommonRenderSettingsData.MpathType,
                        frameNumber: double,
                        sceneName: MString,
                        cameraName: MString,
                        fileFormat: MString,
                        layer: MObject,
                        customTokenString: MString,
                        createDirectory: bool,
                        ReturnStatus: MCommonRenderSettingsData.MStatus) -> const MString

        Synopsis
        -----
        Obtains the image name with the proper subdirectory structure
        (supports custom tokens). Compute the path for the image.The path
        type returned depends on which option has been specified by
        pathType:

        Returns: 
        ----- 
        The image path as a string.

        Parameters:
        -----
        pathType: MCommonRenderSettingsData.MpathType
        	[in] -> decides file path format of the returned string. See above. 

        frameNumber: double
        	[in] -> the frame number to be used. 

        sceneName: MString
        	[in] -> the scene name. 

        cameraName: MString
        	[in] -> the name of the camera rendering this image. 

        fileFormat: MString
        	[in] -> if not an empty string, use this file format instead of the one selected in the render settings to decide the final file name. 

        layer: MObject
        	[in] -> render layer object from which this image is rendered. 

        customTokenString: MString
        	[in] -> space separated list of key-value pairs to replace in the image name (ex. "myToken1=myValue1 myToken2=myValue2") 

        createDirectory: bool
        	[in] -> if true, the image path directory will be created. 

        ReturnStatus: MCommonRenderSettingsData.MStatus
        	[out] -> Status code


        '''
        pass

    def shouldRenderFrameAtTime(self, pathType: MCommonRenderSettingsData.MpathType,
                        frameNumber: double,
                        sceneName: MString,
                        cameraName: MString,
                        fileFormat: MString,
                        layer: MObject,
                        customTokenString: MString): 
        '''
        shouldRenderFrameAtTime(self, pathType: MCommonRenderSettingsData.MpathType,
                        frameNumber: double,
                        sceneName: MString,
                        cameraName: MString,
                        fileFormat: MString,
                        layer: MObject,
                        customTokenString: MString) -> bool

        Synopsis
        -----
        Indicates whether render the frame or not. If true, render it. If
        false, skip it. Determine whether to render the frame or not by
        comparing image file name.If file already exists, skip rendering
        it. If not, render the frame.

        Returns: 
        ----- 
        Whether to render the frame or not. If true, render it. If false,
        skip it.

        Parameters:
        -----
        pathType: MCommonRenderSettingsData.MpathType
        	[in] -> decides file path format of the returned string. See above. 

        frameNumber: double
        	[in] -> the frame number to be used. 

        sceneName: MString
        	[in] -> the scene name. 

        cameraName: MString
        	[in] -> the name of the camera rendering this image. 

        fileFormat: MString
        	[in] -> if not an empty string, use this file format instead of the one selected in the render settings to decide the final file name. 

        layer: MObject
        	[in] -> render layer object from which this image is rendered. 

        customTokenString: MString
        	[in] -> space separated list of key-value pairs to replace in the image name (ex. "myToken1=myValue1 myToken2=myValue2")


        '''
        pass

    def getBufferName(self, renderPass: MObject,
                        layer: MObject,
                        cameraName: MString,
                        customTokenString: MString,
                        leaveUnmatchedTokens: bool,
                        ReturnStatus: MCommonRenderSettingsData.MStatus): 
        '''
        getBufferName(self, renderPass: MObject,
                        layer: MObject,
                        cameraName: MString,
                        customTokenString: MString,
                        leaveUnmatchedTokens: bool,
                        ReturnStatus: MCommonRenderSettingsData.MStatus) -> const MString

        Synopsis
        -----
        Get image buffer name. This name will be used when multiple
        buffers are rendered into the same image. This is only valid for
        image formats which support multiple buffers, such as OpenEXR.

        Returns: 
        ----- 
        The name of buffer as a string.

        Parameters:
        -----
        renderPass: MObject
        	[in] -> Render pass object of the this rendering image. 

        layer: MObject
        	[in] -> render layer object pointer from which this image is rendered. 

        cameraName: MString
        	[in] -> The name of the camera rendering this image. 

        customTokenString: MString
        	[in] -> Space separated list of key-value pairs to replace in the buffer name (ex. "myToken1=myValue1 myToken2=myValue2"). 

        leaveUnmatchedTokens: bool
        	[in] -> whether to leave the unmatched tokens. 

        ReturnStatus: MCommonRenderSettingsData.MStatus
        	[out] -> Status code.


        '''
        pass

    def getPreRenderFrameCmd(self): 
        '''
        getPreRenderFrameCmd(self) -> MString

        Synopsis
        -----
        Return the preRenderFrame MEL command, which is run immediately
        before rendering a frame. It is run before the configurable
        preRenderMel string. This command is guaranteed to be a non-empty
        string.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getPostRenderFrameCmd(self): 
        '''
        getPostRenderFrameCmd(self) -> MString

        Synopsis
        -----
        Return the postRenderFrame MEL command, which is run immediately
        after rendering a frame. It is run after the configurable
        postRenderMel string. This command is guaranteed to be a non-
        empty string.

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

    def renumberFrames(self): 
        '''
        renumberFrames(self) -> bool

        Synopsis
        -----
        When true, images need to be renumbered. This only affects the
        image names.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MpathType:
    '''Defines the types file paths. 
    Non-functional class.  Values for this enum:
    kRelativePath
    kFullPathImage
    kFullPathTmp
    '''

    def __init__(self):
        pass

    def kRelativePath(self):
        '''This is an enum of MpathType.
        - Description: Relative to the project. 
        - Value: 0
        '''
        pass

    def kFullPathImage(self):
        '''This is an enum of MpathType.
        - Description: Full path. 
        - Value: 1
        '''
        pass

    def kFullPathTmp(self):
        '''This is an enum of MpathType.
        - Description: Full path in the temporary directory. 
        - Value: 2
        '''
        pass

class MDrawProcedureBase:
    '''This class provides an interface through which a plug-in can be
writen to implement a class to provide custom hardware drawing
effects.
The derived class can be added, removed, or reordered in a list
of draw procedures used by the hardware renderer. Please refer to
documentation for
MHardwareRenderer for more details.
Each procedure has a user defined string name and can be enabled
or disabled. Name, and enabling methods must be defined.
All derived classes must over the
execute() method. This is the method that will be called by the hardware
renderer to which the procedure is attached. The call will only
be made if the procedure is enabled.
'''
    def __init__(self):
        pass


    def execute(self): 
        '''
        execute(self) -> bool

        Synopsis
        -----
        This method gets called by the renderer to execture the draw
        procedure. Derived class of MDrawProcedureBase must implement
        this method as it defined as a pure virtual method on this class.
        The implementation is free to perform any drawing functionality
        from within this method.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setEnabled(self, value: bool): 
        '''
        setEnabled(self, value: bool)

        Synopsis
        -----
        This method sets whether the draw procedure is enabled or not.

        Returns:
        -----
        None

        Parameters:
        -----
        value: bool
        	[in] -> Boolean value to set the enabling state. 


        '''
        pass

    def enabled(self): 
        '''
        enabled(self) -> bool

        Synopsis
        -----
        This method returns whether the draw procedure is enabled or not.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setName(self, name: MString): 
        '''
        setName(self, name: MString)

        Synopsis
        -----
        This method sets the name for the draw procedure.

        Returns:
        -----
        None

        Parameters:
        -----
        name: MString
        	[in] -> Name to set. 


        '''
        pass

class MFnImageSource:
    '''Function set for image sources.
An image source is a node that is used in render graphs, e.g.
compositing graphs, shading networks. It provides access to the
images produced by 3D scene renderers, or 2D image processing
tasks. This class provides functionality for working with image
sources, e.g. retrieving the path of rendered image source files.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kImageSource.Reimplemented from MFnDependencyNode.

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
        className(self) -> MFnImageSource.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnImageSource".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getImageName(self, pathType: MCommonRenderSettingsData.MCommonRenderSettingsData,
                        frameNumber: double,
                        sceneName: MString,
                        camera: MObject,
                        renderLayer: MObject,
                        bufferName: MString,
                        ReturnStatus: MFnImageSource.MStatus): 
        '''
        getImageName(self, pathType: MCommonRenderSettingsData.MCommonRenderSettingsData,
                        frameNumber: double,
                        sceneName: MString,
                        camera: MObject,
                        renderLayer: MObject,
                        bufferName: MString,
                        ReturnStatus: MFnImageSource.MStatus) -> MString

        Synopsis
        -----
        Return image path associated with this image source.

        Returns: 
        ----- 
        Path to image file.

        Parameters:
        -----
        pathType: MCommonRenderSettingsData.MCommonRenderSettingsData
        	[in] -> Project relative, full, or temporary directory. 

        frameNumber: double
        	[in] -> Desired frame in image sequence. 

        sceneName: MString
        	[in] -> Scene for which image was rendered. 

        camera: MObject
        	[in] -> Parent transform of the camera used to render the scene. 

        renderLayer: MObject
        	[in] -> Render layer used to render scene. 

        bufferName: MString
        	[out] -> Name of the buffer containing the image, used with OpenEXR files. 

        ReturnStatus: MFnImageSource.MStatus
        	[out] -> Status code. 


        '''
        pass

class MFnRenderLayer:
    '''Function set for render layer.
Provide functionalities for working with render layers such as
getting the objects present in the render layer or checking
whether the given object is in the current layer.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kRenderLayer.Reimplemented from MFnDependencyNode.

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
        className(self) -> MFnRenderLayer.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnRenderLayer".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def inLayer(self, transform: MObject,
                        ReturnStatus: MFnRenderLayer.MStatus): 
        '''
        inLayer(self, transform: MObject,
                        ReturnStatus: MFnRenderLayer.MStatus) -> bool

        Synopsis
        -----
        Returns true if the given shape is in this layer. This method
        will check all container layers for transform containment. The
        MObject specified must be a shape node.

        Returns: 
        ----- 
        True if the given node is in the layer, false otherwise.

        Parameters:
        -----
        transform: MObject
        	[in] -> MObject

        ReturnStatus: MFnRenderLayer.MStatus
        	[out] -> Return code.


        '''
        pass

    def layerChildren(self, array: MObjectArray,
                        recurse: bool): 
        '''
        layerChildren(self, array: MObjectArray,
                        recurse: bool)

        Synopsis
        -----
        Returns the container layers for this layer. Container layers
        provide the ability for a given render layer to "contain" other
        render layers.

        Returns:
        -----
        None

        Parameters:
        -----
        array: MObjectArray
        	[in] -> List of contained render layers. 

        recurse: bool
        	[in] -> If true then the list operation will be applied recursively to any contained render layers which themselves contain other render layers.


        '''
        pass

    def inCurrentRenderLayer(self, objectPath: MDagPath,
                        ReturnStatus: MFnRenderLayer.MStatus): 
        '''
        inCurrentRenderLayer(self, objectPath: MDagPath,
                        ReturnStatus: MFnRenderLayer.MStatus) -> bool

        Synopsis
        -----
        The function checks if the given object is present in the current
        render layer or not.

        Returns: 
        ----- 
        True if the given object is in the current render layer, false
        otherwise.

        Parameters:
        -----
        objectPath: MDagPath
        	[in] -> Path of the render layer object. 

        ReturnStatus: MFnRenderLayer.MStatus
        	[out] -> Status code.


        '''
        pass

    def listMembers(self, objectsInLayer: MObjectArray): 
        '''
        listMembers(self, objectsInLayer: MObjectArray)

        Synopsis
        -----
        Returns the objects present in the render layer.

        Returns:
        -----
        None

        Parameters:
        -----
        objectsInLayer: MObjectArray
        	[in] -> The array of MObjects, present in the layer.


        '''
        pass

    def isPlugAdjusted(self, scenePlug: MPlug,
                        retStatus: MFnRenderLayer.MStatus): 
        '''
        isPlugAdjusted(self, scenePlug: MPlug,
                        retStatus: MFnRenderLayer.MStatus) -> bool

        Synopsis
        -----
        The function checks if the specified plug is adjusted or not;
        returns true if the plug is adjusted, else returns false.

        Returns: 
        ----- 
        True if the plug is adjusted, false otherwise.

        Parameters:
        -----
        scenePlug: MPlug
        	[in] -> The plug which needs to be checked for adjustment. 

        retStatus: MFnRenderLayer.MStatus
        	[out] -> MStatus


        '''
        pass

    def adjustmentPlug(self, scenePlug: MPlug,
                        retStatus: MFnRenderLayer.MStatus): 
        '''
        adjustmentPlug(self, scenePlug: MPlug,
                        retStatus: MFnRenderLayer.MStatus) -> MPlug

        Synopsis
        -----
        Returns the render layer adjustment value plug for the specified
        plug. If there is no layer override on the plug, a copy of
        scenePlug is returned.

        Returns: 
        ----- 
        The render layer adjustment plug.

        Parameters:
        -----
        scenePlug: MPlug
        	[in] -> The plug for which the adjustment is sought. 

        retStatus: MFnRenderLayer.MStatus
        	[out] -> MStatus


        '''
        pass

    def externalRenderPasses(self, renderPassArray: MObjectArray): 
        '''
        externalRenderPasses(self, renderPassArray: MObjectArray)

        Synopsis
        -----
        The function builds an array of unique render pass nodes
        (MObject) that are connected to the renderPass attribute. This
        function descends recursively into render pass sets to collect
        all connected render passes.

        Returns:
        -----
        None

        Parameters:
        -----
        renderPassArray: MObjectArray
        	[out] -> Array to which the result of the search is written.


        '''
        pass

    def passHasObject(self, renderPass: MObject,
                        objectInstance: MDagPath,
                        ReturnStatus: MFnRenderLayer.MStatus): 
        '''
        passHasObject(self, renderPass: MObject,
                        objectInstance: MDagPath,
                        ReturnStatus: MFnRenderLayer.MStatus) -> bool

        Synopsis
        -----
        Returns true if the specified object instance contributes to the
        given render pass, based on the pass contribution maps attached
        to the layer. This method does not verify whether the object
        instance or the renderPass are actually rendered by the layer.

        Returns: 
        ----- 
        True if the object contributes to the pass, false otherwise.

        Parameters:
        -----
        renderPass: MObject
        	[in] -> a render pass node 

        objectInstance: MDagPath
        	[in] -> DAG path of a shape instance 

        ReturnStatus: MFnRenderLayer.MStatus
        	[out] -> status of the method call.


        '''
        pass

    def passHasLight(self, renderPass: MObject,
                        light: MObject,
                        ReturnStatus: MFnRenderLayer.MStatus): 
        '''
        passHasLight(self, renderPass: MObject,
                        light: MObject,
                        ReturnStatus: MFnRenderLayer.MStatus) -> bool

        Synopsis
        -----
        Returns true if the specified light contributes to the given
        render pass, based on the pass contribution maps attached to this
        layer. This method does not verify whether the light or the
        renderPass are actually rendered by the layer.

        Returns: 
        ----- 
        True if the light contributes to the pass, false otherwise.

        Parameters:
        -----
        renderPass: MObject
        	[in] -> a render pass node 

        light: MObject
        	[in] -> a light shape node 

        ReturnStatus: MFnRenderLayer.MStatus
        	[out] -> status of the method call.


        '''
        pass

    def findLayerByName(self, renderLayer: MString,
                        ReturnStatus: MFnRenderLayer.MStatus): 
        '''
        findLayerByName(self, renderLayer: MString,
                        ReturnStatus: MFnRenderLayer.MStatus) -> MObject

        Synopsis
        -----
        This function returns an MObject to a render layer that matches
        the specified name. If no render layer is found with the given
        name, MObject::kNullObj is returned.

        Returns: 
        ----- 
        The matching render layer or MObject::kNullObj if no matching
        render layer was found.

        Parameters:
        -----
        renderLayer: MString
        	[in] -> The name of the render layer. 

        ReturnStatus: MFnRenderLayer.MStatus
        	[out] -> status of the method call.


        '''
        pass

    def defaultRenderLayer(self, ReturnStatus: MFnRenderLayer.MStatus): 
        '''
        defaultRenderLayer(self, ReturnStatus: MFnRenderLayer.MStatus) -> MObject

        Synopsis
        -----
        Returns the MObject for the defaultRenderLayer. This MObject can
        be used in MFnRenderLayer.

        Returns: 
        ----- 
        The default render layer.

        Parameters:
        -----
        ReturnStatus: MFnRenderLayer.MStatus
        	[out] -> status of the method call.


        '''
        pass

    def listAllRenderLayers(self, array: MObjectArray): 
        '''
        listAllRenderLayers(self, array: MObjectArray)

        Synopsis
        -----
        Returns the list of render layers currently in the system.

        Returns:
        -----
        None

        Parameters:
        -----
        array: MObjectArray
        	[in] -> MObjectArray


        '''
        pass

    def currentLayer(self, ReturnStatus: MFnRenderLayer.MStatus): 
        '''
        currentLayer(self, ReturnStatus: MFnRenderLayer.MStatus) -> MObject

        Synopsis
        -----
        Returns the MObject for the current render layer. This MObject
        can be used in MFnRenderLayer.

        Returns: 
        ----- 
        The current render layer.

        Parameters:
        -----
        ReturnStatus: MFnRenderLayer.MStatus
        	[out] -> status of the method call.


        '''
        pass

class MFnRenderPass:
    '''Function set for render passes.
Provide functionalities for working with render passes such as
retrieving renderer-specific implementations.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kRenderPass.Reimplemented from MFnDependencyNode.

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
        className(self) -> MFnRenderPass.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnRenderPass".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def frameBufferType(self, ReturnStatus: MFnRenderPass.MStatus): 
        '''
        frameBufferType(self, ReturnStatus: MFnRenderPass.MStatus) -> MPxRenderPassImpl.MPxRenderPassImpl

        Synopsis
        -----
        Returns the data type of the frame buffer associated with the
        render pass.

        Returns:
        -----
        None

        Parameters:
        -----
        ReturnStatus: MFnRenderPass.MStatus
        	[out] -> Status code.


        '''
        pass

    def frameBufferChannels(self, ReturnStatus: MFnRenderPass.MStatus): 
        '''
        frameBufferChannels(self, ReturnStatus: MFnRenderPass.MStatus) -> int

        Synopsis
        -----
        Returns the number of channels of the frame buffer associated
        with the render pass.

        Returns:
        -----
        None

        Parameters:
        -----
        ReturnStatus: MFnRenderPass.MStatus
        	[out] -> Status code.


        '''
        pass

    def usesFiltering(self, ReturnStatus: MFnRenderPass.MStatus): 
        '''
        usesFiltering(self, ReturnStatus: MFnRenderPass.MStatus) -> bool

        Synopsis
        -----
        Returns true if frame buffer filtering is requested. This setting
        may be ignored in the cases of frame buffer types and frame
        buffer semantics that do not allow interpolation.

        Returns:
        -----
        None

        Parameters:
        -----
        ReturnStatus: MFnRenderPass.MStatus
        	[out] -> Status code.


        '''
        pass

    def passID(self, ReturnStatus: MFnRenderPass.MStatus): 
        '''
        passID(self, ReturnStatus: MFnRenderPass.MStatus) -> MString

        Synopsis
        -----
        Returns the passID string that uniquely identifies the renderpass
        definition associated with the pass.

        Returns:
        -----
        None

        Parameters:
        -----
        ReturnStatus: MFnRenderPass.MStatus
        	[out] -> Status code.


        '''
        pass

    def customTokenString(self, ReturnStatus: MFnRenderPass.MStatus): 
        '''
        customTokenString(self, ReturnStatus: MFnRenderPass.MStatus) -> MString

        Synopsis
        -----
        Returns a custom token string that can be passed to
        MCommonRenderSettingsData::getImageName() to generate a file name
        for the pass.

        Returns:
        -----
        None

        Parameters:
        -----
        ReturnStatus: MFnRenderPass.MStatus
        	[out] -> Status code.


        '''
        pass

class MGeometryData:
    '''This class allows storage of arbitrary data which is formated to
be specifically suitable for usage using a 3D display interface
such as OpenGL.
Format options include:
There are specific "type" identifiers to provide a semantic on
for the data. These include:
Currently Maya only interprets a fixed format subset for data
with recongnized semantics, This does not mean that the user
cannot create any arbitrary format for data storage. Support
formats with semantics includes:
Memory allocation of the correct size is left up to the user of
this class.
Memory can be marked as "owned" by this class or the user of this
class. Ownership by this class is the default behaviour specified
in the constructor. If the data is marked as being owned by the
class, it is assumed that the data is created using a "new"
operation, as the destructor of this class will use a "delete"
operation to free memory.
Internal Maya data which is passed to the user via this class is
always assumed to be non-modifiable.
'''
    def __init__(self):
        pass


    def objectName(self): 
        '''
        objectName(self) -> char*

        Synopsis
        -----
        Return the logical name of the geometry.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def uniqueID(self): 
        '''
        uniqueID(self) -> int

        Synopsis
        -----
        Return the per session unique identifier.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def dataType(self): 
        '''
        dataType(self) -> MGeometryData.MGeometryData

        Synopsis
        -----
        Get the data type for the data.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def elementType(self): 
        '''
        elementType(self) -> MGeometryData.MGeometryData

        Synopsis
        -----
        Returns the data type.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def elementTypeSize(self): 
        '''
        elementTypeSize(self) -> int

        Synopsis
        -----
        Return the element type size.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def elementSize(self): 
        '''
        elementSize(self) -> MGeometryData.MGeometryData

        Synopsis
        -----
        Return element size.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def elementCount(self): 
        '''
        elementCount(self) -> int

        Synopsis
        -----
        Return element count.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def data(self): 
        '''
        data(self) -> void*

        Synopsis
        -----
        Retrieve a pointer to the internal data.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setCollectionNumber(self, collectionNumber: int): 
        '''
        setCollectionNumber(self, collectionNumber: int)

        Synopsis
        -----
        Set the collection number for the object. Numbers less than 0 are
        invalid collection numbers.

        Returns:
        -----
        None

        Parameters:
        -----
        collectionNumber: int
        	[in] -> The number to use 


        '''
        pass

    def collectionNumber(self): 
        '''
        collectionNumber(self) -> int

        Synopsis
        -----
        Get the collection number of the data. Collection numbers are
        zero-based.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setObjectOwnsData(self, value: bool): 
        '''
        setObjectOwnsData(self, value: bool)

        Synopsis
        -----
        Set ownship of the interal data.

        Returns:
        -----
        None

        Parameters:
        -----
        value: bool
        	[in] -> ownership flag to set to. 


        '''
        pass

    def objectOwnsData(self): 
        '''
        objectOwnsData(self) -> bool

        Synopsis
        -----
        Return if the MGeometryData object owns the internal data or not.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class ElementSize:
    '''Specifies the size or dimension of each data element of the storage. 
    Non-functional class.  Values for this enum:
    kInvalidElementSize
    kOne
    kTwo
    kThree
    kFour
    '''

    def __init__(self):
        pass

    def kInvalidElementSize(self):
        '''This is an enum of ElementSize.
        - Description: Invalid element size. 
        - Value: 0
        '''
        pass

    def kOne(self):
        '''This is an enum of ElementSize.
        - Description: Single value. 
        - Value: 1
        '''
        pass

    def kTwo(self):
        '''This is an enum of ElementSize.
        - Description: 2-tuple 
        - Value: 2
        '''
        pass

    def kThree(self):
        '''This is an enum of ElementSize.
        - Description: 3-tuple 
        - Value: 3
        '''
        pass

    def kFour(self):
        '''This is an enum of ElementSize.
        - Description: 4-tuple 
        - Value: 4
        '''
        pass

class ElementType:
    '''Specifies the data type of each data element of the storage. 
    Non-functional class.  Values for this enum:
    kInvalidElementType
    kFloat
    kDouble
    kChar
    kUnsignedChar
    kInt16
    kUnsignedInt16
    kInt32
    kUnsignedInt32
    '''

    def __init__(self):
        pass

    def kInvalidElementType(self):
        '''This is an enum of ElementType.
        - Description: Invalid element type (default value) 
        - Value: -1
        '''
        pass

    def kFloat(self):
        '''This is an enum of ElementType.
        - Description: IEEE single precision floating point. 
        - Value: 0
        '''
        pass

    def kDouble(self):
        '''This is an enum of ElementType.
        - Description: IEEE double precision floating point. 
        - Value: 1
        '''
        pass

    def kChar(self):
        '''This is an enum of ElementType.
        - Description: Signed char. 
        - Value: 2
        '''
        pass

    def kUnsignedChar(self):
        '''This is an enum of ElementType.
        - Description: Unsigned char. 
        - Value: 3
        '''
        pass

    def kInt16(self):
        '''This is an enum of ElementType.
        - Description: Signed 16-bit integer. 
        - Value: 4
        '''
        pass

    def kUnsignedInt16(self):
        '''This is an enum of ElementType.
        - Description: Unsigned 16-bit integer. 
        - Value: 5
        '''
        pass

    def kInt32(self):
        '''This is an enum of ElementType.
        - Description: Signed 32-bit integer. 
        - Value: 6
        '''
        pass

    def kUnsignedInt32(self):
        '''This is an enum of ElementType.
        - Description: Unsigned 32-bit integer. 
        - Value: 7
        '''
        pass

class DataType:
    '''Specifies the data type of the storage array. 
    Non-functional class.  Values for this enum:
    kInvalidDataType
    kPosition
    kNormal
    kTexCoord
    kColor
    kWeight
    kAPISupported
    kTangent
    kBiNormal
    kVelocity
    kPrimitiveCenter
    kColorMask
    kUserData
    kMaxDataTypeIndex
    '''

    def __init__(self):
        pass

    def kInvalidDataType(self):
        '''This is an enum of DataType.
        - Description: Invalid data type (default value) 
        - Value: 0
        '''
        pass

    def kPosition(self):
        '''This is an enum of DataType.
        - Description: Position vector. 
        - Value: 1
        '''
        pass

    def kNormal(self):
        '''This is an enum of DataType.
        - Description: Normal vector. 
        - Value: 2
        '''
        pass

    def kTexCoord(self):
        '''This is an enum of DataType.
        - Description: Texture coordinate tuple. 
        - Value: 3
        '''
        pass

    def kColor(self):
        '''This is an enum of DataType.
        - Description: Color tuple. 
        - Value: 4
        '''
        pass

    def kWeight(self):
        '''This is an enum of DataType.
        - Description: Vertex weighting data. 
        - Value: 5
        '''
        pass

    def kAPISupported(self):
        '''This is an enum of DataType.
        - Description: Separator to indicate native draw API supported types. 
        - Value: 6
        '''
        pass

    def kTangent(self):
        '''This is an enum of DataType.
        - Description: Tangent vector. 
        - Value: 7
        '''
        pass

    def kBiNormal(self):
        '''This is an enum of DataType.
        - Description: Bi-normal vector. 
        - Value: 8
        '''
        pass

    def kVelocity(self):
        '''This is an enum of DataType.
        - Description: Velocity vector. 
        - Value: 9
        '''
        pass

    def kPrimitiveCenter(self):
        '''This is an enum of DataType.
        - Description: Center of primitive. 
        - Value: 10
        '''
        pass

    def kColorMask(self):
        '''This is an enum of DataType.
        - Description: Mapped, unmapped color mask. 
        - Value: 11
        '''
        pass

    def kUserData(self):
        '''This is an enum of DataType.
        - Description: Arbitrary "user data". 
        - Value: 12
        '''
        pass

    def kMaxDataTypeIndex(self):
        '''This is an enum of DataType.
        - Description: Valid entries are < kMaxDataTypeIndex. 
        - Value: 13
        '''
        pass

class MGeometryLegacy:
    '''MGeometryLegacy stores the collection of
MGeometryData arrays which describe a Maya surface, including per-component
data such as UV mapping and colour.
Various methods are provided for returning
MGeometryData containing the data for different properties of the geometry:
the
position() method returns position data, the
normal() method returns normals, and so on.
The
primitiveArray() method returns
MGeometryPrimitive's which provide indexing into those property arrays for each
primitive to be drawn.
'''
    def __init__(self):
        pass


    def primitiveArrayCount(self): 
        '''
        primitiveArrayCount(self) -> int

        Synopsis
        -----
        Get the number of primitive arrays for this surface.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def primitiveArray(self, arrayNumber: int): 
        '''
        primitiveArray(self, arrayNumber: int) -> const MGeometryPrimitive

        Synopsis
        -----
        Get the primitive indexing data for this surface. The surface
        geometry may consist of more than one MGeometryPrimitive, each
        representing an array of primitives. For example, if the surface
        was composed of both triangles and quads there might be one
        MGeometryPrimitive for the triangles and a second for the quads.
        The arrayNumber parameter is used to select between these.Each
        MGeometryPrimitive contains indices which are used to map the
        MGeometryData returned by the other methods of this class onto
        the primitives. For example, if the returned MGeometryPrimitive
        is for an array of triangles it will contain three indices for
        each triangle. Those indices can be used to index into the
        position data returned by the position() method, the normal data
        returned by the normal() method, and so on.

        Returns: 
        ----- 
        Primitive data structure, which may be empty.

        Parameters:
        -----
        arrayNumber: int
        	[in] -> Number of the index data to retrieve. Must be in the range 0 to 


        '''
        pass

    def position(self): 
        '''
        position(self) -> const MGeometryData

        Synopsis
        -----
        Get the position data for this surface.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def normal(self): 
        '''
        normal(self) -> const MGeometryData

        Synopsis
        -----
        Get the normal data for this surface.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def componentId(self): 
        '''
        componentId(self) -> const MGeometryData

        Synopsis
        -----
        Get the Maya component id data for this surface. This array
        allows you to correlate MGeometryLegacy entries with the
        corresponding component on the Maya surface (e.g. for meshes,
        this array will contains the vertex id).

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def texCoord(self, name: MString): 
        '''
        texCoord(self, name: MString) -> const MGeometryData

        Synopsis
        -----
        Get a texture coordinate set by name.

        Returns: 
        ----- 
        The texture coordinate data (which may be empty).

        Parameters:
        -----
        name: MString
        	[in] -> the name of the set to return


        '''
        pass

    def color(self, name: MString): 
        '''
        color(self, name: MString) -> const MGeometryData

        Synopsis
        -----
        Get a color set by name.

        Returns: 
        ----- 
        The color data (which may be empty).

        Parameters:
        -----
        name: MString
        	[in] -> the name of the set to return


        '''
        pass

    def tangent(self, name: MString): 
        '''
        tangent(self, name: MString) -> const MGeometryData

        Synopsis
        -----
        Get a tangent set by name.

        Returns: 
        ----- 
        The tangent data (which may be empty).

        Parameters:
        -----
        name: MString
        	[in] -> the name of the uv set tangent data should be returned for


        '''
        pass

    def binormal(self, name: MString): 
        '''
        binormal(self, name: MString) -> const MGeometryData

        Synopsis
        -----
        Get a binormal set by name.

        Returns: 
        ----- 
        The binormal data (which may be empty).

        Parameters:
        -----
        name: MString
        	[in] -> the name of the uv set binormal data should be returned for


        '''
        pass

    def data(self, what: MGeometryData.MGeometryData,
                        name: MString): 
        '''
        data(self, what: MGeometryData.MGeometryData,
                        name: MString) -> const MGeometryData

        Synopsis
        -----
        Get arbitrary surface data by name.

        Returns: 
        ----- 
        The geometry data (which may be empty).

        Parameters:
        -----
        what: MGeometryData.MGeometryData
        	[in] -> the type of data requested 

        name: MString
        	[in] -> the name of the data set requested


        '''
        pass

class MGeometryList:
    '''This class holds the set of data elements which represent a Maya
surface.
It provides iterated access to a list of geometry items, along
with the rendering context require to render them (e.g. matrix,
etc).
'''
    def __init__(self):
        pass


    def enum(self): 
        '''
        enum(self) -> anonymous

        Synopsis
        -----
        Bit flags for the geometry method that govern which OpenGL state
        Maya sets for you. No renderer setup is required for this
        element. Setup the model view matrix for this element. Setup the
        fixed function lighting state for this element. Setup the
        back/front face culling state for this element. Setup all
        renderer state for this element.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def isDone(self): 
        '''
        isDone(self) -> bool

        Synopsis
        -----
        Tests to see if the iterator has reached the end of the elements
        it contains. Once this method returns true, you should not call
        any further methods on the iterator.

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
        Advance to the next element in the iterator. This should only be
        called if the iterator indicates it has more elements through the
        isDone() method.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def reset(self): 
        '''
        reset(self)

        Synopsis
        -----
        Reset this iterator to the first element. This allows you to
        iterate multiple times through the list.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def length(self): 
        '''
        length(self) -> int

        Synopsis
        -----
        Query the total number of elements available through this
        iterator.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setCurrentElement(self, i: int): 
        '''
        setCurrentElement(self, i: int)

        Synopsis
        -----
        Randomly access the ith element in the iterator.

        Returns:
        -----
        None

        Parameters:
        -----
        i: int
        	[in] -> the index of the element you want to access 


        '''
        pass

    def geometry(self, setupFlags: int): 
        '''
        geometry(self, setupFlags: int) -> MGeometryLegacy

        Synopsis
        -----
        Get the geometry for the current element in the iterator.

        Returns: 
        ----- 
        The geometry for the current element.

        Parameters:
        -----
        setupFlags: int
        	[in] -> the parts of the rendering pipeline your shader needs setup in order to render. This can be any combination of kMatrices, kFixedFunctionLighting, kCulling, or kAll. For efficiency, you can avoid the overhead of setting up parts of the rendering pipeline not used by your shader (e.g. fixed function lighting).


        '''
        pass

    def objectToWorldMatrix(self): 
        '''
        objectToWorldMatrix(self) -> const MMatrix&

        Synopsis
        -----
        Get the object to world matrix for the current element in the
        iterator.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def projectionMatrix(self): 
        '''
        projectionMatrix(self) -> const MMatrix&

        Synopsis
        -----
        Get the camera project matrix for the current element in the
        iterator.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def viewMatrix(self): 
        '''
        viewMatrix(self) -> const MMatrix&

        Synopsis
        -----
        Get the camera view matrix for the current element in the
        iterator.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def path(self): 
        '''
        path(self) -> MDagPath

        Synopsis
        -----
        Get the dag path for the current element in the iterator.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def cullMode(self): 
        '''
        cullMode(self) -> MGeometryList.MGeometryList

        Synopsis
        -----
        Get the rendering cull mode to use for current element in the
        iterator.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def addLast(self, path: MDagPath,
                        components: MObject): 
        '''
        addLast(self, path: MDagPath,
                        components: MObject) -> bool

        Synopsis
        -----
        Add the geometry representing a shape to this geometry iterator.
        Note that you are only able to add geometry items to
        MGeometryLists you have created using the public constructor.
        Trying to add elements to an iterator passed to you from Maya
        (e.g. in a shader render call) will fail.

        Returns: 
        ----- 
        True if the element was added to the iterator, false otherwise.

        Parameters:
        -----
        path: MDagPath
        	[in] -> The DAG path for the shape to add 

        components: MObject
        	[in] -> The optional set of components (faces) to include in the geometry. A NULL value indicates the whole object should be added


        '''
        pass

    @overload
    def addLast(self, geometry: MGeometryLegacy,
                        matrix: MMatrix): 
        '''
        addLast(self, geometry: MGeometryLegacy,
                        matrix: MMatrix) -> bool

        Synopsis
        -----
        Add arbitrary geometry to this geometry iterator. Note that you
        are only able to add geometry items to MGeometryLists you have
        created using the public constructor. Trying to add elements to
        an iterator passed to you from Maya (e.g. in a shader render
        call) will fail.

        Returns: 
        ----- 
        True if the element was added to the iterator, false otherwise.

        Parameters:
        -----
        geometry: MGeometryLegacy
        	[in] -> the geometry cache to add 

        matrix: MMatrix
        	[in] -> the transformation to associate with this geometry


        '''
        pass

class MCullMode:
    '''Defines the culling modes to use when rendering this geometry. 
    Non-functional class.  Values for this enum:
    kCullNone
    kCullCW
    kCullCCW
    '''

    def __init__(self):
        pass

    def kCullNone(self):
        '''This is an enum of MCullMode.
        - Description: No culling should be performed on this geometry. 
        - Value: 0
        '''
        pass

    def kCullCW(self):
        '''This is an enum of MCullMode.
        - Description: Cull clockwise faces when rendering this geometry. 
        - Value: 1
        '''
        pass

    def kCullCCW(self):
        '''This is an enum of MCullMode.
        - Description: Cull counter-clockwise faces when rendering this geometry. 
        - Value: 2
        '''
        pass

class MGeometryManager:
    '''This class provides methods for managing MGeometry resources.
It provides an interface for loading and using hardware textures.
'''
    def __init__(self):
        pass


    def getGeometry(self, shape: MDagPath,
                        requirements: MGeometryRequirementsLegacy,
                        components: MObject): 
        '''
        getGeometry(self, shape: MDagPath,
                        requirements: MGeometryRequirementsLegacy,
                        components: MObject) -> MGeometryManager.OPENMAYA_MAJOR_NAMESPACE_OPEN MGeometryLegacy

        Synopsis
        -----
        Access the Geometry cache for a shape.

        Returns: 
        ----- 
        The cached geometry.

        Parameters:
        -----
        shape: MDagPath
        	[in] -> the surface 

        requirements: MGeometryRequirementsLegacy
        	[in] -> the surface data you want in the cache. Attempting to access cache data not included in the requirements will fail. 

        components: MObject
        	[in] -> an optional component group, for accessing a sub-selection of faces (e.g. the faces assigned to a material)


        '''
        pass

    def dereferenceDefaultGeometry(self, geomIterator: MGeometryList): 
        '''
        dereferenceDefaultGeometry(self, geomIterator: MGeometryList)

        Synopsis
        -----
        This is the companion method to referenceDefaultGeometry() and
        must always be called immediately after usage of data supplied by
        the reference call. This call simply maintains proper internal
        state for any data used.

        Returns:
        -----
        None

        Parameters:
        -----
        geomIterator: MGeometryList
        	[in] -> The geometry iterator returned from 


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

class GeometricShape:
    '''Default geometry shapes. 
    Non-functional class.  Values for this enum:
    kDefaultSphere
    kDefaultPlane
    kDefaultCube
    '''

    def __init__(self):
        pass

    def kDefaultSphere(self):
        '''This is an enum of GeometricShape.
        - Description: Sphere with radius 1, centered at 0,0,0. 
        - Value: 0
        '''
        pass

    def kDefaultPlane(self):
        '''This is an enum of GeometricShape.
        - Description: Plane with width and height of 1, centered at 0,0,0. Assuming "Y-Up" orientation: width = x-axis, and height = y-axis. 
        - Value: 1
        '''
        pass

    def kDefaultCube(self):
        '''This is an enum of GeometricShape.
        - Description: Cube with width, height and depth of 1, centered at 0,0,0. 
        - Value: 2
        '''
        pass

class MGeometryPrimitive:
    '''MGeometryPrimitive is a class describes the topology used for accessing
MGeometryData.
Topology is specified as a set of index values which references
into data elements in an
MGeometryData. Index values can be assumed to be stored in contiguous memory.
A "draw primitive type" indicates the format of the indexing as
follows:
Internal Maya data which is passed to the user via this class is
always assumed to be non-modifiable.
'''
    def __init__(self):
        pass


    def uniqueID(self): 
        '''
        uniqueID(self) -> int

        Synopsis
        -----
        Return the per session unique identifier.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def drawPrimitiveType(self): 
        '''
        drawPrimitiveType(self) -> MGeometryPrimitive.MGeometryPrimitive

        Synopsis
        -----
        Get the data type for the data.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def elementCount(self): 
        '''
        elementCount(self) -> int

        Synopsis
        -----
        Return element count.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def dataType(self): 
        '''
        dataType(self) -> MGeometryData.MGeometryData

        Synopsis
        -----
        Return element data type.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def data(self): 
        '''
        data(self) -> void*

        Synopsis
        -----
        Retrieve a pointer to the internal data.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class DrawPrimitiveType:
    '''Specifies the data primitive type constructed by the indexing array. 
    Non-functional class.  Values for this enum:
    kInvalidIndexType
    kPoints
    kLines
    kLineStrip
    kLineLoop
    kTriangles
    kTriangleStrip
    kTriangleFan
    kQuads
    kQuadStrip
    kPolygon
    kMaxDrawPrimitiveTypeIndex
    '''

    def __init__(self):
        pass

    def kInvalidIndexType(self):
        '''This is an enum of DrawPrimitiveType.
        - Description: Default value is not valid. 
        - Value: 0
        '''
        pass

    def kPoints(self):
        '''This is an enum of DrawPrimitiveType.
        - Description: Corresponds to GL_POINTS in OpenGL. 
        - Value: 1
        '''
        pass

    def kLines(self):
        '''This is an enum of DrawPrimitiveType.
        - Description: Corresponds to GL_LINES in OpenGL (individual unconnected line segments) 
        - Value: 2
        '''
        pass

    def kLineStrip(self):
        '''This is an enum of DrawPrimitiveType.
        - Description: Corresponds to GL_LINE_STRIP in OpenGL. 
        - Value: 3
        '''
        pass

    def kLineLoop(self):
        '''This is an enum of DrawPrimitiveType.
        - Description: Corresponds to GL_LINE_LOOP in OpenGL (non-filled, connected line segments) 
        - Value: 4
        '''
        pass

    def kTriangles(self):
        '''This is an enum of DrawPrimitiveType.
        - Description: Corresponds to GL_TRIANGLES In OpenGL. 
        - Value: 5
        '''
        pass

    def kTriangleStrip(self):
        '''This is an enum of DrawPrimitiveType.
        - Description: Corresponds to GL_TRIANGLE_STRIP in OpenGL. 
        - Value: 6
        '''
        pass

    def kTriangleFan(self):
        '''This is an enum of DrawPrimitiveType.
        - Description: Corresponds to GL_TRIANGLE_FAN in OpenGL. 
        - Value: 7
        '''
        pass

    def kQuads(self):
        '''This is an enum of DrawPrimitiveType.
        - Description: Corresponds to GL_QUADS in OpenGL. 
        - Value: 8
        '''
        pass

    def kQuadStrip(self):
        '''This is an enum of DrawPrimitiveType.
        - Description: Corresponds to GL_QUAD_STRIP in OpenGL. 
        - Value: 9
        '''
        pass

    def kPolygon(self):
        '''This is an enum of DrawPrimitiveType.
        - Description: Corresponds to GL_POLYGON in OpenGL. 
        - Value: 10
        '''
        pass

    def kMaxDrawPrimitiveTypeIndex(self):
        '''This is an enum of DrawPrimitiveType.
        - Description: Number of primitive types. 
        - Value: 11
        '''
        pass

class MGeometryRequirementsLegacy:
    '''MGeometryRequirementsLegacy stores the collection of MGeometryRequirementsData arrays which
describe a Maya surface, including per-component data such as UV
mapping and colour.
'''
    def __init__(self):
        pass


    def addPosition(self, dimension: int): 
        '''
        addPosition(self, dimension: int)

        Synopsis
        -----
        Add position to the set of required elements.

        Returns:
        -----
        None

        Parameters:
        -----
        dimension: int
        	[in] -> the size of the position requirement. Valid values are 3 and 4. Default is 3. 


        '''
        pass

    def addNormal(self, dimension: int): 
        '''
        addNormal(self, dimension: int)

        Synopsis
        -----
        Add normal to the set of required elements.

        Returns:
        -----
        None

        Parameters:
        -----
        dimension: int
        	[in] -> the size of the normal requirement. Valid values are 3 and 4. Default is 3. 


        '''
        pass

    def addTexCoord(self, name: MString): 
        '''
        addTexCoord(self, name: MString)

        Synopsis
        -----
        Add a texture coordinate set to the list of required elements.

        Returns:
        -----
        None

        Parameters:
        -----
        name: MString
        	[in] -> the name of the uv set to add 


        '''
        pass

    def addTangent(self, name: MString,
                        dimension: int): 
        '''
        addTangent(self, name: MString,
                        dimension: int)

        Synopsis
        -----
        Add a tangent set to the list of required elements.

        Returns:
        -----
        None

        Parameters:
        -----
        name: MString
        	[in] -> the name of the uv set to add tangent data for 

        dimension: int
        	[in] -> the size of the normal requirement. Valid values are 3 and 4. Default is 3. 


        '''
        pass

    def addBinormal(self, name: MString,
                        dimension: int): 
        '''
        addBinormal(self, name: MString,
                        dimension: int)

        Synopsis
        -----
        Add a binormal set to the list of required elements.

        Returns:
        -----
        None

        Parameters:
        -----
        name: MString
        	[in] -> the name of the uv set to add binormal data for 

        dimension: int
        	[in] -> the size of the normal requirement. Valid values are 3 and 4. Default is 3. 


        '''
        pass

    def addColor(self, name: MString): 
        '''
        addColor(self, name: MString)

        Synopsis
        -----
        Add a color set to the list of required elements.

        Returns:
        -----
        None

        Parameters:
        -----
        name: MString
        	[in] -> the name of the color set to add 


        '''
        pass

    def addFaceOffsets(self): 
        '''
        addFaceOffsets(self)

        Synopsis
        -----
        Add face offsets to the set of required elements. Face offsets
        are used internally to calculate component-indexed data such as
        shading group membership. Note that geometry data is cached
        internally, so it is important to call this method whenever you
        use MGeometryRequirementsLegacy if you will ever require this
        information.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MGLFunctionTable:
    '''The best cross platform alternative for drawing in Viewport 2.0
is via
MHWRender::MVertexBuffer,
MHWRender::MPxGeometryOverride, and other classes providing an abstraction from the underlying
hardware API.
The
MHWRender::MUIDrawManager offers handy options for very simple drawing commands.
Drawing in raw OpenGL mode will still be allowed, but we
recommend you use the core profile subset of the OpenGL API to
ensure compatibility with future versions of Maya.
MGLFunctionTable is a utility class which provides wrappers for the basic
functions in the OpenGL API.
Core functions up to OpenGL 2.0 are provided here, as well as a
number of ARB/EXT and vendor specific extensions. Refer to the
MGLExtension enumeration for extensions which are checked.
Please refer to an OpenGL reference for usage of the OpenGL
functions provided in this wrapper class.
When using the functions provided, the standard GL* type and
constant definitions to be used can be found in MGLDefinitions.h.
MGLDefinitions.h basically provides a wrapper for what would
normally be found in gl.h and glext.h files.
The naming convention used in this file is to take the regular
GL* definitions and add a "M" prefix. This is to avoid conflicts
with existing type and constant declarations which may be found
in files such as gl.h and glext.h. It is recommended that
externally provided files which have GL definitions not be
included in the same C++ file to avoid conflicts.
MGLFunctionTable cannot be created on its own, and must be retrieved via a method
on the
MHardwareRenderer class. It is possible that this class will not be available, if
the hardware renderer class cannot be instantiated. This would be
due to insufficient graphics hardware support.
Below is an example of initializing and using the function table
to draw a simple 3-line axis. Note the usage of the definitions
from MGLDefinitions such as MGL_LIGHTING versus GL_LIGHTING, and
MGL_LINES and MGL_DEPTH_TEST.
Here is a similar example of using the function table in Python.
'''
    def __init__(self):
        pass


    def extensionExists(self, extension: MGLFunctionTable.MGLExtension): 
        '''
        extensionExists(self, extension: MGLFunctionTable.MGLExtension) -> MGLFunctionTable.OPENMAYA_MAJOR_NAMESPACE_OPENbool

        Synopsis
        -----
        Provides information as to whether a given OpenGL extension
        exists. That is, the extension is reported to be supported.

        Returns: 
        ----- 
        true if the extension exists, false otherwise.

        Parameters:
        -----
        extension: MGLFunctionTable.MGLExtension
        	[in] -> Extension enumeration.


        '''
        pass

    def numTexUnits(self): 
        '''
        numTexUnits(self) -> int

        Synopsis
        -----
        Get information about the maximum number of texture units. This
        may not be the same as the number of interpolants available.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def numTexInterpolants(self): 
        '''
        numTexInterpolants(self) -> int

        Synopsis
        -----
        Get information about the maximum number of texture interpolants.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def numTexImageUnits(self): 
        '''
        numTexImageUnits(self) -> int

        Synopsis
        -----
        Get information about the maximum number of texture image units
        available.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def maxTextureSize(self): 
        '''
        maxTextureSize(self) -> int

        Synopsis
        -----
        Get information about the maximum texture size.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def maxVertexAttributes(self): 
        '''
        maxVertexAttributes(self) -> int

        Synopsis
        -----
        Get information about the maximum number of vertex attributes
        available.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MGLversion:
    '''OpenGL versions checked. 
    Non-functional class.  Values for this enum:
    kMGL_Version11
    kMGL_Version12
    kMGL_Version121
    kMGL_Version13
    kMGL_Version14
    kMGL_Version15
    kMGL_Version20
    '''

    def __init__(self):
        pass

    def kMGL_Version11(self):
        '''This is an enum of MGLversion.
        - Description: GL 1.1. 
        - Value: 0
        '''
        pass

    def kMGL_Version12(self):
        '''This is an enum of MGLversion.
        - Description: GL 1.2. 
        - Value: 1
        '''
        pass

    def kMGL_Version121(self):
        '''This is an enum of MGLversion.
        - Description: GL 1.2.1. 
        - Value: 2
        '''
        pass

    def kMGL_Version13(self):
        '''This is an enum of MGLversion.
        - Description: GL 1.3.1. 
        - Value: 3
        '''
        pass

    def kMGL_Version14(self):
        '''This is an enum of MGLversion.
        - Description: GL 1.4.1. 
        - Value: 4
        '''
        pass

    def kMGL_Version15(self):
        '''This is an enum of MGLversion.
        - Description: GL 1.5. 
        - Value: 5
        '''
        pass

    def kMGL_Version20(self):
        '''This is an enum of MGLversion.
        - Description: GL 2.0. 
        - Value: 6
        '''
        pass

class MHardwareRenderer:
    '''Static hardware renderer interface class.
MHardwareRenderer is an interface class which wraps the hardware renderer.
'''
    def __init__(self):
        pass


    def getCurrentExposureNumber(self, backEndString: MString,
                        number: int): 
        '''
        getCurrentExposureNumber(self, backEndString: MString,
                        number: int)

        Synopsis
        -----
        This method returns the current exposure number during rendering.
        If the renderer is not currently rendering a value of 0 is
        returned as the current exposure number.

        Returns:
        -----
        None

        Parameters:
        -----
        backEndString: MString
        	[in] -> Backend string. 

        number: int
        	[out] -> Current exposure number


        '''
        pass

    def getTotalExposureCount(self, backEndString: MString,
                        number: int): 
        '''
        getTotalExposureCount(self, backEndString: MString,
                        number: int)

        Synopsis
        -----
        This method returns the total number of exposures for rendering a
        single frame. If the renderer is not currently rendering a value
        of 0 is returned as the total exposure count.

        Returns:
        -----
        None

        Parameters:
        -----
        backEndString: MString
        	[in] -> Backend string. 

        number: int
        	[out] -> Total exposure count.


        '''
        pass

    def makeSwatchContextCurrent(self, backEndString: MString,
                        desiredWidth: int,
                        desiredHeight: int): 
        '''
        makeSwatchContextCurrent(self, backEndString: MString,
                        desiredWidth: int,
                        desiredHeight: int)

        Synopsis
        -----
        The swatch context is a "scratch" context which can be used to
        hardware render an image for swatch display. The swatch context
        has the following pixel format:The maximum context size is 512 by
        512, and the minimum size : 64 by 64. The actual maximum size is
        dependent on the video card and available memory resources.This
        method makes the swatch context "current", and should be called
        before attempting to draw anything for swatch rendering.The
        desired image width and height represents the desired viewport
        size to render. These values will be clamped between the minimum
        and maximum values of the swatch context.If for any reason the
        swatch context cannot be made current, no rendering should be
        performed as the destination of the rendering is undefined.This
        method should never be called while in the middle of drawing to
        another context (e.g. during MPxHwShaderNode::glGeometry()) as
        draw calls will be redirected to the swatch context.e.g. Refer to
        MPxHwShaderNode::renderSwatchImage() for swatch rendering for
        hardware shaders for more details on the usage of this method.

        Returns:
        -----
        None

        Parameters:
        -----
        backEndString: MString
        	[in] -> 

        desiredWidth: int
        	[in] -> 

        desiredHeight: int
        	[in] -> 


        '''
        pass

    def readSwatchContextPixels(self, backEndString: MString,
                        image: MImage): 
        '''
        readSwatchContextPixels(self, backEndString: MString,
                        image: MImage)

        Synopsis
        -----
        Read the contents of the swatch context into an MImage. MImage is
        assumed to be of the correct pixel format (24-bit RGBA, with
        8-bits per channel). MImage is assumed to also have pre-allocated
        the correct amount of data as this routine will copy the swatch
        context contents directly into the MImage.If the swatch context
        is not available for any reason, or MImage has not been properly
        set up, then a failure condition will be returned.

        Returns:
        -----
        None

        Parameters:
        -----
        backEndString: MString
        	[in] -> Backend string. 

        image: MImage
        	[out] -> MImage


        '''
        pass

    def getSwatchOrthoCameraSetting(self, l: double,
                        r: double,
                        b: double,
                        t: double,
                        n: double,
                        f: double): 
        '''
        getSwatchOrthoCameraSetting(self, l: double,
                        r: double,
                        b: double,
                        t: double,
                        n: double,
                        f: double)

        Synopsis
        -----
        This method returns an orthographics camera clipping plane values
        which form the camera viewing volume. These values are the
        default values used for rendering the swatch.

        Returns:
        -----
        None

        Parameters:
        -----
        l: double
        	[out] -> The left side clipping plane 

        r: double
        	[out] -> The right side clipping plane 

        b: double
        	[out] -> The bottom side clipping plane 

        t: double
        	[out] -> The top side clipping plane 

        n: double
        	[out] -> The near side clipping plane 

        f: double
        	[out] -> The far side clipping plane 


        '''
        pass

    def getSwatchPerspectiveCameraSetting(self, l: double,
                        r: double,
                        b: double,
                        t: double,
                        n: double,
                        f: double): 
        '''
        getSwatchPerspectiveCameraSetting(self, l: double,
                        r: double,
                        b: double,
                        t: double,
                        n: double,
                        f: double)

        Synopsis
        -----
        This method returns a perspective camera clipping plane values
        which form the camera viewing volume. These values are the
        default values used for rendering the swatch.

        Returns:
        -----
        None

        Parameters:
        -----
        l: double
        	[out] -> The left side clipping plane 

        r: double
        	[out] -> The right side clipping plane 

        b: double
        	[out] -> The bottom side clipping plane 

        t: double
        	[out] -> The top side clipping plane 

        n: double
        	[out] -> The near side clipping plane 

        f: double
        	[out] -> The far side clipping plane 


        '''
        pass

    def getSwatchPerspectiveCameraTranslation(self, x: float,
                        y: float,
                        z: float,
                        w: float): 
        '''
        getSwatchPerspectiveCameraTranslation(self, x: float,
                        y: float,
                        z: float,
                        w: float)

        Synopsis
        -----
        This method returns a perspective camera 3D translation values.
        These are the default values used for rendering the swatch.

        Returns:
        -----
        None

        Parameters:
        -----
        x: float
        	[out] -> The value for the x coord component 

        y: float
        	[out] -> The value for the y coord component 

        z: float
        	[out] -> The value for the z coord component 

        w: float
        	[out] -> The value for the w coord component 


        '''
        pass

    def getSwatchLightDirection(self, x: float,
                        y: float,
                        z: float,
                        w: float): 
        '''
        getSwatchLightDirection(self, x: float,
                        y: float,
                        z: float,
                        w: float)

        Synopsis
        -----
        This method returns the direction vector of the default
        directional light used for rendering the swatch.

        Returns:
        -----
        None

        Parameters:
        -----
        x: float
        	[out] -> The value for the x coord component 

        y: float
        	[out] -> The value for the y coord component 

        z: float
        	[out] -> The value for the z coord component 

        w: float
        	[out] -> The value for the w coord component 


        '''
        pass

    def drawSwatchBackGroundQuads(self, quadColor: MColor,
                        textured: bool,
                        numberOfRepeats: int): 
        '''
        drawSwatchBackGroundQuads(self, quadColor: MColor,
                        textured: bool,
                        numberOfRepeats: int)

        Synopsis
        -----
        This draws a set of quads in a checkboard pattern. Areas that are
        not drawn will have the background color show through.By default
        the checker repeat is 8, but can be overridden by the user.By
        default the quad colour is opaque grey, but can be overridden by
        the user.By default the quads are not drawn textured. This can be
        overridden by the user.The quads will completely cover the entire
        background.

        Returns:
        -----
        None

        Parameters:
        -----
        quadColor: MColor
        	[in] -> The value for the quad color. Default is RGBA(0.5,0.5,0.5,1.0); 

        textured: bool
        	[in] -> Whether to draw with texture coordinates. Default is false. 

        numberOfRepeats: int
        	[in] -> Number of checkerboard repeats. Default is 8. 


        '''
        pass

class DrawProcedureStatusCode:
    '''Draw Procedure status codes. 
    Non-functional class.  Values for this enum:
    kSuccess
    kFailure
    kItemExists
    kItemNotFound
    kLocationNotFound
    '''

    def __init__(self):
        pass

    def kSuccess(self):
        '''This is an enum of DrawProcedureStatusCode.
        - Description: Success. 
        - Value: 0
        '''
        pass

    def kFailure(self):
        '''This is an enum of DrawProcedureStatusCode.
        - Description: Failure. 
        - Value: 1
        '''
        pass

    def kItemExists(self):
        '''This is an enum of DrawProcedureStatusCode.
        - Description: Item already exists. 
        - Value: 2
        '''
        pass

    def kItemNotFound(self):
        '''This is an enum of DrawProcedureStatusCode.
        - Description: Item is not found. 
        - Value: 3
        '''
        pass

    def kLocationNotFound(self):
        '''This is an enum of DrawProcedureStatusCode.
        - Description: Location not found. 
        - Value: 4
        '''
        pass

class BufferPixelFormat:
    '''Specify the pixel format of the current buffer. 
    Non-functional class.  Values for this enum:
    kRGBA_Fix8
    kRGBA_Float16
    kDepth_Float32
    '''

    def __init__(self):
        pass

    def kRGBA_Fix8(self):
        '''This is an enum of BufferPixelFormat.
        - Description: 8 bit Red, Green, Blue, and Alpha channel 
        - Value: 0
        '''
        pass

    def kRGBA_Float16(self):
        '''This is an enum of BufferPixelFormat.
        - Description: 16 bit Red, Green, Blue, and Alpha channel 
        - Value: 1
        '''
        pass

    def kDepth_Float32(self):
        '''This is an enum of BufferPixelFormat.
        - Description: 32 bit floating point depth buffer 
        - Value: 2
        '''
        pass

class CallLocation:
    '''Draw Procedure call locations. 
    Non-functional class.  Values for this enum:
    kPreRendering
    kPreExposure
    kPostExposure
    kPostRendering
    '''

    def __init__(self):
        pass

    def kPreRendering(self):
        '''This is an enum of CallLocation.
        - Description: Before rendering one frame. No model or view matrices. 
        - Value: 0
        '''
        pass

    def kPreExposure(self):
        '''This is an enum of CallLocation.
        - Description: Before rendering one "exposure". If multiple exposures are are required to render one frame. After the frame buffer is cleared and model and view matrices are set up for the current exposure. 
        - Value: 1
        '''
        pass

    def kPostExposure(self):
        '''This is an enum of CallLocation.
        - Description: After rendering one "exposure". 
        - Value: 2
        '''
        pass

    def kPostRendering(self):
        '''This is an enum of CallLocation.
        - Description: After rendering one frame. Before a possible fame buffer swap. 
        - Value: 3
        '''
        pass

class GeometricShape:
    '''Default geometry shapes. 
    Non-functional class.  Values for this enum:
    kDefaultSphere
    kDefaultPlane
    kDefaultCube
    '''

    def __init__(self):
        pass

    def kDefaultSphere(self):
        '''This is an enum of GeometricShape.
        - Description: Sphere with radius 1, centered at 0,0,0. 
        - Value: 0
        '''
        pass

    def kDefaultPlane(self):
        '''This is an enum of GeometricShape.
        - Description: Plane with width and height of 1, centered at 0,0,0. Assuming "Y-Up" orientation: width = x-axis, and height = y-axis. 
        - Value: 1
        '''
        pass

    def kDefaultCube(self):
        '''This is an enum of GeometricShape.
        - Description: Cube with width, height and depth of 1, centered at 0,0,0. 
        - Value: 2
        '''
        pass

class MHwrCallback:
    '''Rendering Callbacks.
This class is used to register callbacks to gain access to Maya's
Hardware Rendering device status. You can be notified of device
creation, lost reset and deletion.
To register callbacks, inherit from this class and override
deviceNew, deviceLost, deviceReset, deviceDeleted. Any number of
these methods can be overridden by the callback. Then register
the callbacks by calling the
addCallback() method.
If multiple callbacks need to be registered, the order of
invocation can be set by adding each callback with a priority
number, 0 being the highest priority.
'''
    def __init__(self):
        pass


    def addCallback(self, callback: MHwrCallback,
                        priority: int): 
        '''
        addCallback(self, callback: MHwrCallback,
                        priority: int)

        Synopsis
        -----
        Static procedure to add a rendering callback. The callbacks are
        stored internally in a sorted list and are invoked following the
        appropriate device state change depending on which methods are
        overridden. Adding the same callback more than once will have no
        effect.

        Returns:
        -----
        None

        Parameters:
        -----
        callback: MHwrCallback
        	[in] -> object to add to the list of callbacks to invoke 

        priority: int
        	[in] -> priority for this callback, lower priorities are invoked first 


        '''
        pass

    def removeCallback(self, callback: MHwrCallback): 
        '''
        removeCallback(self, callback: MHwrCallback)

        Synopsis
        -----
        Static procedure to remove a rendering callback. The callback
        will be removed from the list of callbacks, but its up to the
        client to actually delete the object. Unstability may result if a
        callback is deleted and not removed from the callback
        list.Removing an un-installed callback will have no effect.

        Returns:
        -----
        None

        Parameters:
        -----
        callback: MHwrCallback
        	[in] -> object to remove from the list of callbacks 


        '''
        pass

class MHwTextureManager:
    '''The
MHwTextureManager provides an interface for loading and using hardware textures.
'''
    def __init__(self):
        pass


    @overload
    def glBind(self, fileTextureObject: MObject,
                        targetType: MImageFileInfo.MImageFileInfo,
                        imageType: MImageFileInfo.MImageFileInfo): 
        '''
        glBind(self, fileTextureObject: MObject,
                        targetType: MImageFileInfo.MImageFileInfo,
                        imageType: MImageFileInfo.MImageFileInfo) -> MHwTextureManager.OPENMAYA_MAJOR_NAMESPACE_OPEN MStatus

        Synopsis
        -----
        Bind the contents of a file texture node to the currently active
        OpenGL texture unit.

        Returns:
        -----
        None

        Parameters:
        -----
        fileTextureObject: MObject
        	[in] -> 

        targetType: MImageFileInfo.MImageFileInfo
        	[in] -> 

        imageType: MImageFileInfo.MImageFileInfo
        	[in] -> 


        '''
        pass

    @overload
    def glBind(self, fileTextureConnection: MPlug,
                        targetType: MImageFileInfo.MImageFileInfo,
                        imageType: MImageFileInfo.MImageFileInfo): 
        '''
        glBind(self, fileTextureConnection: MPlug,
                        targetType: MImageFileInfo.MImageFileInfo,
                        imageType: MImageFileInfo.MImageFileInfo)

        Synopsis
        -----
        Bind the contents of a specific file texture node attribute (e.g.
        color, alpha) to the currently active OpenGL texture unit. As
        part of this operation, the texture target will also be enabled
        (i.e. there is no need to call glEnable( targetType) before or
        after calling this method).

        Returns:
        -----
        None

        Parameters:
        -----
        fileTextureConnection: MPlug
        	[in] -> 

        targetType: MImageFileInfo.MImageFileInfo
        	[in] -> 

        imageType: MImageFileInfo.MImageFileInfo
        	[in] -> 


        '''
        pass

    def registerTextureFile(self, fileName: MString,
                        hTexture: MHwTextureManager.MHwTextureFileHandle): 
        '''
        registerTextureFile(self, fileName: MString,
                        hTexture: MHwTextureManager.MHwTextureFileHandle)

        Synopsis
        -----
        Register a named texture file. Returns a handle to a texture
        entry in the texture manager. The caller is responsible for
        calling the associated deregisterTextureFile to avoid leaking
        memory.

        Returns:
        -----
        None

        Parameters:
        -----
        fileName: MString
        	[in] -> the texture file to register 

        hTexture: MHwTextureManager.MHwTextureFileHandle
        	[out] -> the output handle to a texture entry representing the given file.


        '''
        pass

    def deregisterTextureFile(self, hTexture: MHwTextureManager.MHwTextureFileHandle): 
        '''
        deregisterTextureFile(self, hTexture: MHwTextureManager.MHwTextureFileHandle)

        Synopsis
        -----
        Deregisters the given handle to a texture entry in the manager.
        If there are no other handles to this texture entry, the texture
        resource will be freed.This method assumes that a context is
        already set. Failing to have a valid current context when
        invoking this method will cause a memory leak.

        Returns:
        -----
        None

        Parameters:
        -----
        hTexture: MHwTextureManager.MHwTextureFileHandle
        	[in] -> the texture handle to release


        '''
        pass

    def textureFile(self, hTexture: MHwTextureManager.MHwTextureFileHandle,
                        fileName: MString): 
        '''
        textureFile(self, hTexture: MHwTextureManager.MHwTextureFileHandle,
                        fileName: MString)

        Synopsis
        -----
        Return the file name associated with a given texture file handle.

        Returns:
        -----
        None

        Parameters:
        -----
        hTexture: MHwTextureManager.MHwTextureFileHandle
        	[in] -> the texture handle to query 

        fileName: MString
        	[in] -> the output file name


        '''
        pass

    @overload
    def glBind(self, hTexture: MHwTextureManager.MHwTextureFileHandle,
                        targetType: MImageFileInfo.MImageFileInfo,
                        imageType: MImageFileInfo.MImageFileInfo): 
        '''
        glBind(self, hTexture: MHwTextureManager.MHwTextureFileHandle,
                        targetType: MImageFileInfo.MImageFileInfo,
                        imageType: MImageFileInfo.MImageFileInfo)

        Synopsis
        -----
        Bind the contents of a specific file to the currently active
        OpenGL texture unit. As part of this operation, the texture
        target will also be enabled (i.e. there is no need to call
        glEnable( targetType) before or after calling this method).

        Returns:
        -----
        None

        Parameters:
        -----
        hTexture: MHwTextureManager.MHwTextureFileHandle
        	[in] -> 

        targetType: MImageFileInfo.MImageFileInfo
        	[in] -> 

        imageType: MImageFileInfo.MImageFileInfo
        	[in] -> 


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

class MLightLinks:
    '''Class providing read-only Light Linking API functions.
This class provides read-only access to the light linking
information expressed in Maya's light linker nodes.
To extract Maya's light linking information, use the following
sequence of calls:
Lights can be linked either to DAG hierarchies or to shading
groups. Additionnally, light linking information can store a list
of illuminating lights and a list excluded lights. The algorithm
used to determine which light should contribute can be described
by the pseudo code below.
for each face group on the object, corresponding to each shading
engine, do the following:
For the given face group, the set of lights illuminating it are
then (ObjectLink - FaceIgnore) + (FaceLink - ObjectIgnore).
It is important to note that component linking works at the
granularity of a shading group on a surface. In order to get
results from the
MLightLinks API, it is necessary to pass in components that correspond
exactly to all the faces on that object in a particular shading
group. For example, if pPlaneShape1.f[0:10] belongs to a shading
group which is linked to a given light, then there will be no
result from
MLightLinks::getLinkedLights() if the argument is set to pPlaneShape1.f[0], or
pPlaneShape1.f[0:5], or pPlaneShape1.f[10], etc - it must be
exactly pPlaneShape1.f[0:10].
'''
    def __init__(self):
        pass


    def parseLinks(self, linkNode: MObject,
                        verbose: bool,
                        stream: std.std,
                        useIgnore: bool,
                        componentSupport: bool): 
        '''
        parseLinks(self, linkNode: MObject,
                        verbose: bool,
                        stream: std.std,
                        useIgnore: bool,
                        componentSupport: bool)

        Synopsis
        -----
        Compiles the information contained in a light linker node into a
        table of object/light links. The getLinkedLights() and
        getLinkedObjects() methods are used to query this table.Whenever
        light linking information changes (objects are added/deleted or
        links are made/broken), the parseLinks() method must be called to
        update the table with the new link information, otherwise the
        query methods will return outdated information.

        Returns:
        -----
        None

        Parameters:
        -----
        linkNode: MObject
        	[in] -> The light linker node to be parsed. If this parameter is set to the null object (the default), then all light linker nodes in the scene will be parsed. It is highly recommended that this default be used. 

        verbose: bool
        	[in] -> Enables verbose output from the parsing procedure (default false). 

        stream: std.std
        	[in] -> Stream to which debugging information is output when 'verbose' is set to true. 

        useIgnore: bool
        	[in] -> light/object relationship will be queried using getIgnoreObjects or getIgnoreLights. getLinkedObjects and getLinkedLights are not affected. 

        componentSupport: bool
        	[in] -> Use component level light links where specified.


        '''
        pass

    def getLinkedLights(self, objectPath: MDagPath,
                        objectComponent: MObject,
                        linkedLights: MDagPathArray): 
        '''
        getLinkedLights(self, objectPath: MDagPath,
                        objectComponent: MObject,
                        linkedLights: MDagPathArray)

        Synopsis
        -----
        Queries the light link table to find the lights that are linked
        to a particular object or object component. parseLinks() must
        have been called at some point to generate the table that is
        being queried.

        Returns:
        -----
        None

        Parameters:
        -----
        objectPath: MDagPath
        	[in] -> The object whose linked lights are desired. 

        objectComponent: MObject
        	[in] -> If non-null, specifies that only lights linked to the specified component on the object should be returned. Otherwise, only lights linked to the entire object will be returned. 

        linkedLights: MDagPathArray
        	[out] -> Returns the DAG paths of the lights linked to the specified object or component.


        '''
        pass

    def getLinkedObjects(self, lightPath: MDagPath,
                        linkedObjects: MSelectionList): 
        '''
        getLinkedObjects(self, lightPath: MDagPath,
                        linkedObjects: MSelectionList)

        Synopsis
        -----
        Queries the light link table to find the objects or object
        components that are linked to a particular light. parseLinks()
        must have been called at some point to generate the table that is
        being queried.

        Returns:
        -----
        None

        Parameters:
        -----
        lightPath: MDagPath
        	[in] -> The light whose linked objects are desired. 

        linkedObjects: MSelectionList
        	[out] -> Returns the list of objects/components that are linked to the specified light.


        '''
        pass

    def getIgnoredLights(self, objectPath: MDagPath,
                        objectComponent: MObject,
                        ignoredLights: MDagPathArray): 
        '''
        getIgnoredLights(self, objectPath: MDagPath,
                        objectComponent: MObject,
                        ignoredLights: MDagPathArray)

        Synopsis
        -----
        Queries the light link table to find the lights that ignores a
        particular object or object component. parseLinks() must have
        been called at some point to generate the table that is being
        queried.

        Returns:
        -----
        None

        Parameters:
        -----
        objectPath: MDagPath
        	[in] -> The object whose linked lights are desired. 

        objectComponent: MObject
        	[in] -> If non-null, specifies that only lights that ignore the specified component on the object should be returned. Otherwise, only lights that ignore the entire object will be returned. 

        ignoredLights: MDagPathArray
        	[out] -> Returns the DAG paths of the lights that ignores the specified object or component.


        '''
        pass

    def getIgnoredObjects(self, lightPath: MDagPath,
                        ignoredObjects: MSelectionList): 
        '''
        getIgnoredObjects(self, lightPath: MDagPath,
                        ignoredObjects: MSelectionList)

        Synopsis
        -----
        Queries the light link table to find the objects or object
        components that are ignored to a particular light. parseLinks()
        must have been called at some point to generate the table that is
        being queried.

        Returns:
        -----
        None

        Parameters:
        -----
        lightPath: MDagPath
        	[in] -> The light whose ignored objects are desired. 

        ignoredObjects: MSelectionList
        	[out] -> Returns the list of objects/components that are ignored to the specified light.


        '''
        pass

    def getShadowLinkedLights(self, objectPath: MDagPath,
                        objectComponent: MObject,
                        linkedLights: MDagPathArray): 
        '''
        getShadowLinkedLights(self, objectPath: MDagPath,
                        objectComponent: MObject,
                        linkedLights: MDagPathArray)

        Synopsis
        -----
        Queries the light link table to find the lights that are shadow
        linked to a particular object or object component. parseLinks()
        must have been called at some point to generate the table that is
        being queried.

        Returns:
        -----
        None

        Parameters:
        -----
        objectPath: MDagPath
        	[in] -> The object whose shadow linked lights are desired. 

        objectComponent: MObject
        	[in] -> If non-null, specifies that only lights shadow linked to the specified component on the object should be returned. Otherwise, only lights shadow linked to the entire object will be returned. 

        linkedLights: MDagPathArray
        	[out] -> Returns the DAG paths of the lights shadow linked to the specified object or component.


        '''
        pass

    def getShadowLinkedObjects(self, lightPath: MDagPath,
                        linkedObjects: MSelectionList): 
        '''
        getShadowLinkedObjects(self, lightPath: MDagPath,
                        linkedObjects: MSelectionList)

        Synopsis
        -----
        Queries the light link table to find the objects or object
        components that are shadow linked to a particular light.
        parseLinks() must have been called at some point to generate the
        table that is being queried.

        Returns:
        -----
        None

        Parameters:
        -----
        lightPath: MDagPath
        	[in] -> The light whose shadow linked objects are desired. 

        linkedObjects: MSelectionList
        	[out] -> Returns the list of objects/components that are shadow linked to the specified light.


        '''
        pass

    def getShadowIgnoredLights(self, objectPath: MDagPath,
                        objectComponent: MObject,
                        ignoredLights: MDagPathArray): 
        '''
        getShadowIgnoredLights(self, objectPath: MDagPath,
                        objectComponent: MObject,
                        ignoredLights: MDagPathArray)

        Synopsis
        -----
        Queries the light link table to find the lights that ignore a
        particular object or object component when casting shadows. This
        is referred to as shadow ignoring the objects. parseLinks() must
        have been called at some point to generate the table that is
        being queried.

        Returns:
        -----
        None

        Parameters:
        -----
        objectPath: MDagPath
        	[in] -> The object whose shadow ignored lights are desired. 

        objectComponent: MObject
        	[in] -> If non-null, specifies that only lights that shadow ignore the specified component on the object should be returned. Otherwise, only lights that shadow ignore the entire object will be returned. 

        ignoredLights: MDagPathArray
        	[out] -> Returns the DAG paths of the lights that shadow ignores the specified object or component.


        '''
        pass

    def getShadowIgnoredObjects(self, lightPath: MDagPath,
                        ignoredObjects: MSelectionList): 
        '''
        getShadowIgnoredObjects(self, lightPath: MDagPath,
                        ignoredObjects: MSelectionList)

        Synopsis
        -----
        Queries the light link table to find the objects or object
        components that are ignored to a particular light when
        calculating shadows. These are referred to as shadow ignored
        objects. parseLinks() must have been called at some point to
        generate the table that is being queried.

        Returns:
        -----
        None

        Parameters:
        -----
        lightPath: MDagPath
        	[in] -> The light whose shadow ignored objects are desired. 

        ignoredObjects: MSelectionList
        	[out] -> Returns the list of objects/components that are shadow ignored to the specified light.


        '''
        pass

class MRenderingInfo:
    '''Information to perform rendering into a hardware render target.
MRenderingInfo is a class which holds information about rendering into hardware
render targets.
'''
    def __init__(self):
        pass


    def originX(self): 
        '''
        originX(self) -> MRenderingInfo.OPENMAYA_MAJOR_NAMESPACE_OPENint

        Synopsis
        -----
        Origin (x) of region to render to in pixels. Return the x
        coordinate in pixels of the origin of the region to render.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def originY(self): 
        '''
        originY(self) -> int

        Synopsis
        -----
        Origin (y) of region to render to in pixels. Return the y
        coordinate in pixels of the origin of the region to render.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def width(self): 
        '''
        width(self) -> int

        Synopsis
        -----
        Width of region to render in pixels. Return the width in pixels
        of the region to render.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def height(self): 
        '''
        height(self) -> int

        Synopsis
        -----
        Height of region to render in pixels. Return the width in pixels
        of the region to render.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def renderingAPI(self): 
        '''
        renderingAPI(self) -> MViewportRenderer.MViewportRenderer

        Synopsis
        -----
        Native target rendering API. Return the native rendering API used
        for a render target.See MViewportRender::RenderingAPI for a list
        of possible api values that can be returned.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def renderingVersion(self): 
        '''
        renderingVersion(self) -> float

        Synopsis
        -----
        Native target rendering version. Return the native rendering API
        version used for a render target.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def cameraPath(self): 
        '''
        cameraPath(self) -> const MDagPath&

        Synopsis
        -----
        Current camera being used to render with. Return the dag path of
        the current camera being used for rendering.Information about the
        camera itself can be extracted via MFnCamera.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def renderTarget(self): 
        '''
        renderTarget(self) -> const MRenderTargetLegacy&

        Synopsis
        -----
        Current render target. Return the current render target being
        used for rendering.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def viewMatrix(self): 
        '''
        viewMatrix(self) -> const MMatrix&

        Synopsis
        -----
        Current view matrix. Return the current view matrix being used
        for rendering.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def projectionMatrix(self): 
        '''
        projectionMatrix(self) -> const MMatrix&

        Synopsis
        -----
        Current projection matrix. Return the current projection matrix
        being used for rendering.The projection matrix will be
        appropriate regardless of whether the caller is rendering into a
        OpenGL or a DirectX context, as each drawing API interprets
        projection matrices differently.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MRenderCallback:
    '''Rendering Callbacks.
This class is used to register callbacks to gain access to Maya's
rendering information during software rendering. You can modify
Maya's shadow maps, RGB pixmap, and depth map to composite your
own rendering effects into Maya's rendering.
To register callbacks, inherit from this class and override
renderCallback(),
shadowCastCallback(), or
postProcessCallback(). Any number of these methods can be overridden by the callback.
Then register the callbacks by calling the
addCallback() method.
Each of the callback method gets passed a
MRenderData which contains the information.
MRenderData also provides utility methods for converting between world space
and screen space. In the case of shadowCastCallback,
MRenderShadowData is provided and it also has utility methods for converting
between world space and shadow map space.
If there are callbacks registered, prior to shadow maps being
written out,
shadowCastCallback() will be invoked with light information and a pointer to the
shadow map passed in. Then immediately after software rendering
completes,
renderCallback() will be invoked with the rendering's dimension info and image
passed in. Lastly, during post-processing,
postProcessCallback() will be invoked with the rendering's dimension and pointers to
the rgb pixmap and depthmap passed in.
If multiple callbacks need to be registered, the order of
invocation can be set by adding each callback with a priority
number, 0 being the highest priority.
'''
    def __init__(self):
        pass


    def shadowCastCallback(self, data: MRenderShadowData): 
        '''
        shadowCastCallback(self, data: MRenderShadowData) -> bool

        Synopsis
        -----
        Method to override for plugging into shadow map creation. The
        argument provides information about the light and shadow map
        currently being processed. If false is returned, the renderer
        will abort and no image will be generated.

        Returns: 
        ----- 
        True if the operation was successful and false otherwise.

        Parameters:
        -----
        data: MRenderShadowData
        	[in] -> data and functions related to the current shadow map


        '''
        pass

    def renderCallback(self, data: MRenderData): 
        '''
        renderCallback(self, data: MRenderData) -> bool

        Synopsis
        -----
        Method to override for plugging into image rendering. This method
        will be invoked following the software render (but before the
        post process) of each frame. The data argument provides
        information about the image and camera projection; these are
        useful in transforming to and from world and image space. If
        false is returned, the renderer will abort and no image will be
        generated.

        Returns: 
        ----- 
        True if the operation was successful and false otherwise.

        Parameters:
        -----
        data: MRenderData
        	[in] -> data and functions related to the current frame


        '''
        pass

    def postProcessCallback(self, data: MRenderData): 
        '''
        postProcessCallback(self, data: MRenderData) -> bool

        Synopsis
        -----
        Method to override for plugging into the post-process. This
        method will be invoked following the post process rendering
        (shader glow, optical effects, 2D motion blur). The data argument
        provides information about the image and camera projection; these
        are useful in transforming to and from world and image space. If
        false is returned, the renderer will abort and no image will be
        generated.

        Returns: 
        ----- 
        True if the operation was successful and false otherwise.

        Parameters:
        -----
        data: MRenderData
        	[in] -> data and functions related to the current frame


        '''
        pass

    def addCallback(self, callback: MRenderCallback,
                        priority: int): 
        '''
        addCallback(self, callback: MRenderCallback,
                        priority: int)

        Synopsis
        -----
        Static procedure to add a rendering callback. The callbacks are
        stored internally in a sorted list and are invoked following the
        shadow map generation, software render, or post process depending
        on which methods are overridden. Adding the same callback more
        than once will have no effect.

        Returns:
        -----
        None

        Parameters:
        -----
        callback: MRenderCallback
        	[in] -> object to add to the list of callbacks to invoke 

        priority: int
        	[in] -> priority for this callback, lower priorities are invoked first 


        '''
        pass

    def removeCallback(self, callback: MRenderCallback): 
        '''
        removeCallback(self, callback: MRenderCallback)

        Synopsis
        -----
        Static procedure to remove a rendering callback. The callback
        will be removed from the list of callbacks, but its up to the
        client to actually delete the object. Unstability may result if a
        callback is deleted and not removed from the callback
        list.Removing an un-installed callback will have no effect.

        Returns:
        -----
        None

        Parameters:
        -----
        callback: MRenderCallback
        	[in] -> object to remove from the list of callbacks 


        '''
        pass

    def addRenderTileCallback(self, func: MMessage.MMessage,
                        ReturnStatus: MRenderCallback.MStatus): 
        '''
        addRenderTileCallback(self, func: MMessage.MMessage,
                        ReturnStatus: MRenderCallback.MStatus) -> MCallbackId

        Synopsis
        -----
        Static procedure to add a callback to receive tiles as they get
        rendered and before they get displayed in the Render View Window.
        The user is provided with the co-ordinates of the origin of the
        tile, its dimensions, as well as a read only copy of the image
        being rendered.NOTE: This callback can only serve one client at a
        time.

        Returns: 
        ----- 
        The callback ID of the newly registered callback.

        Parameters:
        -----
        func: MMessage.MMessage
        	[in] -> callback function, please check 

        ReturnStatus: MRenderCallback.MStatus
        	[out] -> success status of callback registration.


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

class MRenderData:
    '''Access Rendering Data.
The rendered image and depth map can be changed following the
software render by instanciating a
MRenderCallback and overriding renderCallback() or postProcessCallback(). When
these methods are invoked, a
MRenderData is passed as an argument; the rgbaArr and depthArr can then be
changed by this API. Methods and data are provided to assist in
transforming back and forth from world space to image space.
Paint Effects and Fur are two examples which use this mechanism
to change the rendered image.
'''
    def __init__(self):
        pass


    def worldToScreen(self, inPoint: MFloatPoint,
                        outPoint: MFloatPoint): 
        '''
        worldToScreen(self, inPoint: MFloatPoint,
                        outPoint: MFloatPoint)

        Synopsis
        -----
        Converts world space point to screen space. Screen depth is
        stored in outPoint.z.

        Returns:
        -----
        None

        Parameters:
        -----
        inPoint: MFloatPoint
        	[in] -> The original point in world space 

        outPoint: MFloatPoint
        	[out] -> The converted point in screen space 


        '''
        pass

    def screenToWorld(self, inPoint: MFloatPoint,
                        outPoint: MFloatPoint): 
        '''
        screenToWorld(self, inPoint: MFloatPoint,
                        outPoint: MFloatPoint)

        Synopsis
        -----
        Converts screen space point to world space. Screen depth is
        stored in inPoint.z.

        Returns:
        -----
        None

        Parameters:
        -----
        inPoint: MFloatPoint
        	[in] -> The original point in screen space 

        outPoint: MFloatPoint
        	[out] -> The converted point in world space 


        '''
        pass

    def rgbaArr(self): 
        '''
        rgbaArr(self) -> char*

        Synopsis
        -----
        this is a 1d array representing the output image buffer. It is of
        size: resX * resY * 4 * bytesPerChannel. The array is indexed as
        [(resX * x + y) * 4 * bytesPerChannel], where (x,y) is the
        current pixel coordinates. The "4" multiplier is used for storing
        RGBA information, in the order of a,b,g,r (on OSX) or b,g,r,a (on
        Windows and Linux).

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def depthArr(self): 
        '''
        depthArr(self) -> float*

        Synopsis
        -----
        this is a 1d array representing the output depth buffer. It is of
        size: resX * resY, where each depth value is a single precision
        floating point vlue. It is indexed as [resX * x + y], where (x,y)
        is the current pixel coordinates.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MRenderPassDef:
    '''Render pass information.
This class provides a means to access information about a
specific render pass. Initialize by passing to
MRenderPassRegistry::getRenderPassDefinition(), or by calling create() to generate and register a new pass.
'''
    def __init__(self):
        pass


    def getID(self, ReturnStatus: MRenderPassDef.MStatus): 
        '''
        getID(self, ReturnStatus: MRenderPassDef.MStatus) -> MString

        Synopsis
        -----
        Retrieve the pass ID for this pass.

        Returns: 
        ----- 
        The pass ID

        Parameters:
        -----
        ReturnStatus: MRenderPassDef.MStatus
        	[out] -> Status code


        '''
        pass

    def getName(self, ReturnStatus: MRenderPassDef.MStatus): 
        '''
        getName(self, ReturnStatus: MRenderPassDef.MStatus) -> MString

        Synopsis
        -----
        Retrieve the pass name for this pass.

        Returns: 
        ----- 
        The pass name

        Parameters:
        -----
        ReturnStatus: MRenderPassDef.MStatus
        	[out] -> Status code


        '''
        pass

    def getGroup(self, ReturnStatus: MRenderPassDef.MStatus): 
        '''
        getGroup(self, ReturnStatus: MRenderPassDef.MStatus) -> MString

        Synopsis
        -----
        Retrieve the pass group for this pass.

        Returns: 
        ----- 
        The pass group

        Parameters:
        -----
        ReturnStatus: MRenderPassDef.MStatus
        	[out] -> Status code


        '''
        pass

    def getDescription(self, ReturnStatus: MRenderPassDef.MStatus): 
        '''
        getDescription(self, ReturnStatus: MRenderPassDef.MStatus) -> MString

        Synopsis
        -----
        Retrieve the description for this pass.

        Returns: 
        ----- 
        The description

        Parameters:
        -----
        ReturnStatus: MRenderPassDef.MStatus
        	[out] -> Status code


        '''
        pass

    def getAttributeType(self, attributeName: MString,
                        ReturnStatus: MRenderPassDef.MStatus): 
        '''
        getAttributeType(self, attributeName: MString,
                        ReturnStatus: MRenderPassDef.MStatus) -> MString

        Synopsis
        -----
        Retrieve the type of a given render pass attribute.

        Returns: 
        ----- 
        The type of the given attribute.

        Parameters:
        -----
        attributeName: MString
        	[in] -> The name of the render pass attribute to query. 

        ReturnStatus: MRenderPassDef.MStatus
        	[out] -> Status code.


        '''
        pass

    def addFloatParameter(self, longName: MString,
                        shortName: MString,
                        UIName: MString,
                        minValue: float,
                        maxValue: float,
                        defaultValue: float): 
        '''
        addFloatParameter(self, longName: MString,
                        shortName: MString,
                        UIName: MString,
                        minValue: float,
                        maxValue: float,
                        defaultValue: float)

        Synopsis
        -----
        Define a single-precision floating-point parameter for the pass.

        Returns:
        -----
        None

        Parameters:
        -----
        longName: MString
        	[in] -> The full name of the parameter 

        shortName: MString
        	[in] -> The short name of the parameter 

        UIName: MString
        	[in] -> Name to display in UI for the parameter 

        minValue: float
        	[out] -> The minimum value of the parameter 

        maxValue: float
        	[out] -> The maximum value of the parameter 

        defaultValue: float
        	[out] -> The default value of the parameter


        '''
        pass

    def addDoubleParameter(self, longName: MString,
                        shortName: MString,
                        UIName: MString,
                        minValue: double,
                        maxValue: double,
                        defaultValue: double): 
        '''
        addDoubleParameter(self, longName: MString,
                        shortName: MString,
                        UIName: MString,
                        minValue: double,
                        maxValue: double,
                        defaultValue: double)

        Synopsis
        -----
        Define a double-precision floating-point parameter for the pass.

        Returns:
        -----
        None

        Parameters:
        -----
        longName: MString
        	[in] -> The full name of the parameter 

        shortName: MString
        	[in] -> The short name of the parameter 

        UIName: MString
        	[in] -> Name to display in UI for the parameter 

        minValue: double
        	[out] -> The minimum value of the parameter 

        maxValue: double
        	[out] -> The maximum value of the parameter 

        defaultValue: double
        	[out] -> The default value of the parameter


        '''
        pass

    def addIntParameter(self, longName: MString,
                        shortName: MString,
                        UIName: MString,
                        minValue: int,
                        maxValue: int,
                        defaultValue: int): 
        '''
        addIntParameter(self, longName: MString,
                        shortName: MString,
                        UIName: MString,
                        minValue: int,
                        maxValue: int,
                        defaultValue: int)

        Synopsis
        -----
        Define an integer parameter for the pass.

        Returns:
        -----
        None

        Parameters:
        -----
        longName: MString
        	[in] -> The full name of the parameter 

        shortName: MString
        	[in] -> The short name of the parameter 

        UIName: MString
        	[in] -> Name to display in UI for the parameter 

        minValue: int
        	[out] -> The minimum value of the parameter 

        maxValue: int
        	[out] -> The maximum value of the parameter 

        defaultValue: int
        	[out] -> The default value of the parameter


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

class MRenderPassRegistry:
    '''Access the render pass registry.
This class provides a means to register custom render pass
definitions with Maya's internal render pass registry. It can
also be used to query pass definitions.
'''
    def __init__(self):
        pass


    def getRenderPassDefinition(self, passID: MString,
                        ReturnStatus: MRenderPassRegistry.MStatus): 
        '''
        getRenderPassDefinition(self, passID: MString,
                        ReturnStatus: MRenderPassRegistry.MStatus) -> MRenderPassRegistry.OPENMAYA_MAJOR_NAMESPACE_OPEN MRenderPassDef

        Synopsis
        -----
        Retrieve the definition of the specified render pass.

        Returns: 
        ----- 
        The render pass definition if successful

        Parameters:
        -----
        passID: MString
        	[in] -> The ID of the pass 

        ReturnStatus: MRenderPassRegistry.MStatus
        	[out] -> Status code


        '''
        pass

    def registerRenderPassDefinition(self, passID: MString,
                        passName: MString,
                        passGroup: MString,
                        description: MString,
                        overload: bool,
                        ReturnStatus: MRenderPassRegistry.MStatus): 
        '''
        registerRenderPassDefinition(self, passID: MString,
                        passName: MString,
                        passGroup: MString,
                        description: MString,
                        overload: bool,
                        ReturnStatus: MRenderPassRegistry.MStatus) -> MRenderPassDef

        Synopsis
        -----
        Creates a new render pass definition and registers it with the
        internal render pass registry. Returns the definition.

        Returns: 
        ----- 
        The render pass definition if successful

        Parameters:
        -----
        passID: MString
        	[in] -> The ID of the pass 

        passName: MString
        	[in] -> The name of the new pass 

        passGroup: MString
        	[in] -> The classification of the new pass 

        description: MString
        	[in] -> A description of the new pass 

        overload: bool
        	[in] -> If true, override any existing pass with the same passID with this pass definiton 

        ReturnStatus: MRenderPassRegistry.MStatus
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

class MRenderProfile:
    '''Render profile.
The
MRenderProfile class describes the rendering APIs and algorithms supported by a
given rendering entity (e.g. a shading node, a renderer). A
single profile can contain multiple entries allowing, for
example, a shading node to specify that it supports both OpenGL
and Direct3D rendering. The profile entries refer to renderers
rather than rendering APIs as the rendering elements may depend
on specific services, information or algorithms implemented by
the renderer (e.g. a global light table, or render state cache).
'''
    def __init__(self):
        pass


    def numberOfRenderers(self): 
        '''
        numberOfRenderers(self) -> int

        Synopsis
        -----
        Find the number of renderers in this profile.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def addRenderer(self, renderer: MRenderProfile.MStandardRenderer): 
        '''
        addRenderer(self, renderer: MRenderProfile.MStandardRenderer)

        Synopsis
        -----
        Add one of Maya's internal renderers to this render profile.

        Returns:
        -----
        None

        Parameters:
        -----
        renderer: MRenderProfile.MStandardRenderer
        	[in] -> The internal Maya renderer to add to this profile. 


        '''
        pass

    @overload
    def addRenderer(self, name: MString,
                        version: float): 
        '''
        addRenderer(self, name: MString,
                        version: float)

        Synopsis
        -----
        Add a custom entry to this render profile. The name and version
        specified must correspond to a renderer registered with Maya.
        Currently, only Maya's internal renderers (just named after the
        APIs they use: "OpenGL", "D3D", or "Software") are supported.
        When registering support for Maya's internal renderers, it's
        simpler to use the other version of this method.

        Returns:
        -----
        None

        Parameters:
        -----
        name: MString
        	[in] -> The name of the renderer. 

        version: float
        	[in] -> The version of the renderer or rendering API. 


        '''
        pass

    @overload
    def hasRenderer(self, renderer: MRenderProfile.MStandardRenderer): 
        '''
        hasRenderer(self, renderer: MRenderProfile.MStandardRenderer) -> bool

        Synopsis
        -----
        See if a Maya renderer is listed in this profile.

        Returns:
        -----
        None

        Parameters:
        -----
        renderer: MRenderProfile.MStandardRenderer
        	[in] -> The internal Maya renderer to search for 


        '''
        pass

    @overload
    def hasRenderer(self, name: MString,
                        version: float): 
        '''
        hasRenderer(self, name: MString,
                        version: float) -> bool

        Synopsis
        -----
        Find a custom entry in this render profile.

        Returns:
        -----
        None

        Parameters:
        -----
        name: MString
        	[in] -> The name of the renderer. 

        version: float
        	[in] -> The version of the renderer or rendering API. 


        '''
        pass

class MStandardRenderer:
    '''Maya's internal renderers. 
    Non-functional class.  Values for this enum:
    kMayaSoftware
    kMayaOpenGL
    kMayaD3D
    '''

    def __init__(self):
        pass

    def kMayaSoftware(self):
        '''This is an enum of MStandardRenderer.
        - Description:  
        - Value: 0
        '''
        pass

    def kMayaOpenGL(self):
        '''This is an enum of MStandardRenderer.
        - Description:  
        - Value: 1
        '''
        pass

    def kMayaD3D(self):
        '''This is an enum of MStandardRenderer.
        - Description:  
        - Value: 2
        '''
        pass

class MRenderSetup:
    '''Utilities for obtaining render setup information.
'''
    def __init__(self):
        pass


    def className(self): 
        '''
        className(self) -> MRenderSetup.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

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

    def getEnabledSelectedNodeNames(self, renderLayerName: MString,
                        status: MRenderSetup.MStatus): 
        '''
        getEnabledSelectedNodeNames(self, renderLayerName: MString,
                        status: MRenderSetup.MStatus) -> MStringArray

        Synopsis
        -----
        Return the members of a render setup render layer. DAG children
        of render layer members are implicitly members of the render
        layer, and are not returned by this call.

        Returns: 
        ----- 
        Array of members of the render setup render layer.

        Parameters:
        -----
        renderLayerName: MString
        	[in] -> Name of the render setup render layer. 

        status: MRenderSetup.MStatus
        	[out] -> Return status.


        '''
        pass

class MRenderShadowData:
    '''Access Rendering Shadow Map Data.
The shadow map can be changed by instanciating a
MRenderCallback and overriding shadowCastCallback(). When this is invoked, a
MRenderShadowData is passed as an argument; the depthMaps and midDistMaps members
can then be changed by this API. Methods and data are provided to
assist in transforming back and forth from world space to z
buffer space. Paint Effects and Fur are two examples which use
this mechanism to change the shadow map.
To prevent self shadowing, Maya uses a mid distance map to
resolve the ambiguity. Details of this technique can be obtained
from Graphics Gems III, "The Shadow Depth Map Revisited".
'''
    def __init__(self):
        pass


    def worldToZbuffer(self, inPoint: MFloatPoint,
                        outPoint: MFloatPoint): 
        '''
        worldToZbuffer(self, inPoint: MFloatPoint,
                        outPoint: MFloatPoint)

        Synopsis
        -----
        Converts world space point to shadow map. Shadow depth is stored
        in inPoint.z

        Returns:
        -----
        None

        Parameters:
        -----
        inPoint: MFloatPoint
        	[in] -> The original point in world space 

        outPoint: MFloatPoint
        	[out] -> The converted point in shadow map 


        '''
        pass

    def zbufferToWorld(self, inPoint: MFloatPoint,
                        outPoint: MFloatPoint): 
        '''
        zbufferToWorld(self, inPoint: MFloatPoint,
                        outPoint: MFloatPoint)

        Synopsis
        -----
        Converts shadow map point to world space. Shadow depth is stored
        in inPoint.z.

        Returns:
        -----
        None

        Parameters:
        -----
        inPoint: MFloatPoint
        	[in] -> The original point in shadow map 

        outPoint: MFloatPoint
        	[out] -> The converted point in world space 


        '''
        pass

class LightType:
    '''Light Types. 
    Non-functional class.  Values for this enum:
    kInvalid
    kPoint
    kDirectional
    kSpot
    '''

    def __init__(self):
        pass

    def kInvalid(self):
        '''This is an enum of LightType.
        - Description:  
        - Value: 0
        '''
        pass

    def kPoint(self):
        '''This is an enum of LightType.
        - Description:  
        - Value: 1
        '''
        pass

    def kDirectional(self):
        '''This is an enum of LightType.
        - Description:  
        - Value: 2
        '''
        pass

    def kSpot(self):
        '''This is an enum of LightType.
        - Description:  
        - Value: 3
        '''
        pass

class MRenderTargetLegacy:
    '''MRenderTargetLegacy is a class contains information about a given hardware render
target.
'''
    def __init__(self):
        pass


    def width(self): 
        '''
        width(self) -> MRenderTargetLegacy.OPENMAYA_MAJOR_NAMESPACE_OPENint

        Synopsis
        -----
        Width of render target in pixels. Return the width in pixels of
        the render target.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def height(self): 
        '''
        height(self) -> int

        Synopsis
        -----
        Height of render target in pixels. Return the height in pixels of
        the render target.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def writeColorBuffer(self, image: MImage,
                        x: signed,
                        y: signed,
                        writeDepth: bool): 
        '''
        writeColorBuffer(self, image: MImage,
                        x: signed,
                        y: signed,
                        writeDepth: bool)

        Synopsis
        -----
        Write a 2d image directly to the color buffer, without any
        transformation. Method will make the context current if it is not
        already.If a depth component in the image also exists, then depth
        values can also be written to.

        Returns:
        -----
        None

        Parameters:
        -----
        image: MImage
        	[in] -> an 

        x: signed
        	[in] -> lower left corner x position in the target to place the image. Default value is 0. 

        y: signed
        	[in] -> lower left corner y position in the target to place the image Default value is 0. 

        writeDepth: bool
        	[in] -> write the depth component of the incoming image to the depth component of the render target. If image does not contain any depth component then nothing will be written. Default value is false.


        '''
        pass

class MRenderUtil:
    '''Common API rendering functions.
MRenderUtil is a class which provides static API methods to access Maya's
rendering functionalities.
'''
    def __init__(self):
        pass


    def mayaRenderState(self): 
        '''
        mayaRenderState(self) -> OPENMAYA_MAJOR_NAMESPACE_OPEN MRenderUtil.OPENMAYA_MAJOR_NAMESPACE_OPEN MRenderUtil

        Synopsis
        -----
        Returns an enumerated type specifying the current state of the
        Maya renderer.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def raytrace(self, rayOrigin: MFloatVector,
                        rayDirection: MFloatVector,
                        notUsed: void,
                        raySampler: void,
                        rayDepth: short,
                        resultColor: MFloatVector,
                        resultTransparency: MFloatVector,
                        isReflectedRays: bool): 
        '''
        raytrace(self, rayOrigin: MFloatVector,
                        rayDirection: MFloatVector,
                        notUsed: void,
                        raySampler: void,
                        rayDepth: short,
                        resultColor: MFloatVector,
                        resultTransparency: MFloatVector,
                        isReflectedRays: bool)

        Synopsis
        -----
        This utility method provides functionality to raytrace from
        within a shader plug-in. This method shoots a single ray given a
        ray origin and a ray direction, and returns the color and
        transparency of the result.In order for a shader plug-in to
        raytrace, the following steps are necessary:raySampler is needed
        from the renderer. This can be obtained by creating an input
        attribute named 'raySampler' (rtr).rayDepth is needed from the
        renderer. This can be obtained by creating an input attribute
        named 'rayDepth' (rd).The "Enable Raytracing" flag needs to be
        turned on in renderGlobal->
        renderQuality->raytracing.isReflectedRays tells if these rays are
        for reflection or refraction. This allows the raytracer to check
        the corresponding ray depth limit under
        renderGlobal->renderQuality for terminating the rays.All objects
        to be seen by the raytracer need to have their "Visible In
        Reflections" or "Visible In Refraction" flags turned on.This
        method only works in the software renderer.

        Returns:
        -----
        None

        Parameters:
        -----
        rayOrigin: MFloatVector
        	[in] -> Origin of the ray to shoot from in camera space 

        rayDirection: MFloatVector
        	[in] -> Direction of the ray to shoot at in camera space 

        notUsed: void
        	[in] -> unused argument left for compatibility 

        raySampler: void
        	[in] -> Pointer to the raytracer from the renderer 

        rayDepth: short
        	[in] -> Current ray depth from the renderer 

        resultColor: MFloatVector
        	[out] -> Storage for the result color 

        resultTransparency: MFloatVector
        	[out] -> Storage for the result transparency 

        isReflectedRays: bool
        	[in] -> true for reflected rays (default), false for refracted rays


        '''
        pass

    @overload
    def raytrace(self, rayOrigins: MFloatVectorArray,
                        rayDirections: MFloatVectorArray,
                        notUsed: void,
                        raySampler: void,
                        rayDepth: short,
                        resultColors: MFloatVectorArray,
                        resultTransparencies: MFloatVectorArray,
                        isReflectedRays: bool): 
        '''
        raytrace(self, rayOrigins: MFloatVectorArray,
                        rayDirections: MFloatVectorArray,
                        notUsed: void,
                        raySampler: void,
                        rayDepth: short,
                        resultColors: MFloatVectorArray,
                        resultTransparencies: MFloatVectorArray,
                        isReflectedRays: bool)

        Synopsis
        -----
        This utility method provides functionality to raytrace from
        within a shader plug-in. This method shoots a number of rays
        given ray origins and ray directions, and returns the colors and
        transparencies of the results.The size of rayOrigins,
        rayDirections, colors, and transparencies arrays must be the
        same.In order for a shader plug-in to raytrace, the following
        steps are necessary:raySampler is needed from the renderer. This
        can be obtained by creating an input attribute named 'raySampler'
        (rtr).rayDepth is needed from the renderer. This can be obtained
        by creating an input attribute named 'rayDepth' (rd).The "Enable
        Raytracing" flag needs to be turned on in renderGlobal->
        renderQuality->raytracing.isReflectedRays tells if these rays are
        for reflection or refraction. This allows the raytracer to check
        the corresponding ray depth limit under
        renderGlobal->renderQuality for terminating the rays.All objects
        to be seen by the raytracer need to have their "Visible In
        Reflections" or "Visible In Refraction" flags turned on.This
        method only works in the software renderer.

        Returns:
        -----
        None

        Parameters:
        -----
        rayOrigins: MFloatVectorArray
        	[in] -> Origins of the ray to shoot from in camera space 

        rayDirections: MFloatVectorArray
        	[in] -> Directions of the ray to shoot at in camera space 

        notUsed: void
        	[in] -> unused argument left for compatability 

        raySampler: void
        	[in] -> Pointer to the raytracer from the renderer 

        rayDepth: short
        	[in] -> Current ray depth from the renderer 

        resultColors: MFloatVectorArray
        	[out] -> Storage for the result colors 

        resultTransparencies: MFloatVectorArray
        	[out] -> Storage for the result transparencies 

        isReflectedRays: bool
        	[in] -> true for reflected rays (default), false for refracted rays


        '''
        pass

    def raytraceFirstGeometryIntersections(self, rayOrigins: MFloatVectorArray,
                        rayDirections: MFloatVectorArray,
                        notUsed: void,
                        raySampler: void,
                        resultIntersections: MFloatVectorArray,
                        resultIntersected: MIntArray): 
        '''
        raytraceFirstGeometryIntersections(self, rayOrigins: MFloatVectorArray,
                        rayDirections: MFloatVectorArray,
                        notUsed: void,
                        raySampler: void,
                        resultIntersections: MFloatVectorArray,
                        resultIntersected: MIntArray)

        Synopsis
        -----
        This utility method provides functionality to find the location
        of the first geometry intersected by a ray from within a shader
        plug-in. This method shoots a number of rays given ray origins
        and ray directions, and returns whether the rays intersected
        anything, and if so, the locations of the first geometry
        intersected in camera space. The plug-in should check the
        resultIntersected values to see if a ray has intersected any
        geometry (0 = no geometry intersected, 1 = geometry
        intersected).The size of rayOrigins, rayDirections,
        resultIntersections, and resultIntersected arrays must be the
        same.In order for a shader plug-in to raytrace, the following
        steps are necessary:raySampler is needed from the renderer. This
        can be obtained by creating an input attribute named 'raySampler'
        (rtr).The "Enable Raytracing" flag needs to be turned on in
        renderGlobal-> renderQuality->raytracing.All objects to be seen
        by the raytracer need to have their "Visible In Reflections"
        flags turned on.This method only works in the software renderer.

        Returns:
        -----
        None

        Parameters:
        -----
        rayOrigins: MFloatVectorArray
        	[in] -> Origins of the ray to shoot from in camera space 

        rayDirections: MFloatVectorArray
        	[in] -> Directions of the ray to shoot at in camera space 

        notUsed: void
        	[in] -> unused argument left for compatability 

        raySampler: void
        	[in] -> Pointer to the raytracer from the renderer 

        resultIntersections: MFloatVectorArray
        	[out] -> Storage for the result intersection locations in camera space 

        resultIntersected: MIntArray
        	[out] -> Storage for the result intersected flags (0 = no geometry intersected, 1 = geometry intersected)


        '''
        pass

    def sampleShadingNetwork(self, shadingNodeName: MString,
                        numSamples: int,
                        useShadowMaps: bool,
                        reuseMaps: bool,
                        cameraMatrix: MFloatMatrix,
                        points: MFloatPointArray,
                        uCoords: MFloatArray,
                        vCoords: MFloatArray,
                        normals: MFloatVectorArray,
                        refPoints: MFloatPointArray,
                        tangentUs: MFloatVectorArray,
                        tangentVs: MFloatVectorArray,
                        filterSizes: MFloatArray,
                        resultColors: MFloatVectorArray,
                        resultTransparencies: MFloatVectorArray): 
        '''
        sampleShadingNetwork(self, shadingNodeName: MString,
                        numSamples: int,
                        useShadowMaps: bool,
                        reuseMaps: bool,
                        cameraMatrix: MFloatMatrix,
                        points: MFloatPointArray,
                        uCoords: MFloatArray,
                        vCoords: MFloatArray,
                        normals: MFloatVectorArray,
                        refPoints: MFloatPointArray,
                        tangentUs: MFloatVectorArray,
                        tangentVs: MFloatVectorArray,
                        filterSizes: MFloatArray,
                        resultColors: MFloatVectorArray,
                        resultTransparencies: MFloatVectorArray)

        Synopsis
        -----
        This utility method allows you to sample a shading node/shading
        engine. You can specify the location and property of the sample
        point, and the method will return the result color and
        transparency. If you are sampling a shading engine, and there are
        lights in the scene, you can optionally request shadows to be
        computed as well.If you specify a shading node to be evaluated,
        you'll need to provide the attribute to be evaluated. For
        example, valid shading nodes are checker1.outAlpha,
        file1.outColor, etc.If you specify a shading engine to be
        evaluated, only the name will be needed. For example, valid
        shading engines are initialShadingGroup, phong1SG, etc.Since
        setting up sampling is an expensive operation, try to pass in as
        many sample points at one time as possible and let the sampler
        process them in batch. Try to avoid calling the sampler with just
        one sample.For extremely complicated shading networks, it is
        possible that passing in too many samples in one batch will cause
        a stack overflow. If this condition occurs, simply reduce the
        number of samples per batch.Certain type of shading network
        requires certain type of input, and not all inputs are needed.
        For example, a 2D texture such as file or checker does not need
        point/normal/tangent information. Pass in NULL for parameters
        which are not needed.In general, 2D textures require UV
        coordinates, 3D textures require points and refPoints, lighting
        calculations require points and normals.To calculate camera space
        related shaders, such as hilights in a phong shader, an eye to
        world matrix needs to be supplied. This matrix is used to convert
        supplied world coordinates into camera coordinate. The matrix can
        be obtained by getting the inclusive matrix of the camera's DAG
        node.This method can be used in both interactive and batch.

        Returns:
        -----
        None

        Parameters:
        -----
        shadingNodeName: MString
        	[in] -> Name of the shading node/shading engine 

        numSamples: int
        	[in] -> Number of samples to be calculated 

        useShadowMaps: bool
        	[in] -> Whether to calculate shadows 

        reuseMaps: bool
        	[in] -> If calculating shadows, whether to reuse shadowmaps 

        cameraMatrix: MFloatMatrix
        	[in] -> The eyeToWorld matrix to be used for conversion 

        points: MFloatPointArray
        	[in] -> Locations to be sampled in world space 

        uCoords: MFloatArray
        	[in] -> U coordinates of the samples 

        vCoords: MFloatArray
        	[in] -> V coordinates of the samples 

        normals: MFloatVectorArray
        	[in] -> Normals at the sample points in world space 

        refPoints: MFloatPointArray
        	[in] -> RefPoints to be used for 3D texture in world space 

        tangentUs: MFloatVectorArray
        	[in] -> U tangents at the sample points in world space 

        tangentVs: MFloatVectorArray
        	[in] -> V tangents at the sample points in world space 

        filterSizes: MFloatArray
        	[in] -> Filter sizes to be used for 2D/3D textures 

        resultColors: MFloatVectorArray
        	[out] -> Storage for result colors 

        resultTransparencies: MFloatVectorArray
        	[out] -> storage for result transparencies


        '''
        pass

    def generatingIprFile(self): 
        '''
        generatingIprFile(self) -> bool

        Synopsis
        -----
        Returns true if an IPR file is being created. This can be used to
        optimize the IPR file. Lights do not need to request particle
        information (IPR does not support particle rendering) when
        creating a IPR file.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def relativeFileName(self, absFileName: MString,
                        ReturnStatus: MRenderUtil.MStatus): 
        '''
        relativeFileName(self, absFileName: MString,
                        ReturnStatus: MRenderUtil.MStatus) -> MString

        Synopsis
        -----
        Extract relative file name from the given (absolute) file name.
        If the given file name does not begin with a project root, return
        value is same as the input file name.

        Returns: 
        ----- 
        file name without the project path

        Parameters:
        -----
        absFileName: MString
        	[in] -> input file name 

        ReturnStatus: MRenderUtil.MStatus
        	[out] -> status code


        '''
        pass

    @overload
    def exactFileTextureName(self, fileNode: MObject,
                        texturePath: MString,
                        ReturnStatus: MRenderUtil.MStatus): 
        '''
        exactFileTextureName(self, fileNode: MObject,
                        texturePath: MString,
                        ReturnStatus: MRenderUtil.MStatus) -> bool

        Synopsis
        -----
        Attempts to resolve the file texture name specified on a file
        texture node into an absolute path to an image file on disk. The
        function applies exactly the same logic that is used by the file
        texture node internally for resolving the image file path.This
        method is not supported in Python. See the version which returns
        a string.

        Returns: 
        ----- 
        true if the image file pathname was successfully resolved, false
        otherwise.

        Parameters:
        -----
        fileNode: MObject
        	[in] -> a file texture node 

        texturePath: MString
        	[out] -> returns an absolute pathname to the texture file referenced by the node. 

        ReturnStatus: MRenderUtil.MStatus
        	[out] -> status code


        '''
        pass

    @overload
    def exactFileTextureName(self, baseName: MString,
                        useFrameExt: bool,
                        currentFrameExt: MString,
                        contextNodeFullName: MString,
                        exactName: MString,
                        ReturnStatus: MRenderUtil.MStatus): 
        '''
        exactFileTextureName(self, baseName: MString,
                        useFrameExt: bool,
                        currentFrameExt: MString,
                        contextNodeFullName: MString,
                        exactName: MString,
                        ReturnStatus: MRenderUtil.MStatus) -> bool

        Synopsis
        -----
        Attempts to resolve the file name specified into an absolute path
        to a file on disk. The function applies exactly the same logic
        that is used by the file texture node internally for resolving
        the image file path.This method is not supported in Python. See
        the version which returns a string.

        Returns: 
        ----- 
        true if the file pathname was successfully resolved.  false if
        the pathname could not be resolved.

        Parameters:
        -----
        baseName: MString
        	[in] -> a file name to be resolved 

        useFrameExt: bool
        	[in] -> use frame extension for image file name 

        currentFrameExt: MString
        	[in] -> specify a frame extension if useFrameExt is used. 

        contextNodeFullName: MString
        	[in] -> full name of the file owner Node. 

        exactName: MString
        	[out] -> resolved file name with absolute path 

        ReturnStatus: MRenderUtil.MStatus
        	[out] -> status code


        '''
        pass

    def exactFileTextureUvTileData(self, fileNode: MObject,
                        tilePaths: MStringArray,
                        tilePositions: MFloatArray,
                        ReturnStatus: MRenderUtil.MStatus): 
        '''
        exactFileTextureUvTileData(self, fileNode: MObject,
                        tilePaths: MStringArray,
                        tilePositions: MFloatArray,
                        ReturnStatus: MRenderUtil.MStatus) -> bool

        Synopsis
        -----
        Attempts to resolve all the paths to UV tiles for the given file
        texture node into absolute paths to image files on disk. Also
        computes the lower left coordinate of each tile in UV space. The
        coordinates are returned in a flat array of floats so for tile
        'n', the coordinate is given by: (tilePositions[n*2],
        tilePositions[n*2+1]).This function applies exactly the same
        logic that is used by the file texture node internally for
        resolving the UV tile paths and positions.This method is not
        supported in Python.

        Returns: 
        ----- 
        True if at least one tile was resolved, false otherwise.

        Parameters:
        -----
        fileNode: MObject
        	[in] -> A file texture node 

        tilePaths: MStringArray
        	[out] -> Returns the set of absolute pathnames to the UV tiles for the given texture texture file node 

        tilePositions: MFloatArray
        	[out] -> Returns the lower left coordinate of each tile in UV space. 

        ReturnStatus: MRenderUtil.MStatus
        	[out] -> Status code


        '''
        pass

    @overload
    def convertPsdFile(self, fileNode: MObject,
                        texturePath: MString,
                        forExport: bool,
                        ReturnStatus: MRenderUtil.MStatus): 
        '''
        convertPsdFile(self, fileNode: MObject,
                        texturePath: MString,
                        forExport: bool,
                        ReturnStatus: MRenderUtil.MStatus) -> bool

        Synopsis
        -----
        Internal use only. This method converts a Psd file texture to an
        IFF file that can be used by Maya.It writes out the current layer
        set image the file node. The intermediate image will be either 8
        or 16 b.p.c, based on the input psd file.This method is not
        supported in Python. See the version which returns a string.

        Returns: 
        ----- 
        true if the image file pathname was successfully resolved and
        exporting psd file is succeeded.  false if the pathname could not
        be resolved or exporting psd file fails.

        Parameters:
        -----
        fileNode: MObject
        	[in] -> a file texture node 

        texturePath: MString
        	[out] -> returns an absolute pathname to the texture file referenced by the node. 

        forExport: bool
        	[out] -> if true the resulting IFF file will be stored in the project directory tree, otherwise it will be stored in a temporary file which will be deleted when Maya exits. 

        ReturnStatus: MRenderUtil.MStatus
        	[out] -> status code


        '''
        pass

    @overload
    def exactImagePlaneFileName(self, imagePlaneNode: MObject,
                        texturePath: MString,
                        ReturnStatus: MRenderUtil.MStatus): 
        '''
        exactImagePlaneFileName(self, imagePlaneNode: MObject,
                        texturePath: MString,
                        ReturnStatus: MRenderUtil.MStatus) -> bool

        Synopsis
        -----
        Attempts to resolve the file texture name specified on an image
        plane node into an absolute path to an image file on disk. The
        function applies exactly the same logic that is used by the image
        plane node internally for resolving the image file path.This
        method is not supported in Python. See the version which returns
        a string.

        Returns: 
        ----- 
        true if the image file pathname was successfully resolved.  false
        if the pathname could not be resolved.

        Parameters:
        -----
        imagePlaneNode: MObject
        	[in] -> an image plane node 

        texturePath: MString
        	[out] -> returns an absolute pathname to the texture file referenced by the node. 

        ReturnStatus: MRenderUtil.MStatus
        	[out] -> status code


        '''
        pass

    @overload
    def exactFileTextureName(self, fileNode: MObject,
                        ReturnStatus: MRenderUtil.MStatus): 
        '''
        exactFileTextureName(self, fileNode: MObject,
                        ReturnStatus: MRenderUtil.MStatus) -> MString

        Synopsis
        -----
        Attempts to resolve the file texture name specified on a file
        texture node into an absolute path to an image file on disk. The
        function applies exactly the same logic that is used by the file
        texture node internally for resolving the image file path.

        Returns: 
        ----- 
        An absolute pathname to the texture file referenced by the node.
        If the path cannot be resolved than an empty string is returned

        Parameters:
        -----
        fileNode: MObject
        	[in] -> a file texture node 

        ReturnStatus: MRenderUtil.MStatus
        	[out] -> status code


        '''
        pass

    @overload
    def exactFileTextureName(self, baseName: MString,
                        useFrameExt: bool,
                        currentFrameExt: MString,
                        contextNodeFullName: MString,
                        ReturnStatus: MRenderUtil.MStatus): 
        '''
        exactFileTextureName(self, baseName: MString,
                        useFrameExt: bool,
                        currentFrameExt: MString,
                        contextNodeFullName: MString,
                        ReturnStatus: MRenderUtil.MStatus) -> MString

        Synopsis
        -----
        Attempts to resolve the file name specified into an absolute path
        to a file on disk. The function applies exactly the same logic
        that is used by the file texture node internally for resolving
        the image file path.

        Returns: 
        ----- 
        An absolute path to the texture based on its file name. If the
        path cannot be resolved, then an empty string is returned.

        Parameters:
        -----
        baseName: MString
        	[in] -> a file name to be resolved 

        useFrameExt: bool
        	[in] -> use frame extension for image file name 

        currentFrameExt: MString
        	[in] -> specify a frame extension if useFrameExt is used. 

        contextNodeFullName: MString
        	[in] -> full name of the file owner Node. 

        ReturnStatus: MRenderUtil.MStatus
        	[out] -> status code


        '''
        pass

    @overload
    def convertPsdFile(self, fileNode: MObject,
                        forExport: bool,
                        ReturnStatus: MRenderUtil.MStatus): 
        '''
        convertPsdFile(self, fileNode: MObject,
                        forExport: bool,
                        ReturnStatus: MRenderUtil.MStatus) -> MString

        Synopsis
        -----
        Internal use only. This method converts a Psd file texture to an
        IFF file that can be used by Maya.It writes out the current layer
        set image the file node. The intermediate image will be either 8
        or 16 b.p.c, based on the input psd file.

        Returns: 
        ----- 
        true if the image file pathname was successfully resolved and
        exporting psd file is succeeded.  false if the pathname could not
        be resolved or exporting psd file fails.

        Parameters:
        -----
        fileNode: MObject
        	[in] -> a file texture node 

        forExport: bool
        	[out] -> if true the resulting IFF file will be stored in the project directory tree, otherwise it will be stored in a temporary file which will be deleted when Maya exits. 

        ReturnStatus: MRenderUtil.MStatus
        	[out] -> status code


        '''
        pass

    @overload
    def exactImagePlaneFileName(self, imagePlaneNode: MObject,
                        ReturnStatus: MRenderUtil.MStatus): 
        '''
        exactImagePlaneFileName(self, imagePlaneNode: MObject,
                        ReturnStatus: MRenderUtil.MStatus) -> MString

        Synopsis
        -----
        Attempts to resolve the file texture name specified on an image
        plane node into an absolute path to an image file on disk. The
        function applies exactly the same logic that is used by the image
        plane node internally for resolving the image file path.

        Returns: 
        ----- 
        An absolute pathname to the texture file referenced by the node.
        If the pathname cannot be resolved, then the returned string is
        empty

        Parameters:
        -----
        imagePlaneNode: MObject
        	[in] -> an image plane node 

        ReturnStatus: MRenderUtil.MStatus
        	[out] -> status code


        '''
        pass

    def inCurrentRenderLayer(self, objectPath: MDagPath,
                        ReturnStatus: MRenderUtil.MStatus): 
        '''
        inCurrentRenderLayer(self, objectPath: MDagPath,
                        ReturnStatus: MRenderUtil.MStatus) -> bool

        Synopsis
        -----
        Returns true if the specified path is in the current render
        layer. If the object at the end of the DAG path has not been
        assigned to any layer, then each node in hierarchy from bottom up
        will be tested whether its contained in the current render layer.

        Returns: 
        ----- 
        true if the object is in the current render layer.

        Parameters:
        -----
        objectPath: MDagPath
        	[in] -> Path of object to test 

        ReturnStatus: MRenderUtil.MStatus
        	[out] -> Status code


        '''
        pass

    def renderPass(self): 
        '''
        renderPass(self) -> MRenderUtil.MRenderUtil

        Synopsis
        -----
        Returns an enumerated type specifying the current pass the Maya
        renderer is executing.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def mainBeautyPassCustomTokenString(self): 
        '''
        mainBeautyPassCustomTokenString(self) -> MString

        Synopsis
        -----
        Returns the custom token string of the main beauty pass for use
        by renderers in file naming.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def mainBeautyPassName(self): 
        '''
        mainBeautyPassName(self) -> MString

        Synopsis
        -----
        Returns the name of the main beauty pass for use by renderers for
        token substitution.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def diffuseReflectance(self, lightBlindData: void,
                        lightDirection: MFloatVector,
                        pointCamera: MFloatVector,
                        normal: MFloatVector,
                        lightBackFace: bool,
                        ReturnStatus: MRenderUtil.MStatus): 
        '''
        diffuseReflectance(self, lightBlindData: void,
                        lightDirection: MFloatVector,
                        pointCamera: MFloatVector,
                        normal: MFloatVector,
                        lightBackFace: bool,
                        ReturnStatus: MRenderUtil.MStatus) -> float

        Synopsis
        -----
        This utility function computes and returns the diffuse or
        lambertian reflectance for a given light source and surface.

        Returns:
        -----
        None

        Parameters:
        -----
        lightBlindData: void
        	[in] -> The reference to the aLightBlindData attribute of the current light being evaluated 

        lightDirection: MFloatVector
        	[in] -> The direction of the light being evaluated 

        pointCamera: MFloatVector
        	[in] -> The position of the camera 

        normal: MFloatVector
        	[in] -> The surface normal 

        lightBackFace: bool
        	[in] -> Is the back face being lit, true or false. 

        ReturnStatus: MRenderUtil.MStatus
        	[out] -> Status code 


        '''
        pass

    def maximumSpecularReflection(self, lightBlindData: void,
                        lightDirection: MFloatVector,
                        pointCamera: MFloatVector,
                        normal: MFloatVector,
                        rayDirection: MFloatVector,
                        ReturnStatus: MRenderUtil.MStatus): 
        '''
        maximumSpecularReflection(self, lightBlindData: void,
                        lightDirection: MFloatVector,
                        pointCamera: MFloatVector,
                        normal: MFloatVector,
                        rayDirection: MFloatVector,
                        ReturnStatus: MRenderUtil.MStatus) -> MFloatVector

        Synopsis
        -----
        This utility function computes and returns the vector
        corresponding to the point on the light source that provides the
        maximum specular reflection.

        Returns:
        -----
        None

        Parameters:
        -----
        lightBlindData: void
        	[in] -> The reference to the aLightBlindData attribute of the current light being evaluated 

        lightDirection: MFloatVector
        	[in] -> The direction of the light being evaluated 

        pointCamera: MFloatVector
        	[in] -> The position of the camera 

        normal: MFloatVector
        	[in] -> The surface normal 

        rayDirection: MFloatVector
        	[in] -> The direction of the current intersection ray in camera space 

        ReturnStatus: MRenderUtil.MStatus
        	[out] -> Status code 


        '''
        pass

    def lightAttenuation(self, lightBlindData: void,
                        pointCamera: MFloatVector,
                        normal: MFloatVector,
                        lightBackFace: bool,
                        ReturnStatus: MRenderUtil.MStatus): 
        '''
        lightAttenuation(self, lightBlindData: void,
                        pointCamera: MFloatVector,
                        normal: MFloatVector,
                        lightBackFace: bool,
                        ReturnStatus: MRenderUtil.MStatus) -> float

        Synopsis
        -----
        This utility function computes and returns light attentuation
        factor of a light. Note that the result of 1 will be returned if
        the light being evaluated does not support light attentuation.

        Returns:
        -----
        None

        Parameters:
        -----
        lightBlindData: void
        	[in] -> The reference to the aLightBlindData attribute of the current light being evaluated 

        pointCamera: MFloatVector
        	[in] -> The position of the camera 

        normal: MFloatVector
        	[in] -> The surface normal 

        lightBackFace: bool
        	[in] -> Is the back face being lit, true or false. 

        ReturnStatus: MRenderUtil.MStatus
        	[out] -> Status code 


        '''
        pass

    def hemisphereCoverage(self, lightBlindData: void,
                        lightDirection: MFloatVector,
                        pointCamera: MFloatVector,
                        rayDirection: MFloatVector,
                        lightBackFace: bool,
                        ReturnStatus: MRenderUtil.MStatus): 
        '''
        hemisphereCoverage(self, lightBlindData: void,
                        lightDirection: MFloatVector,
                        pointCamera: MFloatVector,
                        rayDirection: MFloatVector,
                        lightBackFace: bool,
                        ReturnStatus: MRenderUtil.MStatus) -> float

        Synopsis
        -----
        This utility function computes and returns the fraction of the
        light that is transmitted by an object. It is mostly used for
        translucence and scattering effects.

        Returns:
        -----
        None

        Parameters:
        -----
        lightBlindData: void
        	[in] -> The reference to the aLightBlindData attribute of the current light being evaluated 

        lightDirection: MFloatVector
        	[in] -> The direction of the light being evaluated 

        pointCamera: MFloatVector
        	[in] -> The position of the camera 

        rayDirection: MFloatVector
        	[in] -> The direction of the current intersection ray in camera space 

        lightBackFace: bool
        	[in] -> Is the back face being lit, true or false. 

        ReturnStatus: MRenderUtil.MStatus
        	[out] -> Status code 


        '''
        pass

    def sendRenderProgressInfo(self, pixFile: MString,
                        percentageDone: int): 
        '''
        sendRenderProgressInfo(self, pixFile: MString,
                        percentageDone: int)

        Synopsis
        -----
        This utility function sends batch rendering status to Maya.

        Returns:
        -----
        None

        Parameters:
        -----
        pixFile: MString
        	[in] -> File name of the last rendered batch image 

        percentageDone: int
        	[in] -> percentage rendered 


        '''
        pass

    def getCommonRenderSettings(self, mrgData: MCommonRenderSettingsData): 
        '''
        getCommonRenderSettings(self, mrgData: MCommonRenderSettingsData)

        Synopsis
        -----
        Fill the set of common render setting values.

        Returns:
        -----
        None

        Parameters:
        -----
        mrgData: MCommonRenderSettingsData
        	[out] -> Render settings. 


        '''
        pass

    def renderObjectItem(self, objectId: void,
                        item: MSelectionList): 
        '''
        renderObjectItem(self, objectId: void,
                        item: MSelectionList)

        Synopsis
        -----
        Procedure to look up a selection item for a given sample object
        id. This is only guaranteed to work when software rendering. As
        multiple processors may be used when software rendering; a
        critical section should be used to protect multiple threads from
        simulaneously performing DG evaluation. This includes querying
        attribute values.

        Returns:
        -----
        None

        Parameters:
        -----
        objectId: void
        	[in] -> The sample object id to look-up 

        item: MSelectionList
        	[in] -> The corresponding item for the id


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

    def eval2dTexture(self, texNode: MObject,
                        uCoords: MDoubleArray,
                        vCoords: MDoubleArray,
                        resultColors: MVectorArray,
                        resultAlphas: MDoubleArray): 
        '''
        eval2dTexture(self, texNode: MObject,
                        uCoords: MDoubleArray,
                        vCoords: MDoubleArray,
                        resultColors: MVectorArray,
                        resultAlphas: MDoubleArray)

        Synopsis
        -----
        If a supported texture node is given, this method can be called
        to evaluate that texture at a number of (u,v) texture coordinate
        values.

        Returns:
        -----
        None

        Parameters:
        -----
        texNode: MObject
        	[in] -> texture node to evaluate. It doesn't need to be connected to anything. 

        uCoords: MDoubleArray
        	[in] -> array of u coordinate values 

        vCoords: MDoubleArray
        	[in] -> array of v coordinate values 

        resultColors: MVectorArray
        	[out] -> if non-NULL, receives the result of the connected texture's outColor attribute, evaluated at all the (u,v) coordinates given by the uCoords and vCoords arrays. 

        resultAlphas: MDoubleArray
        	[out] -> if non-NULL, receives the outAlpha values evaluated from the texture at these same points.


        '''
        pass

    def noiseTableSize(self): 
        '''
        noiseTableSize(self) -> int

        Synopsis
        -----
        Access the size of Maya's noise table. The noise table is a
        constant set of random floating point values in the range [-1.0,
        1.0] used by many of Maya's procedural textures.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def noiseTableCubeSide(self): 
        '''
        noiseTableCubeSide(self) -> int

        Synopsis
        -----
        The size of Maya's noise table is a perfect cube. This method
        returns the cubic root of the table size.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def valueInNoiseTable(self, index: int): 
        '''
        valueInNoiseTable(self, index: int) -> float

        Synopsis
        -----
        Returns a raw value from Maya's noise table at the given index.
        If the index is out of bounds, the index modulo noiseTableSize()
        is used instead. The noise table is a constant set of random
        floating point values in the range [-1.0, 1.0] used by many of
        Maya's procedural textures.

        Returns: 
        ----- 
        A value from the noise table in the range [-1.0, 1.0]

        Parameters:
        -----
        index: int
        	[in] -> The index to retrieve from the noise table


        '''
        pass

    def noise1(self, x: float): 
        '''
        noise1(self, x: float) -> float

        Synopsis
        -----
        Generates continous non-repeating one dimensional noise based on
        Maya's internal noise table.

        Returns: 
        ----- 
        A noise value that is non-repeating and continuous on the given
        coordinate

        Parameters:
        -----
        x: float
        	[in] -> The one dimensional coordinate for which to generate noise


        '''
        pass

    def noise2(self, x: float,
                        y: float): 
        '''
        noise2(self, x: float,
                        y: float) -> float

        Synopsis
        -----
        Generates continous non-repeating two dimensional noise based on
        Maya's internal noise table.

        Returns: 
        ----- 
        A noise value that is non-repeating and continuous on the given
        coordinate

        Parameters:
        -----
        x: float
        	[in] -> The x coordinate for which to generate noise 

        y: float
        	[in] -> The y coordinate for which to generate noise


        '''
        pass

    def noise3(self, x: float,
                        y: float,
                        z: float): 
        '''
        noise3(self, x: float,
                        y: float,
                        z: float) -> float

        Synopsis
        -----
        Generates continous non-repeating three dimensional noise based
        on Maya's internal noise table.

        Returns: 
        ----- 
        A noise value that is non-repeating and continuous on the given
        coordinate

        Parameters:
        -----
        x: float
        	[in] -> The x coordinate for which to generate noise 

        y: float
        	[in] -> The y coordinate for which to generate noise 

        z: float
        	[in] -> The y coordinate for which to generate noise


        '''
        pass

    def noise4(self, x: float,
                        y: float,
                        z: float,
                        t: float,
                        numTimeSteps: short): 
        '''
        noise4(self, x: float,
                        y: float,
                        z: float,
                        t: float,
                        numTimeSteps: short) -> float

        Synopsis
        -----
        Generates continous four dimensional (space + time) noise based
        on Maya's internal noise table. The noise will loop in a seamless
        manner. The larger the value for the numTimeSteps parameter the
        longer it will take for the noise to loop (i.e. more samples
        would be required along the time axis to cause the sequence to
        restart).

        Returns: 
        ----- 
        A noise value that is continuous on the given coordinate

        Parameters:
        -----
        x: float
        	[in] -> The x coordinate for which to generate noise 

        y: float
        	[in] -> The y coordinate for which to generate noise 

        z: float
        	[in] -> The y coordinate for which to generate noise 

        t: float
        	[in] -> The time coordinate for which to generate noise 

        numTimeSteps: short
        	[in] -> Controls the repetition of the noise with respect to time


        '''
        pass

class MRenderState:
    '''Defines the current rendering state of Maya. 
    Non-functional class.  Values for this enum:
    kNotRendering
    kBatchRender
    kInteractiveRender
    kIprRender
    kHardwareRender
    '''

    def __init__(self):
        pass

    def kNotRendering(self):
        '''This is an enum of MRenderState.
        - Description: Not rendering. 
        - Value: 0
        '''
        pass

    def kBatchRender(self):
        '''This is an enum of MRenderState.
        - Description: Performing a batch render. 
        - Value: 1
        '''
        pass

    def kInteractiveRender(self):
        '''This is an enum of MRenderState.
        - Description: Performing an interactive render. 
        - Value: 2
        '''
        pass

    def kIprRender(self):
        '''This is an enum of MRenderState.
        - Description: Performing an IPR render. 
        - Value: 3
        '''
        pass

    def kHardwareRender(self):
        '''This is an enum of MRenderState.
        - Description: Performing a hardware render. 
        - Value: 4
        '''
        pass

class MRenderPass:
    '''Defines the current pass of Maya. 
    Non-functional class.  Values for this enum:
    kAll
    kColorOnly
    kShadowOnly
    kAmbientOnly
    kDiffuseOnly
    kSpecularOnly
    '''

    def __init__(self):
        pass

    def kAll(self):
        '''This is an enum of MRenderPass.
        - Description: Default case, compute everything. 
        - Value: 0
        '''
        pass

    def kColorOnly(self):
        '''This is an enum of MRenderPass.
        - Description: Compute only color information, no shadows. 
        - Value: 1
        '''
        pass

    def kShadowOnly(self):
        '''This is an enum of MRenderPass.
        - Description: Compute only shadow information, no color. 
        - Value: 2
        '''
        pass

    def kAmbientOnly(self):
        '''This is an enum of MRenderPass.
        - Description: Compute only ambient information. 
        - Value: 3
        '''
        pass

    def kDiffuseOnly(self):
        '''This is an enum of MRenderPass.
        - Description: Compute only diffuse information. 
        - Value: 4
        '''
        pass

    def kSpecularOnly(self):
        '''This is an enum of MRenderPass.
        - Description: Compute only specular information. 
        - Value: 5
        '''
        pass

class MRenderView:
    '''Static class providing Render View API functions.
This class provides access to the Maya Render View. The class
allows plugins to send image data to the Render View in the same
way that the Maya renderer does. Either a "full render" or a
"region   render" can be performed. In a full render, the Render
View expects to receive pixel data that fills the entire image,
while a region render expects only updates to a specified image
region.
To send an image to the Render View, use the following sequence
of calls:
'''
    def __init__(self):
        pass


    def doesRenderEditorExist(self): 
        '''
        doesRenderEditorExist(self) -> MRenderView.OPENMAYA_MAJOR_NAMESPACE_OPENbool

        Synopsis
        -----
        Determines whether or not a Render View exists to receive image
        data. If this function returns false, then Maya is currently
        running in batch mode, so it would be pointless to try to send
        data to the Render View.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setCurrentCamera(self, currentCamera: MDagPath): 
        '''
        setCurrentCamera(self, currentCamera: MDagPath)

        Synopsis
        -----
        Informs the render client of the camera that will be performing
        the rendering.

        Returns:
        -----
        None

        Parameters:
        -----
        currentCamera: MDagPath
        	[in] -> Camera to be used in the render.


        '''
        pass

    def getRenderRegion(self, left: int,
                        right: int,
                        bottom: int,
                        top: int): 
        '''
        getRenderRegion(self, left: int,
                        right: int,
                        bottom: int,
                        top: int)

        Synopsis
        -----
        Retrieves the currently selected Render Region in Maya's Render
        View. The region extends from the bottom-left corner
        (left,bottom) to the upper-right corner (right,top) inclusive
        (i.e. the row y=top and column x=right are part of the region).

        Returns:
        -----
        None

        Parameters:
        -----
        left: int
        	[out] -> receives the left extent of the region 

        right: int
        	[out] -> receives the right extent of the region 

        bottom: int
        	[out] -> receives the bottom extent of the region 

        top: int
        	[out] -> receives the top extent of the region


        '''
        pass

    def startRender(self, width: int,
                        height: int,
                        doNotClearBackground: bool,
                        immediateFeedback: bool): 
        '''
        startRender(self, width: int,
                        height: int,
                        doNotClearBackground: bool,
                        immediateFeedback: bool)

        Synopsis
        -----
        Informs the Render View that a full image render is about to
        begin. The entire Render View buffer will be cleared in
        anticipation of receiving an entire image.

        Returns:
        -----
        None

        Parameters:
        -----
        width: int
        	[in] -> width of the image to be sent to the Render View (must be greater than zero). 

        height: int
        	[in] -> height of the image to be sent to the Render View (must be greater than zero). 

        doNotClearBackground: bool
        	[in] -> When true, the Render View is not cleared before starting to draw. Default (false) is to clear the Render View. 

        immediateFeedback: bool
        	[in] -> When true, each call to 


        '''
        pass

    def startRegionRender(self, imageWidth: int,
                        imageHeight: int,
                        regionLeft: int,
                        regionRight: int,
                        regionBottom: int,
                        regionTop: int,
                        doNotClearBackground: bool,
                        immediateFeedback: bool): 
        '''
        startRegionRender(self, imageWidth: int,
                        imageHeight: int,
                        regionLeft: int,
                        regionRight: int,
                        regionBottom: int,
                        regionTop: int,
                        doNotClearBackground: bool,
                        immediateFeedback: bool)

        Synopsis
        -----
        Informs the Render View that a region render is about to begin.
        The specified region will be cleared in anticipation of receiving
        new image data for it. The specified region must lie within the
        image region (0,0)->(imageWidth-1,imageHeight-1). The region
        'left' coordinate must be less than the region 'right'
        coordinate, and the region 'bottom' coordinate must be less than
        the region 'top' coordinate.

        Returns:
        -----
        None

        Parameters:
        -----
        imageWidth: int
        	[in] -> width of the image in which the region is embedded. (must be greater than zero). 

        imageHeight: int
        	[in] -> height of the image in which the region is embedded (must be greater than zero). 

        regionLeft: int
        	[in] -> left extent of the region. 

        regionRight: int
        	[in] -> right extent of the region. The column x=regionRight is considered part of the region. 

        regionBottom: int
        	[in] -> bottom extent of the region. 

        regionTop: int
        	[in] -> top extent of the region. The row y=regionTop is considered part of the region. 

        doNotClearBackground: bool
        	[in] -> When true, the Render View is not cleared before starting to draw. Default (false) is to clear the Render View. 

        immediateFeedback: bool
        	[in] -> When true, each call to 


        '''
        pass

    def updatePixels(self, left: int,
                        right: int,
                        bottom: int,
                        top: int,
                        pPixels: RV_PIXEL,
                        isHdr: bool,
                        numberOfAOVs: int,
                        pAOVs: RV_AOV): 
        '''
        updatePixels(self, left: int,
                        right: int,
                        bottom: int,
                        top: int,
                        pPixels: RV_PIXEL,
                        isHdr: bool,
                        numberOfAOVs: int,
                        pAOVs: RV_AOV)

        Synopsis
        -----
        Sends a block of pixels to the Render View. Pixel colors are
        represented as 4-channel floating point values. For low dynamic
        range images, color values are in standard RGB (sRGB) colorspace,
        and in the range (0,255.0). For high dynamic range (HDR) images,
        the range is unbounded, and values are in linear CIE XYZ color
        space, with the X, Y, and Z values stored respectively in the R,
        G and B fields of the RV_PIXEL structure. Alpha values for HDR
        images are expected to be in the range (0,1). Out of range alpha
        values are not clamped, and may behave unexpectedly.

        Returns:
        -----
        None

        Parameters:
        -----
        left: int
        	[in] -> left extent of the update region. 

        right: int
        	[in] -> right extent of the update region. The column x=right is considered part of the region. 

        bottom: int
        	[in] -> bottom extent of the update region. 

        top: int
        	[in] -> top extent of the update region. The row y=regionTop is considered part of the region. 

        pPixels: RV_PIXEL
        	[in] -> buffer containing the pixel data for the image. The buffer should contain (right-left+1)*(top-bottom+1) pixels. 

        isHdr: bool
        	[in] -> indicates whether the image has high dynamic range 

        numberOfAOVs: int
        	[in] -> indicates the number of arbitrary output variable (AOV) buffers (not yet implemented). 

        pAOVs: RV_AOV
        	[in] -> array of 


        '''
        pass

    def refresh(self, left: int,
                        right: int,
                        bottom: int,
                        top: int): 
        '''
        refresh(self, left: int,
                        right: int,
                        bottom: int,
                        top: int)

        Synopsis
        -----
        Requests that the Render View refresh the display of a particular
        region of the displayed image.

        Returns:
        -----
        None

        Parameters:
        -----
        left: int
        	[in] -> left extent of the update region. 

        right: int
        	[in] -> right extent of the update region. The column x=right is considered part of the region. 

        bottom: int
        	[in] -> bottom extent of the update region. 

        top: int
        	[in] -> top extent of the update region. The row y=regionTop is considered part of the region.


        '''
        pass

    def endRender(self): 
        '''
        endRender(self)

        Synopsis
        -----
        Informs the Render View that the current render has completed.
        The Render View is refreshed and no further updates are accepted.

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

class MSwatchRenderBase:
    '''Swatch Render Base class.
A class providing an interface through which a plugin can
implement a class to provide custom rendered images for swatches
which are displayed in hypershade and the Attribute Editor.
By deriving from this class and implementing the doIteration
function, swatches for nodes (having the required classification)
can be custom rendered by the plugin.
The derived class needs to be registered with Maya using the
interface provided by
MSwatchRenderRegister. Please refer to documentation of
MSwatchRenderRegister for more details.
To indicate that swatch for a certain node type will be generated
by the plugin the classfication string of the node needs to
contain the following string : "swatch/<swatch generator name>"
The swatch generator name string should match the name used to
register the swatch generator class.
'''
    def __init__(self):
        pass


    def doIteration(self): 
        '''
        doIteration(self) -> bool

        Synopsis
        -----
        Method called from the MSwatchRenderRegister for generation of
        swatch image. The doIteration function is called repeatedly
        (during idle events) until it returns true. Using this swatch
        image can be generated in stages.This method should be overridden
        in derived classes which can compute the swatches in several
        steps.Reimplemented in MHWShaderSwatchGenerator.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def renderParallel(self): 
        '''
        renderParallel(self) -> bool

        Synopsis
        -----
        Method indicates if the swatch is rendered parallel.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def cancelParallelRendering(self): 
        '''
        cancelParallelRendering(self)

        Synopsis
        -----
        Method to cancel the parallel rendering. The derived classes
        should provide the implementation accordingly if required.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setRenderQuality(self, quality: int): 
        '''
        setRenderQuality(self, quality: int)

        Synopsis
        -----
        Method to set the render quality in which the swatch will be
        rendered. The derived classes should make sure that the larger
        the number is set, the better quality is applied.

        Returns:
        -----
        None

        Parameters:
        -----
        quality: int
        	[in] -> The quality to render the swatch 


        '''
        pass

    def renderQuality(self): 
        '''
        renderQuality(self) -> int

        Synopsis
        -----
        Returns the quality in which the swatch will be rendered.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def cancelCurrentSwatchRender(self): 
        '''
        cancelCurrentSwatchRender(self)

        Synopsis
        -----
        The method cancels the swatch which is being rendered in
        parallel, and push the swatch render item back to the render
        queue after. The render plugins should make sure that
        MSwatchRenderBase::cancelParallelRendering() is implemented
        acoordingly.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def enableSwatchRender(self, enable: bool): 
        '''
        enableSwatchRender(self, enable: bool)

        Synopsis
        -----
        Enable/disable swatch rendering.

        Returns:
        -----
        None

        Parameters:
        -----
        enable: bool
        	[in] -> Flag indicating if swatch rendering should be enabled or disabled. 


        '''
        pass

    def finishParallelRender(self): 
        '''
        finishParallelRender(self)

        Synopsis
        -----
        Method to update the swatch image when the parallel rendering is
        finished. If swatch is rendered parallel, this method must be
        called after parallel rendering finished.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MSwatchRenderRegister:
    '''Manages swatch generators.
Provides an interface for plugins to register/unregister swatch
generator classes (derived from
MSwatchRenderBase) with Maya. Whenever a swatch needs to be generated for a node,
it checks the classfication string of the node for the preferred
swatch generator. If a match is found, it creates and manages the
swatch generator object (that is it deletes the swatch generator
object once the image has been generated). The doIteration
function is called for generating the swatch. The doIteration
function is called repeatedly (during idle events) till it
returns true. This allows for generation of the swatch in stages.
'''
    def __init__(self):
        pass


    def registerSwatchRender(self, swatchGenName: MString,
                        fnPtr: MSwatchRenderCreatorFnPtr): 
        '''
        registerSwatchRender(self, swatchGenName: MString,
                        fnPtr: MSwatchRenderCreatorFnPtr) -> MSwatchRenderRegister.OPENMAYA_MAJOR_NAMESPACE_OPEN MStatus

        Synopsis
        -----
        registers a new swatch generator creation function by name.
        Register the swatch rendering object creation function with the
        swatch render manager.The signature of the function needs to be
        as follows: This function needs to allocate the swatch generator
        object using new and return the pointer. (This is necessary
        because delete is called on the returned pointer by Maya when
        work is done.)

        Returns: 
        ----- 
        MS::kFailure if an error occured. Common potential errors
        include: the swatch generator name has already been used.
        MS::kSuccess otherwise.

        Parameters:
        -----
        swatchGenName: MString
        	[in] -> A name to identify the swatch generator. Should match the name used in the "swatch" classfication string of the nodes

        fnPtr: MSwatchRenderCreatorFnPtr
        	[in] -> Pointer to a function which takes the node and resolution of the swatch image to be generated and creates the swatch generator object.


        '''
        pass

    def unregisterSwatchRender(self, swatchGen: MString): 
        '''
        unregisterSwatchRender(self, swatchGen: MString)

        Synopsis
        -----
        removes the previously registered swatch generator Un-register
        the swatch rendering object from the swatch render manager.

        Returns:
        -----
        None

        Parameters:
        -----
        swatchGen: MString
        	[in] -> The name which was used for the swatch generator. Should match the name used during registration.


        '''
        pass

class MUniformParameter:
    '''Uniform parameter.
The
MUniformParameter class provides a high-level interface to hardware shader uniform
parameters. By defining your shader's uniform parameters through
this class, you allow Maya to handle the attributes, editing,
serialisation, and caching for you in a standard way that ensure
you'll be able to leverage future performance and functionlity
improvements.
At setup time (either initial load or when the effect/technique
is changed), your shader simply creates the list of parameters it
requires, specifying the name, type, semantic of the parameters.
At render time, you can then use the parameters to directly
access the appropriate buffers for that surface data.
If you include a custom Attribute Editor template for your shader
node, you can include these surface parameters by calling the
AEhwUniformTemplateParameters script function. The following
sample code provides a basic template you can modify - however
your AE template can use as much or as little of this as you
like:
'''
    def __init__(self):
        pass


    def name(self): 
        '''
        name(self) -> MString

        Synopsis
        -----
        Get the name of this parameter.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def type(self): 
        '''
        type(self) -> MUniformParameter.MUniformParameter

        Synopsis
        -----
        Get the type of this parameter.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def semantic(self): 
        '''
        semantic(self) -> MUniformParameter.MUniformParameter

        Synopsis
        -----
        Get the semantic of this parameter.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def numRows(self): 
        '''
        numRows(self) -> int

        Synopsis
        -----
        Get the number of rows in this parameter.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def numColumns(self): 
        '''
        numColumns(self) -> int

        Synopsis
        -----
        Get the number of columns in this parameter.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def numElements(self): 
        '''
        numElements(self) -> int

        Synopsis
        -----
        Get the number of elements in this parameter (including rows and
        columns)

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def userData(self): 
        '''
        userData(self) -> void*

        Synopsis
        -----
        Get the user data for this parameter. User data can be used to
        store plugin specific information that you want to associate with
        this parameter. Typically this will be used to store a handle to
        the effect parameter.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setRangeMin(self, rangeMin: double): 
        '''
        setRangeMin(self, rangeMin: double)

        Synopsis
        -----
        Sets the hard range lower bound for a numeric uniform parameter.

        Returns:
        -----
        None

        Parameters:
        -----
        rangeMin: double
        	[in] -> The lower bound of the range. 


        '''
        pass

    def setRangeMax(self, rangeMax: double): 
        '''
        setRangeMax(self, rangeMax: double)

        Synopsis
        -----
        Sets the hard range upper bound for a numeric uniform parameter.

        Returns:
        -----
        None

        Parameters:
        -----
        rangeMax: double
        	[in] -> The upper bound of the range. 


        '''
        pass

    def setSoftRangeMin(self, softRangeMin: double): 
        '''
        setSoftRangeMin(self, softRangeMin: double)

        Synopsis
        -----
        Sets the soft range lower bound for a numeric uniform parameter.

        Returns:
        -----
        None

        Parameters:
        -----
        softRangeMin: double
        	[in] -> The lower bound of the slider. 


        '''
        pass

    def setSoftRangeMax(self, softRangeMax: double): 
        '''
        setSoftRangeMax(self, softRangeMax: double)

        Synopsis
        -----
        Sets the soft range upper bound for a numeric uniform parameter.

        Returns:
        -----
        None

        Parameters:
        -----
        softRangeMax: double
        	[in] -> The upper bound of the slider. 


        '''
        pass

    def setUIHidden(self, hiddenState: bool): 
        '''
        setUIHidden(self, hiddenState: bool)

        Synopsis
        -----
        Sets the hidden state of this parameter.

        Returns:
        -----
        None

        Parameters:
        -----
        hiddenState: bool
        	[in] -> True will hide the corresponding attribute in the attribute editor. 


        '''
        pass

    def UIHidden(self): 
        '''
        UIHidden(self) -> bool

        Synopsis
        -----
        Gets the hidden state of this parameter.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setEnumFieldNames(self, fieldNames: MString): 
        '''
        setEnumFieldNames(self, fieldNames: MString)

        Synopsis
        -----
        Sets the field names of an enum attribute. The format of the
        string is the same as returned by the MEL command `attributeQuery
        -listEnum`.

        Returns:
        -----
        None

        Parameters:
        -----
        fieldNames: MString
        	[in] -> A string of colon ":" delimited field names which can specify an index value separated by an equal sign "=". The indexing starts at zero and the index value of an item when it is not explicitely specified is the index of the previous item (if any) incremented by one. Example: "Shaded:Wireframe=8:Bounding Box" defines 3 values with index 0, 8, and 9. 


        '''
        pass

    def setKeyable(self, keyable: bool): 
        '''
        setKeyable(self, keyable: bool)

        Synopsis
        -----
        Sets the keyable state of this parameter.

        Returns:
        -----
        None

        Parameters:
        -----
        keyable: bool
        	[in] -> True if the attribute should be keyable 


        '''
        pass

    def keyable(self): 
        '''
        keyable(self) -> bool

        Synopsis
        -----
        Gets the keyable state of this parameter.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def isATexture(self): 
        '''
        isATexture(self) -> bool

        Synopsis
        -----
        Test if this parameter stores a texture.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def hasChanged(self, iterator: MGeometryList): 
        '''
        hasChanged(self, iterator: MGeometryList) -> bool

        Synopsis
        -----
        Has the value of this parameter changed since the last time it
        was accessed? This allows your shader to minimise state changes
        by only updating modified parameters.

        Returns: 
        ----- 
        true if this parameter's value has changed since the last time
        its value was accessed. false otherwise.

        Parameters:
        -----
        iterator: MGeometryList
        	[in] -> the current shape being rendered.


        '''
        pass

    @overload
    def hasChanged(self, context: MHWRender.MHWRender): 
        '''
        hasChanged(self, context: MHWRender.MHWRender) -> bool

        Synopsis
        -----
        Has the value of this parameter changed since the last time it
        was accessed? This allows your shader to minimise state changes
        by only updating modified parameters.

        Returns: 
        ----- 
        true if this parameter's value has changed since the last time
        its value was accessed. false otherwise.

        Parameters:
        -----
        context: MHWRender.MHWRender
        	[in] -> Draw context being used for render.


        '''
        pass

    @overload
    def getAsFloatArray(self, iterator: MGeometryList): 
        '''
        getAsFloatArray(self, iterator: MGeometryList) -> float*

        Synopsis
        -----
        Get the value of this uniform parameter as one or more floating
        point values. Because some parameters can be shape-dependent, the
        method requires access to the current geometry item being
        rendered.

        Returns: 
        ----- 
        A pointer to an array of floating point values for this uniform
        parameter.

        Parameters:
        -----
        iterator: MGeometryList
        	[in] -> the current shape being rendered.


        '''
        pass

    @overload
    def getAsFloatArray(self, context: MHWRender.MHWRender): 
        '''
        getAsFloatArray(self, context: MHWRender.MHWRender) -> float*

        Synopsis
        -----
        Get the value of this uniform parameter as one or more floating
        point values. Because some parameters can be shape-dependent, the
        method requires access to the current context being rendered.

        Returns: 
        ----- 
        A pointer to an array of floating point values for this uniform
        parameter.

        Parameters:
        -----
        context: MHWRender.MHWRender
        	[in] -> Draw context being used for render.


        '''
        pass

    def setAsFloatArray(self, value: float,
                        maxElements: int): 
        '''
        setAsFloatArray(self, value: float,
                        maxElements: int)

        Synopsis
        -----
        Set the value of this uniform parameter as one or more floating
        point values. Note that it is not possible to set shape-specific
        parameters.

        Returns:
        -----
        None

        Parameters:
        -----
        value: float
        	[in] -> a pointer an array of floats holding the new floating point value(s) for this parameter. 

        maxElements: int
        	[in] -> the maximum number of elements in the value array. 


        '''
        pass

    @overload
    def getAsFloat(self, iterator: MGeometryList): 
        '''
        getAsFloat(self, iterator: MGeometryList) -> float

        Synopsis
        -----
        Get the value of this uniform parameter as a float. Because some
        parameters can be shape-dependent, the method requires access to
        the current geometry item being rendered.

        Returns: 
        ----- 
        The current float value of this uniform parameter.

        Parameters:
        -----
        iterator: MGeometryList
        	[in] -> the current shape being rendered.


        '''
        pass

    @overload
    def getAsFloat(self, context: MHWRender.MHWRender): 
        '''
        getAsFloat(self, context: MHWRender.MHWRender) -> float

        Synopsis
        -----
        Get the value of this uniform parameter as a float. Because some
        parameters can be shape-dependent, the method requires access to
        the current context being rendered.

        Returns: 
        ----- 
        The current float value of this uniform parameter.

        Parameters:
        -----
        context: MHWRender.MHWRender
        	[in] -> Draw context being used for render.


        '''
        pass

    def setAsFloat(self, value: float): 
        '''
        setAsFloat(self, value: float)

        Synopsis
        -----
        Set the value of this uniform parameter as a float. Note that it
        is not possible to set shape-dependent parameters.

        Returns:
        -----
        None

        Parameters:
        -----
        value: float
        	[in] -> the new float value for this parameter. 


        '''
        pass

    @overload
    def getAsString(self, iterator: MGeometryList): 
        '''
        getAsString(self, iterator: MGeometryList) -> MString

        Synopsis
        -----
        Get the value of this uniform parameter as a string. Because some
        parameters can be shape-dependent, the method requires access to
        the current geometry item being rendered.

        Returns: 
        ----- 
        The current string value of this uniform parameter.

        Parameters:
        -----
        iterator: MGeometryList
        	[in] -> the current shape being rendered.


        '''
        pass

    @overload
    def getAsString(self, context: MHWRender.MHWRender): 
        '''
        getAsString(self, context: MHWRender.MHWRender) -> MString

        Synopsis
        -----
        Get the value of this uniform parameter as a string. Because some
        parameters can be shape-dependent, the method requires access to
        the current context being rendered.

        Returns: 
        ----- 
        The current string value of this uniform parameter.

        Parameters:
        -----
        context: MHWRender.MHWRender
        	[in] -> Draw context being used for render.


        '''
        pass

    def setAsString(self, value: MString): 
        '''
        setAsString(self, value: MString)

        Synopsis
        -----
        Set the value of this uniform parameter as a string. Note that it
        is not possible to set shape-dependent parameters.

        Returns:
        -----
        None

        Parameters:
        -----
        value: MString
        	[in] -> the new string value for this parameter. 


        '''
        pass

    @overload
    def getAsBool(self, iterator: MGeometryList): 
        '''
        getAsBool(self, iterator: MGeometryList) -> bool

        Synopsis
        -----
        Get the value of this uniform parameter as a boolean value.
        Because some parameters can be shape-dependent, the method
        requires access to the current geometry item being rendered.

        Returns: 
        ----- 
        The current boolean value of this uniform parameter.

        Parameters:
        -----
        iterator: MGeometryList
        	[in] -> the current shape being rendered.


        '''
        pass

    @overload
    def getAsBool(self, context: MHWRender.MHWRender): 
        '''
        getAsBool(self, context: MHWRender.MHWRender) -> bool

        Synopsis
        -----
        Get the value of this uniform parameter as a boolean value.
        Because some parameters can be shape-dependent, the method
        requires access to the current context being rendered.

        Returns: 
        ----- 
        The current boolean value of this uniform parameter.

        Parameters:
        -----
        context: MHWRender.MHWRender
        	[in] -> Draw context being used for render.


        '''
        pass

    def setAsBool(self, value: bool): 
        '''
        setAsBool(self, value: bool)

        Synopsis
        -----
        Set the value of this uniform parameter as a boolean value. Note
        that it is not possible to set shape-dependent parameters.

        Returns:
        -----
        None

        Parameters:
        -----
        value: bool
        	[in] -> the new value for this parameter. 


        '''
        pass

    @overload
    def getAsInt(self, iterator: MGeometryList): 
        '''
        getAsInt(self, iterator: MGeometryList) -> int

        Synopsis
        -----
        Get the value of this uniform parameter as an integer. Because
        some parameters can be shape-dependent, the method requires
        access to the current geometry item being rendered.

        Returns: 
        ----- 
        The current integer value of this uniform parameter.

        Parameters:
        -----
        iterator: MGeometryList
        	[in] -> the current shape being rendered.


        '''
        pass

    @overload
    def getAsInt(self, context: MHWRender.MHWRender): 
        '''
        getAsInt(self, context: MHWRender.MHWRender) -> int

        Synopsis
        -----
        Get the value of this uniform parameter as an integer. Because
        some parameters can be shape-dependent, the method requires
        access to the current context being rendered.

        Returns: 
        ----- 
        The current integer value of this uniform parameter.

        Parameters:
        -----
        context: MHWRender.MHWRender
        	[in] -> Draw context being used for render.


        '''
        pass

    def setAsInt(self, value: int): 
        '''
        setAsInt(self, value: int)

        Synopsis
        -----
        Set the value of this uniform parameter as an integer value. Note
        that it is not possible to set shape-dependent parameters.

        Returns:
        -----
        None

        Parameters:
        -----
        value: int
        	[in] -> the new value for this parameter. 


        '''
        pass

    def setUINiceName(self, name: MString): 
        '''
        setUINiceName(self, name: MString)

        Synopsis
        -----
        Sets the UI Nice Name for the attribute.

        Returns:
        -----
        None

        Parameters:
        -----
        name: MString
        	[in] -> The name that will be displayed in the Attribute Editor 


        '''
        pass

    def getSource(self): 
        '''
        getSource(self) -> MPlug

        Synopsis
        -----
        Get the source plug connected to this parameter. Other than
        textures, this will typically be a NULL plug.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setDirty(self): 
        '''
        setDirty(self)

        Synopsis
        -----
        Mark the data for this parameter as dirty. This will force the
        parameter to report that it has been changed the next time it is
        accessed. This allows external events (e.g. device lost, texture
        management, etc) to force a shader to re-set parameters tied to
        externally managed resources.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class DataType:
    '''Parameter data types. 
    Non-functional class.  Values for this enum:
    kTypeUnknown
    kTypeBool
    kTypeInt
    kTypeFloat
    kType1DTexture
    kType2DTexture
    kType3DTexture
    kTypeCubeTexture
    kTypeEnvTexture
    kTypeString
    kTypeEnum
    '''

    def __init__(self):
        pass

    def kTypeUnknown(self):
        '''This is an enum of DataType.
        - Description:  
        - Value: 0
        '''
        pass

    def kTypeBool(self):
        '''This is an enum of DataType.
        - Description:  
        - Value: 1
        '''
        pass

    def kTypeInt(self):
        '''This is an enum of DataType.
        - Description:  
        - Value: 2
        '''
        pass

    def kTypeFloat(self):
        '''This is an enum of DataType.
        - Description:  
        - Value: 3
        '''
        pass

    def kType1DTexture(self):
        '''This is an enum of DataType.
        - Description:  
        - Value: 4
        '''
        pass

    def kType2DTexture(self):
        '''This is an enum of DataType.
        - Description:  
        - Value: 5
        '''
        pass

    def kType3DTexture(self):
        '''This is an enum of DataType.
        - Description:  
        - Value: 6
        '''
        pass

    def kTypeCubeTexture(self):
        '''This is an enum of DataType.
        - Description:  
        - Value: 7
        '''
        pass

    def kTypeEnvTexture(self):
        '''This is an enum of DataType.
        - Description:  
        - Value: 8
        '''
        pass

    def kTypeString(self):
        '''This is an enum of DataType.
        - Description:  
        - Value: 9
        '''
        pass

    def kTypeEnum(self):
        '''This is an enum of DataType.
        - Description:  
        - Value: 10
        '''
        pass

class DataSemantic:
    '''Parameter semantics (i.e. what the parameter represents). 
    Non-functional class.  Values for this enum:
    kSemanticUnknown
    kSemanticObjectDir
    kSemanticWorldDir
    kSemanticViewDir
    kSemanticProjectionDir
    kSemanticObjectPos
    kSemanticWorldPos
    kSemanticViewPos
    kSemanticProjectionPos
    kSemanticColor
    kSemanticNormal
    kSemanticBump
    kSemanticEnvironment
    kSemanticWorldMatrix
    kSemanticWorldInverseMatrix
    kSemanticWorldInverseTransposeMatrix
    kSemanticViewMatrix
    kSemanticViewInverseMatrix
    kSemanticViewInverseTransposeMatrix
    kSemanticProjectionMatrix
    kSemanticProjectionInverseMatrix
    kSemanticProjectionInverseTransposeMatrix
    kSemanticWorldViewMatrix
    kSemanticWorldViewInverseMatrix
    kSemanticWorldViewInverseTransposeMatrix
    kSemanticWorldViewProjectionMatrix
    kSemanticWorldViewProjectionInverseMatrix
    kSemanticWorldViewProjectionInverseTransposeMatrix
    kSemanticColorTexture
    kSemanticNormalTexture
    kSemanticBumpTexture
    kSemanticNormalizationTexture
    kSemanticTranspDepthTexture
    kSemanticOpaqueDepthTexture
    kSemanticTime
    kSemanticWorldTransposeMatrix
    kSemanticViewTransposeMatrix
    kSemanticProjectionTransposeMatrix
    kSemanticWorldViewTransposeMatrix
    kSemanticWorldViewProjectionTransposeMatrix
    kSemanticViewProjectionMatrix
    kSemanticViewProjectionInverseMatrix
    kSemanticViewProjectionTransposeMatrix
    kSemanticViewProjectionInverseTransposeMatrix
    kSemanticLocalViewer
    kSemanticViewportPixelSize
    kSemanticBackgroundColor
    kSemanticFrameNumber
    kSemanticNearClipPlane
    kSemanticFarClipPlane
    kSemanticHWSPrimitiveBase
    kSemanticHWSPrimitiveCountPerInstance
    kSemanticHWSObjectLevel
    kSemanticHWSFaceLevel
    kSemanticHWSEdgeLevel
    kSemanticHWSVertexLevel
    kSemanticHWSOccluder
    kSemanticHWSFrontCCW
    kSemanticHWSInstancedDraw
    kSemanticHWSHighlighting
    '''

    def __init__(self):
        pass

    def kSemanticUnknown(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 0
        '''
        pass

    def kSemanticObjectDir(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 1
        '''
        pass

    def kSemanticWorldDir(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 2
        '''
        pass

    def kSemanticViewDir(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 3
        '''
        pass

    def kSemanticProjectionDir(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 4
        '''
        pass

    def kSemanticObjectPos(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 5
        '''
        pass

    def kSemanticWorldPos(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 6
        '''
        pass

    def kSemanticViewPos(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 7
        '''
        pass

    def kSemanticProjectionPos(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 8
        '''
        pass

    def kSemanticColor(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 9
        '''
        pass

    def kSemanticNormal(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 10
        '''
        pass

    def kSemanticBump(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 11
        '''
        pass

    def kSemanticEnvironment(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 12
        '''
        pass

    def kSemanticWorldMatrix(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 13
        '''
        pass

    def kSemanticWorldInverseMatrix(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 14
        '''
        pass

    def kSemanticWorldInverseTransposeMatrix(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 15
        '''
        pass

    def kSemanticViewMatrix(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 16
        '''
        pass

    def kSemanticViewInverseMatrix(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 17
        '''
        pass

    def kSemanticViewInverseTransposeMatrix(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 18
        '''
        pass

    def kSemanticProjectionMatrix(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 19
        '''
        pass

    def kSemanticProjectionInverseMatrix(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 20
        '''
        pass

    def kSemanticProjectionInverseTransposeMatrix(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 21
        '''
        pass

    def kSemanticWorldViewMatrix(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 22
        '''
        pass

    def kSemanticWorldViewInverseMatrix(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 23
        '''
        pass

    def kSemanticWorldViewInverseTransposeMatrix(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 24
        '''
        pass

    def kSemanticWorldViewProjectionMatrix(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 25
        '''
        pass

    def kSemanticWorldViewProjectionInverseMatrix(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 26
        '''
        pass

    def kSemanticWorldViewProjectionInverseTransposeMatrix(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 27
        '''
        pass

    def kSemanticColorTexture(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 28
        '''
        pass

    def kSemanticNormalTexture(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 29
        '''
        pass

    def kSemanticBumpTexture(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 30
        '''
        pass

    def kSemanticNormalizationTexture(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 31
        '''
        pass

    def kSemanticTranspDepthTexture(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 32
        '''
        pass

    def kSemanticOpaqueDepthTexture(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 33
        '''
        pass

    def kSemanticTime(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 34
        '''
        pass

    def kSemanticWorldTransposeMatrix(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 35
        '''
        pass

    def kSemanticViewTransposeMatrix(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 36
        '''
        pass

    def kSemanticProjectionTransposeMatrix(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 37
        '''
        pass

    def kSemanticWorldViewTransposeMatrix(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 38
        '''
        pass

    def kSemanticWorldViewProjectionTransposeMatrix(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 39
        '''
        pass

    def kSemanticViewProjectionMatrix(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 40
        '''
        pass

    def kSemanticViewProjectionInverseMatrix(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 41
        '''
        pass

    def kSemanticViewProjectionTransposeMatrix(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 42
        '''
        pass

    def kSemanticViewProjectionInverseTransposeMatrix(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 43
        '''
        pass

    def kSemanticLocalViewer(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 44
        '''
        pass

    def kSemanticViewportPixelSize(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 45
        '''
        pass

    def kSemanticBackgroundColor(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 46
        '''
        pass

    def kSemanticFrameNumber(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 47
        '''
        pass

    def kSemanticNearClipPlane(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 48
        '''
        pass

    def kSemanticFarClipPlane(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 49
        '''
        pass

    def kSemanticHWSPrimitiveBase(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 50
        '''
        pass

    def kSemanticHWSPrimitiveCountPerInstance(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 51
        '''
        pass

    def kSemanticHWSObjectLevel(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 52
        '''
        pass

    def kSemanticHWSFaceLevel(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 53
        '''
        pass

    def kSemanticHWSEdgeLevel(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 54
        '''
        pass

    def kSemanticHWSVertexLevel(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 55
        '''
        pass

    def kSemanticHWSOccluder(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 56
        '''
        pass

    def kSemanticHWSFrontCCW(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 57
        '''
        pass

    def kSemanticHWSInstancedDraw(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 58
        '''
        pass

    def kSemanticHWSHighlighting(self):
        '''This is an enum of DataSemantic.
        - Description:  
        - Value: 59
        '''
        pass

class MUniformParameterList:
    '''Uniform Parameter.
MUniformParameterArray specify the list of uniform shader
parameters used by a hardware shader, allowing Maya to handle
setting up the node and user interfaces to the data, the
population and access of cached data, etc.
'''
    def __init__(self):
        pass


    def append(self, element: MUniformParameter): 
        '''
        append(self, element: MUniformParameter)

        Synopsis
        -----
        Append a new parameter to this end of this list.

        Returns:
        -----
        None

        Parameters:
        -----
        element: MUniformParameter
        	[in] -> The new parameter to append 


        '''
        pass

    def length(self): 
        '''
        length(self) -> int

        Synopsis
        -----
        Get the number of parameters in this list.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setLength(self, n: int): 
        '''
        setLength(self, n: int)

        Synopsis
        -----
        Set the number of parameters in this list. If this is greater
        than the current number of parameters in the list, the caller is
        responsible for setting the new parameters to valid values using
        setElement.

        Returns:
        -----
        None

        Parameters:
        -----
        n: int
        	[in] -> The number of parameters in this list. 


        '''
        pass

    def getElement(self, n: int): 
        '''
        getElement(self, n: int) -> MUniformParameter

        Synopsis
        -----
        Get the nth parameter in this list.

        Returns: 
        ----- 
        The nth parameter in the list

        Parameters:
        -----
        n: int
        	[in] -> the index of the element to return


        '''
        pass

    def setElement(self, n: int,
                        p: MUniformParameter): 
        '''
        setElement(self, n: int,
                        p: MUniformParameter)

        Synopsis
        -----
        Get the nth parameter in this list.

        Returns:
        -----
        None

        Parameters:
        -----
        n: int
        	[in] -> the index of the element to return 

        p: MUniformParameter
        	[out] -> the requested parameter


        '''
        pass

class MUserData:
    '''Virtual base class for user data caching.
MUserData is a virtual base class meant to provide a means for users to
attach blind data to certain Maya object types such that the
lifetime of the blind data is managed by Maya.
'''
    def __init__(self):
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

class MVaryingParameter:
    '''Geometric data cache.
The
MVaryingParameter class provides a high-level interface to hardware shader varying
parameters. By defining your shader's varying data through this
class, you allow Maya to handle the attributes, editing,
serialisation, requirements setup, and cache management for you
in a standard way that ensure you'll be able to leverage future
performance and functionlity improvements.
At setup time (either initial load or when the effect/technique
is changed), your shader simply creates the list of parameters it
requires, specifying the name, type, semantic of the parameters.
At render time, you can then use the parameters to directly
access the appropriate buffers for that surface data.
If you include a custom Attribute Editor template for your shader
node, you can include these surface parameters by calling the
AEhwShaderTemplateParameters script function. The following
sample code provides a basic template you can modify - however
your AE template can use as much or as little of this as you
like:
'''
    def __init__(self):
        pass


    def name(self): 
        '''
        name(self) -> const MString

        Synopsis
        -----
        Get the name of this parameter.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def type(self): 
        '''
        type(self) -> MVaryingParameter.MVaryingParameter

        Synopsis
        -----
        Get the type of this parameter.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def semantic(self): 
        '''
        semantic(self) -> MVaryingParameter.MVaryingParameter

        Synopsis
        -----
        Get the semantic of this parameter.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def semanticName(self): 
        '''
        semanticName(self) -> const MString

        Synopsis
        -----
        Get the semantic name assigned to this parameter The semanticName
        is used to identify a custom vertex stream request in order to
        fill the stream with the appropriate data requested by a shader
        override.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def destinationSet(self): 
        '''
        destinationSet(self) -> MString

        Synopsis
        -----
        Get the destination Set of this parameter.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def dimension(self): 
        '''
        dimension(self) -> int

        Synopsis
        -----
        Get the dimension of this parameter.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getBuffer(self, geometry: MGeometryLegacy,
                        data: void,
                        elements: int,
                        count: int): 
        '''
        getBuffer(self, geometry: MGeometryLegacy,
                        data: void,
                        elements: int,
                        count: int)

        Synopsis
        -----
        Get the data for this parameter as a system memory buffer.

        Returns:
        -----
        None

        Parameters:
        -----
        geometry: MGeometryLegacy
        	[in] -> the geometry cache the data should be retrieved from. This corresponds to the shape (e.g. mesh) you want the data for. 

        data: void
        	[out] -> returns a pointer to the data (or NULL if the parameter is not available). 

        elements: int
        	[out] -> the number of elements specified for this parameter (e.g. is it 3 floats or 4 floats?) 

        count: int
        	[out] -> the number of values returned for this parameter (e.g. there are 426 normals)


        '''
        pass

    def getSourceType(self): 
        '''
        getSourceType(self) -> MVaryingParameter.MVaryingParameter

        Synopsis
        -----
        Get the type of data (e.g. position, normal, uv) currently
        populating this parameter. This method will only return a useful
        value when called on leaf-level parameters (e.g. structures do
        not have sources, only the elements of a structure have sources).

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getSourceSetName(self): 
        '''
        getSourceSetName(self) -> MString

        Synopsis
        -----
        If the current data type supports data sets (e.g. uv sets, color
        sets), get the name of the data set populating this parameter.
        This method will only return a useful value when called on leaf-
        level parameters (e.g. structures do not have sources, only the
        elements of a structure have sources).

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setSource(self, type: MVaryingParameter.MVaryingParameter,
                        setName: MString): 
        '''
        setSource(self, type: MVaryingParameter.MVaryingParameter,
                        setName: MString)

        Synopsis
        -----
        While the source of geometry parameters is usually configured by
        the artist through Maya's user interface, this method allows you
        to programatically set the source of a geometry parameter,
        including both the data type (e.g. position, normal, etc) and an
        optional set name (e.g. UV set "map1"). This is useful for
        implementing custom default values or shader operations.

        Returns:
        -----
        None

        Parameters:
        -----
        type: MVaryingParameter.MVaryingParameter
        	[in] -> the type of data to populate this parameter with 

        setName: MString
        	[in] -> the specific data set to use for parameter types which support data sets, such as UV and color.


        '''
        pass

    def getElementSize(self): 
        '''
        getElementSize(self) -> int

        Synopsis
        -----
        Get the size in bytes of one element of this parameter.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getMaximumStride(self): 
        '''
        getMaximumStride(self) -> int

        Synopsis
        -----
        Get the maximum stride of this parameter in bytes. For parameter
        that accept a range of element counts, this corresponds to the
        maximum number of elements the parameter supports.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def addElement(self, child: MVaryingParameter): 
        '''
        addElement(self, child: MVaryingParameter)

        Synopsis
        -----
        Add a child element to this parameter. This operation is only
        valid for parameters of type kStructure.

        Returns:
        -----
        None

        Parameters:
        -----
        child: MVaryingParameter
        	[in] -> the parameter to add to the structure.


        '''
        pass

    def numElements(self): 
        '''
        numElements(self) -> int

        Synopsis
        -----
        Get the number of elements in this structure. This operation is
        only valid for parameters of type kStructure.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getElement(self, i: int): 
        '''
        getElement(self, i: int) -> MVaryingParameter

        Synopsis
        -----
        Get an element within a structure. This operation is only valid
        for parameters of type kStructure.

        Returns: 
        ----- 
        The structure element. This will be a NULL element if an invalid
        index was specified.

        Parameters:
        -----
        i: int
        	[in] -> The index of the structure element to return.


        '''
        pass

    def removeElements(self): 
        '''
        removeElements(self)

        Synopsis
        -----
        Remove all child elements from a structure. This operation is
        only valid for parameters of type kStructure.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getUpdateId(self): 
        '''
        getUpdateId(self) -> int

        Synopsis
        -----
        Get the update id. The update id is increased every time the
        parameter sources or sourceSet are changed. A plugin can compare
        the update id value between subsequent calls to this function to
        know if the source has changed since the last call.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MVaryingParameterType:
    '''Parameter types. 
    Non-functional class.  Values for this enum:
    kInvalidParameter
    kStructure
    kFloat
    kDouble
    kChar
    kUnsignedChar
    kInt16
    kUnsignedInt16
    kInt32
    kUnsignedInt32
    '''

    def __init__(self):
        pass

    def kInvalidParameter(self):
        '''This is an enum of MVaryingParameterType.
        - Description:  
        - Value: -1
        '''
        pass

    def kStructure(self):
        '''This is an enum of MVaryingParameterType.
        - Description:  
        - Value: 0
        '''
        pass

    def kFloat(self):
        '''This is an enum of MVaryingParameterType.
        - Description:  
        - Value: 1
        '''
        pass

    def kDouble(self):
        '''This is an enum of MVaryingParameterType.
        - Description:  
        - Value: 2
        '''
        pass

    def kChar(self):
        '''This is an enum of MVaryingParameterType.
        - Description:  
        - Value: 3
        '''
        pass

    def kUnsignedChar(self):
        '''This is an enum of MVaryingParameterType.
        - Description:  
        - Value: 4
        '''
        pass

    def kInt16(self):
        '''This is an enum of MVaryingParameterType.
        - Description:  
        - Value: 5
        '''
        pass

    def kUnsignedInt16(self):
        '''This is an enum of MVaryingParameterType.
        - Description:  
        - Value: 6
        '''
        pass

    def kInt32(self):
        '''This is an enum of MVaryingParameterType.
        - Description:  
        - Value: 7
        '''
        pass

    def kUnsignedInt32(self):
        '''This is an enum of MVaryingParameterType.
        - Description:  
        - Value: 8
        '''
        pass

class MVaryingParameterSemantic:
    '''Parameter semantics (i.e. what the parameter represents). 
    Non-functional class.  Values for this enum:
    kNoSemantic
    kPosition
    kNormal
    kTexCoord
    kColor
    kWeight
    kTangent
    kBinormal
    '''

    def __init__(self):
        pass

    def kNoSemantic(self):
        '''This is an enum of MVaryingParameterSemantic.
        - Description:  
        - Value: 0
        '''
        pass

    def kPosition(self):
        '''This is an enum of MVaryingParameterSemantic.
        - Description:  
        - Value: 1
        '''
        pass

    def kNormal(self):
        '''This is an enum of MVaryingParameterSemantic.
        - Description:  
        - Value: 2
        '''
        pass

    def kTexCoord(self):
        '''This is an enum of MVaryingParameterSemantic.
        - Description:  
        - Value: 3
        '''
        pass

    def kColor(self):
        '''This is an enum of MVaryingParameterSemantic.
        - Description:  
        - Value: 4
        '''
        pass

    def kWeight(self):
        '''This is an enum of MVaryingParameterSemantic.
        - Description:  
        - Value: 5
        '''
        pass

    def kTangent(self):
        '''This is an enum of MVaryingParameterSemantic.
        - Description:  
        - Value: 7
        '''
        pass

    def kBinormal(self):
        '''This is an enum of MVaryingParameterSemantic.
        - Description:  
        - Value: 8
        '''
        pass

class MVaryingParameterList:
    '''Geometric data cache.
MVaryingParameterList specify the surface component level data used by a hardware
shader, allowing Maya to handle setting up the node and user
interfaces to the data, the population and access of cached data,
etc.
'''
    def __init__(self):
        pass


    def append(self, element: MVaryingParameter): 
        '''
        append(self, element: MVaryingParameter)

        Synopsis
        -----
        Append a new parameter to this end of this list.

        Returns:
        -----
        None

        Parameters:
        -----
        element: MVaryingParameter
        	[in] -> The new parameter to append 


        '''
        pass

    def length(self): 
        '''
        length(self) -> int

        Synopsis
        -----
        Get the number of parameters in this list.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setLength(self, n: int): 
        '''
        setLength(self, n: int)

        Synopsis
        -----
        Set the number of parameters in this list. If this is greater
        than the current number of parameters in the list, the caller is
        responsible for setting the new parameters to valid values using
        setElement.

        Returns:
        -----
        None

        Parameters:
        -----
        n: int
        	[in] -> The number of parameters in this list. 


        '''
        pass

    def getElement(self, n: int): 
        '''
        getElement(self, n: int) -> MVaryingParameter

        Synopsis
        -----
        Get the nth parameter in this list.

        Returns: 
        ----- 
        The nth parameter in the list

        Parameters:
        -----
        n: int
        	[in] -> The index of the element to return


        '''
        pass

    def setElement(self, n: int,
                        p: MVaryingParameter): 
        '''
        setElement(self, n: int,
                        p: MVaryingParameter)

        Synopsis
        -----
        Set the nth parameter in this list.

        Returns:
        -----
        None

        Parameters:
        -----
        n: int
        	[in] -> The index of the element to set 

        p: MVaryingParameter
        	[in] -> The value to set


        '''
        pass

class MViewportRenderer:
    '''MViewportRenderer is a class which represents a hardware viewport renderer.
'''
    def __init__(self):
        pass


    def initialize(self): 
        '''
        initialize(self)

        Synopsis
        -----
        Renderer initialization. This method gets called to allow the
        renderer to perform a one time initialization.The corresponding
        method for cleanup is uninitialize().Initialization is called if
        and only if the renderer has been registered. See register()
        method.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def uninitialize(self): 
        '''
        uninitialize(self)

        Synopsis
        -----
        Renderer cleanup. This method gets called to allow the renderer
        to perform a one time de-initialization.The corresponding method
        for cleanup is initialize().

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def render(self, info: MRenderingInfo): 
        '''
        render(self, info: MRenderingInfo)

        Synopsis
        -----
        Method which does the actual rendering. This method gets called
        to allow the renderer to perform rendering.It will be called
        whenever the viewport to which it is registered, requires a
        refresh.

        Returns:
        -----
        None

        Parameters:
        -----
        info: MRenderingInfo
        	[in] -> 


        '''
        pass

    def nativelySupports(self, api: MViewportRenderer.MViewportRenderer,
                        version: float): 
        '''
        nativelySupports(self, api: MViewportRenderer.MViewportRenderer,
                        version: float) -> bool

        Synopsis
        -----
        Query the native rendering API's supported by this renderer.
        Query the renderer to see if the renderer can natively support a
        specific API and API version number.This is to provide
        compatibility checks between the drawing API used for the render
        target of this renderer, and the renderer itself.As an example
        the render target may be using OpenGL natively while the renderer
        associated with the render target is using Direct3D. In this case
        the method should return false.As an example the render target
        may be using Direct3D version K natively while the renderer
        associated with the render target is using Direct3D version L. In
        this case the method may return false.

        Returns: 
        ----- 
        MViewportRenderer::RenderingAPI : rendering API.

        Parameters:
        -----
        api: MViewportRenderer.MViewportRenderer
        	[in] -> rendering API natively used by the render target 

        version: float
        	[in] -> rendering API version of the API natively used by the render target


        '''
        pass

    def override(self, override: MViewportRenderer.MViewportRenderer): 
        '''
        override(self, override: MViewportRenderer.MViewportRenderer) -> bool

        Synopsis
        -----
        Check if override exists. This method gets called to query the
        renderer to see if it has a given type of render target override.

        Returns: 
        ----- 
        true if the renderer overrides the render target override.

        Parameters:
        -----
        override: MViewportRenderer.MViewportRenderer
        	[in] -> render target override


        '''
        pass

    def overrideThenStandardExclusion(self): 
        '''
        overrideThenStandardExclusion(self) -> int

        Synopsis
        -----
        Rendering exclusion for standard pass of kOverrideThenStandard.
        This method gets called to query the renderer to see what should
        be excluded from the standard pass when the RenderingOverride
        mode is kOverrideThenStandard.If this method is not redefined by
        the derived class, it returns kExcludeAll.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def registerRenderer(self): 
        '''
        registerRenderer(self)

        Synopsis
        -----
        Register the renderer. Registration should occur when the plugin
        is initialized. A renderer will be available for usage from 3d
        modeling viewports if and only if it has been
        registered.Additionally, the initialization method initialize()
        will be made only if a renderer has been registered.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def deregisterRenderer(self): 
        '''
        deregisterRenderer(self)

        Synopsis
        -----
        Deregister the renderer. Deregistration should occur when the
        plugin is unloaded.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def name(self): 
        '''
        name(self) -> const MString&

        Synopsis
        -----
        Return the internal name of the renderer.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def UIname(self): 
        '''
        UIname(self) -> const MString&

        Synopsis
        -----
        Return the name of the renderer as it should appear to users.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setUIName(self, name: MString): 
        '''
        setUIName(self, name: MString)

        Synopsis
        -----
        Set the name of the renderer as it should appear to users.

        Returns:
        -----
        None

        Parameters:
        -----
        name: MString
        	[in] -> name to set 


        '''
        pass

    def renderingOverride(self): 
        '''
        renderingOverride(self) -> MViewportRenderer.MViewportRenderer

        Synopsis
        -----
        Return the override status.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setRenderingOverride(self, override: MViewportRenderer.RenderingOverride): 
        '''
        setRenderingOverride(self, override: MViewportRenderer.RenderingOverride)

        Synopsis
        -----
        Set the rendering override for the renderer.

        Returns:
        -----
        None

        Parameters:
        -----
        override: MViewportRenderer.RenderingOverride
        	[in] -> override value to set 


        '''
        pass

class RenderingAPI:
    '''API used for rendering. 
    Non-functional class.  Values for this enum:
    kOpenGL
    kDirect3D
    kSoftware
    '''

    def __init__(self):
        pass

    def kOpenGL(self):
        '''This is an enum of RenderingAPI.
        - Description: Renderer uses hardware OpenGL for rendering. 
        - Value: 0
        '''
        pass

    def kDirect3D(self):
        '''This is an enum of RenderingAPI.
        - Description: Renderer uses hardware Direct3D for rendering. 
        - Value: 1
        '''
        pass

    def kSoftware(self):
        '''This is an enum of RenderingAPI.
        - Description: Renderer renders using software. 
        - Value: 2
        '''
        pass

class RenderingOverride:
    '''Override status. 
    Non-functional class.  Values for this enum:
    kNoOverride
    kOverrideAllDrawing
    kOverrideThenStandard
    kOverrideThenUI
    '''

    def __init__(self):
        pass

    def kNoOverride(self):
        '''This is an enum of RenderingOverride.
        - Description: Override nothing. 
        - Value: 0
        '''
        pass

    def kOverrideAllDrawing(self):
        '''This is an enum of RenderingOverride.
        - Description: Override all drawing. 
        - Value: 1
        '''
        pass

    def kOverrideThenStandard(self):
        '''This is an enum of RenderingOverride.
        - Description: Override all drawing, then follow with a standard render pass. 
        - Value: 2
        '''
        pass

    def kOverrideThenUI(self):
        '''This is an enum of RenderingOverride.
        - Description: Override draw, then follow with a UI only render pass. 
        - Value: 3
        '''
        pass

