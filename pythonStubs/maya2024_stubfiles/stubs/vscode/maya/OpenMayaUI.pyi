
'''
Stub class file for:
OpenMayaUI

Maya2024 Python API stub file
Vscode Version
Generated from original Maya documentation.
Autodesk Maya2024  c1997-2023 Autodesk, Inc. All rights reserved. 
'''


from typing import overload




class M3dView:
    '''A 3-D view.
M3dView provides methods for working with 3D model views. 3D views are
based on OpenGL drawing areas.
Maya can operate in two different color modes, RGBA and color
index. Color index mode is used to increase performance when
shading is not required. Drawing in color index mode is more
complicated, but this class provides methods to simplify color
selection.
Maya has four color tables that can be used in RGBA, and that
must be used in color index mode. These four color tables
represent four sets of bit planes that are independent of each
other. So, for example, it is possible to clear all active
objects from the display and redraw them without redrawing the
dormant and templated objects. The active and dormant color
tables contain the same colors, but use different bitplanes.
The extra performance of color index mode comes at the cost of a
limited number of colors. If this restriction causes difficulty,
then it is possible for the user to force all displays into RGBA
mode where any color may be used.
When an object is affected by another in the scene, it is drawn
in a magenta colour by default. This is denoted in the
DisplayStatus enum by kActiveAffected. These objects are drawn in
the active planes even though they are dormant for performance
reasons.
'''
    def __init__(self):
        pass


    def active3dView(self, ReturnStatus: M3dView.MStatus): 
        '''
        active3dView(self, ReturnStatus: M3dView.MStatus) -> M3dView

        Synopsis
        -----
        Returns the active view in the form of a class (M3dView) that can
        operate on it.

        Returns: 
        ----- 
        Active view class.

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> 


        '''
        pass

    def numberOf3dViews(self): 
        '''
        numberOf3dViews(self) -> int

        Synopsis
        -----
        Returns the number of 3D views currently in existance.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def get3dView(self, index: int,
                        view: M3dView): 
        '''
        get3dView(self, index: int,
                        view: M3dView)

        Synopsis
        -----
        Returns the 3D view at the given index.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> index of the view to get 

        view: M3dView
        	[out] -> storage for the returned view


        '''
        pass

    def displayStatus(self, path: MDagPath,
                        ReturnStatus: M3dView.MStatus): 
        '''
        displayStatus(self, path: MDagPath,
                        ReturnStatus: M3dView.MStatus) -> M3dView.M3dView

        Synopsis
        -----
        Returns the display status of the given DAG path.

        Returns: 
        ----- 
        Display status for the DAG

        Parameters:
        -----
        path: MDagPath
        	[in] -> the DAG path to get. 

        ReturnStatus: M3dView.MStatus
        	[out] -> Status code.


        '''
        pass

    def makeSharedContextCurrent(self): 
        '''
        makeSharedContextCurrent(self)

        Synopsis
        -----
        makes the shared context current. If in DirectX mode it does
        nothing.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def display(self, ReturnStatus: M3dView.MStatus): 
        '''
        display(self, ReturnStatus: M3dView.MStatus) -> M3dView.MGLContext

        Synopsis
        -----
        Mac OS X and Windows. Returns the OpenGL context for this view.

        Returns: 
        ----- 
        The OpenGL context. On 32-bit OS X this is an AGLContext. On
        64-bit OS X this is an NSOpenGLContext pointer. On Windows this
        is an HGLRC.

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status Code


        '''
        pass

    def applicationShell(self, ReturnStatus: M3dView.MStatus): 
        '''
        applicationShell(self, ReturnStatus: M3dView.MStatus) -> M3dView.MNativeWindowHdl

        Synopsis
        -----
        Returns the native handle for Maya's main window. This is
        equivalent to MQtUtil::nativeWindow(MQtUtil::mainWindow()).

        Returns: 
        ----- 
        The window handle.

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status Code


        '''
        pass

    def getScreenPosition(self, x: int,
                        y: int,
                        ReturnStatus: M3dView.MStatus): 
        '''
        getScreenPosition(self, x: int,
                        y: int,
                        ReturnStatus: M3dView.MStatus)

        Synopsis
        -----
        Returns the current position of this view window in screen
        coordinates. This is useful for finding out the exact location of
        the window as it appears on the screen. These values are in UI
        coordinate space so the y value increases from bottom to top.

        Returns:
        -----
        None

        Parameters:
        -----
        x: int
        	[out] -> - x coordinate of the upper-left corner of the view 

        y: int
        	[out] -> - y coordinate of the upper-left corner of the view 

        ReturnStatus: M3dView.MStatus
        	[out] -> Status Code


        '''
        pass

    def widget(self, ReturnStatus: M3dView.MStatus): 
        '''
        widget(self, ReturnStatus: M3dView.MStatus) -> M3dView.QWidget*

        Synopsis
        -----
        Returns the view's Qt widget.

        Returns: 
        ----- 
        A QWidget pointer to the Qt widget containing the view's drawing
        region, or NULL if the view's drawing region has not yet been
        created.

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status Code


        '''
        pass

    def window(self, ReturnStatus: M3dView.MStatus): 
        '''
        window(self, ReturnStatus: M3dView.MStatus) -> M3dView.MNativeWindowHdl

        Synopsis
        -----
        Returns the native window for this view. This is equivalent to
        MQtUtil::nativeWindow(view.widget()).

        Returns: 
        ----- 
        The X window

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status Code


        '''
        pass

    def portWidth(self, ReturnStatus: M3dView.MStatus): 
        '''
        portWidth(self, ReturnStatus: M3dView.MStatus) -> int

        Synopsis
        -----
        Returns the width of the current viewport.

        Returns: 
        ----- 
        The width of this viewport

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status Code


        '''
        pass

    def portHeight(self, ReturnStatus: M3dView.MStatus): 
        '''
        portHeight(self, ReturnStatus: M3dView.MStatus) -> int

        Synopsis
        -----
        Returns the height of the current viewport.

        Returns: 
        ----- 
        The height of this viewport

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status Code


        '''
        pass

    def devicePixelRatio(self, ReturnStatus: M3dView.MStatus): 
        '''
        devicePixelRatio(self, ReturnStatus: M3dView.MStatus) -> double

        Synopsis
        -----
        Introduced in 2023.0 Returns the ratio between Qt logical pixel
        and viewport rendering pixel.This scale factor can be use to
        convert between Qt coordinate (pointer positions) and viewport
        coordinate (for intersection detection).

        Returns: 
        ----- 
        1.0 on Windows, Linux, Mac with normal-dpi display, or
        environment variable
        QT_MAC_WANTS_BEST_RESOLUTION_OPENGL_SURFACE=0 was set  2.0 or
        more on Mac with hi-dpi (retina) display

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status Code


        '''
        pass

    def isVisible(self, ReturnStatus: M3dView.MStatus): 
        '''
        isVisible(self, ReturnStatus: M3dView.MStatus) -> bool

        Synopsis
        -----
        Returns true if this viewport is visible.

        Returns: 
        ----- 
        True if this viewport is visible

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status Code


        '''
        pass

    def playblastPortWidth(self, ReturnStatus: M3dView.MStatus): 
        '''
        playblastPortWidth(self, ReturnStatus: M3dView.MStatus) -> int

        Synopsis
        -----
        Returns the port width of current playblast. Valid only when
        playblast command has been called. Otherwise, an invalid value 0
        is returned.

        Returns: 
        ----- 
        The port width of current playblast.

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status Code


        '''
        pass

    def playblastPortHeight(self, ReturnStatus: M3dView.MStatus): 
        '''
        playblastPortHeight(self, ReturnStatus: M3dView.MStatus) -> int

        Synopsis
        -----
        Returns the port height of current playblast. Valid only when
        playblast command has been called. Otherwise, an invalid value 0
        is returned.

        Returns: 
        ----- 
        The height of current playblast.

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status Code


        '''
        pass

    def pushViewport(self, x: int,
                        y: int,
                        width: int,
                        height: int): 
        '''
        pushViewport(self, x: int,
                        y: int,
                        width: int,
                        height: int)

        Synopsis
        -----
        Set the current viewport dimensions. Will keep track of the last
        viewport dimensions on a stack. When finished with this viewport,
        the current dimensions should be removed from the top of stack
        using M3dView::popViewport().

        Returns:
        -----
        None

        Parameters:
        -----
        x: int
        	[in] -> Lower left corner of viewport (x coordinate). 

        y: int
        	[in] -> Lower left corner of viewport (y coordinate). 

        width: int
        	[in] -> Width of the viewport. 

        height: int
        	[in] -> Height of the viewport.


        '''
        pass

    def popViewport(self): 
        '''
        popViewport(self)

        Synopsis
        -----
        Pop the current viewport off of the viewport stack.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def viewport(self, x: int,
                        y: int,
                        width: int,
                        height: int): 
        '''
        viewport(self, x: int,
                        y: int,
                        width: int,
                        height: int)

        Synopsis
        -----
        Get the current viewport dimensions.

        Returns:
        -----
        None

        Parameters:
        -----
        x: int
        	[out] -> Lower left corner of viewport (x coordinate). 

        y: int
        	[out] -> Lower left corner of viewport (y coordinate). 

        width: int
        	[out] -> Width of the viewport. 

        height: int
        	[out] -> Height of the viewport.


        '''
        pass

    def beginSelect(self, buffer: M3dView.GLuint,
                        size: M3dView.GLsizei): 
        '''
        beginSelect(self, buffer: M3dView.GLuint,
                        size: M3dView.GLsizei)

        Synopsis
        -----
        Start selecting. The buffer passed is used to record selection
        hits. A selection hit consists of the following 4 items:

        Returns:
        -----
        None

        Parameters:
        -----
        buffer: M3dView.GLuint
        	[in] -> OpenGl pick buffer 

        size: M3dView.GLsizei
        	[in] -> Buffer size (number of GLint) 


        '''
        pass

    def endSelect(self): 
        '''
        endSelect(self) -> M3dView.GLint

        Synopsis
        -----
        Finish a selection sequence. Result is stored in the buffer
        passed in the beginSelect call.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def selectMode(self): 
        '''
        selectMode(self) -> bool

        Synopsis
        -----
        Tells if this M3dView is in selection mode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def textureMode(self): 
        '''
        textureMode(self) -> bool

        Synopsis
        -----
        Tells if this M3dView is in texture mode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def loadName(self, name: M3dView.GLuint): 
        '''
        loadName(self, name: M3dView.GLuint)

        Synopsis
        -----
        Replace the top of the name stack with the given name. Valid only
        when beginSelect() has been called.

        Returns:
        -----
        None

        Parameters:
        -----
        name: M3dView.GLuint
        	[in] -> Name to be loaded onto the top of the stack. 


        '''
        pass

    def pushName(self, name: M3dView.GLuint): 
        '''
        pushName(self, name: M3dView.GLuint)

        Synopsis
        -----
        Push a new name on the name stack. Valid only when beginSelect()
        has been called.

        Returns:
        -----
        None

        Parameters:
        -----
        name: M3dView.GLuint
        	[in] -> Name to be loaded onto the top of the stack. 


        '''
        pass

    def popName(self): 
        '''
        popName(self)

        Synopsis
        -----
        Removes the top of the name stack. Valid only when beginSelect()
        has been called.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def initNames(self): 
        '''
        initNames(self)

        Synopsis
        -----
        Reset the name stack. Valid only when beginSelect() has been
        called.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def beginXorDrawing(self, drawOrthographic: bool,
                        disableDepthTesting: bool,
                        lineWidth: float,
                        stipplePattern: M3dView.LineStipplePattern,
                        lineColor: MColor): 
        '''
        beginXorDrawing(self, drawOrthographic: bool,
                        disableDepthTesting: bool,
                        lineWidth: float,
                        stipplePattern: M3dView.LineStipplePattern,
                        lineColor: MColor)

        Synopsis
        -----
        Setup the context for exclusive-or (XOR) drawing. In XOR drawing
        the color values of the pixels being drawn is exclusive-ored with
        the color values already present in the view. The advantage of
        this is that exclusive-oring the same pixels with the same color
        values a second time will restore the pixels to their original
        colors, making it possible to temporarily display and erase lines
        without having to redraw the entire view. This makes XOR drawing
        particularly useful for drawing guidelines for tools.One
        disadvantage of XOR drawing is that the final color after the
        exclusive-or will not match your drawing color, except when the
        original color of the pixel was black. For example, XORing a
        white line across a red background will result in a cyan line and
        XORing it across a changing background will result in a line of
        changing colors. However in most situations where you would use
        XOR drawing the color of the lines is irrelevant just so long as
        they are visible.It is an error to call beginXorDrawing() again
        before calling endXorDrawing() first.

        Returns:
        -----
        None

        Parameters:
        -----
        drawOrthographic: bool
        	[in] -> Draw using orthographic projection. Default is true. 

        disableDepthTesting: bool
        	[in] -> Disable depth testing during draw. Default is true. 

        lineWidth: float
        	[in] -> Set up line width. Default is 1. 

        stipplePattern: M3dView.LineStipplePattern
        	[in] -> Line stipple pattern. Default is kStippleNone. 

        lineColor: MColor
        	[in] -> Line color. Default is white (1,1,1).


        '''
        pass

    def endXorDrawing(self): 
        '''
        endXorDrawing(self)

        Synopsis
        -----
        Reset the context to non-exclusive-or (non-XOR) screen drawing.
        If endXorDrawing() is called without first calling
        beginXorDrawing() an error will result.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def numDormantColors(self, ReturnStatus: M3dView.MStatus): 
        '''
        numDormantColors(self, ReturnStatus: M3dView.MStatus) -> int

        Synopsis
        -----
        Returns the number of dormant object colors in the internal
        application color table.

        Returns: 
        ----- 
        The number of dormant colors

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status code


        '''
        pass

    def numActiveColors(self, ReturnStatus: M3dView.MStatus): 
        '''
        numActiveColors(self, ReturnStatus: M3dView.MStatus) -> int

        Synopsis
        -----
        Returns the number of active object colors in the internal
        application color table.

        Returns: 
        ----- 
        The number of active colors

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status code


        '''
        pass

    def numUserDefinedColors(self, ReturnStatus: M3dView.MStatus): 
        '''
        numUserDefinedColors(self, ReturnStatus: M3dView.MStatus) -> int

        Synopsis
        -----
        Returns the number of user defined colors in the internal
        application color table. These colors may be changed by the user
        and assigned to specific objects. See the methods of MFnDagNode
        for information on assigning user defined colors to individual
        objects.The user defined colors are not a color table of their
        own. They exist in the active and dormant color tables.

        Returns: 
        ----- 
        The number of user defined colors

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status code


        '''
        pass

    def setUserDefinedColor(self, index: int,
                        color: MColor): 
        '''
        setUserDefinedColor(self, index: int,
                        color: MColor)

        Synopsis
        -----
        Sets the user defined color at the given index. Valid indices
        range between zero and the number of user defined colors.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> index into the user defined color 

        color: MColor
        	[in] -> color to set to


        '''
        pass

    def userDefinedColorIndex(self, index: int,
                        ReturnStatus: M3dView.MStatus): 
        '''
        userDefinedColorIndex(self, index: int,
                        ReturnStatus: M3dView.MStatus) -> int

        Synopsis
        -----
        Returns the index for the given user-defined color. Valid values
        for the index argument range between zero and the number of user-
        defined colors minus one.The index returned gives the location of
        the specified color inside the active and dormant color tables
        (the index is the same in both tables).

        Returns: 
        ----- 
        Index of user-defined color into the active and dormant tables

        Parameters:
        -----
        index: int
        	[in] -> Index into user-defined colors 

        ReturnStatus: M3dView.MStatus
        	[out] -> Status code


        '''
        pass

    def colorAtIndex(self, index: int,
                        table: M3dView.ColorTable,
                        ReturnStatus: M3dView.MStatus): 
        '''
        colorAtIndex(self, index: int,
                        table: M3dView.ColorTable,
                        ReturnStatus: M3dView.MStatus) -> MColor

        Synopsis
        -----
        Returns the value of the color at the given index in the
        application's color table.

        Returns: 
        ----- 
        The color

        Parameters:
        -----
        index: int
        	[in] -> Index of the color to retrieve 

        table: M3dView.ColorTable
        	[in] -> Table to index into 

        ReturnStatus: M3dView.MStatus
        	[out] -> Status code


        '''
        pass

    def getColorIndexAndTable(self, glindex: int,
                        index: int,
                        table: M3dView.ColorTable): 
        '''
        getColorIndexAndTable(self, glindex: int,
                        index: int,
                        table: M3dView.ColorTable)

        Synopsis
        -----
        Returns the color table and index representing the given OpenGL
        color-index value. This method is useful when converting color
        indices obtained from glReadPixels(GL_COLOR_INDEX) to Maya color-
        index values suitable for use with the colorAtIndex and
        setDrawColor methods.

        Returns:
        -----
        None

        Parameters:
        -----
        glindex: int
        	[in] -> Value of the OpenGL color-index to retrieve 

        index: int
        	[out] -> Returned ColorTable index 

        table: M3dView.ColorTable
        	[out] -> Returned ColorTable


        '''
        pass

    def isBackgroundGradient(self, ReturnStatus: M3dView.MStatus): 
        '''
        isBackgroundGradient(self, ReturnStatus: M3dView.MStatus) -> bool

        Synopsis
        -----
        Returns whether a gradient is being used as the background color.

        Returns: 
        ----- 
        true background is a color gradient  false background is a solid
        color

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status code


        '''
        pass

    def templateColor(self, ReturnStatus: M3dView.MStatus): 
        '''
        templateColor(self, ReturnStatus: M3dView.MStatus) -> MColor

        Synopsis
        -----
        Returns the value of the template color.

        Returns: 
        ----- 
        The template color

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status code


        '''
        pass

    def backgroundColor(self, ReturnStatus: M3dView.MStatus): 
        '''
        backgroundColor(self, ReturnStatus: M3dView.MStatus) -> MColor

        Synopsis
        -----
        Returns the value of the background color.

        Returns: 
        ----- 
        The background color

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status code


        '''
        pass

    def backgroundColorTop(self, ReturnStatus: M3dView.MStatus): 
        '''
        backgroundColorTop(self, ReturnStatus: M3dView.MStatus) -> MColor

        Synopsis
        -----
        Returns the value of the background gradient top color.

        Returns: 
        ----- 
        The background gradient top color

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status code


        '''
        pass

    def backgroundColorBottom(self, ReturnStatus: M3dView.MStatus): 
        '''
        backgroundColorBottom(self, ReturnStatus: M3dView.MStatus) -> MColor

        Synopsis
        -----
        Returns the value of the background gradient bottom color.

        Returns: 
        ----- 
        The background gradient bottom color

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status code


        '''
        pass

    def liveColor(self, ReturnStatus: M3dView.MStatus): 
        '''
        liveColor(self, ReturnStatus: M3dView.MStatus) -> MColor

        Synopsis
        -----
        Returns the color for live objects.

        Returns: 
        ----- 
        The live color

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status code


        '''
        pass

    def referenceLayerColor(self, ReturnStatus: M3dView.MStatus): 
        '''
        referenceLayerColor(self, ReturnStatus: M3dView.MStatus) -> MColor

        Synopsis
        -----
        Returns the color for objects which belong to a display layer
        whose display type is Reference. This color is also used for
        objects whose display override is set to Reference.

        Returns: 
        ----- 
        The reference layer color

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status code


        '''
        pass

    def activeTemplateColor(self, ReturnStatus: M3dView.MStatus): 
        '''
        activeTemplateColor(self, ReturnStatus: M3dView.MStatus) -> MColor

        Synopsis
        -----
        Returns the color for active template objects.

        Returns: 
        ----- 
        The active template color

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status code


        '''
        pass

    def leadColor(self, ReturnStatus: M3dView.MStatus): 
        '''
        leadColor(self, ReturnStatus: M3dView.MStatus) -> MColor

        Synopsis
        -----
        Returns the color for lead objects.

        Returns: 
        ----- 
        The lead color

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status code


        '''
        pass

    def hiliteColor(self, ReturnStatus: M3dView.MStatus): 
        '''
        hiliteColor(self, ReturnStatus: M3dView.MStatus) -> MColor

        Synopsis
        -----
        Returns the color for hilited objects.

        Returns: 
        ----- 
        The hilite color

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status code


        '''
        pass

    def activeAffectedColor(self, ReturnStatus: M3dView.MStatus): 
        '''
        activeAffectedColor(self, ReturnStatus: M3dView.MStatus) -> MColor

        Synopsis
        -----
        Returns the color for active affected objects.

        Returns: 
        ----- 
        The active affected color

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status code


        '''
        pass

    def getCamera(self, camera: MDagPath): 
        '''
        getCamera(self, camera: MDagPath)

        Synopsis
        -----
        Get the camera for this view.

        Returns:
        -----
        None

        Parameters:
        -----
        camera: MDagPath
        	[out] -> Dag path for the camera (allocated by caller)


        '''
        pass

    def setCamera(self, camera: MDagPath): 
        '''
        setCamera(self, camera: MDagPath)

        Synopsis
        -----
        Set the camera for this view.

        Returns:
        -----
        None

        Parameters:
        -----
        camera: MDagPath
        	[in] -> Dag path of the camera for this view


        '''
        pass

    def scheduleRefreshAllViews(self): 
        '''
        scheduleRefreshAllViews(self)

        Synopsis
        -----
        Schedule a forced refresh for all 3d-views. This method may be
        called safely at any time from any thread. The refresh will occur
        on the main thread when Maya next becomes idle. If a refresh has
        already been scheduled but has not yet occurred then this method
        will do nothing.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def scheduleRefresh(self): 
        '''
        scheduleRefresh(self)

        Synopsis
        -----
        Schedule a forced refresh for this 3d-view. This method may be
        called safely at any time from any thread. The refresh will occur
        on the main thread when Maya next becomes idle. If a refresh has
        already been scheduled for this view but has not yet occurred
        then this method will do nothing.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def refresh(self, all: bool,
                        force: bool): 
        '''
        refresh(self, all: bool,
                        force: bool)

        Synopsis
        -----
        Refresh the this view. If all is set to true then all of the
        3d-view will be refreshed.If force is set to true, then the views
        will be refreshed even if they do not require it. This option
        should be used with extreme care because extra refreshes will
        greatly degrade application performance. In almost all cases it
        is better to use the default behavior where the view is only
        refreshed if it is required.

        Returns:
        -----
        None

        Parameters:
        -----
        all: bool
        	[in] -> If true then refresh all views, otherwise refresh this view. 

        force: bool
        	[in] -> If true then force views to refresh even if they do not require it.


        '''
        pass

    @overload
    def refresh(self, all: bool,
                        force: bool,
                        offscreen: bool): 
        '''
        refresh(self, all: bool,
                        force: bool,
                        offscreen: bool)

        Synopsis
        -----
        Refresh the this view. If all is set to true then all of the
        3d-view will be refreshed.If force is set to true, then the views
        will be refreshed even if they do not require it. This option
        should be used with extreme care because extra refreshes will
        greatly degrade application performance. In almost all cases it
        is better to use the default behavior where the view is only
        refreshed if it is required.

        Returns:
        -----
        None

        Parameters:
        -----
        all: bool
        	[in] -> If true then refresh all views, otherwise refresh this view. 

        force: bool
        	[in] -> If true then force views to refresh even if they do not require it. 

        offscreen: bool
        	[in] -> Should the buffer be redrawn if it's offscreen?


        '''
        pass

    @overload
    def refresh(self, buffer: MPxGlBuffer): 
        '''
        refresh(self, buffer: MPxGlBuffer)

        Synopsis
        -----
        Refresh the this view into the GL buffer buffer. This refresh
        function always forces an update and always only draws the this
        view. The buffer argument should refer to a buffer that has been
        configured with the correct depth, color, z-buffer, etc. This
        configuration normally occurs in the constructor of the
        MPxGlBuffer and the behavior is undefined. If a buffer is
        configured for one view configuration and then is used for a
        different configuration. This may occur when Maya switches from
        wireframe to shaded mode since it also changes from color index
        to RGB mode.If the MPxGlBuffer is double buffered, drawing always
        is done to the back buffer and swapping is left to the user.

        Returns:
        -----
        None

        Parameters:
        -----
        buffer: MPxGlBuffer
        	[in] -> The 


        '''
        pass

    @overload
    def refresh(self, buffer: MPxGlBuffer,
                        offscreen: bool): 
        '''
        refresh(self, buffer: MPxGlBuffer,
                        offscreen: bool)

        Synopsis
        -----
        Refresh the this view into the GL buffer buffer. This refresh
        function always forces an update and always only draws the this
        view. The buffer argument should refer to a buffer that has been
        configured with the correct depth, color, z-buffer, etc. This
        configuration normally occurs in the constructor of the
        MPxGlBuffer and the behavior is undefined. If a buffer is
        configured for one view configuration and then is used for a
        different configuration. This may occur when Maya switches from
        wireframe to shaded mode since it also changes from color index
        to RGB mode.

        Returns:
        -----
        None

        Parameters:
        -----
        buffer: MPxGlBuffer
        	[in] -> The 

        offscreen: bool
        	[in] -> Should the buffer be redrawn if it's offscreen?


        '''
        pass

    @overload
    def refresh(self, buffer: MPxGlBuffer,
                        offscreen: bool,
                        projMatrix: MMatrix): 
        '''
        refresh(self, buffer: MPxGlBuffer,
                        offscreen: bool,
                        projMatrix: MMatrix)

        Synopsis
        -----
        Refresh the this view into the GL buffer buffer. This refresh
        function always forces an update and always only draws the this
        view. The buffer argument should refer to a buffer that has been
        configured with the correct depth, color, z-buffer, etc. This
        configuration normally occurs in the constructor of the
        MPxGlBuffer and the behavior is undefined. If a buffer is
        configured for one view configuration and then is used for a
        different configuration. This may occur when Maya switches from
        wireframe to shaded mode since it also changes from color index
        to RGB mode.

        Returns:
        -----
        None

        Parameters:
        -----
        buffer: MPxGlBuffer
        	[in] -> The 

        offscreen: bool
        	[in] -> Should the buffer be redrawn if it's offscreen? 

        projMatrix: MMatrix
        	[in] -> Projection matrix to provide to openGL before drawing


        '''
        pass

    def getLightCount(self, count: int,
                        visible: bool): 
        '''
        getLightCount(self, count: int,
                        visible: bool)

        Synopsis
        -----
        Get the number of lights for the view.

        Returns:
        -----
        None

        Parameters:
        -----
        count: int
        	[out] -> The number of visible lights for the view. 

        visible: bool
        	[in] -> Specify whether to count visible lights only. By Default this is set true.


        '''
        pass

    def getLightingMode(self, mode: M3dView.M3dView): 
        '''
        getLightingMode(self, mode: M3dView.M3dView)

        Synopsis
        -----
        Get the current lighting mode for the view.

        Returns:
        -----
        None

        Parameters:
        -----
        mode: M3dView.M3dView
        	[out] -> The lighting mode for the view.


        '''
        pass

    def getLightPath(self, lightNumber: int,
                        lightPath: MDagPath): 
        '''
        getLightPath(self, lightNumber: int,
                        lightPath: MDagPath)

        Synopsis
        -----
        Get the path to a certain light.

        Returns:
        -----
        None

        Parameters:
        -----
        lightNumber: int
        	[in] -> Number of the light interested in 

        lightPath: MDagPath
        	[out] -> Path to light.


        '''
        pass

    def isLightVisible(self, lightNumber: int,
                        visible: bool): 
        '''
        isLightVisible(self, lightNumber: int,
                        visible: bool)

        Synopsis
        -----
        Find out if a light is visible in the view.

        Returns:
        -----
        None

        Parameters:
        -----
        lightNumber: int
        	[in] -> The number of the light to check. 

        visible: bool
        	[out] -> Whether the light is visible or not.


        '''
        pass

    def getLightIndex(self, lightNumber: int,
                        lightIndex: int): 
        '''
        getLightIndex(self, lightNumber: int,
                        lightIndex: int)

        Synopsis
        -----
        Get the internal light index for a given light number.

        Returns:
        -----
        None

        Parameters:
        -----
        lightNumber: int
        	[in] -> The number of the light to check. 

        lightIndex: int
        	[out] -> The internal light index (returned)


        '''
        pass

    @overload
    def viewToWorld(self, x_pos: short,
                        y_pos: short,
                        worldPt: MPoint,
                        worldVector: MVector): 
        '''
        viewToWorld(self, x_pos: short,
                        y_pos: short,
                        worldPt: MPoint,
                        worldVector: MVector)

        Synopsis
        -----
        Takes a point in port coordinates and returns a corresponding ray
        in world coordinates.

        Returns:
        -----
        None

        Parameters:
        -----
        x_pos: short
        	[in] -> the x position of the point in port coordinates 

        y_pos: short
        	[in] -> the y position of the point in port coordinates 

        worldPt: MPoint
        	[out] -> (returned) the source of the ray 

        worldVector: MVector
        	[out] -> (returned) the direction of the ray


        '''
        pass

    @overload
    def viewToWorld(self, x_pos: short,
                        y_pos: short,
                        nearClipPt: MPoint,
                        farClipPt: MPoint): 
        '''
        viewToWorld(self, x_pos: short,
                        y_pos: short,
                        nearClipPt: MPoint,
                        farClipPt: MPoint)

        Synopsis
        -----
        Takes a point in port coordinates and returns a point on the near
        and far clipping planes.

        Returns:
        -----
        None

        Parameters:
        -----
        x_pos: short
        	[in] -> the x position of the point in port coordinates 

        y_pos: short
        	[in] -> the y position of the point in port coordinates 

        nearClipPt: MPoint
        	[out] -> (returned) point on near clipping plane 

        farClipPt: MPoint
        	[out] -> (returned) point on far clipping plane


        '''
        pass

    def viewToObjectSpace(self, x_pos: short,
                        y_pos: short,
                        localMatrixInverse: MMatrix,
                        oPt: MPoint,
                        oVector: MVector): 
        '''
        viewToObjectSpace(self, x_pos: short,
                        y_pos: short,
                        localMatrixInverse: MMatrix,
                        oPt: MPoint,
                        oVector: MVector)

        Synopsis
        -----
        Takes a point in port coordinates and returns a corresponding ray
        in object coordinates.

        Returns:
        -----
        None

        Parameters:
        -----
        x_pos: short
        	[in] -> the x position of the point in port coordinates 

        y_pos: short
        	[in] -> the y position of the point in port coordinates 

        localMatrixInverse: MMatrix
        	[in] -> the inclusive matrix inverse of the object in question 

        oPt: MPoint
        	[out] -> (returned) the source of the ray in object space 

        oVector: MVector
        	[out] -> (returned) the direction of the ray in object space


        '''
        pass

    def worldToView(self, worldPt: MPoint,
                        x_pos: short,
                        y_pos: short,
                        ReturnStatus: M3dView.MStatus): 
        '''
        worldToView(self, worldPt: MPoint,
                        x_pos: short,
                        y_pos: short,
                        ReturnStatus: M3dView.MStatus) -> bool

        Synopsis
        -----
        converts a point in world space to port space. The return value
        indicates if the point is not clipped.

        Returns: 
        ----- 
        true point is not clipped  false point is undefined or outside
        frustum

        Parameters:
        -----
        worldPt: MPoint
        	[in] -> the point to world space 

        x_pos: short
        	[out] -> (returned) The x coordinate of the world point in port space. 

        y_pos: short
        	[out] -> (returned) The y coordinate of the world point in port space. 

        ReturnStatus: M3dView.MStatus
        	[out] -> Status code


        '''
        pass

    def projectionMatrix(self, projMat: MMatrix): 
        '''
        projectionMatrix(self, projMat: MMatrix)

        Synopsis
        -----
        Returns the projection matrix currently being used by OpenGL in
        the current view.

        Returns:
        -----
        None

        Parameters:
        -----
        projMat: MMatrix
        	[out] -> A place to store the projection matrix


        '''
        pass

    def modelViewMatrix(self, modelViewMatrix: MMatrix): 
        '''
        modelViewMatrix(self, modelViewMatrix: MMatrix)

        Synopsis
        -----
        Returns the modelview matrix currently being used by OpenGL in
        the current view.

        Returns:
        -----
        None

        Parameters:
        -----
        modelViewMatrix: MMatrix
        	[out] -> A place to store the modelview matrix


        '''
        pass

    def viewSelectedPrefix(self, ReturnStatus: M3dView.MStatus): 
        '''
        viewSelectedPrefix(self, ReturnStatus: M3dView.MStatus) -> MString

        Synopsis
        -----
        Returns the Returns the prefix used when displaying the camera
        name in the heads up display when view selected in on.

        Returns: 
        ----- 
        The prefix.

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> the return status


        '''
        pass

    def setViewSelectedPrefix(self, prefix: MString): 
        '''
        setViewSelectedPrefix(self, prefix: MString)

        Synopsis
        -----
        Sets the prefix for the camera name as displayed in the heads up
        display when view selected is enabled. The prefix is concatenated
        with the camera name.The default value is "isolate: "

        Returns:
        -----
        None

        Parameters:
        -----
        prefix: MString
        	[in] -> The prefix to use.


        '''
        pass

    def showViewSelectedChildren(self, ReturnStatus: M3dView.MStatus): 
        '''
        showViewSelectedChildren(self, ReturnStatus: M3dView.MStatus) -> bool

        Synopsis
        -----
        Returns turn if view selected shows all of the children of the
        obejcts that are flagged for view selected.

        Returns: 
        ----- 
        true if the children of view selected objects are drawn.

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> The return status


        '''
        pass

    def setShowViewSelectedChildren(self, show: bool): 
        '''
        setShowViewSelectedChildren(self, show: bool)

        Synopsis
        -----
        This method changes the way that view selected works. By default,
        view selected with show all of the children of the objects in the
        view selected set. If false is passed to this method, then only
        the obejcts in the view selected set and their shapes will be
        drawn.

        Returns:
        -----
        None

        Parameters:
        -----
        show: bool
        	[in] -> true if all of the children of view selected objects should be displayed. true is the default behavior for view selected.


        '''
        pass

    def getM3dViewFromModelPanel(self, name: MString,
                        view: M3dView): 
        '''
        getM3dViewFromModelPanel(self, name: MString,
                        view: M3dView)

        Synopsis
        -----
        Given the name of a model panel, get the M3dView used by that
        panel. If this fails, then a panel with the given name could not
        be located.

        Returns:
        -----
        None

        Parameters:
        -----
        name: MString
        	[in] -> The name of the model panel. 

        view: M3dView
        	[out] -> The 


        '''
        pass

    def getM3dViewFromModelEditor(self, name: MString,
                        view: M3dView): 
        '''
        getM3dViewFromModelEditor(self, name: MString,
                        view: M3dView)

        Synopsis
        -----
        Given the name of a model editor, get the M3dView used by that
        editor. If this fails, then a editor with the given name could
        not be located.

        Returns:
        -----
        None

        Parameters:
        -----
        name: MString
        	[in] -> The name of the model editor. 

        view: M3dView
        	[out] -> The 


        '''
        pass

    def displayStyle(self, ReturnStatus: M3dView.MStatus): 
        '''
        displayStyle(self, ReturnStatus: M3dView.MStatus) -> M3dView.M3dView

        Synopsis
        -----
        Return the display style for this 3d view. The display style can
        be wireframe, flat-shaded, or smooth-shaded.

        Returns: 
        ----- 
        The display style for this view

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status code


        '''
        pass

    def isShadeActiveOnly(self, ReturnStatus: M3dView.MStatus): 
        '''
        isShadeActiveOnly(self, ReturnStatus: M3dView.MStatus) -> bool

        Synopsis
        -----
        Returns true if this view's display style is shaded for objects
        that are active and wireframe otherwise.

        Returns: 
        ----- 
        true Only active objects are shaded if this view is in shaded
        mode  false All objects are shaded if this view is in shaded mode

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status code


        '''
        pass

    def setDisplayStyle(self, style: M3dView.DisplayStyle,
                        activeOnly: bool): 
        '''
        setDisplayStyle(self, style: M3dView.DisplayStyle,
                        activeOnly: bool)

        Synopsis
        -----
        Sets the display style for this view. The display style can be
        wireframe, flat-shaded, or smooth-shaded.

        Returns:
        -----
        None

        Parameters:
        -----
        style: M3dView.DisplayStyle
        	[in] -> The display style to be set for this view 

        activeOnly: bool
        	[in] -> Specifies whether only active objects are to be shaded in shaded mode.


        '''
        pass

    def setObjectDisplay(self, displayMask: int): 
        '''
        setObjectDisplay(self, displayMask: int)

        Synopsis
        -----
        It is assumed in the below accessor methods that
        M3dView::DisplayObjects enum values can be cast to and from
        TexcludeObjectDisplay values impicitly, but that is not enforced
        elsewhere. Sets a display object mask that indicates which object
        types are drawn in the current view. By default everything is
        displayed.

        Returns:
        -----
        None

        Parameters:
        -----
        displayMask: int
        	[in] -> The display object mask made with 


        '''
        pass

    def objectDisplay(self, ReturnStatus: M3dView.MStatus): 
        '''
        objectDisplay(self, ReturnStatus: M3dView.MStatus) -> int

        Synopsis
        -----
        Returns a display object mask that indicates which object types
        are drawn in the current view.

        Returns: 
        ----- 
        The display object mask which can be bit 'AND'ed against the
        M3dView::DisplayObjects enum.

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> the return status


        '''
        pass

    def setPluginObjectDisplay(self, pluginDisplayFilter: MString,
                        on: bool): 
        '''
        setPluginObjectDisplay(self, pluginDisplayFilter: MString,
                        on: bool)

        Synopsis
        -----
        Enables or disables a user-defined display filter (i.e. one which
        was registered using MFnPlugin::registerDisplayFilter() or the
        'pluginDisplayFilter' command).In Default Viewport, the plug-in
        will have to check the state of the user-defined display filter
        in the node's draw code. In Viewport 2.0, nodes will be filtered
        automatically based on the classification associated with the
        filter. During selection/snapping, the plugin will have to check
        the state of the filter in the node's select/snap code.

        Returns:
        -----
        None

        Parameters:
        -----
        pluginDisplayFilter: MString
        	[in] -> The name of the plugin display filter. 

        on: bool
        	[in] -> Enable or disable the plugin display filter.


        '''
        pass

    def pluginObjectDisplay(self, pluginDisplayFilter: MString,
                        ReturnStatus: M3dView.MStatus): 
        '''
        pluginObjectDisplay(self, pluginDisplayFilter: MString,
                        ReturnStatus: M3dView.MStatus) -> bool

        Synopsis
        -----
        Returns true if the plugin display filter specified by the
        pluginDisplayFilter is enabled in the current view.

        Returns: 
        ----- 
        true if the plugin display filter is enabled

        Parameters:
        -----
        pluginDisplayFilter: MString
        	[in] -> The name of the plugin display filter. 

        ReturnStatus: M3dView.MStatus
        	[out] -> the return status


        '''
        pass

    def getRendererName(self, ReturnStatus: M3dView.MStatus): 
        '''
        getRendererName(self, ReturnStatus: M3dView.MStatus) -> M3dView.M3dView

        Synopsis
        -----
        Get the name of the current renderer being used for drawing to
        this view. The current possible return values
        are:kDefaultQualityRenderer : This is equivalent to when the
        renderer name is "base_OpenGL_Renderer" when queried from the
        "modelEditor" command kHighQualityRenderer : This is equivalent
        to when the renderer name is "hwRender_OpenGL_Renderer" when
        queried from the "modelEditor" command kViewport2Renderer : This
        is equivalent to the viewport 2.0 renderer.Note that the latter
        is not supported on platforms running the IRIX operating system.

        Returns: 
        ----- 
        The name of the current renderer.

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> the return status


        '''
        pass

    def rendererString(self, ReturnStatus: M3dView.MStatus): 
        '''
        rendererString(self, ReturnStatus: M3dView.MStatus) -> MString

        Synopsis
        -----
        Get the string name of the current renderer being used for
        drawing to this view.

        Returns: 
        ----- 
        String name

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> Status code (see below)


        '''
        pass

    def wireframeOnlyInShadedMode(self, ReturnStatus: M3dView.MStatus): 
        '''
        wireframeOnlyInShadedMode(self, ReturnStatus: M3dView.MStatus) -> bool

        Synopsis
        -----
        Return whether we are in shaded mode, but that only non shaded
        drawing should occur (wireframe). In general it will return true
        only when the current renderer is "hwRender_OpenGL_Renderer". See
        the M3dView::getRendererString() method for more details.

        Returns: 
        ----- 
        true if we are in this mode.

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> the return status


        '''
        pass

    def wireframeOnShaded(self, ReturnStatus: M3dView.MStatus): 
        '''
        wireframeOnShaded(self, ReturnStatus: M3dView.MStatus) -> bool

        Synopsis
        -----
        Return whether we draw wireframe in shaded mode.

        Returns: 
        ----- 
        true if we draw wireframe in shaded mode.

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> the return status


        '''
        pass

    def xray(self, ReturnStatus: M3dView.MStatus): 
        '''
        xray(self, ReturnStatus: M3dView.MStatus) -> bool

        Synopsis
        -----
        Return true if the X-Ray mode is enabled.

        Returns: 
        ----- 
        true if the X-Ray mode is enabled.

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> the return status


        '''
        pass

    def xrayJoints(self, ReturnStatus: M3dView.MStatus): 
        '''
        xrayJoints(self, ReturnStatus: M3dView.MStatus) -> bool

        Synopsis
        -----
        Return true if the X-Ray Joints mode is enabled.

        Returns: 
        ----- 
        true if the X-Ray Joints mode is enabled.

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> the return status


        '''
        pass

    def twoSidedLighting(self, ReturnStatus: M3dView.MStatus): 
        '''
        twoSidedLighting(self, ReturnStatus: M3dView.MStatus) -> bool

        Synopsis
        -----
        Return true if the Two-sided lighting mode is enabled.

        Returns: 
        ----- 
        true if the Two-sided lighting mode is enabled.

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> the return status


        '''
        pass

    def usingMipmappedTextures(self): 
        '''
        usingMipmappedTextures(self) -> bool

        Synopsis
        -----
        Returns if the view is using mipmapped texture display.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def usingDefaultMaterial(self): 
        '''
        usingDefaultMaterial(self) -> bool

        Synopsis
        -----
        Returns true if the view is currently displaying objects using
        the default material.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setDisallowPolygonOffset(self, v: bool): 
        '''
        setDisallowPolygonOffset(self, v: bool)

        Synopsis
        -----
        Certain Maya actions will use glPolygonOffset to offset polygons
        drawing into the depth buffer. This method controls this
        behavior. When true, it prevents Maya from altering the polygon
        offset parameters.

        Returns:
        -----
        None

        Parameters:
        -----
        v: bool
        	[in] -> enable/disable the polygon offset


        '''
        pass

    def disallowPolygonOffset(self): 
        '''
        disallowPolygonOffset(self) -> bool

        Synopsis
        -----
        Returns the current state of the disallow polygon offset bit. See
        setDisallowPolygonOffset for more information.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def updateViewingParameters(self): 
        '''
        updateViewingParameters(self)

        Synopsis
        -----
        This method tells the camera to set the view's transformation
        matrix.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def multipleDrawEnabled(self): 
        '''
        multipleDrawEnabled(self) -> bool

        Synopsis
        -----
        This method returns the multiple draw enable state for this view.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setRenderOverrideName(self, name: MString): 
        '''
        setRenderOverrideName(self, name: MString)

        Synopsis
        -----
        Set the name of a render override (MHWRender::MRenderOverride) to
        use. The override must be registered before it can be used.The
        override cannot be set unless the view is set to be using the
        Viewport 2.0 renderer.If the override name is an empty string
        then the any existing override will be removed.

        Returns:
        -----
        None

        Parameters:
        -----
        name: MString
        	[in] -> Name of the override.


        '''
        pass

    def renderOverrideName(self, ReturnStatus: M3dView.MStatus): 
        '''
        renderOverrideName(self, ReturnStatus: M3dView.MStatus) -> MString

        Synopsis
        -----
        Get the current render override name. If none then an empty
        string will be returned.

        Returns: 
        ----- 
        Override name.

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> return status.


        '''
        pass

    def setObjectListFilterName(self, name: MString): 
        '''
        setObjectListFilterName(self, name: MString)

        Synopsis
        -----
        Set the name of the object list filter (MObjectListFilter) to
        use. The filter must be registered before it can be used.If the
        name is an empty string then any existing filter will be
        removed.Any previously set filter will be replaced with the new
        one.

        Returns:
        -----
        None

        Parameters:
        -----
        name: MString
        	[in] -> Name of the filter.


        '''
        pass

    def objectListFilterName(self, ReturnStatus: M3dView.MStatus): 
        '''
        objectListFilterName(self, ReturnStatus: M3dView.MStatus) -> MString

        Synopsis
        -----
        Get the current object list filter name. If none then an empty
        string will be returned.

        Returns: 
        ----- 
        Filter name.

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> 


        '''
        pass

    def setShowObjectFilterNameInHUD(self, show: bool): 
        '''
        setShowObjectFilterNameInHUD(self, show: bool)

        Synopsis
        -----
        Sets whether or not to display the object filter UI name in the
        heads up display when an object filter is active. This string is
        concatenated with the camera name.

        Returns:
        -----
        None

        Parameters:
        -----
        show: bool
        	[in] -> If true, show the filter UI name in the HUD


        '''
        pass

    def showObjectFilterNameInHUD(self, ReturnStatus: M3dView.MStatus): 
        '''
        showObjectFilterNameInHUD(self, ReturnStatus: M3dView.MStatus) -> bool

        Synopsis
        -----
        Returns whether the object filter UI name is shown in the heads
        up display when an object filter is active.

        Returns: 
        ----- 
        True if the filter UI name is shown

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> the return status


        '''
        pass

    def viewIsFiltered(self, ReturnStatus: M3dView.MStatus): 
        '''
        viewIsFiltered(self, ReturnStatus: M3dView.MStatus) -> bool

        Synopsis
        -----
        Returns the state of view filtering for this view.

        Returns: 
        ----- 
        True if the view is filtered.

        Parameters:
        -----
        ReturnStatus: M3dView.MStatus
        	[out] -> return status


        '''
        pass

    def filteredObjectList(self, list: MSelectionList): 
        '''
        filteredObjectList(self, list: MSelectionList)

        Synopsis
        -----
        Returns a selection list containing all of the objects that
        remain after filtering is applied to the view.

        Returns:
        -----
        None

        Parameters:
        -----
        list: MSelectionList
        	[out] -> The list of objects left after filtering.


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

class DisplayStyle:
    '''Display styles for a 3D view. 
    Non-functional class.  Values for this enum:
    kBoundingBox
    kFlatShaded
    kGouraudShaded
    kWireFrame
    kPoints
    '''

    def __init__(self):
        pass

    def kBoundingBox(self):
        '''This is an enum of DisplayStyle.
        - Description: Bounding box display. 
        - Value: 0
        '''
        pass

    def kFlatShaded(self):
        '''This is an enum of DisplayStyle.
        - Description: Flat shaded display. 
        - Value: 1
        '''
        pass

    def kGouraudShaded(self):
        '''This is an enum of DisplayStyle.
        - Description: Gouraud shaded display. 
        - Value: 2
        '''
        pass

    def kWireFrame(self):
        '''This is an enum of DisplayStyle.
        - Description: Wire frame display. 
        - Value: 3
        '''
        pass

    def kPoints(self):
        '''This is an enum of DisplayStyle.
        - Description: Points only display. 
        - Value: 4
        '''
        pass

class DisplayStatus:
    '''Drawing modes for individual objects. 
    Non-functional class.  Values for this enum:
    kActive
    kLive
    kDormant
    kInvisible
    kHilite
    kTemplate
    kActiveTemplate
    kActiveComponent
    kLead
    kIntermediateObject
    kActiveAffected
    kNoStatus
    '''

    def __init__(self):
        pass

    def kActive(self):
        '''This is an enum of DisplayStatus.
        - Description: Object is active (selected). 
        - Value: 0
        '''
        pass

    def kLive(self):
        '''This is an enum of DisplayStatus.
        - Description: Object is live (construction surface). 
        - Value: 1
        '''
        pass

    def kDormant(self):
        '''This is an enum of DisplayStatus.
        - Description: Object is dormant (not selected, no other drawing mode enabled). 
        - Value: 2
        '''
        pass

    def kInvisible(self):
        '''This is an enum of DisplayStatus.
        - Description: Object is invisible (not drawn). 
        - Value: 3
        '''
        pass

    def kHilite(self):
        '''This is an enum of DisplayStatus.
        - Description: Object is hilited (has selectable components). 
        - Value: 4
        '''
        pass

    def kTemplate(self):
        '''This is an enum of DisplayStatus.
        - Description: Object is templated (Not renderable). 
        - Value: 5
        '''
        pass

    def kActiveTemplate(self):
        '''This is an enum of DisplayStatus.
        - Description: Object is active and templated. 
        - Value: 6
        '''
        pass

    def kActiveComponent(self):
        '''This is an enum of DisplayStatus.
        - Description: Object has active components. 
        - Value: 7
        '''
        pass

    def kLead(self):
        '''This is an enum of DisplayStatus.
        - Description: Last selected object. 
        - Value: 8
        '''
        pass

    def kIntermediateObject(self):
        '''This is an enum of DisplayStatus.
        - Description: Construction object (not drawn). 
        - Value: 9
        '''
        pass

    def kActiveAffected(self):
        '''This is an enum of DisplayStatus.
        - Description: Affected by active object(s). 
        - Value: 10
        '''
        pass

    def kNoStatus(self):
        '''This is an enum of DisplayStatus.
        - Description: Object does not have a valid display status. 
        - Value: 11
        '''
        pass

class ColorTable:
    '''Reference to color palettes. 
    Non-functional class.  Values for this enum:
    kActiveColors
    kDormantColors
    kTemplateColor
    kBackgroundColor
    '''

    def __init__(self):
        pass

    def kActiveColors(self):
        '''This is an enum of ColorTable.
        - Description: Colors for active objects. 
        - Value: 0
        '''
        pass

    def kDormantColors(self):
        '''This is an enum of ColorTable.
        - Description: Colors for dormant objects. 
        - Value: 2
        '''
        pass

    def kTemplateColor(self):
        '''This is an enum of ColorTable.
        - Description: Colors for templated objects. 
        - Value: 5
        '''
        pass

    def kBackgroundColor(self):
        '''This is an enum of ColorTable.
        - Description: Colors for background color. 
        - Value: 6
        '''
        pass

class TextPosition:
    '''Alignment values when drawing text. 
    Non-functional class.  Values for this enum:
    kLeft
    kCenter
    kRight
    '''

    def __init__(self):
        pass

    def kLeft(self):
        '''This is an enum of TextPosition.
        - Description: Draw text to the left of the point. 
        - Value: 0
        '''
        pass

    def kCenter(self):
        '''This is an enum of TextPosition.
        - Description: Draw text centered around the point. 
        - Value: 1
        '''
        pass

    def kRight(self):
        '''This is an enum of TextPosition.
        - Description: Draw text to the right of the point. 
        - Value: 2
        '''
        pass

class DisplayObjects:
    '''Display modes Bit masks used in combination with the return value of the dirtyMask() method to determine which portions of the geometry are dirty. 
    Non-functional class.  Values for this enum:
    kDisplayEverything
    kDisplayNurbsCurves
    kDisplayNurbsSurfaces
    kDisplayMeshes
    kDisplayPlanes
    kDisplayLights
    kDisplayCameras
    kDisplayJoints
    kDisplayIkHandles
    kDisplayDeformers
    kDisplayDynamics
    kDisplayParticleInstancers
    kDisplayLocators
    kDisplayDimensions
    kDisplaySelectHandles
    kDisplayPivots
    kDisplayTextures
    kDisplayGrid
    kDisplayCVs
    kDisplayHulls
    kDisplayStrokes
    kDisplaySubdivSurfaces
    kDisplayFluids
    kDisplayFollicles
    kDisplayHairSystems
    kDisplayImagePlane
    kDisplayNCloths
    kDisplayNRigids
    kDisplayDynamicConstraints
    kDisplayManipulators
    kDisplayNParticles
    kExcludeMotionTrails
    kExcludePluginShapes
    '''

    def __init__(self):
        pass

    def kDisplayEverything(self):
        '''This is an enum of DisplayObjects.
        - Description: Show everything. 
        - Value: -1
        '''
        pass

    def kDisplayNurbsCurves(self):
        '''This is an enum of DisplayObjects.
        - Description: Show nurbs curves. 
        - Value: 1
        '''
        pass

    def kDisplayNurbsSurfaces(self):
        '''This is an enum of DisplayObjects.
        - Description: Show nurbs surfaces. 
        - Value: 2
        '''
        pass

    def kDisplayMeshes(self):
        '''This is an enum of DisplayObjects.
        - Description: Show meshes. 
        - Value: 4
        '''
        pass

    def kDisplayPlanes(self):
        '''This is an enum of DisplayObjects.
        - Description: Show planes. 
        - Value: 8
        '''
        pass

    def kDisplayLights(self):
        '''This is an enum of DisplayObjects.
        - Description: Show lights. 
        - Value: 16
        '''
        pass

    def kDisplayCameras(self):
        '''This is an enum of DisplayObjects.
        - Description: Show camera. 
        - Value: 32
        '''
        pass

    def kDisplayJoints(self):
        '''This is an enum of DisplayObjects.
        - Description: Show joints. 
        - Value: 64
        '''
        pass

    def kDisplayIkHandles(self):
        '''This is an enum of DisplayObjects.
        - Description: Show IK handles. 
        - Value: 128
        '''
        pass

    def kDisplayDeformers(self):
        '''This is an enum of DisplayObjects.
        - Description: Show deformers. 
        - Value: 256
        '''
        pass

    def kDisplayDynamics(self):
        '''This is an enum of DisplayObjects.
        - Description: Show dynamics. 
        - Value: 512
        '''
        pass

    def kDisplayParticleInstancers(self):
        '''This is an enum of DisplayObjects.
        - Description: Show particle instancers. 
        - Value: 1024
        '''
        pass

    def kDisplayLocators(self):
        '''This is an enum of DisplayObjects.
        - Description: Show locators. 
        - Value: 2048
        '''
        pass

    def kDisplayDimensions(self):
        '''This is an enum of DisplayObjects.
        - Description: Show dimensions. 
        - Value: 4096
        '''
        pass

    def kDisplaySelectHandles(self):
        '''This is an enum of DisplayObjects.
        - Description: Show selection handles. 
        - Value: 8192
        '''
        pass

    def kDisplayPivots(self):
        '''This is an enum of DisplayObjects.
        - Description: Show pivots. 
        - Value: 16384
        '''
        pass

    def kDisplayTextures(self):
        '''This is an enum of DisplayObjects.
        - Description: Show textures. 
        - Value: 32768
        '''
        pass

    def kDisplayGrid(self):
        '''This is an enum of DisplayObjects.
        - Description: Show the grid. 
        - Value: 65536
        '''
        pass

    def kDisplayCVs(self):
        '''This is an enum of DisplayObjects.
        - Description: Show NURBS CVs. 
        - Value: 131072
        '''
        pass

    def kDisplayHulls(self):
        '''This is an enum of DisplayObjects.
        - Description: Show NURBS hulls. 
        - Value: 262144
        '''
        pass

    def kDisplayStrokes(self):
        '''This is an enum of DisplayObjects.
        - Description: Show strokes. 
        - Value: 524288
        '''
        pass

    def kDisplaySubdivSurfaces(self):
        '''This is an enum of DisplayObjects.
        - Description: Show subdivision surfaces. 
        - Value: 1048576
        '''
        pass

    def kDisplayFluids(self):
        '''This is an enum of DisplayObjects.
        - Description: Show fluids. 
        - Value: 2097152
        '''
        pass

    def kDisplayFollicles(self):
        '''This is an enum of DisplayObjects.
        - Description: Show follicles. 
        - Value: 4194304
        '''
        pass

    def kDisplayHairSystems(self):
        '''This is an enum of DisplayObjects.
        - Description: Show hair systems. 
        - Value: 8388608
        '''
        pass

    def kDisplayImagePlane(self):
        '''This is an enum of DisplayObjects.
        - Description: Show image plane. 
        - Value: 16777216
        '''
        pass

    def kDisplayNCloths(self):
        '''This is an enum of DisplayObjects.
        - Description: Show nCloths. 
        - Value: 33554432
        '''
        pass

    def kDisplayNRigids(self):
        '''This is an enum of DisplayObjects.
        - Description: Show nRigids. 
        - Value: 67108864
        '''
        pass

    def kDisplayDynamicConstraints(self):
        '''This is an enum of DisplayObjects.
        - Description: Show nDynamicConstraints. 
        - Value: 134217728
        '''
        pass

    def kDisplayManipulators(self):
        '''This is an enum of DisplayObjects.
        - Description: Show Manipulators. 
        - Value: 268435456
        '''
        pass

    def kDisplayNParticles(self):
        '''This is an enum of DisplayObjects.
        - Description: Show nParticles. 
        - Value: 536870912
        '''
        pass

    def kExcludeMotionTrails(self):
        '''This is an enum of DisplayObjects.
        - Description: Show motion trails. 
        - Value: 1073741824
        '''
        pass

    def kExcludePluginShapes(self):
        '''This is an enum of DisplayObjects.
        - Description: Show plugin shapes. 
        - Value: -2147483648
        '''
        pass

class LightingMode:
    '''Lighting mode used in this 3D view. 
    Non-functional class.  Values for this enum:
    kLightAll
    kLightSelected
    kLightActive
    kLightDefault
    kUnused1
    kLightNone
    '''

    def __init__(self):
        pass

    def kLightAll(self):
        '''This is an enum of LightingMode.
        - Description: All lights. 
        - Value: 0
        '''
        pass

    def kLightSelected(self):
        '''This is an enum of LightingMode.
        - Description: Selected lights. 
        - Value: 1
        '''
        pass

    def kLightActive(self):
        '''This is an enum of LightingMode.
        - Description: Active lights. 
        - Value: 2
        '''
        pass

    def kLightDefault(self):
        '''This is an enum of LightingMode.
        - Description: Default light. 
        - Value: 3
        '''
        pass

    def kUnused1(self):
        '''This is an enum of LightingMode.
        - Description: Not currently used in Maya. 
        - Value: 4
        '''
        pass

    def kLightNone(self):
        '''This is an enum of LightingMode.
        - Description: No lights / lighting disabled. 
        - Value: 5
        '''
        pass

class RendererName:
    '''Current hardware rendering engine used in this view. 
    Non-functional class.  Values for this enum:
    kDefaultQualityRenderer
    kHighQualityRenderer
    kViewport2Renderer
    kExternalRenderer
    '''

    def __init__(self):
        pass

    def kDefaultQualityRenderer(self):
        '''This is an enum of RendererName.
        - Description: Equivalent to when the renderer name is "base_OpenGL_Renderer" when queried from the "modelEditor" command. 
        - Value: 0
        '''
        pass

    def kHighQualityRenderer(self):
        '''This is an enum of RendererName.
        - Description: Equivalent to when the renderer name is "hwRender_OpenGL_Renderer" when queried from the "modelEditor" command. 
        - Value: 1
        '''
        pass

    def kViewport2Renderer(self):
        '''This is an enum of RendererName.
        - Description: Equivalent to the viewport 2.0 renderer. 
        - Value: 2
        '''
        pass

    def kExternalRenderer(self):
        '''This is an enum of RendererName.
        - Description: An externally defined renderer name has been set. 
        - Value: 3
        '''
        pass

class DepthBufferFormat:
    '''Possible depth buffer formats to read into. 
    Non-functional class.  Values for this enum:
    kDepth_8
    kDepth_Float
    '''

    def __init__(self):
        pass

    def kDepth_8(self):
        '''This is an enum of DepthBufferFormat.
        - Description: 8 bits. 
        - Value: 0
        '''
        pass

    def kDepth_Float(self):
        '''This is an enum of DepthBufferFormat.
        - Description: Floating point. 
        - Value: 1
        '''
        pass

class LineStipplePattern:
    '''Line stipple pattern. 
    Non-functional class.  Values for this enum:
    kStippleNone
    kStippleDashed
    '''

    def __init__(self):
        pass

    def kStippleNone(self):
        '''This is an enum of LineStipplePattern.
        - Description: No stipple. Solid line 
        - Value: 0
        '''
        pass

    def kStippleDashed(self):
        '''This is an enum of LineStipplePattern.
        - Description: Dashed line stipple. 
        - Value: 1
        '''
        pass

class MCursor:
    '''Manipulate Cursors.
The
MCursor class implements a cursor class, and is used to pass all cursor
arguments to Maya API methods.
The cursor image and mask are stored in xbm format to the
constructor along with the cursor dimensions and the cursor
hotspot.
'''
    def __init__(self):
        pass


    def __eq__(self, other: MCursor): 
        '''
        __eq__(self, other: MCursor) -> bool

        Synopsis
        -----
        Equality operator. Allows 2 MCursors to be compared to see if
        they are identical.

        Returns: 
        ----- 
        true if the objects are same.  false if the objects are
        different.

        Parameters:
        -----
        other: MCursor
        	[in] -> the 


        '''
        pass

    def __neq__(self, other: MCursor): 
        '''
        __neq__(self, other: MCursor) -> bool

        Synopsis
        -----
        Inequality operator. Allows 2 MCursors to be compared to see if
        they are not the same.

        Returns: 
        ----- 
        true if the objects are different.  false if the objects are
        same.

        Parameters:
        -----
        other: MCursor
        	[in] -> the 


        '''
        pass

class MDeviceChannel:
    '''Input device channel.
Input device channel class.
'''
    def __init__(self):
        pass


    def name(self): 
        '''
        name(self) -> MString

        Synopsis
        -----
        Return the short name of the channel.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def longName(self): 
        '''
        longName(self) -> MString

        Synopsis
        -----
        Return the long name of the channel.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def axisIndex(self): 
        '''
        axisIndex(self) -> int

        Synopsis
        -----
        Returns the device state index corresponding to this device
        channel.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def hasChildren(self): 
        '''
        hasChildren(self) -> bool

        Synopsis
        -----
        Determine whether this channel has children.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def parent(self): 
        '''
        parent(self) -> MDeviceChannel

        Synopsis
        -----
        Return the parent of this channel.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def childByIndex(self, index: int): 
        '''
        childByIndex(self, index: int) -> MDeviceChannel

        Synopsis
        -----
        Return the specified child of this channel.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> 


        '''
        pass

    def numChildren(self): 
        '''
        numChildren(self) -> int

        Synopsis
        -----
        Return the number of children of this channel.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MDeviceState:
    '''Input device state.
MDeviceState is a generic event class for input devices. Input device classes
(such as
MPxMidiInputDevice) are responsible for converting specific event types to an
MDeviceState which Maya understands.
'''
    def __init__(self):
        pass


    @overload
    def devicePosition(self, axis: short): 
        '''
        devicePosition(self, axis: short) -> int

        Synopsis
        -----
        Returns the position of the device for the specified axis.

        Returns: 
        ----- 
        The position of the device for the specified axis

        Parameters:
        -----
        axis: short
        	[in] -> The device axis to be tested


        '''
        pass

    @overload
    def devicePosition(self, axisName: MString): 
        '''
        devicePosition(self, axisName: MString) -> int

        Synopsis
        -----
        Returns the position of the device for the specified axis.

        Returns: 
        ----- 
        The position of the device for the specified axis

        Parameters:
        -----
        axisName: MString
        	[in] -> The name of the device axis to be tested


        '''
        pass

    @overload
    def setDevicePosition(self, position: int,
                        axis: short): 
        '''
        setDevicePosition(self, position: int,
                        axis: short)

        Synopsis
        -----
        Sets the position of the device for the specified axis.

        Returns:
        -----
        None

        Parameters:
        -----
        position: int
        	[in] -> The new position value 

        axis: short
        	[in] -> The axis of the device to be set 


        '''
        pass

    @overload
    def setDevicePosition(self, position: int,
                        axis: MString): 
        '''
        setDevicePosition(self, position: int,
                        axis: MString)

        Synopsis
        -----
        Sets the position of the device for the specified axis.

        Returns:
        -----
        None

        Parameters:
        -----
        position: int
        	[in] -> The new position value 

        axis: MString
        	[in] -> The name of the axis of the device to be set 


        '''
        pass

    @overload
    def buttonState(self, button: short): 
        '''
        buttonState(self, button: short) -> bool

        Synopsis
        -----
        Returns the state of the given button.

        Returns: 
        ----- 
        true button pressed  false button released

        Parameters:
        -----
        button: short
        	[in] -> The number of the button to be tested


        '''
        pass

    @overload
    def buttonState(self, buttonName: MString): 
        '''
        buttonState(self, buttonName: MString) -> bool

        Synopsis
        -----
        Returns the state of the named button.

        Returns: 
        ----- 
        true button pressed  false button released

        Parameters:
        -----
        buttonName: MString
        	[in] -> The name of the button to be tested


        '''
        pass

    @overload
    def setButtonState(self, state: bool,
                        button: short): 
        '''
        setButtonState(self, state: bool,
                        button: short)

        Synopsis
        -----
        Set the state of the specified button.

        Returns:
        -----
        None

        Parameters:
        -----
        state: bool
        	[in] -> The state to be set (

        button: short
        	[in] -> The button number 


        '''
        pass

    @overload
    def setButtonState(self, state: bool,
                        buttonName: MString): 
        '''
        setButtonState(self, state: bool,
                        buttonName: MString)

        Synopsis
        -----
        Set the state of the specified button.

        Returns:
        -----
        None

        Parameters:
        -----
        state: bool
        	[in] -> The state to be set (

        buttonName: MString
        	[in] -> The name of the button to be set 


        '''
        pass

    def maxAxis(self): 
        '''
        maxAxis(self) -> int

        Synopsis
        -----
        Return the value of the axis with the largest value. This is used
        to dejitter absolute devices.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def isNull(self): 
        '''
        isNull(self) -> bool

        Synopsis
        -----
        Returns true if this device state is NULL;.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MDrawData:
    '''The
MDrawData class holds geometry specific information for user defined
shapes which maya does not intrinsicly know about.
This class is used in the draw methods of
MPxSurfaceShapeUI For each draw request you must create and add a draw data object
which will contain geometry specific information that you will
need in the subsequent call to
MPxSurfaceShapeUI::draw.
MDrawData contains one void* member which is a pointer to an object that
you define. This object is the geometry needed to draw your
shape.
To create draw data use the function
MPxSurfaceShapeUI::getDrawData. This function takes two arguments, the first is a pointer to
your geometry object, the second is the draw data being created.
To add the data to a request use
MDrawRequest::setDrawData.
Draw data is also used to carry texture information to your draw
method. For materials with texture you must call
MMaterial::evaluateTexture from your
MPxSurfaceShapeUI::getDrawRequests method. Then in your draw method use
MMaterial::applyTexture to set up the viewport to draw using the textured material.
'''
    def __init__(self):
        pass


    def geometry(self): 
        '''
        geometry(self) -> void*

        Synopsis
        -----
        Returns the geometry associated with this draw data object. The
        geometry is set using the getDrawData method of
        MPxSurfaceShapeUI.

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

class MDrawInfo:
    '''This class is used by the getDrawRequests method of
MPxSurfaceShapeUI to specify the current object drawing state for a user defined
shape.
This getPrototype method is used to construct a draw request
object based on the current draw state for the object.
See
MDrawRequest for more information.
'''
    def __init__(self):
        pass


    def getPrototype(self, drawHandler: MPxSurfaceShapeUI): 
        '''
        getPrototype(self, drawHandler: MPxSurfaceShapeUI) -> MDrawRequest

        Synopsis
        -----
        This method creates a draw request based on the current draw
        state. The draw request is placed onto maya's drawing queue
        (MDrawRequestQueue) where it can be processed in turn. The
        drawHandler argument is the shape that will be doing the drawing
        which is the object calling this function.See MDrawRequest for
        more information.

        Returns: 
        ----- 
        A draw request

        Parameters:
        -----
        drawHandler: MPxSurfaceShapeUI
        	[in] -> the ui object that is doing the drawing


        '''
        pass

    def view(self): 
        '''
        view(self) -> M3dView

        Synopsis
        -----
        Returns the view that the drawing will take place.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def multiPath(self): 
        '''
        multiPath(self) -> const MDagPath

        Synopsis
        -----
        Returns the path to the object to be drawn.

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
        projectionMatrix(self) -> const MMatrix

        Synopsis
        -----
        Returns the camera*projection matrix.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def inclusiveMatrix(self): 
        '''
        inclusiveMatrix(self) -> const MMatrix

        Synopsis
        -----
        Returns the world space inclusive matrix.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def displayStyle(self): 
        '''
        displayStyle(self) -> M3dView.M3dView

        Synopsis
        -----
        The display appearance.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def displayStatus(self): 
        '''
        displayStatus(self) -> M3dView.M3dView

        Synopsis
        -----
        Returns the status of the object to draw.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def objectDisplayStatus(self, displayObj: M3dView.M3dView): 
        '''
        objectDisplayStatus(self, displayObj: M3dView.M3dView) -> bool

        Synopsis
        -----
        Determines whether the specified objects are allowed to be
        displayed.

        Returns:
        -----
        None

        Parameters:
        -----
        displayObj: M3dView.M3dView
        	[in] -> 


        '''
        pass

    def pluginObjectDisplayStatus(self, pluginDisplayFilter: MString): 
        '''
        pluginObjectDisplayStatus(self, pluginDisplayFilter: MString) -> bool

        Synopsis
        -----
        Determines whether the specified plugin object is allowed to be
        displayed.

        Returns: 
        ----- 
        true The specified object can be displayed.  false The specified
        object is excluded from display.

        Parameters:
        -----
        pluginDisplayFilter: MString
        	[in] -> The name of the plugin display filter which is registered by pluginDisplayFilter command.


        '''
        pass

    def inSelect(self): 
        '''
        inSelect(self) -> bool

        Synopsis
        -----
        Returns true if this is called from within the select method of
        MPxSurfaceShapeUI.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def inUserInteraction(self): 
        '''
        inUserInteraction(self) -> bool

        Synopsis
        -----
        Returns true during any interactive refresh, as when user is
        interacting with the scene in any way including camera changes,
        object or component TRS changes, etc. Use userChangingViewContext
        for determining whether user is changing the view using view
        context tools such as tumble, dolly or track.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def userChangingViewContext(self): 
        '''
        userChangingViewContext(self) -> bool

        Synopsis
        -----
        Returns true during any interactive refresh, as when user is
        changing the view using view context tools such as tumble, dolly
        or track. Useful for changing drawing mode to something simpler
        to speed up interaction re-draw. Use inUserInteraction for
        determining whether user is interacting with the scene in any
        way.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def completelyInside(self): 
        '''
        completelyInside(self) -> bool

        Synopsis
        -----
        Returns true if the object being drawn is inside the viewing
        frustum.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def canDrawComponent(self, isDisplayOn: bool,
                        mask: MSelectionMask): 
        '''
        canDrawComponent(self, isDisplayOn: bool,
                        mask: MSelectionMask) -> bool

        Synopsis
        -----
        Convenience method to test if components specified by the given
        mask can be drawn.

        Returns: 
        ----- 
        true the specified component can be drawn  false the specified
        component cannot be drawn

        Parameters:
        -----
        isDisplayOn: bool
        	[in] -> component display is on 

        mask: MSelectionMask
        	[in] -> component mask to test


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

class MDrawRequest:
    '''This class encapsulates all the information needed to fulfill a
request to draw an object or part of an object.
This class is used by the draw methods of
MPxSurfaceShapeUI derived objects.
The draw request should be created in the overridden
MPxSurfaceShapeUI::getDrawRequests method. Once created the appropriate "set" methods of this class
should be used to define what is being requested. Then the
request should be placed on the draw reqeust queue using
MDrawRequestQueue::add.
When your request gets processed by maya, your overriden
MPxSurfaceShape::draw method will get called with your request.
Use the query methods of this class to determine what to draw.
You create a draw request using the method
MDrawInfo::getPrototype. A draw request automatically picks up certain information
(listed below) upon its creation. So you don't have to set any of
this information unless you want to change it.
Information automatically set by
MDrawInfo::getPrototype :
The draw token is an integer value which you can use to specify
what is to be drawn. This is object specific and so you should
define an enum with the information you require to decide what is
being drawn in your
MPxSurfaceShapeUI::draw method.
Here is an example of draw token values for a polygonal mesh
object as defined in an
MPxSurfaceShapeUI derived class.
'''
    def __init__(self):
        pass


    def component(self): 
        '''
        component(self) -> MObject

        Synopsis
        -----
        An optional component. If set draw the components that are
        specified, otherwise draw all components of this type for the
        object.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setComponent(self, comp: MObject): 
        '''
        setComponent(self, comp: MObject)

        Synopsis
        -----
        Set a component to be drawn.

        Returns:
        -----
        None

        Parameters:
        -----
        comp: MObject
        	[in] -> component to be drawn 


        '''
        pass

    def setDrawData(self, data: MDrawData): 
        '''
        setDrawData(self, data: MDrawData)

        Synopsis
        -----
        Set the object specific draw data.

        Returns:
        -----
        None

        Parameters:
        -----
        data: MDrawData
        	[in] -> draw data 


        '''
        pass

    def setDisplayStatus(self, status: M3dView.M3dView): 
        '''
        setDisplayStatus(self, status: M3dView.M3dView)

        Synopsis
        -----
        Set the state of object (active, dormant, etc.).

        Returns:
        -----
        None

        Parameters:
        -----
        status: M3dView.M3dView
        	[in] -> display status 


        '''
        pass

    def setDisplayCulling(self, value: bool): 
        '''
        setDisplayCulling(self, value: bool)

        Synopsis
        -----
        Sets the state of the culling flag for the object.

        Returns:
        -----
        None

        Parameters:
        -----
        value: bool
        	[in] -> culling value to be set 


        '''
        pass

    def setDisplayCullOpposite(self, value: bool): 
        '''
        setDisplayCullOpposite(self, value: bool)

        Synopsis
        -----
        Sets the state of the culling flag for the object.

        Returns:
        -----
        None

        Parameters:
        -----
        value: bool
        	[in] -> culling value to be set 


        '''
        pass

    def setDisplayStyle(self, style: M3dView.M3dView): 
        '''
        setDisplayStyle(self, style: M3dView.M3dView)

        Synopsis
        -----
        Sets how the object should be drawn (wireframe, shaded, etc.).

        Returns:
        -----
        None

        Parameters:
        -----
        style: M3dView.M3dView
        	[in] -> display style to set 


        '''
        pass

    @overload
    def color(self, table: M3dView.M3dView): 
        '''
        color(self, table: M3dView.M3dView) -> int

        Synopsis
        -----
        Returns the wireframe display color. The color table specifies
        which of the 4 color planes to use. This table can be active,
        dormant, template, or background.

        Returns:
        -----
        None

        Parameters:
        -----
        table: M3dView.M3dView
        	[in] -> color table 


        '''
        pass

    @overload
    def setColor(self, value: int,
                        table: M3dView.M3dView): 
        '''
        setColor(self, value: int,
                        table: M3dView.M3dView)

        Synopsis
        -----
        Sets the wireframe display color. The color table specifies which
        of the 4 color planes to use. This table can be active, dormant,
        template, or background.

        Returns:
        -----
        None

        Parameters:
        -----
        value: int
        	[in] -> index into the color table 

        table: M3dView.M3dView
        	[in] -> color table 


        '''
        pass

    @overload
    def color(self): 
        '''
        color(self) -> MColor

        Synopsis
        -----
        Returns the RGBA wireframe display color.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def setColor(self, color: MColor): 
        '''
        setColor(self, color: MColor)

        Synopsis
        -----
        Sets the RGBA wireframe display color.

        Returns:
        -----
        None

        Parameters:
        -----
        color: MColor
        	[in] -> The RGBA wireframe color 


        '''
        pass

    def setMaterial(self, material: MMaterial): 
        '''
        setMaterial(self, material: MMaterial)

        Synopsis
        -----
        Returns the shaded material.

        Returns:
        -----
        None

        Parameters:
        -----
        material: MMaterial
        	[in] -> the material to set 


        '''
        pass

    def setIsTransparent(self, value: bool): 
        '''
        setIsTransparent(self, value: bool)

        Synopsis
        -----
        Sets the transparency state of the object.

        Returns:
        -----
        None

        Parameters:
        -----
        value: bool
        	[in] -> the transparency value 


        '''
        pass

    def setDrawLast(self, value: bool): 
        '''
        setDrawLast(self, value: bool)

        Synopsis
        -----
        Specifies the order in which this object will be drawn.

        Returns:
        -----
        None

        Parameters:
        -----
        value: bool
        	[in] -> draw last flag 


        '''
        pass

    def token(self): 
        '''
        token(self) -> int

        Synopsis
        -----
        Returns the user-defined draw token for this request. The token
        is used to identify a particular part of an object to draw. It is
        also used to distinguish draw requests generated by derived UI
        objects from those generated by base classes. It some cases, it
        provides a way of indicating that a component should be displayed
        without creating a component MObject.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setToken(self, value: int): 
        '''
        setToken(self, value: int)

        Synopsis
        -----
        Set the user-defined draw token for this request. The token is
        used to identify a particular part of an object to draw. It is
        also used to distinguish draw requests generated by derived UI
        objects from those generated by base classes. It some cases, it
        provides a way of indicating that a component should be displayed
        without creating a component MObject.

        Returns:
        -----
        None

        Parameters:
        -----
        value: int
        	[in] -> 


        '''
        pass

    def matrix(self): 
        '''
        matrix(self) -> const MMatrix&

        Synopsis
        -----
        Returns the draw matrix. This is typically the world matrix of
        the object, filled in by MDrawInfo::getPrototype(). Commonly this
        will be equal to multiPath().inclusiveMatrix() but in some
        circumstances will be a modified matrix, for example, when
        animation ghosts are being drawn.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setMatrix(self, value: MMatrix): 
        '''
        setMatrix(self, value: MMatrix)

        Synopsis
        -----
        Set the draw matrix.

        Returns:
        -----
        None

        Parameters:
        -----
        value: MMatrix
        	[in] -> The matrix to set. 


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

class MDrawRequestQueue:
    '''This class defines a simple interface for a collection of
MDrawRequest objects.
An
MDrawRequestQueue object is passed to the getDrawRequests method of a user defined
shape's UI class (
MPxSurfaceShapeUI). This queue keeps track of all the things that need to get draw
when a refresh of the view occurs.
Maya will call the getDrawRequest methods of all the visible DAG
objects before a refresh happens. Then as the refresh happens,
each draw request will be processed and the corresponding draw
method for each DAG object will get called. For user defined
shapes
MPxSurfaceShapeUI::draw will get called.
'''
    def __init__(self):
        pass


    def isEmpty(self): 
        '''
        isEmpty(self) -> bool

        Synopsis
        -----
        Returns true if the queu is empty.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def add(self, request: MDrawRequest): 
        '''
        add(self, request: MDrawRequest)

        Synopsis
        -----
        Adds a draw request to the draw queue.

        Returns:
        -----
        None

        Parameters:
        -----
        request: MDrawRequest
        	[in] -> the draw request to add 


        '''
        pass

    def remove(self): 
        '''
        remove(self) -> MDrawRequest

        Synopsis
        -----
        Removes a draw request from the draw queue.

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

class MDrawTraversal:
    '''MDrawTraversal is a utility class for interactive drawing.
The purpose of the class is to traverse through the current scene
dag and provide a means of accessing a list of visible objects
with respect to a given frustum specification, and application
"visibility" criteria.
The additional "visibility" criteria include:
Note that as the traversal is not dependent on a 3d modeling
viewport. There are thus no checks for per viewport visibility
properties such as per viewport dag object type overrides, and
"isolate select".
Additionally, render layer visibility checks are not performed,
as these pertain to software rendering.
After traversal the list will contain leaf level nodes (shapes),
which have passed the "visibility" criteria.
For the actual frustum culling, there is a choice of two culling
algorithms:
Note that hierarchical culling may force evaluation of geometry
on dag objects which are not visible.
The default is thus to perform leaf level culling only.
Frustum culling is performed against the bounding boxes of dag
objects encountered.
API writers can derive from this class and change the
filterNode() virtual method to perform custom filtering of objects during
traversal. That is they will be excluded from the output list. By
default this class does no additional filtering.
'''
    def __init__(self):
        pass


    def enum(self): 
        '''
        enum(self) -> anonymous

        Synopsis
        -----
        Item status enum. Check if item is active. Check if item is
        templated.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def traverse(self): 
        '''
        traverse(self)

        Synopsis
        -----
        Perform traversal of the current scene from the root of the dag
        hierarchy. A valid frustum must be set before calling this
        method.If the traversal was succesfull a list of traversal items
        will have been evaluated.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def filterNode(self, traversalItem: MDagPath): 
        '''
        filterNode(self, traversalItem: MDagPath) -> bool

        Synopsis
        -----
        Method to allow filtering during traversal. The traversalItem can
        be examined, and if it is not match the desired criteria, it will
        not be added to the output traversal list.A return value of
        "false" will result in filtering out this item. A return value of
        "true" will result in regular filtering to occuring.API writers
        can derive from MDrawTraversal, and implement their own
        filterNode() method to perform custom filtering as desired.

        Returns: 
        ----- 
        Will always return false for MDrawTraversal class.

        Parameters:
        -----
        traversalItem: MDagPath
        	[in] -> path to item to test.


        '''
        pass

    @overload
    def setFrustum(self, cameraPath: MDagPath,
                        portWidth: int,
                        portHeight: int): 
        '''
        setFrustum(self, cameraPath: MDagPath,
                        portWidth: int,
                        portHeight: int)

        Synopsis
        -----
        Set the frustum to cull with. The frustum is based on the
        attributes of the camera argument provided.Note that traversal
        always requries that a valid frustum to be set. There is no
        default frustum provided.

        Returns:
        -----
        None

        Parameters:
        -----
        cameraPath: MDagPath
        	[in] -> path to a valid scene camera. 

        portWidth: int
        	[in] -> width of the viewport to cull against. 

        portHeight: int
        	[in] -> height of the viewport to cull against.


        '''
        pass

    def setOrthoFrustum(self, left: double,
                        right: double,
                        bottom: double,
                        top: double,
                        nearpt: double,
                        farpt: double,
                        worldXform: MMatrix): 
        '''
        setOrthoFrustum(self, left: double,
                        right: double,
                        bottom: double,
                        top: double,
                        nearpt: double,
                        farpt: double,
                        worldXform: MMatrix)

        Synopsis
        -----
        Set up an orthographic view frustum to cull with. The frustum is
        symmetric about the vertical and horizontal.Note that traversal
        always requries that a valid frustum to be set. There is no
        default frustum provided.

        Returns:
        -----
        None

        Parameters:
        -----
        left: double
        	[in] -> Left side of frustum (local space). 

        right: double
        	[in] -> Right side of frustum (local space). 

        bottom: double
        	[in] -> Bottom of frustum (local space). 

        top: double
        	[in] -> Top of frustum (local space). 

        nearpt: double
        	[in] -> Front / near point of frustum (local space). 

        farpt: double
        	[in] -> Back / far point of frustum (local space). 

        worldXform: MMatrix
        	[in] -> transformation from local to world space.


        '''
        pass

    def setPerspFrustum(self, fovX: double,
                        aspectXY: double,
                        nearDist: double,
                        farDist: double,
                        worldXform: MMatrix): 
        '''
        setPerspFrustum(self, fovX: double,
                        aspectXY: double,
                        nearDist: double,
                        farDist: double,
                        worldXform: MMatrix)

        Synopsis
        -----
        Set up an perspective view frustum to cull with. The frustum is
        symmetric about the vertical and horizontal.Note that traversal
        always requries that a valid frustum to be set. There is no
        default frustum provided.

        Returns:
        -----
        None

        Parameters:
        -----
        fovX: double
        	[in] -> Field of view in X. 

        aspectXY: double
        	[in] -> aspect ratio X / Y. 

        nearDist: double
        	[in] -> distance to near plane. 

        farDist: double
        	[in] -> distance to far plane. 

        worldXform: MMatrix
        	[in] -> transformation from local to world space.


        '''
        pass

    @overload
    def setFrustum(self, left: double,
                        right: double,
                        bottom: double,
                        top: double,
                        nearpt: double,
                        farpt: double,
                        worldXform: MMatrix): 
        '''
        setFrustum(self, left: double,
                        right: double,
                        bottom: double,
                        top: double,
                        nearpt: double,
                        farpt: double,
                        worldXform: MMatrix)

        Synopsis
        -----
        Set up a frustum to cull with. The frustum can be asymmetric is
        distance about the vertial and horizontal.Note that traversal
        always requries that a valid frustum to be set. There is no
        default frustum provided.

        Returns:
        -----
        None

        Parameters:
        -----
        left: double
        	[in] -> Left side of frustum (local space). 

        right: double
        	[in] -> Right side of frustum (local space). 

        bottom: double
        	[in] -> Bottom of frustum (local space). 

        top: double
        	[in] -> Top of frustum (local space). 

        nearpt: double
        	[in] -> Front / near point of frustum (local space). 

        farpt: double
        	[in] -> Back / far point of frustum (local space). 

        worldXform: MMatrix
        	[in] -> transformation from local to world space.


        '''
        pass

    @overload
    def setFrustum(self, nearBottomLeft: MPoint,
                        nearBottomRight: MPoint,
                        nearTopLeft: MPoint,
                        nearTopRight: MPoint,
                        farBottomLeft: MPoint,
                        farBottomRight: MPoint,
                        farTopLeft: MPoint,
                        farTopRight: MPoint,
                        worldXform: MMatrix): 
        '''
        setFrustum(self, nearBottomLeft: MPoint,
                        nearBottomRight: MPoint,
                        nearTopLeft: MPoint,
                        nearTopRight: MPoint,
                        farBottomLeft: MPoint,
                        farBottomRight: MPoint,
                        farTopLeft: MPoint,
                        farTopRight: MPoint,
                        worldXform: MMatrix)

        Synopsis
        -----
        Set up a frustum to cull with by specifying the 8 corner points.
        Asymmetric frustum's can be set up using this method.Note that
        traversal always requries that a valid frustum to be set. There
        is no default frustum provided.

        Returns:
        -----
        None

        Parameters:
        -----
        nearBottomLeft: MPoint
        	[in] -> Near bottom left corner of frustum (local space). 

        nearBottomRight: MPoint
        	[in] -> Near bottom Right corner of frustum (local space). 

        nearTopLeft: MPoint
        	[in] -> Near top left corner of frustum (local space). 

        nearTopRight: MPoint
        	[in] -> Near top right corner of frustum (local space). 

        farBottomLeft: MPoint
        	[in] -> Far bottom left corner of frustum (local space). 

        farBottomRight: MPoint
        	[in] -> Far bottom right corner of frustum (local space). 

        farTopLeft: MPoint
        	[in] -> Far top left corner of frustum (local space). 

        farTopRight: MPoint
        	[in] -> Far top right corner of frustum (local space). 

        worldXform: MMatrix
        	[in] -> transformation from local to world space.


        '''
        pass

    def frustumValid(self): 
        '''
        frustumValid(self) -> bool

        Synopsis
        -----
        Returns whether the current frustum set is valid or not. If it is
        not valid a call to the traverse() function will result in
        returning failure.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setLeafLevelCulling(self, cullAtLeafLevel: bool): 
        '''
        setLeafLevelCulling(self, cullAtLeafLevel: bool)

        Synopsis
        -----
        Set whether to cull at the leaf levels, or perform hierarchical
        culling. This value should be set before traversing using the
        traverse() function.If a value is not explicitly set, the default
        is to perform culling at the leaf levels only.

        Returns:
        -----
        None

        Parameters:
        -----
        cullAtLeafLevel: bool
        	[in] -> flag to indicate culling preference.


        '''
        pass

    def leafLevelCulling(self): 
        '''
        leafLevelCulling(self) -> bool

        Synopsis
        -----
        Returns whether the current cull algorithm will cull at the leaf
        levels, or perform hierarchical culling. The default value is
        leaf level culling.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def enableFiltering(self, val: bool): 
        '''
        enableFiltering(self, val: bool)

        Synopsis
        -----
        Sets whether to use enable usage of the filterNode() method to
        perform custom filtering. By default this is set to
        false.Filtering must be enabled for filterNode() to be called
        during traversal.

        Returns:
        -----
        None

        Parameters:
        -----
        val: bool
        	[in] -> value for enabling. 


        '''
        pass

    def filteringEnabled(self): 
        '''
        filteringEnabled(self) -> bool

        Synopsis
        -----
        Tells whether custom filtering has been enabled. That is, to use
        the filterNode() method during traversal.By default this is set
        to false.Filtering must be enabled for filterNode() to be called
        during traversal.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def numberOfItems(self): 
        '''
        numberOfItems(self) -> int

        Synopsis
        -----
        Return the number of items found after traversal.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def itemPath(self, itemNumber: int,
                        path: MDagPath): 
        '''
        itemPath(self, itemNumber: int,
                        path: MDagPath)

        Synopsis
        -----
        Get the path for a given item in the list of found items after
        traversal.

        Returns:
        -----
        None

        Parameters:
        -----
        itemNumber: int
        	[in] -> which item to return. 

        path: MDagPath
        	[out] -> path of item (returned).


        '''
        pass

    def itemHasStatus(self, itemNumber: int,
                        test: int): 
        '''
        itemHasStatus(self, itemNumber: int,
                        test: int) -> bool

        Synopsis
        -----
        Test the display status for a given item in the list of found
        items after traversal.

        Returns: 
        ----- 
        true, if item status matches the display status to test against.

        Parameters:
        -----
        itemNumber: int
        	[in] -> which item to return. 

        test: int
        	[in] -> the display status to check the item against.


        '''
        pass

class MEvent:
    '''System event information.
The
MEvent class is used for querying system events such as mouse presses.
Events are handled by an
MPxContext derived class in which MEvents are passed and can be accessed.
Since Maya has default actions for several events, only a subset
are avalaible through the API. The events that can be accessed
are:
Several modifiers for events are also accessible through the API.
Modifiers are actions that occur during an event. For example,
holding down the shift key while pressing a mouse button causes a
button press event to occur with a shift modifier.
A modifier can be used to determine if two mouse events occur
simulaneously. The second mouse event is registered as a modifier
in the hold event of the first mouse button. So if you wanted to
determine if both the left and middle buttons are pressed then
you would query the modifier in the hold event of the first mouse
button using the
isModifierMiddleMouseButton() and
isModifierLeftMouseButton() methods.
'''
    def __init__(self):
        pass


    def getPosition(self, x_pos: short,
                        y_pos: short): 
        '''
        getPosition(self, x_pos: short,
                        y_pos: short)

        Synopsis
        -----
        Get the location of the event in view co-ordinates. The origin is
        at the lower left corner of the window.

        Returns:
        -----
        None

        Parameters:
        -----
        x_pos: short
        	[out] -> storage for horizonal position 

        y_pos: short
        	[out] -> storage for vertical position


        '''
        pass

    def setPosition(self, x_pos: short,
                        y_pos: short): 
        '''
        setPosition(self, x_pos: short,
                        y_pos: short)

        Synopsis
        -----
        set the location of the event to the specified location. The
        origin is at the lower left corner of the window.

        Returns:
        -----
        None

        Parameters:
        -----
        x_pos: short
        	[in] -> horizonal position to set 

        y_pos: short
        	[in] -> vertical position to set


        '''
        pass

    def getWindowPosition(self, x_pos: short,
                        y_pos: short): 
        '''
        getWindowPosition(self, x_pos: short,
                        y_pos: short)

        Synopsis
        -----
        This routine is used by responders to query the position of the
        pointer when the event occurred. It is given in screen co-
        ordinates.The origin is at the upper left corner of the window.

        Returns:
        -----
        None

        Parameters:
        -----
        x_pos: short
        	[out] -> storage for horizonal position 

        y_pos: short
        	[out] -> storage for vertical position


        '''
        pass

    def mouseButton(self, ReturnStatus: MEvent.MStatus): 
        '''
        mouseButton(self, ReturnStatus: MEvent.MStatus) -> MEvent.MEvent

        Synopsis
        -----
        Get the mouse button of the last event.

        Returns: 
        ----- 
        Mouse button from last event.

        Parameters:
        -----
        ReturnStatus: MEvent.MStatus
        	[out] -> 


        '''
        pass

    def isModifierKeyRelease(self, ReturnStatus: MEvent.MStatus): 
        '''
        isModifierKeyRelease(self, ReturnStatus: MEvent.MStatus) -> bool

        Synopsis
        -----
        Was a modifier key released.

        Returns: 
        ----- 
        true A modifier key was released.  false No modifier key was
        released.

        Parameters:
        -----
        ReturnStatus: MEvent.MStatus
        	[out] -> 


        '''
        pass

    def modifiers(self, ReturnStatus: MEvent.MStatus): 
        '''
        modifiers(self, ReturnStatus: MEvent.MStatus) -> MEvent.MEvent

        Synopsis
        -----
        This routine is used by responders to find the state of the
        modifiers during the event.

        Returns: 
        ----- 
        Modifier type.

        Parameters:
        -----
        ReturnStatus: MEvent.MStatus
        	[out] -> 


        '''
        pass

    def setModifiers(self, modType: MEvent.ModifierType): 
        '''
        setModifiers(self, modType: MEvent.ModifierType)

        Synopsis
        -----
        set the event modifiers.

        Returns:
        -----
        None

        Parameters:
        -----
        modType: MEvent.ModifierType
        	[in] -> Type of modifier to set to.


        '''
        pass

    def isModifierNone(self, ReturnStatus: MEvent.MStatus): 
        '''
        isModifierNone(self, ReturnStatus: MEvent.MStatus) -> bool

        Synopsis
        -----
        Determines if there are any modifiers for this event.

        Returns: 
        ----- 
        true There are modifiers for this event.  false There are NO
        modifiers for this event.

        Parameters:
        -----
        ReturnStatus: MEvent.MStatus
        	[out] -> 


        '''
        pass

    def isModifierShift(self, ReturnStatus: MEvent.MStatus): 
        '''
        isModifierShift(self, ReturnStatus: MEvent.MStatus) -> bool

        Synopsis
        -----
        return state of shift key.

        Returns: 
        ----- 
        true Shift key triggered this event.  false The shift key did not
        cause this event.

        Parameters:
        -----
        ReturnStatus: MEvent.MStatus
        	[out] -> 


        '''
        pass

    def isModifierControl(self, ReturnStatus: MEvent.MStatus): 
        '''
        isModifierControl(self, ReturnStatus: MEvent.MStatus) -> bool

        Synopsis
        -----
        return state of control key.

        Returns: 
        ----- 
        true Control key triggered this event.  false The control key did
        not cause this event.

        Parameters:
        -----
        ReturnStatus: MEvent.MStatus
        	[out] -> 


        '''
        pass

    def isModifierLeftMouseButton(self, ReturnStatus: MEvent.MStatus): 
        '''
        isModifierLeftMouseButton(self, ReturnStatus: MEvent.MStatus) -> bool

        Synopsis
        -----
        Return the state of the left mouse button. This method is only
        valid when called in the hold event for another mouse press.

        Returns: 
        ----- 
        true Left mouse button triggered this event.  false The left
        moust button did not cause this event.

        Parameters:
        -----
        ReturnStatus: MEvent.MStatus
        	[out] -> 


        '''
        pass

    def isModifierMiddleMouseButton(self, ReturnStatus: MEvent.MStatus): 
        '''
        isModifierMiddleMouseButton(self, ReturnStatus: MEvent.MStatus) -> bool

        Synopsis
        -----
        Return the state of the middle mouse button. This method is only
        valid when called in the hold event for another mouse press.

        Returns: 
        ----- 
        true Middle mouse button triggered this event.  false The middle
        moust button did not cause this event.

        Parameters:
        -----
        ReturnStatus: MEvent.MStatus
        	[out] -> 


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

class ModifierType:
    '''Modifier key types. 
    Non-functional class.  Values for this enum:
    shiftKey
    controlKey
    '''

    def __init__(self):
        pass

    def shiftKey(self):
        '''This is an enum of ModifierType.
        - Description:  
        - Value: 1
        '''
        pass

    def controlKey(self):
        '''This is an enum of ModifierType.
        - Description:  
        - Value: 4
        '''
        pass

class MouseButtonType:
    '''Mouse button types. 
    Non-functional class.  Values for this enum:
    kLeftMouse
    kMiddleMouse
    '''

    def __init__(self):
        pass

    def kLeftMouse(self):
        '''This is an enum of MouseButtonType.
        - Description:  
        - Value: 64
        '''
        pass

    def kMiddleMouse(self):
        '''This is an enum of MouseButtonType.
        - Description:  
        - Value: 128
        '''
        pass

class MExternalDropCallback:
    '''Provides a callback hook into Maya's drag-and-drop mechanism.
This class is used to register callbacks to gain access to Maya's
drag-and-drop information during dropping an external object to
Maya. You can replace or augment Maya's drop behavior for
external drag-and-drop operations.
To register callbacks, inherit from this class and override
externalDropCallback(). The method can be overridden by the callback. Then register the
callbacks by calling the
addCallback() or addSceneItemCallback() methods.
Each of the callback methods gets passed the name of the drop
site control (in case of using
addCallback() for registration) or UFE path string (in case of using
addSceneItemCallback() for registration). Also, the callback
methods get passed an
MExternalDropData instance which contains additional information provided by the
system (for example, text or URL information associated with the
drop).
If multiple callbacks need to be registered, the order of
invocation can be set by adding each callback with a priority
number, 0 being the highest priority. Callbacks are then invoked
in priority order. Note that the first callback that does not
return kMayaDefault will cause the invocations to stop; lower
priority callbacks will then not be invoked.
'''
    def __init__(self):
        pass


    def externalDropCallback(self, doDrop: bool,
                        targetName: MString,
                        data: MExternalDropData): 
        '''
        externalDropCallback(self, doDrop: bool,
                        targetName: MString,
                        data: MExternalDropData) -> OPENMAYA_NAMESPACE_CLOSEMExternalDropCallback.OPENMAYA_NAMESPACE_CLOSEMExternalDropCallback

        Synopsis
        -----
        This pure virtual method must be implemented by derived callback
        classes. It is called one or more times during a drag-and-drop
        operation, as a user drags the mouse over various UI
        elements.When called with doDrop false, the callback is simply
        checking whether it is valid to drop the current item onto the
        control in question. If doDrop is true, the callback should
        actually perform the drop operation, if any.In case of using
        addCallback() for registration, the targetName provided is the
        full path to the control, and can be for example passed to MEL
        commands that query or operate on UI objects.In case of using
        addSceneItemCallback() for registration, the targetName provided
        is the full ufe path string to the ufe scene item under the mouse
        cursor (for example in Outliner).The MExternalDropData instance
        contains the actual drop data provided by the operating system.
        For example, if a file is being dragged from the desktop into
        Maya, the drop data might contain the path (as a URL) of the
        file.

        Returns: 
        ----- 
        a status code indicating what action Maya should take following
        the callback

        Parameters:
        -----
        doDrop: bool
        	[in] -> true if the drop action should actually be performed (on mouse up), or false if this callback is just checking for a valid drop (on mouse drag) 

        targetName: MString
        	[in] -> the full name of the UI element or the scene item onto which the drop will take place 

        data: MExternalDropData
        	[in] -> an instance of 


        '''
        pass

    def addCallback(self, cb: MExternalDropCallback,
                        priority: int): 
        '''
        addCallback(self, cb: MExternalDropCallback,
                        priority: int)

        Synopsis
        -----
        Add a callback to the general list.

        Returns:
        -----
        None

        Parameters:
        -----
        cb: MExternalDropCallback
        	[in] -> The callback object to add. 

        priority: int
        	[in] -> The priority of the callback (zero is highest priority).


        '''
        pass

    def removeCallback(self, cb: MExternalDropCallback): 
        '''
        removeCallback(self, cb: MExternalDropCallback)

        Synopsis
        -----
        Remove a callback from the general list.

        Returns:
        -----
        None

        Parameters:
        -----
        cb: MExternalDropCallback
        	[in] -> The callback object to remove.


        '''
        pass

    def addUFEItemCallback(self, cb: MExternalDropCallback,
                        priority: int): 
        '''
        addUFEItemCallback(self, cb: MExternalDropCallback,
                        priority: int)

        Synopsis
        -----
        Add a callback to the list containing UFE item callbacks.

        Returns:
        -----
        None

        Parameters:
        -----
        cb: MExternalDropCallback
        	[in] -> The callback object to add. 

        priority: int
        	[in] -> The priority of the callback (zero is highest priority).


        '''
        pass

    def removeUFEItemCallback(self, cb: MExternalDropCallback): 
        '''
        removeUFEItemCallback(self, cb: MExternalDropCallback)

        Synopsis
        -----
        Remove a callback from the list containing UFE item callbacks.

        Returns:
        -----
        None

        Parameters:
        -----
        cb: MExternalDropCallback
        	[in] -> The callback object to remove.


        '''
        pass

class MExternalDropStatus:
    '''Possible return values from externalDropCallback(), used to inform Maya of what further action to take, if any. 
    Non-functional class.  Values for this enum:
    kMayaDefault
    kNoMayaDefaultAndAccept
    kNoMayaDefaultAndNoAccept
    '''

    def __init__(self):
        pass

    def kMayaDefault(self):
        '''This is an enum of MExternalDropStatus.
        - Description: Run Maya default action. 
        - Value: 0
        '''
        pass

    def kNoMayaDefaultAndAccept(self):
        '''This is an enum of MExternalDropStatus.
        - Description: Skip Maya default action and accept the drop. 
        - Value: 1
        '''
        pass

    def kNoMayaDefaultAndNoAccept(self):
        '''This is an enum of MExternalDropStatus.
        - Description: Skip Maya default action and do not accept the drop. 
        - Value: 2
        '''
        pass

class MExternalDropData:
    '''Drag-and-drop data, used with
MExternalDropCallback.
MExternalDropData is the data that a drag-and-drop operation carries if dragging
from an external application and dropping onto Maya.
It typically arrives from a
MExternalDropCallback callback method.
'''
    def __init__(self):
        pass


    def hasText(self): 
        '''
        hasText(self) -> bool

        Synopsis
        -----
        Query whether the drop contains text data.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def text(self): 
        '''
        text(self) -> MString

        Synopsis
        -----
        Obtain the text data contained in the drop, if any.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def hasUrls(self): 
        '''
        hasUrls(self) -> bool

        Synopsis
        -----
        Query whether the drop contains URL data.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def urls(self): 
        '''
        urls(self) -> MStringArray

        Synopsis
        -----
        Obtain the URL data contained in the drop, if any.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def hasHtml(self): 
        '''
        hasHtml(self) -> bool

        Synopsis
        -----
        Query whether the drop contains html data.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def html(self): 
        '''
        html(self) -> MString

        Synopsis
        -----
        Obtain the html data contained in the drop, if any.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def hasColor(self): 
        '''
        hasColor(self) -> bool

        Synopsis
        -----
        Query whether the drop contains color data.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def color(self): 
        '''
        color(self) -> MColor

        Synopsis
        -----
        Obtain the color data contained in the drop, if any.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def hasImage(self): 
        '''
        hasImage(self) -> bool

        Synopsis
        -----
        Query whether the drop contains image data.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def image(self): 
        '''
        image(self) -> MImage

        Synopsis
        -----
        Obtain the image data contained in the drop, if any.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def formats(self): 
        '''
        formats(self) -> MStringArray

        Synopsis
        -----
        Obtain the list of data formats contained in the drop.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def hasFormat(self, format: MString): 
        '''
        hasFormat(self, format: MString) -> bool

        Synopsis
        -----
        Query whether the drop contains data in a given format. The
        result will be true iff the format is contained in the result of
        the formats() method.

        Returns: 
        ----- 
        true the drop contains data with the given format  false the drop
        does not contain data with the given format

        Parameters:
        -----
        format: MString
        	[in] -> The format to look for.


        '''
        pass

    def dataSize(self, format: MString): 
        '''
        dataSize(self, format: MString) -> int

        Synopsis
        -----
        Return the size (in bytes) of the data with the given format
        contained in the drop.

        Returns: 
        ----- 
        the size of the data, in bytes (zero if the format is not
        present)

        Parameters:
        -----
        format: MString
        	[in] -> The format to look for.


        '''
        pass

    def keyboardModifiers(self): 
        '''
        keyboardModifiers(self) -> int

        Synopsis
        -----
        Return the modifier state for this drop. Use
        MExternalDropData::KeyboardModifiers bitmask to distinguish the
        states.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def mouseButtons(self): 
        '''
        mouseButtons(self) -> int

        Synopsis
        -----
        Return the mouse button state for this drop. Use
        MExternalDropData::MouseButtons bitmask to distinguish the
        states.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MFeedbackLine:
    '''Feedback line.
The
MFeedbackLine class is used to display information back to the user. The
format for the feedback line which indicates the number and type
of the arguments should be set with the setFormat method. The
values of the arguments should be set using the setValue method.
'''
    def __init__(self):
        pass


    def setFormat(self, format: MString): 
        '''
        setFormat(self, format: MString) -> MFeedbackLine.OPENMAYA_MAJOR_NAMESPACE_OPEN MStatus

        Synopsis
        -----
        Set the format string for the feedback line. The format begins
        with a format specifier "^" followed by the format size, format
        decimal character ".", decimal size, and format type. For
        example: the format "^6.3f" which specifies that there is going
        to be one value given, it is a float, with 3 decimal places
        shown.

        Returns: 
        ----- 
        MS::kSuccess operation successful  MS::kInsufficientMemory
        insufficient memory

        Parameters:
        -----
        format: MString
        	[in] -> the format string for the feedback line


        '''
        pass

    def setTitle(self, title: MString): 
        '''
        setTitle(self, title: MString)

        Synopsis
        -----
        Set the title string.

        Returns:
        -----
        None

        Parameters:
        -----
        title: MString
        	[in] -> the title string


        '''
        pass

    def setValue(self, index: short,
                        value: double): 
        '''
        setValue(self, index: short,
                        value: double)

        Synopsis
        -----
        Set the value of a given index in the feedback line.

        Returns:
        -----
        None

        Parameters:
        -----
        index: short
        	[in] -> the index whose value should be set 

        value: double
        	[in] -> the value of the index


        '''
        pass

    def showFeedback(self): 
        '''
        showFeedback(self) -> bool

        Synopsis
        -----
        Return whether or not the feedback line is is supposed to be
        displaying data.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setShowFeedback(self, showFeedback: bool): 
        '''
        setShowFeedback(self, showFeedback: bool)

        Synopsis
        -----
        Set whether the feedback line is supposed to be displaying data.

        Returns:
        -----
        None

        Parameters:
        -----
        showFeedback: bool
        	[in] -> whether or not the feedback line should display data 


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

class MFnCircleSweepManip:
    '''CircleSweepManip function set.
The CircleSweepManip allows the user to manipulate a point
constrained to move around a circle, in order to specify a sweep
angle. This manipulator generates a single floating point value
corresponding to the sweep angle.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kCircleSweepManip.Reimplemented from MFnManip3D.

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
        className(self) -> MFnCircleSweepManip.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnCircleSweepManip".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def create(self, ReturnStatus: MFnCircleSweepManip.MStatus): 
        '''
        create(self, ReturnStatus: MFnCircleSweepManip.MStatus) -> MObject

        Synopsis
        -----
        Creates a new CircleSweepManip. This function set's object is set
        to be the new manipulator.This method should only be used to
        create a non-composite CircleSweepManip.The name that appears in
        the feedback line is "circleSweep"

        Returns: 
        ----- 
        Newly created CircleSweepManip

        Parameters:
        -----
        ReturnStatus: MFnCircleSweepManip.MStatus
        	[out] -> return status


        '''
        pass

    @overload
    def create(self, manipName: MString,
                        angleName: MString,
                        ReturnStatus: MFnCircleSweepManip.MStatus): 
        '''
        create(self, manipName: MString,
                        angleName: MString,
                        ReturnStatus: MFnCircleSweepManip.MStatus) -> MObject

        Synopsis
        -----
        Creates a new CircleSweepManip. This function set's object is set
        to be the new manipulator.This method should only be used to
        create a non-composite CircleSweepManip.The name that appears in
        the feedback line is specified by the angleName argument.

        Returns: 
        ----- 
        Newly created CircleSweepManip.

        Parameters:
        -----
        manipName: MString
        	[in] -> Name of the manip for UI purposes. 

        angleName: MString
        	[in] -> Label for the angle value which appears in the feedback line. 

        ReturnStatus: MFnCircleSweepManip.MStatus
        	[out] -> Status code.


        '''
        pass

    def connectToAnglePlug(self, anglePlug: MPlug): 
        '''
        connectToAnglePlug(self, anglePlug: MPlug)

        Synopsis
        -----
        Connect to the angle plug. The data type corresponding to the
        anglePlug is a double. (Note that MFnUnitAttribute::kAngle is
        used to specify an angle attribute.)

        Returns:
        -----
        None

        Parameters:
        -----
        anglePlug: MPlug
        	[in] -> the angle plug


        '''
        pass

    def setCenterPoint(self, centerPoint: MPoint): 
        '''
        setCenterPoint(self, centerPoint: MPoint)

        Synopsis
        -----
        Sets the center point of the CircleSweepManip.

        Returns:
        -----
        None

        Parameters:
        -----
        centerPoint: MPoint
        	[in] -> the center point of the CircleSweepManip


        '''
        pass

    def setStartPoint(self, startPoint: MPoint): 
        '''
        setStartPoint(self, startPoint: MPoint)

        Synopsis
        -----
        Sets the start point of the CircleSweepManip.

        Returns:
        -----
        None

        Parameters:
        -----
        startPoint: MPoint
        	[in] -> the start point of the CircleSweepManip


        '''
        pass

    def setEndPoint(self, endPoint: MPoint): 
        '''
        setEndPoint(self, endPoint: MPoint)

        Synopsis
        -----
        Sets the end point of the CircleSweepManip.

        Returns:
        -----
        None

        Parameters:
        -----
        endPoint: MPoint
        	[in] -> the end point of the CircleSweepManip


        '''
        pass

    def setNormal(self, normal: MVector): 
        '''
        setNormal(self, normal: MVector)

        Synopsis
        -----
        Sets the normal of the CircleSweepManip.

        Returns:
        -----
        None

        Parameters:
        -----
        normal: MVector
        	[in] -> the normal of the CircleSweepManip


        '''
        pass

    def setRadius(self, radius: double): 
        '''
        setRadius(self, radius: double)

        Synopsis
        -----
        Sets the radius of the CircleSweepManip.

        Returns:
        -----
        None

        Parameters:
        -----
        radius: double
        	[in] -> the radius of the CircleSweepManip


        '''
        pass

    def setAngle(self, angle: MAngle): 
        '''
        setAngle(self, angle: MAngle)

        Synopsis
        -----
        Sets the angle of the CircleSweepManip.

        Returns:
        -----
        None

        Parameters:
        -----
        angle: MAngle
        	[in] -> the angle of the CircleSweepManip


        '''
        pass

    def setDrawAsArc(self, state: bool): 
        '''
        setDrawAsArc(self, state: bool)

        Synopsis
        -----
        Sets whether or not to draw as arc.

        Returns:
        -----
        None

        Parameters:
        -----
        state: bool
        	[in] -> whether or not to draw as arc


        '''
        pass

    def startPoint(self, ReturnStatus: MFnCircleSweepManip.MStatus): 
        '''
        startPoint(self, ReturnStatus: MFnCircleSweepManip.MStatus) -> MPoint

        Synopsis
        -----
        Returns the start point.

        Returns: 
        ----- 
        The start point

        Parameters:
        -----
        ReturnStatus: MFnCircleSweepManip.MStatus
        	[out] -> return status


        '''
        pass

    def endPoint(self, ReturnStatus: MFnCircleSweepManip.MStatus): 
        '''
        endPoint(self, ReturnStatus: MFnCircleSweepManip.MStatus) -> MPoint

        Synopsis
        -----
        Returns the end point.

        Returns: 
        ----- 
        The end point

        Parameters:
        -----
        ReturnStatus: MFnCircleSweepManip.MStatus
        	[out] -> return status


        '''
        pass

    def centerIndex(self, ReturnStatus: MFnCircleSweepManip.MStatus): 
        '''
        centerIndex(self, ReturnStatus: MFnCircleSweepManip.MStatus) -> int

        Synopsis
        -----
        Returns the index for the center of the CircleSweepManip. The
        data type corresponding to this index is
        MFnNumericData::k3Double.

        Returns: 
        ----- 
        The center index

        Parameters:
        -----
        ReturnStatus: MFnCircleSweepManip.MStatus
        	[out] -> return status


        '''
        pass

    def axisIndex(self, ReturnStatus: MFnCircleSweepManip.MStatus): 
        '''
        axisIndex(self, ReturnStatus: MFnCircleSweepManip.MStatus) -> int

        Synopsis
        -----
        Returns the index for the axis of CircleSweepManip. The data type
        corresponding to this index is MFnNumericData::k3Double.

        Returns: 
        ----- 
        The axis index

        Parameters:
        -----
        ReturnStatus: MFnCircleSweepManip.MStatus
        	[out] -> return status


        '''
        pass

    def angleIndex(self, ReturnStatus: MFnCircleSweepManip.MStatus): 
        '''
        angleIndex(self, ReturnStatus: MFnCircleSweepManip.MStatus) -> int

        Synopsis
        -----
        Returns the index for the angle of CircleSweepManip. The data
        type corresponding to this index is a double.

        Returns: 
        ----- 
        The angle index

        Parameters:
        -----
        ReturnStatus: MFnCircleSweepManip.MStatus
        	[out] -> return status


        '''
        pass

    def startCircleIndex(self, ReturnStatus: MFnCircleSweepManip.MStatus): 
        '''
        startCircleIndex(self, ReturnStatus: MFnCircleSweepManip.MStatus) -> int

        Synopsis
        -----
        Returns the index for the start of the circle of
        CircleSweepManip. The data type corresponding to this index is a
        double.

        Returns: 
        ----- 
        The circle start index

        Parameters:
        -----
        ReturnStatus: MFnCircleSweepManip.MStatus
        	[out] -> return status


        '''
        pass

    def endCircleIndex(self, ReturnStatus: MFnCircleSweepManip.MStatus): 
        '''
        endCircleIndex(self, ReturnStatus: MFnCircleSweepManip.MStatus) -> int

        Synopsis
        -----
        Returns the index for the end of the circle of CircleSweepManip.
        The data type corresponding to this index is a double.

        Returns: 
        ----- 
        The circle end index

        Parameters:
        -----
        ReturnStatus: MFnCircleSweepManip.MStatus
        	[out] -> return status


        '''
        pass

class MFnCurveSegmentManip:
    '''CurveSegmentManip function set.
The CurveSegmentManip allows the user to manipulate two points on
a curve, in order to specify a curve segment. This manipulator
generates two floating point values, which correspond to the
parameters of the start and end of the curve segment.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kCurveSegmentManip.Reimplemented from MFnManip3D.

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
        className(self) -> MFnCurveSegmentManip.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnCurveSegmentManip".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def create(self, ReturnStatus: MFnCurveSegmentManip.MStatus): 
        '''
        create(self, ReturnStatus: MFnCurveSegmentManip.MStatus) -> MObject

        Synopsis
        -----
        Creates a new CurveSegmentManip. This function set's object is
        set to be the new manipulator.This method should only be used to
        create a non-composite CurveSegmentManip.The name that appears in
        the feedback line is "CurveSegment"

        Returns: 
        ----- 
        Newly created CurveSegmentManip

        Parameters:
        -----
        ReturnStatus: MFnCurveSegmentManip.MStatus
        	[out] -> return status


        '''
        pass

    @overload
    def create(self, manipName: MString,
                        startParamName: MString,
                        endParamName: MString,
                        ReturnStatus: MFnCurveSegmentManip.MStatus): 
        '''
        create(self, manipName: MString,
                        startParamName: MString,
                        endParamName: MString,
                        ReturnStatus: MFnCurveSegmentManip.MStatus) -> MObject

        Synopsis
        -----
        Creates a new CurveSegmentManip. This function set's object is
        set to be the new manipulator.This method should only be used to
        create a non-composite CurveSegmentManip.The names that appears
        in the feedback line are specified by the startParamName and
        endParamName arguments.

        Returns: 
        ----- 
        Newly created CurveSegmentManip.

        Parameters:
        -----
        manipName: MString
        	[in] -> Name of the manip for UI purposes. 

        startParamName: MString
        	[in] -> Label for the startParam value which appears in the feedback line. 

        endParamName: MString
        	[in] -> Label for the endParam value which appears in the feedback line. 

        ReturnStatus: MFnCurveSegmentManip.MStatus
        	[out] -> Status code.


        '''
        pass

    def connectToCurvePlug(self, curvePlug: MPlug): 
        '''
        connectToCurvePlug(self, curvePlug: MPlug)

        Synopsis
        -----
        Connect to the curve plug. The data type corresponding to the
        curvePlug is MFnData::kNurbsCurve.

        Returns:
        -----
        None

        Parameters:
        -----
        curvePlug: MPlug
        	[in] -> the curve plug


        '''
        pass

    def connectToStartParamPlug(self, startParamPlug: MPlug): 
        '''
        connectToStartParamPlug(self, startParamPlug: MPlug)

        Synopsis
        -----
        Connect to the startParam plug. The data type corresponding to
        the startParamPlug is a double.

        Returns:
        -----
        None

        Parameters:
        -----
        startParamPlug: MPlug
        	[in] -> the startParam plug


        '''
        pass

    def connectToEndParamPlug(self, endParamPlug: MPlug): 
        '''
        connectToEndParamPlug(self, endParamPlug: MPlug)

        Synopsis
        -----
        Connect to the endParam plug. The data type corresponding to the
        endParamPlug is a double.

        Returns:
        -----
        None

        Parameters:
        -----
        endParamPlug: MPlug
        	[in] -> the endParam plug


        '''
        pass

    def setStartParameter(self, startParameter: double): 
        '''
        setStartParameter(self, startParameter: double)

        Synopsis
        -----
        Sets the start parameter.

        Returns:
        -----
        None

        Parameters:
        -----
        startParameter: double
        	[in] -> the start parameter


        '''
        pass

    def setEndParameter(self, endParameter: double): 
        '''
        setEndParameter(self, endParameter: double)

        Synopsis
        -----
        Sets the end parameter.

        Returns:
        -----
        None

        Parameters:
        -----
        endParameter: double
        	[in] -> the end parameter


        '''
        pass

    def startParameter(self, ReturnStatus: MFnCurveSegmentManip.MStatus): 
        '''
        startParameter(self, ReturnStatus: MFnCurveSegmentManip.MStatus) -> double

        Synopsis
        -----
        Returns the start parameter.

        Returns: 
        ----- 
        start parameter

        Parameters:
        -----
        ReturnStatus: MFnCurveSegmentManip.MStatus
        	[out] -> return status


        '''
        pass

    def endParameter(self, ReturnStatus: MFnCurveSegmentManip.MStatus): 
        '''
        endParameter(self, ReturnStatus: MFnCurveSegmentManip.MStatus) -> double

        Synopsis
        -----
        Returns the end parameter.

        Returns: 
        ----- 
        End parameter

        Parameters:
        -----
        ReturnStatus: MFnCurveSegmentManip.MStatus
        	[out] -> return status


        '''
        pass

    def curveIndex(self, ReturnStatus: MFnCurveSegmentManip.MStatus): 
        '''
        curveIndex(self, ReturnStatus: MFnCurveSegmentManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the curve. The data type corresponding to
        this index is MFnData::kNurbsCurve.

        Returns: 
        ----- 
        Curve index

        Parameters:
        -----
        ReturnStatus: MFnCurveSegmentManip.MStatus
        	[out] -> return status


        '''
        pass

    def startParamIndex(self, ReturnStatus: MFnCurveSegmentManip.MStatus): 
        '''
        startParamIndex(self, ReturnStatus: MFnCurveSegmentManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the start parameter of the
        CurveSegmentManip. The data type corresponding to this index is a
        double.

        Returns: 
        ----- 
        Start parameter index

        Parameters:
        -----
        ReturnStatus: MFnCurveSegmentManip.MStatus
        	[out] -> return status


        '''
        pass

    def endParamIndex(self, ReturnStatus: MFnCurveSegmentManip.MStatus): 
        '''
        endParamIndex(self, ReturnStatus: MFnCurveSegmentManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the end parameter of the CurveSegmentManip.
        The data type corresponding this index is a double.

        Returns: 
        ----- 
        End parameter index

        Parameters:
        -----
        ReturnStatus: MFnCurveSegmentManip.MStatus
        	[out] -> return status


        '''
        pass

class MFnDirectionManip:
    '''DirectionManip function set.
The DirectionManip allows the user to specify a direction, as
defined by the vector from the start point to the manipulator
position. It uses a FreePointTriadManip to specify the end point
of a vector relative to a given start point. This manipulator
generates a vector from the start point to the end point.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kDirectionManip.Reimplemented from MFnManip3D.

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
        className(self) -> MFnDirectionManip.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnDirectionManip".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def create(self, ReturnStatus: MFnDirectionManip.MStatus): 
        '''
        create(self, ReturnStatus: MFnDirectionManip.MStatus) -> MObject

        Synopsis
        -----
        Creates a new DirectionManip. This function set's object is set
        to be the new manipulator.This method should only be used to
        create a non-composite DirectionManip.The name that appears in
        the feedback line is "direction"

        Returns: 
        ----- 
        Newly created DirectionManip

        Parameters:
        -----
        ReturnStatus: MFnDirectionManip.MStatus
        	[out] -> return status


        '''
        pass

    @overload
    def create(self, manipName: MString,
                        directionName: MString,
                        ReturnStatus: MFnDirectionManip.MStatus): 
        '''
        create(self, manipName: MString,
                        directionName: MString,
                        ReturnStatus: MFnDirectionManip.MStatus) -> MObject

        Synopsis
        -----
        Creates a new DirectionManip. This function set's object is set
        to be the new manipulator.This method should only be used to
        create a non-composite DirectionManip.The name that appears in
        the feedback line is specified by the directionName argument.

        Returns: 
        ----- 
        Newly created DirectionManip.

        Parameters:
        -----
        manipName: MString
        	[in] -> Name of the manip for UI purposes. 

        directionName: MString
        	[in] -> Label for the direction value which appears in the feedback line. 

        ReturnStatus: MFnDirectionManip.MStatus
        	[out] -> Status code.


        '''
        pass

    def connectToDirectionPlug(self, directionPlug: MPlug): 
        '''
        connectToDirectionPlug(self, directionPlug: MPlug)

        Synopsis
        -----
        Connect to the direction plug. The data type corresponding to the
        directionPlug is MFnNumericData::k3Double.

        Returns:
        -----
        None

        Parameters:
        -----
        directionPlug: MPlug
        	[in] -> the direction plug


        '''
        pass

    def setNormalizeDirection(self, state: bool): 
        '''
        setNormalizeDirection(self, state: bool)

        Synopsis
        -----
        Sets whether or not to the direction should be normalized. By
        default the direction is normalized.

        Returns:
        -----
        None

        Parameters:
        -----
        state: bool
        	[in] -> whether or not the direction should be normalized


        '''
        pass

    def setDrawStart(self, state: bool): 
        '''
        setDrawStart(self, state: bool)

        Synopsis
        -----
        Sets whether or not to draw the start of the DirectionManip. The
        start of the DirectionManip is indicated by a grey dot. By
        default the start is not drawn.

        Returns:
        -----
        None

        Parameters:
        -----
        state: bool
        	[in] -> whether or not the start should be drawn


        '''
        pass

    def setStartPoint(self, startPoint: MPoint): 
        '''
        setStartPoint(self, startPoint: MPoint)

        Synopsis
        -----
        Sets the start point of the DirectionManip.

        Returns:
        -----
        None

        Parameters:
        -----
        startPoint: MPoint
        	[in] -> the start point of the DirectionManip


        '''
        pass

    def setDirection(self, direction: MVector): 
        '''
        setDirection(self, direction: MVector)

        Synopsis
        -----
        Sets the direction of the DirectionManip.

        Returns:
        -----
        None

        Parameters:
        -----
        direction: MVector
        	[in] -> the direction of the DirectionManip


        '''
        pass

    def startPointIndex(self, ReturnStatus: MFnDirectionManip.MStatus): 
        '''
        startPointIndex(self, ReturnStatus: MFnDirectionManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the start point of the DirectionManip. The
        data type corresponding to this index is
        MFnNumericData::k3Double.

        Returns: 
        ----- 
        Start point index

        Parameters:
        -----
        ReturnStatus: MFnDirectionManip.MStatus
        	[out] -> return status


        '''
        pass

    def endPointIndex(self, ReturnStatus: MFnDirectionManip.MStatus): 
        '''
        endPointIndex(self, ReturnStatus: MFnDirectionManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the end point of the DirectionManip. The
        data type corresponding to this index is
        MFnNumericData::k3Double.

        Returns: 
        ----- 
        End point index

        Parameters:
        -----
        ReturnStatus: MFnDirectionManip.MStatus
        	[out] -> return status


        '''
        pass

    def directionIndex(self, ReturnStatus: MFnDirectionManip.MStatus): 
        '''
        directionIndex(self, ReturnStatus: MFnDirectionManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the direction. The data type corresponding
        to this index is MFnNumericData::k3Double.

        Returns: 
        ----- 
        Direction index

        Parameters:
        -----
        ReturnStatus: MFnDirectionManip.MStatus
        	[out] -> return status


        '''
        pass

class MFnDiscManip:
    '''DiscManip function set.
The DiscManip allows the user to rotate a disc in order to
specify a rotation about an axis. This manipulator generates a
single floating point value corresponding to the rotation.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kDiscManip.Reimplemented from MFnManip3D.

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
        className(self) -> MFnDiscManip.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnDiscManip".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def create(self, ReturnStatus: MFnDiscManip.MStatus): 
        '''
        create(self, ReturnStatus: MFnDiscManip.MStatus) -> MObject

        Synopsis
        -----
        Creates a new DiscManip. This function set's object is set to be
        the new manipulator.This method should only be used to create a
        non-composite DiscManip.The name that appears in the feedback
        line is "Disc"

        Returns: 
        ----- 
        Newly created DiscManip

        Parameters:
        -----
        ReturnStatus: MFnDiscManip.MStatus
        	[out] -> return status


        '''
        pass

    @overload
    def create(self, manipName: MString,
                        angleName: MString,
                        ReturnStatus: MFnDiscManip.MStatus): 
        '''
        create(self, manipName: MString,
                        angleName: MString,
                        ReturnStatus: MFnDiscManip.MStatus) -> MObject

        Synopsis
        -----
        Creates a new DiscManip. This function set's object is set to be
        the new manipulator.This method should only be used to create a
        non-composite DiscManip.The name that appears in the feedback
        line is specified by the angleName argument.

        Returns: 
        ----- 
        Newly created DiscManip.

        Parameters:
        -----
        manipName: MString
        	[in] -> Name of the manip for UI purposes. 

        angleName: MString
        	[in] -> Label for the angle value which appears in the feedback line. 

        ReturnStatus: MFnDiscManip.MStatus
        	[out] -> Status code.


        '''
        pass

    def connectToAnglePlug(self, anglePlug: MPlug): 
        '''
        connectToAnglePlug(self, anglePlug: MPlug)

        Synopsis
        -----
        Connect to the angle plug. The data type corresponding to the
        anglePlug is a double. (Note that MFnUnitAttribute::kAngle is
        used to specify an angle attribute.)

        Returns:
        -----
        None

        Parameters:
        -----
        anglePlug: MPlug
        	[in] -> the angle plug


        '''
        pass

    def setCenterPoint(self, centerPoint: MPoint): 
        '''
        setCenterPoint(self, centerPoint: MPoint)

        Synopsis
        -----
        Sets the center point of the DiscManip.

        Returns:
        -----
        None

        Parameters:
        -----
        centerPoint: MPoint
        	[in] -> the center point of the DiscManip


        '''
        pass

    def setNormal(self, normal: MVector): 
        '''
        setNormal(self, normal: MVector)

        Synopsis
        -----
        Sets the normal of the DiscManip.

        Returns:
        -----
        None

        Parameters:
        -----
        normal: MVector
        	[in] -> the normal of the DiscManip


        '''
        pass

    def setRadius(self, radius: double): 
        '''
        setRadius(self, radius: double)

        Synopsis
        -----
        Sets the radius of the DiscManip.

        Returns:
        -----
        None

        Parameters:
        -----
        radius: double
        	[in] -> the radius of the DiscManip


        '''
        pass

    def setAngle(self, angle: MAngle): 
        '''
        setAngle(self, angle: MAngle)

        Synopsis
        -----
        Sets the angle of the DiscManip.

        Returns:
        -----
        None

        Parameters:
        -----
        angle: MAngle
        	[in] -> the angle of the DiscManip


        '''
        pass

    def centerIndex(self, ReturnStatus: MFnDiscManip.MStatus): 
        '''
        centerIndex(self, ReturnStatus: MFnDiscManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the center of the DiscManip. The data type
        corresponding to this index is MFnNumericData::k3Double.

        Returns: 
        ----- 
        Center index

        Parameters:
        -----
        ReturnStatus: MFnDiscManip.MStatus
        	[out] -> return status


        '''
        pass

    def axisIndex(self, ReturnStatus: MFnDiscManip.MStatus): 
        '''
        axisIndex(self, ReturnStatus: MFnDiscManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the axis of the DiscManip. The data type
        corresponding to this index is MFnNumericData::k3Double.

        Returns: 
        ----- 
        Axis index

        Parameters:
        -----
        ReturnStatus: MFnDiscManip.MStatus
        	[out] -> return status


        '''
        pass

    def angleIndex(self, ReturnStatus: MFnDiscManip.MStatus): 
        '''
        angleIndex(self, ReturnStatus: MFnDiscManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the angle. The data type corresponding to
        this index is a double.

        Returns: 
        ----- 
        Angle index

        Parameters:
        -----
        ReturnStatus: MFnDiscManip.MStatus
        	[out] -> return status


        '''
        pass

class MFnDistanceManip:
    '''DistanceManip function set.
The DistanceManip allows the user to manipulate a point that is
constrained to move along a line. This manipulator generates a
single floating point value. Scaling factors can be used to
determine how int the manipulator appears when it is drawn.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kDistanceManip.Reimplemented from MFnManip3D.

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
        className(self) -> MFnDistanceManip.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnDistanceManip".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def create(self, ReturnStatus: MFnDistanceManip.MStatus): 
        '''
        create(self, ReturnStatus: MFnDistanceManip.MStatus) -> MObject

        Synopsis
        -----
        Creates a new DistanceManip. This function set's object is set to
        be the new manipulator.This method should only be used to create
        a non-composite DistanceManip.The name that appears in the
        feedback line is "Distance"

        Returns: 
        ----- 
        Newly created DistanceManip

        Parameters:
        -----
        ReturnStatus: MFnDistanceManip.MStatus
        	[out] -> return status


        '''
        pass

    @overload
    def create(self, manipName: MString,
                        distanceName: MString,
                        ReturnStatus: MFnDistanceManip.MStatus): 
        '''
        create(self, manipName: MString,
                        distanceName: MString,
                        ReturnStatus: MFnDistanceManip.MStatus) -> MObject

        Synopsis
        -----
        Creates a new DistanceManip. This function set's object is set to
        be the new manipulator.This method should only be used to create
        a non-composite DistanceManip.The name that appears in the
        feedback line is specified by the distanceName argument.

        Returns: 
        ----- 
        Newly created DistanceManip.

        Parameters:
        -----
        manipName: MString
        	[in] -> Name of the manip for UI purposes. 

        distanceName: MString
        	[in] -> Label for the distance value which appears in the feedback line. 

        ReturnStatus: MFnDistanceManip.MStatus
        	[out] -> Status code.


        '''
        pass

    def connectToDistancePlug(self, distancePlug: MPlug): 
        '''
        connectToDistancePlug(self, distancePlug: MPlug)

        Synopsis
        -----
        Connect to the distance plug. The data type corresponding to the
        distancePlug is a double. (Note that MFnUnitAttribute::kDistance
        is used to specify a distance attribute.)

        Returns:
        -----
        None

        Parameters:
        -----
        distancePlug: MPlug
        	[in] -> the distance plug


        '''
        pass

    def setStartPoint(self, startPoint: MPoint): 
        '''
        setStartPoint(self, startPoint: MPoint)

        Synopsis
        -----
        Sets the start point of the DistanceManip.

        Returns:
        -----
        None

        Parameters:
        -----
        startPoint: MPoint
        	[in] -> the start point of the DistanceManip


        '''
        pass

    def setDirection(self, direction: MVector): 
        '''
        setDirection(self, direction: MVector)

        Synopsis
        -----
        Sets the direction of the DistanceManip.

        Returns:
        -----
        None

        Parameters:
        -----
        direction: MVector
        	[in] -> the direction of the DistanceManip


        '''
        pass

    def setDrawStart(self, state: bool): 
        '''
        setDrawStart(self, state: bool)

        Synopsis
        -----
        Sets whether or not to draw the start of the DistanceManip. The
        start of the DistanceManip is indicated by a grey dot. By default
        the start is not drawn.

        Returns:
        -----
        None

        Parameters:
        -----
        state: bool
        	[in] -> whether or not the start should be drawn


        '''
        pass

    def setDrawLine(self, state: bool): 
        '''
        setDrawLine(self, state: bool)

        Synopsis
        -----
        Sets whether or not to draw a line from the start to the end of
        the DistanceManip. By default the line is drawn.

        Returns:
        -----
        None

        Parameters:
        -----
        state: bool
        	[in] -> whether or not the line should be drawn


        '''
        pass

    def setScalingFactor(self, scalingFactor: double): 
        '''
        setScalingFactor(self, scalingFactor: double)

        Synopsis
        -----
        Sets the scaling factor. The scaling factor is used to determine
        how int the DistanceManip appears when it is drawn. The default
        scaling factor is 1.0.

        Returns:
        -----
        None

        Parameters:
        -----
        scalingFactor: double
        	[in] -> the scaling factor


        '''
        pass

    def isDrawStartOn(self, ReturnStatus: MFnDistanceManip.MStatus): 
        '''
        isDrawStartOn(self, ReturnStatus: MFnDistanceManip.MStatus) -> bool

        Synopsis
        -----
        Returns whether or not the start of the DistanceManip is being
        drawn. By default the start is not drawn.

        Returns: 
        ----- 
        true the start of the DistanceManip is being drawn  false the
        start of the DistanceManip is not being drawn

        Parameters:
        -----
        ReturnStatus: MFnDistanceManip.MStatus
        	[out] -> return status


        '''
        pass

    def isDrawLineOn(self, ReturnStatus: MFnDistanceManip.MStatus): 
        '''
        isDrawLineOn(self, ReturnStatus: MFnDistanceManip.MStatus) -> bool

        Synopsis
        -----
        Returns whether or not a line is being drawn from the start to
        the end of the DistanceManip. By default the line is drawn.

        Returns: 
        ----- 
        true the line of the DistanceManip is being drawn  false the line
        of the DistanceManip is not being drawn

        Parameters:
        -----
        ReturnStatus: MFnDistanceManip.MStatus
        	[out] -> return status


        '''
        pass

    def scalingFactor(self, ReturnStatus: MFnDistanceManip.MStatus): 
        '''
        scalingFactor(self, ReturnStatus: MFnDistanceManip.MStatus) -> double

        Synopsis
        -----
        Returns the scaling factor. The scaling factor is used to
        determine how int the DistanceManip appears when it is drawn.

        Returns: 
        ----- 
        Scaling factor

        Parameters:
        -----
        ReturnStatus: MFnDistanceManip.MStatus
        	[out] -> return status


        '''
        pass

    def distanceIndex(self, ReturnStatus: MFnDistanceManip.MStatus): 
        '''
        distanceIndex(self, ReturnStatus: MFnDistanceManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the distance. The data type corresponding to
        this index is a double.

        Returns: 
        ----- 
        Distance index

        Parameters:
        -----
        ReturnStatus: MFnDistanceManip.MStatus
        	[out] -> return status


        '''
        pass

    def directionIndex(self, ReturnStatus: MFnDistanceManip.MStatus): 
        '''
        directionIndex(self, ReturnStatus: MFnDistanceManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the direction. The data type corresponding
        to this index is MFnNumericData::k3Double.

        Returns: 
        ----- 
        Direction index

        Parameters:
        -----
        ReturnStatus: MFnDistanceManip.MStatus
        	[out] -> return status


        '''
        pass

    def startPointIndex(self, ReturnStatus: MFnDistanceManip.MStatus): 
        '''
        startPointIndex(self, ReturnStatus: MFnDistanceManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the start point of the DistanceManip. The
        data type corresponding to this index is
        MFnNumericData::k3Double.

        Returns: 
        ----- 
        Start point index

        Parameters:
        -----
        ReturnStatus: MFnDistanceManip.MStatus
        	[out] -> return status


        '''
        pass

    def currentPointIndex(self, ReturnStatus: MFnDistanceManip.MStatus): 
        '''
        currentPointIndex(self, ReturnStatus: MFnDistanceManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the current point of the DistanceManip. The
        data type corresponding to this index is
        MFnNumericData::k3Double.

        Returns: 
        ----- 
        Current point index

        Parameters:
        -----
        ReturnStatus: MFnDistanceManip.MStatus
        	[out] -> return status


        '''
        pass

class MFnFreePointTriadManip:
    '''FreePointTriadManip function set.
The FreePointTriadManip provides a moveable point, which can be
moved anywhere, and has axes for constrained x, y, and z movement
and obeys grid snapping, point snapping, and curve snapping. The
FreePointTriadManip generates the 3D position of the moveable
point. It is useful for specifying the position of an object in
space.
Note that only the
MFnNumericData::k3Double data type is supported when connecting to a pointPlug via
connectToPointPlug.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kFreePointTriadManip.Reimplemented from MFnManip3D.

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
        className(self) -> MFnFreePointTriadManip.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnFreePointTriadManip".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def create(self, ReturnStatus: MFnFreePointTriadManip.MStatus): 
        '''
        create(self, ReturnStatus: MFnFreePointTriadManip.MStatus) -> MObject

        Synopsis
        -----
        Creates a new FreePointTriadManip. This function set's object is
        set to be the new manipulator.This method should only be used to
        create a non-composite FreePointTriadManip.The name that appears
        in the feedback line is "point"

        Returns: 
        ----- 
        Newly created FreePointTriadManip

        Parameters:
        -----
        ReturnStatus: MFnFreePointTriadManip.MStatus
        	[out] -> return status


        '''
        pass

    @overload
    def create(self, manipName: MString,
                        pointName: MString,
                        ReturnStatus: MFnFreePointTriadManip.MStatus): 
        '''
        create(self, manipName: MString,
                        pointName: MString,
                        ReturnStatus: MFnFreePointTriadManip.MStatus) -> MObject

        Synopsis
        -----
        Creates a new FreePointTriadManip. This function set's object is
        set to be the new manipulator.This method should only be used to
        create a non-composite FreePointTriadManip.The name that appears
        in the feedback line is specified by the pointName argument.

        Returns: 
        ----- 
        Newly created FreePointTriadManip.

        Parameters:
        -----
        manipName: MString
        	[in] -> Name of the manip for UI purposes. 

        pointName: MString
        	[in] -> Label for the position value which appears in the feedback line. 

        ReturnStatus: MFnFreePointTriadManip.MStatus
        	[out] -> Status code.


        '''
        pass

    def connectToPointPlug(self, pointPlug: MPlug): 
        '''
        connectToPointPlug(self, pointPlug: MPlug)

        Synopsis
        -----
        Connect to the point plug. The data type corresponding to the
        pointPlug is MFnNumericData::k3Double.

        Returns:
        -----
        None

        Parameters:
        -----
        pointPlug: MPlug
        	[in] -> the point plug


        '''
        pass

    def setDrawAxes(self, state: bool): 
        '''
        setDrawAxes(self, state: bool)

        Synopsis
        -----
        Sets whether or not to draw the axes of the FreePointTriadManip.
        By default the axes are drawn.

        Returns:
        -----
        None

        Parameters:
        -----
        state: bool
        	[in] -> whether or not the axes should be drawn


        '''
        pass

    def setSnapMode(self, state: bool): 
        '''
        setSnapMode(self, state: bool)

        Synopsis
        -----
        Sets whether or not to the FreePointTriadManip should be in snap
        mode.

        Returns:
        -----
        None

        Parameters:
        -----
        state: bool
        	[in] -> whether or not the FreePointTriadManip should be in snap mode


        '''
        pass

    def setKeyframeAll(self, state: bool): 
        '''
        setKeyframeAll(self, state: bool)

        Synopsis
        -----
        Sets whether or not keyframeAll is on.

        Returns:
        -----
        None

        Parameters:
        -----
        state: bool
        	[in] -> whether or not keyframeAll is on


        '''
        pass

    def setDrawArrowHead(self, state: bool): 
        '''
        setDrawArrowHead(self, state: bool)

        Synopsis
        -----
        Sets whether or not drawArrowHead is on.

        Returns:
        -----
        None

        Parameters:
        -----
        state: bool
        	[in] -> whether or not drawArrowHead is on


        '''
        pass

    def setGlobalTriadPlane(self, whichPlane: MFnFreePointTriadManip.ManipPlane): 
        '''
        setGlobalTriadPlane(self, whichPlane: MFnFreePointTriadManip.ManipPlane)

        Synopsis
        -----
        Sets which plane to use as the global triad plane. The global
        triad plane does not change until the context switches.

        Returns:
        -----
        None

        Parameters:
        -----
        whichPlane: MFnFreePointTriadManip.ManipPlane
        	[in] -> which plane to use as the global triad plane


        '''
        pass

    def setPoint(self, pointValue: MPoint): 
        '''
        setPoint(self, pointValue: MPoint)

        Synopsis
        -----
        Set the point manipulator value to the given vector. This method
        can be called in the MPxManipContainer::connectToDependNode()
        method to set the initial position for the manipulator.

        Returns:
        -----
        None

        Parameters:
        -----
        pointValue: MPoint
        	[in] -> The new value of the point manipValue


        '''
        pass

    def setDirection(self, direction: MVector): 
        '''
        setDirection(self, direction: MVector)

        Synopsis
        -----
        Sets the orientation of the FreePointTriadManip.

        Returns:
        -----
        None

        Parameters:
        -----
        direction: MVector
        	[in] -> the new direction for freePointTriadManip.


        '''
        pass

    def isDrawAxesOn(self, ReturnStatus: MFnFreePointTriadManip.MStatus): 
        '''
        isDrawAxesOn(self, ReturnStatus: MFnFreePointTriadManip.MStatus) -> bool

        Synopsis
        -----
        Returns whether or not the axes of the FreePointTriadManip are
        being drawn. By default the axes are drawn.

        Returns: 
        ----- 
        true the axes of the FreePointTriadManip are being drawn  false
        the axes of the FreePointTriadManip are not being drawn

        Parameters:
        -----
        ReturnStatus: MFnFreePointTriadManip.MStatus
        	[out] -> return status


        '''
        pass

    def isSnapModeOn(self, ReturnStatus: MFnFreePointTriadManip.MStatus): 
        '''
        isSnapModeOn(self, ReturnStatus: MFnFreePointTriadManip.MStatus) -> bool

        Synopsis
        -----
        Returns whether or not the FreePointTriadManip is in snap mode.

        Returns: 
        ----- 
        true the FreePointTriadManip is in snap mode  false the
        FreePointTriadManip is not in snap mode

        Parameters:
        -----
        ReturnStatus: MFnFreePointTriadManip.MStatus
        	[out] -> return status


        '''
        pass

    def isKeyframeAllOn(self, ReturnStatus: MFnFreePointTriadManip.MStatus): 
        '''
        isKeyframeAllOn(self, ReturnStatus: MFnFreePointTriadManip.MStatus) -> bool

        Synopsis
        -----
        Returns whether or not the FreePointTriadManip is in keyframeAll
        mode.

        Returns: 
        ----- 
        true the FreePointTriadManip is in keyframeAll mode  false the
        FreePointTriadManip is not in keyframeAll mode

        Parameters:
        -----
        ReturnStatus: MFnFreePointTriadManip.MStatus
        	[out] -> return status


        '''
        pass

    def pointIndex(self, ReturnStatus: MFnFreePointTriadManip.MStatus): 
        '''
        pointIndex(self, ReturnStatus: MFnFreePointTriadManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the point of the FreePointTriadManip. The
        data type corresponding to this index is
        MFnNumericData::k3Double.

        Returns: 
        ----- 
        Point index

        Parameters:
        -----
        ReturnStatus: MFnFreePointTriadManip.MStatus
        	[out] -> return status


        '''
        pass

class ManipPlane:
    '''Interaction plane for the manip center. 
    Non-functional class.  Values for this enum:
    kYZPlane
    kXZPlane
    kXYPlane
    kViewPlane
    '''

    def __init__(self):
        pass

    def kYZPlane(self):
        '''This is an enum of ManipPlane.
        - Description: Y-Z Plane. 
        - Value: 0
        '''
        pass

    def kXZPlane(self):
        '''This is an enum of ManipPlane.
        - Description: X-Z Plane. 
        - Value: 1
        '''
        pass

    def kXYPlane(self):
        '''This is an enum of ManipPlane.
        - Description: X-Y Plane. 
        - Value: 2
        '''
        pass

    def kViewPlane(self):
        '''This is an enum of ManipPlane.
        - Description: View Plane. 
        - Value: 3
        '''
        pass

class MFnManip3D:
    '''3D manipulator function set
MFnManip3D allows the creation and manipulation of 3D manipulators.
MFnManip3D is the base class from which
MFnFreePointTriadManip,
MFnDirectionManip,
MFnDistanceManip,
MFnPointOnCurveManip,
MFnPointOnSurfaceManip,
MFnDiscManip,
MFnCircleSweepManip,
MFnToggleManip,
MFnStateManip, and
MFnCurveSegmentManip are derived.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kManipulator3D.Reimplemented from MFnTransform.Reimplemented
        in MFnRotateManip, MFnScaleManip, MFnFreePointTriadManip,
        MFnToggleManip, MFnDirectionManip, MFnDistanceManip,
        MFnStateManip, MFnCircleSweepManip, MFnCurveSegmentManip,
        MFnPointOnCurveManip, MFnPointOnSurfaceManip, and MFnDiscManip.

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
        className(self) -> MFnManip3D.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnManip3D".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def isVisible(self, ReturnStatus: MFnManip3D.MStatus): 
        '''
        isVisible(self, ReturnStatus: MFnManip3D.MStatus) -> bool

        Synopsis
        -----
        Returns whether or not the manipulator is visible.

        Returns: 
        ----- 
        true the manipulator is visible  false the manipulator is not
        visible

        Parameters:
        -----
        ReturnStatus: MFnManip3D.MStatus
        	[out] -> return status


        '''
        pass

    def setVisible(self, isVisible: bool): 
        '''
        setVisible(self, isVisible: bool)

        Synopsis
        -----
        Sets whether or not the manipulator is visible.

        Returns:
        -----
        None

        Parameters:
        -----
        isVisible: bool
        	[out] -> whether or not the manipulator is visible


        '''
        pass

    def manipScale(self, ReturnStatus: MFnManip3D.MStatus): 
        '''
        manipScale(self, ReturnStatus: MFnManip3D.MStatus) -> float

        Synopsis
        -----
        Returns the manipulator scale.

        Returns: 
        ----- 
        The manipulator scale

        Parameters:
        -----
        ReturnStatus: MFnManip3D.MStatus
        	[out] -> return status


        '''
        pass

    def setManipScale(self, size: float): 
        '''
        setManipScale(self, size: float)

        Synopsis
        -----
        Sets the manipulator scale.

        Returns:
        -----
        None

        Parameters:
        -----
        size: float
        	[in] -> the manipulator scale


        '''
        pass

    def isOptimizePlaybackOn(self, ReturnStatus: MFnManip3D.MStatus): 
        '''
        isOptimizePlaybackOn(self, ReturnStatus: MFnManip3D.MStatus) -> bool

        Synopsis
        -----
        Returns whether or not optimize playback is on.

        Returns: 
        ----- 
        true optimize playback is on  false optimize playback is off

        Parameters:
        -----
        ReturnStatus: MFnManip3D.MStatus
        	[out] -> return status


        '''
        pass

    def setOptimizePlayback(self, optimizePlayback: bool): 
        '''
        setOptimizePlayback(self, optimizePlayback: bool)

        Synopsis
        -----
        Sets whether or not to optimize the playback.

        Returns:
        -----
        None

        Parameters:
        -----
        optimizePlayback: bool
        	[in] -> whether or not to optimize the playback


        '''
        pass

    def globalSize(self): 
        '''
        globalSize(self) -> float

        Synopsis
        -----
        Returns the global manipulator size.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setGlobalSize(self, size: float): 
        '''
        setGlobalSize(self, size: float)

        Synopsis
        -----
        Sets the global manipulator size.

        Returns:
        -----
        None

        Parameters:
        -----
        size: float
        	[in] -> the global manipulator size 


        '''
        pass

    def handleSize(self): 
        '''
        handleSize(self) -> float

        Synopsis
        -----
        Returns the manipulator handle size.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setHandleSize(self, size: float): 
        '''
        setHandleSize(self, size: float)

        Synopsis
        -----
        Sets the manipulator handle size.

        Returns:
        -----
        None

        Parameters:
        -----
        size: float
        	[in] -> the manipulator handle size 


        '''
        pass

    def lineSize(self): 
        '''
        lineSize(self) -> float

        Synopsis
        -----
        Returns the manipulator line size.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setLineSize(self, size: float): 
        '''
        setLineSize(self, size: float)

        Synopsis
        -----
        Sets the manipulator line size.

        Returns:
        -----
        None

        Parameters:
        -----
        size: float
        	[in] -> the manipulator line size 


        '''
        pass

    def deleteManipulator(self, manip: MObject): 
        '''
        deleteManipulator(self, manip: MObject)

        Synopsis
        -----
        Delete a manipulator. This method should be used to delete
        manipulators that have been created using base manipulator
        create() methods.

        Returns:
        -----
        None

        Parameters:
        -----
        manip: MObject
        	[in] -> the manipulator to be deleted


        '''
        pass

    def drawPlaneHandles(self): 
        '''
        drawPlaneHandles(self) -> bool

        Synopsis
        -----
        This method returns the global option that says if the planar
        manipulator handles should be drawn or not. Setting this will
        affect the drawing of all manipulators that support the planar
        handles.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setDrawPlaneHandles(self, drawPlaneHandles: bool): 
        '''
        setDrawPlaneHandles(self, drawPlaneHandles: bool)

        Synopsis
        -----
        Sets the global option to display planar handles or not on
        supported manipulators.

        Returns:
        -----
        None

        Parameters:
        -----
        drawPlaneHandles: bool
        	[in] -> if the planar handles should be drawn or not. 


        '''
        pass

    def rotateXYZValue(self, valIndex: int,
                        ReturnStatus: MFnManip3D.MStatus): 
        '''
        rotateXYZValue(self, valIndex: int,
                        ReturnStatus: MFnManip3D.MStatus) -> MEulerRotation

        Synopsis
        -----
        Gets the rotation for the active manipulator.

        Returns: 
        ----- 
        Rotate value of the active manip

        Parameters:
        -----
        valIndex: int
        	[in] -> rotation index of the manipulator 

        ReturnStatus: MFnManip3D.MStatus
        	[out] -> return status


        '''
        pass

class MFnPointOnCurveManip:
    '''PointOnCurveManip function set.
The PointOnCurveManip allows the user to manipulate a point
constrained to move along a curve, in order to specify the "u"
curve parameter value. This manipulator generates a single
floating point value corresponding to the curve parameter.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kPointOnCurveManip.Reimplemented from MFnManip3D.

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
        className(self) -> MFnPointOnCurveManip.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnPointOnCurveManip".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def create(self, ReturnStatus: MFnPointOnCurveManip.MStatus): 
        '''
        create(self, ReturnStatus: MFnPointOnCurveManip.MStatus) -> MObject

        Synopsis
        -----
        Creates a new PointOnCurveManip. This function set's object is
        set to be the new manipulator.This method should only be used to
        create a non-composite PointOnCurveManip.The name that appears in
        the feedback line is "param"

        Returns: 
        ----- 
        Newly created PointOnCurveManip

        Parameters:
        -----
        ReturnStatus: MFnPointOnCurveManip.MStatus
        	[out] -> return status


        '''
        pass

    @overload
    def create(self, manipName: MString,
                        paramName: MString,
                        ReturnStatus: MFnPointOnCurveManip.MStatus): 
        '''
        create(self, manipName: MString,
                        paramName: MString,
                        ReturnStatus: MFnPointOnCurveManip.MStatus) -> MObject

        Synopsis
        -----
        Creates a new PointOnCurveManip. This function set's object is
        set to be the new manipulator.This method should only be used to
        create a non-composite PointOnCurveManip.The name that appears in
        the feedback line is specified by the paramName argument.

        Returns: 
        ----- 
        Newly created PointOnCurveManip.

        Parameters:
        -----
        manipName: MString
        	[in] -> Name of the manip for UI purposes. 

        paramName: MString
        	[in] -> Label for the parameter value that appears in the feedback line. 

        ReturnStatus: MFnPointOnCurveManip.MStatus
        	[out] -> Status code.


        '''
        pass

    def connectToCurvePlug(self, curvePlug: MPlug): 
        '''
        connectToCurvePlug(self, curvePlug: MPlug)

        Synopsis
        -----
        Connect to the curve plug. The data type corresponding to the
        curvePlug is MFnData::kNurbsCurve.

        Returns:
        -----
        None

        Parameters:
        -----
        curvePlug: MPlug
        	[in] -> the curve plug


        '''
        pass

    def connectToParamPlug(self, paramPlug: MPlug): 
        '''
        connectToParamPlug(self, paramPlug: MPlug)

        Synopsis
        -----
        Connect to the param plug. The data type corresponding to the
        paramPlug is a double.

        Returns:
        -----
        None

        Parameters:
        -----
        paramPlug: MPlug
        	[in] -> the param plug


        '''
        pass

    def setDrawCurve(self, state: bool): 
        '''
        setDrawCurve(self, state: bool)

        Synopsis
        -----
        Sets whether or not the curve is drawn.

        Returns:
        -----
        None

        Parameters:
        -----
        state: bool
        	[in] -> whether or not the curve should be drawn


        '''
        pass

    def setParameter(self, parameter: double): 
        '''
        setParameter(self, parameter: double)

        Synopsis
        -----
        Sets the parameter.

        Returns:
        -----
        None

        Parameters:
        -----
        parameter: double
        	[in] -> the parameter


        '''
        pass

    def isDrawCurveOn(self, ReturnStatus: MFnPointOnCurveManip.MStatus): 
        '''
        isDrawCurveOn(self, ReturnStatus: MFnPointOnCurveManip.MStatus) -> bool

        Synopsis
        -----
        Returns whether or not the curve is drawn.

        Returns: 
        ----- 
        true the curve is being drawn  false the curve is not being drawn

        Parameters:
        -----
        ReturnStatus: MFnPointOnCurveManip.MStatus
        	[out] -> return status


        '''
        pass

    def parameter(self, ReturnStatus: MFnPointOnCurveManip.MStatus): 
        '''
        parameter(self, ReturnStatus: MFnPointOnCurveManip.MStatus) -> double

        Synopsis
        -----
        Returns the parameter.

        Returns: 
        ----- 
        Parameter

        Parameters:
        -----
        ReturnStatus: MFnPointOnCurveManip.MStatus
        	[out] -> return status


        '''
        pass

    def curvePoint(self, ReturnStatus: MFnPointOnCurveManip.MStatus): 
        '''
        curvePoint(self, ReturnStatus: MFnPointOnCurveManip.MStatus) -> MPoint

        Synopsis
        -----
        Returns the curve point.

        Returns: 
        ----- 
        The curve point

        Parameters:
        -----
        ReturnStatus: MFnPointOnCurveManip.MStatus
        	[out] -> return status


        '''
        pass

    def curveIndex(self, ReturnStatus: MFnPointOnCurveManip.MStatus): 
        '''
        curveIndex(self, ReturnStatus: MFnPointOnCurveManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the curve. The data type corresponding to
        this index is MFnData::kNurbsCurve.

        Returns: 
        ----- 
        Curve index

        Parameters:
        -----
        ReturnStatus: MFnPointOnCurveManip.MStatus
        	[out] -> return status


        '''
        pass

    def paramIndex(self, ReturnStatus: MFnPointOnCurveManip.MStatus): 
        '''
        paramIndex(self, ReturnStatus: MFnPointOnCurveManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the parameter of the PointOnCurveManip. The
        data type corresponding to this index is a double.

        Returns: 
        ----- 
        Parameter index

        Parameters:
        -----
        ReturnStatus: MFnPointOnCurveManip.MStatus
        	[out] -> return status


        '''
        pass

class MFnPointOnSurfaceManip:
    '''PointOnSurfaceManip function set.
The PointOnSurfaceManip allows the user to manipulate a point
constrained to move along a surface, in order to specify the (u,
v) surface parameter values. This manipulator generates two
floating point values corresponding to the surface (u, v)
parameters.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kPointOnSurfaceManip.Reimplemented from MFnManip3D.

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
        className(self) -> MFnPointOnSurfaceManip.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnPointOnSurfaceManip".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def create(self, ReturnStatus: MFnPointOnSurfaceManip.MStatus): 
        '''
        create(self, ReturnStatus: MFnPointOnSurfaceManip.MStatus) -> MObject

        Synopsis
        -----
        Creates a new PointOnSurfaceManip. This function set's object is
        set to be the new manipulator.This method should only be used to
        create a non-composite PointOnSurfaceManip.The name that appears
        in the feedback line is "param"

        Returns: 
        ----- 
        Newly created PointOnSurfaceManip

        Parameters:
        -----
        ReturnStatus: MFnPointOnSurfaceManip.MStatus
        	[out] -> return status


        '''
        pass

    @overload
    def create(self, manipName: MString,
                        paramName: MString,
                        ReturnStatus: MFnPointOnSurfaceManip.MStatus): 
        '''
        create(self, manipName: MString,
                        paramName: MString,
                        ReturnStatus: MFnPointOnSurfaceManip.MStatus) -> MObject

        Synopsis
        -----
        Creates a new PointOnSurfaceManip. This function set's object is
        set to be the new manipulator.This method should only be used to
        create a non-composite PointOnSurfaceManip.The name that appears
        in the feedback line is specified by the paramName argument.

        Returns: 
        ----- 
        Newly created PointOnSurfaceManip.

        Parameters:
        -----
        manipName: MString
        	[in] -> Name of the manip for UI purposes. 

        paramName: MString
        	[in] -> Label for the parameter value which appears in the feedback line 

        ReturnStatus: MFnPointOnSurfaceManip.MStatus
        	[out] -> Status code.


        '''
        pass

    def connectToSurfacePlug(self, surfacePlug: MPlug): 
        '''
        connectToSurfacePlug(self, surfacePlug: MPlug)

        Synopsis
        -----
        Connect to the surface plug. The data type corresponding to the
        surfacePlug is MFnData::kNurbsSurface.

        Returns:
        -----
        None

        Parameters:
        -----
        surfacePlug: MPlug
        	[in] -> the surface plug


        '''
        pass

    def connectToParamPlug(self, paramPlug: MPlug): 
        '''
        connectToParamPlug(self, paramPlug: MPlug)

        Synopsis
        -----
        Connect to the param plug. The data type corresponding to the
        paramPlug is MFnNumericData::k2Double.

        Returns:
        -----
        None

        Parameters:
        -----
        paramPlug: MPlug
        	[in] -> the param plug


        '''
        pass

    def setDrawSurface(self, state: bool): 
        '''
        setDrawSurface(self, state: bool)

        Synopsis
        -----
        Sets whether or not the surface is drawn.

        Returns:
        -----
        None

        Parameters:
        -----
        state: bool
        	[in] -> whether or not the surface should be drawn


        '''
        pass

    def setDrawArrows(self, state: bool): 
        '''
        setDrawArrows(self, state: bool)

        Synopsis
        -----
        Sets whether or not the arrows should be drawn.

        Returns:
        -----
        None

        Parameters:
        -----
        state: bool
        	[in] -> whether or not the arrows should be drawn


        '''
        pass

    def setParameters(self, u: double,
                        v: double): 
        '''
        setParameters(self, u: double,
                        v: double)

        Synopsis
        -----
        Sets the u and v parameters.

        Returns:
        -----
        None

        Parameters:
        -----
        u: double
        	[in] -> u parameter 

        v: double
        	[in] -> v parameter


        '''
        pass

    def getParameters(self, u: double,
                        v: double): 
        '''
        getParameters(self, u: double,
                        v: double)

        Synopsis
        -----
        Returns the parameter.

        Returns:
        -----
        None

        Parameters:
        -----
        u: double
        	[out] -> u parameter 

        v: double
        	[out] -> v parameter


        '''
        pass

    def isDrawSurfaceOn(self, ReturnStatus: MFnPointOnSurfaceManip.MStatus): 
        '''
        isDrawSurfaceOn(self, ReturnStatus: MFnPointOnSurfaceManip.MStatus) -> bool

        Synopsis
        -----
        Returns whether or not the surface is drawn.

        Returns: 
        ----- 
        true the surface is being drawn  false the surface is not being
        drawn

        Parameters:
        -----
        ReturnStatus: MFnPointOnSurfaceManip.MStatus
        	[out] -> return status


        '''
        pass

    def surfaceIndex(self, ReturnStatus: MFnPointOnSurfaceManip.MStatus): 
        '''
        surfaceIndex(self, ReturnStatus: MFnPointOnSurfaceManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the surface. The data type corresponding to
        this index is MFnData::kNurbsSurface.

        Returns: 
        ----- 
        Surface index

        Parameters:
        -----
        ReturnStatus: MFnPointOnSurfaceManip.MStatus
        	[out] -> return status


        '''
        pass

    def paramIndex(self, ReturnStatus: MFnPointOnSurfaceManip.MStatus): 
        '''
        paramIndex(self, ReturnStatus: MFnPointOnSurfaceManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the parameter of the PointOnSurfaceManip.
        The data type corresponding to this index is
        MFnNumericData::k2Double.

        Returns: 
        ----- 
        Parameter index

        Parameters:
        -----
        ReturnStatus: MFnPointOnSurfaceManip.MStatus
        	[out] -> return status


        '''
        pass

class MFnRotateManip:
    '''RotateManip function set.
This class provides access to the built-in Maya rotate
manipulator. The manipulator consists of three constrained-axis
rotation rings, a view rotation ring, as well as an invisible
trackball that allows the user to rotate in arbitrary directions
on the sphere.
The manipulator provides data to the plugin through the rotation
manipVal. The rotation value is a vector consisting of x, y, and
z rotations. Rotations are measured from the initial rotation
(usually <0,0,0>) of the manipulator.
The manipulator can be configured either to display with an
object (which must be a DAG node) or to display at an arbitrary
point using the rotationCenter manipVal.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kRotateManip.Reimplemented from MFnManip3D.

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
        className(self) -> MFnRotateManip.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnRotateManip".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def create(self, ReturnStatus: MFnRotateManip.MStatus): 
        '''
        create(self, ReturnStatus: MFnRotateManip.MStatus) -> MObject

        Synopsis
        -----
        Creates a new RotateManip, and attaches this function set to the
        new manipulator. This method should only be used to create a non-
        composite manipulator, meaning that the manipulator is standalone
        and not part of a container.When the manipulator is being used,
        the feedback line will display a string including "Rotation",
        indicating that this manipulator is in use.

        Returns: 
        ----- 
        An object corresponding to the new manipulator

        Parameters:
        -----
        ReturnStatus: MFnRotateManip.MStatus
        	[in] -> return status


        '''
        pass

    @overload
    def create(self, manipName: MString,
                        rotationName: MString,
                        ReturnStatus: MFnRotateManip.MStatus): 
        '''
        create(self, manipName: MString,
                        rotationName: MString,
                        ReturnStatus: MFnRotateManip.MStatus) -> MObject

        Synopsis
        -----
        Creates a new RotateManip, and attaches this function set to the
        new manipulator. This method should only be used to create a non-
        composite manipulator, meaning that the manipulator is standalone
        and not part of a container.When the manipulator is being used,
        the feedback line will display a string including rotationName,
        indicating that this manipulator is in use.

        Returns: 
        ----- 
        An object corresponding to the new manipulator.

        Parameters:
        -----
        manipName: MString
        	[in] -> Name of the manip for UI purposes. 

        rotationName: MString
        	[in] -> Label for the rotation value displayed in the feedback line. 

        ReturnStatus: MFnRotateManip.MStatus
        	[out] -> Status code.


        '''
        pass

    def connectToRotationPlug(self, rotationPlug: MPlug): 
        '''
        connectToRotationPlug(self, rotationPlug: MPlug)

        Synopsis
        -----
        Create a 1-1 connection from the rotation manipVal to the
        rotationPlug parameter. Any changes to the rotation manipVal will
        be immediately reflected in the connected plug. Connecting to the
        "rotation" plug on a transform node will produce similar behavior
        to the built-in rotate manipulator.The plug must have a data type
        of MFnNumericData::k3Double.

        Returns:
        -----
        None

        Parameters:
        -----
        rotationPlug: MPlug
        	[in] -> The plug to connect the rotation value to


        '''
        pass

    def connectToRotationCenterPlug(self, rotationCenterPlug: MPlug): 
        '''
        connectToRotationCenterPlug(self, rotationCenterPlug: MPlug)

        Synopsis
        -----
        Create a 1-1 association of the rotation center on the
        manipulator and the rotationCenterPlug parameter. When both the
        rotation center is attached to a plug and the displayWithNode()
        method has been called, the manipulator will display with the
        node regardless of the connection made to the rotation center.The
        plug must have a data type of MFnNumericData::k3Double.

        Returns:
        -----
        None

        Parameters:
        -----
        rotationCenterPlug: MPlug
        	[in] -> The plug to connect the rotation center to


        '''
        pass

    def setInitialRotation(self, rotation: MEulerRotation): 
        '''
        setInitialRotation(self, rotation: MEulerRotation)

        Synopsis
        -----
        Sets the initial rotation for the rotate manipulator. Setting the
        initial rotation will prevent the manipulator from jumping back
        to the default rotation when there is already an existing
        rotation on the target plug.

        Returns:
        -----
        None

        Parameters:
        -----
        rotation: MEulerRotation
        	[in] -> The initial rotation


        '''
        pass

    def displayWithNode(self, node: MObject): 
        '''
        displayWithNode(self, node: MObject)

        Synopsis
        -----
        Configures the manipulator to display with the node, causing the
        position of the manipulator to follow the position of the node
        whenever the node is moved. The node must be a DAG object.

        Returns:
        -----
        None

        Parameters:
        -----
        node: MObject
        	[in] -> The node the manipulator should display with


        '''
        pass

    def setRotateMode(self, mode: MFnRotateManip.RotateMode): 
        '''
        setRotateMode(self, mode: MFnRotateManip.RotateMode)

        Synopsis
        -----
        Sets the mode for the rotation manipulator. The manipulator mode
        controls the appearance of the manipulator when is it
        used.ModesThe following modes are supported for the rotation
        manipulator:

        Returns:
        -----
        None

        Parameters:
        -----
        mode: MFnRotateManip.RotateMode
        	[in] -> The new manipulator mode


        '''
        pass

    def rotateMode(self): 
        '''
        rotateMode(self) -> MFnRotateManip.MFnRotateManip

        Synopsis
        -----
        Returns the current rotation mode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setSnapMode(self, snapEnabled: bool): 
        '''
        setSnapMode(self, snapEnabled: bool)

        Synopsis
        -----
        Sets the snap mode. The snap modes can be either on (true) or off
        (false). When snap mode is on, rotation manip values will snap to
        the values within some increment apart.

        Returns:
        -----
        None

        Parameters:
        -----
        snapEnabled: bool
        	[in] -> The new snap mode


        '''
        pass

    def isSnapModeOn(self): 
        '''
        isSnapModeOn(self) -> bool

        Synopsis
        -----
        Returns true when snap mode is on.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setSnapIncrement(self, snapInc: double): 
        '''
        setSnapIncrement(self, snapInc: double)

        Synopsis
        -----
        Sets the snap increment. The snap increment is specified in
        degrees. Manipulator values will snap to the next rotation at an
        angle of snapInc from the original rotation. Note that snap
        rotate does not apply to the trackball rotations (when dragging
        between the rotate discs).

        Returns:
        -----
        None

        Parameters:
        -----
        snapInc: double
        	[in] -> The new snap increment in degrees


        '''
        pass

    def snapIncrement(self): 
        '''
        snapIncrement(self) -> double

        Synopsis
        -----
        Returns the snapping increment in degrees.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def rotationIndex(self, ReturnStatus: MFnRotateManip.MStatus): 
        '''
        rotationIndex(self, ReturnStatus: MFnRotateManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the rotation manipVal for the manipulator.
        When plugToManip conversion functions are used to produce the
        rotation manipVal, the manipulator data must be of the type
        MFnNumericData::k3Double, with X,Y, and Z rotations given in
        radians. This is easily accomplished by using the MEulerRotation
        class to manage the rotations.

        Returns: 
        ----- 
        Rotation index

        Parameters:
        -----
        ReturnStatus: MFnRotateManip.MStatus
        	[out] -> return status


        '''
        pass

    def rotationCenterIndex(self, ReturnStatus: MFnRotateManip.MStatus): 
        '''
        rotationCenterIndex(self, ReturnStatus: MFnRotateManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the rotation center for the manipulator.
        Note that the rotation center is only used for positioning the
        display of the manipulator, and has no effect on the rotation
        values generated by the manipulator.

        Returns: 
        ----- 
        Rotation center index

        Parameters:
        -----
        ReturnStatus: MFnRotateManip.MStatus
        	[out] -> return status


        '''
        pass

    def setRotationCenter(self, rotationCenter: MPoint): 
        '''
        setRotationCenter(self, rotationCenter: MPoint)

        Synopsis
        -----
        Sets the position of the rotation center for the manipulator. The
        value set by this method is ignored if a plug has been connected
        to the rotationCenterPlug. This value is only relevant when there
        is no plug connection to rotationCenterPlug nor node associated
        with the manip (see connectToRotationCenterPlug and
        displayWithNode, respectively).Note that the rotation center is
        only used for positioning the display of the manipulator, and has
        no effect on the rotation values generated by the manipulator.

        Returns:
        -----
        None

        Parameters:
        -----
        rotationCenter: MPoint
        	[in] -> The world space position of the rotation center.


        '''
        pass

class RotateMode:
    '''Manipulator rotation modes. 
    Non-functional class.  Values for this enum:
    kObjectSpace
    kWorldSpace
    kGimbal
    '''

    def __init__(self):
        pass

    def kObjectSpace(self):
        '''This is an enum of RotateMode.
        - Description: Object Space (default) 
        - Value: 0
        '''
        pass

    def kWorldSpace(self):
        '''This is an enum of RotateMode.
        - Description: World Space. 
        - Value: 1
        '''
        pass

    def kGimbal(self):
        '''This is an enum of RotateMode.
        - Description: Gimbal. 
        - Value: 2
        '''
        pass

class MFnScaleManip:
    '''ScaleManip function set.
This class provides access to the built-in Maya scale
manipulator. The manipulator consists of three constrained-axis
scale handles for non-proportional scaling, and a central handle
for proportional scaling.
The manipulator provides data to the plugin through the scale
manipVal. The scale value is a vector consisting of X, Y, and Z
scale values. Each scale value represents a factor controlling
how much an object should be extended along that dimension. The
scale values are absolute and the initial scale value has a
default of <1.0,1.0,1.0>.
The manipulator can be configured either to display with an
object (which must be a DAG node) or to display at an arbitrary
point using the scaleCenter manipVal.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kScaleManip.Reimplemented from MFnManip3D.

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
        className(self) -> MFnScaleManip.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnScaleManip".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def create(self, ReturnStatus: MFnScaleManip.MStatus): 
        '''
        create(self, ReturnStatus: MFnScaleManip.MStatus) -> MObject

        Synopsis
        -----
        Creates a new ScaleManip, and attaches this function set to the
        new manipulator. This method should only be used to create a non-
        composite manipulator, meaning that the manipulator is standalone
        and not part of a container.When the manipulator is being used,
        the feedback line will display a string including "Scale",
        indicating that this manipulator is in use.

        Returns: 
        ----- 
        An object corresponding to the new manipulator

        Parameters:
        -----
        ReturnStatus: MFnScaleManip.MStatus
        	[out] -> return status


        '''
        pass

    @overload
    def create(self, manipName: MString,
                        scaleName: MString,
                        ReturnStatus: MFnScaleManip.MStatus): 
        '''
        create(self, manipName: MString,
                        scaleName: MString,
                        ReturnStatus: MFnScaleManip.MStatus) -> MObject

        Synopsis
        -----
        Creates a new ScaleManip, and attaches this function set to the
        new manipulator. This method should only be used to create a non-
        composite manipulator, meaning that the manipulator is standalone
        and not part of a container.When the manipulator is being used,
        the feedback line will display a string including scaleName,
        indicating that this manipulator is in use.

        Returns: 
        ----- 
        An object corresponding to the new manipulator.

        Parameters:
        -----
        manipName: MString
        	[in] -> Name of the manip for UI purposes. 

        scaleName: MString
        	[in] -> Label for the scale value displayed in the feedback line. 

        ReturnStatus: MFnScaleManip.MStatus
        	[out] -> Status code.


        '''
        pass

    def connectToScalePlug(self, scalePlug: MPlug): 
        '''
        connectToScalePlug(self, scalePlug: MPlug)

        Synopsis
        -----
        Create a 1-1 connection from the scale manipVal to the scalePlug
        parameter. Any changes to the scale manipVal will be immediately
        reflected in the connected plug. Connecting to the "scale" plug
        on a transform node will produce similar behavior to the built-in
        scale manipulator.The plug must have a data type of
        MFnNumericData::k3Double.

        Returns:
        -----
        None

        Parameters:
        -----
        scalePlug: MPlug
        	[in] -> The plug to connect the scale value to


        '''
        pass

    def connectToScaleCenterPlug(self, scaleCenterPlug: MPlug): 
        '''
        connectToScaleCenterPlug(self, scaleCenterPlug: MPlug)

        Synopsis
        -----
        Create a 1-1 association of the scale center on the manipulator
        and the scaleCenterPlug parameter. When both the scale center is
        attached to a plug and the displayWithNode() method has been
        called, the manipulator will display with the node regardless of
        the connection made to the scale center.The plug must have a data
        type of MFnNumericData::k3Double.

        Returns:
        -----
        None

        Parameters:
        -----
        scaleCenterPlug: MPlug
        	[in] -> The plug to connect the scale center to


        '''
        pass

    def setInitialScale(self, scale: MVector): 
        '''
        setInitialScale(self, scale: MVector)

        Synopsis
        -----
        Sets the initial scale for the scale manipulator. Setting the
        initial scale will prevent the manipulator from jumping back to
        the default scale when there is already an existing scale on the
        target plug.

        Returns:
        -----
        None

        Parameters:
        -----
        scale: MVector
        	[in] -> The initial scale


        '''
        pass

    def displayWithNode(self, node: MObject): 
        '''
        displayWithNode(self, node: MObject)

        Synopsis
        -----
        Configures the manipulator to display with the node, causing the
        position of the manipulator to follow the position of the node
        whenever the node is moved. The node must be a DAG object.

        Returns:
        -----
        None

        Parameters:
        -----
        node: MObject
        	[in] -> The node the manipulator should display with


        '''
        pass

    def setSnapMode(self, snapEnabled: bool): 
        '''
        setSnapMode(self, snapEnabled: bool)

        Synopsis
        -----
        Sets the snap mode. The snap modes can be either on (true) or off
        (false). When snap mode is on, scale values will snap to scale
        value within some interval apart. The interval is set using
        setSnapIncrement().

        Returns:
        -----
        None

        Parameters:
        -----
        snapEnabled: bool
        	[in] -> The new snap mode


        '''
        pass

    def isSnapModeOn(self): 
        '''
        isSnapModeOn(self) -> bool

        Synopsis
        -----
        Returns true when snap mode is on.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setSnapIncrement(self, snapInc: double): 
        '''
        setSnapIncrement(self, snapInc: double)

        Synopsis
        -----
        Sets the snap increment. The snap increment is specified in the
        working unit, and is the distance between snap points when
        dragging the scale handles.

        Returns:
        -----
        None

        Parameters:
        -----
        snapInc: double
        	[in] -> The new snap increment


        '''
        pass

    def snapIncrement(self): 
        '''
        snapIncrement(self) -> double

        Synopsis
        -----
        Returns the snapping increment in working units.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setOrientation(self, orientation: MEulerRotation): 
        '''
        setOrientation(self, orientation: MEulerRotation)

        Synopsis
        -----
        Sets the arbitrary orientation of the MFnScaleManip. This only
        has any effect when the orientation mode is set to
        kArbitraryOrientation

        Returns:
        -----
        None

        Parameters:
        -----
        orientation: MEulerRotation
        	[in] -> the new orientation for 


        '''
        pass

    def getOrientation(self, ReturnStatus: MFnScaleManip.MStatus): 
        '''
        getOrientation(self, ReturnStatus: MFnScaleManip.MStatus) -> MEulerRotation

        Synopsis
        -----
        Returns the orientation used by the manip when its
        orientationMode is set to kArbitraryOrientation.

        Returns: 
        ----- 
        Current orientation direction of the manip

        Parameters:
        -----
        ReturnStatus: MFnScaleManip.MStatus
        	[out] -> return status


        '''
        pass

    def setOrientationMode(self, mode: MFnScaleManip.ScaleOrientationMode): 
        '''
        setOrientationMode(self, mode: MFnScaleManip.ScaleOrientationMode)

        Synopsis
        -----
        Sets the orientation mode of the MFnScaleManip. When the
        manipulator's orientationMode is set to kArbitraryOrientation the
        manipulator will be oriented according to the value set by
        setOrientation(). When the orientationMode is set to
        kDefaultOrientation the manipulator will be aligned with the
        world-space axes.

        Returns:
        -----
        None

        Parameters:
        -----
        mode: MFnScaleManip.ScaleOrientationMode
        	[in] -> the new orientation mode of the 


        '''
        pass

    def getOrientationMode(self, ReturnStatus: MFnScaleManip.MStatus): 
        '''
        getOrientationMode(self, ReturnStatus: MFnScaleManip.MStatus) -> MFnScaleManip.MFnScaleManip

        Synopsis
        -----
        Gets the orientation mode of the MFnScaleManip.

        Returns: 
        ----- 
        current orientation mode of the manip

        Parameters:
        -----
        ReturnStatus: MFnScaleManip.MStatus
        	[out] -> return status


        '''
        pass

    def scaleIndex(self, ReturnStatus: MFnScaleManip.MStatus): 
        '''
        scaleIndex(self, ReturnStatus: MFnScaleManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the scale manipVal for this manipulator.

        Returns: 
        ----- 
        Scale index

        Parameters:
        -----
        ReturnStatus: MFnScaleManip.MStatus
        	[out] -> return status


        '''
        pass

    def scaleCenterIndex(self, ReturnStatus: MFnScaleManip.MStatus): 
        '''
        scaleCenterIndex(self, ReturnStatus: MFnScaleManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the scale center manipVal for this
        manipulator. Note that the scale center is only used for display
        of the manipulator and has no effect on scale values produced by
        the manipulator.

        Returns: 
        ----- 
        Scale center index

        Parameters:
        -----
        ReturnStatus: MFnScaleManip.MStatus
        	[out] -> return status


        '''
        pass

class MFnStateManip:
    '''StateManip function set.
The StateManip allows the user to switch between multiple states.
It is drawn as a circle with a notch. Each click on the circle
increments the value of the state (modulo the maximum number of
states). This manipulator generates an integer value
corresponding to the state of the manip.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kStateManip.Reimplemented from MFnManip3D.

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
        className(self) -> MFnStateManip.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnStateManip".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def create(self, ReturnStatus: MFnStateManip.MStatus): 
        '''
        create(self, ReturnStatus: MFnStateManip.MStatus) -> MObject

        Synopsis
        -----
        Creates a new StateManip. This function set's object is set to be
        the new manipulator.This method should only be used to create a
        non-composite StateManip.The name that appears in the feedback
        line is "state"

        Returns: 
        ----- 
        Newly created StateManip

        Parameters:
        -----
        ReturnStatus: MFnStateManip.MStatus
        	[out] -> return status


        '''
        pass

    @overload
    def create(self, manipName: MString,
                        stateName: MString,
                        ReturnStatus: MFnStateManip.MStatus): 
        '''
        create(self, manipName: MString,
                        stateName: MString,
                        ReturnStatus: MFnStateManip.MStatus) -> MObject

        Synopsis
        -----
        Creates a new StateManip. This function set's object is set to be
        the new manipulator.This method should only be used to create a
        non-composite StateManip.The name that appears in the feedback
        line is specified by the stateName argument.

        Returns: 
        ----- 
        Newly created StateManip

        Parameters:
        -----
        manipName: MString
        	[in] -> Name of the manip for UI purposes. 

        stateName: MString
        	[in] -> Label for the state value which appears in the feedback line. 

        ReturnStatus: MFnStateManip.MStatus
        	[out] -> Status code.


        '''
        pass

    def connectToStatePlug(self, statePlug: MPlug): 
        '''
        connectToStatePlug(self, statePlug: MPlug)

        Synopsis
        -----
        Connect to the state plug. The data type corresponding to the
        statePlug is a int integer.

        Returns:
        -----
        None

        Parameters:
        -----
        statePlug: MPlug
        	[in] -> the state plug


        '''
        pass

    def setInitialState(self, initialState: int): 
        '''
        setInitialState(self, initialState: int)

        Synopsis
        -----
        Sets the initial state of the StateManip.

        Returns:
        -----
        None

        Parameters:
        -----
        initialState: int
        	[in] -> initial state of the StateManip


        '''
        pass

    def setMaxStates(self, numStates: int): 
        '''
        setMaxStates(self, numStates: int)

        Synopsis
        -----
        Sets the maximum number of states that the StateManip will have.
        The default number of maximum states is 4.

        Returns:
        -----
        None

        Parameters:
        -----
        numStates: int
        	[in] -> the maxiumum number of states


        '''
        pass

    def maxStates(self, ReturnStatus: MFnStateManip.MStatus): 
        '''
        maxStates(self, ReturnStatus: MFnStateManip.MStatus) -> int

        Synopsis
        -----
        Returns the number of maximum states.

        Returns: 
        ----- 
        Maximum states

        Parameters:
        -----
        ReturnStatus: MFnStateManip.MStatus
        	[out] -> return status


        '''
        pass

    def state(self, ReturnStatus: MFnStateManip.MStatus): 
        '''
        state(self, ReturnStatus: MFnStateManip.MStatus) -> int

        Synopsis
        -----
        Returns the current state.

        Returns: 
        ----- 
        Current states

        Parameters:
        -----
        ReturnStatus: MFnStateManip.MStatus
        	[out] -> return status


        '''
        pass

    def positionIndex(self, ReturnStatus: MFnStateManip.MStatus): 
        '''
        positionIndex(self, ReturnStatus: MFnStateManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the position of the StateManip. The data
        type corresponding to this index is MFnNumericData::k3Double.

        Returns: 
        ----- 
        Position index

        Parameters:
        -----
        ReturnStatus: MFnStateManip.MStatus
        	[out] -> return status


        '''
        pass

    def stateIndex(self, ReturnStatus: MFnStateManip.MStatus): 
        '''
        stateIndex(self, ReturnStatus: MFnStateManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the state. The data type corresponding to
        this index is a int integer.

        Returns: 
        ----- 
        State index

        Parameters:
        -----
        ReturnStatus: MFnStateManip.MStatus
        	[out] -> return status


        '''
        pass

class MFnToggleManip:
    '''ToggleManip function set.
The ToggleManip allows the user to switch between two modes or
some on/off state. It is drawn as a circle with or without a dot.
When the mode is on, the dot is drawn in the circle; when the
mode is off, the circle is drawn without the dot. This
manipulator generates a boolean value corresponding to whether or
not the mode is on or off.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kToggleManip.Reimplemented from MFnManip3D.

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
        className(self) -> MFnToggleManip.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnToggleManip".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def create(self, ReturnStatus: MFnToggleManip.MStatus): 
        '''
        create(self, ReturnStatus: MFnToggleManip.MStatus) -> MObject

        Synopsis
        -----
        Creates a new ToggleManip. This function set's object is set to
        be the new manipulator.This method should only be used to create
        a non-composite ToggleManip.The name that appears in the feedback
        line is "toggle"

        Returns: 
        ----- 
        Newly created ToggleManip

        Parameters:
        -----
        ReturnStatus: MFnToggleManip.MStatus
        	[out] -> return status


        '''
        pass

    @overload
    def create(self, manipName: MString,
                        toggleName: MString,
                        ReturnStatus: MFnToggleManip.MStatus): 
        '''
        create(self, manipName: MString,
                        toggleName: MString,
                        ReturnStatus: MFnToggleManip.MStatus) -> MObject

        Synopsis
        -----
        Creates a new ToggleManip. This function set's object is set to
        be the new manipulator.This method should only be used to create
        a non-composite ToggleManip.The name that appears in the feedback
        line is specified by the toggleName argument.

        Returns: 
        ----- 
        Newly created ToggleManip.

        Parameters:
        -----
        manipName: MString
        	[in] -> Name of the manip for UI purposes. 

        toggleName: MString
        	[in] -> Label for the toggle value which appears in the feedback line. 

        ReturnStatus: MFnToggleManip.MStatus
        	[out] -> Status code.


        '''
        pass

    def connectToTogglePlug(self, togglePlug: MPlug): 
        '''
        connectToTogglePlug(self, togglePlug: MPlug)

        Synopsis
        -----
        Connect to the toggle plug. The data type corresponding to the
        togglePlug is a boolean value.

        Returns:
        -----
        None

        Parameters:
        -----
        togglePlug: MPlug
        	[in] -> the toggle plug


        '''
        pass

    def startPoint(self, ReturnStatus: MFnToggleManip.MStatus): 
        '''
        startPoint(self, ReturnStatus: MFnToggleManip.MStatus) -> MPoint

        Synopsis
        -----
        Returns the start point.

        Returns: 
        ----- 
        The start point

        Parameters:
        -----
        ReturnStatus: MFnToggleManip.MStatus
        	[out] -> return status


        '''
        pass

    def direction(self, ReturnStatus: MFnToggleManip.MStatus): 
        '''
        direction(self, ReturnStatus: MFnToggleManip.MStatus) -> MVector

        Synopsis
        -----
        Returns the direction.

        Returns: 
        ----- 
        The direction

        Parameters:
        -----
        ReturnStatus: MFnToggleManip.MStatus
        	[out] -> return status


        '''
        pass

    def length(self, ReturnStatus: MFnToggleManip.MStatus): 
        '''
        length(self, ReturnStatus: MFnToggleManip.MStatus) -> double

        Synopsis
        -----
        Returns the length.

        Returns: 
        ----- 
        Length

        Parameters:
        -----
        ReturnStatus: MFnToggleManip.MStatus
        	[out] -> return status


        '''
        pass

    def toggle(self, ReturnStatus: MFnToggleManip.MStatus): 
        '''
        toggle(self, ReturnStatus: MFnToggleManip.MStatus) -> bool

        Synopsis
        -----
        Returns the toggle.

        Returns: 
        ----- 
        Toggle

        Parameters:
        -----
        ReturnStatus: MFnToggleManip.MStatus
        	[out] -> return status


        '''
        pass

    def startPointIndex(self, ReturnStatus: MFnToggleManip.MStatus): 
        '''
        startPointIndex(self, ReturnStatus: MFnToggleManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the start point of the ToggleManip. The data
        type corresponding to this index is MFnNumericData::k3Double.

        Returns: 
        ----- 
        Start point index

        Parameters:
        -----
        ReturnStatus: MFnToggleManip.MStatus
        	[out] -> return status


        '''
        pass

    def directionIndex(self, ReturnStatus: MFnToggleManip.MStatus): 
        '''
        directionIndex(self, ReturnStatus: MFnToggleManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the direction. The data type corresponding
        to this index is MFnNumericData::k3Double.

        Returns: 
        ----- 
        Direction index

        Parameters:
        -----
        ReturnStatus: MFnToggleManip.MStatus
        	[out] -> return status


        '''
        pass

    def lengthIndex(self, ReturnStatus: MFnToggleManip.MStatus): 
        '''
        lengthIndex(self, ReturnStatus: MFnToggleManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the length of the ToggleManip. The data type
        corresponding to this index is a double.

        Returns: 
        ----- 
        Length index

        Parameters:
        -----
        ReturnStatus: MFnToggleManip.MStatus
        	[out] -> return status


        '''
        pass

    def toggleIndex(self, ReturnStatus: MFnToggleManip.MStatus): 
        '''
        toggleIndex(self, ReturnStatus: MFnToggleManip.MStatus) -> int

        Synopsis
        -----
        Returns the index of the toggle of the ToggleManip. The data type
        corresponding to this index is a boolean.

        Returns: 
        ----- 
        Toggle index

        Parameters:
        -----
        ReturnStatus: MFnToggleManip.MStatus
        	[out] -> return status


        '''
        pass

    def setStartPoint(self, startPoint: MPoint): 
        '''
        setStartPoint(self, startPoint: MPoint)

        Synopsis
        -----
        Sets the start point of the ToggleManip.

        Returns:
        -----
        None

        Parameters:
        -----
        startPoint: MPoint
        	[in] -> the start point of the ToggleManip


        '''
        pass

    def setDirection(self, direction: MVector): 
        '''
        setDirection(self, direction: MVector)

        Synopsis
        -----
        Sets the direction of the ToggleManip.

        Returns:
        -----
        None

        Parameters:
        -----
        direction: MVector
        	[in] -> the direction of the ToggleManip


        '''
        pass

    def setLength(self, length: double): 
        '''
        setLength(self, length: double)

        Synopsis
        -----
        Sets the length of the ToggleManip.

        Returns:
        -----
        None

        Parameters:
        -----
        length: double
        	[in] -> the length of the ToggleManip


        '''
        pass

    def setToggle(self, toggle: bool): 
        '''
        setToggle(self, toggle: bool)

        Synopsis
        -----
        Sets the toggle of the ToggleManip.

        Returns:
        -----
        None

        Parameters:
        -----
        toggle: bool
        	[in] -> the toggle of the ToggleManip


        '''
        pass

class MGraphEditorInfo:
    '''Graph Editor state information with manipulation capabilities.
This class provides methods to obtain UI related information from
a specific Graph Editor. Support is included for
obtaining/setting viewport bounds and obtaining animation curve
nodes.
Note: the following are built-in GraphEditor-specific event
callback names:
 (getting the names of the curves selected in the default Graph
Editor)
 (getting the default Graph Editor's viewport bounds when it
encounters a refresh event)
 (setting the default Graph Editor's viewport bounds)
'''
    def __init__(self):
        pass


    def getAnimCurveNodes(self, animCurveNodeArray: MObjectArray,
                        animCurveQuery: MGraphEditorInfo.AnimCurveQuery): 
        '''
        getAnimCurveNodes(self, animCurveNodeArray: MObjectArray,
                        animCurveQuery: MGraphEditorInfo.AnimCurveQuery)

        Synopsis
        -----
        Returns an array of animCurve nodes, based on the attached Graph
        Editor's state information, which captures: 1) animCurve nodes
        present in the Outliner, but not visible in the viewport 2)
        animCurve nodes highlighted in the Outliner and visible in the
        viewport 3) animCurve nodes selected (via keys/tangent handles)
        in the viewport 4) animCurve nodes known to exist (independent of
        any Outliner filtering)

        Returns:
        -----
        None

        Parameters:
        -----
        animCurveNodeArray: MObjectArray
        	[out] -> an array to store the found anim curves 

        animCurveQuery: MGraphEditorInfo.AnimCurveQuery
        	[in] -> the anim curves to enumerate (by display state)


        '''
        pass

    def isStackedViewportMode(self): 
        '''
        isStackedViewportMode(self) -> bool

        Synopsis
        -----
        Returns whether or not the Graph Editor is in Stacked view mode.
        return true if the Graph Editor is in Stacked view mode; false
        otherwise

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def isNormalizedViewportMode(self): 
        '''
        isNormalizedViewportMode(self) -> bool

        Synopsis
        -----
        Returns whether or not the Graph Editor is in Normalized view
        mode. return true if the Graph Editor is in a Normalized view
        mode. NOTE: Stacked mode also uses Normalized mode. So this
        method returns true in Stacked mode, as well; false if not in
        Stacked -nor- Normalized modes.

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

class AnimCurveQuery:
    '''Defines the query criteria for animation curves specifically with respect to the attached Graph Editor's own viewport. 
    Non-functional class.  Values for this enum:
    kAnimCurveOutlinerOnly
    kAnimCurveHighlighted
    kAnimCurveSelected
    kAnimCurveAllKnown
    '''

    def __init__(self):
        pass

    def kAnimCurveOutlinerOnly(self):
        '''This is an enum of AnimCurveQuery.
        - Description: Curve(s) present in Outliner (but not visible in the viewport). Note: this is not currently supported 
        - Value: 0
        '''
        pass

    def kAnimCurveHighlighted(self):
        '''This is an enum of AnimCurveQuery.
        - Description: Curve(s) highlighted in Outliner (and visible in the viewport) 
        - Value: 1
        '''
        pass

    def kAnimCurveSelected(self):
        '''This is an enum of AnimCurveQuery.
        - Description: Curve(s) selected (via keys/tangent handles) in the viewport. 
        - Value: 2
        '''
        pass

    def kAnimCurveAllKnown(self):
        '''This is an enum of AnimCurveQuery.
        - Description: Curve(s) known to exist (independent of any Outliner filtering) 
        - Value: 3
        '''
        pass

class MHWShaderSwatchGenerator:
    '''Hardware shader swatch generator utility class.
Derived from the
MSwatchRenderBase class as a utility for generating a swatch for a plugin hardware
shader class. This class supports hardware shaders derived from
both
MPxHardwareShader and the older
MPxHwShaderNode base classes.
'''
    def __init__(self):
        pass


    def initialize(self): 
        '''
        initialize(self) -> const MString&

        Synopsis
        -----
        This method sets a swatch name, and registers a new swatch
        generator creation function for the swatch name. The string
        returned from this method can be used for node classification
        purpose.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getSwatchBackgroundColor(self, r: float,
                        g: float,
                        b: float,
                        a: float): 
        '''
        getSwatchBackgroundColor(self, r: float,
                        g: float,
                        b: float,
                        a: float)

        Synopsis
        -----
        This method returns the default background color for the hardware
        rendered swatch.

        Returns:
        -----
        None

        Parameters:
        -----
        r: float
        	[out] -> Storage variable for red component. 

        g: float
        	[out] -> Storage variable for green component. 

        b: float
        	[out] -> Storage variable for blue component. 

        a: float
        	[out] -> Storage variable for alpha component. 


        '''
        pass

    def doIteration(self): 
        '''
        doIteration(self) -> bool

        Synopsis
        -----
        This method will be called from the MSwatchRenderRegister for
        generating a swatch image. This doIteration function is called
        repeatedly (during idle events) till it returns true.
        Reimplemented from MSwatchRenderBase.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MManipData:
    '''Manipulator Data.
This class encapulates manipulator data which is returned from
the manipulator conversion functions.
MManipData is used to represent data that is either simple or complex.
Simple data is used to represent bool, short, int, unsigned int,
float, and double types. Complex data is used to represent
MObjects created by
MFnData, or classes derived from
MFnData.
'''
    def __init__(self):
        pass


    def isSimple(self): 
        '''
        isSimple(self) -> bool

        Synopsis
        -----
        Returns whether or not the manipulator data is simple or complex.
        Simple data is used to represent bool, short, int, unsigned int,
        float, and double types. Complex data is used to represent
        MObjects created by MFnData, or classes derived from MFnData.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def asBool(self): 
        '''
        asBool(self) -> bool

        Synopsis
        -----
        Returns the manipulator data as a bool.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def asShort(self): 
        '''
        asShort(self) -> short

        Synopsis
        -----
        Returns the manipulator data as a short.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def asLong(self): 
        '''
        asLong(self) -> int

        Synopsis
        -----
        Returns the manipulator data as a int.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def asUnsigned(self): 
        '''
        asUnsigned(self) -> int

        Synopsis
        -----
        Returns the manipulator data as an unsigned int.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def asFloat(self): 
        '''
        asFloat(self) -> float

        Synopsis
        -----
        Returns the manipulator data as a float.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def asDouble(self): 
        '''
        asDouble(self) -> double

        Synopsis
        -----
        Returns the manipulator data as a double.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def asMObject(self): 
        '''
        asMObject(self) -> MObject

        Synopsis
        -----
        Returns the manipulator data as an MObject. The MObjects returned
        from this method are created and used by MFnData or classes
        derived from MFnData.

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

class MMaterial:
    '''This class is used in the draw functions of user defined shapes
(see
MPxSurfaceShapeUI) for setting up and querying materials used in shaded mode
drawing.
'''
    def __init__(self):
        pass


    def evaluateMaterial(self, view: M3dView,
                        path: MDagPath): 
        '''
        evaluateMaterial(self, view: M3dView,
                        path: MDagPath)

        Synopsis
        -----
        Evaluate a material. Must be called before evaluating or getting
        any material properties.

        Returns:
        -----
        None

        Parameters:
        -----
        view: M3dView
        	[in] -> the view 

        path: MDagPath
        	[in] -> path to the object


        '''
        pass

    def evaluateShininess(self): 
        '''
        evaluateShininess(self)

        Synopsis
        -----
        Perform necessary evaluation to be able to get shininess back.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def evaluateDiffuse(self): 
        '''
        evaluateDiffuse(self)

        Synopsis
        -----
        Perform necessary evaluation to be able to get diffuse back.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def evaluateEmission(self): 
        '''
        evaluateEmission(self)

        Synopsis
        -----
        Perform necessary evaluation to be able to get emission back.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def evaluateSpecular(self): 
        '''
        evaluateSpecular(self)

        Synopsis
        -----
        Perform necessary evaluation to be able to get specular back.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def evaluateTexture(self, data: MDrawData): 
        '''
        evaluateTexture(self, data: MDrawData)

        Synopsis
        -----
        Evaluate texturing related information. Must be called before
        getting any texture properties such as getHasTransparency(),
        getTextureTransformation() and applyTexture().This method should
        be called from MPxSurfaceShapeUI::getDrawRequests. The draw data
        argument is the MDrawData for the request that will carry the
        texture information to the MPxSurfaceShapeUI::draw method.

        Returns:
        -----
        None

        Parameters:
        -----
        data: MDrawData
        	[in] -> draw request data to carry the texture information


        '''
        pass

    def materialIsTextured(self): 
        '''
        materialIsTextured(self) -> bool

        Synopsis
        -----
        Do we have a texture (evaluated or not).

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setMaterial(self, path: MDagPath,
                        hasTransparency: bool): 
        '''
        setMaterial(self, path: MDagPath,
                        hasTransparency: bool)

        Synopsis
        -----
        Set the current GL material.

        Returns:
        -----
        None

        Parameters:
        -----
        path: MDagPath
        	[in] -> path to the object 

        hasTransparency: bool
        	[in] -> whether the material has transparency


        '''
        pass

    def getShininess(self, value: float): 
        '''
        getShininess(self, value: float)

        Synopsis
        -----
        Get the GL shininess.

        Returns:
        -----
        None

        Parameters:
        -----
        value: float
        	[out] -> storage for shininess


        '''
        pass

    def getDiffuse(self, color: MColor): 
        '''
        getDiffuse(self, color: MColor)

        Synopsis
        -----
        Get the GL diffuse color.

        Returns:
        -----
        None

        Parameters:
        -----
        color: MColor
        	[out] -> storage for the diffuse color


        '''
        pass

    def getEmission(self, color: MColor): 
        '''
        getEmission(self, color: MColor)

        Synopsis
        -----
        Get the GL emission color.

        Returns:
        -----
        None

        Parameters:
        -----
        color: MColor
        	[out] -> storage for the emission color


        '''
        pass

    def getSpecular(self, color: MColor): 
        '''
        getSpecular(self, color: MColor)

        Synopsis
        -----
        Get the GL specular color.

        Returns:
        -----
        None

        Parameters:
        -----
        color: MColor
        	[out] -> storage for the specular color


        '''
        pass

    def getHasTransparency(self, value: bool): 
        '''
        getHasTransparency(self, value: bool)

        Synopsis
        -----
        Determine if material or texture has transparency.

        Returns:
        -----
        None

        Parameters:
        -----
        value: bool
        	[out] -> True if material or texture has transparency, false otherwise.


        '''
        pass

    @overload
    def getTextureTransformation(self, data: MDrawData,
                        texXform: MMatrix): 
        '''
        getTextureTransformation(self, data: MDrawData,
                        texXform: MMatrix)

        Synopsis
        -----
        Get the current textures transformation.

        Returns:
        -----
        None

        Parameters:
        -----
        data: MDrawData
        	[in] -> the draw data from the draw request 

        texXform: MMatrix
        	[out] -> storage for the texture transformation


        '''
        pass

    @overload
    def getTextureTransformation(self, data: MDrawData,
                        rotateUV: float,
                        scaleU: float,
                        scaleV: float,
                        translateU: float,
                        translateV: float,
                        rotateFrame: float): 
        '''
        getTextureTransformation(self, data: MDrawData,
                        rotateUV: float,
                        scaleU: float,
                        scaleV: float,
                        translateU: float,
                        translateV: float,
                        rotateFrame: float)

        Synopsis
        -----
        Get the current textures transformation. The transformations
        should applied in the following order:

        Returns:
        -----
        None

        Parameters:
        -----
        data: MDrawData
        	[in] -> the draw data from the draw request 

        rotateUV: float
        	[out] -> storage for rotatation value of the UV coordinates 

        scaleU: float
        	[out] -> storage for u scale value 

        scaleV: float
        	[out] -> storage for v scale value 

        translateU: float
        	[out] -> storage for u translation value 

        translateV: float
        	[out] -> storage for v translation value 

        rotateFrame: float
        	[out] -> storage for rotatation value of the frame coordinates


        '''
        pass

    def applyTexture(self, view: M3dView,
                        data: MDrawData): 
        '''
        applyTexture(self, view: M3dView,
                        data: MDrawData)

        Synopsis
        -----
        For materials that have texture, this method must be used before
        the OpenGL drawing to apply the texture to the current view. This
        method should be called from within your MPxSurfaceShapeUI::draw
        method.

        Returns:
        -----
        None

        Parameters:
        -----
        view: M3dView
        	[in] -> the view in which the textured drawing is to take place 

        data: MDrawData
        	[in] -> the draw data from the draw request 


        '''
        pass

    def textureImage(self, image: MImage,
                        color: MColor,
                        chan: MMaterial.MtextureChannel,
                        mapped: bool,
                        dagPath: MDagPath,
                        xRes: int,
                        yRes: int): 
        '''
        textureImage(self, image: MImage,
                        color: MColor,
                        chan: MMaterial.MtextureChannel,
                        mapped: bool,
                        dagPath: MDagPath,
                        xRes: int,
                        yRes: int)

        Synopsis
        -----
        For materials that have texture, this method will attempt to
        retrieve the pixel map for a given mapped channel of that
        material. If the channel is not mapped than a status of failure
        will be returned.The material types that can be queried
        include:Currently only channels mapped to single file textures is
        supported.

        Returns:
        -----
        None

        Parameters:
        -----
        image: MImage
        	[out] -> The image retrieved. If no image could be retrieve, the value will not change. 

        color: MColor
        	[out] -> Either the mapped or unmapped color. If the channel is mapped then an RGBA value of (1,1,1,1) will be returned, otherwise the unmapped channel's current color value will be returned. 

        chan: MMaterial.MtextureChannel
        	[in] -> Texture channel to check. 

        mapped: bool
        	[out] -> Whether the channel is mapped or not (true or false) 

        dagPath: MDagPath
        	[in] -> Optional dag path to object. An object path is required to produce texture maps from non-2D procedural textures. 

        xRes: int
        	[in] -> Optional width of image to create. The minimal allowed value is 2. This parameter only applies to procedural textures. The dimension in X will be 128 by default, if a value less than 2 is specified. 

        yRes: int
        	[in] -> Optional height of image to create. The minimal allowed value is 2. This parameter only applies to procedural textures. The dimension in Y will be 128 by default, if a value less than 2 is specified.


        '''
        pass

    def defaultMaterial(self): 
        '''
        defaultMaterial(self) -> MMaterial

        Synopsis
        -----
        Get the default material. There will always be a default material
        in the scene and therefore the result of this function should
        always succeed. The default material will correspond to the
        initialShadingGroup node that is in the scene.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def shadingEngine(self): 
        '''
        shadingEngine(self) -> MObject

        Synopsis
        -----
        Get the shading engined associated with this material.

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

class MtextureChannel:
    '''Channels which can be queried. 
    Non-functional class.  Values for this enum:
    kColor
    kTransparency
    kAmbientColor
    kIncandescence
    kBumpMap
    kDiffuse
    kTransluscence
    kRoughness
    kHighlightSize
    kWhiteness
    kCosinePower
    kEccentricity
    kSpecularRollOff
    kSpecularColor
    kReflectivity
    kReflectedColor
    '''

    def __init__(self):
        pass

    def kColor(self):
        '''This is an enum of MtextureChannel.
        - Description: nop 
        - Value: 0
        '''
        pass

    def kTransparency(self):
        '''This is an enum of MtextureChannel.
        - Description:  
        - Value: 1
        '''
        pass

    def kAmbientColor(self):
        '''This is an enum of MtextureChannel.
        - Description:  
        - Value: 2
        '''
        pass

    def kIncandescence(self):
        '''This is an enum of MtextureChannel.
        - Description:  
        - Value: 3
        '''
        pass

    def kBumpMap(self):
        '''This is an enum of MtextureChannel.
        - Description:  
        - Value: 4
        '''
        pass

    def kDiffuse(self):
        '''This is an enum of MtextureChannel.
        - Description:  
        - Value: 5
        '''
        pass

    def kTransluscence(self):
        '''This is an enum of MtextureChannel.
        - Description:  
        - Value: 6
        '''
        pass

    def kRoughness(self):
        '''This is an enum of MtextureChannel.
        - Description: PhongE only. 
        - Value: 7
        '''
        pass

    def kHighlightSize(self):
        '''This is an enum of MtextureChannel.
        - Description: PhongE only. 
        - Value: 8
        '''
        pass

    def kWhiteness(self):
        '''This is an enum of MtextureChannel.
        - Description: PhongE only. 
        - Value: 9
        '''
        pass

    def kCosinePower(self):
        '''This is an enum of MtextureChannel.
        - Description: Phong only. 
        - Value: 10
        '''
        pass

    def kEccentricity(self):
        '''This is an enum of MtextureChannel.
        - Description: Blinn only. 
        - Value: 11
        '''
        pass

    def kSpecularRollOff(self):
        '''This is an enum of MtextureChannel.
        - Description: Blinn only. 
        - Value: 12
        '''
        pass

    def kSpecularColor(self):
        '''This is an enum of MtextureChannel.
        - Description: Blinn and Phong(E) only. 
        - Value: 13
        '''
        pass

    def kReflectivity(self):
        '''This is an enum of MtextureChannel.
        - Description: Blinn and Phong(E) only. 
        - Value: 14
        '''
        pass

    def kReflectedColor(self):
        '''This is an enum of MtextureChannel.
        - Description: Blinn and Phong(E) only. 
        - Value: 15
        '''
        pass

class MMaterialArray:
    '''Array of pointers of
MMaterial data type.
This class implements an array of
MMaterial. Common convenience functions are available, and the
implementation is compatible with the internal Maya
implementation so that it can be passed efficiently between
plugins and internal maya data structures.
'''
    def __init__(self):
        pass


    @overload
    def __getitem__(self, index: unsigned): 
        '''
        __getitem__(self, index: unsigned) -> const MMaterial

        Synopsis
        -----
        Returns the value of the element at the given index. No range
        checking is done - valid indices are 0 to length()-1.

        Returns: 
        ----- 
        The value of the indicated element.

        Parameters:
        -----
        index: unsigned
        	[in] -> the index of the element whose value is to be returned


        '''
        pass

    def set(self, element: MMaterial,
                        index: unsigned): 
        '''
        set(self, element: MMaterial,
                        index: unsigned)

        Synopsis
        -----
        Sets the value of the indicated element to the indicated
        MMaterial value. NOTE: This method does not grow the array if the
        index is out of bounds. Only a valid index should be used.

        Returns:
        -----
        None

        Parameters:
        -----
        element: MMaterial
        	[in] -> the new value for the indicated element 

        index: unsigned
        	[in] -> the index of the element that is to be set to the the new value


        '''
        pass

    def setLength(self, length: unsigned): 
        '''
        setLength(self, length: unsigned)

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
        length: unsigned
        	[in] -> the new size of the array 


        '''
        pass

    def length(self): 
        '''
        length(self)

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

    def remove(self, index: unsigned): 
        '''
        remove(self, index: unsigned)

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
        index: unsigned
        	[in] -> index of the element to be removed


        '''
        pass

    def insert(self, element: MMaterial,
                        index: unsigned): 
        '''
        insert(self, element: MMaterial,
                        index: unsigned)

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
        element: MMaterial
        	[in] -> the new value to insert into the array 

        index: unsigned
        	[in] -> the index of the element to set to the the new value


        '''
        pass

    def append(self, element: MMaterial): 
        '''
        append(self, element: MMaterial)

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
        element: MMaterial
        	[in] -> the value for the new last element


        '''
        pass

    def copy(self, source: MMaterialArray): 
        '''
        copy(self, source: MMaterialArray)

        Synopsis
        -----
        Copy the contents of the source array to this array.

        Returns:
        -----
        None

        Parameters:
        -----
        source: MMaterialArray
        	[in] -> array to copy from


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

    def setSizeIncrement(self, newIncrement: unsigned): 
        '''
        setSizeIncrement(self, newIncrement: unsigned)

        Synopsis
        -----
        Set the size by which the array will be expanded whenever
        expansion is necessary.

        Returns:
        -----
        None

        Parameters:
        -----
        newIncrement: unsigned
        	[in] -> the new increment 


        '''
        pass

    def sizeIncrement(self): 
        '''
        sizeIncrement(self)

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

    @overload
    def __getitem__(self, index: unsigned): 
        '''
        __getitem__(self, index: unsigned) -> MMaterial

        Synopsis
        -----
        Returns the value of the element at the given index. No range
        checking is done - valid indices are 0 to length()-1.

        Returns: 
        ----- 
        The value of the indicated element.

        Parameters:
        -----
        index: unsigned
        	[in] -> the index of the element whose value is to be returned


        '''
        pass

class MObjectListFilter:
    '''Class for defining a scene list filter.
MObjectListFilter provides an interface to define a list of selection items which
can be used to filter the display of items for interactive 3D
scene rendering.
The selection list can either have the meaning of rendering only
the items in that list (an inclusion list) or only rendering
items which are not in the list (an exclusion list).
Programmers using this interface can derive from this class and
implement the required methods. The derived class is responsible
for
'''
    def __init__(self):
        pass


    def requireListUpdate(self): 
        '''
        requireListUpdate(self) -> bool

        Synopsis
        -----
        This method is called by Maya to determine whether the contents
        of the object list for the filter has changed since the last
        requireLastUpdate() call was made. If the list has changed then
        getList() will be called to query for the contents of the
        filter.This method will be called once per frame render or
        refresh if the filter is actively being used for rendering.Users
        should never call this method themselves.Derived classes must
        implement this method.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getList(self, list: MSelectionList): 
        '''
        getList(self, list: MSelectionList)

        Synopsis
        -----
        This method will return the selection list to use for filtering
        scene rendering. Currently filtering at the component level is
        not supported. Any components specified for selection items in
        the list will be ignored.This method will be called when an
        update is indicated (by returning true from
        requireListUpdate()).If the filter type
        (MObjectListFilter::MFilterType) is
        MObjectListFilter::kExclusionList, Maya will by default monitor
        for scene changes. When objects are added or removed from the
        scene this indicates that an update is required which in turns
        indicates that this method needs to be called.Derived classes
        must implement this method.

        Returns:
        -----
        None

        Parameters:
        -----
        list: MSelectionList
        	[out] -> Object filter list (


        '''
        pass

    def dependentOnSceneUpdates(self): 
        '''
        dependentOnSceneUpdates(self) -> MObjectListFilter.MObjectListFilter

        Synopsis
        -----
        Return whether the update of the filter list is dependent on
        scene updates. If the method returns that it is dependent on
        scene updates then Maya will monitor for these changes and
        internally keep track that the filter requires an update on scene
        modifications. When Maya calls requireListUpdate() it will also
        check this internal state to determine wheter getList() needs to
        be called.For example, if MObjectListFilter::kAddRemoveObjects is
        returned from this method then any additions or removals of dag
        objects from the scene will result in getList() being called to
        obtain a new filter list. In this situation, if there is no other
        explicit condition that the filter requires for update then
        requireListUpdate() could return a "false" value to avoid
        unnecessary filter list updates.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setFilterType(self, filterType: MObjectListFilter.MObjectListFilter): 
        '''
        setFilterType(self, filterType: MObjectListFilter.MObjectListFilter)

        Synopsis
        -----
        Set the filter type. This is a convenience method for the user.
        This method will never be called by Maya.

        Returns:
        -----
        None

        Parameters:
        -----
        filterType: MObjectListFilter.MObjectListFilter
        	[in] -> Filter type defined by 


        '''
        pass

    def filterType(self): 
        '''
        filterType(self) -> MObjectListFilter.MObjectListFilter

        Synopsis
        -----
        Query the filter type.

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
        Query the name identifier.

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
        Query the UI name.

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
        Set the UI name.

        Returns:
        -----
        None

        Parameters:
        -----
        name: MString
        	[in] -> UI name 


        '''
        pass

    def registerFilter(self, filter: MObjectListFilter): 
        '''
        registerFilter(self, filter: MObjectListFilter)

        Synopsis
        -----
        Register the object filter as one of an available set of filters.
        It is not valid to register different object filters that have
        the same name as the name uniquely identifies the filter.The same
        filter cannot be registered more than once. If registerFilter()
        is called with the same filter more than once before calling
        deregisterFilter(), then the filter will not be added again, but
        a success status code will be returned.

        Returns:
        -----
        None

        Parameters:
        -----
        filter: MObjectListFilter
        	[in] -> Filter to register


        '''
        pass

    def deregisterFilter(self, filter: MObjectListFilter): 
        '''
        deregisterFilter(self, filter: MObjectListFilter)

        Synopsis
        -----
        Deregister the object filter from the list of available filters.

        Returns:
        -----
        None

        Parameters:
        -----
        filter: MObjectListFilter
        	[in] -> Filter to deregister


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

class MFilterType:
    '''Type of filter list. 
    Non-functional class.  Values for this enum:
    kInclusionList
    kExclusionList
    kNumberOfFilterTypes
    '''

    def __init__(self):
        pass

    def kInclusionList(self):
        '''This is an enum of MFilterType.
        - Description: Include only items on the list. 
        - Value: 0
        '''
        pass

    def kExclusionList(self):
        '''This is an enum of MFilterType.
        - Description: Exclude only items on the list. 
        - Value: 1
        '''
        pass

    def kNumberOfFilterTypes(self):
        '''This is an enum of MFilterType.
        - Description: Not to be used. This is the number of filter types. 
        - Value: 2
        '''
        pass

class MSceneUpdateType:
    '''Type of scene update. 
    Non-functional class.  Values for this enum:
    kNone
    kAddRemoveObjects
    '''

    def __init__(self):
        pass

    def kNone(self):
        '''This is an enum of MSceneUpdateType.
        - Description: List update is not dependent on scene changes. 
        - Value: 0
        '''
        pass

    def kAddRemoveObjects(self):
        '''This is an enum of MSceneUpdateType.
        - Description: List update is dependent on addition or removal of dag objects from the scene. 
        - Value: 1
        '''
        pass

class MPanelCanvasInfo:
    '''Panel state information setting and retrieval
This class provides methods for setting and retrieving common
information for all supported panels. Currently, the Graph Editor
is the only supported editor.
'''
    def __init__(self):
        pass


    @overload
    def getViewportBounds(self, left: double,
                        right: double,
                        bottom: double,
                        top: double): 
        '''
        getViewportBounds(self, left: double,
                        right: double,
                        bottom: double,
                        top: double)

        Synopsis
        -----
        Return the viewport bounds. Get the attached Graph Editor's
        viewport bounds, using the currently defined animation time
        units.Note: a viewport that is displaying stacked curves or re-
        normalized curves uses a different vertical axis scale.

        Returns:
        -----
        None

        Parameters:
        -----
        left: double
        	[out] -> left co-ordinate 

        right: double
        	[out] -> right co-ordinate 

        bottom: double
        	[out] -> bottom co-ordinate 

        top: double
        	[out] -> top co-ordinate


        '''
        pass

    @overload
    def getViewportBounds(self, boundsArray: MDoubleArray): 
        '''
        getViewportBounds(self, boundsArray: MDoubleArray)

        Synopsis
        -----
        Get the attached Graph Editor's viewport bounds, using the
        currently defined animation time units. Note: a viewport that is
        displaying stacked curves or re-normalized curves uses a
        different vertical axis scale.

        Returns:
        -----
        None

        Parameters:
        -----
        boundsArray: MDoubleArray
        	[out] -> an array of four doubles representing in order: (left, right, bottom, top) bounds co-ordinates


        '''
        pass

    def getViewportSize(self, width: int,
                        height: int): 
        '''
        getViewportSize(self, width: int,
                        height: int)

        Synopsis
        -----
        Return the viewport size. Get the attached Graph Editor's
        viewport size, excluding the time line.

        Returns:
        -----
        None

        Parameters:
        -----
        width: int
        	[out] -> width of viewport 

        height: int
        	[out] -> height of viewport


        '''
        pass

    @overload
    def setViewportBounds(self, left: double,
                        right: double,
                        bottom: double,
                        top: double): 
        '''
        setViewportBounds(self, left: double,
                        right: double,
                        bottom: double,
                        top: double)

        Synopsis
        -----
        Set the viewport bounds. Set the attached Graph Editor's viewport
        bounds to those that are supplied using the currently defined
        animation time units as seen in the viewport.Note: a viewport
        that is displaying stacked curves or re-normalized curves is not
        currently supported.

        Returns:
        -----
        None

        Parameters:
        -----
        left: double
        	[in] -> left co-ordinate 

        right: double
        	[in] -> right co-ordinate 

        bottom: double
        	[in] -> bottom co-ordinate 

        top: double
        	[in] -> top co-ordinate


        '''
        pass

    @overload
    def setViewportBounds(self, boundsArray: MDoubleArray): 
        '''
        setViewportBounds(self, boundsArray: MDoubleArray)

        Synopsis
        -----
        Set the attached Graph Editor's viewport bounds to those that are
        supplied using the currently defined animation time units as seen
        in the viewport. Note: a viewport that is displaying stacked
        curves or re-normalized curves is not currently supported.

        Returns:
        -----
        None

        Parameters:
        -----
        boundsArray: MDoubleArray
        	[in] -> an array of exactly four doubles representing in order: (left, right, bottom, top) bounds co-ordinates


        '''
        pass

    def supportsUIDrawing(self): 
        '''
        supportsUIDrawing(self) -> bool

        Synopsis
        -----
        Returns whether the attached panel control supports drawing
        primitives in screen space. If such drawing is not supported, the
        registerDrawUICallback () method will return
        MStatus::kNotImplemented.Note that for the Graph Editor, if the
        panel for drawing has not yet been created (e.g., when the
        default Graph Editor has not yet been opened), this method will
        return false.Note that the Graph Editor will return false if it
        exists, but the panel for drawing has not yet been created (e.g.,
        for the default Graph Editor when it has not yet been opened, but
        exists by default).

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
        name(self) -> MString

        Synopsis
        -----
        Return the name of the currently attached panel. Returns the name
        of the currently attached Graph Editor (if any)

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

class MProgressWindow:
    '''Create and manipulate progress windows.
The
MProgressWindow class manages a window containing a status message, a graphical
progress gauge, and optionally a "Hit ESC to Cancel" label for
interruptable operations.
Only a single progress window may be displayed at any time. To
reserve the use of the progress window, use the
reserve() method in this class. Any methods that change the state of the
progress window will fail unless the progress window has first
been successfully reserved.
The
startProgress() and
endProgress() functions show and hide the progress window.
endProgress() also has the effect of unreserving the progress window, allowing
it to be reserved for another use.
The MEL command "progressWindow" provides equivalent
functionality to this class. Attempting to manipulate a progress
window that is in use by MEL will cause the methods in this class
to fail.
'''
    def __init__(self):
        pass


    def reserve(self): 
        '''
        reserve(self) -> bool

        Synopsis
        -----
        Reserves a progress window for use through this class. This
        method must be called before setting progress window parameters
        or starting progress.Reserve will fail if progress window is
        already in use or when this method is called from worker thread.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def startProgress(self): 
        '''
        startProgress(self)

        Synopsis
        -----
        Displays the progress window on the screen.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def endProgress(self): 
        '''
        endProgress(self)

        Synopsis
        -----
        Destroys the progress window and removes it from the screen. This
        method also unreserves the progress window, making it available
        for future reservation.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setProgressRange(self, minValue: int,
                        maxValue: int): 
        '''
        setProgressRange(self, minValue: int,
                        maxValue: int)

        Synopsis
        -----
        Sets the range (minValue, maxValue) of the progress indicator.
        When the progress value is set through setProgress() or
        advanceProgress(), it is checked against the minimum and maximum
        progress values. If the new progress value lies outside this
        range, it is clamped to a value in this range.When the progress
        value is set to a value of minValue, the progress bar is
        displayed as empty. When the progress value is set to a value of
        maxValue, the progress bar is displayed as full. Intermediate
        progress values are displayed as intermediate positions of the
        progress bar.

        Returns:
        -----
        None

        Parameters:
        -----
        minValue: int
        	[in] -> Minimum progress value 

        maxValue: int
        	[in] -> Maximum progress value


        '''
        pass

    def setProgressMin(self, minValue: int): 
        '''
        setProgressMin(self, minValue: int)

        Synopsis
        -----
        Sets the minimum value for the progress. Any progress value less
        then minValue will be set to minValue, with the progress bar
        displayed as empty.

        Returns:
        -----
        None

        Parameters:
        -----
        minValue: int
        	[in] -> Minimum progress value


        '''
        pass

    def setProgressMax(self, maxValue: int): 
        '''
        setProgressMax(self, maxValue: int)

        Synopsis
        -----
        Sets the maximum value for the progress. Any progress value
        greater then maxValue will be set to maxValue, with the progress
        bar displayed as full.

        Returns:
        -----
        None

        Parameters:
        -----
        maxValue: int
        	[in] -> Maximum progress value


        '''
        pass

    def progressMin(self, ReturnStatus: MProgressWindow.MStatus): 
        '''
        progressMin(self, ReturnStatus: MProgressWindow.MStatus) -> int

        Synopsis
        -----
        Get the minimum progress value.

        Returns: 
        ----- 
        Minimum progress value. Returns -1 if query fails.

        Parameters:
        -----
        ReturnStatus: MProgressWindow.MStatus
        	[out] -> Status code


        '''
        pass

    def progressMax(self, ReturnStatus: MProgressWindow.MStatus): 
        '''
        progressMax(self, ReturnStatus: MProgressWindow.MStatus) -> int

        Synopsis
        -----
        Get the maximum progress value.

        Returns: 
        ----- 
        Maximum progress value. Returns -1 if query fails.

        Parameters:
        -----
        ReturnStatus: MProgressWindow.MStatus
        	[out] -> Status code


        '''
        pass

    def setProgress(self, progress: int): 
        '''
        setProgress(self, progress: int)

        Synopsis
        -----
        Sets the progress value. If progress is not between progressMin()
        and progressMax() inclusively, it is set to whichever of
        progressMin() or progressMax() is closest.Advancing the progress
        value updates the progress bar to show the new amount of
        progress.

        Returns:
        -----
        None

        Parameters:
        -----
        progress: int
        	[in] -> New progress value


        '''
        pass

    def advanceProgress(self, amount: int): 
        '''
        advanceProgress(self, amount: int)

        Synopsis
        -----
        Increases the progress value by amount. If the resulting progress
        value is not between progressMin() and progressMax() inclusively,
        it is set to whichever of progressMin() or progressMax() is
        closest.Advancing the progress value updates the progress bar to
        show the new amount of progress.

        Returns:
        -----
        None

        Parameters:
        -----
        amount: int
        	[in] -> Value to add to current progress


        '''
        pass

    def progress(self, ReturnStatus: MProgressWindow.MStatus): 
        '''
        progress(self, ReturnStatus: MProgressWindow.MStatus) -> int

        Synopsis
        -----
        Get the progress value.

        Returns: 
        ----- 
        Progress value. Returns -1 if query fails.

        Parameters:
        -----
        ReturnStatus: MProgressWindow.MStatus
        	[out] -> Status code


        '''
        pass

    def setTitle(self, title: MString): 
        '''
        setTitle(self, title: MString)

        Synopsis
        -----
        Sets the title of the progress window.

        Returns:
        -----
        None

        Parameters:
        -----
        title: MString
        	[in] -> New title


        '''
        pass

    def title(self, ReturnStatus: MProgressWindow.MStatus): 
        '''
        title(self, ReturnStatus: MProgressWindow.MStatus) -> MString

        Synopsis
        -----
        Get the window title.

        Returns: 
        ----- 
        Window title string.

        Parameters:
        -----
        ReturnStatus: MProgressWindow.MStatus
        	[out] -> Status code


        '''
        pass

    def setProgressStatus(self, progressStatus: MString): 
        '''
        setProgressStatus(self, progressStatus: MString)

        Synopsis
        -----
        Sets the progress status string. This string is shown above the
        progress bar and usually is of the form "Performing operation:
        <tt>XXX</tt>" where XXX is a numerical indication of the amount
        completed.

        Returns:
        -----
        None

        Parameters:
        -----
        progressStatus: MString
        	[in] -> New status string


        '''
        pass

    def progressStatus(self, ReturnStatus: MProgressWindow.MStatus): 
        '''
        progressStatus(self, ReturnStatus: MProgressWindow.MStatus) -> MString

        Synopsis
        -----
        Get the progress status string.

        Returns: 
        ----- 
        Progress status string.

        Parameters:
        -----
        ReturnStatus: MProgressWindow.MStatus
        	[out] -> Status code


        '''
        pass

    def setInterruptable(self, value: bool): 
        '''
        setInterruptable(self, value: bool)

        Synopsis
        -----
        Sets whether the progress window is interruptable. An
        interruptable progress window can accept a signal from the user
        indicating that the operation should be cancelled.isCancelled()
        is used to check if the user has tried to cancel an interruptable
        progress window.

        Returns:
        -----
        None

        Parameters:
        -----
        value: bool
        	[in] -> True if the progress window should be made interruptable.


        '''
        pass

    def isInterruptable(self, ReturnStatus: MProgressWindow.MStatus): 
        '''
        isInterruptable(self, ReturnStatus: MProgressWindow.MStatus) -> bool

        Synopsis
        -----
        Determine whether the progress window is interruptable.

        Returns: 
        ----- 
        true when the progress window is interruptable

        Parameters:
        -----
        ReturnStatus: MProgressWindow.MStatus
        	[out] -> Status code


        '''
        pass

    def isCancelled(self, ReturnStatus: MProgressWindow.MStatus): 
        '''
        isCancelled(self, ReturnStatus: MProgressWindow.MStatus) -> bool

        Synopsis
        -----
        Determine whether the user has tried to cancel an interruptable
        progress window.

        Returns: 
        ----- 
        true when user has tried to cancel progress. If the progress
        window is not interruptable, this method returns false.

        Parameters:
        -----
        ReturnStatus: MProgressWindow.MStatus
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

class MQtUtil:
    '''Qt Utility Methods.
This class provides some basic methods for accessing the Qt
controls which underlie Maya's UI.
The safest way to use the Qt API from within Maya is to create
your own Qt window and populate it with your own controls.
While it is possible to use the Qt API to modify existing Maya UI
elements, such as those created using Maya commands from MEL or
Python, such modifications are not supported by Autodesk and
could lead to Maya becoming unstable or inoperable.
In practice, you will likely find a number of modifications which
appear safe, such as changing a control's text or reorganizing
the items on a menu. However, Autodesk provides no guarantees
that the underlying implementations of those UI elements won't
change from one release of Maya to another, potentially in ways
that may make formerly safe usage become unsafe. So if you choose
to incorporate such actions into your plug-in be aware that you
may have to modify your code in future versions of Maya.
In Qt a layout (i.e. a QLayout or something derived from it) is
not a widget. It is attached to a widget to control the
positioning of that widget's children but is not itself a child
of the widget and does not appear in the widget hierarchy.
In Maya, layouts are also widgets which are part of the
hierarchy. For example, if you have a window named "myWin" which
contains a layout named "myLayout" which in turn holds a button
named "myButton", then the button's full hierarchical name would
be "myWin|myLayout|myButton".
To bridge this difference, each Maya layout is given its own
placeholder QWidget to which the corresponding QLayout is applied
and bearing the same name as the layout. The children of the
layout are then parented beneath the placeholder widget. When you
call the
findLayout() method, it is the placeholder widget which is returned.
The one exception to this use of placeholders is the top-level
layout of a window. Rather than introduce a superfluous
placeholder widget, the top-level QLayout is attached directly to
the window. So a call to
findLayout() for a top-level layout will return the window. Note, however,
that the top-level layout's hierarchical name is still structured
as if it had its own dedicated widget in the hierarchy. E.g.
"myWin|myLayout". This can lead to the somewhat incongruous
result that calling
fullName() on the result of a
findLayout() call for a top-level layout will return the name of the window
rather than the layout. E.g:
In the example above,
 will contain "myWin" rather than the string we started out with,
"myWin|myLayout". To get around this problem pass the widget's
QLayout to
fullName() instead:
Now
 will contain "myWin|myLayout" as expected.
Not all Maya layouts are implemented by a single QLayout attached
to a single placeholder widget (or window). In some cases the
layout is implemented by a small sub-tree of widgets and
QLayouts. Despite this added complexity behind the scenes, Maya
still treats the entire sub-tree as a single element in the
hierarchy for which the
findLayout() method will return the top-level widget of the sub-tree.
To simplify the traversal of these complex layouts, the
getLayoutChildren() and
getParent() methods treat complex layouts as if they are a single layout
widget with their children parented directly beneath, skipping
over any internal widgets which the layout's sub-tree may
contain. In this way,
getLayoutChildren() returns the same set of children as the
 command's
 flags, while
getParent() returns the same layout as a control's
 flags.
Some Qt header files redefine certain standard C++ library
symbols. As such it is important that the Qt headers be included
before any other header files which might reference those
symbols.
To ensure proper compilation, your source files should always
include any Qt header files they use (QWidget, QEvent, etc)
before all other header files. If the source includes MQtUtil.h
then it should come after the Qt headers but before any others.
Qt is made available under both open source and commercial
licenses. The type of license required depends upon your intended
use of Qt. For more information, see the Qt Licensing page at
https://www.qt.io/faq/'''
    def __init__(self):
        pass


    def findControl(self, controlName: MString,
                        ancestor: MQtUtil.QWidget): 
        '''
        findControl(self, controlName: MString,
                        ancestor: MQtUtil.QWidget) -> MQtUtil.OPENMAYA_MAJOR_NAMESPACE_OPENQWidget*

        Synopsis
        -----
        Returns the QWidget for the named Maya control.

        Returns: 
        ----- 
        Pointer to the control's underlying QWidget. Returns NULL if the
        control is not found.

        Parameters:
        -----
        controlName: MString
        	[in] -> Name of the control within Maya. May be a plain name ("myButton") or a hierarchical name ("myWin|myLayout|myButton"). If a hierarchical name is supplied then the search will begin with the UI element at the start of the hierarchy and descend from there.

        ancestor: MQtUtil.QWidget
        	[in] -> Pointer to an ancestor UI element which appears somewhere in the UI hierarchy above the control. If not NULL then the search will begin at the specified ancestor and descend from there.


        '''
        pass

    def findLayout(self, layoutName: MString,
                        ancestor: MQtUtil.QWidget): 
        '''
        findLayout(self, layoutName: MString,
                        ancestor: MQtUtil.QWidget) -> MQtUtil.QWidget*

        Synopsis
        -----
        Returns the QWidget for the named Maya layout. In Maya a layout
        is part of the widget tree and is represented by a QWidget to
        which the actual QLayout has been applied. This method returns a
        pointer to that QWidget.There are some important exceptions to
        this rule. See the "Layouts In Maya Vs. Qt" discussion in the
        class documentation for further details.

        Returns: 
        ----- 
        Pointer to the layout's underlying QWidget. Returns NULL if the
        layout is not found.

        Parameters:
        -----
        layoutName: MString
        	[in] -> Name of the layout within Maya. May be a plain name ("myLayout") or a hierarchical name ("myWin|myLayout"). If a hierarchical name is supplied then the search will begin with the UI element at the start of the hierarchy and then descend from there.

        ancestor: MQtUtil.QWidget
        	[in] -> Pointer to an ancestor UI element which appears somewhere in the UI hierarchy above the layout. If not NULL then the search will begin at the specified ancestor and descend from there.


        '''
        pass

    def findMenuItem(self, itemName: MString): 
        '''
        findMenuItem(self, itemName: MString) -> MQtUtil.QAction*

        Synopsis
        -----
        Returns the QAction for the named Maya menuItem.

        Returns: 
        ----- 
        Pointer to the menuItem's underlying QAction. Returns NULL if the
        menuItem is not found.

        Parameters:
        -----
        itemName: MString
        	[in] -> Name of the menuItem within Maya. May be a plain name ("myItem") or a hierarchical name ("myMenu|myItem"). If a hierarchical name is supplied then the search will begin with the UI element at the start of the hierarchy and then descend from there.


        '''
        pass

    def findWindow(self, windowName: MString): 
        '''
        findWindow(self, windowName: MString) -> MQtUtil.QWidget*

        Synopsis
        -----
        Returns the QWidget for the named Maya window.

        Returns: 
        ----- 
        Pointer to the window's underlying QWidget. Returns NULL if the
        window is not found.

        Parameters:
        -----
        windowName: MString
        	[in] -> Name of the window within Maya.


        '''
        pass

    def fullName(self, uiElement: MQtUtil.QObject): 
        '''
        fullName(self, uiElement: MQtUtil.QObject) -> MString

        Synopsis
        -----
        Returns the full, hierarchical name of a UI element. This is the
        name which uniquely identifies the element within Maya and can be
        passed to Maya's UI commands.For example, if a window was created
        as follows using MEL:window myWin; columnLayout myLayout; button
        -l "Press Me" myButton;then passing a pointer to 'myButton's
        QObject would return the string "myWin|myLayout|myButton".

        Returns: 
        ----- 
        String containing the full hierarchical name of the UI element,
        or an empty string if the element does not exist.

        Parameters:
        -----
        uiElement: MQtUtil.QObject
        	[in] -> pointer to a UI element's QObject


        '''
        pass

    def getCurrentParent(self): 
        '''
        getCurrentParent(self) -> MQtUtil.QWidget*

        Synopsis
        -----
        Returns the placeholder widget for the current layout if there is
        one. The current layout is set when a layout is created using a
        Maya layout command. In MEL, this layout can be queried using
        "setParent -q". When adding a QWidget to a Maya layout, the new
        QWidget should be parented to this widget. For example, in the
        following MEL code the plug-in command 'myControl' should create
        a custom QWidget-derived control and parent it to the
        columnLayout's placeholder QWidget, and then add it using
        addWidgetToMayaLayout().window myWin; columnLayout; myControl;
        showWindow;

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def createPixmap(self, imageName: MString,
                        autoScale: bool): 
        '''
        createPixmap(self, imageName: MString,
                        autoScale: bool) -> MQtUtil.QPixmap*

        Synopsis
        -----
        Looks for a pixmap first in the Qt resources, and then in a file
        on disk. Returns the pixmap with the given name. If autoscale is
        true, then the image at the appropriate DPI is selected.

        Returns: 
        ----- 
        Pointer to the created pixmap.

        Parameters:
        -----
        imageName: MString
        	[in] -> The image to look up.

        autoScale: bool
        	[in] -> A boolean that if true, looks for a version of the image at the current scaling factor.


        '''
        pass

    def createCursor(self, cursorName: MString,
                        autoScale: bool): 
        '''
        createCursor(self, cursorName: MString,
                        autoScale: bool) -> MQtUtil.QCursor*

        Synopsis
        -----
        Looks for a cursor first in the Qt resources, and then in a file
        on disk. Returns the cursor with the given name. If autoscale is
        true, then the cursor at the appropriate DPI is selected.

        Returns: 
        ----- 
        Pointer to the created cursor.

        Parameters:
        -----
        cursorName: MString
        	[in] -> The cursor to look up.

        autoScale: bool
        	[in] -> A boolean that if true, looks for a version of the cursor at the current scaling factor.


        '''
        pass

    def createIcon(self, iconName: MString,
                        autoScale: bool): 
        '''
        createIcon(self, iconName: MString,
                        autoScale: bool) -> MQtUtil.QIcon*

        Synopsis
        -----
        Looks for a icon first in the Qt resources, and then in a file on
        disk. Returns the icon with the given name. If autoscale is true,
        then the icon at the appropriate DPI is selected.

        Returns: 
        ----- 
        Pointer to the created icon.

        Parameters:
        -----
        iconName: MString
        	[in] -> The image to look up.

        autoScale: bool
        	[in] -> A boolean that if true, looks for a version of the icon at the current scaling factor.


        '''
        pass

    def getLayoutChildren(self, layout: MQtUtil.QWidget): 
        '''
        getLayoutChildren(self, layout: MQtUtil.QWidget) -> MQtUtil.QList<QObject*>

        Synopsis
        -----
        Returns a list of all the Maya UI elements parented directly
        beneath the specified Maya layout. There may not always be a one-
        to-one correspondence between a Maya layout and a QLayout. For
        example, some of Maya's layouts are implemented by a small sub-
        tree of widgets which handle different aspects of the layout.This
        method will treat that entire sub-tree as a single layout element
        and return all of the Maya controls and sub-layouts which it
        handles as a flattened list, with all of Maya's internal objects
        removed.This method can be used in conjunction with getParent()
        to navigate up and down through such complex layouts as if they
        were single UI elements.

        Returns: 
        ----- 
        A list of QObjects for all of the Maya controls and layouts
        parented beneath the specified layout.

        Parameters:
        -----
        layout: MQtUtil.QWidget
        	[in] -> Pointer to a Maya layout's QWidget. See 


        '''
        pass

    def getParent(self, uiElement: MQtUtil.QObject): 
        '''
        getParent(self, uiElement: MQtUtil.QObject) -> MQtUtil.QObject*

        Synopsis
        -----
        Returns a pointer to a UI element's parent element within Maya's
        UI hierarchy. There may not always be a one-to-one correspondence
        between an element in Maya's UI hierarchy and a Qt object. For
        example, some of Maya's layouts are implemented by a small sub-
        tree of widgets. This method will treat that entire sub-tree as a
        single element by stepping to its head object.This method can be
        used in conjunction with getLayoutChildren() to navigate up and
        down through such complex layouts as if they were single UI
        elements.

        Returns: 
        ----- 
        A pointer to the element's parent element, or NULL is the element
        has no parent or is a window.

        Parameters:
        -----
        uiElement: MQtUtil.QObject
        	[in] -> A pointer to a UI element's QObject


        '''
        pass

    def addWidgetToMayaLayout(self, control: MQtUtil.QWidget,
                        layout: MQtUtil.QWidget,
                        uiType: MString): 
        '''
        addWidgetToMayaLayout(self, control: MQtUtil.QWidget,
                        layout: MQtUtil.QWidget,
                        uiType: MString) -> MString

        Synopsis
        -----
        Adds a QWidget to an existing Maya layout, such as that returned
        by getCurrentParent() or getLayout(). Once the QWidget has been
        added, it can be used in MEL or Python scripts like native Maya
        controls. In order to integrate the control into Maya's UI,
        several modifications are made:

        Returns: 
        ----- 
        String containing the full hierarchical name of the added
        control, or an empty string on failure. Commands which create
        custom Maya controls must return this name so that it can be used
        in scripts to find the added control.

        Parameters:
        -----
        control: MQtUtil.QWidget
        	[in] -> The QWidget to be added. If the control is named (with QObject::setObjectName), the name may be modified to make it unique, this will be done by adding a numeric suffix. Otherwise a default name, based on the class name will be used. 

        layout: MQtUtil.QWidget
        	[in] -> The placeholder widget for the Maya layout 

        uiType: MString
        	[in] -> A Maya ui-type name for the QWidget being added. Defaults to the name of its class. This name can be used by the Maya commands 


        '''
        pass

    def registerUIType(self, className: MString,
                        fn: MQtUtil.UITypeCreatorFn,
                        command: MString): 
        '''
        registerUIType(self, className: MString,
                        fn: MQtUtil.UITypeCreatorFn,
                        command: MString) -> bool

        Synopsis
        -----
        Registers a class name (UI-type) with a function to create the
        QWidget of that type, and a command to edit it with. The loadUI
        command looks at each widget element of the Qt Designer XML
        document, and if the class attribute matches a registered class
        name, it calls the associated function to create the object.If
        there are any dynamic string properties with a '-' (MEL) or '+'
        (Python) prefix, the associated command is called in edit mode
        with the property name as the flag and the value as the flag
        value.For example, with the following registration: The following
        XML fragment will delegate creation of the object to createCustom
        and then call custom -edit -setValue 33 "custom1". <widget
        class="QCustom" name="custom1"> <property name="-setValue">
        <string>33</string> </property> </widget> Some Qt types are
        associated by default with internal Maya commands, such as
        QPushButton -> button etc. This can be queried with loadUI
        -listTypes.

        Returns: 
        ----- 
        true if successful, false if the class name is already
        registered.

        Parameters:
        -----
        className: MString
        	[in] -> The name of the QWidget-derived class created by the function. 

        fn: MQtUtil.UITypeCreatorFn
        	[in] -> The creator function. 

        command: MString
        	[in] -> The command to be used to edit the created QWidget.


        '''
        pass

    def deregisterUIType(self, className: MString): 
        '''
        deregisterUIType(self, className: MString) -> bool

        Synopsis
        -----
        De-registers a widget class (UI-type) which has been previously
        registered with registerUIType().

        Returns: 
        ----- 
        true if successful, false if the class name is not registered.

        Parameters:
        -----
        className: MString
        	[in] -> The name of the class to be de-registered.


        '''
        pass

    def mainWindow(self): 
        '''
        mainWindow(self) -> MQtUtil.QWidget*

        Synopsis
        -----
        Returns Maya's main window.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def resourceGLContext(self): 
        '''
        resourceGLContext(self) -> MQtUtil.QGLContext*

        Synopsis
        -----
        Returns Maya internal QGLContext that the plug-in may use to
        create resource-sharing OpenGL context.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def nativeWindow(self, control: MQtUtil.QWidget): 
        '''
        nativeWindow(self, control: MQtUtil.QWidget) -> MQtUtil.MNativeWindowHdl

        Synopsis
        -----
        /*! Returns a platform-specific native window handle for the
        specified control. If the control is native then its native
        handle will be returned, otherwise a native window will be
        created for it. This may reduce performance so native should only
        be requested when necessary.

        Returns: 
        ----- 
        The native window handle of the specified control. On Linux this
        will be an Xlib 'Window'. On 32-bit OS X it will be an
        'HIViewRef'. On 64-bit OS X it will be an 'NSView' pointer. On
        Microsoft Windows it will be an 'HWND'.

        Parameters:
        -----
        control: MQtUtil.QWidget
        	[in] -> Control whose native window handle is to be returned.


        '''
        pass

    def toMString(self, qstr: MQtUtil.QString): 
        '''
        toMString(self, qstr: MQtUtil.QString) -> MString

        Synopsis
        -----
        Convenience utility to convert a QString to an MString.

        Returns: 
        ----- 
        An MString containing the same text as 'qstr'.

        Parameters:
        -----
        qstr: MQtUtil.QString
        	[in] -> QString to be converted.


        '''
        pass

    def toQString(self, mstr: MString): 
        '''
        toQString(self, mstr: MString) -> MQtUtil.QString

        Synopsis
        -----
        Convenience utility to convert an MString to a QString.

        Returns: 
        ----- 
        A QString containing the same text as 'mstr'.

        Parameters:
        -----
        mstr: MString
        	[in] -> MString


        '''
        pass

    @overload
    def dpiScale(self, size: int): 
        '''
        dpiScale(self, size: int) -> int

        Synopsis
        -----
        Get the scaled size for Maya interface scaling. This public
        method should be used when define the size of Qt widget, e.g.:
        Setting the width of a Maya Qt control.

        Returns: 
        ----- 
        The scaled size in Qt.

        Parameters:
        -----
        size: int
        	[in] -> The size in Maya UI


        '''
        pass

    @overload
    def dpiScale(self, size: float): 
        '''
        dpiScale(self, size: float) -> float

        Synopsis
        -----
        Get the scaled size for Maya interface scaling. This public
        method should be used when define the size of Qt widget, e.g.:
        Setting the width of a Maya Qt control.

        Returns: 
        ----- 
        The scaled size in Qt.

        Parameters:
        -----
        size: float
        	[in] -> The size in Maya UI


        '''
        pass

    @overload
    def newClocaleValidator(self, bottom: double,
                        top: double,
                        decimals: int,
                        parent: MQtUtil.QObject): 
        '''
        newClocaleValidator(self, bottom: double,
                        top: double,
                        decimals: int,
                        parent: MQtUtil.QObject) -> MQtUtil.QDoubleValidator*

        Synopsis
        -----
        Introduced in 2022.0 Creates a overloaded QDoubleValidator
        instance that will automatically convert decimal separator to dot
        to facilidate interfacing with Maya.Mel, Python or std::atof are
        all expecting numbers to use "decimal dot" as a separator despite
        the current locale settingThere is 2 versions of that method and
        they are matching QDoubleValidator constructors declaration

        Returns: 
        ----- 
        Pointer to the allocated validator, these instance are reference
        counted and Qt will take care of deallocating validator when
        assoiciated controls gets destroyed

        Parameters:
        -----
        bottom: double
        	[in] -> lower numerical limit 

        top: double
        	[in] -> upper numerical limit 

        decimals: int
        	[in] -> number of accepted decimals 

        parent: MQtUtil.QObject
        	[in] -> widget


        '''
        pass

    @overload
    def newClocaleValidator(self, parent: MQtUtil.QObject): 
        '''
        newClocaleValidator(self, parent: MQtUtil.QObject) -> MQtUtil.QDoubleValidator*

        Synopsis
        -----
        Introduced in 2022.0

        Returns:
        -----
        None

        Parameters:
        -----
        parent: MQtUtil.QObject
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

class MTextureEditorDrawInfo:
    '''Drawing state for drawing to the UV texture window with custom
shapes.
This class is used by drawUV method of
MPxSurfaceShapeUI to specify the current UV drawing state for a user defined
shape. API users must override the canDrawUV method on
MPxSurfaceShapeUI to recieve drawUV calls. The only situation where the drawing
style can change is during a selection event. However, selection
events are currently not passed onto the API user. Therefore,
most of the functionality in this class is place holder for
future work.
'''
    def __init__(self):
        pass


    def drawingFunction(self): 
        '''
        drawingFunction(self) -> MTextureEditorDrawInfo.MTextureEditorDrawInfo

        Synopsis
        -----
        Indicates the current drawing state for a drawUV method call.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setDrawingFunction(self, func: MTextureEditorDrawInfo.MTextureEditorDrawInfo): 
        '''
        setDrawingFunction(self, func: MTextureEditorDrawInfo.MTextureEditorDrawInfo)

        Synopsis
        -----
        Sets the current drawing state. Currently the API user is unable
        to set these values. All drawing state values are determined
        internally and passed onto the API programmer.

        Returns:
        -----
        None

        Parameters:
        -----
        func: MTextureEditorDrawInfo.MTextureEditorDrawInfo
        	[in] -> drawing function. 


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

class DrawingFunction:
    '''Draw modes. 
    Non-functional class.  Values for this enum:
    kDrawFunctionFirst
    kDrawWireframe
    kDrawEverything
    kDrawVertexForSelect
    kDrawEdgeForSelect
    kDrawFacetForSelect
    kDrawUVForSelect
    kDrawFunctionLast
    '''

    def __init__(self):
        pass

    def kDrawFunctionFirst(self):
        '''This is an enum of DrawingFunction.
        - Description: Lowest possible enum value. 
        - Value: 1
        '''
        pass

    def kDrawWireframe(self):
        '''This is an enum of DrawingFunction.
        - Description: Draw wireframe only (default) 
        - Value: 1
        '''
        pass

    def kDrawEverything(self):
        '''This is an enum of DrawingFunction.
        - Description: Draw vertices, uvs, faces, and edges. 
        - Value: 2
        '''
        pass

    def kDrawVertexForSelect(self):
        '''This is an enum of DrawingFunction.
        - Description: Draw vertices for selection. 
        - Value: 3
        '''
        pass

    def kDrawEdgeForSelect(self):
        '''This is an enum of DrawingFunction.
        - Description: Draw edges for selection. 
        - Value: 4
        '''
        pass

    def kDrawFacetForSelect(self):
        '''This is an enum of DrawingFunction.
        - Description: Draw faces for selection. 
        - Value: 5
        '''
        pass

    def kDrawUVForSelect(self):
        '''This is an enum of DrawingFunction.
        - Description: Draw uvs for selection. 
        - Value: 6
        '''
        pass

    def kDrawFunctionLast(self):
        '''This is an enum of DrawingFunction.
        - Description: Highest possible enum value. 
        - Value: 6
        '''
        pass

class MToolsInfo:
    '''Tool information.
MToolsInfo is a caretaker class used to keep track of the state of the
current tool property sheet. The tool writer should make sure to
call the setDirtyFlag method when any of the values are modified.
The dirty flag is used to indicate that the UI needs to be
updated when the value of a tool property sheet option has
changed.
'''
    def __init__(self):
        pass


    def setDirtyFlag(self, context: MPxContext): 
        '''
        setDirtyFlag(self, context: MPxContext) -> MToolsInfo.OPENMAYA_MAJOR_NAMESPACE_OPENvoid

        Synopsis
        -----
        This method should be called by a tool when the value of a tool
        property sheet option has changed. The dirty flag will only be
        set if this is the current tool.

        Returns:
        -----
        None

        Parameters:
        -----
        context: MPxContext
        	[in] -> the context whose value has changed 


        '''
        pass

    def isDirty(self): 
        '''
        isDirty(self) -> bool

        Synopsis
        -----
        This method returns whether or not the dirty flag is set.

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

class MUiMessage:
    '''UI messages.
This class is used to register callbacks to track the deletion of
UI objects.
The first parameter passed to the add callback method is the name
of the UI that will trigger the callback.
The method returns an id which is used to remove the callback.
To remove a callback use
MMessage::removeCallback.
All callbacks that are registered by a plug-in must be removed by
that plug-in when it is unloaded. Failure to do so will result in
a fatal error.
'''
    def __init__(self):
        pass


    def addUiDeletedCallback(self, uiName: MString,
                        func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MUiMessage.MStatus): 
        '''
        addUiDeletedCallback(self, uiName: MString,
                        func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MUiMessage.MStatus) -> MUiMessage.OPENMAYA_MAJOR_NAMESPACE_OPENMCallbackId

        Synopsis
        -----
        This method registers a callback for UI deleted messages. The
        callback function will be passed any client data that was
        provided when the callback was registered.

        Returns: 
        ----- 
        Identifier used for removing the callback.

        Parameters:
        -----
        uiName: MString
        	[in] -> the name of the UI object to register the callback for 

        func: MMessage.MMessage
        	[in] -> the callback function, which takes the following parameters: 

        clientData: void
        	[in] -> User defined data that will be passed to the callback function 

        ReturnStatus: MUiMessage.MStatus
        	[out] -> status code


        '''
        pass

    def addCameraChangedCallback(self, panelName: MString,
                        func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MUiMessage.MStatus): 
        '''
        addCameraChangedCallback(self, panelName: MString,
                        func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MUiMessage.MStatus) -> MCallbackId

        Synopsis
        -----
        This method registers a callback for cameras being changed in 3d
        views. The callback is called when the camera changes for the
        given panel, not when attributes on the panel's camera change.The
        callback function will be passed any client data that was
        provided when the callback was registered.

        Returns: 
        ----- 
        Identifier used for removing the callback.

        Parameters:
        -----
        panelName: MString
        	[in] -> Name of panel to which to attach the callback. 

        func: MMessage.MMessage
        	[in] -> the callback function, which takes the following parameters: 

        clientData: void
        	[in] -> User defined data that will be passed to the callback function 

        ReturnStatus: MUiMessage.MStatus
        	[out] -> status code


        '''
        pass

    def add3dViewDestroyMsgCallback(self, panelName: MString,
                        func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MUiMessage.MStatus): 
        '''
        add3dViewDestroyMsgCallback(self, panelName: MString,
                        func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MUiMessage.MStatus) -> MCallbackId

        Synopsis
        -----
        This method registers a callback for when a particular 3d view
        gets destroyed. The callback is called before the destruction of
        the view.The callback function will be passed any client data
        that was provided when the callback was registered.

        Returns: 
        ----- 
        Identifier used for removing the callback.

        Parameters:
        -----
        panelName: MString
        	[in] -> Name of panel to which to attach the callback. 

        func: MMessage.MMessage
        	[in] -> the callback function, which takes the following parameters: 

        clientData: void
        	[in] -> User defined data that will be passed to the callback function 

        ReturnStatus: MUiMessage.MStatus
        	[out] -> status code


        '''
        pass

    def add3dViewPreRenderMsgCallback(self, panelName: MString,
                        func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MUiMessage.MStatus): 
        '''
        add3dViewPreRenderMsgCallback(self, panelName: MString,
                        func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MUiMessage.MStatus) -> MCallbackId

        Synopsis
        -----
        This method registers a callback for when a particular 3d view is
        about to render it's contents. It is called before the scene is
        drawn, but after the background has been drawn.The callback
        function will be passed any client data that was provided when
        the callback was registered.

        Returns: 
        ----- 
        Identifier used for removing the callback.

        Parameters:
        -----
        panelName: MString
        	[in] -> Name of panel to which to attach the callback. 

        func: MMessage.MMessage
        	[in] -> the callback function, which takes the following parameters: 

        clientData: void
        	[in] -> User defined data that will be passed to the callback function 

        ReturnStatus: MUiMessage.MStatus
        	[out] -> status code


        '''
        pass

    def add3dViewPostRenderMsgCallback(self, panelName: MString,
                        func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MUiMessage.MStatus): 
        '''
        add3dViewPostRenderMsgCallback(self, panelName: MString,
                        func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MUiMessage.MStatus) -> MCallbackId

        Synopsis
        -----
        This method registers a callback for when the 3d view is about to
        display it's rendered contents to the viewport. It is called for
        every refresh of the view, after the scene is drawn, but before
        any 2d adornments are drawn.The callback function will be passed
        any client data that was provided when the callback was
        registered.

        Returns: 
        ----- 
        Identifier used for removing the callback.

        Parameters:
        -----
        panelName: MString
        	[in] -> Name of panel to which to attach the callback. 

        func: MMessage.MMessage
        	[in] -> the callback function, which takes the following parameters: 

        clientData: void
        	[in] -> User defined data that will be passed to the callback function 

        ReturnStatus: MUiMessage.MStatus
        	[out] -> status code


        '''
        pass

    def add3dViewPreMultipleDrawPassMsgCallback(self, panelName: MString,
                        func: MUiMessage.MUiMessage,
                        clientData: void,
                        ReturnStatus: MUiMessage.MStatus): 
        '''
        add3dViewPreMultipleDrawPassMsgCallback(self, panelName: MString,
                        func: MUiMessage.MUiMessage,
                        clientData: void,
                        ReturnStatus: MUiMessage.MStatus) -> MCallbackId

        Synopsis
        -----
        This method registers a callback for when a particular 3d view's
        specific pass is about to be drawn when multiple drawing is
        enabled. The 3D view callbacks are called in the following order:
        The callback function will be passed any client data that was
        provided when the callback was registered.

        Returns: 
        ----- 
        Identifier used for removing the callback.

        Parameters:
        -----
        panelName: MString
        	[in] -> Name of panel to which to attach the callback. 

        func: MUiMessage.MUiMessage
        	[in] -> the callback function, which takes the following parameters: 

        clientData: void
        	[in] -> User defined data that will be passed to the callback function 

        ReturnStatus: MUiMessage.MStatus
        	[out] -> status code


        '''
        pass

    def add3dViewPostMultipleDrawPassMsgCallback(self, panelName: MString,
                        func: MUiMessage.MUiMessage,
                        clientData: void,
                        ReturnStatus: MUiMessage.MStatus): 
        '''
        add3dViewPostMultipleDrawPassMsgCallback(self, panelName: MString,
                        func: MUiMessage.MUiMessage,
                        clientData: void,
                        ReturnStatus: MUiMessage.MStatus) -> MCallbackId

        Synopsis
        -----
        This method registers a callback for when a particular 3d view's
        specified pass is finshed when multiple drawing is enabled. See
        add3dViewPreMultipleDrawPassMsgCallback for the order in which 3D
        view callbacks are called.The callback function will be passed
        any client data that was provided when the callback was
        registered.

        Returns: 
        ----- 
        Identifier used for removing the callback.

        Parameters:
        -----
        panelName: MString
        	[in] -> Name of panel to which to attach the callback. 

        func: MUiMessage.MUiMessage
        	[in] -> the callback function, which takes the following parameters: 

        clientData: void
        	[in] -> User defined data that will be passed to the callback function 

        ReturnStatus: MUiMessage.MStatus
        	[out] -> status code


        '''
        pass

    def add3dViewRendererChangedCallback(self, panelName: MString,
                        func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MUiMessage.MStatus): 
        '''
        add3dViewRendererChangedCallback(self, panelName: MString,
                        func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MUiMessage.MStatus) -> MCallbackId

        Synopsis
        -----
        This method registers a callback for when the renderer for a
        particular 3d view changes. The callback function will be passed
        any client data that was provided when the callback was
        registered.

        Returns: 
        ----- 
        Identifier used for removing the callback.

        Parameters:
        -----
        panelName: MString
        	[in] -> Name of panel to which to attach the callback. 

        func: MMessage.MMessage
        	[in] -> the callback function, which takes the following parameters: 

        clientData: void
        	[in] -> User defined data that will be passed to the callback function 

        ReturnStatus: MUiMessage.MStatus
        	[out] -> status code


        '''
        pass

    def add3dViewRenderOverrideChangedCallback(self, panelName: MString,
                        func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MUiMessage.MStatus): 
        '''
        add3dViewRenderOverrideChangedCallback(self, panelName: MString,
                        func: MMessage.MMessage,
                        clientData: void,
                        ReturnStatus: MUiMessage.MStatus) -> MCallbackId

        Synopsis
        -----
        This method registers a callback for when the render override for
        a particular 3d view changes. The callback function will be
        passed any client data that was provided when the callback was
        registered.

        Returns: 
        ----- 
        Identifier used for removing the callback.

        Parameters:
        -----
        panelName: MString
        	[in] -> Name of panel to which to attach the callback. 

        func: MMessage.MMessage
        	[in] -> the callback function, which takes the following parameters: 

        clientData: void
        	[in] -> User defined data that will be passed to the callback function 

        ReturnStatus: MUiMessage.MStatus
        	[out] -> status code


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

