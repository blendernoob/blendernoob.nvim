
'''
Stub class file for:
OpenMayaMPx

Maya2024 Python API stub file
Vscode Version
Generated from original Maya documentation.
Autodesk Maya2024  c1997-2023 Autodesk, Inc. All rights reserved. 
'''


from typing import overload




class MPx3dModelView:
    '''MPx3dModelView is the class for user defined model views.
The
MPx3dModelView class works with the
MPxModelEditorCommand class to create a user defined model editor that may be used in
a window or in a scripted panel. When registering the model
editor with the
MFnPlugin::registerModelEditorCommand() method, an appropriate MPx3dModelView::creator() method is
required. This class works for interactive Maya views and is not
designed for rendering.
One of the interesting uses of a
MPx3dModelView is that it allows multiple cameras to be drawn into the same
window. Like a normal model view, this view has a main camera
associated with it. This camera is obtained with the
getCamera() method and is the camera used for manipulations and selection.
To setup a multiple camera draw, first the number of passes must
be set by an overloaded
multipleDrawPassCount() method. The
preMultipleDraw() method allows any setup to be performed. The
preMultipleDrawPass(unsigned int) is called for each pass, with the argument indicating which pass
is currently being used. The camera for the specific pass may be
set with the
setCameraInDraw() method. The
postMultipleDrawPass(unsigned int) method is called after the drawing for the indicated pass is
complete. Finally any cleanup may be done with the
postMultipleDraw() method.
During the drawing, a filter exists to determine which items
should be drawn. The okForMultipleDraw(MdagPath &) allows
filtering of what should be drawn. Another approach which is
faster is to tuen on the view selected mode (
setViewSelected()) and use the
setObjectsToView() or
viewSelectedSet() to specify which items should be drawn. These values may be set
per pass so that each camera has control over what gets drawn.
'''
    def __init__(self):
        pass


    def name(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        name(self, ReturnStatus: MPx3dModelView.MStatus) -> MString

        Synopsis
        -----
        Returns the name of the view.

        Returns: 
        ----- 
        The name of the view.

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> status


        '''
        pass

    def viewType(self): 
        '''
        viewType(self) -> MString

        Synopsis
        -----
        Returns a string specifying the view type. The view type should
        be a different string for every class derived from
        MPx3dModelView. The default type is "MPx3dModelView".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def preMultipleDraw(self): 
        '''
        preMultipleDraw(self)

        Synopsis
        -----
        This method is called before any drawing is performed in the
        model view. It should control any setting required for every pass
        that will be drawn.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def postMultipleDraw(self): 
        '''
        postMultipleDraw(self)

        Synopsis
        -----
        This method is called after the drawing is finished. Any cleanup
        should be done by this method.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def preMultipleDrawPass(self, index: int): 
        '''
        preMultipleDrawPass(self, index: int)

        Synopsis
        -----
        This method is called immediately before a specific pass is about
        to be drawn. The unsigned int argument indictates which pass is
        about to be drawn.Typically the camera (set with the
        setCameraInDraw method) and any pass specific settings would be
        made here.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> A number indicating which pass is about to be drawn. 


        '''
        pass

    def postMultipleDrawPass(self, index: int): 
        '''
        postMultipleDrawPass(self, index: int)

        Synopsis
        -----
        This method is called when a specified pass is finshed.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> A number indicating which pass was just drawn. 


        '''
        pass

    def okForMultipleDraw(self, dp: MDagPath): 
        '''
        okForMultipleDraw(self, dp: MDagPath) -> bool

        Synopsis
        -----
        This method provides some filter capabilities as to what is
        drawn. When ever a draw operation during the multiple camera
        drawing, this method will get called. If true is returned, then
        the object will be drawn.This method is useful for filtering out
        multiple occurances of manipulators and ground planes.To reduce
        the number of objects queried, look at the setViewSelected()
        method along with the setObjectsToView() method.

        Returns: 
        ----- 
        true if it is OK to draw the passed object.

        Parameters:
        -----
        dp: MDagPath
        	[in] -> A 


        '''
        pass

    def multipleDrawPassCount(self): 
        '''
        multipleDrawPassCount(self) -> int

        Synopsis
        -----
        This method returns the number of multiple draw passes that are
        going to be made. By default a 1 is returned.

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

    def setMultipleDrawEnable(self, enable: bool): 
        '''
        setMultipleDrawEnable(self, enable: bool)

        Synopsis
        -----
        This method turns enables/disables multiple camera drawing for
        this view. If multiple draw is disabled, then this view will
        behave like a normal Maya view.

        Returns:
        -----
        None

        Parameters:
        -----
        enable: bool
        	[in] -> If true, then multiple draw is enabled. 


        '''
        pass

    def destroyOnPanelDestruction(self): 
        '''
        destroyOnPanelDestruction(self) -> bool

        Synopsis
        -----
        This method queries the destruction setting for this
        MPx3dModelView which is employed when the panel associated with
        this view is destroyed. By choosing to have the MPx3dModelView
        destroyed along with the panel, you are guaranteed that a new
        MPx3dModelView will be created the next time the editor is
        displayed.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setDestroyOnPanelDestruction(self, how: bool): 
        '''
        setDestroyOnPanelDestruction(self, how: bool)

        Synopsis
        -----
        This method enables/disables destruction of the MPx3dModelView
        object when the panel is destroyed. By default, Maya does not
        destroy the MPx3dModelView when the panel is destroyed. Example
        cases of destroying a panel are when you tear off a panel, or
        close a torn-off panel.By choosing to have the MPx3dModelView
        destroyed along with the panel, you are guaranteed that a new
        MPx3dModelView will be created the next time the editor is
        displayed.

        Returns:
        -----
        None

        Parameters:
        -----
        how: bool
        	[in] -> If true, destroy the 


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

    def removingCamera(self, cameraPath: MDagPath): 
        '''
        removingCamera(self, cameraPath: MDagPath)

        Synopsis
        -----
        This method should be overloaded in MPx3dModelView derived
        classes. It will get called whenever a camera that was used with
        this MPx3dModelView is deleted. The MPx3dModelView should then
        remove any reference to the deleted camera.

        Returns:
        -----
        None

        Parameters:
        -----
        cameraPath: MDagPath
        	[in] -> The 


        '''
        pass

    def setDoUpdateOnMove(self, value: bool): 
        '''
        setDoUpdateOnMove(self, value: bool)

        Synopsis
        -----
        Some viewports require a refresh when the user has moved the top
        level window. This flag enables this custom view to trigger a
        refresh event when the top level window of the view is moved to a
        new location.The default value for this flag is false.

        Returns:
        -----
        None

        Parameters:
        -----
        value: bool
        	[in] -> The state of the doUpdateOnMove flag.


        '''
        pass

    def doUpdateOnMove(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        doUpdateOnMove(self, ReturnStatus: MPx3dModelView.MStatus) -> bool

        Synopsis
        -----
        Returns the state of the doUpdateOnMove flag. This flag tells the
        refresh architecture if it is necessary to refresh your view when
        the user moves the control window for this viewport. If this flag
        is true, then refresh will be triggered on window move.

        Returns: 
        ----- 
        the state of the doUpdateOnMove flag

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[in] -> return status of the check


        '''
        pass

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

    def drawText(self, text: MString,
                        position: MPoint,
                        textPosition: M3dView.M3dView): 
        '''
        drawText(self, text: MString,
                        position: MPoint,
                        textPosition: M3dView.M3dView)

        Synopsis
        -----
        Draws the given text at the given spot in the default font. This
        method is provided as a convienient way to draw OpenGL text.

        Returns:
        -----
        None

        Parameters:
        -----
        text: MString
        	[in] -> Text to draw 

        position: MPoint
        	[in] -> Position in space to draw at 

        textPosition: M3dView.M3dView
        	[in] -> Text position relative to the point


        '''
        pass

    def beginGL(self): 
        '''
        beginGL(self)

        Synopsis
        -----
        Setup port for native OpenGL drawing calls. Only make openGL
        calls between the beginGL() and endGL() methods. M3dView and
        MPx3dModelView calls should not be made betwen beginGL() and
        endGL() calls.This should only be used if there is not a M3dView
        or MPx3dModelView method that performs the required task.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def endGL(self): 
        '''
        endGL(self)

        Synopsis
        -----
        End OpenGL drawing.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setCameraInDraw(self, camera: MDagPath): 
        '''
        setCameraInDraw(self, camera: MDagPath)

        Synopsis
        -----
        Sets the camera during a draw. If the normal setCamera() method
        is used, then that camera will not get its parameters loaded
        during the draw.

        Returns:
        -----
        None

        Parameters:
        -----
        camera: MDagPath
        	[in] -> Dag path of the camera


        '''
        pass

    @overload
    def setDrawCameraOverride(self, worldMatrix: MMatrix,
                        projectionMatrix: MMatrix,
                        left: double,
                        right: double,
                        bottom: double,
                        top: double,
                        nearpt: double,
                        farpt: double,
                        isOrtho: bool): 
        '''
        setDrawCameraOverride(self, worldMatrix: MMatrix,
                        projectionMatrix: MMatrix,
                        left: double,
                        right: double,
                        bottom: double,
                        top: double,
                        nearpt: double,
                        farpt: double,
                        isOrtho: bool)

        Synopsis
        -----
        Sets the camera during a draw. Users must supply all of the
        parameters of the cameras. This only affects the draw
        matrices.Maya uses view frustum culling to remove objects from
        the draw loop. To override the draw camera, you must also provide
        the frustum left, right, bottom, top parameters.

        Returns:
        -----
        None

        Parameters:
        -----
        worldMatrix: MMatrix
        	[in] -> the worldMatrix of the camera. This will be used to construct the view matrix. 

        projectionMatrix: MMatrix
        	[in] -> projection matrix of the camera. 

        left: double
        	[in] -> the left edge of the frustum. 

        right: double
        	[in] -> the right edge of the frustum. 

        bottom: double
        	[in] -> the bottom edge of the frustum. 

        top: double
        	[in] -> the top edge of the frustum. 

        nearpt: double
        	[in] -> the near pt of the frustum. 

        farpt: double
        	[in] -> the far pt of the frustum. 

        isOrtho: bool
        	[in] -> indicates if the frustum pts correspond to an ortho camera (default is false). 


        '''
        pass

    @overload
    def setDrawCameraOverride(self, worldMatrix: MMatrix,
                        projectionMatrix: MMatrix,
                        frustum: MPointArray): 
        '''
        setDrawCameraOverride(self, worldMatrix: MMatrix,
                        projectionMatrix: MMatrix,
                        frustum: MPointArray)

        Synopsis
        -----
        Sets the camera during a draw. Users must supply all of the
        parameters of the cameras. This only affects the draw
        matrices.Maya uses view frustum culling to remove objects from
        the draw loop. To override the draw camera, you must also provide
        the frustum points so that objects and be appropriately culled
        from the scene.

        Returns:
        -----
        None

        Parameters:
        -----
        worldMatrix: MMatrix
        	[in] -> the worldMatrix of the camera. This will be used to construct the view matrix. 

        projectionMatrix: MMatrix
        	[in] -> projection matrix of the camera. 

        frustum: MPointArray
        	[in] -> The 8 frustum points in the following order nearBottomLeft, nearBottomRight, nearTopLeft, nearTopRight, farBottomLeft, farBottomRight, farTopLeft, farTopRight 


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

    def setCameraSet(self, cameraSet: MObject): 
        '''
        setCameraSet(self, cameraSet: MObject)

        Synopsis
        -----
        Set the cameraSet for this view.

        Returns:
        -----
        None

        Parameters:
        -----
        cameraSet: MObject
        	[in] -> cameraSet object for this view


        '''
        pass

    def getCameraSet(self, cameraSet: MObject): 
        '''
        getCameraSet(self, cameraSet: MObject)

        Synopsis
        -----
        Get the cameraSet for this view.

        Returns:
        -----
        None

        Parameters:
        -----
        cameraSet: MObject
        	[out] -> dependency node object for the cameraSet (allocated by caller)


        '''
        pass

    def setCurrentCameraSetCamera(self, cameraName: MString): 
        '''
        setCurrentCameraSetCamera(self, cameraName: MString)

        Synopsis
        -----
        Set a camera used by the currently specified cameraSet as the
        controlled camera for this view.

        Returns:
        -----
        None

        Parameters:
        -----
        cameraName: MString
        	[in] -> camera layer camera name for this view


        '''
        pass

    def getCurrentCameraSetCamera(self, cameraName: MString): 
        '''
        getCurrentCameraSetCamera(self, cameraName: MString)

        Synopsis
        -----
        Get the cameraSet for this view.

        Returns:
        -----
        None

        Parameters:
        -----
        cameraName: MString
        	[out] -> dependency node object for the cameraSet (allocated by caller)


        '''
        pass

    def getCameraHUDName(self): 
        '''
        getCameraHUDName(self) -> MString

        Synopsis
        -----
        Return the name to use for the camera in the heads up display.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setDisplayHUD(self, enable: bool): 
        '''
        setDisplayHUD(self, enable: bool)

        Synopsis
        -----
        Enables or disables the drawing the heads up display in this
        view. This method only affects this view and will stop all heads
        up display elements from being drawn in this view.

        Returns:
        -----
        None

        Parameters:
        -----
        enable: bool
        	[in] -> The enable state of the heads up display in this view.


        '''
        pass

    def displayHUD(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        displayHUD(self, ReturnStatus: MPx3dModelView.MStatus) -> bool

        Synopsis
        -----
        Returns the heads up display state for this view.

        Returns: 
        ----- 
        The enable state for the HUD

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> the return status


        '''
        pass

    def drawHUDNow(self): 
        '''
        drawHUDNow(self)

        Synopsis
        -----
        Forces the HUD viewport elements to be drawn immediately. This
        should only be called when setDrawAdornments has been set to
        false. And this method should only be called in the postMultiple*
        draw methods. This allows the drawing of display elements during
        a specific pass while attached to a specific camera.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setDrawAdornments(self, display: bool): 
        '''
        setDrawAdornments(self, display: bool)

        Synopsis
        -----
        Toggles the control of how adornments are drawn in the view.
        Adornments are objects that are drawn in the viewport that are
        not scene entities. This includes the origin axis and the camera
        decorations like film gate and resolution gate. These items are
        usually drawn last and outside of the multiple refresh loop. You
        can choose to disable the drawing of the adornments by specifying
        false here, and you can control the drawing of the feature within
        their display loop calling displayAdornmentsNow() method on this
        class. By default this flag is true; so adornments are always
        drawn unless explicitly disabled by you.

        Returns:
        -----
        None

        Parameters:
        -----
        display: bool
        	[in] -> toggle to control the display of the adornments.


        '''
        pass

    def drawAdornments(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        drawAdornments(self, ReturnStatus: MPx3dModelView.MStatus) -> bool

        Synopsis
        -----
        Returns the state of the adornment drawing for this view. See
        setDrawAdornments for more information on adornment drawing.

        Returns:
        -----
        None

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> Status code. 


        '''
        pass

    def drawAdornmentsNow(self): 
        '''
        drawAdornmentsNow(self)

        Synopsis
        -----
        Forces the adornment viewport elements to be drawn immediately.
        This should only be called when setDrawAdornments has been set to
        false. And this method should only be called in the postMultiple*
        draw methods. This allows you to draw camera adornments during a
        specific pass while attached to a specific camera.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setDisplayAxis(self, enable: bool): 
        '''
        setDisplayAxis(self, enable: bool)

        Synopsis
        -----
        Sets the axis display in the MPx3dModelView.

        Returns:
        -----
        None

        Parameters:
        -----
        enable: bool
        	[in] -> If true, then the axis is displayed.


        '''
        pass

    def displayAxisOn(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        displayAxisOn(self, ReturnStatus: MPx3dModelView.MStatus) -> bool

        Synopsis
        -----
        Returns the axis display state for this MPx3dModelView.

        Returns: 
        ----- 
        true if the axis is displayed.

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> The return status.


        '''
        pass

    def setDisplayAxisAtOrigin(self, enable: bool): 
        '''
        setDisplayAxisAtOrigin(self, enable: bool)

        Synopsis
        -----
        Sets the origin axis display in the MPx3dModelView.

        Returns:
        -----
        None

        Parameters:
        -----
        enable: bool
        	[in] -> If true, then the origin axis is displayed.


        '''
        pass

    def displayAxisAtOriginOn(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        displayAxisAtOriginOn(self, ReturnStatus: MPx3dModelView.MStatus) -> bool

        Synopsis
        -----
        Returns the origin axis display state for this MPx3dModelView.

        Returns: 
        ----- 
        true if the origin axis is displayed.

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> The return status.


        '''
        pass

    def setDisplayCameraAnnotation(self, enable: bool): 
        '''
        setDisplayCameraAnnotation(self, enable: bool)

        Synopsis
        -----
        Sets the camera annotation display in the MPx3dModelView.

        Returns:
        -----
        None

        Parameters:
        -----
        enable: bool
        	[in] -> If true, then the camera annotation is displayed.


        '''
        pass

    def displayCameraAnnotationOn(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        displayCameraAnnotationOn(self, ReturnStatus: MPx3dModelView.MStatus) -> bool

        Synopsis
        -----
        Returns the camera annotation display state for this
        MPx3dModelView.

        Returns: 
        ----- 
        true if the camera annotation is displayed.

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> The return status.


        '''
        pass

    def isVisible(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        isVisible(self, ReturnStatus: MPx3dModelView.MStatus) -> bool

        Synopsis
        -----
        This method returns true if this view is visible, otherwise false
        is returned.

        Returns: 
        ----- 
        true if the view is visible, otherwise false is returned.

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> The return status.


        '''
        pass

    def displayStyle(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        displayStyle(self, ReturnStatus: MPx3dModelView.MStatus) -> M3dView.M3dView

        Synopsis
        -----
        Return the display style for this 3d view. The display style can
        be wireframe, flat-shaded, or smooth-shaded.

        Returns: 
        ----- 
        The display style for this view

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> Status code


        '''
        pass

    def isShadeActiveOnly(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        isShadeActiveOnly(self, ReturnStatus: MPx3dModelView.MStatus) -> bool

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
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> Status code


        '''
        pass

    def setDisplayStyle(self, style: M3dView.M3dView,
                        activeOnly: bool): 
        '''
        setDisplayStyle(self, style: M3dView.M3dView,
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
        style: M3dView.M3dView
        	[in] -> The display style to be set for this view 

        activeOnly: bool
        	[in] -> Specifies whether only active objects are to be shaded in shaded mode.


        '''
        pass

    def portWidth(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        portWidth(self, ReturnStatus: MPx3dModelView.MStatus) -> int

        Synopsis
        -----
        Returns the width of the current viewport.

        Returns: 
        ----- 
        The width of this viewport

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> Status Code


        '''
        pass

    def portHeight(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        portHeight(self, ReturnStatus: MPx3dModelView.MStatus) -> int

        Synopsis
        -----
        Returns the height of the current viewport.

        Returns: 
        ----- 
        The height of this viewport

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> Status Code


        '''
        pass

    def beginXorDrawing(self, drawOrthographic: bool,
                        disableDepthTesting: bool,
                        lineWidth: float,
                        stipplePattern: M3dView.M3dView,
                        lineColor: MColor): 
        '''
        beginXorDrawing(self, drawOrthographic: bool,
                        disableDepthTesting: bool,
                        lineWidth: float,
                        stipplePattern: M3dView.M3dView,
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

        stipplePattern: M3dView.M3dView
        	[in] -> Line stipple pattern. Default is 

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

    @overload
    def setDrawColor(self, index: int,
                        table: M3dView.M3dView): 
        '''
        setDrawColor(self, index: int,
                        table: M3dView.M3dView)

        Synopsis
        -----
        Set the color to draw in. The index argument is an index into the
        application's color tables. Valid values range between zero and
        the size of the table minus one. The size of the active and
        dormant color tables can be found using methods of this class.
        The background and template color tables are both of size
        one.These indices do not directly correspond to those of the
        underlying OpenGL color index mode. Using the glIndex call
        directly is not recommended and may cause unpredictable results.
        This method should be used instead.Note that this method will
        work in either RGBA mode or color index mode.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> index of the color to draw in 

        table: M3dView.M3dView
        	[in] -> color table to index into


        '''
        pass

    @overload
    def setDrawColor(self, color: MColor): 
        '''
        setDrawColor(self, color: MColor)

        Synopsis
        -----
        Set the color to draw in. This method should only be used in RGBA
        mode. It is a convenient replacement for glColor.

        Returns:
        -----
        None

        Parameters:
        -----
        color: MColor
        	[in] -> color to draw in


        '''
        pass

    def numDormantColors(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        numDormantColors(self, ReturnStatus: MPx3dModelView.MStatus) -> int

        Synopsis
        -----
        Returns the number of dormant object colors in the internal
        application color table.

        Returns: 
        ----- 
        The number of dormant colors

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> Status code


        '''
        pass

    def numActiveColors(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        numActiveColors(self, ReturnStatus: MPx3dModelView.MStatus) -> int

        Synopsis
        -----
        Returns the number of active object colors in the internal
        application color table.

        Returns: 
        ----- 
        The number of active colors

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> Status code


        '''
        pass

    def numUserDefinedColors(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        numUserDefinedColors(self, ReturnStatus: MPx3dModelView.MStatus) -> int

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
        ReturnStatus: MPx3dModelView.MStatus
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
                        ReturnStatus: MPx3dModelView.MStatus): 
        '''
        userDefinedColorIndex(self, index: int,
                        ReturnStatus: MPx3dModelView.MStatus) -> int

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

        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> Status code


        '''
        pass

    def isBackgroundGradient(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        isBackgroundGradient(self, ReturnStatus: MPx3dModelView.MStatus) -> bool

        Synopsis
        -----
        Returns whether a gradient is being used as the background color.

        Returns: 
        ----- 
        true background is a color gradient  false background is a solid
        color

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> Status code


        '''
        pass

    def templateColor(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        templateColor(self, ReturnStatus: MPx3dModelView.MStatus) -> MColor

        Synopsis
        -----
        Returns the value of the template color.

        Returns: 
        ----- 
        The template color

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> Status code


        '''
        pass

    def backgroundColor(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        backgroundColor(self, ReturnStatus: MPx3dModelView.MStatus) -> MColor

        Synopsis
        -----
        Returns the value of the background color.

        Returns: 
        ----- 
        The background color

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> Status code


        '''
        pass

    def backgroundColorTop(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        backgroundColorTop(self, ReturnStatus: MPx3dModelView.MStatus) -> MColor

        Synopsis
        -----
        Returns the value of the background gradient top color.

        Returns: 
        ----- 
        The background gradient top color

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> Status code


        '''
        pass

    def backgroundColorBottom(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        backgroundColorBottom(self, ReturnStatus: MPx3dModelView.MStatus) -> MColor

        Synopsis
        -----
        Returns the value of the background gradient bottom color.

        Returns: 
        ----- 
        The background gradient bottom color

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> Status code


        '''
        pass

    def colorAtIndex(self, index: int,
                        table: M3dView.M3dView,
                        ReturnStatus: MPx3dModelView.MStatus): 
        '''
        colorAtIndex(self, index: int,
                        table: M3dView.M3dView,
                        ReturnStatus: MPx3dModelView.MStatus) -> MColor

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

        table: M3dView.M3dView
        	[in] -> Table to index into 

        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> Status code


        '''
        pass

    def getColorIndexAndTable(self, glindex: int,
                        index: int,
                        table: M3dView.M3dView): 
        '''
        getColorIndexAndTable(self, glindex: int,
                        index: int,
                        table: M3dView.M3dView)

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

        table: M3dView.M3dView
        	[out] -> Returned ColorTable


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
                        ReturnStatus: MPx3dModelView.MStatus): 
        '''
        worldToView(self, worldPt: MPoint,
                        x_pos: short,
                        y_pos: short,
                        ReturnStatus: MPx3dModelView.MStatus) -> bool

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
        	[out] -> the x position of the point in port coordinates 

        y_pos: short
        	[out] -> the y position of the point in port coordinates 

        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> Status code


        '''
        pass

    def setObjectDisplay(self, displayType: M3dView.M3dView,
                        display: bool): 
        '''
        setObjectDisplay(self, displayType: M3dView.M3dView,
                        display: bool)

        Synopsis
        -----
        Sets the display option for various types of objects. By default
        everything is displayed.

        Returns:
        -----
        None

        Parameters:
        -----
        displayType: M3dView.M3dView
        	[in] -> The type of object to display 

        display: bool
        	[in] -> Should the object type be displayed?


        '''
        pass

    def objectDisplay(self, dispObjs: M3dView.M3dView,
                        ReturnStatus: MPx3dModelView.MStatus): 
        '''
        objectDisplay(self, dispObjs: M3dView.M3dView,
                        ReturnStatus: MPx3dModelView.MStatus) -> bool

        Synopsis
        -----
        Test whether specific types of objects are to be displayed.

        Returns: 
        ----- 
        True if any of the object types specified by dispObjs are set to
        be displayed.

        Parameters:
        -----
        dispObjs: M3dView.M3dView
        	[in] -> Bit mask of object display flags to be tested. 

        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> Status code.


        '''
        pass

    def setBackfaceCulling(self, culling: bool): 
        '''
        setBackfaceCulling(self, culling: bool)

        Synopsis
        -----
        Sets backface culling.

        Returns:
        -----
        None

        Parameters:
        -----
        culling: bool
        	[in] -> sets the backface culling state


        '''
        pass

    def isBackfaceCulling(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        isBackfaceCulling(self, ReturnStatus: MPx3dModelView.MStatus) -> bool

        Synopsis
        -----
        Returns the state of backface culling.

        Returns: 
        ----- 
        true if backface culling is enabled.

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> return status


        '''
        pass

    def setWireframeOnShaded(self, onShaded: bool): 
        '''
        setWireframeOnShaded(self, onShaded: bool)

        Synopsis
        -----
        Displays as wireframe on shaded.

        Returns:
        -----
        None

        Parameters:
        -----
        onShaded: bool
        	[in] -> sets the wireframe on shaded state


        '''
        pass

    def isWireframeOnShaded(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        isWireframeOnShaded(self, ReturnStatus: MPx3dModelView.MStatus) -> bool

        Synopsis
        -----
        Returns the state of wireframe on shaded.

        Returns: 
        ----- 
        true if backface onShaded is enabled.

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> return status


        '''
        pass

    def setXrayEnabled(self, xray: bool): 
        '''
        setXrayEnabled(self, xray: bool)

        Synopsis
        -----
        Sets xray display state.

        Returns:
        -----
        None

        Parameters:
        -----
        xray: bool
        	[in] -> sets the xray display state


        '''
        pass

    def isXrayEnabled(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        isXrayEnabled(self, ReturnStatus: MPx3dModelView.MStatus) -> bool

        Synopsis
        -----
        Returns the state of xray display.

        Returns: 
        ----- 
        true if xray is enabled.

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> return status


        '''
        pass

    def setTextureDisplayEnabled(self, textureDisplay: bool): 
        '''
        setTextureDisplayEnabled(self, textureDisplay: bool)

        Synopsis
        -----
        Enables texture display.

        Returns:
        -----
        None

        Parameters:
        -----
        textureDisplay: bool
        	[in] -> sets the texture display state


        '''
        pass

    def isTextureDisplayEnabled(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        isTextureDisplayEnabled(self, ReturnStatus: MPx3dModelView.MStatus) -> bool

        Synopsis
        -----
        Returns the enable state of texture display.

        Returns: 
        ----- 
        true if texture display is enabled.

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> return status


        '''
        pass

    def setTwoSidedLighting(self, twoSided: bool): 
        '''
        setTwoSidedLighting(self, twoSided: bool)

        Synopsis
        -----
        Enables two sided lighting.

        Returns:
        -----
        None

        Parameters:
        -----
        twoSided: bool
        	[in] -> sets the two sided lighting state


        '''
        pass

    def isTwoSidedLighting(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        isTwoSidedLighting(self, ReturnStatus: MPx3dModelView.MStatus) -> bool

        Synopsis
        -----
        Returns the state of two sided lighting.

        Returns: 
        ----- 
        true if two sided lighting is enabled.

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> return status


        '''
        pass

    def setLightingMode(self, lightingMode: MPx3dModelView.MPx3dModelView): 
        '''
        setLightingMode(self, lightingMode: MPx3dModelView.MPx3dModelView)

        Synopsis
        -----
        Sets the lighting mode.

        Returns:
        -----
        None

        Parameters:
        -----
        lightingMode: MPx3dModelView.MPx3dModelView
        	[in] -> sets the lighting mode


        '''
        pass

    def lightingMode(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        lightingMode(self, ReturnStatus: MPx3dModelView.MStatus) -> MPx3dModelView.MPx3dModelView

        Synopsis
        -----
        Returns the lighting mode.

        Returns: 
        ----- 
        The lighting mode.

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> return status


        '''
        pass

    def setFogEnabled(self, state: bool): 
        '''
        setFogEnabled(self, state: bool)

        Synopsis
        -----
        Enables and disables fog. If fog is enabled for one pass and
        disabled for another, the background fog will not be drawn. To
        display background fog in that configuration, use the
        MPx3dModelView::setBackgroundFogEnabled() call.

        Returns:
        -----
        None

        Parameters:
        -----
        state: bool
        	[in] -> true is fog should be on.


        '''
        pass

    def isFogEnabled(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        isFogEnabled(self, ReturnStatus: MPx3dModelView.MStatus) -> bool

        Synopsis
        -----
        Returns true if fog is enabled.

        Returns: 
        ----- 
        true is fog is enabled.

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> status


        '''
        pass

    def fogSource(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        fogSource(self, ReturnStatus: MPx3dModelView.MStatus) -> MPx3dModelView.MPx3dModelView

        Synopsis
        -----
        Returns the algorithm used to compute fog. See
        MPx3dModelView::setFogSource for a description.

        Returns: 
        ----- 
        The algorithm used to compute fog.

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> status


        '''
        pass

    def setFogSource(self, source: MPx3dModelView.MPx3dModelView): 
        '''
        setFogSource(self, source: MPx3dModelView.MPx3dModelView)

        Synopsis
        -----
        Sets the type of fog algorithm to use. If the source argument is
        kFogFragment (default) then fog is computed per pixel. If the
        argument is kFogCoordinate then if the geometry has specified
        vertex fog coordinates, and the OpenGL extension for vertex fog
        is supported by the graphics system, then fog is computed per
        vertex.

        Returns:
        -----
        None

        Parameters:
        -----
        source: MPx3dModelView.MPx3dModelView
        	[in] -> The type of algorithm to use.


        '''
        pass

    def fogMode(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        fogMode(self, ReturnStatus: MPx3dModelView.MStatus) -> MPx3dModelView.MPx3dModelView

        Synopsis
        -----
        Return the type of drop off used with fog. See
        MPx3dModelView::setFogMode for description of the drop off types.

        Returns: 
        ----- 
        The type of drop off used with fog.

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> status


        '''
        pass

    def setFogMode(self, mode: MPx3dModelView.MPx3dModelView): 
        '''
        setFogMode(self, mode: MPx3dModelView.MPx3dModelView)

        Synopsis
        -----
        Sets the drop-off mode for fog. The possibilities are:

        Returns:
        -----
        None

        Parameters:
        -----
        mode: MPx3dModelView.MPx3dModelView
        	[in] -> The type of drop off to use with fog.


        '''
        pass

    def fogDensity(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        fogDensity(self, ReturnStatus: MPx3dModelView.MStatus) -> double

        Synopsis
        -----
        Returns the fog density.

        Returns: 
        ----- 
        The fog density.

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> status


        '''
        pass

    def setFogDensity(self, density: double): 
        '''
        setFogDensity(self, density: double)

        Synopsis
        -----
        Determines the density of hardware fogging. This is meaniful for
        kFogExponential and kFogExponentialSquared drop off types (set by
        the MPx3dModelView::setFogMode() method).

        Returns:
        -----
        None

        Parameters:
        -----
        density: double
        	[in] -> 


        '''
        pass

    def fogStart(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        fogStart(self, ReturnStatus: MPx3dModelView.MStatus) -> double

        Synopsis
        -----
        Returns the fog start position.

        Returns: 
        ----- 
        The fog start position.

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> status


        '''
        pass

    def setFogStart(self, start: double): 
        '''
        setFogStart(self, start: double)

        Synopsis
        -----
        Determines the start location of hardware fogging. This is
        meaniful for kFogLinear drop off type (set by the
        MPx3dModelView::setFogMode() method).

        Returns:
        -----
        None

        Parameters:
        -----
        start: double
        	[in] -> 


        '''
        pass

    def fogEnd(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        fogEnd(self, ReturnStatus: MPx3dModelView.MStatus) -> double

        Synopsis
        -----
        Returns the fog end position.

        Returns: 
        ----- 
        The fog end location.

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> status


        '''
        pass

    def setFogEnd(self, end: double): 
        '''
        setFogEnd(self, end: double)

        Synopsis
        -----
        Determines the end location of hardware fogging. This is meaniful
        for kFogLinear drop off type (set by the
        MPx3dModelView::setFogMode() method).

        Returns:
        -----
        None

        Parameters:
        -----
        end: double
        	[in] -> 


        '''
        pass

    def fogColor(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        fogColor(self, ReturnStatus: MPx3dModelView.MStatus) -> MColor

        Synopsis
        -----
        Returns the fog color.

        Returns: 
        ----- 
        The fog color.

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> status


        '''
        pass

    def setFogColor(self, color: MColor): 
        '''
        setFogColor(self, color: MColor)

        Synopsis
        -----
        Sets the color used for hardware fogging.

        Returns:
        -----
        None

        Parameters:
        -----
        color: MColor
        	[in] -> The color used by hardware fogging.


        '''
        pass

    def isBackgroundFogEnabled(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        isBackgroundFogEnabled(self, ReturnStatus: MPx3dModelView.MStatus) -> bool

        Synopsis
        -----
        Returns true if the background fog is enabled.

        Returns: 
        ----- 
        true, if the background fog is enabled, otherwise false.

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> status


        '''
        pass

    def setBackgroundFogEnabled(self, state: bool): 
        '''
        setBackgroundFogEnabled(self, state: bool)

        Synopsis
        -----
        Enables and disables background fog.

        Returns:
        -----
        None

        Parameters:
        -----
        state: bool
        	[in] -> true if background fog should be enabled.


        '''
        pass

    def viewSelectedPrefix(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        viewSelectedPrefix(self, ReturnStatus: MPx3dModelView.MStatus) -> MString

        Synopsis
        -----
        Returns the prefix used when displaying the camera name in the
        heads up display when view selected in on.

        Returns: 
        ----- 
        The prefix.

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
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

    def viewSelected(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        viewSelected(self, ReturnStatus: MPx3dModelView.MStatus) -> bool

        Synopsis
        -----
        Returns the state of view selected for this view.

        Returns: 
        ----- 
        true if view selected is enabled.

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> return status


        '''
        pass

    def setViewSelected(self, enable: bool): 
        '''
        setViewSelected(self, enable: bool)

        Synopsis
        -----
        Enables the view selected mode.

        Returns:
        -----
        None

        Parameters:
        -----
        enable: bool
        	[in] -> enable or disable view selected mode.


        '''
        pass

    def viewSelectedSet(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        viewSelectedSet(self, ReturnStatus: MPx3dModelView.MStatus) -> MObject

        Synopsis
        -----
        Returns an MObject for the set used by view selected. If there is
        not a set associated with this view, then an invalid MObject will
        be returned. Check the isNull() method of the MObject to see if a
        valid set was found.

        Returns: 
        ----- 
        The MObject

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
        	[out] -> return status


        '''
        pass

    def setViewSelectedSet(self, set: MObject): 
        '''
        setViewSelectedSet(self, set: MObject)

        Synopsis
        -----
        Sets the list of objects used by view selected as an object set.
        View selected must be turned on for this to have an effect.

        Returns:
        -----
        None

        Parameters:
        -----
        set: MObject
        	[in] -> The object set to be used by view selected.


        '''
        pass

    def getObjectsToView(self, list: MSelectionList): 
        '''
        getObjectsToView(self, list: MSelectionList)

        Synopsis
        -----
        Returns a selection list containing all of the objects on the
        view selected list.

        Returns:
        -----
        None

        Parameters:
        -----
        list: MSelectionList
        	[out] -> The list of objects used by view selected.


        '''
        pass

    def setObjectsToView(self, list: MSelectionList): 
        '''
        setObjectsToView(self, list: MSelectionList)

        Synopsis
        -----
        Sets the list of objects used by view selected as a selection
        list. View selected must be turned on for this to have an effect.

        Returns:
        -----
        None

        Parameters:
        -----
        list: MSelectionList
        	[in] -> The objects to view with view selected.


        '''
        pass

    def viewIsFiltered(self, ReturnStatus: MPx3dModelView.MStatus): 
        '''
        viewIsFiltered(self, ReturnStatus: MPx3dModelView.MStatus) -> bool

        Synopsis
        -----
        Returns the state of view filtering for this view. This includes
        both view selected state and additional object list filters.

        Returns: 
        ----- 
        True if the view is filtered.

        Parameters:
        -----
        ReturnStatus: MPx3dModelView.MStatus
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

    def hasStereoBufferSupport(self): 
        '''
        hasStereoBufferSupport(self) -> bool

        Synopsis
        -----
        Returns true if this 3dModelView is running in stereo buffer
        mode. This should be used in cases where the API developer has
        requested to create stereo buffer enabled view. See
        wantStereoGLBuffer()

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getAsM3dView(self, view: M3dView): 
        '''
        getAsM3dView(self, view: M3dView)

        Synopsis
        -----
        Get this MPx3dModelView as a M3dView.

        Returns:
        -----
        None

        Parameters:
        -----
        view: M3dView
        	[out] -> The 


        '''
        pass

    def wantStereoGLBuffer(self): 
        '''
        wantStereoGLBuffer(self) -> bool

        Synopsis
        -----
        Users should override this method if they want a stereo buffer
        enabled MPx3dModelView. You must have a graphics card that can
        support stereo mode. If your graphics card does not support
        stereo mode, a non-stereo buffer is created.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setInStereoDrawMode(self, flag: bool): 
        '''
        setInStereoDrawMode(self, flag: bool)

        Synopsis
        -----
        Derived classes should call this method to indicate to Maya
        whether the view is currently drawing in stereo. One place where
        this is useful to know is for playblast which will check the view
        to see if it is in stereo mode, and enforce rendering of left and
        right stereo pairs versus mono rendering.

        Returns:
        -----
        None

        Parameters:
        -----
        flag: bool
        	[in] -> Flag telling if drawing in stereo mode.


        '''
        pass

    def requestOkForDraw(self, request: MDrawRequest): 
        '''
        requestOkForDraw(self, request: MDrawRequest) -> bool

        Synopsis
        -----
        This method provides some filter capabilities as to what is
        drawn. When ever a draw operation during the multiple camera
        drawing, this method will get called. If true is returned, then
        the object will be drawn.This method is useful for excluding
        types of material from the draw loop.

        Returns: 
        ----- 
        true if it is OK to draw the passed object.

        Parameters:
        -----
        request: MDrawRequest
        	[in] -> A 


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

class LightingMode:
    '''Lighting mode used in this view. 
    Non-functional class.  Values for this enum:
    kLightAll
    kLightSelected
    kLightActive
    kLightDefault
    kLightNone
    kLightQuality
    '''

    def __init__(self):
        pass

    def kLightAll(self):
        '''This is an enum of LightingMode.
        - Description: Use all lights. 
        - Value: 0
        '''
        pass

    def kLightSelected(self):
        '''This is an enum of LightingMode.
        - Description: Selected lights only. 
        - Value: 1
        '''
        pass

    def kLightActive(self):
        '''This is an enum of LightingMode.
        - Description: Active lights only. 
        - Value: 2
        '''
        pass

    def kLightDefault(self):
        '''This is an enum of LightingMode.
        - Description: Default light only. 
        - Value: 3
        '''
        pass

    def kLightNone(self):
        '''This is an enum of LightingMode.
        - Description: Use no lights. 
        - Value: 4
        '''
        pass

    def kLightQuality(self):
        '''This is an enum of LightingMode.
        - Description: Use per pixel lighting. 
        - Value: 5
        '''
        pass

class FogSource:
    '''Fog computation modes. 
    Non-functional class.  Values for this enum:
    kFogFragment
    kFogCoordinate
    '''

    def __init__(self):
        pass

    def kFogFragment(self):
        '''This is an enum of FogSource.
        - Description: Computed per pixel (default). 
        - Value: 0
        '''
        pass

    def kFogCoordinate(self):
        '''This is an enum of FogSource.
        - Description: Computed by specified vertex fog coordinates. 
        - Value: 1
        '''
        pass

class FogMode:
    '''Drop-off modes for fog. 
    Non-functional class.  Values for this enum:
    kFogLinear
    kFogExponential
    kFogExponentialSquared
    '''

    def __init__(self):
        pass

    def kFogLinear(self):
        '''This is an enum of FogMode.
        - Description: Linear drop off. 
        - Value: 0
        '''
        pass

    def kFogExponential(self):
        '''This is an enum of FogMode.
        - Description: Exponential drop-off. 
        - Value: 1
        '''
        pass

    def kFogExponentialSquared(self):
        '''This is an enum of FogMode.
        - Description: Squared exponential drop-off. 
        - Value: 2
        '''
        pass

class MPxAnimCurveInterpolator:
    '''Base Class for User-defined Animation Curve Interpolation Types.
MPxAnimCurveInterpolator is the base class for user defined Anim Curve Interpolation
Types. It allows for the creation and evaluation of customized
animation curves, in addition to determination of the type ID and
name of the curve. The evaluation of an animCurve between two of
its keyframes is determined by interpolators (also known as
"tangent types") at those keyframes. This class allows for the
creation of custom tangent types. Note that the valid type ranges
are:
Types 1 to 18 Maya's built-in tangent types. See
MFnAnimCurve::TangentType. Types 19 to 26 Custom tangent types which are available to all
users, and should only be used internally. Types 27 to 63 Maya's
built-in tangent types. See
MFnAnimCurve::TangentType. Types 64 to 32767 Custom tangent types which can be reserved by
customers. You can request between 1 to 8 id's per request. Visit
Autodesk Maya Developer Tangent Types ID Block Registration to submit your request. See also
Autodesk Developer Network for more information.
'''
    def __init__(self):
        pass


    def initialize(self, animCurve: MObject,
                        keyIndex: int): 
        '''
        initialize(self, animCurve: MObject,
                        keyIndex: int)

        Synopsis
        -----
        Initialize the interpolator to evaluate keyframe values within
        the time span of the given interval. The interval starts at the
        keyframe denoted by the value of the interval and continues to
        the next keyframe.It is not necessary to override this method.

        Returns:
        -----
        None

        Parameters:
        -----
        animCurve: MObject
        	[in] -> 

        keyIndex: int
        	[in] -> 


        '''
        pass

    def evaluate(self, val: MTime): 
        '''
        evaluate(self, val: MTime) -> double

        Synopsis
        -----
        Compute an interpolated keyframe value at the given time, which
        is an absolute time between the start and end times.

        Returns: 
        ----- 
        interpolated keyframe value

        Parameters:
        -----
        val: MTime
        	[in] -> specified time value


        '''
        pass

    def typeId(self): 
        '''
        typeId(self) -> MFnAnimCurve.MFnAnimCurve

        Synopsis
        -----
        Returns the tangent type of this curve.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def typeName(self): 
        '''
        typeName(self) -> MString

        Synopsis
        -----
        Returns the name under which the interpolator type was
        registered. The name is used in the UI and when specifying a
        tangent type to the keyTangent command.It is not necessary to
        override this method.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class InterpolatorFlags:
    '''Defines the flags used when registering a new animation curve iterpolator. 
    Non-functional class.  Values for this enum:
    kEvaluateAtKey
    kLockType
    '''

    def __init__(self):
        pass

    def kEvaluateAtKey(self):
        '''This is an enum of InterpolatorFlags.
        - Description: Animation curves do not typically evaluate at the keyframe times. Instead, the keyframe value is used. For custom interpolators that may want to define their curves such that they do not pass through the keyframe values, kEvaluateAtKey can be set which will cause the interpolator to be evaluated at the keyframe times. 
        - Value: 1
        '''
        pass

    def kLockType(self):
        '''This is an enum of InterpolatorFlags.
        - Description: Many curve operations to move keys or change tangent types may cause a ripple of tangent type changes for neighboring keyframes to a tangent type known to be compatible with the new curve shape. Some custom interpolators may be able to accomodate such changes to neighboring keyframes without being exchanged for a different type. Setting kLockType will prevent the custom tangent type from being automatically exchanged. 
        - Value: 2
        '''
        pass

class MPxAssembly:
    '''Parent class of all user defined assembly nodes.
MPxAssembly is the parent class of all user defined assembly nodes. User
defined assemblies are DAG nodes. An assembly allows activation
of one of its representations. The implementation of
representations is not specified by the
MPxAssembly API: for example, a representation can be a data structure
internal to the assembly implementation, identified by string
name, or it can be a DAG node.
An assembly object is also a DAG container. As such, operations
on containers can be done on assemblies.
This class can be used to implement new kinds of assembly nodes
within Maya that integrate with Maya's scene assembly workflows.
For use of assemblies, see function set
MFnAssembly. For use of container functionality on assemblies, see function
set
MFnContainerNode.
To extend Maya's scene assembly, you can write a dependency graph
plug-in with an assembly node that is derived from
MPxAssembly. The plug-in can be written either in C++ or in Python. A
minimal scene assembly node must maintain a list of
representations, and be able to activate one of them,
inactivating the previous representation in the process.
An
MPxAssembly derived node must be created with no representation active. In
other words, after the
MPxAssembly derived class constructor executes, the
getActive() method must return the empty string. This is to ensure support
for workflows where nested assembly hierarchies are expanded a
single level at a time.
The fundamental properties of a representation are the following:
Here is a summary description of how to override
MPxAssembly methods to implement a scene assembly node. The following
MPxAssembly pure virtual methods must be overriden by even the most basic
scene assembly node.
All other virtual methods have default implementations in
MPxAssembly. Please refer to the documentation of these methods to determine
if this default behavior is appropriate for your plug-in.
Assembly nodes can track certain edits done on their members.
These edits are non-destructive and recorded separately from the
representation data onto which they are applied. Please see the
Maya documentation for more details. Edits are a property of the
assembly node, not of individual representations, and when
switching active representations will be applied to a newly-
activated representation if the representation can apply edits
(see
canRepApplyEdits()).
A plug-in node can opt in to the Maya edit tracking system simply
by overriding
supportsEdits() to return true.
To interact with edits once they have been created, see
MItEdits.
To avoid node name clashes on member nodes, each assembly node
can optionally have a representation namespace, a namespace into
which all nodes resulting from activating a representation will
be placed. This representation namespace is always a child
namespace of the namespace in which the assembly node itself has
been placed. In the case of nested assemblies, this will produce
a hierarchy of namespaces that matches the hierarchy of
assemblies.
Without the use of namespaces, member node name clashes will be
resolved by Maya adding a numerical suffix to clashing nodes. If
an assembly node is tracking edits on its members, this name
clash resolution will cause edits to fail, as edits are applied
by name. Therefore, the use of representation namespaces is very
strongly recommended when tracking assembly member edits.
An
MPxAssembly derived class can completely override the activation of a
representation (and therefore inactivation of the previously-
active representation) provided by
activate(). However,
MPxAssembly provides the
performActivate() and
performInactivate() non-virtual methods as building blocks from which a derived
class
activate() method can be implemented. See the
performActivate() and
performInactivate() methods for a description of services that can be useful to
derived class implementations of
activate().
Once a derived assembly node type has been implemented, and
registered into Maya's type system through
MFnPlugin::registerNode(), it should be registered to the assembly command as an available
assembly node type. See the assembly command documentation for
more details.
The default representation inactivation code flushes the undo
queue on activating a new representation. This is done for
performance reasons: undoable inactivation of the previously-
active representation with a very large number of nodes and
attribute connections (e.g. a large and deeply-nested hierarchy)
would require an undoable delete, which is time-consuming (to
record the operations to undo), and memory-consuming (as the undo
data is stored in memory). The consequence of this is that once a
representation switch is done, any operations previously on the
undo queue are lost.
However, this behavior is under plugin control, by overriding
MPxAssembly::inactivateRep(). If the current representation is known to be lightweight (e.g.
in terms of number of Maya nodes), a plugin can bypass the
default representation inactivation code, and implement its own
inactivation using the normal undoable delete, and therefore
preserve undo capability.
Assembly nodes can be created inside a hierarchy of assemblies.
An assembly can be nested inside another assembly; the nested
assembly is a DAG child of its parent assembly.
MFnAssembly::getParentAssembly() and
MFnAssembly::getSubAssemblies() can be used to efficiently navigate the hierarchy of assembly
nodes. Nested assemblies are created through the activation of a
representation on their parent assembly.
An assembly node that does not have an assembly parent is called
a top-level assembly. It is created through file I/O (either
opening a file, or importing a file at the top level), or through
scripting. Top-level assemblies have special properties:
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MPxNode.MPxNode

        Synopsis
        -----
        Returns the type of node that this is. This is used to
        differentiate user defined nodes that are derived off different
        MPx base classes.It is not necessary to override this
        method.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def createRepresentation(self, input: MString,
                        type: MString,
                        representation: MString,
                        undoRedo: MDagModifier,
                        ReturnStatus: MPxAssembly.MStatus): 
        '''
        createRepresentation(self, input: MString,
                        type: MString,
                        representation: MString,
                        undoRedo: MDagModifier,
                        ReturnStatus: MPxAssembly.MStatus) -> MString

        Synopsis
        -----
        Create a representation and add it to the list of
        representations. The input argument string is used as input data
        to the representation creation process. The semantics of this
        input are defined by the assembly derived class...The type of the
        representation is a property of the representation ..that
        expresses its commonality with other representations of this
        assembly type, ..for example a "Bounding Box" representation
        type. See the getRepType() method.If non-empty, the
        representation argument is used as a starting point for the
        representation name. This string value can be modified by the
        derived implementation to meet representation name uniqueness, or
        other constraints. If empty, the implementation is responsible
        for creating the representation name. The final representation
        name is returned by this method, after it has been added to the
        assembly.If non-null, the pointer to an MDagModifier object can
        be used to help implement undo / redo for createRepresentation():
        its redoIt() and undoIt() methods can be called in an MPxCommand.
        Note that MDagModifier can execute an arbitrary command through
        MDGModifier::commandToExecute().

        Returns: 
        ----- 
        Added representation name.

        Parameters:
        -----
        input: MString
        	[in] -> Input data for representation creation. 

        type: MString
        	[in] -> Type of representation to create. 

        representation: MString
        	[in] -> Representation name starting point. 

        undoRedo: MDagModifier
        	[in] -> Pointer to 

        ReturnStatus: MPxAssembly.MStatus
        	[out] -> Return status. 


        '''
        pass

    def activate(self, representation: MString): 
        '''
        activate(self, representation: MString) -> bool

        Synopsis
        -----
        Activate a representation in the list of representations. Derived
        implementations should inactivate the currently-active
        representation, if any, activate the newly-active representation,
        and return true for success. If the argument representation is
        not in the list of this node's representations, this method
        should return false. Passing in an empty string argument means
        inactivate the previously-active representation (if any),
        activate no representation, and return true.The default
        implementation does the following:  See performInactivate() and
        performActivate() documentation for more details.If you have
        opted into Maya's edit tracking system by overriding
        MPxAssembly::supportsEdits() to return true, you must call
        performActivate() and performInactivate() from within your
        implementation of activate() to get proper edit handling
        behaviour. This will ensure that edits are properly saved and
        restored when you switch representations.

        Returns: 
        ----- 
        Whether activation of the argument representation was successful
        or not.

        Parameters:
        -----
        representation: MString
        	[in] -> Representation to activate. 


        '''
        pass

    def getActive(self): 
        '''
        getActive(self) -> MString

        Synopsis
        -----
        Get the active representation in the list of representations.
        Derived implementations should return the active representation,
        if any, else an empty string. If the list of representations is
        empty, the return object should be an empty string.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def isActive(self, representation: MString): 
        '''
        isActive(self, representation: MString) -> bool

        Synopsis
        -----
        Determines whether the argument representation is the active
        representation. The default implementation compares the argument
        representation to the result of getActive().

        Returns: 
        ----- 
        true if the argument is active, false otherwise.

        Parameters:
        -----
        representation: MString
        	[in] -> Representation to query. 


        '''
        pass

    def getRepresentations(self, ReturnStatus: MPxAssembly.MStatus): 
        '''
        getRepresentations(self, ReturnStatus: MPxAssembly.MStatus) -> MStringArray

        Synopsis
        -----
        Returns an array of the representations managed by the node
        attached to this function set.

        Returns: 
        ----- 
        representations array.

        Parameters:
        -----
        ReturnStatus: MPxAssembly.MStatus
        	[out] -> Return status


        '''
        pass

    def getRepType(self, representation: MString): 
        '''
        getRepType(self, representation: MString) -> MString

        Synopsis
        -----
        Get the type of the argument representation. The type of a
        representation is a string that expresses its commonality with
        other representations of this assembly type. The type string does
        not have to be user-readable, and does not have to be localized;
        the type label should be used for UI purposes. If the argument
        representation is not found in this assembly, an empty string is
        returned.

        Returns: 
        ----- 
        Representation type.

        Parameters:
        -----
        representation: MString
        	[in] -> Representation whose type must be returned.


        '''
        pass

    def getRepLabel(self, representation: MString): 
        '''
        getRepLabel(self, representation: MString) -> MString

        Synopsis
        -----
        Get the label of the argument representation. The label of a
        representation is a string that is meant to be shown in the UI
        and identify the representation meaningfully to a user. The
        representation label should support localization requirements. If
        the argument representation is not found in this assembly, an
        empty string is returned.

        Returns: 
        ----- 
        Representation label.

        Parameters:
        -----
        representation: MString
        	[in] -> Representation whose label must be returned.


        '''
        pass

    def repTypes(self): 
        '''
        repTypes(self) -> MStringArray

        Synopsis
        -----
        Return the list of representation types that can be created for
        this assembly node. This can be a fixed list of representation
        types, or it can vary according to the state of the assembly
        node. For example, an assembly node might only want to allow one
        representation of a given type, so repTypes() could be used to
        enforce that constraint.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def deleteRepresentation(self, rep: MString): 
        '''
        deleteRepresentation(self, rep: MString)

        Synopsis
        -----
        Delete a representation managed by the node.

        Returns:
        -----
        None

        Parameters:
        -----
        rep: MString
        	[in] -> Representation to delete.


        '''
        pass

    def deleteAllRepresentations(self): 
        '''
        deleteAllRepresentations(self)

        Synopsis
        -----
        Delete all representations managed by this node.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getRepNamespace(self): 
        '''
        getRepNamespace(self) -> MString

        Synopsis
        -----
        Get the representations namespace of this assembly node. This is
        the namespace where nodes created by the activation of a
        representation will be added. This namespace is shared by all
        representations. The name can be updated by Maya if a name clash
        occurs when the namespace is added to its parent namespace (see
        MPxAssembly::updateRepNamespace() for details).The default
        implementation returns a namespace formatted as follows: assembly
        base name appended with the '_NS' prefix. The plugin could decide
        to not support namespaces by returning an empty string.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def updateRepNamespace(self, repNamespace: MString): 
        '''
        updateRepNamespace(self, repNamespace: MString)

        Synopsis
        -----
        This method is called by Maya to tell the assembly that the base
        representation namespace specified by getRepNamespace() has been
        changed.

        Returns:
        -----
        None

        Parameters:
        -----
        repNamespace: MString
        	[in] -> New namespace for representations. 


        '''
        pass

    def setRepName(self, representation: MString,
                        newName: MString,
                        ReturnStatus: MPxAssembly.MStatus): 
        '''
        setRepName(self, representation: MString,
                        newName: MString,
                        ReturnStatus: MPxAssembly.MStatus) -> MString

        Synopsis
        -----
        Rename a representation. The newName argument is used as a
        starting point for the new representation name. This string value
        can be modified by the derived implementation to meet
        representation name uniqueness, or other constraints. This method
        returns the final representation name.

        Returns: 
        ----- 
        New representation name.

        Parameters:
        -----
        representation: MString
        	[in] -> Current representation name. 

        newName: MString
        	[in] -> New representation name starting point. 

        ReturnStatus: MPxAssembly.MStatus
        	[out] -> Return status.


        '''
        pass

    def setRepLabel(self, representation: MString,
                        label: MString): 
        '''
        setRepLabel(self, representation: MString,
                        label: MString)

        Synopsis
        -----
        Change the representation label.

        Returns:
        -----
        None

        Parameters:
        -----
        representation: MString
        	[in] -> Representation name. 

        label: MString
        	[in] -> New representation label.


        '''
        pass

    def supportsEdits(self): 
        '''
        supportsEdits(self) -> bool

        Synopsis
        -----
        Opt in/out of Maya's edit tracking system. Override this method
        to return true if you want your assembly to support tracking of
        edits to its member nodes.The edits system is node-based and only
        representations that have Maya nodes can handle tracking. Only
        certain types of edits can be tracked (see MItEdits for more
        details).Use the MItEdits interface to manage/query edits
        generated by the edits system.The default implementation returns
        false, so edits are not tracked.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def supportsMemberChanges(self): 
        '''
        supportsMemberChanges(self) -> bool

        Synopsis
        -----
        Can members of the assembly be changed? If the assembly does not
        use Maya's edit tracking system (see supportsEdits()), does it
        support changes to its member nodes, outside of activation? If
        so, this means that any mutating operation on Maya nodes
        (parenting, connecting, disconnecting, renaming, deleting,
        setting attributes, adding attributes, removing attributes,
        locking) can be performed on member nodes of the assembly.This
        method is only used if supportsEdits() returns false. If
        supportsEdits() returns true, Maya will track edits to assembly
        members, and the return value of supportsMemberChanges() will
        have no meaning.The default implementation returns false, so that
        any mutating operation to member nodes of the assembly is
        prevented, and the assembly behaves as a read-only container of
        nodes. Override this method to return true if the assembly
        supports changes to its member nodes, e.g. if it implements its
        own edit tracking system without using Maya's.This predicate is
        only used outside of representation activation. During
        activation, all types of changes to the assembly's members are
        allowed, including of course deleting the previous
        representation's nodes, and creating nodes for the new
        representation.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def canRepApplyEdits(self, representation: MString): 
        '''
        canRepApplyEdits(self, representation: MString) -> bool

        Synopsis
        -----
        Determines whether the given representation can apply edits to
        its data. The default implementation returns false.

        Returns: 
        ----- 
        true if the representation can apply tracked edits, false
        otherwise.

        Parameters:
        -----
        representation: MString
        	[in] -> Representation to query. 


        '''
        pass

    def handlesAddEdits(self): 
        '''
        handlesAddEdits(self) -> bool

        Synopsis
        -----
        Determines whether the assembly is responsible for supplying
        edits to its data. If this method returns true, Maya will call
        MPxAssembly::addEdits(). These edits will later be applied,
        either by Maya, or by the assembly through
        MPxAssembly::applyEdits(), if MPxAssembly::handlesApplyEdits()
        returns true.Edits can be added for any node in the assembly's
        representations, which includes edits to any nested assembly of
        this assembly. In a scene with multiple levels of nested
        assemblies, if more than one nested assembly has edits to a given
        lower-level nested assembly, edits are applied by Maya starting
        at the most nested assembly level, moving up the chain of nesting
        assemblies. In this way, the most nested assembly's edit are
        overridden by less nested assembly edits, if they edit the same
        attribute or connection.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def addEdits(self): 
        '''
        addEdits(self)

        Synopsis
        -----
        Add edits so they can be applied by Maya when switching
        representations. This method is called by Maya to allow an
        assembly node to provide edits to be applied at each
        representation switch. These edits will later be applied, either
        by Maya, or by the assembly through MPxAssembly::applyEdits(), if
        MPxAssembly::handlesApplyEdits() returns true.Edits can be added
        for any node in the assembly's representations, which includes
        edits to any nested assembly of this assembly. In a scene with
        multiple levels of nested assemblies, if more than one nested
        assembly has edits to a given lower-level nested assembly, edits
        are applied by Maya starting at the most nested assembly level,
        moving up the chain of nesting assemblies. In this way, the most
        nested assembly's edit are overridden by less nested assembly
        edits, if they edit the same attribute or connection.In the event
        that edits have already been added to this assembly (e.g. from a
        Maya scene representation), the new edits will simply be added to
        the list.To add edits for a node, the plugin must call the
        methods addSetAttrEdit(), addConnectAttrEdit(),
        addDisconnectAttrEdit(), addDeleteAttrEdit(), and
        addAddAttrEdit(), as appropriate, for each edit to be added. An
        assembly should only add edits that it owns, and not those of
        nested assemblies: those will be queried by Maya separately. The
        assembly on which an edit is added is referred to as the edit
        owner.The methods for adding edits require a targetAssembly name
        to be specified. The targetAssembly name is the most enclosing
        assembly holding the edited node. The targetAssembly is always
        specified as a node name relative to the namespace of this parent
        assembly (i.e. the edit owner) on which the method is being
        called.To specify a relative node name that is in a namespace at
        or above the parent assembly namespace, a special syntax of "..:"
        is incorporated to indicate the parent namespace without
        explicitly naming it.Use of this convention is necessary when the
        targetAssembly is the same as the parent assembly. The
        targetAssembly name in this case would be the same as the parent
        assembly name and would be specified as "..:parentAssemblyName".A
        similar convention is used for specifying node names that reside
        in the parent assembly namespace, for example to specify the
        destination attribute for an edit, the format
        "..:parentAssemblyNamespace:nodeName.attr"The implementation in
        this class returns MS::kFailure.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def beforeSave(self): 
        '''
        beforeSave(self)

        Synopsis
        -----
        Method called by Maya to allow assemblies to do any required
        preparation before file save. It is called by Maya on top-level
        assemblies that are about to be saved, before the file I/O
        operation is actually performed.Note that if this assembly
        supports edit tracking, any changes made within beforeSave() will
        not be recorded as edits.Default implementation is to do nothing.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def postLoad(self): 
        '''
        postLoad(self)

        Synopsis
        -----
        Method called by Maya to initialize assemblies after their
        creation. It is called on top-level assemblies after file I/O has
        completed, and on nested assemblies after the representation that
        contains them has finished activating. Maya does not call the
        postLoad() method when creating a node directly through the
        assembly command; it will only do so in two cases, (1) after file
        I/O (top-level assemblies only), or (2) after activation (nested
        assemblies only).Note how this is later than
        MPxNode::postConstructor(), which is called immediately after the
        node has been created. For example, if the assembly is created
        through file I/O, the file I/O operation that created the node in
        the scene is not complete at the point of the postConstructor()
        call.In contrast, in our example, postLoad() is called after the
        file I/O operation (open, import) is done, so a postLoad()
        implementation can itself issue file I/O operations with the
        knowledge that previous I/O operations have completed.Note that
        if this assembly supports edit tracking, any changes made within
        postLoad() will be considered part of the setup process for the
        assembly and will not be recorded as
        edits.MPxAssembly::postLoad() should never be called directly.
        Always use MFnAssembly::postLoad(), to ensure that Maya's
        internal postLoad() initialization is invoked before
        MPxAssembly::postLoad() is called.An implementation of postLoad()
        should check MFnAssembly::canActivate() to determine whether it
        can activate a representation. See
        MFnAssembly::activateNonRecursive() for more details.Default
        implementation is to do nothing.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def memberAdded(self, member: MObject): 
        '''
        memberAdded(self, member: MObject)

        Synopsis
        -----
        Called immediately after the argument node has been added to this
        assembly. Default implementation does nothing.

        Returns:
        -----
        None

        Parameters:
        -----
        member: MObject
        	[in] -> Newly-added member node. 


        '''
        pass

    def memberRemoved(self, member: MObject): 
        '''
        memberRemoved(self, member: MObject)

        Synopsis
        -----
        Called immediately after the argument node has been removed from
        this assembly. Default implementation does nothing.

        Returns:
        -----
        None

        Parameters:
        -----
        member: MObject
        	[in] -> Newly-removed member node. 


        '''
        pass

    def performActivate(self, representation: MString): 
        '''
        performActivate(self, representation: MString) -> bool

        Synopsis
        -----
        Provide access to the Maya core representation activation
        functionality. This is useful to plugins overriding the default
        activate() method; see the activate() documentation for more
        details. A plugin implementing its own activate() method should
        call performActivate() when activating the newly-active
        representation to ensure it obtains the Maya services it
        needs.The core representation activation functionality will call
        activateRep(). It will then initialize any nested assembly
        created by the activation using postLoad(), and will finally
        apply edits to the activated representation. If the postLoad()
        implementation of the newly-created nested assemblies calls
        activate(), this will recurse into performActivate() for the
        nested assembly.Any changes made during performActivate() will
        not be tracked as edits, so that activating a representation will
        not generate spurious edits. Furthermore, performActivate() is
        not constrained to only those operations supported by edit
        tracking, so that node adds, deletes and renames are allowed, as
        expected.

        Returns: 
        ----- 
        true for success, false for failure.

        Parameters:
        -----
        representation: MString
        	[in] -> Representation to activate.


        '''
        pass

    def performInactivate(self): 
        '''
        performInactivate(self) -> bool

        Synopsis
        -----
        Provide access to the Maya core representation inactivation
        functionality. This is useful to plugins overriding the default
        activate() method; see the activate() documentation for more
        details. A plugin implementing its own activate() method should
        call performInactivate() when inactivating the currently-active
        representation to ensure it obtains the Maya services it
        needs.The core representation inactivation functionality performs
        the exact reverse of performActivate(). It first unapplies edits
        to the currently-active representation. It then loops over all
        nested assemblies (if any) and recursively calls
        performInactivate() on each. Finally, it calls
        inactivateRep().Any changes made during performInactivate() will
        not be tracked as edits, so that inactivating a representation
        will not generate spurious edits. Furthermore,
        performInactivate() is not constrained to only those operations
        supported by edit tracking, so that node adds, deletes and
        renames are allowed, as expected.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def activateRep(self, representation: MString): 
        '''
        activateRep(self, representation: MString)

        Synopsis
        -----
        Called during activation to activate the new active
        representation. See activate() documentation for more details.

        Returns:
        -----
        None

        Parameters:
        -----
        representation: MString
        	[in] -> Representation name.


        '''
        pass

    def inactivateRep(self): 
        '''
        inactivateRep(self) -> bool

        Synopsis
        -----
        Called during activation to inactivate the currently active
        representation. See activate() documentation for more details.The
        default implementation clears out all nodes in the assembly.
        Derived assembly node types that wish to change this behavior
        (e.g. hide nodes rather than removing them) should override this
        method.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def postActivateRep(self, representation: MString): 
        '''
        postActivateRep(self, representation: MString)

        Synopsis
        -----
        Called after activation of a representation including the load,
        activation and edits of any created sub-assemblies but prior to
        the application of edits.

        Returns:
        -----
        None

        Parameters:
        -----
        representation: MString
        	[in] -> Name of representation that was activated. 


        '''
        pass

    def preApplyEdits(self): 
        '''
        preApplyEdits(self)

        Synopsis
        -----
        Method called by performActivate() just before edits are applied.
        This method is called by performActivate() after the new
        representation has been activated with activateRep(), after any
        newly-created nested assemblies have been initialized with
        postLoad(), but just before edits are applied to this assembly
        (and any nested assemblies).A use of this method might be to
        manage the assembly's list of edits before they are applied,
        perhaps adding edits.This is called regardless of whether the
        representation supports edits or not.The default implementation
        does nothing.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def preUnapplyEdits(self): 
        '''
        preUnapplyEdits(self)

        Synopsis
        -----
        Method called by performInactivate() just before edits are
        unapplied. This method is called by performInactivate() before
        unapplying edits, before any nested assemblies are inactivated,
        and before the current representation is inactivated with
        inactivateRep(). Therefore, when this call is made, no change has
        been made to the currently-active representation.A use of this
        method might be to manage the assembly's list of edits before
        they are unapplied, perhaps removing edits. Any removed edit will
        be unapplied first, which can be done safely because the current
        representation has not been inactivated yet.This is called
        regardless of whether the representation supports edits or
        not.The default implementation does nothing.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def postApplyEdits(self): 
        '''
        postApplyEdits(self)

        Synopsis
        -----
        Method called by performActivate() just after edits are applied.
        This method is called by performActivate() after edits are
        applied to this assembly (and all nested assemblies).A use of
        this method might be to perform additional work after edit
        application.This is called regardless of whether the
        representation supports edits or not.The default implementation
        does nothing.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def postUnapplyEdits(self): 
        '''
        postUnapplyEdits(self)

        Synopsis
        -----
        Method called by performInactivate() just after edits are
        unapplied. This method is called by performInactivate() after
        unapplying edits, before any nested assemblies are inactivated,
        and before the current representation is inactivated with
        inactivateRep().A use of this method might be to perform
        additional work after edit unapplication.This is called
        regardless of whether the representation supports edits or
        not.The default implementation does nothing.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getInitialRep(self, assembly: MObject,
                        hasInitialRep: bool,
                        ReturnStatus: MPxAssembly.MStatus): 
        '''
        getInitialRep(self, assembly: MObject,
                        hasInitialRep: bool,
                        ReturnStatus: MPxAssembly.MStatus) -> MString

        Synopsis
        -----
        Get the initial representation to use when the specified assembly
        is first loaded. This method can be customized by the assembly
        implementation to determine which representation should be
        activated when an assembly is first initialized. The
        hasInitialRep return argument must be set to false if no initial
        representation has been determined. Returning an empty string
        with hasInitialRep true means the initial active representation
        for the assembly should be no representation.This method should
        not be called directly - individual assemblies should always call
        MFnAssembly::getInitialRep(). When an assembly requests its
        initial representation, Maya will internally locate the
        associated top level assembly node and invoke this method on it
        to return the actual representation to use.This base class
        defines no implementation, sets the hasInitialRep return argument
        to false, and returns an empty string. Derived implementations
        can override this method to customize this behaviour. Maya
        ensures that this method will only be called on top level
        assemblies.

        Returns: 
        ----- 
        The initial representation to use, if any, else an empty string.

        Parameters:
        -----
        assembly: MObject
        	[in] -> The assembly for which the initial representation is being requested 

        hasInitialRep: bool
        	[out] -> Return whether or not we have an initial representation 

        ReturnStatus: MPxAssembly.MStatus
        	[out] -> Return status


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

    def activating(self): 
        '''
        activating(self) -> bool

        Synopsis
        -----
        Return true when this assembly is activating a representation,
        within a call to activate() or activateNonRecursive(). Reset to
        false just before initializing nested assemblies (through
        postLoad()) and applying edits. This can be used to implement
        activation-specific behavior for the assembly.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def typeId(self): 
        '''
        typeId(self) -> MTypeId

        Synopsis
        -----
        Returns the TYPEID of this node. The TYPEID is a four byte
        identifier that uniquely identifies this type of node to the
        binary file format.It is not necessary to override this
        method.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def typeName(self): 
        '''
        typeName(self) -> MString

        Synopsis
        -----
        Returns the type name of this node. The type name identifies the
        node type to the ASCII file format. It may also be used with the
        MEL command "createNode" to create a new node of this type.It is
        not necessary to override this method.Reimplemented from MPxNode.

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
        Returns the name of this particular instance of this class. Each
        object in the dependency graph has a name. This name will be used
        by the UI and by MEL.It is not necessary to override this
        method.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def thisMObject(self): 
        '''
        thisMObject(self) -> MObject

        Synopsis
        -----
        Returns the MObject associated with this user defined node. This
        makes it possible to use MFnDependencyNode or to construct plugs
        to this node's attributes.It is not necessary to override this
        method.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setExistWithoutInConnections(self, flag: bool): 
        '''
        setExistWithoutInConnections(self, flag: bool)

        Synopsis
        -----
        This method specifies whether or not the node can exist without
        input connections. If a node connected to this node is deleted
        resulting in no more input connections and if this flag is false,
        then this node will be deleted.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
        flag: bool
        	[in] -> true if this node can exist without input connections, false otherwise


        '''
        pass

    def existWithoutInConnections(self, ReturnStatus: MPxAssembly.MStatus): 
        '''
        existWithoutInConnections(self, ReturnStatus: MPxAssembly.MStatus) -> bool

        Synopsis
        -----
        Determines whether or not this node can exist without input
        connections. If a node connected to this node is deleted
        resulting in no more input connections and if this flag is false,
        then this node will be deleted.Reimplemented from MPxNode.

        Returns: 
        ----- 
        true is this node can exist without input connections, false
        otherwise

        Parameters:
        -----
        ReturnStatus: MPxAssembly.MStatus
        	[out] -> Status code.


        '''
        pass

    def setExistWithoutOutConnections(self, flag: bool): 
        '''
        setExistWithoutOutConnections(self, flag: bool)

        Synopsis
        -----
        This method specifies whether or not the node can exist without
        output connections. If a node connected to this node is deleted
        resulting in no more output connections and if this flag is
        false, then this node will be deleted.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
        flag: bool
        	[in] -> true if this node can exist without output connections, false otherwise


        '''
        pass

    def existWithoutOutConnections(self, ReturnStatus: MPxAssembly.MStatus): 
        '''
        existWithoutOutConnections(self, ReturnStatus: MPxAssembly.MStatus) -> bool

        Synopsis
        -----
        Determines whether or not this node can exist without output
        connections. If a node connected to this node is deleted
        resulting in no more output connections and if this flag is
        false, then this node will be deleted.Reimplemented from MPxNode.

        Returns: 
        ----- 
        true is this node can exist without output connections, false
        otherwise

        Parameters:
        -----
        ReturnStatus: MPxAssembly.MStatus
        	[out] -> Status code.


        '''
        pass

    def addSetAttrEdit(self, targetAssembly: MString,
                        plugName: MString,
                        parameters: MString,
                        editData: MPxEditData): 
        '''
        addSetAttrEdit(self, targetAssembly: MString,
                        plugName: MString,
                        parameters: MString,
                        editData: MPxEditData)

        Synopsis
        -----
        Add a set attribute edit to be applied by Maya when switching
        representations. This method is intended to be called by the
        plugin's addEdits() method, to add a set attribute edit. The set
        attribute edit is implemented with the setAttr command, so the
        full generality of setAttr command options is possible.The
        targetAssembly name is specified relative to this assembly. Refer
        to the addEdits() method documentation for more information about
        specifying the targetAssembly for edits.The plugName is in
        "nodeName.attr" format, and is specified relative to this
        assembly. Refer to the addEdits() method documentation for more
        information about specifying relative node names for edits.The
        editData is an optional user data element that can be associated
        with this edit. The object must be dynamically allocated.
        Ownership of the editData will be assumed by Maya and subsequent
        management of the data object, including its eventual deletion
        will be handled along with the edit it is associated with. For
        this reason, an editData object should only be associated with a
        single edit, the same object should not be shared or associated
        with other edits. If multiple edits have editData of the same
        value, each edit must have its own unique copy.

        Returns:
        -----
        None

        Parameters:
        -----
        targetAssembly: MString
        	[in] -> The most enclosing assembly holding the edited node. 

        plugName: MString
        	[in] -> The name of the node and attr, in "nodeName.attr" syntax. 

        parameters: MString
        	[in] -> Parameters to be added to the setAttr command, in MEL syntax. 

        editData: MPxEditData
        	[in] -> Optional user-defined data to be associated with the edit


        '''
        pass

    def addConnectAttrEdit(self, targetAssembly: MString,
                        srcPlugName: MString,
                        dstPlugName: MString,
                        editData: MPxEditData): 
        '''
        addConnectAttrEdit(self, targetAssembly: MString,
                        srcPlugName: MString,
                        dstPlugName: MString,
                        editData: MPxEditData)

        Synopsis
        -----
        Add a connect attribute edit to be applied by Maya when switching
        representations. This method is intended to be called by the
        plugin's addEdits() method, to add a connect attribute edit.The
        targetAssembly name is specified relative to this assembly. Refer
        to the addEdits() method documentation for more information about
        specifying the targetAssembly for edits.The srcPlugName and
        dstPlugName are in "nodeName.attr" format, and are specified
        relative to this assembly. Refer to the addEdits() method
        documentation for more information about specifying relative node
        names for edits.Note that the targetAssembly for connections is
        determined by the destination plug of the connection.The editData
        is an optional user data element that can be associated with this
        edit. The object must be dynamically allocated. Ownership of the
        editData will be assumed by Maya and subsequent management of the
        data object, including its eventual deletion will be handled
        along with the edit it is associated with. For this reason, an
        editData object should only be associated with a single edit, the
        same object should not be shared or associated with other edits.
        If multiple edits have editData of the same value, each edit must
        have its own unique copy.

        Returns:
        -----
        None

        Parameters:
        -----
        targetAssembly: MString
        	[in] -> The most enclosing assembly holding the destination plug node. 

        srcPlugName: MString
        	[in] -> The name of the node and attribute that are the source of the connection, in "nodeName.attr" syntax. 

        dstPlugName: MString
        	[in] -> The name of the node and attribute that are the destination of the connection, in "nodeName.attr" syntax. 

        editData: MPxEditData
        	[in] -> Optional user-defined data to be associated with the edit 


        '''
        pass

    def addDisconnectAttrEdit(self, targetAssembly: MString,
                        srcPlugName: MString,
                        dstPlugName: MString,
                        editData: MPxEditData): 
        '''
        addDisconnectAttrEdit(self, targetAssembly: MString,
                        srcPlugName: MString,
                        dstPlugName: MString,
                        editData: MPxEditData)

        Synopsis
        -----
        Add a disconnect attribute edit to be applied by Maya when
        switching representations. This method is intended to be called
        by the plugin's addEdits() method, to add a disconnect attribute
        edit.The targetAssembly name is specified relative to this
        assembly. Refer to the addEdits() method documentation for more
        information about specifying the targetAssembly for edits.The
        srcPlugName and dstPlugName are in "nodeName.attr" format, and
        are specified relative to this assembly. Refer to the addEdits()
        method documentation for more information about specifying
        relative node names for edits.Note that the targetAssembly for
        disconnections is determined by the destination plug of the
        connection.The editData is an optional user data element that can
        be associated with this edit. The object must be dynamically
        allocated. Ownership of the editData will be assumed by Maya and
        subsequent management of the data object, including its eventual
        deletion will be handled along with the edit it is associated
        with. For this reason, an editData object should only be
        associated with a single edit, the same object should not be
        shared or associated with other edits. If multiple edits have
        editData of the same value, each edit must have its own unique
        copy.Note: it is recommended that a disconnectAttrEdit be
        followed by a setAttrEdit on the destination plug to ensure it is
        set to a predictable value after disconnection.

        Returns:
        -----
        None

        Parameters:
        -----
        targetAssembly: MString
        	[in] -> The most enclosing assembly holding the destination plug node. 

        srcPlugName: MString
        	[in] -> The name of the node and attribute that are the source of the connection, in "nodeName.attr" syntax. 

        dstPlugName: MString
        	[in] -> The name of the node and attribute that are the destination of the connection, in "nodeName.attr" syntax. 

        editData: MPxEditData
        	[in] -> Optional user-defined data to be associated with the edit 


        '''
        pass

    def addDeleteAttrEdit(self, targetAssembly: MString,
                        nodeName: MString,
                        attributeName: MString,
                        editData: MPxEditData): 
        '''
        addDeleteAttrEdit(self, targetAssembly: MString,
                        nodeName: MString,
                        attributeName: MString,
                        editData: MPxEditData)

        Synopsis
        -----
        Add a delete attribute edit to be applied by Maya when switching
        representations. This method is intended to be called by the
        plugin's addEdits() method, to insert an edit that will remove a
        dynamic attribute from a node.The targetAssembly name and
        nodeName are specified relative to this assembly. Refer to the
        addEdits() method documentation for more information about
        specifying the targetAssembly and relative node names for
        edits.The editData is an optional user data element that can be
        associated with this edit. The object must be dynamically
        allocated. Ownership of the editData will be assumed by Maya and
        subsequent management of the data object, including its eventual
        deletion will be handled along with the edit it is associated
        with. For this reason, an editData object should only be
        associated with a single edit, the same object should not be
        shared or associated with other edits. If multiple edits have
        editData of the same value, each edit must have its own unique
        copy.

        Returns:
        -----
        None

        Parameters:
        -----
        targetAssembly: MString
        	[in] -> The most enclosing assembly holding the affected node. 

        nodeName: MString
        	[in] -> The name of the node that the attribute will be removed from. 

        attributeName: MString
        	[in] -> The long name or short name of the attribute to be removed. 

        editData: MPxEditData
        	[in] -> Optional user-defined data to be associated with the edit 


        '''
        pass

    def addAddAttrEdit(self, targetAssembly: MString,
                        nodeName: MString,
                        longAttributeName: MString,
                        shortAttributeName: MString,
                        parameters: MString,
                        editData: MPxEditData): 
        '''
        addAddAttrEdit(self, targetAssembly: MString,
                        nodeName: MString,
                        longAttributeName: MString,
                        shortAttributeName: MString,
                        parameters: MString,
                        editData: MPxEditData)

        Synopsis
        -----
        Add an add attribute edit to be applied by Maya when switching
        representations. This method is intended to be called by the
        plugin's addEdits() method, to insert an edit that will add a
        dynamic attribute to a node.The targetAssembly name and nodeName
        are specified relative to this assembly. Refer to the addEdits()
        method documentation for more information about specifying the
        targetAssembly and relative node names for edits.The parameters
        value is used to specify additional arguments to the addAttr
        command, such as the attribute type or data type information.
        Refer to the addAttr command for additional information.The
        editData is an optional user data element that can be associated
        with this edit. The object must be dynamically allocated.
        Ownership of the editData will be assumed by Maya and subsequent
        management of the data object, including its eventual deletion
        will be handled along with the edit it is associated with. For
        this reason, an editData object should only be associated with a
        single edit, the same object should not be shared or associated
        with other edits. If multiple edits have editData of the same
        value, each edit must have its own unique copy.Note: it is
        recommended that an addAttrEdit be followed by a setAttrEdit on
        the new attribute to ensure it is initialized to a predictable
        and valid value.

        Returns:
        -----
        None

        Parameters:
        -----
        targetAssembly: MString
        	[in] -> The most enclosing assembly holding the affected node. 

        nodeName: MString
        	[in] -> The name of the node that the attribute will be added to. 

        longAttributeName: MString
        	[in] -> The long name of the attribute to be added. 

        shortAttributeName: MString
        	[in] -> The short name of the attribute to be added. 

        parameters: MString
        	[in] -> Parameters to be added to the addAttr command, in MEL syntax. 

        editData: MPxEditData
        	[in] -> Optional user-defined data to be associated with the edit 


        '''
        pass

    def addParentEdit(self, targetAssembly: MString,
                        childNodeName: MString,
                        parentNodeName: MString,
                        parameters: MString,
                        editData: MPxEditData): 
        '''
        addParentEdit(self, targetAssembly: MString,
                        childNodeName: MString,
                        parentNodeName: MString,
                        parameters: MString,
                        editData: MPxEditData)

        Synopsis
        -----
        Add a parent edit to be applied by Maya when switching
        representations. This method is intended to be called by the
        plugin's addEdits() method, to insert an edit that will create a
        parenting relationship between two nodes.The targetAssembly name,
        parentNodeName and childNodeName are specified relative to this
        assembly. Refer to the addEdits() method documentation for more
        information about specifying the targetAssembly and relative node
        names for edits.The parameters value is used to specify
        additional arguments to the parent command such as relative or
        shape. Refer to the parent command for additional
        information.Parent edits are only allowed between main-scene
        nodes and nodes in an assembly. The targetAssembly for parenting
        is determined depending on which of the nodes (parent or child)
        is inside an assembly. There are two kinds of parent edits,
        parent-in and parent-out:The editData is an optional user data
        element that can be associated with this edit. The object must be
        dynamically allocated. Ownership of the editData will be assumed
        by Maya and subsequent management of the data object, including
        its eventual deletion will be handled along with the edit it is
        associated with. For this reason, an editData object should only
        be associated with a single edit, the same object should not be
        shared or associated with other edits. If multiple edits have
        editData of the same value, each edit must have its own unique
        copy.

        Returns:
        -----
        None

        Parameters:
        -----
        targetAssembly: MString
        	[in] -> The most enclosing assembly holding the affected node. 

        childNodeName: MString
        	[in] -> The name of the child node being parented 

        parentNodeName: MString
        	[in] -> The name of the parent node 

        parameters: MString
        	[in] -> Parameters to be added to the parent command, in MEL syntax. 

        editData: MPxEditData
        	[in] -> Optional user-defined data to be associated with the edit 


        '''
        pass

    def forceCache(self): 
        '''
        forceCache(self) -> MDataBlock

        Synopsis
        -----
        USE _forceCache() IN SCRIPT. Get the datablock for this node at
        the current evaluation context.If there is no datablock then one
        will be created.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setDoNotWrite(self, flag: bool): 
        '''
        setDoNotWrite(self, flag: bool)

        Synopsis
        -----
        USE _setDoNotWrite() IN SCRIPT. Use this method to mark the "do
        not write" state of this proxy node.If set, this node will not be
        saved when the Maya model is written out.NOTES: 1. Plug-in
        "requires" information will be written out with the model when
        saved. But a subsequent reload and resave of the file will cause
        these to go away. 2. If this node is a DAG and has a parent or
        children, the "do not write" flag of the parent or children will
        not be set. It is the developers responsibility to ensure that
        the resulting scene file is capable of being read in without
        errors due to unwritten nodes.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
        flag: bool
        	[in] -> True if the user node should not be saved. 


        '''
        pass

    def doNotWrite(self, ReturnStatus: MPxAssembly.MStatus): 
        '''
        doNotWrite(self, ReturnStatus: MPxAssembly.MStatus) -> bool

        Synopsis
        -----
        USE _doNotWrite() IN SCRIPT. Use this method to query the "do not
        write" state of this proxy node.True is returned if this node
        will not be saved when the Maya model is written
        out.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
        ReturnStatus: MPxAssembly.MStatus
        	[out] -> 


        '''
        pass

class MPxAttributePatternFactory:
    '''Base class for user-defined attribute pattern factories.
MPxAttributePatternFactory is the parent class of all user defined attribute pattern
factories.
This class can be used to implement new kinds of attribute
pattern factories within Maya that behave in a similar manner to
the attribute pattern factories included in Maya.
'''
    def __init__(self):
        pass


    def createPatternsFromString(self, patternString: MString,
                        createdPatterns: MAttributePatternArray): 
        '''
        createPatternsFromString(self, patternString: MString,
                        createdPatterns: MAttributePatternArray)

        Synopsis
        -----
        Call this to define a new attribute pattern using the pattern
        factory format definition passed in through the string parameter.
        No default implementation is available.

        Returns:
        -----
        None

        Parameters:
        -----
        patternString: MString
        	[in] -> The pattern definition 

        createdPatterns: MAttributePatternArray
        	[out] -> List of attribute patterns created from the string


        '''
        pass

    def createPatternsFromFile(self, patternPath: MString,
                        createdPatterns: MAttributePatternArray): 
        '''
        createPatternsFromFile(self, patternPath: MString,
                        createdPatterns: MAttributePatternArray)

        Synopsis
        -----
        Call this to define a new attribute pattern using the pattern
        factory format definition passed in through the contents of the
        file in the parameter. No default implementation is available.

        Returns:
        -----
        None

        Parameters:
        -----
        patternPath: MString
        	[in] -> The file name to be expanded 

        createdPatterns: MAttributePatternArray
        	[out] -> List of attribute patterns created from the file


        '''
        pass

    def name(self): 
        '''
        name(self) -> MString

        Synopsis
        -----
        Return the name of the pattern factory. It's merely an
        identification for the commands operating on pattern factories
        and has no significance beyond that.

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

class MPxBakeEngine:
    '''Baking functionality.
The
MPxBakeEngine class is a way for users to override the viewport representation
of shaders. Users can provide their own baking engine to bake
advanced shading properties into a texture. This texture is used
by the viewport to represent the shading properties.
'''
    def __init__(self):
        pass


    def setNeedTransparency(self, t: bool): 
        '''
        setNeedTransparency(self, t: bool)

        Synopsis
        -----
        Set whether the bake engine needs to produce an image with
        transparency.

        Returns:
        -----
        None

        Parameters:
        -----
        t: bool
        	[in] -> whether transparency is needed 


        '''
        pass

    def getUVRange(self, minUV: MFloatArray,
                        maxUV: MFloatArray): 
        '''
        getUVRange(self, minUV: MFloatArray,
                        maxUV: MFloatArray)

        Synopsis
        -----
        Tells Maya the UV range the baked texture should cover.

        Returns:
        -----
        None

        Parameters:
        -----
        minUV: MFloatArray
        	[out] -> the minimum UV value 

        maxUV: MFloatArray
        	[out] -> the maximum UV value 


        '''
        pass

    def bake(self, objectPath: MDagPath,
                        cameraPath: MDagPath,
                        samplePlug: MPlug,
                        result: MImage): 
        '''
        bake(self, objectPath: MDagPath,
                        cameraPath: MDagPath,
                        samplePlug: MPlug,
                        result: MImage)

        Synopsis
        -----
        Bake the texture Maya will use to approximate shading properties.

        Returns:
        -----
        None

        Parameters:
        -----
        objectPath: MDagPath
        	[in] -> the object the texture will be applied to 

        cameraPath: MDagPath
        	[in] -> the camera that should be used for baking 

        samplePlug: MPlug
        	[in] -> the plug being sampled, ie baked 

        result: MImage
        	[out] -> the texture


        '''
        pass

class MPxBlendShape:
    '''Base class for user-defined blendshape deformers.
MPxBlendShape allows the creation of user-defined blendshape deformers. It
derives from
MPxGeometryFilter and so offers all the functionality of that class. Additionally,
it has the input target and all other attributes of the Maya
built-in blendShape node.
Custom nodes derived from
MPxBlendShape are treated by Maya just like the built-in blendShape, so all
the weight painting/editing etc. tools that artists are used to
also work on the custom nodes.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MPxNode.MPxNode

        Synopsis
        -----
        This method returns the type of the node. This method should not
        be overridden by the user. It will return
        MPxNode::kBlendShape.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def deformData(self, block: MDataBlock,
                        geomData: MDataHandle,
                        groupId: int,
                        matrix: MMatrix,
                        multiIndex: int): 
        '''
        deformData(self, block: MDataBlock,
                        geomData: MDataHandle,
                        groupId: int,
                        matrix: MMatrix,
                        multiIndex: int)

        Synopsis
        -----
        This method performs the deformation algorithm. A status code of
        MS::kSuccess should be returned unless there was a problem during
        the deformation, such as insufficient memory or required input
        data is missing or invalid.NOTE: the geometry passed to this
        method is in local space and not world space. To convert points
        to world space use the matrix that is suppied.If this method is
        overriden (and returns success or failure), then deform()
        (virtual in MPxGeometryFilter()) is NOT called. If the derived
        node prefers to use deform(), then do not override this method.

        Returns:
        -----
        None

        Parameters:
        -----
        block: MDataBlock
        	[in] -> the node's datablock. 

        geomData: MDataHandle
        	[in] -> a handle to the current geometry being deformed. 

        groupId: int
        	[in] -> the group ID within the geometry to deform 

        matrix: MMatrix
        	[in] -> the geometry's world space transformation matrix. 

        multiIndex: int
        	[in] -> the index corresponding to the requested output geometry.


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

class MPxCacheConfigRuleFilter:
    '''Proxy class for defining a new caching rule filter
Caching rules are defined through the cacheEvaluator command.
They can be built using filter/action pairs. This class allows
defining a custom caching rule filter.
See also:
MCacheConfigRuleRegistry'''
    def __init__(self):
        pass


    def preRulesExecution(self): 
        '''
        preRulesExecution(self) -> MPxCacheConfigRuleFilter.OPENMAYA_MAJOR_NAMESPACE_OPENvoid

        Synopsis
        -----
        Called when cache configuration rule application starts. Note:
        this default implementation does nothing, so it is not necessary
        to call it from derived classes.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def postRulesExecution(self): 
        '''
        postRulesExecution(self)

        Synopsis
        -----
        Called when cache configuration rule application stops. Note:
        this default implementation does nothing, so it is not necessary
        to call it from derived classes.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def isMatch(self, evalNode: MEvaluationNode): 
        '''
        isMatch(self, evalNode: MEvaluationNode) -> bool

        Synopsis
        -----
        Will be called for each evaluation node when filter/action rules
        are applied for the cache configuration. If the filter matches
        (returns true), then the associated action will be called.Note:
        This default implementation returns false for all nodes and does
        not need to be called by derived classes.

        Returns: 
        ----- 
        true the evaluation node matches the filter  false the evaluation
        node does not match the filter

        Parameters:
        -----
        evalNode: MEvaluationNode
        	[in] -> the evaluation node to match


        '''
        pass

class MPxCacheFormat:
    '''CacheFormat definition.
The
MPxCacheFormat class can be used to implement support for new cache file
formats in Maya.
'''
    def __init__(self):
        pass


    def open(self, fileName: MString,
                        mode: MPxCacheFormat.FileAccessMode): 
        '''
        open(self, fileName: MString,
                        mode: MPxCacheFormat.FileAccessMode)

        Synopsis
        -----
        Attempt to open the specified cache format. It is important that
        this function only return success if the cache file is definitely
        supported by this implementation.

        Returns:
        -----
        None

        Parameters:
        -----
        fileName: MString
        	[in] -> Name of the cache file to open 

        mode: MPxCacheFormat.FileAccessMode
        	[in] -> Access mode for the cache file


        '''
        pass

    def isValid(self): 
        '''
        isValid(self)

        Synopsis
        -----
        Confirm whether the current cache file is valid.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def rewind(self): 
        '''
        rewind(self)

        Synopsis
        -----
        Rewind the current cache pointer to the start of the cache.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def extension(self): 
        '''
        extension(self) -> MString

        Synopsis
        -----
        Returns the extension used by this format. This is not the same
        as the format's key, which is used by the plugin to identify
        itself.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def readHeader(self): 
        '''
        readHeader(self)

        Synopsis
        -----
        Read the header from the current cache file, and store any data
        that may be required.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def writeHeader(self, version: MString,
                        startTime: MTime,
                        endTime: MTime): 
        '''
        writeHeader(self, version: MString,
                        startTime: MTime,
                        endTime: MTime)

        Synopsis
        -----
        Write the header for the current cache.

        Returns:
        -----
        None

        Parameters:
        -----
        version: MString
        	[in] -> Maya supplied cache version 

        startTime: MTime
        	[in] -> startTime for this cache, in ticks. There are 6000 ticks per second 

        endTime: MTime
        	[in] -> endTime for this cache, in ticks. There are 6000 ticks per second


        '''
        pass

    def beginWriteChunk(self): 
        '''
        beginWriteChunk(self)

        Synopsis
        -----
        Perform any actions required prior to writing a chunk's
        information. A chunk contains the cache information for a
        specific time, and may contain multiple channels.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def beginReadChunk(self): 
        '''
        beginReadChunk(self)

        Synopsis
        -----
        Start the read process for this chunk. Anything written by
        beginWriteChunk() should be read and validated by this method.A
        chunk contains the cache information for a specific time, and may
        contain multiple channels.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def endReadChunk(self): 
        '''
        endReadChunk(self)

        Synopsis
        -----
        End the read process for this chunk. Anything written by the
        endWriteChunk should be read and validated by this method.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def writeTime(self, time: MTime): 
        '''
        writeTime(self, time: MTime)

        Synopsis
        -----
        Write the current time to the cache.

        Returns:
        -----
        None

        Parameters:
        -----
        time: MTime
        	[in] -> Time to write.


        '''
        pass

    def readTime(self, time: MTime): 
        '''
        readTime(self, time: MTime)

        Synopsis
        -----
        Read the current time from the cache.

        Returns:
        -----
        None

        Parameters:
        -----
        time: MTime
        	[out] -> Current time from the cache.


        '''
        pass

    def findTime(self, time: MTime,
                        foundTime: MTime): 
        '''
        findTime(self, time: MTime,
                        foundTime: MTime)

        Synopsis
        -----
        Find a specific time in the cache.

        Returns:
        -----
        None

        Parameters:
        -----
        time: MTime
        	[in] -> Time to look for. 

        foundTime: MTime
        	[out] -> Nearest time found.


        '''
        pass

    def readNextTime(self, foundTime: MTime): 
        '''
        readNextTime(self, foundTime: MTime)

        Synopsis
        -----
        Read the next time from the cache.

        Returns:
        -----
        None

        Parameters:
        -----
        foundTime: MTime
        	[out] -> the time found


        '''
        pass

    def readArraySize(self): 
        '''
        readArraySize(self)

        Synopsis
        -----
        Read the size of an array in the cache.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def writeDoubleArray(self, array: MDoubleArray): 
        '''
        writeDoubleArray(self, array: MDoubleArray)

        Synopsis
        -----
        Write an array of doubles to the cache.

        Returns:
        -----
        None

        Parameters:
        -----
        array: MDoubleArray
        	[in] -> Array of values to be written.


        '''
        pass

    def writeFloatArray(self, array: MFloatArray): 
        '''
        writeFloatArray(self, array: MFloatArray)

        Synopsis
        -----
        Write a array of floats to the cache.

        Returns:
        -----
        None

        Parameters:
        -----
        array: MFloatArray
        	[in] -> Array of values to be written.


        '''
        pass

    def writeIntArray(self, array: MIntArray): 
        '''
        writeIntArray(self, array: MIntArray)

        Synopsis
        -----
        Write a array of int to the cache.

        Returns:
        -----
        None

        Parameters:
        -----
        array: MIntArray
        	[in] -> Array of values to be written.


        '''
        pass

    def writeDoubleVectorArray(self, array: MVectorArray): 
        '''
        writeDoubleVectorArray(self, array: MVectorArray)

        Synopsis
        -----
        Write an array of double-precision vectors to the cache.

        Returns:
        -----
        None

        Parameters:
        -----
        array: MVectorArray
        	[in] -> Array of values to be written.


        '''
        pass

    def writeFloatVectorArray(self, array: MFloatVectorArray): 
        '''
        writeFloatVectorArray(self, array: MFloatVectorArray)

        Synopsis
        -----
        Write an array of single-precision vectors to the cache.

        Returns:
        -----
        None

        Parameters:
        -----
        array: MFloatVectorArray
        	[in] -> Array of values to be written.


        '''
        pass

    def writeInt32(self, value: int): 
        '''
        writeInt32(self, value: int)

        Synopsis
        -----
        Write an integer to the cache.

        Returns:
        -----
        None

        Parameters:
        -----
        value: int
        	[in] -> the value to be written


        '''
        pass

    def readDoubleArray(self, array: MDoubleArray,
                        size: unsigned): 
        '''
        readDoubleArray(self, array: MDoubleArray,
                        size: unsigned)

        Synopsis
        -----
        Read an array of doubles from the cache.

        Returns:
        -----
        None

        Parameters:
        -----
        array: MDoubleArray
        	[out] -> Array of values read. 

        size: unsigned
        	[in] -> Number of elements expected.


        '''
        pass

    def readFloatArray(self, array: MFloatArray,
                        size: unsigned): 
        '''
        readFloatArray(self, array: MFloatArray,
                        size: unsigned)

        Synopsis
        -----
        Read an array of floats from the cache.

        Returns:
        -----
        None

        Parameters:
        -----
        array: MFloatArray
        	[out] -> Array of values read. 

        size: unsigned
        	[in] -> Number of elements expected.


        '''
        pass

    def readIntArray(self, array: MIntArray,
                        size: unsigned): 
        '''
        readIntArray(self, array: MIntArray,
                        size: unsigned)

        Synopsis
        -----
        Read an array of ints from the cache.

        Returns:
        -----
        None

        Parameters:
        -----
        array: MIntArray
        	[out] -> Array of values read. 

        size: unsigned
        	[in] -> Number of elements expected.


        '''
        pass

    def readDoubleVectorArray(self, array: MVectorArray,
                        arraySize: unsigned): 
        '''
        readDoubleVectorArray(self, array: MVectorArray,
                        arraySize: unsigned)

        Synopsis
        -----
        Read an array of double-precision vectors from the cache.

        Returns:
        -----
        None

        Parameters:
        -----
        array: MVectorArray
        	[out] -> Array of values read. 

        arraySize: unsigned
        	[in] -> Number of elements expected.


        '''
        pass

    def readFloatVectorArray(self, array: MFloatVectorArray,
                        size: unsigned): 
        '''
        readFloatVectorArray(self, array: MFloatVectorArray,
                        size: unsigned)

        Synopsis
        -----
        Read an array of single-precision vectors from the cache.

        Returns:
        -----
        None

        Parameters:
        -----
        array: MFloatVectorArray
        	[out] -> Array of values read. 

        size: unsigned
        	[in] -> Number of elements expected.


        '''
        pass

    def readInt32(self): 
        '''
        readInt32(self) -> int

        Synopsis
        -----
        Read an integer from the cache.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def writeChannelName(self, name: MString): 
        '''
        writeChannelName(self, name: MString)

        Synopsis
        -----
        Write a channel to the cache.

        Returns:
        -----
        None

        Parameters:
        -----
        name: MString
        	[in] -> the channel to be written


        '''
        pass

    def findChannelName(self, name: MString): 
        '''
        findChannelName(self, name: MString)

        Synopsis
        -----
        Seek to a specific channel in the cache.

        Returns:
        -----
        None

        Parameters:
        -----
        name: MString
        	[in] -> the channel to seek


        '''
        pass

    def readChannelName(self, name: MString): 
        '''
        readChannelName(self, name: MString)

        Synopsis
        -----
        Find the next channel name.

        Returns:
        -----
        None

        Parameters:
        -----
        name: MString
        	[in] -> the name that is found


        '''
        pass

    def handlesDescription(self): 
        '''
        handlesDescription(self) -> bool

        Synopsis
        -----
        Report whether this format handles the format description itself
        (usually provided by the default xml description file). If the
        format handles the description itself, it must provide
        implementations of readDescription() and writeDescription().

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def readDescription(self, description: MCacheFormatDescription,
                        descriptionFileLocation: MString,
                        baseFileName: MString): 
        '''
        readDescription(self, description: MCacheFormatDescription,
                        descriptionFileLocation: MString,
                        baseFileName: MString)

        Synopsis
        -----
        Obtain the format description information. If the format returns
        true for handlesDescription(), then it must implement this
        method. The implementation should in turn call
        MCacheFormatDescription::setDistribution(), setTimePerFrame(),
        addDescriptionInfo() and addChannel() as appropriate using the
        supplied description object.In the default implementation, the
        xml description file is stored at descriptionFileLocation +
        baseFileName + ".xml"

        Returns:
        -----
        None

        Parameters:
        -----
        description: MCacheFormatDescription
        	[out] -> the description object to be set up 

        descriptionFileLocation: MString
        	[in] -> the default location of the description file 

        baseFileName: MString
        	[in] -> the default file name (without extension) of the description file


        '''
        pass

    def writeDescription(self, description: MCacheFormatDescription,
                        descriptionFileLocation: MString,
                        baseFileName: MString): 
        '''
        writeDescription(self, description: MCacheFormatDescription,
                        descriptionFileLocation: MString,
                        baseFileName: MString)

        Synopsis
        -----
        Store the format description information. If the format returns
        true for handlesDescription(), then it must implement this
        method. The implementation should in turn call
        MCacheFormatDescription::getDistribution(), getTimePerFrame(),
        getStartAndEndTimes(), getDescriptionInfo(), getNumChannels() and
        the various getChannelXXX() methods using the supplied
        description object as appropriate and store this information in
        such a way that it can be retrieved by readDescription().In the
        default implementation, the xml description file is stored at
        descriptionFileLocation + baseFileName + ".xml"Note that the
        plug-in is not required to store the description in a file using
        descriptionFileLocation and baseFileName. However, it must be
        able to retrieve the same description using just these strings to
        identify the source of the data.

        Returns:
        -----
        None

        Parameters:
        -----
        description: MCacheFormatDescription
        	[in] -> the description object that describes the format 

        descriptionFileLocation: MString
        	[in] -> the default location of the description file 

        baseFileName: MString
        	[in] -> the default file name (without extension) of the description file


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

class FileAccessMode:
    '''Cache file access modes. 
    Non-functional class.  Values for this enum:
    kRead
    kWrite
    kReadWrite
    '''

    def __init__(self):
        pass

    def kRead(self):
        '''This is an enum of FileAccessMode.
        - Description: read only 
        - Value: 0
        '''
        pass

    def kWrite(self):
        '''This is an enum of FileAccessMode.
        - Description: write only 
        - Value: 1
        '''
        pass

    def kReadWrite(self):
        '''This is an enum of FileAccessMode.
        - Description: read and write (e.g. append, edit, etc.) 
        - Value: 2
        '''
        pass

class MPxCameraSet:
    '''Base class for user-defined camera set nodes.
MPxCameraSet is the parent class of all user defined cameraSet nodes.
This class can be used to implement new kinds of cameraSets
within maya that behave in a similar manner to the cameraSet node
included in maya.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MPxNode.MPxNode

        Synopsis
        -----
        Returns the type of node that this is. This is used to
        differentiate user defined nodes that are derived off different
        MPx base classes.It is not necessary to override this
        method.Reimplemented from MPxNode.

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

    def thisMObject(self): 
        '''
        thisMObject(self) -> MObject

        Synopsis
        -----
        Returns the MObject associated with this user defined node. This
        makes it possible to use MFnDependencyNode or to construct plugs
        to this node's attributes.It is not necessary to override this
        method.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MPxCommand:
    '''Base class for user commands.
This is the proxy class for creating MEL commands through the
API.
Each command is derived from this one, and must have a
 method, and optionally
, and
 methods.
The
 method should collect whatever information is required to do the
task, and store it in local class data. It should finally call
 to make the command happen. The
 method should do the actual work, using only the local class
data. The
 method should undo the actual work, again using only the local
class data.
Maya contains support for infinite levels of undo. If a command
written in a plug-in changes the state of anything in Maya, it
should implement
 and
 methods. As well, if the
 method returns successfully, Maya will call the method's
 method immediately afterwards. If that method returns true, the
instance of this class is retained and passed to Maya's undo
manager so that the
 and
 methods can be called when appropriate. If
 returns false, the command instance is destroyed right away.
So, for example, if a command supports both
 and
 modes, in query mode the command should set a flag so that the
 method returns false to prevent that command instance from being
retained by the undo manager. In edit mode, where the state of
Maya is changed,
 should return true to enable undo and redo.
'''
    def __init__(self):
        pass


    def doIt(self, args: MArgList): 
        '''
        doIt(self, args: MArgList)

        Synopsis
        -----
        This method should perform a command by setting up internal class
        data and then calling the redoIt method. The actual action
        performed by the command should be done in the redoIt method.
        This is a pure virtual method, and must be overridden in derived
        classes.Reimplemented in MTemplateCreateNodeCommand<
        CommandClass, CommandName, NodeName >, MTemplateAction<
        ActionClass, CommandName, CommandSyntax >, MTemplateAction<
        CommandClass, CommandName, CommandSyntax >, MPxConstraintCommand,
        MPxPolyTweakUVInteractiveCommand, and MPxToolCommand.

        Returns:
        -----
        None

        Parameters:
        -----
        args: MArgList
        	[in] -> List of arguments passed to the command.


        '''
        pass

    def undoIt(self): 
        '''
        undoIt(self)

        Synopsis
        -----
        This method should undo the work done by the redoIt method based
        on the internal class data only. Reimplemented in
        MTemplateCreateNodeCommand< CommandClass, CommandName, NodeName
        >, and MPxConstraintCommand.

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
        This method should do the actual work of the command based on the
        internal class data only. Internal class data should be set in
        the doIt method.Reimplemented in MTemplateCreateNodeCommand<
        CommandClass, CommandName, NodeName >, and MPxConstraintCommand.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def isUndoable(self): 
        '''
        isUndoable(self) -> bool

        Synopsis
        -----
        This method is used to specify whether or not the command is
        undoable. In the base class, it always returns false. If you are
        writing a command that might be eligible for undo, you should
        override this method.After Maya executes the command's doIt
        method, it will call isUndoable. If isUndoable returns true, Maya
        will retain the instance of the class and pass it to Maya's undo
        manager so that the undoIt and redoIt methods can be called when
        appropriate. If isUndoable returns false, the command instance
        will be immediately destroyed.So, for example, if a command
        supports both query and edit modes, in query mode the command
        should set a flag so that the isUndoable method returns false to
        prevent that command instance from being retained by the undo
        manager. In edit mode, where the state of Maya is changed,
        isUndoable should return true to enable undo and
        redo.Reimplemented in MTemplateCommand< CommandClass,
        CommandName, CommandSyntax >, MTemplateCommand< CommandClass,
        CommandName, MTemplateCreateNodeCommand_newSyntax >, and
        MPxPolyTweakUVInteractiveCommand.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def hasSyntax(self): 
        '''
        hasSyntax(self) -> bool

        Synopsis
        -----
        This method specifies whether or not the command has a syntax
        object.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def syntax(self): 
        '''
        syntax(self) -> MSyntax

        Synopsis
        -----
        This method is intended to be used in an MArgDataBase or
        MArgParser contructor when the plugin command's syntax is being
        initialized. The user should declare and define a syntax
        contstructing method that must be registered with Maya by passing
        the function pointer as a parameter in
        MFnPlugin::registerCommand(). The result is that when
        MPxCommand::syntax() is called it returns the syntax object that
        the user has created in the custom syntax constructing method
        that was registered. To avoid conflicts it is important that the
        user's custom syntax defining method be given a name other than
        "syntax." It can have any other name as long as it corresponds
        with the function pointer used to register the method with Maya.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def isHistoryOn(self): 
        '''
        isHistoryOn(self) -> bool

        Synopsis
        -----
        Returns whether history is on.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def commandString(self): 
        '''
        commandString(self) -> MString

        Synopsis
        -----
        This method returns the command string that is associated with
        this command.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setHistoryOn(self, state: bool): 
        '''
        setHistoryOn(self, state: bool)

        Synopsis
        -----
        This method specifies if history for this command is on.

        Returns:
        -----
        None

        Parameters:
        -----
        state: bool
        	[in] -> true if history is to be on , false otherwise


        '''
        pass

    def setCommandString(self, name: MString): 
        '''
        setCommandString(self, name: MString)

        Synopsis
        -----
        Sets the command string that is associated with this command
        object.

        Returns:
        -----
        None

        Parameters:
        -----
        name: MString
        	[in] -> The command name to be set


        '''
        pass

    def displayInfo(self, theInfo: MString): 
        '''
        displayInfo(self, theInfo: MString)

        Synopsis
        -----
        This method is used to display information in the script editor.

        Returns:
        -----
        None

        Parameters:
        -----
        theInfo: MString
        	[in] -> The string to be displayed 


        '''
        pass

    def displayWarning(self, theWarning: MString,
                        showLineNumber: bool): 
        '''
        displayWarning(self, theWarning: MString,
                        showLineNumber: bool)

        Synopsis
        -----
        This method is used to display a warning in the script editor.
        NOTE: Displaying of line numbers must be enabled in the MEL
        editor window before the showLineNumber parameter has an affect.

        Returns:
        -----
        None

        Parameters:
        -----
        theWarning: MString
        	[in] -> The warning string to be displayed 

        showLineNumber: bool
        	[in] -> Set to true if you want the line number of this command to be displayed. See NOTE above. 


        '''
        pass

    def displayError(self, theError: MString,
                        showLineNumber: bool): 
        '''
        displayError(self, theError: MString,
                        showLineNumber: bool)

        Synopsis
        -----
        This method is used to display an error in the script editor.
        NOTE: Displaying of line numbers must be enabled in the MEL
        editor window before the showLineNumber parameter has an affect.

        Returns:
        -----
        None

        Parameters:
        -----
        theError: MString
        	[in] -> The error string to be displayed 

        showLineNumber: bool
        	[in] -> Set to true if you want the line number of this command to be displayed See NOTE above. 


        '''
        pass

    @overload
    def setResult(self, val: int): 
        '''
        setResult(self, val: int)

        Synopsis
        -----
        This method puts the given value into the return value area for a
        command. The value is cast to an int internally because the Maya
        command engine does not support unsigned ints.

        Returns:
        -----
        None

        Parameters:
        -----
        val: int
        	[in] -> The value to be set 


        '''
        pass

    @overload
    def setResult(self, val: int): 
        '''
        setResult(self, val: int)

        Synopsis
        -----
        This method puts the given value into the return value area for a
        command.

        Returns:
        -----
        None

        Parameters:
        -----
        val: int
        	[in] -> The value to be set 


        '''
        pass

    @overload
    def setResult(self, val: double): 
        '''
        setResult(self, val: double)

        Synopsis
        -----
        This method puts the given value into the return value area for a
        command.

        Returns:
        -----
        None

        Parameters:
        -----
        val: double
        	[in] -> The value to be set 


        '''
        pass

    @overload
    def setResult(self, val: bool): 
        '''
        setResult(self, val: bool)

        Synopsis
        -----
        This method puts the given value into the return value area for a
        command.

        Returns:
        -----
        None

        Parameters:
        -----
        val: bool
        	[in] -> The value to be set 


        '''
        pass

    @overload
    def setResult(self, val: char): 
        '''
        setResult(self, val: char)

        Synopsis
        -----
        This method puts the given value into the return value area for a
        command.

        Returns:
        -----
        None

        Parameters:
        -----
        val: char
        	[in] -> The value to be set 


        '''
        pass

    @overload
    def setResult(self, val: MString): 
        '''
        setResult(self, val: MString)

        Synopsis
        -----
        This method puts the given value into the return value area for a
        command.

        Returns:
        -----
        None

        Parameters:
        -----
        val: MString
        	[in] -> The value to be set 


        '''
        pass

    @overload
    def setResult(self, val: MIntArray): 
        '''
        setResult(self, val: MIntArray)

        Synopsis
        -----
        This method puts the given values into the return value area for
        a command.

        Returns:
        -----
        None

        Parameters:
        -----
        val: MIntArray
        	[in] -> The value to be set 


        '''
        pass

    @overload
    def setResult(self, val: MDoubleArray): 
        '''
        setResult(self, val: MDoubleArray)

        Synopsis
        -----
        This method puts the given values into the return value area for
        a command.

        Returns:
        -----
        None

        Parameters:
        -----
        val: MDoubleArray
        	[in] -> The value to be set 


        '''
        pass

    @overload
    def setResult(self, val: MStringArray): 
        '''
        setResult(self, val: MStringArray)

        Synopsis
        -----
        This method puts the given values into the return value area for
        a command.

        Returns:
        -----
        None

        Parameters:
        -----
        val: MStringArray
        	[in] -> The value to be set 


        '''
        pass

    @overload
    def appendToResult(self, val: int): 
        '''
        appendToResult(self, val: int)

        Synopsis
        -----
        This method will add the given value to the end of the result
        array of integers. The result array can only be of a single type
        so this method can only be used when the result string has not
        been set or is already of integer type.Note: appendToResult
        cannot be used in conjunction with setResult.

        Returns:
        -----
        None

        Parameters:
        -----
        val: int
        	[in] -> The value to be added 


        '''
        pass

    @overload
    def appendToResult(self, val: double): 
        '''
        appendToResult(self, val: double)

        Synopsis
        -----
        This method will add the given value to the end of the result
        array of doubles. The result array can only be of a single type
        so this method can only be used when the result string has not
        been set or is already of type double.Note: appendToResult cannot
        be used in conjunction with setResult.

        Returns:
        -----
        None

        Parameters:
        -----
        val: double
        	[in] -> The value to be added 


        '''
        pass

    @overload
    def appendToResult(self, val: bool): 
        '''
        appendToResult(self, val: bool)

        Synopsis
        -----
        This method will add the given value to the end of the result
        array of integers. The result array can only be of a single type
        so this method can only be used when the result string has not
        been set or is already of integer type.Note: appendToResult
        cannot be used in conjunction with setResult.

        Returns:
        -----
        None

        Parameters:
        -----
        val: bool
        	[in] -> The value to be added 


        '''
        pass

    @overload
    def appendToResult(self, val: char): 
        '''
        appendToResult(self, val: char)

        Synopsis
        -----
        This method will add the given value to the end of the result
        array of strings. The result array can only be of a single type
        so this method can only be used when the result string has not
        been set or is already of type string.Note: appendToResult cannot
        be used in conjunction with setResult.

        Returns:
        -----
        None

        Parameters:
        -----
        val: char
        	[in] -> The value to be added 


        '''
        pass

    @overload
    def appendToResult(self, val: MString): 
        '''
        appendToResult(self, val: MString)

        Synopsis
        -----
        This method will add the given value to the end of the result
        array of strings. The result array can only be of a single type
        so this method can only be used when the result string has not
        been set or is already of type string.Note: appendToResult cannot
        be used in conjunction with setResult.

        Returns:
        -----
        None

        Parameters:
        -----
        val: MString
        	[in] -> The value to be added 


        '''
        pass

    @overload
    def appendToResult(self, val: MStringArray): 
        '''
        appendToResult(self, val: MStringArray)

        Synopsis
        -----
        This method will add the given value to the end of the result
        array of strings. The result array can only be of a single type
        so this method can only be used when the result string has not
        been set or is already of type string.Note: appendToResult cannot
        be used in conjunction with setResult.

        Returns:
        -----
        None

        Parameters:
        -----
        val: MStringArray
        	[in] -> The value to be added 


        '''
        pass

    def isCurrentResultArray(self): 
        '''
        isCurrentResultArray(self) -> bool

        Synopsis
        -----
        This method will return whether the return result for the command
        is an array or not.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def currentResultType(self): 
        '''
        currentResultType(self) -> MPxCommand.MPxCommand

        Synopsis
        -----
        This method will return the type of the current result for the
        command. ReturnValue

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def getCurrentResult(self, val: MIntArray): 
        '''
        getCurrentResult(self, val: MIntArray)

        Synopsis
        -----
        This method gets the current node's result as an array of
        integers, if possible.

        Returns:
        -----
        None

        Parameters:
        -----
        val: MIntArray
        	[out] -> Storage for the return value


        '''
        pass

    @overload
    def getCurrentResult(self, val: MDoubleArray): 
        '''
        getCurrentResult(self, val: MDoubleArray)

        Synopsis
        -----
        This method gets the current node's result as an array of
        doubles, if possible.

        Returns:
        -----
        None

        Parameters:
        -----
        val: MDoubleArray
        	[out] -> Storage for the return value


        '''
        pass

    @overload
    def getCurrentResult(self, val: MStringArray): 
        '''
        getCurrentResult(self, val: MStringArray)

        Synopsis
        -----
        This method gets the current node's result as an array of
        strings, if possible.

        Returns:
        -----
        None

        Parameters:
        -----
        val: MStringArray
        	[out] -> Storage for the return value


        '''
        pass

    def currentIntResult(self, ReturnStatus: MPxCommand.MStatus): 
        '''
        currentIntResult(self, ReturnStatus: MPxCommand.MStatus) -> int

        Synopsis
        -----
        This method gets the current node's result as a int, if possible.

        Returns: 
        ----- 
        The int result.

        Parameters:
        -----
        ReturnStatus: MPxCommand.MStatus
        	[out] -> Optional status code. See below.


        '''
        pass

    def currentDoubleResult(self, ReturnStatus: MPxCommand.MStatus): 
        '''
        currentDoubleResult(self, ReturnStatus: MPxCommand.MStatus) -> double

        Synopsis
        -----
        This method gets the current node's result as a double, if
        possible.

        Returns: 
        ----- 
        The double result.

        Parameters:
        -----
        ReturnStatus: MPxCommand.MStatus
        	[out] -> Optional status code. See below.


        '''
        pass

    def currentStringResult(self, ReturnStatus: MPxCommand.MStatus): 
        '''
        currentStringResult(self, ReturnStatus: MPxCommand.MStatus) -> MString

        Synopsis
        -----
        This method gets the current node's result as a MString, if
        possible.

        Returns: 
        ----- 
        The string result.

        Parameters:
        -----
        ReturnStatus: MPxCommand.MStatus
        	[out] -> Optional status code. See below.


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

class MResultType:
    '''Types of results from commands. 
    Non-functional class.  Values for this enum:
    kLong
    kDouble
    kString
    kNoArg
    '''

    def __init__(self):
        pass

    def kLong(self):
        '''This is an enum of MResultType.
        - Description:  
        - Value: 0
        '''
        pass

    def kDouble(self):
        '''This is an enum of MResultType.
        - Description:  
        - Value: 1
        '''
        pass

    def kString(self):
        '''This is an enum of MResultType.
        - Description:  
        - Value: 2
        '''
        pass

    def kNoArg(self):
        '''This is an enum of MResultType.
        - Description:  
        - Value: 3
        '''
        pass

class MPxComponentShape:
    '''Component helper class for surface shapes.
MPxComponentShape allows the implementation of new user defined shapes using
components. User defined shapes are dependency nodes (and DAG
nodes) which contain overridable drawing, selection, and
component methods. This class provides enhanced functionality for
working with components. As a result, it is a better starting
point than
MPxSurfaceShape for writing surface shape components.
This class provides methods to manipulate and select the
components that make up the shape.
'''
    def __init__(self):
        pass


    @overload
    def transformUsing(self, matrix: MMatrix,
                        componentList: MObjectArray): 
        '''
        transformUsing(self, matrix: MMatrix,
                        componentList: MObjectArray) -> MPxComponentShape.OPENMAYA_MAJOR_NAMESPACE_OPENvoid

        Synopsis
        -----
        Transform the given components using the specified transformation
        matrix. This method should be overridden if the shape supports
        components that can be transformed using maya's move, scale, and
        rotate tools.Reimplemented from MPxSurfaceShape.

        Returns:
        -----
        None

        Parameters:
        -----
        matrix: MMatrix
        	[in] -> the matrix representing the transformation that is to be applied to the components 

        componentList: MObjectArray
        	[in] -> a list of components to be tranformed 


        '''
        pass

    @overload
    def transformUsing(self, mat: MMatrix,
                        componentList: MObjectArray,
                        cachingMode: MPxSurfaceShape.MPxSurfaceShape,
                        pointCache: MPointArray): 
        '''
        transformUsing(self, mat: MMatrix,
                        componentList: MObjectArray,
                        cachingMode: MPxSurfaceShape.MPxSurfaceShape,
                        pointCache: MPointArray)

        Synopsis
        -----
        Transform the given components using the specified transformation
        matrix. This method should be overridden if the shape supports
        components that can be transformed using maya's move, scale, and
        rotate tools.Reimplemented from MPxSurfaceShape.

        Returns:
        -----
        None

        Parameters:
        -----
        mat: MMatrix
        	[in] -> the matrix representing the transformation that is to be applied to the components 

        componentList: MObjectArray
        	[in] -> a list of components to be tranformed. If the list is empty, it indicates that every point in the geometry should be transformed. 

        cachingMode: MPxSurfaceShape.MPxSurfaceShape
        	[in] -> whether the points should be cached in the pointCache argument, or restored from the pointCache. 

        pointCache: MPointArray
        	[in] -> used to store for undo and restore points during undo 


        '''
        pass

    def componentToPlugs(self, component: MObject,
                        list: MSelectionList): 
        '''
        componentToPlugs(self, component: MObject,
                        list: MSelectionList)

        Synopsis
        -----
        Converts the given component into a selection list of plugs. This
        method is used to associate a shapes components into the
        corresponding attributes (plugs) within the shape.Reimplemented
        from MPxSurfaceShape.

        Returns:
        -----
        None

        Parameters:
        -----
        component: MObject
        	[in] -> the component to be converted 

        list: MSelectionList
        	[in] -> a selection list where the plug should be added 


        '''
        pass

    def match(self, mask: MSelectionMask,
                        componentList: MObjectArray): 
        '''
        match(self, mask: MSelectionMask,
                        componentList: MObjectArray) -> bool

        Synopsis
        -----
        This method is used to check for matches between a selection type
        (or mask) and a given component. This method is used to match up
        your components with selection masks.This is used by sets and
        deformers to make sure that the selected components fall into the
        "vertex only" category. This is useful when you want to make sure
        that only a particular component can be deformed.Reimplemented
        from MPxSurfaceShape.

        Returns: 
        ----- 
        true the match was successfull  false the match failed

        Parameters:
        -----
        mask: MSelectionMask
        	[in] -> the selection mask to test against 

        componentList: MObjectArray
        	[in] -> a list of components to be tested


        '''
        pass

    def createFullVertexGroup(self): 
        '''
        createFullVertexGroup(self) -> MObject

        Synopsis
        -----
        This method is used to create a component containing every
        vertex/CV in the object. This method is supposed to return non-
        NULL only if the dag object contains vertices/CVs (control
        points), so derived classes that do should override this
        method.Eg: use MFnSingleIndexedComponent::setCompleteData(
        numVertices ) to specify that a component represents all the
        vertices of the shape.Reimplemented from MPxSurfaceShape.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def localShapeInAttr(self): 
        '''
        localShapeInAttr(self) -> MObject

        Synopsis
        -----
        Returns the input attribute of the shape, which are the control
        points. Reimplemented from MPxSurfaceShape.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setControlPoints(self, cps: MVectorArray): 
        '''
        setControlPoints(self, cps: MVectorArray)

        Synopsis
        -----
        Push the given control points into the node's data block.

        Returns:
        -----
        None

        Parameters:
        -----
        cps: MVectorArray
        	[in] -> the control points to use 


        '''
        pass

class MPxConstraint:
    '''Proxy constraint node.
MPxConstraint is the parent class for user defined constraint nodes. Position,
orientation or scale of an object can be constrained by other
objects. This class works in conjunction with the
MPxConstraintCommand class.
'''
    def __init__(self):
        pass


    def weightAttribute(self): 
        '''
        weightAttribute(self) -> const MObject

        Synopsis
        -----
        Returns the weight attribute for the constraint. Default
        implementation returns MObject::kNullObj.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def targetAttribute(self): 
        '''
        targetAttribute(self) -> const MObject

        Synopsis
        -----
        Returns the target attribute for the constraint. Default
        implementation returns MObject::kNullObj.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def constraintRotateOrderAttribute(self): 
        '''
        constraintRotateOrderAttribute(self) -> const MObject

        Synopsis
        -----
        Returns the rotate order attribute for the constraint. Default
        implementation returns MObject::kNullObj.If is only necessary to
        override this method if the constraint will control rotation.

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

    def thisMObject(self): 
        '''
        thisMObject(self) -> MObject

        Synopsis
        -----
        Returns the MObject associated with this user defined node. This
        makes it possible to use MFnDependencyNode or to construct plugs
        to this node's attributes.It is not necessary to override this
        method.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def passiveOutputAttribute(self): 
        '''
        passiveOutputAttribute(self) -> const MObject

        Synopsis
        -----
        Returns the passive output attribute for the constraint. Default
        implementation returns MObject::kNullObj.Passive output
        attributes do not prevent value modifications to the destination
        attribute when connected.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getOutputAttributes(self, attributeArray: MObjectArray): 
        '''
        getOutputAttributes(self, attributeArray: MObjectArray)

        Synopsis
        -----
        Returns output attributes for the constraint. Default
        implementation clears the input attributeArray and returns.

        Returns:
        -----
        None

        Parameters:
        -----
        attributeArray: MObjectArray
        	[out] -> Array of output attributes. 


        '''
        pass

    def closestPoint(self, dataGeometryObject: MObject,
                        toThisPoint: MPoint,
                        theClosestPoint: MPoint): 
        '''
        closestPoint(self, dataGeometryObject: MObject,
                        toThisPoint: MPoint,
                        theClosestPoint: MPoint)

        Synopsis
        -----
        Returns the closest point on this surface to the given point.

        Returns:
        -----
        None

        Parameters:
        -----
        dataGeometryObject: MObject
        	[in] -> surface 

        toThisPoint: MPoint
        	[in] -> the point to evaluate from 

        theClosestPoint: MPoint
        	[out] -> the calculated closest point


        '''
        pass

    def closestNormal(self, dataGeometryObject: MObject,
                        toThisPoint: MPoint,
                        theNormal: MVector): 
        '''
        closestNormal(self, dataGeometryObject: MObject,
                        toThisPoint: MPoint,
                        theNormal: MVector)

        Synopsis
        -----
        Returns the closest normal on this surface to the given point.

        Returns:
        -----
        None

        Parameters:
        -----
        dataGeometryObject: MObject
        	[in] -> surface 

        toThisPoint: MPoint
        	[in] -> the point to evaluate from 

        theNormal: MVector
        	[out] -> the calculated closest normal


        '''
        pass

    def closestTangent(self, dataGeometryObject: MObject,
                        toThisPoint: MPoint,
                        theTangent: MVector): 
        '''
        closestTangent(self, dataGeometryObject: MObject,
                        toThisPoint: MPoint,
                        theTangent: MVector)

        Synopsis
        -----
        Returns the closest tangent on this surface to the given point.

        Returns:
        -----
        None

        Parameters:
        -----
        dataGeometryObject: MObject
        	[in] -> surface 

        toThisPoint: MPoint
        	[in] -> the point to evaluate from 

        theTangent: MVector
        	[out] -> the calculated closest tangent


        '''
        pass

    def computeAim(self, parentInverseMatrix: MMatrix,
                        targetVector: MVector,
                        aimVector: MVector,
                        upVector: MVector,
                        wUpVector: MVector,
                        order: MEulerRotation.MEulerRotation,
                        jointOrient: MQuaternion,
                        ResultStatus: MPxConstraint.MStatus): 
        '''
        computeAim(self, parentInverseMatrix: MMatrix,
                        targetVector: MVector,
                        aimVector: MVector,
                        upVector: MVector,
                        wUpVector: MVector,
                        order: MEulerRotation.MEulerRotation,
                        jointOrient: MQuaternion,
                        ResultStatus: MPxConstraint.MStatus) -> MEulerRotation

        Synopsis
        -----
        Returns the rotation which aligns the aimVector in local space
        with the targetVector in local space while keeping the upVector
        in local space and the wUpVector world space aligned as closely
        as possible.

        Returns: 
        ----- 
        Aim rotation.

        Parameters:
        -----
        parentInverseMatrix: MMatrix
        	[in] -> 

        targetVector: MVector
        	[in] -> 

        aimVector: MVector
        	[in] -> 

        upVector: MVector
        	[in] -> 

        wUpVector: MVector
        	[in] -> 

        order: MEulerRotation.MEulerRotation
        	[in] -> 

        jointOrient: MQuaternion
        	[in] -> 

        ResultStatus: MPxConstraint.MStatus
        	[out] -> 


        '''
        pass

    def worldUpVector(self, upType: MPxConstraint.MPxConstraint,
                        upVector: MVector,
                        upMatrix: MMatrix,
                        constrPoint: MPoint,
                        ResultStatus: MPxConstraint.MStatus): 
        '''
        worldUpVector(self, upType: MPxConstraint.MPxConstraint,
                        upVector: MVector,
                        upMatrix: MMatrix,
                        constrPoint: MPoint,
                        ResultStatus: MPxConstraint.MStatus) -> MVector

        Synopsis
        -----
        Returns the world up vector based on the requested up type.

        Returns: 
        ----- 
        World up vector.

        Parameters:
        -----
        upType: MPxConstraint.MPxConstraint
        	[in] -> 

        upVector: MVector
        	[in] -> 

        upMatrix: MMatrix
        	[in] -> 

        constrPoint: MPoint
        	[in] -> 

        ResultStatus: MPxConstraint.MStatus
        	[out] -> 


        '''
        pass

    def worldConstraintPoint(self, parentInverseMatrix: MMatrix,
                        translate: MVector,
                        rotatePivot: MVector,
                        rotatePivotTranslate: MVector,
                        ResultStatus: MPxConstraint.MStatus): 
        '''
        worldConstraintPoint(self, parentInverseMatrix: MMatrix,
                        translate: MVector,
                        rotatePivot: MVector,
                        rotatePivotTranslate: MVector,
                        ResultStatus: MPxConstraint.MStatus) -> MPoint

        Synopsis
        -----
        Returns the world constraint point.

        Returns: 
        ----- 
        World constraint point.

        Parameters:
        -----
        parentInverseMatrix: MMatrix
        	[in] -> 

        translate: MVector
        	[in] -> 

        rotatePivot: MVector
        	[in] -> 

        rotatePivotTranslate: MVector
        	[in] -> 

        ResultStatus: MPxConstraint.MStatus
        	[out] -> 


        '''
        pass

    def enableRestPosition(self): 
        '''
        enableRestPosition(self) -> MPxConstraint.OPENMAYA_MAJOR_NAMESPACE_OPEN MObject

        Synopsis
        -----
        Node attribute: enableRestPosition/erp - boolean. This attribute
        defines the constraint behavior when all weights are at zero.If
        true, the constraint goes to the restTranslate position when all
        weights are zero. If false, the constraint output is not computed
        when all weights are zero.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def lockOutput(self): 
        '''
        lockOutput(self) -> MObject

        Synopsis
        -----
        Node attribute: lockOutput/lo - boolean. When enabled, the
        constrained object cannot be moved away from its constrained
        location, and a pairBlend will not be inserted if the user tries
        to keyframe the constrained attributes.This allows for the
        pre-5.0 behavior of constraints. When disabled, the constrained
        object can be moved away from the constraint and a pairBlend will
        be inserted if the object is keyframed and the animation blending
        preference specifies that blending is enabled.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class UpVectorType:
    '''The type of up vector. 
    Non-functional class.  Values for this enum:
    kScene
    kObject
    kObjectRotation
    kVector
    kLast
    '''

    def __init__(self):
        pass

    def kScene(self):
        '''This is an enum of UpVectorType.
        - Description: Scene up vector. 
        - Value: 0
        '''
        pass

    def kObject(self):
        '''This is an enum of UpVectorType.
        - Description: Object up vector. 
        - Value: 1
        '''
        pass

    def kObjectRotation(self):
        '''This is an enum of UpVectorType.
        - Description: Object rotation up vector. 
        - Value: 2
        '''
        pass

    def kVector(self):
        '''This is an enum of UpVectorType.
        - Description: Specified vector. 
        - Value: 3
        '''
        pass

    def kLast(self):
        '''This is an enum of UpVectorType.
        - Description: Last value, used for counting. 
        - Value: 4
        '''
        pass

class MPxConstraintCommand:
    '''Proxy constraint command.
MPxConstraintCommand is the base class for user defined commands which create
constraints. This command gives all of the flags and options of
the base constraint command and in addition allows user defined
flags or behaviours. When registering this command, use the
MFnPlugin::registerConstraintCommand() method. A
MPxConstraint is also required to be used with
MPxConstraintCommand. The
constraintTypeId() virtual must be implemented to return the correct constraint
node type id.
'''
    def __init__(self):
        pass


    def doIt(self, args: MArgList): 
        '''
        doIt(self, args: MArgList)

        Synopsis
        -----
        This virtual method is called when the command is intially
        executed (i.e. before any subsequent undo or redo). Normal usage
        is to do any specialized setup or non-editable flags that your
        command requires here and then return MS::kUnknownParameter so
        that Maya will do its default behaviour. However, you can also
        take complete control of the command by returning MS::kSuccess
        instead.On query the default behaviour is to call the following
        methods:On create the default behaviour is to call the following
        methods:On edit the default behaviour is to call the following
        methods:If you do not return MS::kUnknownParameter then none of
        these methods will be called and you will be responsible for
        performing the equivalent actions yourself.Internally Maya uses
        the equivalent of an MDGModifier to keep track of the changes it
        makes, for later use in undo/redo. Although this modifier is
        provided to some of the class's virtual methods, such as
        setRestPosition(), it is not provided to doIt(), undoIt() or
        redoIt(). So if you decided to take complete control of one of
        the three (i.e. by returning MS::kSuccess) then you will need to
        take full control of all three.Reimplemented from MPxCommand.

        Returns:
        -----
        None

        Parameters:
        -----
        args: MArgList
        	[in] -> the command's argument list.


        '''
        pass

    def undoIt(self): 
        '''
        undoIt(self)

        Synopsis
        -----
        This virtual method is called when the command is being undone.
        Normal usage is to undo any specialized setup that you did in
        doIt() and then return MS::kUnknownParameter so that Maya will do
        its default behaviour.The default behaviour is to undo the
        command's internal DG modifier. See doIt() for more
        details.Reimplemented from MPxCommand.

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
        This virtual method is called when the command is being redone.
        Normal usage is to redo any specialized setup that you did in
        doIt() and then return MS::kUnknownParameter so that Maya will do
        its default behaviour.The default behaviour is to redo the
        command's internal DG modifier. See doIt() for more
        details.Reimplemented from MPxCommand.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def appendSyntax(self): 
        '''
        appendSyntax(self)

        Synopsis
        -----
        This method should be overridden to append syntax to the
        constraint command. The syntax object can be obtained by calling
        the syntax method. The following flags cannot be used as user-
        defined flags as they are reserved for edit and query: "-e",
        "-edit", "-q", "-query".Standard constraint flags that are
        provided are: name "-n" "-name", weight "-w" "-weight", target
        list "-tl" "-targetList", remove "-rm" "-remove", target alias
        "-wal" "-weightAliasList".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def parseArgs(self, argList: MArgList): 
        '''
        parseArgs(self, argList: MArgList)

        Synopsis
        -----
        This virtual method is called by the default behaviour of doIt()
        to parse the command's arguments. Normal usage is to override
        this method to parse any flags or command arguments which are
        specific to your command, and then return MS::kUnknownParameter
        to have Maya do its default behaviour.The default behaviour is:

        Returns:
        -----
        None

        Parameters:
        -----
        argList: MArgList
        	[in] -> the command's argument list.


        '''
        pass

    def syntax(self, ReturnStatus: MPxConstraintCommand.MStatus): 
        '''
        syntax(self, ReturnStatus: MPxConstraintCommand.MStatus) -> MSyntax

        Synopsis
        -----
        USE _syntax() IN PYTHON. This method returns the syntax object of
        this constraint command.The syntax object can be appended to in
        an overridden version of the appendSyntax method.

        Returns: 
        ----- 
        the syntax object

        Parameters:
        -----
        ReturnStatus: MPxConstraintCommand.MStatus
        	[out] -> return status


        '''
        pass

    def doEdit(self): 
        '''
        doEdit(self)

        Synopsis
        -----
        This virtual method is called by the default behaviour of doIt()
        if the command was executed in create or edit mode (i.e. not
        query). Normal usage is to handle any custom editable flags that
        your command supports and then return MS::kUnknownParameter so
        that Maya will do its default behaviour.If the -remove flag was
        set, the default behaviour is to disconnect the targets specified
        on the command line.If the -remove flag was not set, the default
        behaviour is:

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def doCreate(self): 
        '''
        doCreate(self)

        Synopsis
        -----
        This virtual method is called by the default behaviour of doIt()
        when the command is being executed in create mode. It is not
        normally useful to override this method since the node will not
        be created until after the override has returned control to
        Maya.The default behaviour is to:

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def doQuery(self): 
        '''
        doQuery(self)

        Synopsis
        -----
        This virtual method is called by the default behaviour of doIt()
        when the command is being executed in query mode. Normal usage is
        to process the queries for flags which are specific to your
        command and return MS::kSuccess. If none of your command-specific
        flags is being queried then return MS::kUnknownParameter so that
        Maya will handle queries for the standard flags.The default
        behaviour is:If multiple flags are queried only the value of the
        first one will be set as the command's return value, where
        "first" refers to the order in which they are checked, not the
        order in which the appear in the command.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def createdConstraint(self, constraint: MPxConstraint): 
        '''
        createdConstraint(self, constraint: MPxConstraint)

        Synopsis
        -----
        This method is called when an MPxConstraintCommand creates a new
        MPxConstraint node. It can be used for transferring state from
        the command to the node object.

        Returns:
        -----
        None

        Parameters:
        -----
        constraint: MPxConstraint
        	[in] -> the constraint node created by the command. 


        '''
        pass

    def supportsOffset(self): 
        '''
        supportsOffset(self) -> bool

        Synopsis
        -----
        This method is used to control if the constraint supports offset.
        Return true if the constraint should support offset. False is
        returned otherwise and is the default behaviour of this method.If
        this method returns true, then the offsetAttribute() and
        constraintOutputAttribute() methods should both return attributes
        of type MFnNumericData::k3Double. If constraintRestAttribute()
        returns an attribute it should be k3Double as well.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def hasVectorFlags(self): 
        '''
        hasVectorFlags(self) -> bool

        Synopsis
        -----
        This method is used to control if the constraint supports the
        base class vector flags. Return true if the constraint should
        support the vector flags. False is returned otherwise and is the
        default behaviour of this method.If this method returns true,
        then the following methods need to return valid attributes:
        aimVectorAttribute(), upVectorAttribute()
        worldUpMatrixAttribute(), worldUpTypeAttribute(),
        worldUpVectorAttribute().

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def constraintTypeId(self): 
        '''
        constraintTypeId(self) -> MTypeId

        Synopsis
        -----
        This method is used to return the MTypeId of the MPxConstraint
        node that is used with this command. This virtual must be
        implemented in a proxy constraint command.This method must be
        implemented.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def targetType(self): 
        '''
        targetType(self) -> MPxConstraintCommand.MPxConstraintCommand

        Synopsis
        -----
        Maya supports constraints targets which are either transforms or
        nodes derived from "geometryShape". Return the appropriate target
        type in this method.By default, this method returns
        MPxConstraintCommand::kTransform.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def aimVectorAttribute(self): 
        '''
        aimVectorAttribute(self) -> const MObject&

        Synopsis
        -----
        This method returns an attribute which defines the aim vector of
        a constraint. The aimVector attribute defines a vector in the
        space of the constrained object that should be aligned with the
        weighted average vector computed by the constraint. The
        upVectorAttribute(), worldUpVectorAttribute(),
        worldUpMatrixAttribute, and worldUpTypeAttribute() define how the
        constrained object is rotated about the aimVector.The type of the
        returned attribute must be MFnNumericData::k3Double.The default
        behaviour of the method is to return a MObject::kNullObj (i.e. no
        attribute).

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def upVectorAttribute(self): 
        '''
        upVectorAttribute(self) -> const MObject&

        Synopsis
        -----
        This method returns an upVector attribute that is used in
        conjunction with the aimVector. The type of the returned
        attribute must be MFnNumericData::k3Double.The default behaviour
        of the method is to return a MObject::kNullObj (i.e. no
        attribute).

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def worldUpMatrixAttribute(self): 
        '''
        worldUpMatrixAttribute(self) -> const MObject&

        Synopsis
        -----
        This method returns an worldUpMatrix attribute that is used in
        conjunction with the aimVector. The worldUpMatrix returned should
        be a matrix attribute.The default behaviour of the method is to
        return a MObject::kNullObj (i.e. no attribute).

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def worldUpTypeAttribute(self): 
        '''
        worldUpTypeAttribute(self) -> const MObject&

        Synopsis
        -----
        This method returns an worldUpType attribute that is used in
        conjunction with the aimVector. The worldUpType returned should
        be a enum attribute.The default behaviour of the method is to
        return a MObject::kNullObj (i.e. no attribute).

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def worldUpVectorAttribute(self): 
        '''
        worldUpVectorAttribute(self) -> const MObject&

        Synopsis
        -----
        This method returns an worldUpVector attribute that is used in
        conjunction with the aimVector. The type of the returned
        attribute must be MFnNumericData::k3Double.The default behaviour
        of the method is to return a MObject::kNullObj (i.e. no
        attribute).

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def offsetAttribute(self): 
        '''
        offsetAttribute(self) -> const MObject&

        Synopsis
        -----
        This method returns the offset attribute and must be implemented
        if supportsOffset() returns true. The type of the returned
        attribute must be MFnNumericData::k3Double.The default behaviour
        of the method is to return a MObject::kNullObj (i.e. no
        attribute).

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def constraintInstancedAttribute(self): 
        '''
        constraintInstancedAttribute(self) -> const MObject&

        Synopsis
        -----
        This method returns the attribute on the constraint node that
        connects to an instanced constraint attribute of the constrained
        object. The type of the attribute will depend on the constraint
        implementation.The default behaviour of the method is to return a
        MObject::kNullObj (i.e. no attribute).

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def constraintOutputAttribute(self): 
        '''
        constraintOutputAttribute(self) -> const MObject&

        Synopsis
        -----
        This method returns the attribute this constraint will connect to
        the constrained attribute of the constrained object. The type of
        the attribute will depend on the constraint implementation.
        Normally this is an MFnNumericData::k3Double attribute. To
        support an output attribute of any other type, you must do the
        following:The default behaviour of the method is to return
        MObject::kNullObj (i.e. no attribute).

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def constraintRestAttribute(self): 
        '''
        constraintRestAttribute(self) -> const MObject&

        Synopsis
        -----
        This method returns the attribute used to store the constraint's
        rest state. Constraints supporting rest state should implement
        this method.Usually the type of this attribute is
        MFnNumericData::k3Double. If you return an attribute with any
        other type then you will have to override setRestPosition() to
        handle it properly.The default behaviour of the method is to
        return a MObject::kNullObj (i.e. no attribute).

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def constraintEnableRestAttribute(self): 
        '''
        constraintEnableRestAttribute(self) -> const MObject&

        Synopsis
        -----
        This method returns the attribute used to enable and disable the
        rest state at runtime. Constraints supporting rest state should
        implement this method.The constraintRest attribute is a
        boolean.The default behaviour of the method is to return a
        MObject::kNullObj (i.e no attribute).

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def constraintTargetInstancedAttribute(self): 
        '''
        constraintTargetInstancedAttribute(self) -> const MObject&

        Synopsis
        -----
        This method returns the constraintTargetInstanced attribute for
        the constraint. The type of the attribute will depend on the
        constraint implementation. Suggested attribute types include a
        parent matrix or target geometry.The default behaviour of the
        method is to return a MObject::kNullObj (i.e. no attribute).

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def constraintTargetAttribute(self): 
        '''
        constraintTargetAttribute(self) -> const MObject&

        Synopsis
        -----
        This method returns the constraintTarget attribute for the
        constraint. The type of the attribute will depend on the
        constraint implementation but it must be an compound array
        attribute.The default behaviour of the method is to return a
        MObject::kNullObj (i.e. no attribute).

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def constraintTargetWeightAttribute(self): 
        '''
        constraintTargetWeightAttribute(self) -> const MObject&

        Synopsis
        -----
        This method returns the constraintTargetWeight attribute for the
        constraint. The type of the constraintTargetWeight attribute is a
        double.The default behaviour of the method is to return a
        MObject::kNullObj (i.e. no attribute).

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def objectAttribute(self): 
        '''
        objectAttribute(self) -> const MObject&

        Synopsis
        -----
        This method returns the attribute this constraint will drive on
        the constrained object. The type of the returned attribute must
        be the same as that returned by constraintOutputAttribute().The
        default behaviour of the method is to return a MObject::kNullObj
        (i.e. no attribute).

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getObjectAttributesArray(self, array: MObjectArray): 
        '''
        getObjectAttributesArray(self, array: MObjectArray)

        Synopsis
        -----
        This method returns the list of attributes this particular
        constraint considers when inserting a pair blend.

        Returns:
        -----
        None

        Parameters:
        -----
        array: MObjectArray
        	[out] -> Array of attributes. 


        '''
        pass

    def handleNewTargets(self, dagObject: MDagPath): 
        '''
        handleNewTargets(self, dagObject: MDagPath)

        Synopsis
        -----
        This method is used to perform any special processing when
        targets are added to the constraint. For example, the constraint
        may need to keep track of the list of targets to properly
        calculate an offset.

        Returns:
        -----
        None

        Parameters:
        -----
        dagObject: MDagPath
        	[in] -> path to the new constraint target 


        '''
        pass

    def connectTarget(self, targetPath: MDagPath,
                        index: int): 
        '''
        connectTarget(self, targetPath: MDagPath,
                        index: int)

        Synopsis
        -----
        This method is called to make connections between the constraint
        and the target. Since the default behaviour is to do nothing it
        is generally necessary to override this method if your constraint
        is to work properly. The connectTargetAttribute() convenience
        method can be useful in this regard.Default behaviour makes no
        connections.

        Returns:
        -----
        None

        Parameters:
        -----
        targetPath: MDagPath
        	[in] -> DAG path of the target 

        index: int
        	[in] -> index for this target in the node's constraint target attribute


        '''
        pass

    def connectObjectAndConstraint(self, modifier: MDGModifier): 
        '''
        connectObjectAndConstraint(self, modifier: MDGModifier)

        Synopsis
        -----
        This method is used for connecting the constraint and constrained
        object. The utility method
        MPxConstraintCommand::connectObjectAttribute() is used to connect
        the attributes.Default behaviour returns MS::kUnknownParameter so
        that Maya handles the operation.

        Returns:
        -----
        None

        Parameters:
        -----
        modifier: MDGModifier
        	[in] -> DG modifier used to undo and redo the command


        '''
        pass

    def setRestPosition(self, modifier: MDGModifier): 
        '''
        setRestPosition(self, modifier: MDGModifier)

        Synopsis
        -----
        Override this method if you want to control the value to which
        the constraint node's rest position attribute (i.e. the one
        returned by constraintRestAttribute()) and its corresponding
        enable attribute (i.e. the one returned by
        constraintEnableRestAttribute()) are initialized or if
        constraintRestAttribute() or constraintOutputAttribute() return
        attributes which are not of type MFnNumericData::k3Double.The
        default behaviour is to initialize the rest position to the
        computed value of the output attribute (i.e. the one returned by
        constraintOutputAttribute()) and to initialize the enable
        attribute to true.This method is called as part of the default
        doIt() handling, after the constrained object and all the targets
        have been connected and weights have been set. If you have
        overridden doIt() and it does not return MS::kUnknownParameter
        then this method will not be called.

        Returns:
        -----
        None

        Parameters:
        -----
        modifier: MDGModifier
        	[in] -> DG modifier used to undo and redo the command. During the initial execution of the command (i.e. 


        '''
        pass

    def connectGeometryAttribute(self, opaqueTarget: void,
                        index: int,
                        constraintAttribute: MObject): 
        '''
        connectGeometryAttribute(self, opaqueTarget: void,
                        index: int,
                        constraintAttribute: MObject)

        Synopsis
        -----
        Utility method to make any required connections for the
        constraint. Note that it is called by the default implementation
        of connectTarget().

        Returns:
        -----
        None

        Parameters:
        -----
        opaqueTarget: void
        	[in] -> as passed to 

        index: int
        	[in] -> as passed to 

        constraintAttribute: MObject
        	[in] -> as defined by the constraint


        '''
        pass

    def connectTargetAttribute(self, targetPath: MDagPath,
                        index: int,
                        targetAttribute: MObject,
                        constraintAttr: MObject,
                        instanced: bool): 
        '''
        connectTargetAttribute(self, targetPath: MDagPath,
                        index: int,
                        targetAttribute: MObject,
                        constraintAttr: MObject,
                        instanced: bool)

        Synopsis
        -----
        Utility method to make any required connections for the
        constraint.

        Returns:
        -----
        None

        Parameters:
        -----
        targetPath: MDagPath
        	[in] -> as passed to 

        index: int
        	[in] -> as passed to 

        targetAttribute: MObject
        	[in] -> as defined by the target 

        constraintAttr: MObject
        	[in] -> as defined by the constraint 

        instanced: bool
        	[in] -> true if 


        '''
        pass

    def connectObjectAttribute(self, objectAttr: MObject,
                        constraintAttr: MObject,
                        toConstraint: bool,
                        instanced: bool): 
        '''
        connectObjectAttribute(self, objectAttr: MObject,
                        constraintAttr: MObject,
                        toConstraint: bool,
                        instanced: bool)

        Synopsis
        -----
        This method can be used by connectObjectAndConstraint() to make
        any required connections between the constraint and the
        constrained object.

        Returns:
        -----
        None

        Parameters:
        -----
        objectAttr: MObject
        	[in] -> as passed to 

        constraintAttr: MObject
        	[in] -> as defined by the constraint 

        toConstraint: bool
        	[in] -> true if connection is from object to constraint, false if connection is from constraint to object 

        instanced: bool
        	[in] -> true if 


        '''
        pass

    def transformObject(self): 
        '''
        transformObject(self) -> const MObject

        Synopsis
        -----
        This method returns the target object being constrained. The
        object returned will be a "transform" node. This node can be
        queried using MFnTransform to extract information such as
        translate, scale etc which will allow the placement of the
        constrained object in a reasonable default location. For example,
        a geometric constraint may wish to place the constrained object
        on top of the target.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class TargetType:
    '''Defines the type of target object. 
    Non-functional class.  Values for this enum:
    kTransform
    kGeometryShape
    kLast
    '''

    def __init__(self):
        pass

    def kTransform(self):
        '''This is an enum of TargetType.
        - Description: Transform target. 
        - Value: 0
        '''
        pass

    def kGeometryShape(self):
        '''This is an enum of TargetType.
        - Description: Geometry shape(or children of) targets. 
        - Value: 1
        '''
        pass

    def kLast(self):
        '''This is an enum of TargetType.
        - Description: Last value, used for counting. 
        - Value: 2
        '''
        pass

class MPxContext:
    '''Base class for user defined contexts.
This is the base class for user defined contexts.
Contexts provide a way to create interactive tools in Maya. A
context class defines what happens when interactive events, such
as mouse events, occur within an interactive panel in Maya.
Since there are default actions for all tools in Maya, such as
the right mouse button event which brings up an options menu,
only as subset of the events that occur in a view can be
overridden. The events that can be overridden are:
A context is
 by pressing the toolButton for that context. Once the context is
activated, it will handle the events that occur within 3d panel.
A context is
 when some other tool button is pressed.
There can be more than one instance of a context in Maya, for
example, dragging a tool icon into the shelf creates another
instance of that context. Since there can be multiple instances
of the same context there is a command class,
, which is responsible for the creation of contexts. See
 for more information.
'''
    def __init__(self):
        pass


    def toolOnSetup(self, event: MEvent): 
        '''
        toolOnSetup(self, event: MEvent)

        Synopsis
        -----
        This method is called when the context is activated, i.e when the
        toolButton for the context is pressed. Users can override this
        method and use it to set up any user defined data that needs to
        be initialized on each activation.Reimplemented in
        MTemplateSelectionContext< ContextNameString, ContextClass,
        NodeType, ManipulatorClass, ManipulatorNodeName >.

        Returns:
        -----
        None

        Parameters:
        -----
        event: MEvent
        	[in] -> The button press event information. 


        '''
        pass

    def toolOffCleanup(self): 
        '''
        toolOffCleanup(self)

        Synopsis
        -----
        This method is called when the context is deactivated, i.e when
        another context is activated. Users can override this method and
        use it to reset any user defined data to a specific state.
        Reimplemented in MTemplateSelectionContext< ContextNameString,
        ContextClass, NodeType, ManipulatorClass, ManipulatorNodeName >.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def doPress(self, event: MEvent): 
        '''
        doPress(self, event: MEvent)

        Synopsis
        -----
        This method is called when any mouse button is pressed. The base
        method does nothing and should be overridden if the user needs to
        do anything on a button press.This method is called only when it
        is in either default viewport renderer or hardware viewport
        renderer, not viewport 2.0.The event can be used to get more
        explicit information about the press such as the button number.
        See MEvent for more information.Reimplemented in
        MPxSelectionContext.

        Returns:
        -----
        None

        Parameters:
        -----
        event: MEvent
        	[in] -> The button press event information.


        '''
        pass

    def doRelease(self, event: MEvent): 
        '''
        doRelease(self, event: MEvent)

        Synopsis
        -----
        This method is called when any mouse button is released. The base
        method does nothing and should be overridden if the user needs to
        do anything on a button release.This method is called only when
        it is in either default viewport renderer or hardware viewport
        renderer, not viewport 2.0.The event can be used to get more
        explicit information about the release such as the button number.
        See MEvent for more information.Reimplemented in
        MPxSelectionContext.

        Returns:
        -----
        None

        Parameters:
        -----
        event: MEvent
        	[in] -> The mouse button release information.


        '''
        pass

    def doDrag(self, event: MEvent): 
        '''
        doDrag(self, event: MEvent)

        Synopsis
        -----
        This method is called when a mouse drag event occurs. The base
        method does nothing and should be overridden if the user needs to
        do anything during a mouse drag.This method is called only when
        it is in either default viewport renderer or hardware viewport
        renderer, not viewport 2.0.The event can be used to get more
        explicit information about the drag such as the cursor location.
        See MEvent for more information.Reimplemented in
        MPxSelectionContext.

        Returns:
        -----
        None

        Parameters:
        -----
        event: MEvent
        	[in] -> The mouse drag event information.


        '''
        pass

    def doPtrMoved(self, event: MEvent): 
        '''
        doPtrMoved(self, event: MEvent)

        Synopsis
        -----
        This method is called when a mouse move event occurs. The base
        method does nothing and should be overridden if the user needs to
        do anything during a mouse drag.This method is called only when
        it is in either default viewport renderer or hardware viewport
        renderer, not viewport 2.0.The event can be used to get more
        explicit information about the drag such as the cursor location.
        See MEvent for more information.

        Returns:
        -----
        None

        Parameters:
        -----
        event: MEvent
        	[in] -> The mouse drag event information.


        '''
        pass

    def doEnterRegion(self, event: MEvent): 
        '''
        doEnterRegion(self, event: MEvent)

        Synopsis
        -----
        This method is called when the mouse pointer enters a screen
        panel region. The base method sets the help string and the cursor
        which may have been set via setHelpString and setCursor
        respectively.This same method is called for default viewport
        renderer regions, hardware viewport renderer regions, and
        viewport 2.0 regions. There is not a separate method for VP 2.0
        regions as there is with MPxContext::doPress(),
        MPxContext::doHold(), and MPxContext::doRelease().The event can
        be used to get more explicit information about the event. See
        MEvent for more information.

        Returns:
        -----
        None

        Parameters:
        -----
        event: MEvent
        	[in] -> The enter region event information.


        '''
        pass

    def helpStateHasChanged(self, event: MEvent): 
        '''
        helpStateHasChanged(self, event: MEvent)

        Synopsis
        -----
        This method is called whenever the help state may need to be
        updated. The base method does nothing and should be overriden if
        the user needs to change the help information based on events.The
        event can be used to get more explicit information about the
        event. See MEvent for more information.Reimplemented in
        MPxSelectionContext.

        Returns:
        -----
        None

        Parameters:
        -----
        event: MEvent
        	[in] -> The event information.


        '''
        pass

    def deleteAction(self): 
        '''
        deleteAction(self)

        Synopsis
        -----
        This method is called when the delete or backspace key is
        pressed. The default behaviour for this method is to delete the
        items on the current selection list. Users can override this
        method if they wish to do anything else when this event occurs.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def completeAction(self): 
        '''
        completeAction(self)

        Synopsis
        -----
        This method is called when the complete key is pressed. The
        default complete key in Maya is the enter key. Users can override
        this method if a tool has several steps. For example, a tool may
        have several steps where the user must select objects and then
        press the completion key before proceeding.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def addManipulator(self, manipulator: MObject): 
        '''
        addManipulator(self, manipulator: MObject)

        Synopsis
        -----
        This method adds a manipulator to the context. Reimplemented in
        MPxSelectionContext.

        Returns:
        -----
        None

        Parameters:
        -----
        manipulator: MObject
        	[in] -> the manipulator to be added to the context


        '''
        pass

    def deleteManipulators(self): 
        '''
        deleteManipulators(self)

        Synopsis
        -----
        This method deletes all the manipulators that belong to the
        context. Reimplemented in MPxSelectionContext.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setImage(self, image: MString,
                        index: MPxContext.ImageIndex): 
        '''
        setImage(self, image: MString,
                        index: MPxContext.ImageIndex)

        Synopsis
        -----
        This method is used to set an XPM icon image that is to be used
        to represent this tool context in various places including the
        tool bar and can be queried from mel using the contextInfo
        command.

        Returns:
        -----
        None

        Parameters:
        -----
        image: MString
        	[in] -> the name of an XPM file to be used as the icon 

        index: MPxContext.ImageIndex
        	[in] -> the index of the image being set; three image representations are permitted: kImage1, kImage2, kImage3


        '''
        pass

    def image(self, index: MPxContext.ImageIndex,
                        ReturnStatus: MPxContext.MStatus): 
        '''
        image(self, index: MPxContext.ImageIndex,
                        ReturnStatus: MPxContext.MStatus) -> MString

        Synopsis
        -----
        This method is used to retrieve an XPM icon image that has
        previously been set for this tool context. This icon image will
        be used to represent this tool context in various places
        including the tool bar and can be queried from mel using the
        contextInfo command.

        Returns: 
        ----- 
        String name

        Parameters:
        -----
        index: MPxContext.ImageIndex
        	[in] -> the index for the image being retrieved; three image representations are permitted: kImage1, kImage2, kImage3 

        ReturnStatus: MPxContext.MStatus
        	[out] -> Status code (see below)


        '''
        pass

    def inAlternateContext(self): 
        '''
        inAlternateContext(self) -> bool

        Synopsis
        -----
        Introduced in 2024.0 This method is used to indicate if an
        alternate context is active.For example, this method returns true
        if the user moves the camera while the current context is active.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def _dragMarquee(self, event: MEvent): 
        '''
        _dragMarquee(self, event: MEvent)

        Synopsis
        -----
        Introduced in 2020.0

        Returns:
        -----
        None

        Parameters:
        -----
        event: MEvent
        	[in] -> 


        '''
        pass

    def setHelpString(self, str: MString): 
        '''
        setHelpString(self, str: MString)

        Synopsis
        -----
        USE _setHelpString() IN SCRIPT. Set the help string to the given
        MString.This string will appear in the help line in Maya.

        Returns:
        -----
        None

        Parameters:
        -----
        str: MString
        	[in] -> The new help string.


        '''
        pass

    def setTitleString(self, str: MString): 
        '''
        setTitleString(self, str: MString)

        Synopsis
        -----
        USE _setTitleString() IN SCRIPT. Set the title of the context to
        the MString that is passed in.This string will appear in the help
        line when this context is activated.

        Returns:
        -----
        None

        Parameters:
        -----
        str: MString
        	[in] -> The new title string.


        '''
        pass

    def setCursor(self, newCursor: MCursor): 
        '''
        setCursor(self, newCursor: MCursor)

        Synopsis
        -----
        USE _setCursor() IN SCRIPT. Set the cursor used by the context to
        the MCursor that is passed in.

        Returns:
        -----
        None

        Parameters:
        -----
        newCursor: MCursor
        	[in] -> The new cursor.


        '''
        pass

    def beginMarquee(self, event: MEvent): 
        '''
        beginMarquee(self, event: MEvent)

        Synopsis
        -----
        USE _beginMarquee() IN SCRIPT. Start drawing a dragged out
        marquee box.A marquee box is a rectangular area of the screen
        specified by two points representing opposite corners of the
        rectangle. Marquee's are commonly used in the selection of
        multiple items from a region of the screen. The marquee rectangle
        acts as a guideline for the region of the screen that will be
        effected.

        Returns:
        -----
        None

        Parameters:
        -----
        event: MEvent
        	[in] -> Current event information.


        '''
        pass

    def dragMarquee(self, event: MEvent): 
        '''
        dragMarquee(self, event: MEvent)

        Synopsis
        -----
        USE _dragMarquee() IN SCRIPT. Draws a rectangle representing the
        dragged out area initiated with the beginMarquee method.

        Returns:
        -----
        None

        Parameters:
        -----
        event: MEvent
        	[in] -> Current event information.


        '''
        pass

    def releaseMarquee(self, event: MEvent,
                        top: short,
                        left: short,
                        bottom: short,
                        right: short): 
        '''
        releaseMarquee(self, event: MEvent,
                        top: short,
                        left: short,
                        bottom: short,
                        right: short)

        Synopsis
        -----
        USE _releaseMarquee() IN SCRIPT. End the marquee drawing cycle
        and return the coordinates corresponding to the dragged out
        area.The rectangular guideline representing the dragged area is
        cleared.

        Returns:
        -----
        None

        Parameters:
        -----
        event: MEvent
        	[in] -> Current event information. 

        top: short
        	[out] -> highest value 

        left: short
        	[out] -> left-most value 

        bottom: short
        	[out] -> lowest value 

        right: short
        	[out] -> right-most value


        '''
        pass

    def abortAction(self): 
        '''
        abortAction(self)

        Synopsis
        -----
        This method is called when the abort key is pressed. The default
        abort key in Maya is the escape key. Users can override this
        method if they wish to perform certain operations when the abort
        key is pressed. Reimplemented in MPxSelectionContext.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def processNumericalInput(self, values: MDoubleArray,
                        flags: MIntArray,
                        isAbsolute: bool): 
        '''
        processNumericalInput(self, values: MDoubleArray,
                        flags: MIntArray,
                        isAbsolute: bool) -> bool

        Synopsis
        -----
        This method processes the input from the numerical input field.
        Users can override this method if they wish to process numerical
        input. For a given entry in the numeric input field, if the user
        types a dot ".", this indicates that the entry should not be
        modified. The overridden version of this method should take this
        into account using the ignoreEntry method with the flags that are
        passed in. The overridden version of this method should also
        process the numeric input as an absolute input or relative input
        depending on whether the isAbsolute flag is true or not. The
        return value should indicate whether or not the numerical input
        has been processed.Reimplemented in MPxSelectionContext.

        Returns: 
        ----- 
        false the default return value

        Parameters:
        -----
        values: MDoubleArray
        	[in] -> the values from the numerical input field 

        flags: MIntArray
        	[in] -> used in conjunction with the ignoreEntry method, determines whether or not a given entry should be ignored 

        isAbsolute: bool
        	[in] -> whether or not the input should be interpreted as absolute


        '''
        pass

    def feedbackNumericalInput(self): 
        '''
        feedbackNumericalInput(self) -> bool

        Synopsis
        -----
        This method is called to update the numerical feedback. The
        format and values for the feedback line can be set through the
        methods in MFeedbackLine, specifically setFormat and setValue.
        The return value should indicate whether or not the numerical
        feedback has been provided.Reimplemented in MPxSelectionContext.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def argTypeNumericalInput(self, index: int): 
        '''
        argTypeNumericalInput(self, index: int) -> MSyntax.MSyntax

        Synopsis
        -----
        This method is used by the feedback line to determine what units
        to display. Users should override this method to return the
        appropriate argument type for the given index of the numeric
        input field. Specifically, this method should be overridden to
        return one of the following:Reimplemented in MPxSelectionContext.

        Returns: 
        ----- 
        MSyntax::kNoArg the default return value

        Parameters:
        -----
        index: int
        	[in] -> the index of the numerical input whose argument type is requested


        '''
        pass

    def stringClassName(self): 
        '''
        stringClassName(self) -> MString

        Synopsis
        -----
        This method is called to determine the name that uniquely
        identifies the context. Either this method, or the getClassName
        method, should be overridden such that the name is set to the
        appropriate string. For example: This name is used by Maya to
        call the appropriate tool property sheet MEL scripts,
        specifically:If this method is not overriden, by default it will
        set the string to "defaultTool".

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

    def ignoreEntry(self, flags: MIntArray,
                        entry: int): 
        '''
        ignoreEntry(self, flags: MIntArray,
                        entry: int) -> bool

        Synopsis
        -----
        USE _ignoreEntry() IN SCRIPT. This is a helper method which can
        be called from processNumericalInput to examine a flags array and
        return true if the requested (0-based) entry is to be ignored.

        Returns: 
        ----- 
        true the given entry should be ignored  false the given entry
        should not be ignored

        Parameters:
        -----
        flags: MIntArray
        	[in] -> used in conjunction with the processNumericalInput method, determines whether or not a given entry should be ignored. 

        entry: int
        	[in] -> the entry specified by a (0-based) index


        '''
        pass

    def doExitRegion(self, event: MEvent): 
        '''
        doExitRegion(self, event: MEvent)

        Synopsis
        -----
        Introduced in 2024.0 This method is called when the mouse exits
        the viewport.This is a virtual method that must be overridden if
        any action needs to be taken when the mouse exits the viewport.

        Returns:
        -----
        None

        Parameters:
        -----
        event: MEvent
        	[in] -> The exit region event information.


        '''
        pass

class ImageIndex:
    '''Used to select between the three possible images associated with the context. 
    Non-functional class.  Values for this enum:
    kImage1
    kImage2
    kImage3
    '''

    def __init__(self):
        pass

    def kImage1(self):
        '''This is an enum of ImageIndex.
        - Description:  
        - Value: 0
        '''
        pass

    def kImage2(self):
        '''This is an enum of ImageIndex.
        - Description:  
        - Value: 1
        '''
        pass

    def kImage3(self):
        '''This is an enum of ImageIndex.
        - Description:  
        - Value: 2
        '''
        pass

class MPxContextCommand:
    '''Base class for context creation commands.
This is the base class for context creation commands.
The purpose of this command class is to create instances of user
contexts derived from
, and to allow the MEL programmer to edit and query various
properties of the context related to this command.
The user will derive off of this class and override the
 method which will be called when this command is invoked in
Maya.
The context command is registered in Maya using
MFnPlugin::registerContextCommand'''
    def __init__(self):
        pass


    def doEditFlags(self): 
        '''
        doEditFlags(self)

        Synopsis
        -----
        This method is called when the command is called in edit mode.
        This method should be overridden by context commands to determine
        which edit flags are set in conjunction with the argument parser
        for this command. The argument parser for this command can be
        obtained by calling the parser method. If the command is called
        with both the edit flag and the query flag, then the query flag
        will be ignored.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def doQueryFlags(self): 
        '''
        doQueryFlags(self)

        Synopsis
        -----
        This method is called when the command is called in query mode.
        This method should be overridden by context commands to determine
        which query flags are set in conjunction with the argument parser
        for this command. The argument parser for this command can be
        obtained by calling the parser method. If the command is called
        with both the edit flag and the query flag, then the query flag
        will be ignored.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def appendSyntax(self): 
        '''
        appendSyntax(self)

        Synopsis
        -----
        This method should be overridden to append syntax to the context
        command. The syntax object can be obtained by calling the syntax
        method. The following flags cannot be used as user-defined flags
        as they are reserved for edit and query: "-e", "-edit", "-q",
        "-query".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def setResult(self, result: bool): 
        '''
        setResult(self, result: bool)

        Synopsis
        -----
        This method should be called when the result of the context
        command is a boolean.

        Returns:
        -----
        None

        Parameters:
        -----
        result: bool
        	[out] -> the boolean result


        '''
        pass

    @overload
    def setResult(self, result: int): 
        '''
        setResult(self, result: int)

        Synopsis
        -----
        This method should be called when the result of the context
        command is an integer.

        Returns:
        -----
        None

        Parameters:
        -----
        result: int
        	[out] -> the integer result


        '''
        pass

    @overload
    def setResult(self, result: double): 
        '''
        setResult(self, result: double)

        Synopsis
        -----
        This method should be called when the result of the context
        command is a double.

        Returns:
        -----
        None

        Parameters:
        -----
        result: double
        	[out] -> the double result


        '''
        pass

    @overload
    def setResult(self, result: MString): 
        '''
        setResult(self, result: MString)

        Synopsis
        -----
        This method should be called when the result of the context
        command a string.

        Returns:
        -----
        None

        Parameters:
        -----
        result: MString
        	[out] -> the string result


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

    def syntax(self, ReturnStatus: MPxContextCommand.MStatus): 
        '''
        syntax(self, ReturnStatus: MPxContextCommand.MStatus) -> MSyntax

        Synopsis
        -----
        USE _syntax() IN SCRIPT. This method returns the syntax object of
        this context command.From an overridden version of the
        appendSyntax method you may append to the syntax object.

        Returns: 
        ----- 
        The syntax object

        Parameters:
        -----
        ReturnStatus: MPxContextCommand.MStatus
        	[out] -> return status


        '''
        pass

    def parser(self, ReturnStatus: MPxContextCommand.MStatus): 
        '''
        parser(self, ReturnStatus: MPxContextCommand.MStatus) -> MArgParser

        Synopsis
        -----
        USE _parser() IN SCRIPT. This method returns the argument parser
        of this context command.The argument parser can be used in the
        overridden versions of doEditFlags and doQueryFlags to determine
        which flags are set.

        Returns: 
        ----- 
        The argument parser

        Parameters:
        -----
        ReturnStatus: MPxContextCommand.MStatus
        	[out] -> return status


        '''
        pass

class MPxControlCommand:
    '''Base class for control creation commands.
MPxControlCommand is the base class for user defined UI control commands. This
command gives all of the flags and options of the base control
command in addition to any user defined flags or behaviours. When
registering this command, use the
MFnPlugin::registerControlCommand() method. All control commands have a corresponding
MPxUIControl. It is important to note that a given
MPxControlCommand is reponsible for only ONE
MPxUIControl.
'''
    def __init__(self):
        pass


    def doEditFlags(self): 
        '''
        doEditFlags(self)

        Synopsis
        -----
        This method is called when the command is called in edit mode.
        This method should be overridden by control commands to determine
        which edit flags are set in conjunction with the argument parser
        for this command. The argument parser for this command can be
        obtained by calling the parser method.If the command is called
        with both the edit flag and the query flag, then the query flag
        will be ignored.If the command returns MS::kUnknownParameter, the
        flag is processed by the parent class.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def doQueryFlags(self): 
        '''
        doQueryFlags(self)

        Synopsis
        -----
        This method is invoked during query mode, and the default method
        should be overridden in user-defined control commands to
        determine which query flags are set in conjunction with the
        argument parser for the command. The argument parser for this
        command can be obtained by calling the parser method. If the
        command is called with both the edit flag and the query flag,
        then the query flag will be ignored.If the command returns
        MS::kUnknownParameter, the flag is processed by the parent class.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def appendSyntax(self): 
        '''
        appendSyntax(self)

        Synopsis
        -----
        This method should be overridden to append syntax to the control
        command. The syntax object can be obtained by calling the syntax
        method. The following flags cannot be used as user-defined flags
        as they are reserved for edit and query: "-e", "-edit", "-q",
        "-query".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def skipFlagForCreate(self, longFlag: MString): 
        '''
        skipFlagForCreate(self, longFlag: MString) -> bool

        Synopsis
        -----
        Returns true if the passed long flag name should be skipped
        during the creation portion of the command.

        Returns: 
        ----- 
        true if the flag shoiuld be skipped during creation.

        Parameters:
        -----
        longFlag: MString
        	[in] -> The string containing the long flag name.


        '''
        pass

    @overload
    def setResult(self, result: bool): 
        '''
        setResult(self, result: bool)

        Synopsis
        -----
        This method should be called when the result of the control
        command is a boolean.

        Returns:
        -----
        None

        Parameters:
        -----
        result: bool
        	[out] -> the boolean result


        '''
        pass

    @overload
    def setResult(self, result: int): 
        '''
        setResult(self, result: int)

        Synopsis
        -----
        This method should be called when the result of the control
        command is an integer.

        Returns:
        -----
        None

        Parameters:
        -----
        result: int
        	[out] -> the integer result


        '''
        pass

    @overload
    def setResult(self, result: double): 
        '''
        setResult(self, result: double)

        Synopsis
        -----
        This method should be called when the result of the control
        command is a double.

        Returns:
        -----
        None

        Parameters:
        -----
        result: double
        	[out] -> the double result


        '''
        pass

    @overload
    def setResult(self, result: MString): 
        '''
        setResult(self, result: MString)

        Synopsis
        -----
        This method should be called when the result of the control
        command is a string.

        Returns:
        -----
        None

        Parameters:
        -----
        result: MString
        	[out] -> the string result


        '''
        pass

    @overload
    def setResult(self, result: MStringArray): 
        '''
        setResult(self, result: MStringArray)

        Synopsis
        -----
        This method should be called when the result of the control
        command is a string array.

        Returns:
        -----
        None

        Parameters:
        -----
        result: MStringArray
        	[out] -> the string result


        '''
        pass

    @overload
    def setResult(self, result: MIntArray): 
        '''
        setResult(self, result: MIntArray)

        Synopsis
        -----
        This method should be called when the result of the control
        command is a integer array.

        Returns:
        -----
        None

        Parameters:
        -----
        result: MIntArray
        	[out] -> the integer array result


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

    def syntax(self, ReturnStatus: MPxControlCommand.MStatus): 
        '''
        syntax(self, ReturnStatus: MPxControlCommand.MStatus) -> MSyntax

        Synopsis
        -----
        USE _syntax() IN SCRIPT. This method returns the syntax object of
        this control command.The syntax object can be appended to in an
        overridden version of the appendSyntax method.

        Returns: 
        ----- 
        the syntax object

        Parameters:
        -----
        ReturnStatus: MPxControlCommand.MStatus
        	[out] -> return status


        '''
        pass

    def parser(self, ReturnStatus: MPxControlCommand.MStatus): 
        '''
        parser(self, ReturnStatus: MPxControlCommand.MStatus) -> MArgParser

        Synopsis
        -----
        USE _parser() IN SCRIPT. This method returns the argument parser
        of this control command.The argument parser can be used in the
        overridden versions of doEditFlags and doQueryFlags to determine
        which flags are set.

        Returns: 
        ----- 
        The argument parser

        Parameters:
        -----
        ReturnStatus: MPxControlCommand.MStatus
        	[out] -> return status


        '''
        pass

class MPxData:
    '''Base Class for User-defined Dependency Graph Data Types.
In Maya, both intrinsic and user-defined Maya Objects are
registered and recognized by their type identifier (
MTypeId). Data which flows in the Dependency Graph (DG) is implemented
as Maya objects, therefore, the type characteristics of DG Data
are specified by the type id (
MTypeId). The type id is used to at run-time to determine how to create
and destroy Maya Objects, and how they are to be input/output
from/to files.
User-defined Data has two parts. One part is an internal Maya
Data object of neutral type which is common to all user-defined
types. This common Data object implements the interface and
behaviour characteristics required for user-defined Data to act
as Data within Maya. The second part is unique to each user-
defined type and implements the type-specific behaviour.
The Proxy Data (
MPxData) class is the base class for user-defined Data types. All user-
defined Data that is to be passed between Nodes in the DG must be
derived from
MPxData.
MPxData transparently incorporates the common behaviour and defines the
common interface required for DG Data. When initialized with a
unique type id, Data objects of classes derived from
MPxData are recognized by Maya the same as built-in DG Data types, but
are be able to implement user-specified behaviour.
The
MPxData class defines the interface for methods to read, write and
assign Data objects of the the user-defined type. User-defined
types must override these methods to provide type-specific
behaviour.
MPxData also provides common methods for querying the type id and type
name of the Data object.
All user-defined DG Data types require an associated static
creator function that returns a void pointer to a new instance of
the data class. This function is usually a static function within
the user defined data type class.
The registration of the new data type is performed by the
MFnPlugin::registerData() which is invoked in the initializePlugin() function during Plug-
in loading. One of the most important thing that the registration
does is it associates the type id with the data.
Once a user-defined Data type based on
MPxData has been defined and registered, use the Typed Attribute
Function Set (
MFnTypedAttribute) to create an Attribute of the user-defined type. The Attribute
may also be an multi-Attribute (array). Use the DG Node Function
Set (
MFnDependencyNode) to add the Attribute to a user- defined Node. This is usually
done in the initialize() method of the Node creator.
Data of a user-defined type on a Node is accessed in the same way
as intrinsic Data types. The Data is actually held in an Data
Block (
MDataBlock). Use a Data Handle (
MDataHandle) or Array Data Handle (
MArrayDataHandle) to access the Data within a Data Block. Use a Data Block to
obtain a Data Handle or Array Data Handle for either an Attribute
or the associated Plug on the Attribute. The Data Handle or Array
data handle can then be queried for the underlying Data object.
The underlying Data object is a generic Maya Object (
MObject) with a type id of the user-defined type.
Use the Plug-in Data Function Set (
MFnPluginData) to obtain an
MPxData pointer which can be safely cast to a pointer of the user-
defined type.
'''
    def __init__(self):
        pass


    def readASCII(self, argList: MArgList,
                        endOfTheLastParsedElement: int): 
        '''
        readASCII(self, argList: MArgList,
                        endOfTheLastParsedElement: int)

        Synopsis
        -----
        Creates Data in Data Block as specified by input from ASCII file
        record.

        Returns:
        -----
        None

        Parameters:
        -----
        argList: MArgList
        	[in] -> 

        endOfTheLastParsedElement: int
        	[in] -> 


        '''
        pass

    def readBinary(self, inarg: std.std,
                        length: int): 
        '''
        readBinary(self, inarg: std.std,
                        length: int)

        Synopsis
        -----
        Creates Data in Data Block as specified by binary data from the
        given stream.

        Returns:
        -----
        None

        Parameters:
        -----
        inarg: std.std
        	[in] -> 

        length: int
        	[in] -> 


        '''
        pass

    def writeASCII(self, outarg: std.std): 
        '''
        writeASCII(self, outarg: std.std)

        Synopsis
        -----
        Encodes Data in accordance with the ASCII file format and outputs
        it to the given stream.

        Returns:
        -----
        None

        Parameters:
        -----
        outarg: std.std
        	[in] -> 


        '''
        pass

    def writeBinary(self, outarg: std.std): 
        '''
        writeBinary(self, outarg: std.std)

        Synopsis
        -----
        Encodes Data in accordance with the binary file format and
        outputs it to the given stream.

        Returns:
        -----
        None

        Parameters:
        -----
        outarg: std.std
        	[in] -> 


        '''
        pass

    def copy(self, src: MPxData): 
        '''
        copy(self, src: MPxData)

        Synopsis
        -----
        This method initializes an instance of an MPxData derived class
        from another existing instance. This method can be thought of as
        the second half of a copy constructor for the class. The default
        constructor has already been called for the instance, and this
        method is used to set the private data by copying the values from
        an existing instance. This is a pure virtual method, and must be
        overridden in derived classes.Implemented in MPxGeometryData.

        Returns:
        -----
        None

        Parameters:
        -----
        src: MPxData
        	[in] -> The object from which to copy the private data 


        '''
        pass

    def typeId(self): 
        '''
        typeId(self) -> MTypeId

        Synopsis
        -----
        Determines the type id of the Data object. This is a pure virtual
        method, and must be overridden in derived classes.Implemented in
        MPxGeometryData.

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
        Determines the type name of the Data object. This is a pure
        virtual method, and must be overridden in derived
        classes.Implemented in MPxGeometryData.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class Type:
    '''Type of the data. 
    Non-functional class.  Values for this enum:
    kData
    kGeometryData
    kLast
    '''

    def __init__(self):
        pass

    def kData(self):
        '''This is an enum of Type.
        - Description:  
        - Value: 0
        '''
        pass

    def kGeometryData(self):
        '''This is an enum of Type.
        - Description:  
        - Value: 1
        '''
        pass

    def kLast(self):
        '''This is an enum of Type.
        - Description:  
        - Value: 2
        '''
        pass

class MPxDeformerNode:
    '''Base class for user defined deformers with per-vertex weights.
MPxDeformerNode builds on
MPxGeometryFilter to allow the creation of deformers with per-vertex weights.
Built-in Maya nodes which work in this way include the jiggle and
cluster deformers.
The weight values can be modified by the user using the set
editing window or the percent command.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MPxNode.MPxNode

        Synopsis
        -----
        This method returns the type of the node. This method should not
        be overridden by the user. It will return
        MPxNode::kDeformerNode.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def weightValue(self, block: MDataBlock,
                        multiIndex: int,
                        wtIndex: int): 
        '''
        weightValue(self, block: MDataBlock,
                        multiIndex: int,
                        wtIndex: int) -> float

        Synopsis
        -----
        This method returns the weightValue stored in the datablock for
        the given geometry's lattice point/CV/vertex. The weight is the
        combination of painted weights and falloff weights.

        Returns: 
        ----- 
        Weight

        Parameters:
        -----
        block: MDataBlock
        	[in] -> the datablock for the node 

        multiIndex: int
        	[in] -> the index corresponding to the geometry 

        wtIndex: int
        	[in] -> the index corresponding to the component


        '''
        pass

    def envelopeWeights(self, block: MDataBlock,
                        multiIndex: int,
                        numWeights: int): 
        '''
        envelopeWeights(self, block: MDataBlock,
                        multiIndex: int,
                        numWeights: int) -> float*

        Synopsis
        -----
        Introduced in 2024.0 This method returns the envelope weights for
        the deformer.These weights are the combination of painted weights
        and falloff weights. If NULL is returned it means all weights are
        uniformly 1.0 for all verts. The number of weights is equal to
        the number of affected verts of the indexMapper of the deformer
        which is the also the number of iterations of the
        geometryIterator.

        Returns: 
        ----- 
        Weights

        Parameters:
        -----
        block: MDataBlock
        	[in] -> the datablock for the node 

        multiIndex: int
        	[in] -> the index corresponding to the geometry 

        numWeights: int
        	[out] -> the number of weights that are returned (optional)


        '''
        pass

    def setUseExistingConnectionWhenSetEditing(self, state: bool): 
        '''
        setUseExistingConnectionWhenSetEditing(self, state: bool)

        Synopsis
        -----
        Introduced in 2019.0 This method allows the plugin node to
        request special treatment during set editing.It controls the
        connection behavior if all of a geometry's points are removed
        from the deformer set, and then points are subsequently added
        back in to the set again. By default, Maya will reconnect the
        deformer to the shape using a new input/output index. If this
        method is called in the custom deformer's postConstructor method
        and the state is set to true, the deformer will attempt to use
        the original input/output index when reconnecting to the shape.

        Returns:
        -----
        None

        Parameters:
        -----
        state: bool
        	[in] -> whether or not to use the existing connection 


        '''
        pass

    def setDeformationDetails(self, flags: int): 
        '''
        setDeformationDetails(self, flags: int)

        Synopsis
        -----
        Introduced in 2019.0 This method allows the plug-in node to
        inform the system that it intends to deform components other than
        just positions.It should typically be called in advance of any
        deformation taking place (e.g. in postConstructor()), not in the
        deform() method. If it is called from deform(), the setting will
        take effect the next time the DG causes the deformation to be
        calculated.

        Returns:
        -----
        None

        Parameters:
        -----
        flags: int
        	[in] -> Bitwise OR of flags from the DeformationDetails enum


        '''
        pass

    def getDeformationDetails(self, ReturnStatus: MPxDeformerNode.MStatus): 
        '''
        getDeformationDetails(self, ReturnStatus: MPxDeformerNode.MStatus) -> int

        Synopsis
        -----
        Introduced in 2019.0 Retrieves the value set by
        setDeformationDetails().See the documentation of that method for
        the interpretation of the value.

        Returns: 
        ----- 
        The deformation details

        Parameters:
        -----
        ReturnStatus: MPxDeformerNode.MStatus
        	[out] -> Status code.


        '''
        pass

    def indexMapper(self, multiIndex: int,
                        ReturnStatus: MPxDeformerNode.MStatus): 
        '''
        indexMapper(self, multiIndex: int,
                        ReturnStatus: MPxDeformerNode.MStatus) -> const MIndexMapper&

        Synopsis
        -----
        Introduced in 2024.0 This method returns the indexMapper of the
        deformer.The indexMapper defines the subset on which the deformer
        operates. Reimplemented from MPxGeometryFilter.

        Returns: 
        ----- 
        the index mapper

        Parameters:
        -----
        multiIndex: int
        	[in] -> the index corresponding to the geometry 

        ReturnStatus: MPxDeformerNode.MStatus
        	[out] -> Status code.


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

class MPxDragAndDropBehavior:
    '''Drag and Drop Behavior.
This is the base class for user defined drag and drop behaviors.
This class allows a plugin to override the behavior of drag and
drop connections from nodes in the hyperGraph/hyperShade to other
nodes or other UI. These behaviors are defined by the type of
relationship that is trying to be resolved. These are
connectAttrToAttr(),
connectAttrToNode(),
connectNodeToAttr(),
connectNodeToNode(). In order for the overridden methods to be executed the
shouldBeUsedFor() method must be overridden in order to decide which behavior to
use given the source and destination node.
'''
    def __init__(self):
        pass


    def shouldBeUsedFor(self, sourceNode: MObject,
                        destinationNode: MObject,
                        sourcePlug: MPlug,
                        destinationPlug: MPlug): 
        '''
        shouldBeUsedFor(self, sourceNode: MObject,
                        destinationNode: MObject,
                        sourcePlug: MPlug,
                        destinationPlug: MPlug) -> bool

        Synopsis
        -----
        This method must be overridden in order to use a drag and drop
        behavior. The overridden method will be called by the
        defaultNavigation command to determine wether or not to use this
        drag and drop behavior to finish a connection. If the user would
        like to handle the connection between sourceNode/Plug and
        destinationNode/Plug then this routine must pass back true,
        otherwise the routine must pass back false in order for the
        default connection mechanism to work between these two nodes.
        sourcePlug and destinationPlug may be null depending on if there
        were any attributes given in the drag and drop. Use the isNull()
        method on MPlug to assure the plugs are valid.

        Returns:
        -----
        None

        Parameters:
        -----
        sourceNode: MObject
        	[in] -> The source node of the drag and drop or the node being dragged 

        destinationNode: MObject
        	[in] -> the destination node of the drag and drop or the node being dropped upon 

        sourcePlug: MPlug
        	[in] -> The source plug of the drag and drop or the plug being dragged (this may be null) 

        destinationPlug: MPlug
        	[in] -> The destination plug of the drag and drop or the plug being dropped upon (this may be null) 


        '''
        pass

    def connectAttrToAttr(self, sourcePlug: MPlug,
                        destinationPlug: MPlug,
                        force: bool): 
        '''
        connectAttrToAttr(self, sourcePlug: MPlug,
                        destinationPlug: MPlug,
                        force: bool)

        Synopsis
        -----
        This method is called by the defaultNavigation command to connect
        a source attribute to a destination attribute. If this method is
        overidden it should attempt to determine what the user probably
        wants this connection to be, and set up the connection
        appropriately. If the force argument is true it is intended to
        notify the user to break any existing connections to the plug,
        similar to what the mel command "connectAttr" -f flag is used
        for.

        Returns:
        -----
        None

        Parameters:
        -----
        sourcePlug: MPlug
        	[in] -> Source plug in the connection 

        destinationPlug: MPlug
        	[in] -> Destination plug in the connection 

        force: bool
        	[in] -> Tells whether or not to break any existing connections to the destination attribute 


        '''
        pass

    def connectAttrToNode(self, sourcePlug: MPlug,
                        destinationNode: MObject,
                        force: bool): 
        '''
        connectAttrToNode(self, sourcePlug: MPlug,
                        destinationNode: MObject,
                        force: bool)

        Synopsis
        -----
        This method is called by the defaultNavigation command to connect
        a source attribute to a destination node.You should override this
        method if you can determine from the type of source node and
        attribute and the type of destination node what the user is
        trying to do and you know the appropriate connections that must
        be made for the end result to be what the user expects.

        Returns:
        -----
        None

        Parameters:
        -----
        sourcePlug: MPlug
        	[in] -> Source plug for the connection 

        destinationNode: MObject
        	[in] -> Destination node for the connection 

        force: bool
        	[in] -> Tells whether or not to break any existing connections to the destination node 


        '''
        pass

    def connectNodeToAttr(self, sourceNode: MObject,
                        destinationPlug: MPlug,
                        force: bool): 
        '''
        connectNodeToAttr(self, sourceNode: MObject,
                        destinationPlug: MPlug,
                        force: bool)

        Synopsis
        -----
        This method is called by the defaultNavigation command to connect
        a source node to a destination attribute. You should override
        this method if you can determine from the type of source node and
        the type of destination node and attribute what the user is
        trying to do and you know the appropriate connections that must
        be made for the end result to be what the user expects.

        Returns:
        -----
        None

        Parameters:
        -----
        sourceNode: MObject
        	[in] -> Source node for the connection 

        destinationPlug: MPlug
        	[in] -> Destination plug for the connection 

        force: bool
        	[in] -> Tells whether or not to break any existing connections to the destination attribute 


        '''
        pass

    def connectNodeToNode(self, sourceNode: MObject,
                        destinationNode: MObject,
                        force: bool): 
        '''
        connectNodeToNode(self, sourceNode: MObject,
                        destinationNode: MObject,
                        force: bool)

        Synopsis
        -----
        This method is called by the defaultNavigation command to connect
        a source node to a destination node.You should override this
        method if you can determine from the type of source node and the
        type of destination node what the user is trying to do and you
        know the appropriate connections that must be made for the end
        result to be what the user expects.

        Returns:
        -----
        None

        Parameters:
        -----
        sourceNode: MObject
        	[in] -> Source node for the connection 

        destinationNode: MObject
        	[in] -> Destination node for the connection 

        force: bool
        	[in] -> Tells whether or not to break any existing connections to the destination node 


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

class MPxEditData:
    '''Base class used to associate user-defined data with edits.
MPxEditData is a pure virtual base class, used to derive custom data objects
which can be associated with individual
MEdit objects.
A small set of comparison methods need to be defined to support
query operations and use of associative data structures. The base
class defines no other data or behavior.
Derived classes are free to add data members and methods as
required.
As a convenience, Maya implements performIsEqual and
performIsLessThan as the == and < operators, respectively. Python
implementations can then provide comparison methods __eq__ and
__lt__, as expected.
It is expected that classes derived from
MPxEditData will define one or more data members to store the object's value
and this data will be used by the virtual methods performIsEqual
and performIsLessThan for comparison.
In Python, derived class objects passed to the virtual comparison
method implementations will only be visible as
MPxEditData base class objects, not the actual derived class objects.
For this reason, Python classes derived from
MPxEditData have two additional methods,
 and
 that provide a mechanism for the derived class to access its
custom data value using the base class interface.
Since these interfaces are defined directly in Python, the data
value can be any valid Python type.
To handle the common case of having a Python string as a tag
value, similarly to
 and
, Python classes derived from
MPxEditData also have methods
 and
.
The argument to
 is expected to be a plain Python string, not a Unicode string.
The
MPxEditData object takes a copy of the argument to
, and returns a copy of its string from
.
MPxEditData objects associated with an
MEdit must be dynamically allocated. Ownership of the editData will be
assumed by Maya and subsequent management of the data object,
including its eventual deletion will be handled along with the
edit it is associated with. For this reason, an editData object
should only be associated with a single edit, the same object
should not be shared or associated with other edits. If multiple
edits have editData of the same value, each edit must have its
own unique copy.
In Python, the OpenMayaMPx asMPxPtr method is used to transfer
ownership of a dynamically allocated object to Maya. The Python
example below demonstrates how this could be implemented.
'''
    def __init__(self):
        pass


    def isEqual(self, other: MPxEditData): 
        '''
        isEqual(self, other: MPxEditData) -> bool

        Synopsis
        -----
        Compares two MPxEditData objects for equality. The base class
        method makes use of the derived class performIsEqual to determine
        the equality of two objects. Note that the base method will
        simply return false if the two MPxEditData objects are of
        different types.

        Returns: 
        ----- 
        True if both MPxEditData objects refer to the same value, false
        otherwise.

        Parameters:
        -----
        other: MPxEditData
        	[in] -> An editData object to compare with this object


        '''
        pass

    def isLessThan(self, other: MPxEditData): 
        '''
        isLessThan(self, other: MPxEditData) -> bool

        Synopsis
        -----
        Compares two MPxEditData objects to determine their relative
        order for sorting purposes. The base class method makes use of
        the derived class implementation of performIsLessThan to
        determine the ordering of two MPxEditData objects. Note that the
        base method will simply order the values by typeid if the two
        objects are not of the same type.

        Returns: 
        ----- 
        True if this object value is less than the specified MPxEditData
        object value, false otherwise.

        Parameters:
        -----
        other: MPxEditData
        	[in] -> An editData object to compare with this object


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

    def performIsEqual(self, other: MPxEditData): 
        '''
        performIsEqual(self, other: MPxEditData) -> bool

        Synopsis
        -----
        This member function must be implemented by derived classes. It
        should compare two MPxEditData objects for equality. This member
        function is meant to be called by the isEqual member function.

        Returns: 
        ----- 
        True if both MPxEditData objects refer to the same value, false
        otherwise.

        Parameters:
        -----
        other: MPxEditData
        	[in] -> An editData object to compare with this object


        '''
        pass

    def performIsLessThan(self, other: MPxEditData): 
        '''
        performIsLessThan(self, other: MPxEditData) -> bool

        Synopsis
        -----
        This member function must be implemented by derived classes. It
        should compare two MPxEditData objects to determine their
        relative order for sorting purposes. This member function is
        meant to be called by the isLessThan member function.

        Returns: 
        ----- 
        True if this object value is less than the specified MPxEditData
        object value, false otherwise.

        Parameters:
        -----
        other: MPxEditData
        	[in] -> An editData object to compare with this object


        '''
        pass

class MPxEmitterNode:
    '''Base class for user defined particle emitters.
MPxEmitterNode allows the creation and manipulation of dependency graph nodes
representing particle emitters.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MPxNode.MPxNode

        Synopsis
        -----
        This method returns the type of the node. It should not be
        overridden by the user. It will return
        MPxNode::kEmitterNode.Reimplemented from MPxNode.Reimplemented in
        MPxFluidEmitterNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def compute(self, plug: MPlug,
                        dataBlock: MDataBlock): 
        '''
        compute(self, plug: MPlug,
                        dataBlock: MDataBlock)

        Synopsis
        -----
        This method should be overridden in user defined nodes. Recompute
        the given output based on the nodes inputs. The plug represents
        the data value that needs to be recomputed, and the data block
        holds the storage for all of the node's attributes.The MDataBlock
        will provide smart handles for reading and writing this node's
        attribute values. Only these values should be used when
        performing computations.When evaluating the dependency graph,
        Maya will first call the compute method for this node. If the
        plug that is provided to the compute indicates that that the
        attribute was defined by the Maya parent node, the compute method
        should return MS::kUnknownParameter. When this occurs, Maya will
        call the internal Maya node from which the user-defined node is
        derived to compute the plug's value.This means that a user
        defined node does not need to be concerned with computing
        inherited output attributes. However, if desired, these can be
        safely recomputed by this method to change the behaviour of the
        node.Reimplemented from MPxNode.Reimplemented in
        MPxFluidEmitterNode.

        Returns:
        -----
        None

        Parameters:
        -----
        plug: MPlug
        	[in] -> plug representing the attribute that needs to be recomputed 

        dataBlock: MDataBlock
        	[out] -> data block containing storage for the node's attributes


        '''
        pass

    def draw(self, view: M3dView,
                        path: MDagPath,
                        style: M3dView.M3dView): 
        '''
        draw(self, view: M3dView,
                        path: MDagPath,
                        style: M3dView.M3dView)

        Synopsis
        -----
        Overriding this method allows the drawing of custom geometry
        using standard OpenGL calls. The OpenGL state should be left in
        the same state that it was in previously. The OpenGL routine
        glPushAttrib may be used to make this easier.When this routine is
        called, the following conditions may be assumed:As a convenience,
        this draw method will also be used by OpenGL's selection
        mechanism to determine whether this object gets selected by a
        particular mouse event. The user does not need to write a
        separate selection routine.

        Returns:
        -----
        None

        Parameters:
        -----
        view: M3dView
        	[in] -> 3D view that is being drawn into 

        path: MDagPath
        	[in] -> to this node in the DAG 

        style: M3dView.M3dView
        	[in] -> style to draw object in 


        '''
        pass

    def getEmitterType(self, block: MDataBlock): 
        '''
        getEmitterType(self, block: MDataBlock) -> MPxEmitterNode.MPxEmitterNode

        Synopsis
        -----
        Retrieves the type of the emitter, determined by the
        "emitterType" attribute value. This is intended to be called from
        within the emitter's compute() method, in order to decide how the
        emitter should behave when evaluated.

        Returns: 
        ----- 
        An MEmitterType value representing the type of emitter
        (directional, omni, surface, curve, or volume)

        Parameters:
        -----
        block: MDataBlock
        	[out] -> data block containing storage for the node's attributes


        '''
        pass

    def getOwnerShape(self): 
        '''
        getOwnerShape(self) -> MObject

        Synopsis
        -----
        If the emitter is a emitting from an object, this method returns
        the shape node for the object.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getCurrentTime(self, block: MDataBlock): 
        '''
        getCurrentTime(self, block: MDataBlock) -> MTime

        Synopsis
        -----
        Intended to be called from within the emitter's compute() method,
        this method returns the time at which the emitter is currently
        being evaluated. This is equivalent to querying the "currentTime"
        attribute on the emitter.

        Returns: 
        ----- 
        The time at which the emitter is being evaluated.

        Parameters:
        -----
        block: MDataBlock
        	[out] -> data block containing storage for the node's attributes


        '''
        pass

    def getStartTime(self, plugIndex: int,
                        block: MDataBlock): 
        '''
        getStartTime(self, plugIndex: int,
                        block: MDataBlock) -> MTime

        Synopsis
        -----
        Intended to be called from within the emitter's compute() method,
        this method returns the start times for each particle system or
        fluid into which the emitter is emitting. Each of these "targets"
        is identified by an index value corresponding to the order in
        which they are connected to the emitter. The start time value
        gives the time at which the given target is to start receiving
        particles or fluid. If the current time is less than the start
        time for a target, then nothing should be emitted into that
        target in the current evaluation. This value is taken by
        evaluating an element of the emitter node's "startTime" array
        attribute.

        Returns: 
        ----- 
        The start time for the specified target, ie the time at which the
        emitter is to start emitting into that target.

        Parameters:
        -----
        plugIndex: int
        	[in] -> identifies which emitter target's start time is to be evaluated. 

        block: MDataBlock
        	[out] -> data block containing storage for the node's attributes


        '''
        pass

    def getDeltaTime(self, plugIndex: int,
                        block: MDataBlock): 
        '''
        getDeltaTime(self, plugIndex: int,
                        block: MDataBlock) -> MTime

        Synopsis
        -----
        Intended to be called from within the emitter's compute() method,
        this method returns the width of the time interval represented by
        the current emitter evaluation. Usually emitter emission rates
        are given as rates per second, so by converting this deltaTime
        value to seconds, plugin emitters can determine how many
        particles or how much fluid to emit in the current evaluation.
        This value is taken from the emitter's "deltaTime" attribute
        value, and can vary between different emitter targets (particle
        systems or fluid shapes into which the emitter is emitting), due
        to potential differences in oversampling settings. The
        "plugIndex" parameter indicates which target's time delta is
        being evaluated.

        Returns: 
        ----- 
        The time delta for the current emitter evaluation on the
        specified target.

        Parameters:
        -----
        plugIndex: int
        	[in] -> identifies which emitter target's time delta is to be evaluated. 

        block: MDataBlock
        	[out] -> data block containing storage for the node's attributes


        '''
        pass

    def getRandomSeed(self, plugIndex: int,
                        block: MDataBlock): 
        '''
        getRandomSeed(self, plugIndex: int,
                        block: MDataBlock) -> int

        Synopsis
        -----
        Intended to be called from within the emitter's compute() method,
        this method returns the random seed for a specified emission
        target (particle system or fluid shape into which the emitter is
        emitting). This seed value is set on the target itself, and
        should be used to ensure that any randomized emission behavior is
        repeatable when animations are played back repeatedly. The
        resetRandomState() method uses this value (see its documentation
        for details on how to implement repeatable randomized behaviour
        in emitters). This value is obtained by evaluating an element of
        the emitter's "seed" array attribute.

        Returns: 
        ----- 
        The random seed value for the specified target.

        Parameters:
        -----
        plugIndex: int
        	[in] -> identifies which emitter target's random seed is to be evaluated. 

        block: MDataBlock
        	[out] -> data block containing storage for the node's attributes


        '''
        pass

    def getRandomState(self, plugIndex: int,
                        block: MDataBlock): 
        '''
        getRandomState(self, plugIndex: int,
                        block: MDataBlock)

        Synopsis
        -----
        Intended to be called from within the emitter's compute() method,
        this method copies the emitter node attribute representing the
        current random state for a particular emitter target into a local
        variable on the emitter object, to facilitate efficient random
        number generation using the randgen() method. See the
        documentation for resetRandomState() for a description of how to
        use this method in conjunction with the other random stream
        methods of this class.There is only one local random state data
        member, so care should be taken not to inadvertently overwrite
        this member by calling getRandomState() on one target before
        setRandomState() has been called on a previously-evaluated
        target.

        Returns:
        -----
        None

        Parameters:
        -----
        plugIndex: int
        	[in] -> identifies which emitter target's random state is to be copied to the local random state data member. 

        block: MDataBlock
        	[out] -> data block containing storage for the node's attributes 


        '''
        pass

    def setRandomState(self, plugIndex: int,
                        block: MDataBlock): 
        '''
        setRandomState(self, plugIndex: int,
                        block: MDataBlock)

        Synopsis
        -----
        Intended to be called from within the emitter's compute() method,
        this method copies the emitter node class random state data
        member onto the emitter node's random state attribute. See the
        documentation for resetRandomState() for a description of how to
        use this method in conjunction with the other random stream
        methods of this class.There is only one local random state data
        member, so care should be taken not to inadvertently write the
        wrong random state value to the attribute by calling
        setRandomState() on a target before getRandomState() has been
        called for that target.

        Returns:
        -----
        None

        Parameters:
        -----
        plugIndex: int
        	[in] -> identifies which emitter target's random state is to be written from the local random state data member. 

        block: MDataBlock
        	[out] -> data block containing storage for the node's attributes 


        '''
        pass

    def resetRandomState(self, plugIndex: int,
                        block: MDataBlock): 
        '''
        resetRandomState(self, plugIndex: int,
                        block: MDataBlock)

        Synopsis
        -----
        Intended to be called from within the emitter's compute() method,
        this method resets the emitter's random state data member. To
        implement repeatable randomized emitter behavior, the following
        steps should be followed:This way, the emitter gets a repeatable
        stream of random numbers that is independent of the order of
        evaluation of the various emitter targets. Persistence is
        achieved by storing the random state on emitter attributes
        between evaluations, and efficiency is achieved by using a local
        random state variable during evaluations.

        Returns:
        -----
        None

        Parameters:
        -----
        plugIndex: int
        	[in] -> identifies which emitter target's random state is to be reset. 

        block: MDataBlock
        	[out] -> data block containing storage for the node's attributes 


        '''
        pass

    def randgen(self): 
        '''
        randgen(self) -> double

        Synopsis
        -----
        Intended to be called from within the emitter's compute() method,
        this method generates a double-precision random number in the
        rand [0,1]. The emitter object's random state data member is used
        to generate the random number, and will be updated after the
        number is generated. To generate a stream of random numbers for a
        particular target, ensure that getRandomState() is called before
        calling randgen(), and that setRandomState() is called after all
        the random numbers have been generated. See the documentation for
        resetRandomState() for a description of how to use this method in
        conjunction with the other random stream methods of this class.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getRate(self, block: MDataBlock): 
        '''
        getRate(self, block: MDataBlock) -> double

        Synopsis
        -----
        Intended to be called from within the emitter's compute() method,
        this method retrieves the "rate" attribute value common to all
        particle and fluid emitters. For particle emitters, this
        indicates the number of particles to be emitted per second. For
        fluid emitters, this value is usually used as a multiplier
        applied to the emission rates for various fluid grids such as
        density, temperature, etc.

        Returns: 
        ----- 
        The emission rate for the emitter.

        Parameters:
        -----
        block: MDataBlock
        	[out] -> data block containing storage for the node's attributes


        '''
        pass

    def getMinDistance(self, block: MDataBlock): 
        '''
        getMinDistance(self, block: MDataBlock) -> double

        Synopsis
        -----
        Intended to be called from within the emitter's compute() method,
        this method retrieves the "minDistance" attribute value common to
        all particle and fluid emitters. This value indicates the minimum
        distance from the emitter center at which fluid or particles will
        be emitted.

        Returns: 
        ----- 
        The minimum emission distance for the emitter.

        Parameters:
        -----
        block: MDataBlock
        	[out] -> data block containing storage for the node's attributes


        '''
        pass

    def getMaxDistance(self, block: MDataBlock): 
        '''
        getMaxDistance(self, block: MDataBlock) -> double

        Synopsis
        -----
        Intended to be called from within the emitter's compute() method,
        this method retrieves the "maxDistance" attribute value common to
        all particle and fluid emitters. This value indicates the maximum
        distance from the emitter center at which fluid or particles will
        be emitted.

        Returns: 
        ----- 
        The maximum emission distance for the emitter.

        Parameters:
        -----
        block: MDataBlock
        	[out] -> data block containing storage for the node's attributes


        '''
        pass

    def getWorldPosition(self): 
        '''
        getWorldPosition(self) -> MPoint

        Synopsis
        -----
        Returns the worldspace coordinates of the emitter. For curve,
        surface, and volume emitters, this returns the worldspace
        coordinates of the center of the emitter's local space. For point
        emitters, this value usually corresponds to the position of the
        emitter object itself.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getWorldMatrix(self): 
        '''
        getWorldMatrix(self) -> MMatrix

        Synopsis
        -----
        Returns the matrix that maps from the emitter's local space
        coordinates to worldspace.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def volumePrimitiveBoundingBox(self, box: MBoundingBox): 
        '''
        volumePrimitiveBoundingBox(self, box: MBoundingBox) -> bool

        Synopsis
        -----
        For volume emitters, this method returns the object-space
        bounding box of the volume primitive associated with the emitter.

        Returns: 
        ----- 
        true if the emitter has an associated volume primitive, false
        otherwise.

        Parameters:
        -----
        box: MBoundingBox
        	[out] -> receives the object space bounding box for the emission volume primitive.


        '''
        pass

    def volumePrimitivePointInside(self, worldPoint: MPoint,
                        emitterWorldMatrix: MMatrix): 
        '''
        volumePrimitivePointInside(self, worldPoint: MPoint,
                        emitterWorldMatrix: MMatrix) -> bool

        Synopsis
        -----
        For volume emitters, this method determines whether a particular
        point in space lies within the volume defined by the emitter's
        volume primitive.

        Returns: 
        ----- 
        true if the point lies inside the emitter's volume primitive,
        false otherwise.

        Parameters:
        -----
        worldPoint: MPoint
        	[in] -> worldspace coordinates of the point to be tested. 

        emitterWorldMatrix: MMatrix
        	[in] -> object to worldspace matrix for the emitter, which can be obtained using the 


        '''
        pass

    def volumePrimitiveDistanceFromAxis(self, worldPoint: MPoint,
                        emitterWorldMatrix: MMatrix): 
        '''
        volumePrimitiveDistanceFromAxis(self, worldPoint: MPoint,
                        emitterWorldMatrix: MMatrix) -> double

        Synopsis
        -----
        For volume emitters, this method determines the distance from a
        particular point to the major axis of the volumetric primitive
        associated with the emitter. For fluid emitters, this distance
        can be used to implement simple emission dropoff behavior.

        Returns: 
        ----- 
        The distance from the point to the major axis of the emitter's
        volume primitive.

        Parameters:
        -----
        worldPoint: MPoint
        	[in] -> worldspace coordinates of the point to be tested. 

        emitterWorldMatrix: MMatrix
        	[in] -> object to worldspace matrix for the emitter, which can be obtained using the 


        '''
        pass

    def hasValidEmission2dTexture(self, texAttr: MObject,
                        status: MPxEmitterNode.MStatus): 
        '''
        hasValidEmission2dTexture(self, texAttr: MObject,
                        status: MPxEmitterNode.MStatus) -> bool

        Synopsis
        -----
        Certain aspects of Maya's particle and fluid emitters can be
        textured using 2d textures. For example, surface particle
        emitters can use a 2d texture to modulate the emission rate over
        the surface. For these purposes, only a subset of Maya's textures
        are supported, namely the default 2d textures (bulge, checker,
        cloth, file, fluid texture 2d, fractal, grid, mountain, movie,
        noise, ocean, ramp, water). No other nodes are supported. This
        method takes an attribute on an emitter, and determines if there
        is a supported texture connected to it. If the texture is
        supported, then the evalEmission2dTexture() method can be called
        to evaluate the texture at various (u,v) coordinate values.

        Returns: 
        ----- 
        true if the node connected to the specified emitter attribute is
        a texture that can be evaluated using the evalEmission2dTexture()
        method, false otherwise.

        Parameters:
        -----
        texAttr: MObject
        	[in] -> attribute to be tested for a valid texture connection. 

        status: MPxEmitterNode.MStatus
        	[out] -> status code.


        '''
        pass

    def evalEmission2dTexture(self, texAttr: MObject,
                        uCoords: MDoubleArray,
                        vCoords: MDoubleArray,
                        resultColors: MVectorArray,
                        resultAlphas: MDoubleArray): 
        '''
        evalEmission2dTexture(self, texAttr: MObject,
                        uCoords: MDoubleArray,
                        vCoords: MDoubleArray,
                        resultColors: MVectorArray,
                        resultAlphas: MDoubleArray)

        Synopsis
        -----
        If a supported 2d texture (see hasValidEmission2dTexture() method
        documentation) is connected to the given emitter attribute, this
        method can be called to evaluate that texture at a number of
        (u,v) texture coordinate values.

        Returns:
        -----
        None

        Parameters:
        -----
        texAttr: MObject
        	[in] -> attribute whose connected texture is to be evaluated. 

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

    def thisMObject(self): 
        '''
        thisMObject(self) -> MObject

        Synopsis
        -----
        Returns the MObject associated with this user defined node. This
        makes it possible to use MFnDependencyNode or to construct plugs
        to this node's attributes.It is not necessary to override this
        method.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MEmitterType:
    '''Types of emitters. 
    Non-functional class.  Values for this enum:
    kDirectional
    kOmni
    kSurface
    kCurve
    kVolume
    '''

    def __init__(self):
        pass

    def kDirectional(self):
        '''This is an enum of MEmitterType.
        - Description:  
        - Value: 0
        '''
        pass

    def kOmni(self):
        '''This is an enum of MEmitterType.
        - Description:  
        - Value: 1
        '''
        pass

    def kSurface(self):
        '''This is an enum of MEmitterType.
        - Description:  
        - Value: 2
        '''
        pass

    def kCurve(self):
        '''This is an enum of MEmitterType.
        - Description:  
        - Value: 3
        '''
        pass

    def kVolume(self):
        '''This is an enum of MEmitterType.
        - Description:  
        - Value: 4
        '''
        pass

class MPxFieldNode:
    '''Base class for user defined fields.
MPxFieldNode allows the creation and manipulation of dependency graph nodes
representing fields. This is the top level of a hierarchy of
field node function sets. It permits manipulation of the
attributes common to all types of fields.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MPxNode.MPxNode

        Synopsis
        -----
        This method returns the type of the node. This method should not
        be overridden by the user. It will return
        MPxNode::kFieldNode.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def compute(self, plug: MPlug,
                        dataBlock: MDataBlock): 
        '''
        compute(self, plug: MPlug,
                        dataBlock: MDataBlock)

        Synopsis
        -----
        This method should be overridden in user defined nodes. Recompute
        the given output based on the nodes inputs. The plug represents
        the data value that needs to be recomputed, and the data block
        holds the storage for all of the node's attributes.The MDataBlock
        will provide smart handles for reading and writing this node's
        attribute values. Only these values should be used when
        performing computations.When evaluating the dependency graph,
        Maya will first call the compute method for this node. If the
        plug that is provided to the compute indicates that that the
        attribute was defined by the Maya parent node, the compute method
        should return MS::kUnknownParameter. When this occurs, Maya will
        call the internal Maya node from which the user-defined node is
        derived to compute the plug's value.This means that a user
        defined node does not need to be concerned with computing
        inherited output attributes. However, if desired, these can be
        safely recomputed by this method to change the behaviour of the
        node.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
        plug: MPlug
        	[in] -> plug representing the attribute that needs to be recomputed 

        dataBlock: MDataBlock
        	[out] -> data block containing storage for the node's attributes


        '''
        pass

    def getForceAtPoint(self, point: MVectorArray,
                        velocity: MVectorArray,
                        mass: MDoubleArray,
                        force: MVectorArray,
                        deltaTime: double): 
        '''
        getForceAtPoint(self, point: MVectorArray,
                        velocity: MVectorArray,
                        mass: MDoubleArray,
                        force: MVectorArray,
                        deltaTime: double)

        Synopsis
        -----
        This method is not required to be overridden, it is only
        necessary for compatibility with the MFnField function set.
        Compute the force of a field on an array of points, given their
        position, velocity, and mass.This method uses MVectorArray to
        represent the positions of a point.

        Returns:
        -----
        None

        Parameters:
        -----
        point: MVectorArray
        	[in] -> array of positions for each point. 

        velocity: MVectorArray
        	[in] -> array of velocities for each point. If the length of the velocity array is 0, a velocity of 0.0 is assumed for all the points. Note the velocity array is a requirement for the Air and Drag fields to compute forces. 

        mass: MDoubleArray
        	[in] -> array of mass values for each point. If the length of the mass array is 0, a mass of 1.0 is assumed for all the points. 

        force: MVectorArray
        	[out] -> output array of forces applied to each point. If the length of the force array supplied is 0, the array is automatically resized. If the contents of the force array contains data, the computed force is added to the supplied data. This can be useful to accumulate forces of multiple fields. 

        deltaTime: double
        	[in] -> time increment in seconds


        '''
        pass

    def iconSizeAndOrigin(self, width: MPxFieldNode.GLuint,
                        height: MPxFieldNode.GLuint,
                        xbo: MPxFieldNode.GLuint,
                        ybo: MPxFieldNode.GLuint): 
        '''
        iconSizeAndOrigin(self, width: MPxFieldNode.GLuint,
                        height: MPxFieldNode.GLuint,
                        xbo: MPxFieldNode.GLuint,
                        ybo: MPxFieldNode.GLuint)

        Synopsis
        -----
        Define the size and the origin of the field's icon. Maya calls
        this method to determine the size and origin of the icon you wish
        your field to use. Overriding this method is optional.The
        arguments have the same meaning as defined in OpenGL's glBitmap
        method.

        Returns:
        -----
        None

        Parameters:
        -----
        width: MPxFieldNode.GLuint
        	[out] -> the width of the icon in pixels. It needs to be a multiple of 32 on windows and a multiple of 16 on any other platform. 

        height: MPxFieldNode.GLuint
        	[out] -> the height of the icon in pixels. It needs to be a multiple of 32 on windows and a multiple of 16 on any other platform. 

        xbo: MPxFieldNode.GLuint
        	[out] -> the origin of the icon in x direction. 

        ybo: MPxFieldNode.GLuint
        	[out] -> the origin of the icon in y direction.


        '''
        pass

    def iconBitmap(self, bitmap: MPxFieldNode.GLubyte): 
        '''
        iconBitmap(self, bitmap: MPxFieldNode.GLubyte)

        Synopsis
        -----
        Define the bitmap for the field's icon. Maya calls this method to
        get the bitmap for the icon you wish your field to use.
        Overriding this method is optional, but if you do override it
        then you must also override iconSizeAndOrigin().

        Returns:
        -----
        None

        Parameters:
        -----
        bitmap: MPxFieldNode.GLubyte
        	[out] -> Bitmap for the field's icon, in the format expected by OpenGL's glBitmap() function. The storage pointed to by this parameter will have already been allocated by Maya according to the values returned by 


        '''
        pass

    def draw(self, view: M3dView,
                        path: MDagPath,
                        style: M3dView.M3dView): 
        '''
        draw(self, view: M3dView,
                        path: MDagPath,
                        style: M3dView.M3dView)

        Synopsis
        -----
        Overriding this method allows the drawing of custom geometry
        using standard OpenGL calls. The OpenGL state should be left in
        the same state that it was in previously. The OpenGL routine
        glPushAttrib may be used to make this easier.When this routine is
        called, the following conditions may be assumed:As a convenience,
        this draw method will also be used by OpenGL's selection
        mechanism to determine whether this object gets selected by a
        particular mouse event. The user does not need to write a
        separate selection routine.

        Returns:
        -----
        None

        Parameters:
        -----
        view: M3dView
        	[in] -> 3D view that is being drawn into 

        path: MDagPath
        	[in] -> to this node in the DAG 

        style: M3dView.M3dView
        	[in] -> style to draw object in 


        '''
        pass

    def falloffCurve(self, param: double,
                        ReturnStatus: MPxFieldNode.MStatus): 
        '''
        falloffCurve(self, param: double,
                        ReturnStatus: MPxFieldNode.MStatus) -> double

        Synopsis
        -----
        Returns the falloff at the given parameter value.

        Returns: 
        ----- 
        The falloff value at the given the param.

        Parameters:
        -----
        param: double
        	[in] -> Parameter value in the range [0.0, 1.0] 

        ReturnStatus: MPxFieldNode.MStatus
        	[out] -> Status code


        '''
        pass

    def isFalloffCurveConstantOne(self, ReturnStatus: MPxFieldNode.MStatus): 
        '''
        isFalloffCurveConstantOne(self, ReturnStatus: MPxFieldNode.MStatus) -> bool

        Synopsis
        -----
        Returns true if the falloffCurve is a constant one (default) or
        false if not.

        Returns: 
        ----- 
        true if the falloff curve is a constant one, false otherwise

        Parameters:
        -----
        ReturnStatus: MPxFieldNode.MStatus
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

    def thisMObject(self): 
        '''
        thisMObject(self) -> MObject

        Synopsis
        -----
        Returns the MObject associated with this user defined node. This
        makes it possible to use MFnDependencyNode or to construct plugs
        to this node's attributes.It is not necessary to override this
        method.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MPxFileResolver:
    '''Base Class for creating custom Maya File Resolvers.
This class provides a base class from which a custom file
resolver plug-in can be derived. A file resolver plug-in allows
the user to override the manner in which an unresolved file path
value is converted to a resolved file path. The resolved file
path is the location Maya will use to access the physical file.
Maya supports plug-in File Resolvers for file paths defined using
URI values. When an unresolved URI file path is encountered, Maya
will search for any registered URI file resolver plug-ins that
can handle it.
URI file resolvers are registered for a given URI scheme. For
example, a custom file resolver plug-in could be registered to
handle the "http" URI scheme. If Maya attempts to resolve a URI
file path that has the scheme "http", the custom resolver plug-in
will be called. URI schemes are treated in a case-insensitive
manner. For example, the schemes 'http', 'HTTP', and 'Http' are
considered equivalent.
MPxFileResolvers for URI schemes are registered using the
MFnPlugin::registerURIFileResolver method.
'''
    def __init__(self):
        pass


    def resolveURI(self, uriValue: MURI,
                        mode: MPxFileResolver.MPxFileResolver,
                        ReturnStatus: MPxFileResolver.MStatus): 
        '''
        resolveURI(self, uriValue: MURI,
                        mode: MPxFileResolver.MPxFileResolver,
                        ReturnStatus: MPxFileResolver.MStatus) -> MString

        Synopsis
        -----
        This routine is called by Maya to convert a URI value to a file
        path that can be accessed by Maya. This routine is only called if
        the resolveURIWithContext routine is not overridden in derived
        classes. Choose to use this routine when you do not need the
        context (fullName of the URI owner) to perform the
        resolution.Derived classes must override either this method or
        resolveURIWithContext(), but not both. This virtual method must
        be overridden in derived classes if resolveURIWithContext() is
        not overridden, as the default version defined in MPxFileResolver
        simply fails unconditionally.The routine is passed an MURI object
        that contains the URI value that requires resolution. The
        resolver will interpret the data in the URI and determine the
        physical file path value that Maya will use to access the
        file.The output from the routine is a fully qualified file path
        that can be accessed by Maya.It is important to note that
        successful resolution of a file path indicates that the URI
        filepath was successfully converted to a resolved file path.
        Successful resolution does not necessarily indicate whether or
        not the file referred to by the resolved file path actually
        exists.The resolution mode provides additional information to the
        resolver about the reason for the resolution request that can be
        used by the resolver implementation. Refer to the list of
        supported MPxFileResolver::MPxFileResolverMode modes for more
        information.

        Returns: 
        ----- 
        String containing the fully qualified file path of the resolved
        file, or an empty string if the resolution was not successful.

        Parameters:
        -----
        uriValue: MURI
        	[in] -> the unresolved URI value 

        mode: MPxFileResolver.MPxFileResolver
        	[in] -> the resolution mode 

        ReturnStatus: MPxFileResolver.MStatus
        	[out] -> status code, see below.


        '''
        pass

    def resolveURIWithContext(self, uriValue: MURI,
                        mode: MPxFileResolver.MPxFileResolver,
                        contextNodeFullName: MString,
                        ReturnStatus: MPxFileResolver.MStatus): 
        '''
        resolveURIWithContext(self, uriValue: MURI,
                        mode: MPxFileResolver.MPxFileResolver,
                        contextNodeFullName: MString,
                        ReturnStatus: MPxFileResolver.MStatus) -> MString

        Synopsis
        -----
        This routine is called by Maya to convert a URI value to a file
        path that can be accessed by Maya. Derived classes must override
        either this method or resolveURI(), but not both.The routine is
        passed an MURI object that contains the URI value that requires
        resolution. Additionally, it will be passed the owner fullname
        (context) when applicable. The resolver will interpret the data
        in the URI, use the context if required, and determine the
        physical file path value that Maya will use to access the
        file.The context is the fullname of the owner Node. The context
        fullname might be an empty string if the URI is an application
        property not associated to any specific scene element.The output
        from the routine is a fully qualified file path that can be
        accessed by Maya.It is important to note that successful
        resolution of a file path indicates that the URI filepath was
        successfully converted to a resolved file path. Successful
        resolution does not necessarily indicate whether or not the file
        referred to by the resolved file path actually exists.The
        resolution mode provides additional information to the resolver
        about the reason for the resolution request that can be used by
        the resolver implementation. Refer to the list of supported
        MPxFileResolver::MPxFileResolverMode modes for more information.

        Returns: 
        ----- 
        String containing the fully qualified file path of the resolved
        file, or an empty string if the resolution was not successful.

        Parameters:
        -----
        uriValue: MURI
        	[in] -> the unresolved URI value 

        mode: MPxFileResolver.MPxFileResolver
        	[in] -> the resolution mode 

        contextNodeFullName: MString
        	[in] -> the fullname of the URI owner Node 

        ReturnStatus: MPxFileResolver.MStatus
        	[out] -> status code, see below.


        '''
        pass

    def uriScheme(self): 
        '''
        uriScheme(self) -> MString

        Synopsis
        -----
        This routine is called to query the URI scheme that is handled by
        this resolver. An MPxFileResolver handles exactly one URI scheme.
        For example, a resolver that handles the "http" scheme would
        return "http".This virtual method must be overridden in derived
        classes. The default version defined in MPxFileResolver
        unconditionally returns an empty string.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def resolverName(self): 
        '''
        resolverName(self) -> MString

        Synopsis
        -----
        This routine is called to query the name of this resolver. The
        resolver name is specified when the resolver is registered in the
        call to MFnPlugin::registerURIFileResolver. Derived classes do
        not override this method.

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

    def performAfterSaveURI(self, uriValue: MURI,
                        resolvedFullName: MString): 
        '''
        performAfterSaveURI(self, uriValue: MURI,
                        resolvedFullName: MString)

        Synopsis
        -----
        This optional handler is provided so that registered URI file
        resolvers can do custom processing after file save. The method
        will be called by Maya after a scene file associated with this
        URI resolver is saved (i.e. a scene having a URI file path
        corresponding to the URI scheme implemented by this resolver).
        The timing of the call is similar to the MSceneMessage:kAfterSave
        callback, this method will however be called first, before any
        afterSave callbacks are invoked.The arguments to the method
        provide information about the file that was just saved: The URI
        file path is the unresolved path to the file, the resolved path
        gives the physical location of the file.This method is optional,
        it may be overridden in derived resolvers as required. The
        default version defined in MPxFileResolver does nothing.

        Returns:
        -----
        None

        Parameters:
        -----
        uriValue: MURI
        	[in] -> the URI (unresolved path) for the saved file 

        resolvedFullName: MString
        	[in] -> full path to the file that was saved 


        '''
        pass

    def getURIResolversByScheme(self): 
        '''
        getURIResolversByScheme(self) -> MStringArray

        Synopsis
        -----
        Generate a list containing the URI schemes for all registered
        file resolvers. Note: when called together,
        getURIResolversByScheme and getURIResolversByName will return
        lists of corresponding entries.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getURIResolversByName(self): 
        '''
        getURIResolversByName(self) -> MStringArray

        Synopsis
        -----
        Generate a list containing the names of all registered file
        resolvers. Note: when called together, getURIResolversByScheme
        and getURIResolversByName will return lists of corresponding
        entries.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def numURIResolvers(self): 
        '''
        numURIResolvers(self) -> int

        Synopsis
        -----
        Determine the number of registered URI file resolvers.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MPxFileResolverMode:
    '''The MFileResolverMode provides additional information about the reason for the resolution call that can be used by the resolver implementation. 
    Non-functional class.  Values for this enum:
    kNone
    kInput
    '''

    def __init__(self):
        pass

    def kNone(self):
        '''This is an enum of MPxFileResolverMode.
        - Description: (Default) The resolved path is being requested, but there is no additional information specified. When kNone is used, it will not be combined with any other modes listed below. In this case, the resolver should simply return the resolved path as efficiently as possible. The path returned by the resolver will not be checked for existence. 
        - Value: 1
        '''
        pass

    def kInput(self):
        '''This is an enum of MPxFileResolverMode.
        - Description: The resolved path is being requested for an input file. In this case, the resolver plug-in may need to do additional work to ensure that the resolved path is available to the application. The path returned by the resolver will be checked for existence. 
        - Value: 2
        '''
        pass

class MPxFileTranslator:
    '''Base Class for creating Maya File Translators.
This class provides the connection to Maya by which user written
file translators can be added as plug-ins.
This class provides a base class from which one derives in order
to implement Maya "File Translator Plug-Ins." A file translator
plug-in allows Maya to read or write 3rd party file formats.
The identifyFile method is called whenever Maya's file save or
restore dialogs are run, and identifyFile uses the filename and
first few bytes of the file to determine whether it is of a type
supported by the translator. If it is, then Maya will display the
file with the "name" and "icon" specified as arguments to
MFnPlugin::registerFileTranslator.
If an attempt is made to read the file, the "reader" method in
the derived class is called, if an attempt is made to write the
file, the "writer" method is called.
'''
    def __init__(self):
        pass


    def reader(self, file: MFileObject,
                        optionsString: MString,
                        mode: MPxFileTranslator.MPxFileTranslator): 
        '''
        reader(self, file: MFileObject,
                        optionsString: MString,
                        mode: MPxFileTranslator.MPxFileTranslator)

        Synopsis
        -----
        This routine is called by Maya when it is necessary to load a
        file of a type supported by this translator. This virtual method
        must be overloaded in derived classes, as the default version
        defined in MPxFileTranslator simply fails unconditionally. The
        only parameter is an MFileObject that contains the pathname of
        the file to be loaded. This routine is responsible for reading
        the contents of the given file, and creating Maya objects via API
        or MEL calls to reflect the data in the file.Reimplemented in
        MPxMayaAsciiFilter.

        Returns:
        -----
        None

        Parameters:
        -----
        file: MFileObject
        	[in] -> the name of the file to read 

        optionsString: MString
        	[in] -> a string representation of any file options 

        mode: MPxFileTranslator.MPxFileTranslator
        	[in] -> the method used to read the file - open or import


        '''
        pass

    def writer(self, file: MFileObject,
                        optionsString: MString,
                        mode: MPxFileTranslator.MPxFileTranslator): 
        '''
        writer(self, file: MFileObject,
                        optionsString: MString,
                        mode: MPxFileTranslator.MPxFileTranslator)

        Synopsis
        -----
        This routine is called by Maya when it is necessary to save a
        file of a type supported by this translator. This virtual method
        must be overloaded in derived classes, as the default version
        defined in MPxFileTranslator simply fails unconditionally. The
        only parameter is an MFileObject that contains the pathname of
        the file to be written to. This routine is responsible for
        traversing all objects in the current Maya scene, and writing a
        representation to the given file in the supported format.It is
        not essential that all information in the current Maya scene be
        written out, although if it is not, the scene will not be
        recreated when this file is read via the "reader"
        method.Reimplemented in MPxMayaAsciiFilter.

        Returns:
        -----
        None

        Parameters:
        -----
        file: MFileObject
        	[in] -> the name of the file to write 

        optionsString: MString
        	[in] -> a string representation of any file options 

        mode: MPxFileTranslator.MPxFileTranslator
        	[in] -> the method used to write the file - save, export, or export active.


        '''
        pass

    def haveReadMethod(self): 
        '''
        haveReadMethod(self) -> bool

        Synopsis
        -----
        This routine is called by Maya while it is executing in the
        MPxFileTranslator constructor. Maya uses this entry point to
        query the translator and determine if it provides a reader
        method.This virtual method must be overloaded in derived classes
        if a reader method exists, as the default version defined in
        MPxFileTranslator unconditionally returns false.Reimplemented in
        MPxMayaAsciiFilter.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def haveWriteMethod(self): 
        '''
        haveWriteMethod(self) -> bool

        Synopsis
        -----
        This routine is called by Maya while it is executing in the
        MPxFileTranslator constructor. Maya uses this entry point to
        query the translator and determine if it provides a write
        method.This virtual method must be overloaded in derived classes
        if a writer method exists, as the default version defined in
        MPxFileTranslator unconditionally returns false.Reimplemented in
        MPxMayaAsciiFilter.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def haveNamespaceSupport(self): 
        '''
        haveNamespaceSupport(self) -> bool

        Synopsis
        -----
        When a file is imported or referenced into an existing scene,
        there is the possibility that nodes in the incoming file will
        have the same names as nodes already in the scene. Although DAG
        nodes may legally have the same name so long as their DAG paths
        are different, in all other cases node names must be unique.Maya
        has a number of different algorithms which the user may select to
        resolve name clashes. (See the file command for more details.)
        Some of these algorithms involve creating a separate namespace
        for the incoming file and placing some or all of its nodes within
        that namespace.As some translators may have difficulty dealing
        with namespaces, Maya will first call the translator's
        haveNamespaceSupport() method to see if it can handle them.If the
        user requests that namespaces be used to resolve clashes and the
        translator does not support namespaces, then Maya will simply
        place all incoming nodes into the current namespace and it will
        be up to the translator to ensure that no clashes occur,
        otherwise there will be errors during the import/reference.If a
        translator can deal with having Maya placing some or all of a
        file's nodes into a separate namespace, then its derived class
        should override this virtual method to return true.By default the
        method returns false.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def haveReferenceMethod(self): 
        '''
        haveReferenceMethod(self) -> bool

        Synopsis
        -----
        This method is called by Maya to see if the translator implements
        its own custom file referencing. If this function returns true,
        every time a file of this translator's type is referenced and its
        parent is being saved or exported the write method of this
        translator will be called, so the custom file referencing can add
        information to its files.If it returns false, Maya's file
        referencing system will be used by default.This function returns
        false by default.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def defaultExtension(self): 
        '''
        defaultExtension(self) -> MString

        Synopsis
        -----
        This routine is called by Maya whenever it needs to know the
        default extension of a translator. This virtual method may be
        overloaded in derived classes if a default extension exists, as
        the default version defined in MPxFileTranslator unconditionally
        returns an empty string.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def filter(self): 
        '''
        filter(self) -> MString

        Synopsis
        -----
        This virtual method may be overloaded in a derived class to set
        the filter extension that will be used by the file dialog. If the
        defaultExtension method is not implemented in a derived class,
        the standard filter *.* will be returned by MPxFileTranslator and
        used by the file dialog. If defaultExtension is implemented in a
        derived class, that extension will be used in the proper format.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def canBeOpened(self): 
        '''
        canBeOpened(self) -> bool

        Synopsis
        -----
        This routine is called by Maya while it is executing in the
        MPxFileTranslator constructor. Maya uses this entry point to
        query the translator and determine if it can open files. The
        default is true.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def identifyFile(self, file: MFileObject,
                        buffer: char,
                        size: short): 
        '''
        identifyFile(self, file: MFileObject,
                        buffer: char,
                        size: short) -> MPxFileTranslator.MPxFileTranslator

        Synopsis
        -----
        This routine is called by Maya when a file selection dialog
        accesses a new directory. It will potentially be called once for
        every file in the directory.The routine is given an MFileObject
        indicating the file being checked, as well as a pointer to the
        initial file contents. The size parameter indicates the number of
        bytes available at the pointer location.This routine must use
        this data to determine if the file is of a type supported by this
        translator. This virtual method must be overloaded in derived
        classes, as the default version defined in MPxFileTranslator
        unconditionally returns kNotMyFileType.A typical use of this
        method is to check the file extension of the file in question,
        and return a status indicating whether or not the file is of the
        type expected by this MPxFileTranslator. See the plugin example
        animImportExport for an example.

        Returns: 
        ----- 
        MFileKind::kIsMyFileType this file is understood by this
        translator  MFileKind::kNotMyFileType this file is not understood
        by this translator  MFileKind::kCouldBeMyFileType this file is
        understood by this translator, but this translator is not the
        best one to use for reading or writing it

        Parameters:
        -----
        file: MFileObject
        	[in] -> the name of the file to check 

        buffer: char
        	[in] -> a pointer to the initial contents of the file 

        size: short
        	[in] -> the number of valid bytes in the buffer


        '''
        pass

    def fileAccessMode(self): 
        '''
        fileAccessMode(self) -> MPxFileTranslator.MPxFileTranslator

        Synopsis
        -----
        This routine returns the fileAccess mode maya is currently in.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MFileKind:
    '''How the translator identifies this file. 
    Non-functional class.  Values for this enum:
    kIsMyFileType
    kCouldBeMyFileType
    kNotMyFileType
    '''

    def __init__(self):
        pass

    def kIsMyFileType(self):
        '''This is an enum of MFileKind.
        - Description: Translator understands how to read/write this file. 
        - Value: 0
        '''
        pass

    def kCouldBeMyFileType(self):
        '''This is an enum of MFileKind.
        - Description: Translator is not best available to read/write this file. 
        - Value: 1
        '''
        pass

    def kNotMyFileType(self):
        '''This is an enum of MFileKind.
        - Description: Translator does not understand how to read/write this file. 
        - Value: 2
        '''
        pass

class FileAccessMode:
    '''Type of file access. 
    Non-functional class.  Values for this enum:
    kUnknownAccessMode
    kOpenAccessMode
    kReferenceAccessMode
    kImportAccessMode
    kSaveAccessMode
    kExportAccessMode
    kExportActiveAccessMode
    '''

    def __init__(self):
        pass

    def kUnknownAccessMode(self):
        '''This is an enum of FileAccessMode.
        - Description: This mode is set when no file operation is currently in progress. 
        - Value: 0
        '''
        pass

    def kOpenAccessMode(self):
        '''This is an enum of FileAccessMode.
        - Description: This mode is set when data is being read into a new scene. (i.e.: file -open True) 
        - Value: 1
        '''
        pass

    def kReferenceAccessMode(self):
        '''This is an enum of FileAccessMode.
        - Description: This mode is set when a referenced file is being read. This mode can be temporary if the parent file was opened or imported in. For example, if a parent file is being opened, the file access mode will be set to kOpenAccessMode but when the reference file is being read, it will be set to kReferenceAccessMode. It will be set back to kOpenAccessMode once the reference file has been read. 
        - Value: 2
        '''
        pass

    def kImportAccessMode(self):
        '''This is an enum of FileAccessMode.
        - Description: This mode is set when data is being read into the current scene. 
        - Value: 3
        '''
        pass

    def kSaveAccessMode(self):
        '''This is an enum of FileAccessMode.
        - Description: This mode is set when the user saves the file. (i.e.: file -save True) 
        - Value: 4
        '''
        pass

    def kExportAccessMode(self):
        '''This is an enum of FileAccessMode.
        - Description: This mode is set when the user chooses to export all or a referenced file is being written out. This mode can be temporary if the parent file was saved or exported out. For example, if a parent file is being saved, the file access mode will be set to kSaveAccessMode but when the reference file is being written, it will be set to kExportAccessMode. It will be set back to kSaveAccessMode once the reference file has been written. 
        - Value: 5
        '''
        pass

    def kExportActiveAccessMode(self):
        '''This is an enum of FileAccessMode.
        - Description: This mode is set when only the selected items are to be exported. 
        - Value: 6
        '''
        pass

class MPxFluidEmitterNode:
    '''Base class for user defined particle emitters.
MPxFluidEmitterNode allows the creation and manipulation of dependency graph nodes
representing fluid emitters.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MPxNode.MPxNode

        Synopsis
        -----
        This method returns the type of the node. It should not be
        overridden by the user. It will return
        MPxNode::kEmitterNode.Reimplemented from MPxEmitterNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def compute(self, plug: MPlug,
                        dataBlock: MDataBlock): 
        '''
        compute(self, plug: MPlug,
                        dataBlock: MDataBlock)

        Synopsis
        -----
        This method should be overridden in user defined nodes. Recompute
        the given output based on the nodes inputs. The plug represents
        the data value that needs to be recomputed, and the data block
        holds the storage for all of the node's attributes.The MDataBlock
        will provide smart handles for reading and writing this node's
        attribute values. Only these values should be used when
        performing computations.When evaluating the dependency graph,
        Maya will first call the compute method for this node. If the
        plug that is provided to the compute indicates that that the
        attribute was defined by the Maya parent node, the compute method
        should return MS::kUnknownParameter. When this occurs, Maya will
        call the internal Maya node from which the user-defined node is
        derived to compute the plug's value.This means that a user
        defined node does not need to be concerned with computing
        inherited output attributes. However, if desired, these can be
        safely recomputed by this method to change the behaviour of the
        node.Reimplemented from MPxEmitterNode.

        Returns:
        -----
        None

        Parameters:
        -----
        plug: MPlug
        	[in] -> plug representing the attribute that needs to be recomputed 

        dataBlock: MDataBlock
        	[out] -> data block containing storage for the node's attributes


        '''
        pass

    def fluidEmitter(self, fluidObj: MObject,
                        worldMatrix: MMatrix,
                        plugIndex: int): 
        '''
        fluidEmitter(self, fluidObj: MObject,
                        worldMatrix: MMatrix,
                        plugIndex: int)

        Synopsis
        -----
        This is the main method that plug-in fluid emitter nodes must
        override in order to emit into fluids. When an emitter is
        attached to a fluid, at every evaluation step the fluid will call
        this method on the emitter. The method receives a fluid object
        into which to emit, the index of the fluid in the array of fluid
        targets for this emitter, and the worldspace matrix of the fluid.
        The emitter should query its attributes to determine how much
        density, heat, color, and/or fuel to emit into the fluid, then
        call the MFnFluid::emitIntoArrays() method to actually add the
        necessary quantities to the fluid.Returning MS::kUnknownParameter
        from this method will cause Maya to execute the default fluid
        emitter's emission behavior.

        Returns:
        -----
        None

        Parameters:
        -----
        fluidObj: MObject
        	[in] -> the fluid object into which the emitter is emitting. 

        worldMatrix: MMatrix
        	[in] -> object to world transformation matrix for the fluid 

        plugIndex: int
        	[in] -> the index of the fluid in the array of emission targets for this emitter. Pass this value to the random number stream generation routines in 


        '''
        pass

    def fluidDensityEmission(self, block: MDataBlock): 
        '''
        fluidDensityEmission(self, block: MDataBlock) -> double

        Synopsis
        -----
        Intended to be called from within the emitter's compute() method,
        this method retrieves the "fluidDensityEmission" attribute value
        common to all fluid emitters. This indicates the amount of fluid
        material to be emitted per second, and it is modulated by the
        emitter's "rate" attribute value.

        Returns: 
        ----- 
        The fluid density emission rate for the fluid emitter.

        Parameters:
        -----
        block: MDataBlock
        	[out] -> data block containing storage for the node's attributes


        '''
        pass

    def fluidHeatEmission(self, block: MDataBlock): 
        '''
        fluidHeatEmission(self, block: MDataBlock) -> double

        Synopsis
        -----
        Intended to be called from within the emitter's compute() method,
        this method retrieves the "fluidHeatEmission" attribute value
        common to all fluid emitters. This indicates the amount of heat
        to be emitted per second, and it is modulated by the emitter's
        "rate" attribute value.

        Returns: 
        ----- 
        The fluid heat emission rate for the fluid emitter.

        Parameters:
        -----
        block: MDataBlock
        	[out] -> data block containing storage for the node's attributes


        '''
        pass

    def fluidFuelEmission(self, block: MDataBlock): 
        '''
        fluidFuelEmission(self, block: MDataBlock) -> double

        Synopsis
        -----
        Intended to be called from within the emitter's compute() method,
        this method retrieves the "fluidFuelEmission" attribute value
        common to all fluid emitters. This indicates the amount of fuel
        to be emitted per second, and it is modulated by the emitter's
        "rate" attribute value.

        Returns: 
        ----- 
        The fluid fuel emission rate for the fluid emitter.

        Parameters:
        -----
        block: MDataBlock
        	[out] -> data block containing storage for the node's attributes


        '''
        pass

    def fluidEmitColor(self, block: MDataBlock): 
        '''
        fluidEmitColor(self, block: MDataBlock) -> bool

        Synopsis
        -----
        Intended to be called from within the emitter's compute() method,
        this method retrieves the "fluidEmitColor" attribute value common
        to all fluid emitters. This indicates whether or not the emitter
        should emit color into the fluid.

        Returns: 
        ----- 
        true if the emitter should emit color into the fluid, false
        otherwise.

        Parameters:
        -----
        block: MDataBlock
        	[out] -> data block containing storage for the node's attributes


        '''
        pass

    def fluidColor(self, block: MDataBlock): 
        '''
        fluidColor(self, block: MDataBlock) -> MColor

        Synopsis
        -----
        Intended to be called from within the emitter's compute() method,
        this method retrieves the "fluidColor" attribute value common to
        all fluid emitters. This specifies the color to be added to the
        fluid.

        Returns: 
        ----- 
        The color that should be emitted into the fluid.

        Parameters:
        -----
        block: MDataBlock
        	[out] -> data block containing storage for the node's attributes


        '''
        pass

    def fluidDropoff(self, block: MDataBlock): 
        '''
        fluidDropoff(self, block: MDataBlock) -> double

        Synopsis
        -----
        Intended to be called from within the emitter's compute() method,
        this method retrieves the "fluidDropoff" attribute value common
        to all fluid emitters. This specifies the the speed with which
        fluid emission drops off with increasing distance from the
        emitter, with higher values meaning faster dropoff.

        Returns: 
        ----- 
        The dropoff rate for the fluid emitter.

        Parameters:
        -----
        block: MDataBlock
        	[out] -> data block containing storage for the node's attributes


        '''
        pass

    def turbulence(self, block: MDataBlock): 
        '''
        turbulence(self, block: MDataBlock) -> double

        Synopsis
        -----
        Intended to be called from within the emitter's compute() method,
        this method retrieves the "turbulence" attribute value common to
        all fluid emitters. This specifies the amount of turbulence that
        should be applied to the emitter's output.

        Returns: 
        ----- 
        The turbulence value for the fluid emitter.

        Parameters:
        -----
        block: MDataBlock
        	[out] -> data block containing storage for the node's attributes


        '''
        pass

    def fluidJitter(self, block: MDataBlock): 
        '''
        fluidJitter(self, block: MDataBlock) -> bool

        Synopsis
        -----
        Intended to be called from within the emitter's compute() method,
        this method retrieves the "fluidJitter" attribute value common to
        all fluid emitters. This specifies how the voxel grid should be
        sampled for emission. Without jitter, the grid is sampled only at
        voxel centers, but with jitter enabled, each voxel is sampled at
        a random location. The fluid emitter is responsible for
        implementing this behavior. It is recommended that the random
        stream methods on MPxEmitterNode be used to implement repeatable
        randomized behavior in this area.

        Returns: 
        ----- 
        true if jitter should be applied to the emission behavior, false
        otherwise.

        Parameters:
        -----
        block: MDataBlock
        	[out] -> data block containing storage for the node's attributes


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

class MPxGeometryData:
    '''Base Class for User-defined Dependency Graph Geometry Data Types.
This class is used to provide a wrapper or container for some
arbitrary geometry type that you have defined. This allows your
data type to exist as typed attributes on dependency nodes and to
be passed through dependency graph connections.
MP`xGeometryData is similar to
MPxData but includes methods to support sets (also known as groups) and
component iteration.
For user defined shapes (
MPxSurfaceShape derived classes), in order to support maya's deformers you must
declare an
MPxGeometryData class as well as a geometry iterator (
MPxGeometryIterator).
To register geometry data use
MFnPlugin::registerData with the type argument equal to
MPxData::kGeometryData.
'''
    def __init__(self):
        pass


    def updateCompleteVertexGroup(self, component: MObject): 
        '''
        updateCompleteVertexGroup(self, component: MObject) -> bool

        Synopsis
        -----
        This method is used in conjunction with MPxSurfaceShape classes
        which support maya's deformations. This method should make sure
        that complete vertex group data is up-to-date. If the given
        component is not complete (i.e. it represents all elements of
        your geometry) then you must mark is as complete using the
        methods of MFnComponent and return true if the component was
        updated, false if it was already complete.This method is used by
        deformers when deforming the "whole" object and not just selected
        components.

        Returns: 
        ----- 
        Returns true if the component was updated, false if it was
        already complete

        Parameters:
        -----
        component: MObject
        	[in] -> the component to test


        '''
        pass

    def deleteComponent(self, compList: MObjectArray): 
        '''
        deleteComponent(self, compList: MObjectArray) -> bool

        Synopsis
        -----
        This method should be overridden if this data is to support
        component deletion. For user defined shapes (MPxSurfaceShape)
        which support components, this method must be overridden if
        component deletion is to be supported when the shape has history.

        Returns: 
        ----- 
        true if the deletion was successfull, false otherwise

        Parameters:
        -----
        compList: MObjectArray
        	[in] -> a list of components that are to be deleted


        '''
        pass

    def deleteComponentsFromGroups(self, compList: MObjectArray,
                        groupIdArray: MIntArray,
                        groupComponentArray: MObjectArray): 
        '''
        deleteComponentsFromGroups(self, compList: MObjectArray,
                        groupIdArray: MIntArray,
                        groupComponentArray: MObjectArray) -> bool

        Synopsis
        -----
        This method should be overridden to modify the groups that flows
        along with the geometry, as part of the data, based on the
        components being deleted. It should intelligently update the
        groups based on what gets deleted. The class MFnGeometryData can
        be used to access and modify grouping information for data.The
        groupIdArray and groupComponentArray should contain the updated
        grouping information after the deletion has occurred.

        Returns: 
        ----- 
        true if the deletion was successfull, false otherwise

        Parameters:
        -----
        compList: MObjectArray
        	[in] -> a list of components that are to be deleted 

        groupIdArray: MIntArray
        	[in] -> array of group id's 

        groupComponentArray: MObjectArray
        	[in] -> array of updated components, one for each group id


        '''
        pass

    def smartCopy(self, srcGeom: MPxGeometryData): 
        '''
        smartCopy(self, srcGeom: MPxGeometryData) -> bool

        Synopsis
        -----
        This method is used in conjunction with MPxSurfaceShape classes
        which support maya's deformations. This method is used to prvoide
        maya with an efficient way to copy the source data into the
        memory of this data with as little memory allocation as
        possible.This method is not mandatory and only needs to be
        overridden to improve performance of deformations on shapes.

        Returns: 
        ----- 
        true is smartCopy actually took place and succeed, otherwise
        normal copy will take place.

        Parameters:
        -----
        srcGeom: MPxGeometryData
        	[in] -> a pointer to the data to be copied 


        '''
        pass

    def copy(self, src: MPxData): 
        '''
        copy(self, src: MPxData)

        Synopsis
        -----
        This method initializes an instance of an MPxGeometryData derived
        class from another existing instance. This method can be thought
        of as the second half of a copy constructor for the class. The
        default constructor has already been called for the instance, and
        this method is used to set the private data by copying the values
        from an existing instance. This is a pure virtual method, and
        must be overridden in derived classes.Implements MPxData.

        Returns:
        -----
        None

        Parameters:
        -----
        src: MPxData
        	[in] -> The object from which to copy the private data 


        '''
        pass

    def typeId(self): 
        '''
        typeId(self) -> MTypeId

        Synopsis
        -----
        Determines the type id of the Data object. This is a pure virtual
        method, and must be overridden in derived classes.Implements
        MPxData.

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
        Determines the type name of the Data object. This is a pure
        virtual method, and must be overridden in derived
        classes.Implements MPxData.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setMatrix(self, m: MMatrix): 
        '''
        setMatrix(self, m: MMatrix)

        Synopsis
        -----
        Store the matrix associated to MPxGeometryData. The matrix
        transformation will take place when the data is used, for example
        in deformer.

        Returns:
        -----
        None

        Parameters:
        -----
        m: MMatrix
        	[in] -> the matrix to transfer a point from local object space to world space. 


        '''
        pass

    @overload
    def matrix(self): 
        '''
        matrix(self) -> const MMatrix&

        Synopsis
        -----
        Return the matrix associated to MPxGeometryData.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def matrix(self, m: MMatrix): 
        '''
        matrix(self, m: MMatrix) -> bool

        Synopsis
        -----
        Return the matrix associated to MPxGeometryData.

        Returns: 
        ----- 
        true if m is not an identity matrix, false otherwise

        Parameters:
        -----
        m: MMatrix
        	[out] -> the returned matrix that takes a point from local object space to world space.


        '''
        pass

class MPxGeometryFilter:
    '''Base class for user-defined deformers.
MPxGeometryFilter allows the creation of user-defined deformers. A deformer is a
node which takes any number of input geometries, deforms them,
and places the output into the output geometry attribute.
If you write a deformer by deriving from
MPxGeometryFilter, your deformer will derive the benefit of Maya's internal
deformer functionality, namely:
Deformers are full dependency nodes and can have attributes and a
deform() method. In general, to derive the full benefit of the Maya
deformer base class, it is suggested that you do not write your
own
compute() method. Instead, write the
deform() method, which is called by the
MPxGeometryFilter's
compute() method. However, there are some exceptions when you would
instead write your own
compute(), namely:
In the case where you cannot simply override the
deform() method, the following example code shows one possible
compute() method implementation. This
compute() example creates an iterator for the deformer set corresponding
to the output geometry being computed. Note that this sample
compute() implementation does not do any deformation, and does not
implement handling of the nodeState attribute. If you do choose
to override
compute() in your node, there is no reason to implement the
deform() method, since it will not be called by the base class.
For most deformers, implementing
compute() is unnecessary. To create a deformer, derive from this class and
override the
deform() method as demonstrated in the "offsetNode.cpp" example plug-in.
The other methods of the parent class
MPxNode may also be overridden to perform standard dependency node
capabilities.
When implementing the compute method for a deformer, another
consideration is that the input geometry attribute is not cached.
This means that all of the inputs will evaluate each time
MDataBlock::inputArrayValue is called on "inputGeom". If you only want a single
inputGeometry, you can prevent unneeded evaluations by avoiding
calls to
MDataBlock.inputArrayValue. For example, use the technique shown in the above example or
use
MDataBlock::outputArrayValue.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MPxNode.MPxNode

        Synopsis
        -----
        This method returns the type of the node. This method should not
        be overridden by the user. It will return
        MPxNode::kGeometryFilter.Reimplemented from MPxNode.Reimplemented
        in MPxSkinCluster.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def deform(self, block: MDataBlock,
                        iterator: MItGeometry,
                        matrix: MMatrix,
                        multiIndex: int): 
        '''
        deform(self, block: MDataBlock,
                        iterator: MItGeometry,
                        matrix: MMatrix,
                        multiIndex: int)

        Synopsis
        -----
        This method performs the deformation algorithm. A status code of
        MS::kSuccess should be returned unless there was a problem during
        the deformation, such as insufficient memory or required input
        data is missing or invalid.NOTE: the geometry iterator passed to
        this method is in local space and not world space. To convert
        points to world space use the matrix that is suppied.

        Returns:
        -----
        None

        Parameters:
        -----
        block: MDataBlock
        	[in] -> the node's datablock. 

        iterator: MItGeometry
        	[in] -> an iterator for the current geometry being deformed. 

        matrix: MMatrix
        	[in] -> the geometry's world space transformation matrix. 

        multiIndex: int
        	[in] -> the index corresponding to the requested output geometry.


        '''
        pass

    def accessoryAttribute(self): 
        '''
        accessoryAttribute(self) -> MObject

        Synopsis
        -----
        This method returns an MObject for the attribute to which an
        accessory shape is connected. If the accessory shape is deleted,
        the deformer node will automatically be deleted.If your node has
        no associated shape, there is no need to override this method.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def accessoryNodeSetup(self, cmd: MDagModifier): 
        '''
        accessoryNodeSetup(self, cmd: MDagModifier)

        Synopsis
        -----
        This method is called by the "deformer -type" command when your
        node is specified. This method can be used to create and attach
        accessory nodes if your plugin node requires them. To do so,
        override this method, and provide the creation and attachment
        commands to the MDagModifier that is passed as input to the
        method.If your node has no associated nodes, there is no need to
        override this method.

        Returns:
        -----
        None

        Parameters:
        -----
        cmd: MDagModifier
        	[in] -> the dag modifier to which the method will add commands


        '''
        pass

    def setUseExistingConnectionWhenSetEditing(self, state: bool): 
        '''
        setUseExistingConnectionWhenSetEditing(self, state: bool)

        Synopsis
        -----
        This method allows the plugin node to request special treatment
        during set editing. It controls the connection behavior if all of
        a geometry's points are removed from the deformer set, and then
        points are subsequently added back in to the set again. By
        default, Maya will reconnect the deformer to the shape using a
        new input/output index. If this method is called in the custom
        deformer's postConstructor method and the state is set to true,
        the deformer will attempt to use the original input/output index
        when reconnecting to the shape.

        Returns:
        -----
        None

        Parameters:
        -----
        state: bool
        	[in] -> whether or not to use the existing connection 


        '''
        pass

    def setDeformationDetails(self, flags: int): 
        '''
        setDeformationDetails(self, flags: int)

        Synopsis
        -----
        This method allows the plug-in node to inform the system that it
        intends to deform components other than just positions. It should
        typically be called in advance of any deformation taking place
        (e.g. in postConstructor()), not in the deform() method. If it is
        called from deform(), the setting will take effect the next time
        the DG causes the deformation to be calculated.

        Returns:
        -----
        None

        Parameters:
        -----
        flags: int
        	[in] -> Bitwise OR of flags from the DeformationDetails enum


        '''
        pass

    def getDeformationDetails(self, ReturnStatus: MPxGeometryFilter.MStatus): 
        '''
        getDeformationDetails(self, ReturnStatus: MPxGeometryFilter.MStatus) -> int

        Synopsis
        -----
        Retrieves the value set by setDeformationDetails(). See the
        documentation of that method for the interpretation of the value.

        Returns: 
        ----- 
        The deformation details

        Parameters:
        -----
        ReturnStatus: MPxGeometryFilter.MStatus
        	[out] -> Status code.


        '''
        pass

    def setModifiedCallback(self, list: MSelectionList,
                        listAdded: bool): 
        '''
        setModifiedCallback(self, list: MSelectionList,
                        listAdded: bool)

        Synopsis
        -----
        This callback method can be overriden and is called whenever the
        set this deformer is operating on is modified. It passes in a
        selection list of items that are either being added/removed.

        Returns:
        -----
        None

        Parameters:
        -----
        list: MSelectionList
        	[in] -> list of items added/removed 

        listAdded: bool
        	[in] -> whether the list is being added or removed to the set. 


        '''
        pass

    def indexMapper(self, multiIndex: int,
                        ReturnStatus: MPxGeometryFilter.MStatus): 
        '''
        indexMapper(self, multiIndex: int,
                        ReturnStatus: MPxGeometryFilter.MStatus) -> const MIndexMapper&

        Synopsis
        -----
        Introduced in 2024.0 This method returns the indexMapper of the
        deformer.The indexMapper defines the subset on which the deformer
        operates. Reimplemented in MPxDeformerNode.

        Returns: 
        ----- 
        the index mapper

        Parameters:
        -----
        multiIndex: int
        	[in] -> the index corresponding to the geometry 

        ReturnStatus: MPxGeometryFilter.MStatus
        	[out] -> Status code.


        '''
        pass

    def getGeometryIterator(self, iter: MItGeometry,
                        block: MDataBlock,
                        dataHandle: MDataHandle,
                        multiIndex: int,
                        readOnly: bool,
                        ReturnStatus: MPxGeometryFilter.MStatus): 
        '''
        getGeometryIterator(self, iter: MItGeometry,
                        block: MDataBlock,
                        dataHandle: MDataHandle,
                        multiIndex: int,
                        readOnly: bool,
                        ReturnStatus: MPxGeometryFilter.MStatus) -> MFnGeometryData.MFnGeometryData

        Synopsis
        -----
        Introduced in 2022.0 This method initializes a geometry iterator
        for the subset of the geometry that must be deformed.This subset
        is either defined by a groupId or a componentTagExpression.

        Returns: 
        ----- 
        The group content state of the deformer.

        Parameters:
        -----
        iter: MItGeometry
        	[in] -> the iterator to be initialized. 

        block: MDataBlock
        	[in] -> the node's datablock. 

        dataHandle: MDataHandle
        	[in] -> The dataHandle pointing to the geometry data. 

        multiIndex: int
        	[in] -> the index corresponding to the requested output geometry. 

        readOnly: bool
        	[in] -> If false you will be allowed to modify the geometry position data during the iteration. 

        ReturnStatus: MPxGeometryFilter.MStatus
        	[out] -> Status code 


        '''
        pass

    def getFixedSetupData(self, name: MString): 
        '''
        getFixedSetupData(self, name: MString) -> MObject

        Synopsis
        -----
        Introduced in 2022.0 This method retrieves data requested by the
        related node that is implemented for the GPU.A name identifier is
        given to specify what information is requested. It is up to the
        specific CPU and GPU implementations to agree upon the name and
        the type of data.

        Returns: 
        ----- 
        The object containg the data, or the Null object if it could not
        found.

        Parameters:
        -----
        name: MString
        	[in] -> The string identifying what information is requested 


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

    def thisMObject(self): 
        '''
        thisMObject(self) -> MObject

        Synopsis
        -----
        Returns the MObject associated with this user defined node. This
        makes it possible to use MFnDependencyNode or to construct plugs
        to this node's attributes.It is not necessary to override this
        method.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def componentTagExpression(self): 
        '''
        componentTagExpression(self) -> MObject

        Synopsis
        -----
        Introduced in 2022.0 input componentTagExpression attribute

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class DeformationDetails:
    '''Deformation details. 
    Non-functional class.  Values for this enum:
    kDeformsUVs
    kDeformsColors
    '''

    def __init__(self):
        pass

    def kDeformsUVs(self):
        '''This is an enum of DeformationDetails.
        - Description: The deformer will deform UVs. 
        - Value: 2
        '''
        pass

    def kDeformsColors(self):
        '''This is an enum of DeformationDetails.
        - Description: The deformer will deform colors. 
        - Value: 4
        '''
        pass

class MPxGeometryIterator:
    '''Base class for user defined geometry iterators.
This is the base class for user defined geometry iterators.
Geometry iterator allow iterating over components in geometry in
a geometry independent manner. This base class defines the
interface to be used by maya when a generic component iteration
is required.
This class is used in conjunction with
MPxSurfaceShape to provide an iterator for components in a user defined shape.
Also this method can is used by
MPxGeometryData to provide an iterator over geometry that is passed through DG
connections.
The main methods to override in this class are point and
setPoint. The reset, isDone, and next methods have a default
implementation and should only be overridden if the component
being iterator on is not a single indexed component type.
The iterator works in two modes, over components or over all
elements in some geometry. If the components passed into the
constructors are null or empty then the iteration is meant to be
over the entire object.
'''
    def __init__(self):
        pass


    def isDone(self): 
        '''
        isDone(self) -> bool

        Synopsis
        -----
        Indicates if all the items have been traversed yet.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def component(self, component: MObject): 
        '''
        component(self, component: MObject)

        Synopsis
        -----
        Returns a component for the current item in the iteration.

        Returns:
        -----
        None

        Parameters:
        -----
        component: MObject
        	[out] -> storage for the returned component 


        '''
        pass

    def hasPoints(self): 
        '''
        hasPoints(self) -> bool

        Synopsis
        -----
        Indicates whether the underlying geometry has point data.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def iteratorCount(self): 
        '''
        iteratorCount(self) -> int

        Synopsis
        -----
        Returns an estimate of how many items will be iterated over.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def point(self): 
        '''
        point(self) -> MPoint

        Synopsis
        -----
        Returns the current component's positional data.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setPoint(self, point: MPoint): 
        '''
        setPoint(self, point: MPoint)

        Synopsis
        -----
        Sets the current component's positional data.

        Returns:
        -----
        None

        Parameters:
        -----
        point: MPoint
        	[in] -> the new positional value to set 


        '''
        pass

    def setPointGetNext(self, point: MPoint): 
        '''
        setPointGetNext(self, point: MPoint) -> int

        Synopsis
        -----
        Sets the current component's positional data, gets the next
        point.

        Returns: 
        ----- 
        The next index value

        Parameters:
        -----
        point: MPoint
        	[in] -> the positional value to set


        '''
        pass

    def index(self): 
        '''
        index(self) -> int

        Synopsis
        -----
        Returns a unique index for the current item in the iteration. If
        the iteration is over the whole geometry then this index is the
        same as current point. If the iteration is over some elements of
        the geometry specified by a component then this index is the
        index in your geometry.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def hasNormals(self): 
        '''
        hasNormals(self) -> bool

        Synopsis
        -----
        Indicates whether the underlying geometry has normals.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def indexUnsimplified(self): 
        '''
        indexUnsimplified(self) -> int

        Synopsis
        -----
        Returns a unique index for the current item in the iteration
        Rather than being the iterator index this is the index for the
        actual item when simplification is skipping items. This index
        will be equal to index() if no simplification, otherwise it will
        be larger.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def currentPoint(self): 
        '''
        currentPoint(self) -> int

        Synopsis
        -----
        Returns the index that is being iterated on. This value is used
        when iterating over all elements of your geometry, i.e. when
        there are no components specified.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setCurrentPoint(self, index: int): 
        '''
        setCurrentPoint(self, index: int)

        Synopsis
        -----
        Set the current index of the iteration. This value is used when
        iterating over all elements of your geometry, i.e. when there are
        no components specified.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> the current point in the iteration 


        '''
        pass

    def maxPoints(self): 
        '''
        maxPoints(self) -> int

        Synopsis
        -----
        Returns the largest index that will be iterated over. This value
        is used when iterating over all elements of your geometry, i.e.
        when there are no components specified.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setMaxPoints(self, index: int): 
        '''
        setMaxPoints(self, index: int)

        Synopsis
        -----
        Sets the largest index that will be iterated over. This value is
        used when iterating over all elements of your geometry, i.e. when
        there are no components specified.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> the maximum index value 


        '''
        pass

    def setObject(self, shape: MPxSurfaceShape): 
        '''
        setObject(self, shape: MPxSurfaceShape)

        Synopsis
        -----
        Optional method to set a shape object to iterate over to allow
        tweaking of the shape's history (input geometry).

        Returns:
        -----
        None

        Parameters:
        -----
        shape: MPxSurfaceShape
        	[in] -> a user defined shape object 


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

class MPxGlBuffer:
    '''Historically this class was used to created offscreen buffers on
Linux.
This class is now using FBO. Invoke
openFbo() method to create a Frame Buffer Object. The contents of the
frame buffer object (FBO) can be read back by using the
bindFbo() method and OpenGl calls to read pixels. After rendering and
reading pixels, the frame buffer object can be destroyed by
calling
closeFbo().
'''
    def __init__(self):
        pass


    def openFbo(self, width: short,
                        height: short,
                        view: M3dView): 
        '''
        openFbo(self, width: short,
                        height: short,
                        view: M3dView)

        Synopsis
        -----
        Create a frame buffer object where the renderer result will be
        stored. The format of this buffer will be RGBA. Note only one of
        these offscreen buffers should exist.

        Returns:
        -----
        None

        Parameters:
        -----
        width: short
        	[in] -> width of the buffer to create 

        height: short
        	[in] -> height of the buffer to create 

        view: M3dView
        	[in] -> M3dView


        '''
        pass

    def closeFbo(self, view: M3dView): 
        '''
        closeFbo(self, view: M3dView)

        Synopsis
        -----
        Destroy a frame buffer object that was created by createFbo.

        Returns:
        -----
        None

        Parameters:
        -----
        view: M3dView
        	[in] -> M3dView


        '''
        pass

    def bindFbo(self): 
        '''
        bindFbo(self)

        Synopsis
        -----
        If a frame buffer object was created using the method openFbo,
        then this method can be used to bind that Fbo. When the buffer is
        bound, all OpenGL draw calls will render into the created buffer.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def unbindFbo(self): 
        '''
        unbindFbo(self)

        Synopsis
        -----
        If a frame buffer object was created using the method openFbo,
        then this method can be used to unbind that Fbo.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def beginBufferNotify(self): 
        '''
        beginBufferNotify(self)

        Synopsis
        -----
        This method is called when the GL buffer is being setup by the
        viewport renderer. Overriding this call will allow you to access
        the full GL state after it has been setup but before any drawing
        has occurred.If you change any state information from within this
        call; you must make sure you return it back to this state at the
        call to endBufferNotify()

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def endBufferNotify(self): 
        '''
        endBufferNotify(self)

        Synopsis
        -----
        This method is called when the GL buffer is being shutdown by the
        viewport renderer. Overriding this call will allow you to access
        the full GL state after drawing has completed but just before the
        GL buffer is shut down.

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

class MPxHardwareShader:
    '''Base class for user defined hardware shaders.
MPxHardwareShader allows the creation of user-defined hardware shaders. A hardware
shader allows the plug-in writer to control the on-screen display
of an object in Maya.
You must derive a hardware shader node from
MPxHardwareShader for it to have any effect on the on-screen display at all. In
addition to their effect on the on-screen display of objects,
hardware shaders function as surface shader nodes. This allows
you to connect any shading network up to the hardware shader's
outColor attribute to handle the shading during a software
render.
To create a working hardware shader, derive from this class and
override the
render() and optionally the
populateRequirements() methods. The other methods of the parent class
MPxNode may also be overridden to perform dependency node capabilities.
NOTE: Plug-in hardware shaders are fully supported for polygonal
mesh shapes. NURBS surfaces are only supported in the High
Quality Interactive viewport and Hardware Renderer.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MPxNode.MPxNode

        Synopsis
        -----
        This method returns the type of the node. This method should not
        be overridden by the user. It will return
        MPxNode::kHardwareShader.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setVaryingParameters(self, parameters: MVaryingParameterList,
                        remapCurrentValues: bool,
                        dagModifier: MDagModifier): 
        '''
        setVaryingParameters(self, parameters: MVaryingParameterList,
                        remapCurrentValues: bool,
                        dagModifier: MDagModifier)

        Synopsis
        -----
        Call this method to set the list of varying parameters this
        shader uses. Once set, you can use these parameters directly to
        access geometry data for surfaces being shaded. When using this
        method to manage shader varying parameters, there is no need to
        override populateRequirements or handle the node interface as
        Maya will handle parameter setup, presentation and configuration
        for you.It is important to call this method whenever the shader
        parameters are modified (including at load time).This is an
        optional method - shader implementations are still free to manage
        geometry parameters independently if they wish.

        Returns:
        -----
        None

        Parameters:
        -----
        parameters: MVaryingParameterList
        	[in] -> the list of varying parameters for this shader 

        remapCurrentValues: bool
        	[in] -> if true (the default), Maya will attempt to initialise the value of new parameters based on any equivalently named parameters that currently exist on the node. Otherwise, the parameters will be setup using default values. Unless you wish to forcibly reset parameter values, the default value of true should be used. 

        dagModifier: MDagModifier
        	[in] -> an optional DG modifier to use when managing the attributes used to represent the geometry parameters on this shader.


        '''
        pass

    def setUniformParameters(self, parameters: MUniformParameterList,
                        remapCurrentValues: bool,
                        dagModifier: MDagModifier): 
        '''
        setUniformParameters(self, parameters: MUniformParameterList,
                        remapCurrentValues: bool,
                        dagModifier: MDagModifier)

        Synopsis
        -----
        Call this method to set the list of uniform parameters this
        shader uses. Once set, you can use these parameters to access the
        cached values of shader parameters, including testing when the
        value has been updated (to minimise the shader state changes).
        When using this method to manage uniform parameters, Maya will
        handle the underlyintg attributes, serialization and user
        interface for you.It is important to call this method whenever
        the shader parameters are modified (including at load time).This
        is an optional method - shader implementations are still free to
        manage uniform (i.e. shader-level) parameters independently if
        they wish.

        Returns:
        -----
        None

        Parameters:
        -----
        parameters: MUniformParameterList
        	[in] -> the list of uniform parameters for this shader 

        remapCurrentValues: bool
        	[in] -> if true (the default), Maya will attempt to initialise the value of new parameters based on any equivalently named parameters that currently exist on the node. Otherwise, the parameters will be setup using default values. Unless you wish to forcibly reset parameter values, the default value of true should be used. 

        dagModifier: MDagModifier
        	[in] -> an optional DG modifier to use when managing the attributes used to represent the geometry parameters on this shader.


        '''
        pass

    def render(self, iterator: MGeometryList): 
        '''
        render(self, iterator: MGeometryList)

        Synopsis
        -----
        Override this method to render geometry using your hardware
        shader. It is important to note that you can only access surface
        data (e.g. uv sets) that you specified in populateRequirements.
        Any data you did not ask for is unlikely to be available in the
        geometry cache passed to you.For example:

        Returns:
        -----
        None

        Parameters:
        -----
        iterator: MGeometryList
        	[in] -> an iterator containing the geometry items you need to render.


        '''
        pass

    def transparencyOptions(self): 
        '''
        transparencyOptions(self) -> int

        Synopsis
        -----
        This method returns transparency options for usage as hints for
        Maya's internal draw during a given rendering pass. Parameters
        are returned via an integer containing masked out bits. By
        default the mask is set to 0, meaning that the drawing should be
        treated as regular opaque object drawing. This will generally
        mean one call per draw pass.Options to control transparency are
        specified by returning one or more masks specified by the
        TransparencyOptions enumeration :Note : Setting the
        "hasTransparency()" method to true will override this method.
        This is for backward compatibility with behaviour on existing
        hardware shader nodes. It is recommended that shaders use the
        "transparencyOptions()" override, and not longer use the older
        "hasTransparency()" override from their shader classes.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def profile(self): 
        '''
        profile(self) -> const MRenderProfile&

        Synopsis
        -----
        Override this method to specify the renderers your shader
        supports. If this method is not overridden, Maya will assume your
        shader supports only Maya's iternal OpenGL based renderer.Note
        that this method is called inside the rendering loop and as such,
        you should make this method as fast as possible - typically just
        returning a static/precalculated value.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def renderSwatchImage(self, image: MImage): 
        '''
        renderSwatchImage(self, image: MImage)

        Synopsis
        -----
        If the shader specifies to override swatch rendering, then this
        method must be overridden in order to draw anything into a
        swatch. The shader will only draw a swatch if it has been
        registered to do so, by providing a valid classification during
        MFnPlugin::registerNode(). The shader should provide a
        classification that defines a swatch rendering node such as : "sh
        ader/surface/utility/:drawdb/shader/surface/myCustomShader:swatch
        /myCustomShaderSwatchGenerator" and have
        "myCustomShaderSwatchGenerator" registered has a swatch renderer
        : MSwatchRenderRegister::registerSwatchRender("myCustomShaderSwat
        chGenerator", MHWShaderSwatchGenerator::createObj );The default
        implementation is to draw nothing. The basic logic to draw a
        swatch is as follows:

        Returns:
        -----
        None

        Parameters:
        -----
        image: MImage
        	[in] -> 


        '''
        pass

    def findResource(self, name: MString,
                        shaderPath: MString,
                        status: MPxHardwareShader.MStatus): 
        '''
        findResource(self, name: MString,
                        shaderPath: MString,
                        status: MPxHardwareShader.MStatus) -> MString

        Synopsis
        -----
        This is a static utility to find the full path to a shader
        resource (typically a texture). This method will search the list
        of paths in the MAYA_HW_SHADER_RESOURCE_PATH environment
        variable, resolving relative paths based on the directory
        containing the shader.

        Returns: 
        ----- 
        The full path of the resource (e.g.
        "C:/shaders/textures/normals.dds")

        Parameters:
        -----
        name: MString
        	[in] -> The name of the resource to look for (e.g. "normals.dds") 

        shaderPath: MString
        	[in] -> The full path to the current shader (e.g. "C:/shaders/myshader.fx") 

        status: MPxHardwareShader.MStatus
        	[in] -> If a pointer to a status is provided, the status will be set to MS::kSuccess if the resource was found, and MS::kFailure otherwise.


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

class TransparencyOptions:
    '''Transparency option bitmasks. 
    Non-functional class.  Values for this enum:
    kIsTransparent
    kNoTransparencyFrontBackCull
    kNoTransparencyPolygonSort
    '''

    def __init__(self):
        pass

    def kIsTransparent(self):
        '''This is an enum of TransparencyOptions.
        - Description: When set means draw transparent. 
        - Value: 1
        '''
        pass

    def kNoTransparencyFrontBackCull(self):
        '''This is an enum of TransparencyOptions.
        - Description: When set means ignore front back cull. 
        - Value: 2
        '''
        pass

    def kNoTransparencyPolygonSort(self):
        '''This is an enum of TransparencyOptions.
        - Description: When set means ignore polygon sorting. 
        - Value: 4
        '''
        pass

class MPxHwShaderNode:
    '''Base class for user defined hardware shaders.
MPxHwShaderNode allows the creation of user-defined hardware shaders. A hardware
shader allows the plug-in writer to control the on-screen display
of an object in Maya.
You must derive a hardware shader node from
MPxHwShaderNode for it to have any affect on the on-screen display at all. In
addition to their affect on the on-screen display of objects,
hardware shaders function as surface shader nodes. This allows
you to connect any shading network up to the hardware shader's
outColor attribute to handle the shading during a software
render.
To create a working hardware shader, derive from this class and
override the
bind(),
unbind(), and
geometry() methods. If your hardware shader uses texture coordinates from
Maya, you also need to override either texCoordsPerVertex or
getTexCoordSetNames(). The other methods of the parent class
MPxNode may also be overridden to perform dependency node capabilities.
NOTE: Plug-in hardware shaders are fully supported for polygonal
mesh shapes. NURBS surfaces are only supported in the High
Quality Interactive viewport and Hardware Renderer if the
glBind/glGeometry/glUnbind methods of this class are implemented.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MPxNode.MPxNode

        Synopsis
        -----
        This method returns the type of the node. This method should not
        be overridden by the user. It will return
        MPxNode::kHwShaderNode.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def bind(self, request: MDrawRequest,
                        view: M3dView): 
        '''
        bind(self, request: MDrawRequest,
                        view: M3dView)

        Synopsis
        -----
        This method is invoked for hardware rendering to Maya's 3D view.
        This is the preferred method of interactive feedback and
        performance. the "gl" version should be used for batch hardware
        rendering.This method is called to set up the OpenGL state. It
        would typically ensure that textures were bound and that any
        specific OpenGL extensions are enabled. A status code of
        MS::kSuccess should be returned unless there was a problem during
        the display, such as insufficient memory or required input data
        is missing or invalid.

        Returns:
        -----
        None

        Parameters:
        -----
        request: MDrawRequest
        	[in] -> the draw request. 

        view: M3dView
        	[in] -> the view in which to draw.


        '''
        pass

    def unbind(self, request: MDrawRequest,
                        view: M3dView): 
        '''
        unbind(self, request: MDrawRequest,
                        view: M3dView)

        Synopsis
        -----
        This method is invoked for hardware rendering to Maya's 3D view.
        This is the preferred method of interactive feedback and
        performance. the "gl" version should be used for batch hardware
        rendering.This method is called to restore the OpenGL state.
        Specifically, it must disable any OpenGL extensions that the
        matching bind() method may have enabled. This is necessary to
        ensure that the rest of Maya's drawing code continues to work
        correctly. A status code of MS::kSuccess should be returned
        unless there was a problem such as insufficient memory or
        required input data is missing or invalid.The arguments passed to
        this method are the same ones that were passed to the bind()
        method.

        Returns:
        -----
        None

        Parameters:
        -----
        request: MDrawRequest
        	[in] -> the draw request. 

        view: M3dView
        	[in] -> the view in which to draw.


        '''
        pass

    def geometry(self, request: MDrawRequest,
                        view: M3dView,
                        prim: int,
                        writable: int,
                        indexCount: int,
                        indexArray: int,
                        vertexCount: int,
                        vertexIDs: int,
                        vertexArray: float,
                        normalCount: int,
                        normalArrays: floatArrayPtr,
                        colorCount: int,
                        colorArrays: floatArrayPtr,
                        texCoordCount: int,
                        texCoordArrays: floatArrayPtr,
                        faceIDs: int,
                        localUVCoord: float): 
        '''
        geometry(self, request: MDrawRequest,
                        view: M3dView,
                        prim: int,
                        writable: int,
                        indexCount: int,
                        indexArray: int,
                        vertexCount: int,
                        vertexIDs: int,
                        vertexArray: float,
                        normalCount: int,
                        normalArrays: floatArrayPtr,
                        colorCount: int,
                        colorArrays: floatArrayPtr,
                        texCoordCount: int,
                        texCoordArrays: floatArrayPtr,
                        faceIDs: int,
                        localUVCoord: float)

        Synopsis
        -----
        This method is invoked for hardware rendering to Maya's 3D view.
        This is the preferred method of interactive feedback and
        performance. the "gl" version should be used for batch hardware
        rendering.This method does all the actual OpenGL drawing. The
        arguments contain all the data to successfully call
        glDrawElements or glDrawRangeElements. It is possible that there
        will be multiple calls to this method surrounded by a single call
        to bind() and unbind().Note 1. The array of vertex IDs passed in
        corresponds to each triangle's vertex. This allows access to
        associated blind data per vertex. The vertexIDs array allows
        querying of information such as color per vertex etc.The array of
        face IDs passed in can be used to query information at a per face
        level.The array of local uv coords passed in stores the local uv
        of the subdivided face vertices.Note 2. The array of array
        parameters passed to this method can contain sparse information.
        Check array positions against NULL to ensure that the array
        information item is valid.It is necessary to use the indexArray
        to access information contained in the data arrays.

        Returns:
        -----
        None

        Parameters:
        -----
        request: MDrawRequest
        	[in] -> the draw request. 

        view: M3dView
        	[in] -> the view in which to draw. 

        prim: int
        	[in] -> the type of primitive to draw. This is one of the values accepted by glBegin(). Typically it will be GL_TRIANGLES but it could be any of the others. 

        writable: int
        	[in] -> this is a mask which indicates which of the various array arguments can be modified in place. If a bit in writable is set then you can modify corresponding data array (after casting it to a non-const type). If the bit is not set in writable then you must 

        indexCount: int
        	[in] -> specifies both the number of indices to draw and the size of the indexArray argument. 

        indexArray: int
        	[in] -> the array of index values. This array is in a format suitable for passing as the indices argument to 

        vertexCount: int
        	[in] -> the number of elements in the vertexArray, the normalArray, each of the colorArrays, and each of the texCoordArrays, the vertexID, the faceID and the localUVCoord array. The array length is (vertexCount * the size of the type of data). e.g. vertexCount*3 for vertexArray, and vertexCount*1 for vertexID. 

        vertexIDs: int
        	[in] -> the component IDs of the vertices in vertexArray. This array is only provided if it was requested by overriding the 

        vertexArray: float
        	[in] -> the array of vertex data. Currently, this is always 3 element floating point values. This data is in a format suitable for passing to 

        normalCount: int
        	[in] -> the number of individual "normal" arrays that are being provided in normalArrays. See the description of normalsPerVertex method below for details. 

        normalArrays: floatArrayPtr
        	[in] -> the normal (and tangent) data suitable. There may be 0, 1, 2, or 3 "normal" arrays. See the description of the normalsPerVertex method below for details. 

        colorCount: int
        	[in] -> the number of individual color arrays. 

        colorArrays: floatArrayPtr
        	[in] -> the arrays of color data. The first set of color data is pointed to by colorArrays[0]. Each color array contains vertexCount color values, each of which is 4 floating point values long and represents the red, green, blue, and alpha values on a 0 to 1 scale. Each individual array is suitable for passing to 

        texCoordCount: int
        	[in] -> the number of texture coordinate arrays. Each array contains one set of UV texture coordinates. 

        texCoordArrays: floatArrayPtr
        	[in] -> the arrays of texture coordinate data. The first set of texture coordinate data is pointed to by texCoordArrays[0]. Each array contains vertexCount coordinate values, each of which is 2 floating point values long. Each individual array is suitable for passing to 

        faceIDs: int
        	[in] -> the component IDs of the faces in vertexArray. This array is only provided if it was requested by overriding the 

        localUVCoord: float
        	[in] -> the local uv of the smooth vertices in vertexArray. This array is only provided if it was requested by overriding the 


        '''
        pass

    def glBind(self, shapePath: MDagPath): 
        '''
        glBind(self, shapePath: MDagPath)

        Synopsis
        -----
        This method should only be overridden for hardware rendering. The
        implementation can assume the graphics context and model view
        projection matrix have already been set.This method will be
        invoked once per frame and should be overridden to allocate any
        resources needed for the draw. For example, binding vertex
        programs, fragment programs, or allocating textures. A status
        code of MS::kSuccess should be returned unless there was a
        problem such as insufficient memory or required input data is
        missing or invalid.

        Returns:
        -----
        None

        Parameters:
        -----
        shapePath: MDagPath
        	[in] -> Path to the surface being drawn.


        '''
        pass

    def glUnbind(self, shapePath: MDagPath): 
        '''
        glUnbind(self, shapePath: MDagPath)

        Synopsis
        -----
        This method should only be overridden for hardware rendering. The
        implementation can assume the graphics context and model view
        projection matrix have already been set.This method will be
        invoked once per frame and should be overridden to deallocate any
        resources used to draw. It's important that all resources be
        released when a batch hardware render has occured because the
        graphics context will be deleted. It may be desireable to
        override the other version of bind/unbind to keep track of
        whether the draw is for the 3D view or the batch hardware
        renderer. This information could then be used to better track the
        reuse of resources and optimize performance.A status code of
        MS::kSuccess should be returned unless there was a problem.

        Returns:
        -----
        None

        Parameters:
        -----
        shapePath: MDagPath
        	[in] -> Path to the surface being drawn.


        '''
        pass

    def glGeometry(self, shapePath: MDagPath,
                        prim: int,
                        writable: int,
                        indexCount: int,
                        indexArray: int,
                        vertexCount: int,
                        vertexIDs: int,
                        vertexArray: float,
                        normalCount: int,
                        normalArrays: floatArrayPtr,
                        colorCount: int,
                        colorArrays: floatArrayPtr,
                        texCoordCount: int,
                        texCoordArrays: floatArrayPtr,
                        faceIDs: int,
                        localUVCoord: float): 
        '''
        glGeometry(self, shapePath: MDagPath,
                        prim: int,
                        writable: int,
                        indexCount: int,
                        indexArray: int,
                        vertexCount: int,
                        vertexIDs: int,
                        vertexArray: float,
                        normalCount: int,
                        normalArrays: floatArrayPtr,
                        colorCount: int,
                        colorArrays: floatArrayPtr,
                        texCoordCount: int,
                        texCoordArrays: floatArrayPtr,
                        faceIDs: int,
                        localUVCoord: float)

        Synopsis
        -----
        This method should only be overridden for hardware rendering. The
        implementation can assume graphics context and model view
        projection matrix have already been set.This method does all the
        actual OpenGL drawing. The arguments contain all the data to
        successfully call glDrawElements or glDrawRangeElements. It is
        possible that there will be multiple calls to this method
        surrounded by a single call to bind() and unbind().Note 1.  The
        array of vertex IDs passed in corresponds to each triangle's
        vertex. This allows access to associated blind data per vertex.
        The vertexIDs array allows querying of information such as color
        per vertex etc.The array of face IDs passed in can be used to
        query information at a per face level.The array of local uv
        coords passed in stores the local uv of the subdivided face
        vertices.Note 2.  The array of array parameters passed to this
        method can contain sparse information. Check array positions
        against NULL to ensure that the array information item is
        valid.It is necessary to use the indexArray to access information
        contained in the data arrays.

        Returns:
        -----
        None

        Parameters:
        -----
        shapePath: MDagPath
        	[in] -> Path to the surface being drawn. 

        prim: int
        	[in] -> the type of GL primitive is supplied as it would be used for glBegin() or glDrawElements(). Typically it will be GL_TRIANGLES or GL_TRIANGLE_STRIP for drawing polygonal or nurb surfaces respectively. 

        writable: int
        	[in] -> this is a mask which indicates which of the various array arguments can be modified in place. If a bit in writable is set then you can modify corresponding data array (after casting it to a non-const type). If the bit is not set in writable then you must 

        indexCount: int
        	[in] -> specifies both the number of indices to draw and the size of the indexArray argument. 

        indexArray: int
        	[in] -> the array of index values. This array is in a format suitable for passing as the indices argument to 

        vertexCount: int
        	[in] -> the number of elements in the vertexArray, the normalArray, each of the colorArrays, each of the texCoordArrays, the vertexID, the faceID and the localUVCoord array. The array length is (vertexCount * the size of the type of data). e.g. vertexCount*3 for vertexArray, and vertexCount*1 for vertexID. 

        vertexIDs: int
        	[in] -> the component IDs of the vertices in vertexArray. This array is only provided if it was requested by overriding the 

        vertexArray: float
        	[in] -> the array of vertex data. Currently, this is always 3 element floating point values. This data is in a format suitable for passing to 

        normalCount: int
        	[in] -> the number of individual "normal" arrays that are being provided in normalArrays. See the description of normalsPerVertex method below for details. 

        normalArrays: floatArrayPtr
        	[in] -> the normal (and tangent) data suitable. There may be 0, 1, 2, or 3 "normal" arrays. See the description of the normalsPerVertex method below for details. 

        colorCount: int
        	[in] -> the number of individual color arrays. 

        colorArrays: floatArrayPtr
        	[in] -> the arrays of color data. The first set of color data is pointed to by colorArrays[0]. Each color array contains vertexCount color values, each of which is 4 floating point values long and represents the red, green, blue, and alpha values on a 0 to 1 scale. The 3D view and hardware renderer handle missing color data differently. The 3D view will create an array and pass black colors for each vertex, whereas the hardware renderer will supply a NULL pointer to indicate that color per-vertex data is unavailable. 

        texCoordCount: int
        	[in] -> the number of texture coordinate arrays. Each array contains one set of UV texture coordinates. 

        texCoordArrays: floatArrayPtr
        	[in] -> the arrays of texture coordinate data. The first set of texture coordinate data is pointed to by texCoordArrays[0]. Each array contains vertexCount coordinate values, each of which is 2 floating point values long. Each individual array is suitable for passing to 

        faceIDs: int
        	[in] -> the component IDs of the faces in vertexArray. This array is only provided if it was requested by overriding the 

        localUVCoord: float
        	[in] -> the local uv of the smooth vertices in vertexArray. This array is only provided if it was requested by overriding the 


        '''
        pass

    def supportsBatching(self): 
        '''
        supportsBatching(self) -> bool

        Synopsis
        -----
        Specifies whether or not this shader supports batched rendering
        of shapes. In normal rendering, a shader is invoked using
        bind/geometry/unbind (or glBind/glGeometry/glUnbind) once for
        each shape being rendered. When a shader is used in batched
        rendering mode however, bind is called once, a series of geometry
        calls are made for each shape being rendered, followed by a
        single call to unbind (and similarly for glBind, glGeometry and
        glUnbind). As shader binding/unbinding can be expensive, batched
        rendering can significantly improve rendering performance. The
        more (particularly expensive) operations that can be moved out of
        the geometry/glGeometry methods the greater the performance
        improvement is. Ideally, only shape specific operations (such as
        binding geometry arrays and shape matrices) should be left in the
        geometry methods.It is important to note that your shader can
        only use batched rendering mode if there is no shape (i.e. dag
        path) specific code in bind, glBind, unbind, or glUnbind. If any
        of these methods perform shape specific processing, this code
        must either be moved into geometry/glGeometry, or you must return
        false in this method to indicate batching should be disabled for
        this shader.By default, this method will return false to ensure
        compatibility with existing shader code.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def invertTexCoords(self): 
        '''
        invertTexCoords(self) -> bool

        Synopsis
        -----
        Specifies whether this shader requires inverted texture
        coordinates. (i.e. where the top-left hand corner of UV space is
        (0,0) instead of the bottom-left corner).By default, this method
        will return false to ensure compatibility with existing shader
        code.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def currentPath(self): 
        '''
        currentPath(self) -> const MDagPath&

        Synopsis
        -----
        This method returns a reference to the current path that the
        shader is invoked for. The path is only valid before a call to
        any of the attribute specifying routines:The path is not
        guaranteed to be valid at any other time.This method allows the
        plugin to return attribute queries which are relative to a
        specific path or object.For example, the plugin can retrieve the
        MObject from the path, then use the MFnMesh class on the MObject,
        assuming the object is a polygonal surface. Through MFnMesh the
        code can query the actual number of texture coordinate sets on
        the surface and return appropriate values for the
        getTexCoordSetNames() routine.The [gl]bind(), [gl]unbind() and
        [gl]geometry() routines already have access to a dag path which
        is the same path as the one which can be retrieved via this
        method.For performance reasons, it is recommended that for those
        methods the MDagPath passed in as an argument should be used.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def dirtyMask(self): 
        '''
        dirtyMask(self) -> int

        Synopsis
        -----
        This method returns a "dirty" mask that indicates which geometry
        items have changed from the last invocation of the plugin to
        draw. The mask is valid at the time that geometry() or
        glGeometry() is called and at no other time.Note that this mask
        is relative to the geometry for the current object (path) being
        drawn by the shader. The current path is the MDagPath argument
        passed in via the geometry routines.In general the mask will mark
        the geometry as not being dirty.Scenarios where the geometry will
        be marked dirty include:

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def normalsPerVertex(self): 
        '''
        normalsPerVertex(self) -> int

        Synopsis
        -----
        Specifies how many normals per vertex the HW shader would like
        Maya to provide. This can range from 0 to 3. The first normal is
        the surface normal. The second "normal" is the primary tangent
        (generally the "u" direction). The third "normal" is the
        secondary tangent or the binormal (generally the "v" direction).
        Together, the normal, tangent and binormal form an orthogonal
        basis frequently named "tangent space basis".The tangent and
        binormal vectors are guaranteed to be normalized and orthogonal
        to the surface normal. Please note that extracting the tangent
        and/or binormal requires expensive calculations, that will slow
        down refresh time substantially. In a future version, Maya may
        cache the resulting tangent space basis; in the meantime, only
        ask for more than one normal per vertex if they are absolutely
        required.Also note that the tangent and binormal calculation
        requires a uv map. Currently, they are always computed from the
        first available uv map; if there is no uv mapping on the surface,
        Maya will only provide surface normals in the geometry call,
        regardless of the value returned by normalsPerVertex().If you do
        not override this method, Maya will provide 1 normal per
        vertex.Maya will automatically and silently clamp the result of
        this function to the [0,3] range.COMPATIBILITY NOTE: Automatic
        tangent space basis calculation is only supported starting with
        Maya 4.0.1. Maya 4.0 supported a different scheme that was much
        more complicated and no longer supported.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def colorsPerVertex(self): 
        '''
        colorsPerVertex(self) -> int

        Synopsis
        -----
        This method returns the number of color values per vertex that
        the hw shader node would like to receive from Maya. Maya will
        attempt to provide all the color data that the shader would like
        but it will never provide more data that is actually available in
        the shape. The color sets returned by getColorSetNames() will
        override the number of color sets specified by colorsPerVertex().
        If you do not override this method or getColorSetNames(), Maya
        will provide no colors per vertex.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def texCoordsPerVertex(self): 
        '''
        texCoordsPerVertex(self) -> int

        Synopsis
        -----
        This method returns the number of texture coordinate values per
        vertex that the hw shader node would like to receive from Maya.
        Maya will attempt to provide all the texture coordinate data that
        the shader would like but it will never provide more data than is
        actually available in the shape. The uv sets returned by
        getTexCoordSetNames() will override the number of uv sets
        specified by texCoordsPerVertex(). If you do not override this
        method or getTexCoordSetNames(), Maya will provide no texture
        coordinates per vertex.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def hasTransparency(self): 
        '''
        hasTransparency(self) -> bool

        Synopsis
        -----
        This method returns a boolean value that indicates whether the
        object will be drawn transparently or not. Transparent objects
        must be drawn after all the opaque objects in the scene or they
        will not display correctly. Maya uses the return value to
        determine when it can draw this shape.Note : The functionality in
        this method has been subsumed by the transparencyOptions()
        method. It is recommended that shader node writers use this newer
        method as it provides greater control over how transparency is
        interpreted by Maya's refresh mechanism.For backward
        compatibility, if this method is specified and returns a "true"
        value, it will override the transparencyOptions() method.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def provideVertexIDs(self): 
        '''
        provideVertexIDs(self) -> bool

        Synopsis
        -----
        This method returns a boolean value that indicates whether a map
        of the vertex IDs will be provided to the geometry method.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def provideFaceIDs(self): 
        '''
        provideFaceIDs(self) -> bool

        Synopsis
        -----
        This method returns a boolean value that indicates whether a map
        of the face IDs will be provided to the geometry method.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def provideLocalUVCoord(self): 
        '''
        provideLocalUVCoord(self) -> bool

        Synopsis
        -----
        This method returns a boolean value that indicates whether the
        local uv coordinates of the subdivided face vertices will be
        provided to the geometry method.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def transparencyOptions(self): 
        '''
        transparencyOptions(self) -> int

        Synopsis
        -----
        This method returns transparency options for usage as hints for
        Maya's internal draw during a given rendering pass. Parameters
        are returned via an integer containing masked out bits. By
        default the mask is set to 0, meaning that the drawing should be
        treated as regular opaque object drawing. This will generally
        mean one call per draw pass.Options to control transparency are
        specified by returning one or more masks specified by the
        TransparencyOptions enumeration :Note : Setting the
        "hasTransparency()" method to true will override this method.
        This is for backward compatibility with behaviour on existing
        hardware shader nodes. It is recommended that shaders use the
        "transparencyOptions()" override, and not longer use the older
        "hasTransparency()" override from their shader classes.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def renderSwatchImage(self, image: MImage): 
        '''
        renderSwatchImage(self, image: MImage)

        Synopsis
        -----
        If the shader specifies to override swatch rendering, then this
        method must be overridden in order to draw anything into a
        swatch. The shader will only draw a swatch if it has been
        registered to do so, by providing a valid classification during
        MFnPlugin::registerNode(). The shader should provide a
        classification that defines a swatch rendering node such as : "sh
        ader/surface/utility/:drawdb/shader/surface/myCustomShader:swatch
        /myCustomShaderSwatchGenerator" and have
        "myCustomShaderSwatchGenerator" registered has a swatch renderer
        : MSwatchRenderRegister::registerSwatchRender("myCustomShaderSwat
        chGenerator", MHWShaderSwatchGenerator::createObj );The default
        implementation is to draw nothing. The basic logic to draw a
        swatch is as follows:

        Returns:
        -----
        None

        Parameters:
        -----
        image: MImage
        	[in] -> 


        '''
        pass

    def currentShadingEngine(self): 
        '''
        currentShadingEngine(self) -> MObject

        Synopsis
        -----
        This method returns an MObject to the shading engine that is
        currently being rendered. This method will only return a valid
        MObject during the following calls:

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

class Writeable:
    '''Bit masks used in conjuction with the 'writeable' parameter passed to the geometry() method to determine which arrays the shader is allowed to write to. 
    Non-functional class.  Values for this enum:
    kWriteNone
    kWriteVertexArray
    kWriteNormalArray
    kWriteColorArrays
    kWriteTexCoordArrays
    kWriteAll
    '''

    def __init__(self):
        pass

    def kWriteNone(self):
        '''This is an enum of Writeable.
        - Description:  
        - Value: 0
        '''
        pass

    def kWriteVertexArray(self):
        '''This is an enum of Writeable.
        - Description:  
        - Value: 1
        '''
        pass

    def kWriteNormalArray(self):
        '''This is an enum of Writeable.
        - Description:  
        - Value: 2
        '''
        pass

    def kWriteColorArrays(self):
        '''This is an enum of Writeable.
        - Description:  
        - Value: 4
        '''
        pass

    def kWriteTexCoordArrays(self):
        '''This is an enum of Writeable.
        - Description:  
        - Value: 8
        '''
        pass

    def kWriteAll(self):
        '''This is an enum of Writeable.
        - Description:  
        - Value: 15
        '''
        pass

class DirtyMask:
    '''Bit masks used in combination with the return value of the dirtyMask() method to determine which portions of the geometry are dirty. 
    Non-functional class.  Values for this enum:
    kDirtyNone
    kDirtyVertexArray
    kDirtyNormalArray
    kDirtyColorArrays
    kDirtyTexCoordArrays
    kDirtyAll
    '''

    def __init__(self):
        pass

    def kDirtyNone(self):
        '''This is an enum of DirtyMask.
        - Description:  
        - Value: 0
        '''
        pass

    def kDirtyVertexArray(self):
        '''This is an enum of DirtyMask.
        - Description:  
        - Value: 1
        '''
        pass

    def kDirtyNormalArray(self):
        '''This is an enum of DirtyMask.
        - Description:  
        - Value: 2
        '''
        pass

    def kDirtyColorArrays(self):
        '''This is an enum of DirtyMask.
        - Description:  
        - Value: 4
        '''
        pass

    def kDirtyTexCoordArrays(self):
        '''This is an enum of DirtyMask.
        - Description:  
        - Value: 8
        '''
        pass

    def kDirtyAll(self):
        '''This is an enum of DirtyMask.
        - Description:  
        - Value: 15
        '''
        pass

class TransparencyOptions:
    '''Bit masks to be returned by the shader's transparencyOptions() method. 
    Non-functional class.  Values for this enum:
    kIsTransparent
    kNoTransparencyFrontBackCull
    kNoTransparencyPolygonSort
    '''

    def __init__(self):
        pass

    def kIsTransparent(self):
        '''This is an enum of TransparencyOptions.
        - Description: Draw as a transparent object. If this bit is not set then the others are ignored. 
        - Value: 1
        '''
        pass

    def kNoTransparencyFrontBackCull(self):
        '''This is an enum of TransparencyOptions.
        - Description: Do not use the two-pass front-and-back culling algorithm. 
        - Value: 2
        '''
        pass

    def kNoTransparencyPolygonSort(self):
        '''This is an enum of TransparencyOptions.
        - Description: Do not use two-pass drawing of back-to-front sorted polygons. 
        - Value: 4
        '''
        pass

class MPxIkSolverNode:
    '''Base class for user defined IK solvers.
This is the base class for writing user-defined IK solvers. Users
must at least override the following methods in order to write a
solver:
Users can optionally override the following methods if they want
to perform work before or after
 is called:
Since Maya 2018, users no longer need to call the base class
version of these functions if overriding them.
Note that the following virtual methods (declared in
MPxNode) are irrelevant for the
MPxIkSolverNode. If these methods are overridden in a class derived from
MPxIkSolverNode, they will be ignored.
A creator method is necessary to return an instance of the user
solver:
In order to create and register the solver, execute the mel
command:
Once the solver is registered it can be assigned to IK handles
and its solve methods will be called in the same manner as the
solvers within Maya.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MPxNode.MPxNode

        Synopsis
        -----
        This method returns the type of the node. This method should not
        be overridden by the user. It will return
        MPxNode::kIkSolverNode.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def preSolve(self): 
        '''
        preSolve(self)

        Synopsis
        -----
        This method is called before doSolve. Users should override this
        method if there is any preprocessing that needs to be done before
        solving.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def doSolve(self): 
        '''
        doSolve(self)

        Synopsis
        -----
        This is where the main solving takes place. The user must
        override this method.The purpose of this method is to calculate
        joint angles in a skeleton based upon the position of the end
        effector of the handle associated with this solver.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def postSolve(self, stat: MPxIkSolverNode.MStatus): 
        '''
        postSolve(self, stat: MPxIkSolverNode.MStatus)

        Synopsis
        -----
        This method is called after doSolve has finished. The user should
        override this method if there are any post calculations to be
        done.The status argument indicates whether doSolve was
        successful.

        Returns:
        -----
        None

        Parameters:
        -----
        stat: MPxIkSolverNode.MStatus
        	[out] -> The status returned from 


        '''
        pass

    def solverTypeName(self): 
        '''
        solverTypeName(self) -> MString

        Synopsis
        -----
        This method returns the type name of the solver. The user must
        override this method in order for the solver to be identifiable
        when it is registered.Once the solver is registered, the type
        name can be used to assign the solver to an IK handle.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def rotatePlane(self, ReturnStatus: MPxIkSolverNode.MStatus): 
        '''
        rotatePlane(self, ReturnStatus: MPxIkSolverNode.MStatus) -> bool

        Synopsis
        -----
        This method indicates whether this solver supports the rotate
        plane. Solvers that support the rotate plane allow the user to
        manipulate the IK handle's pole vector with the rotate plane
        manipulators.

        Returns: 
        ----- 
        Boolean value: true if the solver supports the rotate plane,
        false otherwise.

        Parameters:
        -----
        ReturnStatus: MPxIkSolverNode.MStatus
        	[in] -> Status code.


        '''
        pass

    def setRotatePlane(self, rotatePlane: bool): 
        '''
        setRotatePlane(self, rotatePlane: bool)

        Synopsis
        -----
        This method sets whether or not this solver supports the rotate
        plane. Solvers that support the rotate plane allow the user to
        manipulate the IK handle's pole vector with the rotate plane
        manipulators.

        Returns:
        -----
        None

        Parameters:
        -----
        rotatePlane: bool
        	[in] -> whether or not the solver supports the rotate plane


        '''
        pass

    def singleChainOnly(self, ReturnStatus: MPxIkSolverNode.MStatus): 
        '''
        singleChainOnly(self, ReturnStatus: MPxIkSolverNode.MStatus) -> bool

        Synopsis
        -----
        This method indicates whether this solver is a single chain
        solver. Single chain solvers are solvers which act on one handle
        only, i.e. the handle groups have only one handle if they are for
        single chain solvers.

        Returns: 
        ----- 
        Boolean value: true if the solver is a single chain solver, false
        otherwise.

        Parameters:
        -----
        ReturnStatus: MPxIkSolverNode.MStatus
        	[in] -> Status code.


        '''
        pass

    def setSingleChainOnly(self, singleChainOnly: bool): 
        '''
        setSingleChainOnly(self, singleChainOnly: bool)

        Synopsis
        -----
        This method sets whether or not this solver is a single chain
        solver. Single chain solvers are solvers which act on one handle
        only, i.e. the handle groups have only one handle if they are for
        single chain solvers.

        Returns:
        -----
        None

        Parameters:
        -----
        singleChainOnly: bool
        	[in] -> whether or not the solver is a single chain solver


        '''
        pass

    def positionOnly(self, ReturnStatus: MPxIkSolverNode.MStatus): 
        '''
        positionOnly(self, ReturnStatus: MPxIkSolverNode.MStatus) -> bool

        Synopsis
        -----
        Indicates whether the ik solution is dependent on the ikHandle
        position only or also uses the orientation.

        Returns: 
        ----- 
        Boolean value: true if the solver does not support handle
        orientation, false otherwise

        Parameters:
        -----
        ReturnStatus: MPxIkSolverNode.MStatus
        	[in] -> Status code.


        '''
        pass

    def setPositionOnly(self, positionOnly: bool): 
        '''
        setPositionOnly(self, positionOnly: bool)

        Synopsis
        -----
        Sets whether or not the solver supports handle orientation.

        Returns:
        -----
        None

        Parameters:
        -----
        positionOnly: bool
        	[in] -> whether or not the solver is positionOnly


        '''
        pass

    def supportJointLimits(self, ReturnStatus: MPxIkSolverNode.MStatus): 
        '''
        supportJointLimits(self, ReturnStatus: MPxIkSolverNode.MStatus) -> bool

        Synopsis
        -----
        This method indicates whether the solver supports limits on joint
        angles.

        Returns: 
        ----- 
        Boolean value. true if the solver supports limits on joint
        angles, false otherwise.

        Parameters:
        -----
        ReturnStatus: MPxIkSolverNode.MStatus
        	[in] -> Status code.


        '''
        pass

    def setSupportJointLimits(self, supportJointLimits: bool): 
        '''
        setSupportJointLimits(self, supportJointLimits: bool)

        Synopsis
        -----
        This method sets whether or not the solver supports limits on
        joint angles.

        Returns:
        -----
        None

        Parameters:
        -----
        supportJointLimits: bool
        	[in] -> whether or not the solver supports joint limits


        '''
        pass

    def uniqueSolution(self, ReturnStatus: MPxIkSolverNode.MStatus): 
        '''
        uniqueSolution(self, ReturnStatus: MPxIkSolverNode.MStatus) -> bool

        Synopsis
        -----
        This method indicates whether the solver provides a unique
        solution.

        Returns: 
        ----- 
        Boolean value: true if the solver provides a unique solution,
        false otherwise.

        Parameters:
        -----
        ReturnStatus: MPxIkSolverNode.MStatus
        	[in] -> Status code.


        '''
        pass

    def setUniqueSolution(self, uniqueSolution: bool): 
        '''
        setUniqueSolution(self, uniqueSolution: bool)

        Synopsis
        -----
        This method sets whether or not the solver provides a unique
        solution.

        Returns:
        -----
        None

        Parameters:
        -----
        uniqueSolution: bool
        	[in] -> whether or not the solver provides a unique solution


        '''
        pass

    def isSingleChainOnly(self): 
        '''
        isSingleChainOnly(self) -> bool

        Synopsis
        -----
        This method indicates whether this solver is a single chain
        solver. Single chain solvers are solvers which act on one handle
        only, i.e. the handle groups have only one handle if they are for
        single chain solvers.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setFuncValueTolerance(self, tolerance: double): 
        '''
        setFuncValueTolerance(self, tolerance: double)

        Synopsis
        -----
        Set the error value for this solver. The user can override this
        if any other calculations should be done here.

        Returns:
        -----
        None

        Parameters:
        -----
        tolerance: double
        	[in] -> Error value


        '''
        pass

    def setMaxIterations(self, value: int): 
        '''
        setMaxIterations(self, value: int)

        Synopsis
        -----
        Set the maximum iterations for a solution by this solver. The
        user can override this if any other calculations should be done
        here.

        Returns:
        -----
        None

        Parameters:
        -----
        value: int
        	[in] -> value to set


        '''
        pass

    def setHandleGroup(self, group: MIkHandleGroup): 
        '''
        setHandleGroup(self, group: MIkHandleGroup)

        Synopsis
        -----
        Set the handle group of this solver.

        Returns:
        -----
        None

        Parameters:
        -----
        group: MIkHandleGroup
        	[in] -> The handle group to be set 


        '''
        pass

    def toWorldSpace(self): 
        '''
        toWorldSpace(self) -> const MMatrix*

        Synopsis
        -----
        Returns the world space matrix for this solver.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def toSolverSpace(self): 
        '''
        toSolverSpace(self) -> const MMatrix*

        Synopsis
        -----
        Returns the local space matrix for this solver.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def funcValueTolerance(self): 
        '''
        funcValueTolerance(self) -> double

        Synopsis
        -----
        Return the error value for this solver.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def maxIterations(self): 
        '''
        maxIterations(self) -> int

        Synopsis
        -----
        Return the the maximum nuber of itertations for a solution by
        this solver.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def snapHandle(self, handle: MObject): 
        '''
        snapHandle(self, handle: MObject)

        Synopsis
        -----
        This function positions the handle at the end effector position.
        The user can override this method.

        Returns:
        -----
        None

        Parameters:
        -----
        handle: MObject
        	[in] -> handle to be set 


        '''
        pass

    def isAttributeCreatedBySolver(self, attr: MObject): 
        '''
        isAttributeCreatedBySolver(self, attr: MObject) -> bool

        Synopsis
        -----
        Introduced in 2019.0 This function returns whether a certain
        attribute on the ikHandle was created by the solver (and
        affecting the result of the solve).

        Returns: 
        ----- 
        True if the attribute is created by the solver and affecting the
        solve

        Parameters:
        -----
        attr: MObject
        	[in] -> attribute to be queried 


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

    def thisMObject(self): 
        '''
        thisMObject(self) -> MObject

        Synopsis
        -----
        Returns the MObject associated with this user defined node. This
        makes it possible to use MFnDependencyNode or to construct plugs
        to this node's attributes.It is not necessary to override this
        method.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MPxImageFile:
    '''Image manipulation.
This class provides methods for reading file images stored on
disk.
The
MPxImageFile class can be used to implement support for new image file
formats in Maya. The implementation is able to support both fixed
and floating point image formats.
MPxImageFile allows custom image formats to be recognized by Maya and any
plug-ins that use Maya's API for accessing images. However be
aware that some third party plugins bypass Maya's API and use
their own internal facilities for accessing images, which means
that they will not recognize MPxImageFile-based image formats.
'''
    def __init__(self):
        pass


    def open(self, pathname: MString,
                        info: MImageFileInfo): 
        '''
        open(self, pathname: MString,
                        info: MImageFileInfo)

        Synopsis
        -----
        Attempt to open the specified file as an image and extract the
        image characteristics. It is important that this function only
        return success if the image is definitely supported by this
        implementation.

        Returns:
        -----
        None

        Parameters:
        -----
        pathname: MString
        	[in] -> the image file to open 

        info: MImageFileInfo
        	[out] -> an optional pointer to the image info structure to fill in. If this pointer is non-NULL, the implementation of this method should parse the image header to populate the information structure.


        '''
        pass

    def load(self, image: MImage,
                        imageNumber: int): 
        '''
        load(self, image: MImage,
                        imageNumber: int)

        Synopsis
        -----
        Load the previously opened image file into an MImage.

        Returns:
        -----
        None

        Parameters:
        -----
        image: MImage
        	[in] -> the image to load the currently open file into 

        imageNumber: int
        	[in] -> the index of image to load (for files containing multiple images)


        '''
        pass

    def glLoad(self, info: MImageFileInfo,
                        imageNumber: int): 
        '''
        glLoad(self, info: MImageFileInfo,
                        imageNumber: int)

        Synopsis
        -----
        Load the previously opened image file as an OpenGL texture. The
        OpenGL texture will already have been bound by the caller of this
        method (i.e. do not call glBind again inside your implementation
        of this method - just use glTexImage2D or equivalent to load the
        texture). The type of texture that has been bound is specified in
        the information structure provided. It is important that your
        implementation verifies this type before loading any data, as
        loading an incompatible type may lead to instability. By
        overriding this method, you can implement non-2D texture support
        (such as cube maps), non-byte texture support (such as float and
        half), and compressed hardware texture support (such as DXT). You
        are free to use any available OpenGL extensions you want to load
        in the texture. While standard Maya shaders will only be able to
        use standard 2D textures, plugin hardware shaders can access
        non-2D textures loaded via this method. If your plugin set
        mipmaps to true at file open time, it is responsible for loading
        or generating the mipmap information inside this method.

        Returns:
        -----
        None

        Parameters:
        -----
        info: MImageFileInfo
        	[in] -> a description of hardware texture to load. 

        imageNumber: int
        	[in] -> the index of image to load (for files containing multiple images)


        '''
        pass

    def close(self): 
        '''
        close(self)

        Synopsis
        -----
        Close the image file.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MPxImagePlane:
    '''Base class for user defined imagePlane nodes.
MPxImagePlane provides you with the ability to write your own image plane
classes. This allows you to support non-standard image data in an
image plane or change the standard behaviour of the image plane.
Note, once you have created a custom image plane and created the
node in a scene. You must attach the image plane to a camera
using the 'imagePlane' attribute on the 'cameraShape'.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MPxNode.MPxNode

        Synopsis
        -----
        Returns the type of node that this is. This is used to
        differentiate user defined nodes that are derived off different
        MPx base classes.It is not necessary to override this
        method.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def loadImageMap(self, fileName: MString,
                        frame: int,
                        image: MImage): 
        '''
        loadImageMap(self, fileName: MString,
                        frame: int,
                        image: MImage)

        Synopsis
        -----
        Override this method to load the file of name fileName into the
        image MImage.

        Returns:
        -----
        None

        Parameters:
        -----
        fileName: MString
        	[in] -> The name of the file to be loaded. 

        frame: int
        	[in] -> The frame number to be displayed. 

        image: MImage
        	[in] -> The image representing the image plane data.


        '''
        pass

    def getExactImageFile(self, refFileName: MString,
                        actualName: MString): 
        '''
        getExactImageFile(self, refFileName: MString,
                        actualName: MString) -> bool

        Synopsis
        -----
        API users can call this method to resolve a file name. Sometimes
        the file path specified by the user node are relative or contain
        environment variables that require expansion. Also
        getExactImageFile() will try to find the image file sequence if
        use sequence is on. API users do not have to call this method,
        and it is only provided for convienence purposes. The full path
        name will be returned in actualName.Python NotesThis method is
        not supported in Python, see exactImageFile() instead

        Returns: 
        ----- 
        true The file was found and the file name was expanded.  false
        The file was not found and the file name was not expanded.

        Parameters:
        -----
        refFileName: MString
        	[in] -> The file name to be expanded 

        actualName: MString
        	[in] -> The exact file name.


        '''
        pass

    def exactImageFile(self, refFileName: MString): 
        '''
        exactImageFile(self, refFileName: MString) -> MString

        Synopsis
        -----
        API users can call this method to resolve a file name. Sometimes
        the file path specified by the user node are relative or contain
        environment variables that require expansion. Also
        getExactImageFile() will try to find the image file sequence if
        use sequence is on. API users do not have to call this method,
        and it is only provided for convienence purposes. The full path
        name will be returned in actualName.

        Returns: 
        ----- 
        String containing the image file name, will be empty string on
        failure

        Parameters:
        -----
        refFileName: MString
        	[in] -> The file name to be expanded


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

    def thisMObject(self): 
        '''
        thisMObject(self) -> MObject

        Synopsis
        -----
        Returns the MObject associated with this user defined node. This
        makes it possible to use MFnDependencyNode or to construct plugs
        to this node's attributes.It is not necessary to override this
        method.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def imageName(self): 
        '''
        imageName(self) -> MObject

        Synopsis
        -----
        The file name of the image to be used in the image plane. Only
        used if Type is set to Image File.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def useFrameExtension(self): 
        '''
        useFrameExtension(self) -> MObject

        Synopsis
        -----
        When this is on, the system will substitute the frame number in
        the Image Name with the number from the Frame Extension attribute
        (see below).

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def coverageOrigin(self): 
        '''
        coverageOrigin(self) -> MObject

        Synopsis
        -----
        Controls the lower-left-corner of the area of the input image
        that will be used on the image plane.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def sourceTexture(self): 
        '''
        sourceTexture(self) -> MObject

        Synopsis
        -----
        If the Type attribute is set to Texture, then this attribute is
        connected to the texture node used by the image plane.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def displayMode(self): 
        '''
        displayMode(self) -> MObject

        Synopsis
        -----
        Controls how the image plane will be displayed both in the 3d
        view, and when rendered.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def displayOnlyIfCurrent(self): 
        '''
        displayOnlyIfCurrent(self) -> MObject

        Synopsis
        -----
        If enabled, you will only see the image plane when you are
        looking through the camera that the plane is attached to.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def offset(self): 
        '''
        offset(self) -> MObject

        Synopsis
        -----
        Controls how much the center of the image plane is offset from
        the centre of the viewing frustum of the camera.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def center(self): 
        '''
        center(self) -> MObject

        Synopsis
        -----
        Controls the world-space position of the center of the image
        plane.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def visibleInReflections(self): 
        '''
        visibleInReflections(self) -> MObject

        Synopsis
        -----
        When ray tracing, controls whether the image plane will sppear in
        reflected surfaces.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def visibleInRefractions(self): 
        '''
        visibleInRefractions(self) -> MObject

        Synopsis
        -----
        When ray tracing, controls whether the image plane will appear
        when seen through a transparent, refractive surface.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def alreadyPremult(self): 
        '''
        alreadyPremult(self) -> MObject

        Synopsis
        -----
        Indicates if the image plane has already been pre-multiplied by
        its alpha.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def composite(self): 
        '''
        composite(self) -> MObject

        Synopsis
        -----
        Indicates whether or not the image plane's color should be
        composited into the final image.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def depthOversample(self): 
        '''
        depthOversample(self) -> MObject

        Synopsis
        -----
        Indicates if the depth information is at a higher resolution than
        the image resolution.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def separateDepth(self): 
        '''
        separateDepth(self) -> MObject

        Synopsis
        -----
        Users can specify a depth buffer that is larger than the image
        buffer using the 'depthFile' attribute.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MPxLocatorNode:
    '''Base class for user defined locators.
MPxLocatorNode allows the creation of user-defined locators. A locator is a DAG
shape that is drawn on the screen, but that is not rendered.
Locators are full dependency nodes and can have attributes and a
compute method.
To create a locator, derive off of this class and override the
draw method. The draw method can be overridden to draw custom
geometry using standard OpenGL calls. The other methods of the
parent class
MPxNode may also be overridden to perform dependency node capabilities
as well.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MPxNode.MPxNode

        Synopsis
        -----
        This method returns the type of the node. This method should not
        be overridden by the user. It will return
        MPxNode::kLocatorNode.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def isBounded(self): 
        '''
        isBounded(self) -> bool

        Synopsis
        -----
        This method should be overridden to return true if the user
        supplies a bounding box routine. Supplying a bounding box routine
        makes refresh and selection more efficient.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def boundingBox(self): 
        '''
        boundingBox(self) -> MBoundingBox

        Synopsis
        -----
        This method should be overridden to return a bounding box for the
        locator. If this method is overridden, then
        MPxLocatorNode::isBounded should also be overridden to return
        true.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getCacheSetup(self, evalNode: MEvaluationNode,
                        disablingInfo: MNodeCacheDisablingInfo,
                        cacheSetupInfo: MNodeCacheSetupInfo,
                        monitoredAttributes: MObjectArray): 
        '''
        getCacheSetup(self, evalNode: MEvaluationNode,
                        disablingInfo: MNodeCacheDisablingInfo,
                        cacheSetupInfo: MNodeCacheSetupInfo,
                        monitoredAttributes: MObjectArray)

        Synopsis
        -----
        Introduced in 2020.0 Disables Cached Playback support by
        default.Built-in locators all enable Cached Playback by default,
        but plug-ins have to explicitly enable it by overriding this
        method.This method should be overridden to enable Cached Playback
        by default for custom locators.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
        evalNode: MEvaluationNode
        	[in] -> This node's evaluation node, contains animated plug information 

        disablingInfo: MNodeCacheDisablingInfo
        	[out] -> Information about why the node disables caching to be reported to the user 

        cacheSetupInfo: MNodeCacheSetupInfo
        	[out] -> Preferences and requirements this node has for caching 

        monitoredAttributes: MObjectArray
        	[out] -> Attributes impacting the behavior of this method that will be monitored for change 


        '''
        pass

    def color(self, displayStatus: M3dView.M3dView): 
        '''
        color(self, displayStatus: M3dView.M3dView) -> int

        Synopsis
        -----
        This method returns the index of the color that is the default
        draw color for the given display status. The index should be used
        with the methods of M3dView. The value is not an index into the
        OpenGL color table.The index that is returned will be into the
        active, dormant, or template color tables depending on the
        display status passed in.

        Returns: 
        ----- 
        The index of the color

        Parameters:
        -----
        displayStatus: M3dView.M3dView
        	[in] -> display status


        '''
        pass

    def colorRGB(self, displayStatus: M3dView.M3dView): 
        '''
        colorRGB(self, displayStatus: M3dView.M3dView) -> MColor

        Synopsis
        -----
        This method returns the RGB values of the default draw color for
        the given display status.

        Returns: 
        ----- 
        The color

        Parameters:
        -----
        displayStatus: M3dView.M3dView
        	[in] -> display status


        '''
        pass

    def excludeAsLocator(self): 
        '''
        excludeAsLocator(self) -> bool

        Synopsis
        -----
        When the modelPanel is set to not draw locators, returing true
        will also not draw the custom locator. If false is returned, the
        custom locator will also be drawn.The default return value is
        true.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def isTransparent(self): 
        '''
        isTransparent(self) -> bool

        Synopsis
        -----
        Indicates that this locator uses transparency during draw()
        method calls. Objects with transparency must be drawn in a
        special queue, i.e. after all opaque objects are drawn.The
        default return value is false. Note this flag is not respected by
        Viewport 2.0.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def drawLast(self): 
        '''
        drawLast(self) -> bool

        Synopsis
        -----
        Indicates that this locator should be the last item draw in a
        given refresh cycle. Objects drawn out-of-order will not preserve
        the proper transparency sorting. Conflicts among multiple objects
        with the drawLast indicator set to TRUE will be resolved by their
        order in the Outliner, where they will be drawn top-to-bottom.The
        default return value is false. Note this flag is not respected by
        Viewport 2.0.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def useClosestPointForSelection(self): 
        '''
        useClosestPointForSelection(self) -> bool

        Synopsis
        -----
        Determines whether Maya should call closestPoint() when doing
        single selection. When doing single selection Maya generally
        chooses the object closest to the selection ray. For locators it
        first does a hit test by calling the locator's draw method to
        determine if any part of it lies within the selection box. If the
        hit test succeeds Maya will add the locator to the list of
        objects being considered for selection and will use the center of
        the locator (i.e. its local origin) in determining its distance
        from the selection ray. This works well for locators which mark a
        single point in space, with no offset, but may not work as well
        for more complex locators.If this method is overridden to return
        true, then rather than using the locator's center to determine
        its distance from the selection ray, Maya will pass the ray to
        the closestPoint() method and use the point it returns. Note that
        you will have override closestPoint() as well to provide an
        appropriate point.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def closestPoint(self, rayPoint: MPoint,
                        rayDir: MVector): 
        '''
        closestPoint(self, rayPoint: MPoint,
                        rayDir: MVector) -> MPoint

        Synopsis
        -----
        Returns the point on the locator, in the locator's local space,
        which is closest along the specified ray. By default, the
        locator's origin (0, 0, 0) is returned.This is currently only
        used by Maya during single selection. See
        useClosestPointForSelection() for further details on that.

        Returns: 
        ----- 
        The point that Maya should consider as the closest point of
        intersection along the parameter ray.

        Parameters:
        -----
        rayPoint: MPoint
        	[in] -> The base point defining the ray in space 

        rayDir: MVector
        	[in] -> The ray direction in space


        '''
        pass

    def getShapeSelectionMask(self): 
        '''
        getShapeSelectionMask(self) -> MSelectionMask

        Synopsis
        -----
        This routine can be overridden to provide information about the
        selection mask of the locator. By default the selection mask for
        locators is returned.

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

    def thisMObject(self): 
        '''
        thisMObject(self) -> MObject

        Synopsis
        -----
        Returns the MObject associated with this user defined node. This
        makes it possible to use MFnDependencyNode or to construct plugs
        to this node's attributes.It is not necessary to override this
        method.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MPxManipulatorNode:
    '''Base class for manipulator creation.
MPxManipulatorNode is the base class used for creating user-defined manipulators.
This class is derived from
MPxNode since manipulators in Maya are dependency nodes.
An
MPxManipulatorNode should implement the following method:
Additionally, several of the following virtuals will need to be
defined:
Implement the following method to properly support undo:
The
draw() method is very important since drawing and picking are done
together. The
colorAndName() method should be called before drawing a GL component that
should be pickable. Several color methods which return color
indexes that Maya use are provided to allow custom manipulators
to have a similar look.
When drawing a GL pickable component, an active name must be set.
Use the
glFirstHandle() to get this value from the base class.
To draw the manipulator in Viewport 2.0, the plugin must also
implement
preDrawUI() and
drawUI(). Note that selection relies on the default viewport draw pass so
the
draw() method must still be implemented even if the manipulator is not
intended for use in the default viewport.
preDrawUI() is called before
drawUI() and should be used to prepare and cache data which will be
needed to draw the manipulator in
drawUI().
A manipulator can be connected to a depend node instead of
updating a node attribute directly in one of the do*() methods.
To connect to a depend node, you must:
This class can work standalone or with
MPxManipContainer.
'''
    def __init__(self):
        pass


    def connectToDependNode(self, node: MObject): 
        '''
        connectToDependNode(self, node: MObject)

        Synopsis
        -----
        This method connects the manipulator to the dependency node. This
        is a virtual method and needs to be overridden from the plug-in.

        Returns:
        -----
        None

        Parameters:
        -----
        node: MObject
        	[in] -> the node to which the manipulator should be connected


        '''
        pass

    def draw(self, view: M3dView,
                        path: MDagPath,
                        style: M3dView.M3dView,
                        status: M3dView.M3dView): 
        '''
        draw(self, view: M3dView,
                        path: MDagPath,
                        style: M3dView.M3dView,
                        status: M3dView.M3dView)

        Synopsis
        -----
        This method is overloaded to draw the manipulators. Selection is
        also setup with this method using the colorAndName() method
        call.This function is empty in this base class.

        Returns:
        -----
        None

        Parameters:
        -----
        view: M3dView
        	[in] -> the view in which to draw 

        path: MDagPath
        	[in] -> the current path 

        style: M3dView.M3dView
        	[in] -> the display appearance 

        status: M3dView.M3dView
        	[in] -> the display status 


        '''
        pass

    def doPress(self, view: M3dView): 
        '''
        doPress(self, view: M3dView)

        Synopsis
        -----
        This method gets called when the manipulator receives a mouse
        down event. You should return kUnknownParameter to allow Maya to
        process the event also.

        Returns:
        -----
        None

        Parameters:
        -----
        view: M3dView
        	[in] -> the view that is active


        '''
        pass

    def doDrag(self, view: M3dView): 
        '''
        doDrag(self, view: M3dView)

        Synopsis
        -----
        This method gets called when the manipulator receives a mouse
        drag event. You should return kUnknownParameter to allow Maya to
        process the event also.

        Returns:
        -----
        None

        Parameters:
        -----
        view: M3dView
        	[in] -> the view that is active


        '''
        pass

    def doRelease(self, view: M3dView): 
        '''
        doRelease(self, view: M3dView)

        Synopsis
        -----
        This method gets called when the manipulator receives a mouse
        release event. You should return kUnknownParameter to allow Maya
        to process the event also.

        Returns:
        -----
        None

        Parameters:
        -----
        view: M3dView
        	[in] -> the view that is active


        '''
        pass

    def doMove(self, view: M3dView,
                        refresh: bool): 
        '''
        doMove(self, view: M3dView,
                        refresh: bool)

        Synopsis
        -----
        This method gets called when the manipulator receives a mouse
        move event, if the manipulator registered for mouse move events.
        To register for mouse move events, invoke registerForMouseMove()
        in the postConstructor of your manipulator.You should return
        kUnknownParameter to allow Maya to process the event also.

        Returns:
        -----
        None

        Parameters:
        -----
        view: M3dView
        	[in] -> the view that is active 

        refresh: bool
        	[out] -> if true, refresh the view on this event. Default is false.


        '''
        pass

    def finishAddingManips(self): 
        '''
        finishAddingManips(self)

        Synopsis
        -----
        This method should be called from the user-defined manipulator
        plug-in near the end of the connectToDependNode method so that
        the converter in the manipulator can be initialized. The
        converter cannot be initialized until all the connections from
        the manip values to the plug values have been specified.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def colorAndName(self, view: M3dView,
                        glName: MPxManipulatorNode.MGLuint,
                        glNameIsPickable: bool,
                        colorIndex: short): 
        '''
        colorAndName(self, view: M3dView,
                        glName: MPxManipulatorNode.MGLuint,
                        glNameIsPickable: bool,
                        colorIndex: short)

        Synopsis
        -----
        This method is used to set the color of the GL component that is
        being drawn next. It is also used to set GL name of the component
        so that picking can be supported.

        Returns:
        -----
        None

        Parameters:
        -----
        view: M3dView
        	[in] -> the view that is active 

        glName: MPxManipulatorNode.MGLuint
        	[in] -> GL "name" (an unsigned int) of the component. Must be unique. 

        glNameIsPickable: bool
        	[in] -> If true, the component will be pickable 

        colorIndex: short
        	[in] -> Color to use, as provided by one of the *Color() methods in this class.


        '''
        pass

    def setHandleColor(self, drawManager: MHWRender.MHWRender,
                        handleName: int,
                        colorIndex: short): 
        '''
        setHandleColor(self, drawManager: MHWRender.MHWRender,
                        handleName: int,
                        colorIndex: short)

        Synopsis
        -----
        This method is used to set the color of component that is being
        drawn next. The color will be correctly selected based on the
        component's state(highlighted, selected, etc.)

        Returns:
        -----
        None

        Parameters:
        -----
        drawManager: MHWRender.MHWRender
        	[in] -> The MUIDrawManager used to draw some simple UI. 

        handleName: int
        	[in] -> The unique name (an unsigned int) of the component. 

        colorIndex: short
        	[in] -> The default color, if the component is neither highlighted nor selected, the colorIndex will be used.


        '''
        pass

    def glFirstHandle(self, firstHandle: MPxManipulatorNode.MGLuint): 
        '''
        glFirstHandle(self, firstHandle: MPxManipulatorNode.MGLuint)

        Synopsis
        -----
        This method is used to find the unsigned int value that should be
        used for the first GL handle.

        Returns:
        -----
        None

        Parameters:
        -----
        firstHandle: MPxManipulatorNode.MGLuint
        	[out] -> Returns the first handle.


        '''
        pass

    def glActiveName(self, glName: MPxManipulatorNode.MGLuint): 
        '''
        glActiveName(self, glName: MPxManipulatorNode.MGLuint)

        Synopsis
        -----
        This method returns the unsigned int value which specifies the
        current active handle.

        Returns:
        -----
        None

        Parameters:
        -----
        glName: MPxManipulatorNode.MGLuint
        	[out] -> active handle


        '''
        pass

    def mouseRay(self, linePoint: MPoint,
                        lineDirection: MVector): 
        '''
        mouseRay(self, linePoint: MPoint,
                        lineDirection: MVector)

        Synopsis
        -----
        This method returns the location of the mouse within a view. The
        location is defined by a point and a direction through the point.
        Both point and direction are in local space.

        Returns:
        -----
        None

        Parameters:
        -----
        linePoint: MPoint
        	[out] -> local space line point of mouse 

        lineDirection: MVector
        	[out] -> local direction of mouse in view


        '''
        pass

    def mouseRayWorld(self, linePoint: MPoint,
                        lineDirection: MVector): 
        '''
        mouseRayWorld(self, linePoint: MPoint,
                        lineDirection: MVector)

        Synopsis
        -----
        This method returns the location of the mouse within a view. The
        location is defined by a point and a direction through the point.
        Both point and direction are in world space.

        Returns:
        -----
        None

        Parameters:
        -----
        linePoint: MPoint
        	[out] -> world space line point of mouse 

        lineDirection: MVector
        	[out] -> world direction of mouse in view


        '''
        pass

    def mousePosition(self, x_pos: short,
                        y_pos: short): 
        '''
        mousePosition(self, x_pos: short,
                        y_pos: short)

        Synopsis
        -----
        This method returns the current mouse position within a view. The
        position is in port coordinates.

        Returns:
        -----
        None

        Parameters:
        -----
        x_pos: short
        	[out] -> returns the x port coordinate 

        y_pos: short
        	[out] -> returns the y port coordinate


        '''
        pass

    def mouseDown(self, x_pos: short,
                        y_pos: short): 
        '''
        mouseDown(self, x_pos: short,
                        y_pos: short)

        Synopsis
        -----
        This method returns the mouse down position within a view. The
        position is in port coordinates.

        Returns:
        -----
        None

        Parameters:
        -----
        x_pos: short
        	[out] -> returns the mouse down x port coordinate 

        y_pos: short
        	[out] -> returns the mouse down y port coordinate


        '''
        pass

    def mouseUp(self, x_pos: short,
                        y_pos: short): 
        '''
        mouseUp(self, x_pos: short,
                        y_pos: short)

        Synopsis
        -----
        This method returns the mouse up position within a view. The
        position is in port coordinates.

        Returns:
        -----
        None

        Parameters:
        -----
        x_pos: short
        	[out] -> returns the mouse up x port coordinate 

        y_pos: short
        	[out] -> returns the mouse up y port coordinate


        '''
        pass

    def registerForMouseMove(self): 
        '''
        registerForMouseMove(self)

        Synopsis
        -----
        This method registers this manipulator to receive mouse move
        events. When registered, the doMove() function will be invoked on
        mouse move events.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def deregisterForMouseMove(self): 
        '''
        deregisterForMouseMove(self)

        Synopsis
        -----
        This method deregisters this manipulator from receiving mouse
        move events.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def addDoubleValue(self, valueName: MString,
                        defaultValue: double,
                        valueIndex: int): 
        '''
        addDoubleValue(self, valueName: MString,
                        defaultValue: double,
                        valueIndex: int)

        Synopsis
        -----
        Manipulators which call connectPlugToValue() must first create
        the value on the node. Use this method to create a value of
        double type.

        Returns:
        -----
        None

        Parameters:
        -----
        valueName: MString
        	[in] -> Name of the value. 

        defaultValue: double
        	[in] -> Default value. 

        valueIndex: int
        	[out] -> Index assigned to this value by Maya. Used in 


        '''
        pass

    def addPointValue(self, valueName: MString,
                        defaultValue: MPoint,
                        valueIndex: int): 
        '''
        addPointValue(self, valueName: MString,
                        defaultValue: MPoint,
                        valueIndex: int)

        Synopsis
        -----
        Manipulators which call connectPlugToValue() must first create
        the value on the node. Use this method to create a value of
        double MPoint.

        Returns:
        -----
        None

        Parameters:
        -----
        valueName: MString
        	[in] -> Name of the value. 

        defaultValue: MPoint
        	[in] -> Default value. 

        valueIndex: int
        	[out] -> Index assigned to this value by Maya. Used in 


        '''
        pass

    def addVectorValue(self, valueName: MString,
                        defaultValue: MVector,
                        valueIndex: int): 
        '''
        addVectorValue(self, valueName: MString,
                        defaultValue: MVector,
                        valueIndex: int)

        Synopsis
        -----
        Manipulators which call connectPlugToValue() must first create
        the value on the node. Use this method to create a value of
        double MVector.

        Returns:
        -----
        None

        Parameters:
        -----
        valueName: MString
        	[in] -> Name of the value. 

        defaultValue: MVector
        	[in] -> Default value. 

        valueIndex: int
        	[out] -> Index assigned to this value by Maya. Used in 


        '''
        pass

    def setDoubleValue(self, valueIndex: int,
                        value: double): 
        '''
        setDoubleValue(self, valueIndex: int,
                        value: double)

        Synopsis
        -----
        This method is used for setting a double value associated with
        the manipulator.

        Returns:
        -----
        None

        Parameters:
        -----
        valueIndex: int
        	[in] -> the index of the value to be set 

        value: double
        	[in] -> the value to set it to


        '''
        pass

    def setPointValue(self, valueIndex: int,
                        value: MPoint): 
        '''
        setPointValue(self, valueIndex: int,
                        value: MPoint)

        Synopsis
        -----
        This method is used for setting an MPoint value associated with
        the manipulator.

        Returns:
        -----
        None

        Parameters:
        -----
        valueIndex: int
        	[in] -> the index of the value to be set 

        value: MPoint
        	[in] -> the value to set it to


        '''
        pass

    def setVectorValue(self, valueIndex: int,
                        value: MVector): 
        '''
        setVectorValue(self, valueIndex: int,
                        value: MVector)

        Synopsis
        -----
        This method is used for setting a MVector value associated with
        the manipulator.

        Returns:
        -----
        None

        Parameters:
        -----
        valueIndex: int
        	[in] -> the index of the value to be set 

        value: MVector
        	[in] -> the value to set it to


        '''
        pass

    def getDoubleValue(self, valueIndex: int,
                        previousValue: bool,
                        value: double): 
        '''
        getDoubleValue(self, valueIndex: int,
                        previousValue: bool,
                        value: double)

        Synopsis
        -----
        This method is used for getting a double value associated with
        the manipulator.

        Returns:
        -----
        None

        Parameters:
        -----
        valueIndex: int
        	[in] -> the index of the value to be set 

        previousValue: bool
        	[in] -> if true, get the previous value. if false, get the current value 

        value: double
        	[out] -> return the double value


        '''
        pass

    def getPointValue(self, valueIndex: int,
                        previousValue: bool,
                        value: MPoint): 
        '''
        getPointValue(self, valueIndex: int,
                        previousValue: bool,
                        value: MPoint)

        Synopsis
        -----
        This method is used for getting a MPoint value associated with
        the manipulator.

        Returns:
        -----
        None

        Parameters:
        -----
        valueIndex: int
        	[in] -> the index of the value to be set 

        previousValue: bool
        	[in] -> if true, get the previous value. if false, get the current value 

        value: MPoint
        	[out] -> return the double value


        '''
        pass

    def getVectorValue(self, valueIndex: int,
                        previousValue: bool,
                        value: MVector): 
        '''
        getVectorValue(self, valueIndex: int,
                        previousValue: bool,
                        value: MVector)

        Synopsis
        -----
        This method is used for getting a MVector value associated with
        the manipulator.

        Returns:
        -----
        None

        Parameters:
        -----
        valueIndex: int
        	[in] -> the index of the value to be set 

        previousValue: bool
        	[in] -> if true, get the previous value. if false, get the current value 

        value: MVector
        	[out] -> return the double value


        '''
        pass

    def connectPlugToValue(self, plug: MPlug,
                        valueIndex: int,
                        plugIndex: int): 
        '''
        connectPlugToValue(self, plug: MPlug,
                        valueIndex: int,
                        plugIndex: int)

        Synopsis
        -----
        This method is called in the connectToDependNode() virtual if it
        is implemented for the custom manipulator. It will connect a plug
        to an already added manipulator value of the same type.

        Returns:
        -----
        None

        Parameters:
        -----
        plug: MPlug
        	[in] -> the plug to connect the value to 

        valueIndex: int
        	[in] -> the index of the value. index is set by add*Value() method 

        plugIndex: int
        	[out] -> a new index for the plug that is being connected


        '''
        pass

    def addDependentPlug(self, plug: MPlug): 
        '''
        addDependentPlug(self, plug: MPlug)

        Synopsis
        -----
        This method adds the plug to the list of those to be keyframed.
        The call to addDependentPlug() should happen prior to the
        manipulator identifying the plugs to be set. For example, if your
        manipulator sets plugs based on the selection list or modifier
        keys you could call addDependentPlug() from your doPress()
        method. Note that the dependentPlugsReset() method is provided to
        clear out the list and should be called prior to
        addDependentPlugs().

        Returns:
        -----
        None

        Parameters:
        -----
        plug: MPlug
        	[in] -> the plug to keyframe when using this manipulator


        '''
        pass

    def dependentPlugsReset(self): 
        '''
        dependentPlugsReset(self)

        Synopsis
        -----
        This method resets the list of dependent plugs for this
        manipulator. Call this method prior to adding plugs via
        addDependentPlug() such as from your doPress() method.

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

    def thisMObject(self): 
        '''
        thisMObject(self) -> MObject

        Synopsis
        -----
        Returns the MObject associated with this user defined node. This
        makes it possible to use MFnDependencyNode or to construct plugs
        to this node's attributes.It is not necessary to override this
        method.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MPxManipContainer:
    '''Base class for user defined manipulator containers.
MPxManipContainer is the base class for user-defined container manipulators. This
class is derived from
MPxNode since manipulators in Maya are dependency nodes.
MPxManipContainer is a container manipulator that has at least one base
manipulator.
MPxManipContainer has methods for adding the following base manipulators types to
the container: FreePointTriadManip, DirectionManip,
DistanceManip, PointOnCurveManip, PointOnSurfaceManip, DiscManip,
CircleSweepManip, ToggleManip, StateManip, and CurveSegmentManip.
A container manipulator has one converter which is the interface
between the container's children manipulators and the node plugs
they affect. The values on the converter that are related to
children manipulators are called converterManipValues, and the
values on the converter that are related to the node plugs are
called converterPlugValues.
The conversion between converterManipValues and
converterPlugValues are performed through conversion callback
methods, except when there is a one-to-one connection between a
converterManipValue and a converterPlugValue.
There are two kinds of conversion callback methods: manipToPlug
and plugToManip. A plugToManipConversionCallback is used to
calculate a converterManipValue from various converterPlugValues.
This callback has access to all the converterPlugValues and
returns the value of a converterManipValue. A
manipToPlugConversionCallback is used to calculate a
converterPlugValue from various converterManipValues. This
callback has access to all the converterManipValues and returns
the value of a converterPlugValue.
In Viewport 2.0, all child manipulators will draw automatically.
However for custom drawing (things done in the
draw() method for the default viewport), the plugin must also implement
preDrawUI() and
drawUI(). Note that selection relies on the default viewport draw pass so
the
draw() method must still be implemented even if the manipulator is not
intended for use in the default viewport.
preDrawUI() is called before
drawUI() and should be used to prepare and cache data which will be
needed to perform the custom drawing in
drawUI().
In order for an
MPxManipContainer to be able to run, the manipulator needs to know that the
initialization is finished through the finishAddingManips method.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MPxNode.MPxNode

        Synopsis
        -----
        This method returns the type of the node. Reimplemented from
        MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def initialize(self): 
        '''
        initialize(self)

        Synopsis
        -----
        This method initializes the manipulator, and should be overriden
        in user-defined manipulators.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def draw(self, view: M3dView,
                        path: MDagPath,
                        style: M3dView.M3dView,
                        status: M3dView.M3dView): 
        '''
        draw(self, view: M3dView,
                        path: MDagPath,
                        style: M3dView.M3dView,
                        status: M3dView.M3dView)

        Synopsis
        -----
        This method can be overloaded to customize the drawing of the
        child manipulators. If the default draw is also required, this
        method should be called from the derived method.

        Returns:
        -----
        None

        Parameters:
        -----
        view: M3dView
        	[in] -> the view in which to draw 

        path: MDagPath
        	[in] -> the current path 

        style: M3dView.M3dView
        	[in] -> the display appearance 

        status: M3dView.M3dView
        	[in] -> the display status 


        '''
        pass

    def connectToDependNode(self, node: MObject): 
        '''
        connectToDependNode(self, node: MObject)

        Synopsis
        -----
        This method connects the manipulator to the dependency node. This
        is a virtual method and needs to be overridden from the plug-in.

        Returns:
        -----
        None

        Parameters:
        -----
        node: MObject
        	[in] -> the node to which the manipulator should be connected


        '''
        pass

    def createChildren(self): 
        '''
        createChildren(self)

        Synopsis
        -----
        This method should be overridden in user defined manipulators.
        This method is called after the user node derived from
        MPxManipContainer is set up.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def addFreePointTriadManip(self, manipName: MString,
                        pointName: MString): 
        '''
        addFreePointTriadManip(self, manipName: MString,
                        pointName: MString) -> MDagPath

        Synopsis
        -----
        This method creates a FreePointTriadManip and adds it to the
        MPxManipContainer container.

        Returns: 
        ----- 
        New FreePointTriadManip

        Parameters:
        -----
        manipName: MString
        	[in] -> manipulator name 

        pointName: MString
        	[in] -> point name


        '''
        pass

    def addDirectionManip(self, manipName: MString,
                        directionName: MString): 
        '''
        addDirectionManip(self, manipName: MString,
                        directionName: MString) -> MDagPath

        Synopsis
        -----
        This method creates a DirectionManip and adds it to the
        MPxManipContainer container.

        Returns: 
        ----- 
        New DirectionManip

        Parameters:
        -----
        manipName: MString
        	[in] -> manipulator name 

        directionName: MString
        	[in] -> direction name


        '''
        pass

    def addDistanceManip(self, manipName: MString,
                        distanceName: MString): 
        '''
        addDistanceManip(self, manipName: MString,
                        distanceName: MString) -> MDagPath

        Synopsis
        -----
        This method creates a DistanceManip and adds it to the
        MPxManipContainer container.

        Returns: 
        ----- 
        New DistanceManip

        Parameters:
        -----
        manipName: MString
        	[in] -> manipulator name 

        distanceName: MString
        	[in] -> distance name


        '''
        pass

    def addPointOnCurveManip(self, manipName: MString,
                        paramName: MString): 
        '''
        addPointOnCurveManip(self, manipName: MString,
                        paramName: MString) -> MDagPath

        Synopsis
        -----
        This method creates a PointOnCurveManip and adds it to the
        MPxManipContainer container.

        Returns: 
        ----- 
        New PointOnCurveManip

        Parameters:
        -----
        manipName: MString
        	[in] -> manipulator name 

        paramName: MString
        	[in] -> parameter name


        '''
        pass

    def addPointOnSurfaceManip(self, manipName: MString,
                        paramName: MString): 
        '''
        addPointOnSurfaceManip(self, manipName: MString,
                        paramName: MString) -> MDagPath

        Synopsis
        -----
        This method creates a PointOnSurfaceManip and adds it to the
        MPxManipContainer container.

        Returns: 
        ----- 
        New PointOnSurfaceManip

        Parameters:
        -----
        manipName: MString
        	[in] -> manipulator name 

        paramName: MString
        	[in] -> parameter name


        '''
        pass

    def addDiscManip(self, manipName: MString,
                        angleName: MString): 
        '''
        addDiscManip(self, manipName: MString,
                        angleName: MString) -> MDagPath

        Synopsis
        -----
        This method creates a DiscManip and adds it to the
        MPxManipContainer container.

        Returns: 
        ----- 
        New DiscManip

        Parameters:
        -----
        manipName: MString
        	[in] -> manipulator name 

        angleName: MString
        	[in] -> angle name


        '''
        pass

    def addCircleSweepManip(self, manipName: MString,
                        angleName: MString): 
        '''
        addCircleSweepManip(self, manipName: MString,
                        angleName: MString) -> MDagPath

        Synopsis
        -----
        This method creates a CircleSweepManip and adds it to the
        MPxManipContainer container.

        Returns: 
        ----- 
        New CircleSweepManip

        Parameters:
        -----
        manipName: MString
        	[in] -> manipulator name 

        angleName: MString
        	[in] -> angle name


        '''
        pass

    def addToggleManip(self, manipName: MString,
                        toggleName: MString): 
        '''
        addToggleManip(self, manipName: MString,
                        toggleName: MString) -> MDagPath

        Synopsis
        -----
        This method creates a ToggleManip and adds it to the
        MPxManipContainer container.

        Returns: 
        ----- 
        New ToggleManip

        Parameters:
        -----
        manipName: MString
        	[in] -> manipulator name 

        toggleName: MString
        	[in] -> toggle name


        '''
        pass

    def addStateManip(self, manipName: MString,
                        stateName: MString): 
        '''
        addStateManip(self, manipName: MString,
                        stateName: MString) -> MDagPath

        Synopsis
        -----
        This method creates a StateManip and adds it to the
        MPxManipContainer container.

        Returns: 
        ----- 
        New StateManip

        Parameters:
        -----
        manipName: MString
        	[in] -> manipulator name 

        stateName: MString
        	[in] -> state name


        '''
        pass

    def addCurveSegmentManip(self, manipName: MString,
                        startParamName: MString,
                        endParamName: MString): 
        '''
        addCurveSegmentManip(self, manipName: MString,
                        startParamName: MString,
                        endParamName: MString) -> MDagPath

        Synopsis
        -----
        This method creates a CurveSegmentManip and adds it to the
        MPxManipContainer container.

        Returns: 
        ----- 
        New CurveSegmentManip

        Parameters:
        -----
        manipName: MString
        	[in] -> manipulator name 

        startParamName: MString
        	[in] -> start parameter name 

        endParamName: MString
        	[in] -> end parameter name


        '''
        pass

    def addRotateManip(self, manipName: MString,
                        rotationName: MString): 
        '''
        addRotateManip(self, manipName: MString,
                        rotationName: MString) -> MDagPath

        Synopsis
        -----
        This method creates a rotate manipulator and adds it to the
        MPxManipContainer container.

        Returns: 
        ----- 
        Dag path to the new rotate manipulator

        Parameters:
        -----
        manipName: MString
        	[in] -> manipulator name 

        rotationName: MString
        	[in] -> name of the rotation vector


        '''
        pass

    def addScaleManip(self, manipName: MString,
                        scaleName: MString): 
        '''
        addScaleManip(self, manipName: MString,
                        scaleName: MString) -> MDagPath

        Synopsis
        -----
        This method creates a scale manipulator and adds it to the
        MPxManipContainer container.

        Returns: 
        ----- 
        Dag path to the new scale manipulator

        Parameters:
        -----
        manipName: MString
        	[in] -> manipulator name 

        scaleName: MString
        	[in] -> name of the scale vector


        '''
        pass

    def addMPxManipulatorNode(self, manipTypeName: MString,
                        manipName: MString,
                        proxyManip: MPxManipulatorNode): 
        '''
        addMPxManipulatorNode(self, manipTypeName: MString,
                        manipName: MString,
                        proxyManip: MPxManipulatorNode)

        Synopsis
        -----
        This method creates a custom MPxManipulatorNode and adds it to
        the MPxManipContainer container.

        Returns:
        -----
        None

        Parameters:
        -----
        manipTypeName: MString
        	[in] -> manipulator name 

        manipName: MString
        	[in] -> name of the manip 

        proxyManip: MPxManipulatorNode
        	[out] -> returns a pointer to the new manipulator


        '''
        pass

    def isManipActive(self, manipType: MFn.MFn,
                        manipObject: MObject): 
        '''
        isManipActive(self, manipType: MFn.MFn,
                        manipObject: MObject) -> bool

        Synopsis
        -----
        This method determines if custom manip is active & gets the
        current manip object.

        Returns: 
        ----- 
        true custom manip is active  false custom manip is inactive

        Parameters:
        -----
        manipType: MFn.MFn
        	[in] -> the type of the custom manip 

        manipObject: MObject
        	[in] -> manipulator object


        '''
        pass

    def finishAddingManips(self): 
        '''
        finishAddingManips(self)

        Synopsis
        -----
        This method should be called from the user-defined manipulator
        plug-in near the end of the connectToDependNode method so that
        the converter in the manipulator can be initialized. The
        converter cannot be initialized until all the connections from
        the manip values to the plug values have been specified.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def addToManipConnectTable(self, mid: MTypeId): 
        '''
        addToManipConnectTable(self, mid: MTypeId)

        Synopsis
        -----
        This method adds the user defined node as an entry in the
        manipConnectTable so that when this node is selected the user can
        use the show manip tool to get the user defined manipulator
        associated with this node. Note that the name of the manipulator
        node has to be the name of the plug-in node appended with
        "Manip".

        Returns:
        -----
        None

        Parameters:
        -----
        mid: MTypeId
        	[in] -> id of the user defined node


        '''
        pass

    def removeFromManipConnectTable(self, id: MTypeId): 
        '''
        removeFromManipConnectTable(self, id: MTypeId)

        Synopsis
        -----
        This method removes the user defined node entry from the
        manipConnectTable.

        Returns:
        -----
        None

        Parameters:
        -----
        id: MTypeId
        	[in] -> id of the user defined node


        '''
        pass

    def plugToManipConversion(self, manipIndex: int): 
        '''
        plugToManipConversion(self, manipIndex: int) -> MManipData

        Synopsis
        -----
        This virtual method calculates and returns the requested
        manipulator value, based upon the values of plugs on the nodes
        being manipulated. To use, call addPlugToManipConversion() for
        each manipulator value (e.g. the start point of a distance manip)
        you want this method to calculate, then implement this method to
        calculate those manipulator values. Each manipulator value is
        identified by the unique index returned by the corresponding
        method of its functionset (e.g.
        MFnDistanceManip::startPointIndex).

        Returns: 
        ----- 
        New manipulator value.

        Parameters:
        -----
        manipIndex: int
        	[in] -> the index of the manipulator value to be calculated


        '''
        pass

    def manipToPlugConversion(self, plugIndex: int): 
        '''
        manipToPlugConversion(self, plugIndex: int) -> MManipData

        Synopsis
        -----
        This virtual method calculates and returns the requested plug
        value, based upon the container's manipulator values. To use,
        call addManipToPlugConversion() for each plug whose value you
        want this method to calculate then implement this method to
        calculate those plug values. Each plug is identified by the
        unique index returned by the addManipToPlugConversion() call.

        Returns: 
        ----- 
        New plug value.

        Parameters:
        -----
        plugIndex: int
        	[in] -> the index of the plug value to be calculated


        '''
        pass

    def addPlugToManipConversion(self, manipIndex: int): 
        '''
        addPlugToManipConversion(self, manipIndex: int)

        Synopsis
        -----
        This method adds a plug to manipulator converter for the
        specified manipulator value (e.g. the start point of a distance
        manip). The converter must be implemented in the
        plugToManipConversion() virtual method of this class.NOTE: The
        conversion methods and callback methods of this class should not
        be mixed. The conversion methods are: addManipToPlugConversion(),
        addManipToPlugConversion() The callback methods are:
        addPlugToManipConversionCallback()
        addManipToPlugConversionCallback()

        Returns:
        -----
        None

        Parameters:
        -----
        manipIndex: int
        	[in] -> the index of the manipulator value for which the converter is being requested. The index is determined by calling the appropriate method of the manipulator's functionset (e.g. 


        '''
        pass

    def addManipToPlugConversion(self, plug: MPlug): 
        '''
        addManipToPlugConversion(self, plug: MPlug) -> int

        Synopsis
        -----
        This method adds a manipulator to plug converter for the
        specified plug. The converter must be implemented in the
        manipToPlugConversion() virtual method of this class.NOTE: The
        conversion methods and callback methods of this class should not
        be mixed. The conversion methods are: addManipToPlugConversion(),
        addManipToPlugConversion() The callback methods are:
        addPlugToManipConversionCallback()
        addManipToPlugConversionCallback()

        Returns: 
        ----- 
        Index used to identify the plug inside the
        manipToPlugConversion() method.

        Parameters:
        -----
        plug: MPlug
        	[in] -> the plug for which the converter is being requested.


        '''
        pass

    def addPlugToInViewEditor(self, plug: MPlug): 
        '''
        addPlugToInViewEditor(self, plug: MPlug)

        Synopsis
        -----
        Adds a plug to the In-View Editor. The first such call will cause
        the In-View Editor to be displayed automatically with the custom
        manip.Should be called from connectToDependNode().

        Returns:
        -----
        None

        Parameters:
        -----
        plug: MPlug
        	[in] -> The plug that the slider should control 


        '''
        pass

    @overload
    def getConverterManipValue(self, manipIndex: int,
                        value: int): 
        '''
        getConverterManipValue(self, manipIndex: int,
                        value: int)

        Synopsis
        -----
        This method retrieves the value of a converterManipValue of type
        unsigned int at a given index from the converter.

        Returns:
        -----
        None

        Parameters:
        -----
        manipIndex: int
        	[in] -> the index of the converterManipValue 

        value: int
        	[out] -> the value at the specified index


        '''
        pass

    @overload
    def getConverterManipValue(self, manipIndex: int,
                        value: double): 
        '''
        getConverterManipValue(self, manipIndex: int,
                        value: double)

        Synopsis
        -----
        This method retrieves the value of a converterManipValue of type
        double at a given index from the converter.

        Returns:
        -----
        None

        Parameters:
        -----
        manipIndex: int
        	[in] -> the index of the converterManipValue 

        value: double
        	[out] -> the value at the specified index


        '''
        pass

    @overload
    def getConverterManipValue(self, manipIndex: int,
                        x: double,
                        y: double): 
        '''
        getConverterManipValue(self, manipIndex: int,
                        x: double,
                        y: double)

        Synopsis
        -----
        This method retrieves the x and y values of a converterManipValue
        of type double at a given index from the converter.

        Returns:
        -----
        None

        Parameters:
        -----
        manipIndex: int
        	[in] -> the index of the converterManipValue 

        x: double
        	[out] -> the x value at the specified index 

        y: double
        	[out] -> the y value at the specified index


        '''
        pass

    @overload
    def getConverterManipValue(self, manipIndex: int,
                        point: MPoint): 
        '''
        getConverterManipValue(self, manipIndex: int,
                        point: MPoint)

        Synopsis
        -----
        This method retrieves the value of a converterManipValue of type
        MPoint at a given index from the converter.

        Returns:
        -----
        None

        Parameters:
        -----
        manipIndex: int
        	[in] -> the index of the converterManipValue 

        point: MPoint
        	[out] -> the value at the specified index


        '''
        pass

    @overload
    def getConverterManipValue(self, manipIndex: int,
                        vector: MVector): 
        '''
        getConverterManipValue(self, manipIndex: int,
                        vector: MVector)

        Synopsis
        -----
        This method retrieves the value of a converterManipValue of type
        MVector at a given index from the converter.

        Returns:
        -----
        None

        Parameters:
        -----
        manipIndex: int
        	[in] -> the index of the converterManipValue 

        vector: MVector
        	[out] -> the value at the specified index


        '''
        pass

    @overload
    def getConverterManipValue(self, manipIndex: int,
                        matrix: MMatrix): 
        '''
        getConverterManipValue(self, manipIndex: int,
                        matrix: MMatrix)

        Synopsis
        -----
        This method retrieves the value of a converterManipValue of type
        MMatrix at a given index from the converter.

        Returns:
        -----
        None

        Parameters:
        -----
        manipIndex: int
        	[in] -> the index of the converterManipValue 

        matrix: MMatrix
        	[out] -> the value at the specified index


        '''
        pass

    @overload
    def getConverterManipValue(self, manipIndex: int,
                        rotation: MEulerRotation): 
        '''
        getConverterManipValue(self, manipIndex: int,
                        rotation: MEulerRotation)

        Synopsis
        -----
        This method retrieves the value of a converterManipValue of type
        MEulerRotation at a given index from the converter.

        Returns:
        -----
        None

        Parameters:
        -----
        manipIndex: int
        	[in] -> the index of the converterManipValue 

        rotation: MEulerRotation
        	[out] -> the value at the specified index


        '''
        pass

    @overload
    def getConverterManipValue(self, manipIndex: int,
                        xform: MTransformationMatrix): 
        '''
        getConverterManipValue(self, manipIndex: int,
                        xform: MTransformationMatrix)

        Synopsis
        -----
        This method retrieves the value of a converterManipValue of type
        MTransformationMatrix at a given index from the converter.

        Returns:
        -----
        None

        Parameters:
        -----
        manipIndex: int
        	[in] -> the index of the converterManipValue 

        xform: MTransformationMatrix
        	[out] -> the value at the specified index


        '''
        pass

    @overload
    def getConverterPlugValue(self, plugIndex: int,
                        value: double): 
        '''
        getConverterPlugValue(self, plugIndex: int,
                        value: double)

        Synopsis
        -----
        This method retrieves the value of a converterPlugValue of type
        double at a given index from the converter.

        Returns:
        -----
        None

        Parameters:
        -----
        plugIndex: int
        	[in] -> the index of the converterPlugValue 

        value: double
        	[out] -> the value at the specified index


        '''
        pass

    @overload
    def getConverterPlugValue(self, plugIndex: int,
                        x: double,
                        y: double): 
        '''
        getConverterPlugValue(self, plugIndex: int,
                        x: double,
                        y: double)

        Synopsis
        -----
        This method retrieves the x and y values of a converterPlugValue
        of type double at a given index from the converter.

        Returns:
        -----
        None

        Parameters:
        -----
        plugIndex: int
        	[in] -> the index of the converterPlugValue 

        x: double
        	[out] -> the x value at the specified index 

        y: double
        	[out] -> the y value at the specified index


        '''
        pass

    @overload
    def getConverterPlugValue(self, plugIndex: int,
                        point: MPoint): 
        '''
        getConverterPlugValue(self, plugIndex: int,
                        point: MPoint)

        Synopsis
        -----
        This method retrieves the value of a converterPlugValue of type
        MPoint at a given index from the converter.

        Returns:
        -----
        None

        Parameters:
        -----
        plugIndex: int
        	[in] -> the index of the converterPlugValue 

        point: MPoint
        	[out] -> the value at the specified index


        '''
        pass

    @overload
    def getConverterPlugValue(self, plugIndex: int,
                        vector: MVector): 
        '''
        getConverterPlugValue(self, plugIndex: int,
                        vector: MVector)

        Synopsis
        -----
        This method retrieves the value of a converterPlugValue of type
        MVector at a given index from the converter.

        Returns:
        -----
        None

        Parameters:
        -----
        plugIndex: int
        	[in] -> the index of the converterPlugValue 

        vector: MVector
        	[out] -> the value at the specified index


        '''
        pass

    @overload
    def getConverterPlugValue(self, plugIndex: int,
                        matrix: MMatrix): 
        '''
        getConverterPlugValue(self, plugIndex: int,
                        matrix: MMatrix)

        Synopsis
        -----
        This method retrieves the value of a converterPlugValue of type
        MMatrix at a given index from the converter.

        Returns:
        -----
        None

        Parameters:
        -----
        plugIndex: int
        	[in] -> the index of the converterPlugValue 

        matrix: MMatrix
        	[out] -> the value at the specified index


        '''
        pass

    @overload
    def getConverterPlugValue(self, plugIndex: int,
                        rotation: MEulerRotation): 
        '''
        getConverterPlugValue(self, plugIndex: int,
                        rotation: MEulerRotation)

        Synopsis
        -----
        This method retrieves the value of a converterPlugValue of type
        MEulerRotation at a given index from the converter.

        Returns:
        -----
        None

        Parameters:
        -----
        plugIndex: int
        	[in] -> the index of the converterPlugValue 

        rotation: MEulerRotation
        	[out] -> the value at the specified index


        '''
        pass

    def doPress(self): 
        '''
        doPress(self)

        Synopsis
        -----
        This method gets called when the manipulator receives a mouse
        down event. You should return kUnknownParameter to specify that
        maya should handle this connection or if you want maya to process
        the connection as well.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def doDrag(self): 
        '''
        doDrag(self)

        Synopsis
        -----
        This method gets called when the manipulator receives a mouse
        drag event. You should return kUnknownParameter to specify that
        maya should handle this connection or if you want maya to process
        the connection as well.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def doRelease(self): 
        '''
        doRelease(self)

        Synopsis
        -----
        This method gets called when the manipulator receives a mouse
        release event. You should return kUnknownParameter to specify
        that maya should handle this connection or if you want maya to
        process the connection as well.

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

    def thisMObject(self): 
        '''
        thisMObject(self) -> MObject

        Synopsis
        -----
        Introduced in 2020.0 Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class baseType:
    '''Built-in manipulator types. 
    Non-functional class.  Values for this enum:
    kFreePointTriadManip
    kDirectionManip
    kDistanceManip
    kPointOnCurveManip
    kPointOnSurfaceManip
    kDiscManip
    kCircleSweepManip
    kToggleManip
    kStateManip
    kCurveSegmentManip
    kCustomManip
    '''

    def __init__(self):
        pass

    def kFreePointTriadManip(self):
        '''This is an enum of baseType.
        - Description:  
        - Value: 0
        '''
        pass

    def kDirectionManip(self):
        '''This is an enum of baseType.
        - Description:  
        - Value: 1
        '''
        pass

    def kDistanceManip(self):
        '''This is an enum of baseType.
        - Description:  
        - Value: 2
        '''
        pass

    def kPointOnCurveManip(self):
        '''This is an enum of baseType.
        - Description:  
        - Value: 3
        '''
        pass

    def kPointOnSurfaceManip(self):
        '''This is an enum of baseType.
        - Description:  
        - Value: 4
        '''
        pass

    def kDiscManip(self):
        '''This is an enum of baseType.
        - Description:  
        - Value: 5
        '''
        pass

    def kCircleSweepManip(self):
        '''This is an enum of baseType.
        - Description:  
        - Value: 6
        '''
        pass

    def kToggleManip(self):
        '''This is an enum of baseType.
        - Description:  
        - Value: 7
        '''
        pass

    def kStateManip(self):
        '''This is an enum of baseType.
        - Description:  
        - Value: 8
        '''
        pass

    def kCurveSegmentManip(self):
        '''This is an enum of baseType.
        - Description:  
        - Value: 9
        '''
        pass

    def kCustomManip(self):
        '''This is an enum of baseType.
        - Description:  
        - Value: 10
        '''
        pass

class MPxMaterialInformation:
    '''Material information proxy.
The
MPxMaterialInformation class is a way for users to override the viewport representation
of shaders. The viewport uses a simple phong model for display in
the viewport. With this class users can provide their own values
for the phong shading parameters.
'''
    def __init__(self):
        pass


    def useMaterialAsTexture(self): 
        '''
        useMaterialAsTexture(self) -> bool

        Synopsis
        -----
        Tells Maya whether to this material should be displayed as a
        texture, ie whether it should be baked.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def materialInfoIsDirty(self, plug: MPlug): 
        '''
        materialInfoIsDirty(self, plug: MPlug) -> bool

        Synopsis
        -----
        Called by Maya to when a plug on the shader has been changed.
        This method tells Maya if the material information is dirty. If
        it is dirty Maya triggers a refresh of the viewport.

        Returns: 
        ----- 
        true if the material information is dirty, false otherwise

        Parameters:
        -----
        plug: MPlug
        	[in] -> the plug that was changed


        '''
        pass

    def connectAsTexture(self, plug: MPlug): 
        '''
        connectAsTexture(self, plug: MPlug) -> bool

        Synopsis
        -----
        Called by Maya to when an incoming connection is made to plug on
        the shader. This method tells Maya if connection should be
        treated as a to a texture. If the connection is treated as a
        texture the Maya will bake the properties of the source plug for
        display in the viewport. Currently only one channel/plug on the
        shader can be treated as a texture.

        Returns: 
        ----- 
        true if connection should be treated as a texture, false
        otherwise

        Parameters:
        -----
        plug: MPlug
        	[in] -> the plug that was connected


        '''
        pass

    def textureDisconnected(self, plug: MPlug): 
        '''
        textureDisconnected(self, plug: MPlug) -> bool

        Synopsis
        -----
        Called whenever an incoming connection to the shader is broken.

        Returns: 
        ----- 
        true if connection should be treated as a texture, false
        otherwise

        Parameters:
        -----
        plug: MPlug
        	[in] -> the plug that was disconnected.


        '''
        pass

    def computeMaterial(self, data: MaterialInputData): 
        '''
        computeMaterial(self, data: MaterialInputData) -> bool

        Synopsis
        -----
        Compute the material properties/information for the shader. These
        properties are the parameters for a simple phong shading model
        used for display in the viewport

        Returns: 
        ----- 
        true if valid material properties/information were created, false
        otherwise

        Parameters:
        -----
        data: MaterialInputData
        	[in] -> the material properties/information


        '''
        pass

class MaterialType:
    '''Material types. These affect how the material is shaded. 
    Non-functional class.  Values for this enum:
    kSimpleMaterial
    kTexture
    kOverrideDraw
    '''

    def __init__(self):
        pass

    def kSimpleMaterial(self):
        '''This is an enum of MaterialType.
        - Description:  
        - Value: 0
        '''
        pass

    def kTexture(self):
        '''This is an enum of MaterialType.
        - Description:  
        - Value: 1
        '''
        pass

    def kOverrideDraw(self):
        '''This is an enum of MaterialType.
        - Description:  
        - Value: 2
        '''
        pass

class MPxMayaAsciiFilter:
    '''Translator to output filtered Maya ASCII files.
MPxMayaAsciiFilter allows output to the Maya ASCII (.ma) file format to be filtered
by a plug-in. The file is output using the same internal
mechanism that is used for normal Maya ASCII output, but allows
your plug-in to prevent certain lines (such as createNodes or
connectAttrs) from being output to the file. In addition, it
allows you to write directly to the file at specific points
during output.
MPxMayaAsciiFilter allows your plug-in to write out files similar to Maya ASCII in
a custom format. It can be used, for example, to partition a
scene into several files, each of which has been filtered to
write out different parts of the scene. Note that the order of
the file cannot be changed - for example, connectAttrs are always
written after createNodes - but it does allow you to control
which connectAttrs and createNodes are output.
MPxMayaAsciiFilter inherits from
MPxFileTranslator. It overrides the
haveWriteMethod(),
haveReadMethod(),
reader(), and
writer() methods in
MPxFileTranslator in such a way that the internal Maya mechanism for reading and
writing Maya ASCII files is used. Because of this, it is not
advised that you override these methods in your plug-in. If you
do, make sure you first call these methods in
MPxMayaAsciiFilter. A pseudo-code example is shown here:
To determine if a given line should be output, override the
methods
writesCreateNode(),
writesSetAttr() and so on. Each of these methods takes as its arguments the
relevant data which is about to be processed and your plug-in can
use this to determine whether or not the line will be output.
For example, you may want to write out everything but render
layer data. The code to do this might look something like what is
shown here:
Note that
writesConnectAttr() has to be overridden as well (as would
writesSetAttr(), writesSelectAttr(), and so on). This is because each line is
handled separately, and nothing clever is done in the base class'
implementation of
writesConnectAttr(), such as having a default behaviour of only outputting
connectAttrs for nodes that are being output. This gives you the
most flexible control over what will be written.
If you were using this class to save a segmented file, a master
file might have to know about the locations of each of the
segments. If your file saved everything but render layers in one
file, and render layers in another, the first file might need to
contain a pointer to the second, so that when the first file is
loaded the second gets read into memory too. To do this, you
would use
MPxMayaAsciiFilter's ability to write directly to the stream during file output.
You can write to the stream during output by overriding the
methods
writePreCreateNodesBlock(),
writePostCreateNodesBlock() and so on. These give you a simple mechanism to write directly
to the file. Each of these methods take an
MPxMayaAsciiFilterOutput as its only argument. To write to the file, simply use the
output operator (
MPxMayaAsciiFilterOutput::operator<<() ) and output the string you wish.
In the example above, the pointer to the render layer file might
be inserted into the main file after all nodes have been created.
The code to do this would look something like what is shown here:
In the above example, after the createNode block was output, the
line
was output. When the file is read in, Maya would reach the line
above and execute it like any other MEL command. It is assumed in
this example that there would be a custom command plug-in called
importRenderLayerFile which would do the work of actually
importing the layer file.
Note:
MPxMayaAsciiFilter gives you the ability to create your own custom file formats
based on standard Maya ASCII files. However, Autodesk does not
support such custom files as they will not, by definition, be
standard Maya ASCII files.
'''
    def __init__(self):
        pass


    def haveWriteMethod(self): 
        '''
        haveWriteMethod(self) -> bool

        Synopsis
        -----
        Overrides MPxFileTranslator::haveWriteMethod() to indicate that
        this translator has a write method. In general this should not be
        overridden.Reimplemented from MPxFileTranslator.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def haveReadMethod(self): 
        '''
        haveReadMethod(self) -> bool

        Synopsis
        -----
        Overrides MPxFileTranslator::haveReadMethod() to indicate that
        this translator has a read method. In general this should not be
        overridden.Reimplemented from MPxFileTranslator.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def reader(self, file: MFileObject,
                        optionsString: MString,
                        mode: MPxMayaAsciiFilter.FileAccessMode): 
        '''
        reader(self, file: MFileObject,
                        optionsString: MString,
                        mode: MPxMayaAsciiFilter.FileAccessMode)

        Synopsis
        -----
        Reader method for the ascii filter translator. In general this
        should not be overridden, since internal Maya methods are called
        in this method.Note: To process any options passed in in the
        optionsString variable, subclasses should override the
        processReadOptions() method, below.Reimplemented from
        MPxFileTranslator.

        Returns:
        -----
        None

        Parameters:
        -----
        file: MFileObject
        	[in] -> The file to be read 

        optionsString: MString
        	[in] -> Any file options to be handled. Passed to 

        mode: MPxMayaAsciiFilter.FileAccessMode
        	[in] -> The access mode (read or import). Currently this is ignored


        '''
        pass

    def writer(self, file: MFileObject,
                        optionsString: MString,
                        mode: MPxMayaAsciiFilter.FileAccessMode): 
        '''
        writer(self, file: MFileObject,
                        optionsString: MString,
                        mode: MPxMayaAsciiFilter.FileAccessMode)

        Synopsis
        -----
        Writer method for the ascii filter translator. In general this
        should not be overridden, since internal Maya methods are called
        in this method.Note: To process any options passed in in the
        optionsString variable, subclasses should override the
        processWriteOptions() method, below.Reimplemented from
        MPxFileTranslator.

        Returns:
        -----
        None

        Parameters:
        -----
        file: MFileObject
        	[in] -> The file to be read 

        optionsString: MString
        	[in] -> Any file options to be handled. Passed to 

        mode: MPxMayaAsciiFilter.FileAccessMode
        	[in] -> The access mode (save, export, or export active). Currently this is ignored.


        '''
        pass

    def file(self): 
        '''
        file(self) -> const MFileObject

        Synopsis
        -----
        Returns the MFileObject associated with the file currently being
        read or written, allowing access to the file's name, path and so
        on.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def processReadOptions(self, optionsString: MString): 
        '''
        processReadOptions(self, optionsString: MString)

        Synopsis
        -----
        Allows the translator to handle any options passed into the
        reader() method, above. This call is made before the file is
        actually read. The default implementation does nothing.

        Returns:
        -----
        None

        Parameters:
        -----
        optionsString: MString
        	[in] -> The file options to be handled.


        '''
        pass

    def processWriteOptions(self, optionsString: MString): 
        '''
        processWriteOptions(self, optionsString: MString)

        Synopsis
        -----
        Allows the translator to handle any options passed into the
        reader() method, above. This call is made before the file is
        actually read. The default implementation does nothing.

        Returns:
        -----
        None

        Parameters:
        -----
        optionsString: MString
        	[in] -> The file options to be handled.


        '''
        pass

    def writesRequirements(self): 
        '''
        writesRequirements(self) -> bool

        Synopsis
        -----
        Determines if "requires" commands should be written in the file.
        By default true is always returned.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def writesMetadata(self): 
        '''
        writesMetadata(self) -> bool

        Synopsis
        -----
        Asserts that "dataStructure/addMetadata/applyMetadata" commands
        should be written in the file. Normally these are always written
        but you may want to override this to prevent metadata from being
        added to Maya files if you export it in other ways.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def writesCreateNode(self, node: MObject): 
        '''
        writesCreateNode(self, node: MObject) -> bool

        Synopsis
        -----
        Determines if a "createNode" command should be written for a
        particular node. By default this method returns true for all
        nodes.

        Returns: 
        ----- 
        True if the createNode should be written, false otherwise.

        Parameters:
        -----
        node: MObject
        	[in] -> The node in question.


        '''
        pass

    def writesSetAttr(self, srcPlug: MPlug): 
        '''
        writesSetAttr(self, srcPlug: MPlug) -> bool

        Synopsis
        -----
        Determines if a "setAttr" command should be written for a
        particular node. By default this method returns true for all
        plugs.

        Returns: 
        ----- 
        bool true if the setAttr should be written; false otherwise.

        Parameters:
        -----
        srcPlug: MPlug
        	[in] -> The plug to be set.


        '''
        pass

    def writesConnectAttr(self, srcPlug: MPlug,
                        destPlug: MPlug): 
        '''
        writesConnectAttr(self, srcPlug: MPlug,
                        destPlug: MPlug) -> bool

        Synopsis
        -----
        Determines if a "connectAttr" command should be written for a
        particular node. By default this method returns true for all
        connections.

        Returns: 
        ----- 
        bool true if the connectAttr should be written; false otherwise.

        Parameters:
        -----
        srcPlug: MPlug
        	[in] -> The source plug in the connection. 

        destPlug: MPlug
        	[in] -> The destination plug in the connection.


        '''
        pass

    def writesDisconnectAttr(self, srcPlug: MPlug,
                        destPlug: MPlug): 
        '''
        writesDisconnectAttr(self, srcPlug: MPlug,
                        destPlug: MPlug) -> bool

        Synopsis
        -----
        Determines if a "disconnectAttr" command should be written for a
        particular connection. By default this method returns true for
        all connection.

        Returns: 
        ----- 
        bool true if the disconnectAttr should be written; false
        otherwise.

        Parameters:
        -----
        srcPlug: MPlug
        	[in] -> The source plug in the connection. 

        destPlug: MPlug
        	[in] -> The destination plug in the connection.


        '''
        pass

    def writesParentNode(self, parent: MDagPath,
                        child: MDagPath): 
        '''
        writesParentNode(self, parent: MDagPath,
                        child: MDagPath) -> bool

        Synopsis
        -----
        Determines if a "parent" command should be written for a
        particular parent and child. By default this method returns true
        for all parents and children.

        Returns: 
        ----- 
        bool true if the disconnectAttr should be written; false
        otherwise.

        Parameters:
        -----
        parent: MDagPath
        	[in] -> The dag path to the parent. 

        child: MDagPath
        	[in] -> The dag path to the child.


        '''
        pass

    def writesSelectNode(self, node: MObject): 
        '''
        writesSelectNode(self, node: MObject) -> bool

        Synopsis
        -----
        Determines if a "select" command should be written for a
        particular node. By default this method returns true for all
        nodes.

        Returns: 
        ----- 
        bool true if the select should be written; false otherwise.

        Parameters:
        -----
        node: MObject
        	[in] -> The node to select


        '''
        pass

    def writesFileReference(self, referenceFile: MFileObject): 
        '''
        writesFileReference(self, referenceFile: MFileObject) -> bool

        Synopsis
        -----
        Determines if a "fileReference" command should be written for a
        file. By default this method returns true for all files.

        Returns: 
        ----- 
        bool true if the fileReference should be written; false
        otherwise.

        Parameters:
        -----
        referenceFile: MFileObject
        	[in] -> The file to be referenced.


        '''
        pass

    def writePostHeader(self, filterOutput: MPxMayaAsciiFilterOutput): 
        '''
        writePostHeader(self, filterOutput: MPxMayaAsciiFilterOutput)

        Synopsis
        -----
        Allows data to be written out to the file after the header block.
        By default this method does nothing.

        Returns:
        -----
        None

        Parameters:
        -----
        filterOutput: MPxMayaAsciiFilterOutput
        	[in] -> the output stream to be written to (using the << operator)


        '''
        pass

    def writePostRequires(self, filterOutput: MPxMayaAsciiFilterOutput): 
        '''
        writePostRequires(self, filterOutput: MPxMayaAsciiFilterOutput)

        Synopsis
        -----
        Allows data to be written out to the file after the requires
        block. By default this method does nothing.

        Returns:
        -----
        None

        Parameters:
        -----
        filterOutput: MPxMayaAsciiFilterOutput
        	[in] -> the output stream to be written to (using the << operator)


        '''
        pass

    def writePreCreateNodesBlock(self, filterOutput: MPxMayaAsciiFilterOutput): 
        '''
        writePreCreateNodesBlock(self, filterOutput: MPxMayaAsciiFilterOutput)

        Synopsis
        -----
        Allows data to be written out to the file before the create nodes
        block. By default this method does nothing.

        Returns:
        -----
        None

        Parameters:
        -----
        filterOutput: MPxMayaAsciiFilterOutput
        	[in] -> the output stream to be written to (using the << operator)


        '''
        pass

    def writePostCreateNodesBlock(self, filterOutput: MPxMayaAsciiFilterOutput): 
        '''
        writePostCreateNodesBlock(self, filterOutput: MPxMayaAsciiFilterOutput)

        Synopsis
        -----
        Allows data to be written out to the file after the create nodes
        block. By default this method does nothing.

        Returns:
        -----
        None

        Parameters:
        -----
        filterOutput: MPxMayaAsciiFilterOutput
        	[in] -> the output stream to be written to (using the << operator)


        '''
        pass

    def writePreConnectAttrsBlock(self, filterOutput: MPxMayaAsciiFilterOutput): 
        '''
        writePreConnectAttrsBlock(self, filterOutput: MPxMayaAsciiFilterOutput)

        Synopsis
        -----
        Allows data to be written out to the file before the connect
        attrs block. By default this method does nothing.

        Returns:
        -----
        None

        Parameters:
        -----
        filterOutput: MPxMayaAsciiFilterOutput
        	[in] -> the output stream to be written to (using the << operator)


        '''
        pass

    def writePostConnectAttrsBlock(self, filterOutput: MPxMayaAsciiFilterOutput): 
        '''
        writePostConnectAttrsBlock(self, filterOutput: MPxMayaAsciiFilterOutput)

        Synopsis
        -----
        Allows data to be written out to the file after the connect attrs
        block. By default this method does nothing.

        Returns:
        -----
        None

        Parameters:
        -----
        filterOutput: MPxMayaAsciiFilterOutput
        	[in] -> the output stream to be written to (using the << operator)


        '''
        pass

    def writePreTrailer(self, filterOutput: MPxMayaAsciiFilterOutput): 
        '''
        writePreTrailer(self, filterOutput: MPxMayaAsciiFilterOutput)

        Synopsis
        -----
        Allows data to be written out to the file before the trailer
        block. By default this method does nothing.

        Returns:
        -----
        None

        Parameters:
        -----
        filterOutput: MPxMayaAsciiFilterOutput
        	[in] -> the output stream to be written to (using the << operator)


        '''
        pass

class MPxMayaAsciiFilterOutput:
    '''Wrapper for a Maya Ascii file output stream.
MPxMayaAsciiFilterOutput is used in conjunction with
MPxMayaAsciiFilter to allow output to the Maya ASCII file. Instances of this class
may only be instantiated through the methods of
MPxMayaAsciiFilter.
'''
    def __init__(self):
        pass


class MPxMidiInputDevice:
    '''Midi input device.
This is the base class for user defined MIDI input devices.
Child classes of
MPxMidiInputDevice should define:
'''
    def __init__(self):
        pass


    def openDevice(self): 
        '''
        openDevice(self)

        Synopsis
        -----
        Open the midi device.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def sendMessage(self, messageType: char,
                        messageParams: char): 
        '''
        sendMessage(self, messageType: char,
                        messageParams: char)

        Synopsis
        -----
        If this midi event belongs to this device then fiil up the
        MDeviceState. Otherwise return NULL. The user should override
        this method.User should override this method.

        Returns:
        -----
        None

        Parameters:
        -----
        messageType: char
        	[in] -> Message to send. 

        messageParams: char
        	[in] -> Message parameters.


        '''
        pass

    def getMessage(self, messageType: char,
                        messageResponse: char): 
        '''
        getMessage(self, messageType: char,
                        messageResponse: char) -> char*

        Synopsis
        -----
        User should override this method.

        Returns:
        -----
        None

        Parameters:
        -----
        messageType: char
        	[in] -> 

        messageResponse: char
        	[out] -> 


        '''
        pass

    def doButtonEvents(self, val: bool): 
        '''
        doButtonEvents(self, val: bool)

        Synopsis
        -----
        This method is used to specify whether this device is accepting
        button events from its child.

        Returns:
        -----
        None

        Parameters:
        -----
        val: bool
        	[in] -> 


        '''
        pass

    def doMovementEvents(self, val: bool): 
        '''
        doMovementEvents(self, val: bool)

        Synopsis
        -----
        This method is used to specify whether this device is accepting
        movement input from its child.

        Returns:
        -----
        None

        Parameters:
        -----
        val: bool
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

    def setNamedButton(self, buttonName: MString,
                        button: short): 
        '''
        setNamedButton(self, buttonName: MString,
                        button: short)

        Synopsis
        -----
        Set the name of the specified button.

        Returns:
        -----
        None

        Parameters:
        -----
        buttonName: MString
        	[in] -> Name of button. 

        button: short
        	[in] -> Index of button. 


        '''
        pass

    def addChannel(self, channel: MDeviceChannel): 
        '''
        addChannel(self, channel: MDeviceChannel)

        Synopsis
        -----
        Add the given channel to this device.

        Returns:
        -----
        None

        Parameters:
        -----
        channel: MDeviceChannel
        	[in] -> Channel to add. 


        '''
        pass

    def setDegreesOfFreedom(self, freedom: int): 
        '''
        setDegreesOfFreedom(self, freedom: int)

        Synopsis
        -----
        Set the degrees of freedom for this device.

        Returns:
        -----
        None

        Parameters:
        -----
        freedom: int
        	[in] -> New degrees of freedom value. 


        '''
        pass

    def setNumberOfButtons(self, buttons: int): 
        '''
        setNumberOfButtons(self, buttons: int)

        Synopsis
        -----
        Set the number of buttons for this device.

        Returns:
        -----
        None

        Parameters:
        -----
        buttons: int
        	[in] -> New number of buttons. 


        '''
        pass

class MPxModelEditorCommand:
    '''Base class for editor creation commands.
MPxModelEditorCommand is the base class for user defined model editor commands. This
command gives all of the flags and options of the modelEditor
command in addition to any user defined flags or behaviours. When
registering this command, use the
MFnPlugin::MFnPlugin::registerModelEditorCommand() method. A
MPx3dModelView is also required to be used with
MPxModelEditorCommand and is specified when the
MPxModelEditorCommand is registered.
'''
    def __init__(self):
        pass


    def doEditFlags(self): 
        '''
        doEditFlags(self)

        Synopsis
        -----
        This method is called when the command is called in edit mode.
        This method should be overridden by panel commands to determine
        which edit flags are set in conjunction with the argument parser
        for this command. The argument parser for this command can be
        obtained by calling the parser method. If the command is called
        with both the edit flag and the query flag, then the query flag
        will be ignored.If the command returns MS::kUnknownParameter, the
        flag is processed by the parent class.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def doQueryFlags(self): 
        '''
        doQueryFlags(self)

        Synopsis
        -----
        This method is called when the command is called in query mode.
        This method should be overridden by panel commands to determine
        which query flags are set in conjunction with the argument parser
        for this command. The argument parser for this command can be
        obtained by calling the parser method. If the command is called
        with both the edit flag and the query flag, then the query flag
        will be ignored.If the command returns MS::kUnknownParameter, the
        flag is processed by the parent class.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def appendSyntax(self): 
        '''
        appendSyntax(self)

        Synopsis
        -----
        This method should be overridden to append syntax to the panel
        command. The syntax object can be obtained by calling the syntax
        method. The following flags cannot be used as user-defined flags
        as they are reserved for edit and query: "-e", "-edit", "-q",
        "-query".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def skipFlagForCreate(self, longFlag: MString): 
        '''
        skipFlagForCreate(self, longFlag: MString) -> bool

        Synopsis
        -----
        Returns true if the passed long flag name should be skipped
        during the creation portion of the command.

        Returns: 
        ----- 
        Return true if the flag shoiuld be skipped during creation.

        Parameters:
        -----
        longFlag: MString
        	[in] -> The string containing the long flag name.


        '''
        pass

    @overload
    def setResult(self, result: bool): 
        '''
        setResult(self, result: bool)

        Synopsis
        -----
        This method should be called when the result of the panel command
        is a boolean.

        Returns:
        -----
        None

        Parameters:
        -----
        result: bool
        	[out] -> the boolean result


        '''
        pass

    @overload
    def setResult(self, result: int): 
        '''
        setResult(self, result: int)

        Synopsis
        -----
        This method should be called when the result of the panel command
        is an integer.

        Returns:
        -----
        None

        Parameters:
        -----
        result: int
        	[out] -> the integer result


        '''
        pass

    @overload
    def setResult(self, result: double): 
        '''
        setResult(self, result: double)

        Synopsis
        -----
        This method should be called when the result of the panel command
        is a double.

        Returns:
        -----
        None

        Parameters:
        -----
        result: double
        	[out] -> the double result


        '''
        pass

    @overload
    def setResult(self, result: MString): 
        '''
        setResult(self, result: MString)

        Synopsis
        -----
        This method should be called when the result of the panel command
        is a string.

        Returns:
        -----
        None

        Parameters:
        -----
        result: MString
        	[out] -> the string result


        '''
        pass

    @overload
    def setResult(self, result: MStringArray): 
        '''
        setResult(self, result: MStringArray)

        Synopsis
        -----
        This method should be called when the result of the panel command
        is a string array.

        Returns:
        -----
        None

        Parameters:
        -----
        result: MStringArray
        	[out] -> the string array result


        '''
        pass

    @overload
    def setResult(self, result: MDoubleArray): 
        '''
        setResult(self, result: MDoubleArray)

        Synopsis
        -----
        This method should be called when the result of the panel command
        is a double array.

        Returns:
        -----
        None

        Parameters:
        -----
        result: MDoubleArray
        	[out] -> the double array result


        '''
        pass

    @overload
    def setResult(self, result: MIntArray): 
        '''
        setResult(self, result: MIntArray)

        Synopsis
        -----
        This method should be called when the result of the panel command
        is an integer array.

        Returns:
        -----
        None

        Parameters:
        -----
        result: MIntArray
        	[out] -> the integer array result


        '''
        pass

    def editorCommandName(self): 
        '''
        editorCommandName(self) -> MString

        Synopsis
        -----
        Returns the name of editor command. The user should override this
        method to return the name of their model editor command. This
        method is called when the model editor is being created and is
        used to be able to associate this command's name with that model
        editor.Currently this association is used by playblast to call
        the appropriate plugin model editor command to provide
        information for the (-cameraSetup) flag. An override for this
        method and an override for the doQueryFlags() method must be
        provided to support multiple camera rendering via playblast.Refer
        the the documentation on the modelEditor command for further
        information about the -cameraSetup flag.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def editorMenuScriptName(self): 
        '''
        editorMenuScriptName(self) -> MString

        Synopsis
        -----
        Returns the name of the script that should get executed to
        construct the menu for the editor. The script should take a
        string argument that holds the name of the created editor.If no
        script is passed, the created editor will not have a menu.

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

    def syntax(self, ReturnStatus: MPxModelEditorCommand.MStatus): 
        '''
        syntax(self, ReturnStatus: MPxModelEditorCommand.MStatus) -> MSyntax

        Synopsis
        -----
        USE _syntax() IN SCRIPT. This method returns the syntax object of
        this panel command.The syntax object can be appended to in an
        overridden version of the appendSyntax method.

        Returns: 
        ----- 
        The syntax object

        Parameters:
        -----
        ReturnStatus: MPxModelEditorCommand.MStatus
        	[out] -> return status


        '''
        pass

    def parser(self, ReturnStatus: MPxModelEditorCommand.MStatus): 
        '''
        parser(self, ReturnStatus: MPxModelEditorCommand.MStatus) -> MArgParser

        Synopsis
        -----
        USE _parser() IN SCRIPT. This method returns the argument parser
        of this panel command.The argument parser can be used in the
        overridden versions of doEditFlags and doQueryFlags to determine
        which flags are set.

        Returns: 
        ----- 
        The argument parser

        Parameters:
        -----
        ReturnStatus: MPxModelEditorCommand.MStatus
        	[out] -> return status


        '''
        pass

class MPxMotionPathNode:
    '''Base class for user defined motionPath nodes.
MPxMotionPathNode provides you with the ability to write your own motion path
classes. A custom motionPath node provides access to Maya's
internal motionPath engine while at the same time allows you to
extend the functionality in ways that are not possible with the
motionPath node.
There are two basic ways to work with the methods available in
this class. The first way is to mimic how Maya's motionPath node
works and then augment the result. You do this by calling the
 method with values you either read from the input plugs or
modified yourself, and the method returns the location and
orientation on the path.
The second way of working is to use the individual a-la-carte
evaluator methods provided in this class to invoke the motionPath
engine on a piecemeal basis. For example, you might call
 to calculate the location on the path, then
 to compute the coordinate space vectors, then offset the
position along those vectors, then call
 to "tilt" the result. The example plug-in "motionPathNode.cpp"
found in the API Developer's Toolkit provides an example of using
the a-la-carte evaluation scheme to add sinusoidal offsets to the
computed result.
Here are some examples of how you might use a custom motionPath
node:
The example plug-in, "motionPathNode.cpp" found in the API
Developer's Toolkit provides a great starting point for exploring
the capabilities of the
MPxMotionPathNode class.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MPxNode.MPxNode

        Synopsis
        -----
        Returns the type of node that this is. This is used to
        differentiate user defined nodes that are derived off different
        MPx base classes.It is not necessary to override this
        method.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def position(self, data: MDataBlock,
                        frac: double,
                        ReturnStatus: MPxMotionPathNode.MStatus): 
        '''
        position(self, data: MDataBlock,
                        frac: double,
                        ReturnStatus: MPxMotionPathNode.MStatus) -> MPoint

        Synopsis
        -----
        This method returns the position on the path associated with the
        motionPath node at a specified fractional distance along the
        path. This method is designed to be called from within your
        compute() method and requires an MDataBlock (`data') to access
        the path. Typically you would pass in the current value of the
        `uValue' plug to get the current location on the path. However,
        you could offset the value to get a position ahead of you on the
        path, for example to simulate someone leaning ahead of time to
        anticpate an upcoming curve on a roller-coaster.

        Returns: 
        ----- 
        If successful, returns the calculated position on the path
        occurring at `frac'. If unsuccessful, a zero value is returned
        and ReturnStatus reports an error code.

        Parameters:
        -----
        data: MDataBlock
        	[in] -> is the data block for the computation. 

        frac: double
        	[in] -> the fraction of the length along the path to sample at. The value is specified in 0 to 1 range where 0 represents the start of the path and 1 the end of the path. Values within the 0 to 1 range are unchanged. Values outside the range are clamped. If you instead have a parametric value for position on the path, use parameterToFractional() to convert the value to a fractional amount. 

        ReturnStatus: MPxMotionPathNode.MStatus
        	[out] -> Status Code.


        '''
        pass

    def getVectors(self, data: MDataBlock,
                        frac: double,
                        front: MVector,
                        side: MVector,
                        up: MVector,
                        worldUp: MVector): 
        '''
        getVectors(self, data: MDataBlock,
                        frac: double,
                        front: MVector,
                        side: MVector,
                        up: MVector,
                        worldUp: MVector)

        Synopsis
        -----
        Calculate the orientation on the motion path at the fractional
        distance `frac' along the path. The returned vectors form an
        orthogonal basis oriented on the path. Only the path and
        `worldUp' factor into the calculation. Additional rotation
        parameters such as banking and twist are not applied here (see
        the example plug-in motionPathNode.cpp for details of how to
        apply these).

        Returns:
        -----
        None

        Parameters:
        -----
        data: MDataBlock
        	[in] -> is the data block for the computation. 

        frac: double
        	[in] -> the fraction of the length along the path to sample at. The value is specified in 0 to 1 range where 0 represents the start of the path and 1 the end of the path. Values within the 0 to 1 range are unchanged. Values outside the range are clamped. If you instead have a parametric value for position on the path, use parameterToFractional() to convert the value to a fractional amount. 

        front: MVector
        	[out] -> returns the forward direction of motion. 

        side: MVector
        	[out] -> returns the vector perpendicular to the motion. 

        up: MVector
        	[out] -> returns the vector perpendicular to the motion. 

        worldUp: MVector
        	[in] -> is an optional parameter which specifies the direction that the computed `up' vector should point. The `front' vector always points along the path, and the `up' vector perpendicular to it in the `worldUp' direction. To instead use the normal to the path, specify NULL.


        '''
        pass

    def banking(self, data: MDataBlock,
                        frac: double,
                        worldUp: MVector,
                        bankScale: double,
                        bankLimit: double,
                        ReturnStatus: MPxMotionPathNode.MStatus): 
        '''
        banking(self, data: MDataBlock,
                        frac: double,
                        worldUp: MVector,
                        bankScale: double,
                        bankLimit: double,
                        ReturnStatus: MPxMotionPathNode.MStatus) -> MQuaternion

        Synopsis
        -----
        Calculate the banking on the motion path at the fractional
        distance `frac' along the path. Banking is a supplemental
        rotation about the direction of motion that can be added to the
        orientation obtained from getVectors. A typical use is to apply
        the result value to the up vector then cross the front vector and
        new up vector to obtain the new side vector.

        Returns: 
        ----- 
        If successful, returns the calculated rotation due to banking on
        the path at `frac'. If unsuccessful, a unit quaternion is
        returned and ReturnStatus reports an error code.

        Parameters:
        -----
        data: MDataBlock
        	[in] -> is the data block for the computation. 

        frac: double
        	[in] -> the fraction of the length along the path to sample at. The value is specified in 0 to 1 range where 0 represents the start of the path and 1 the end of the path. Values within the 0 to 1 range are unchanged. Values outside the range are clamped. If you instead have a parametric value for position on the path, use parameterToFractional() to convert the value to a fractional amount. 

        worldUp: MVector
        	[in] -> The "up" direction. Typically the world up, but could instead be the normal to a surface, for example. 

        bankScale: double
        	[in] -> causes the effect of banking to be more (or less pronounced). A value of 2.0 causes twice the amount of banking. The value can be negative to compute the oppositive of a "lean-in" effect. 

        bankLimit: double
        	[in] -> provides a threshold above which the banking effect is clamped. 

        ReturnStatus: MPxMotionPathNode.MStatus
        	[out] -> Status Code.


        '''
        pass

    def evaluatePath(self, data: MDataBlock,
                        u: double,
                        uRange: double,
                        wraparound: bool,
                        sideOffset: double,
                        upOffset: double,
                        follow: bool,
                        inverseFront: bool,
                        inverseUp: bool,
                        frontAxisIdx: int,
                        upAxisIdx: int,
                        frontTwist: double,
                        upTwist: double,
                        sideTwist: double,
                        bank: bool,
                        bankScale: double,
                        bankLimit: double,
                        resultPosition: MPoint,
                        resultOrientation: MMatrix): 
        '''
        evaluatePath(self, data: MDataBlock,
                        u: double,
                        uRange: double,
                        wraparound: bool,
                        sideOffset: double,
                        upOffset: double,
                        follow: bool,
                        inverseFront: bool,
                        inverseUp: bool,
                        frontAxisIdx: int,
                        upAxisIdx: int,
                        frontTwist: double,
                        upTwist: double,
                        sideTwist: double,
                        bank: bool,
                        bankScale: double,
                        bankLimit: double,
                        resultPosition: MPoint,
                        resultOrientation: MMatrix)

        Synopsis
        -----
        Callable from your custom plug-ins compute() method to evaluate
        the path at the specified location. This method provides an
        alternate to using the a-la-carte evaluator access provided
        elsewhere in this class (e.g. position()). Use this method if you
        want to emulate the evaluation as performed by the motionPath
        node as opposed to chaining several a-la-carte methods together.

        Returns:
        -----
        None

        Parameters:
        -----
        data: MDataBlock
        	[in] -> is the data block for the computation. 

        u: double
        	[in] -> the locaion on the path to sample. See the 

        uRange: double
        	[in] -> defines how the 

        wraparound: bool
        	[in] -> true means that when values go past the end of the path they wrap around to the other end. If false, values are clamped to the ends of the path. 

        sideOffset: double
        	[in] -> The amount to offset the computed position from the path. The offset is applied along the horizontal axis to the path. 

        upOffset: double
        	[in] -> The amount to offset the computed position from the path. The offset is applied along the vertical axis to the path. 

        follow: bool
        	[in] -> If true, orientation aligns to the path direction. If false, orientation is fixed. 

        inverseFront: bool
        	[in] -> If true, the front direction is negated. 

        inverseUp: bool
        	[in] -> If true, the uo direction is negated. 

        frontAxisIdx: int
        	[out] -> an index (x-0, y=1, z=2) specifying which local axis of the result is aligned to the front direction. 

        upAxisIdx: int
        	[out] -> an index (x-0, y=1, z=2) specifying which local axis of the result is aligned to the up direction. 

        frontTwist: double
        	[in] -> the amount of roll to add to the computed orientation. 

        upTwist: double
        	[in] -> the amount of yaw to add to the computed orientation. 

        sideTwist: double
        	[in] -> the amount of pitch to add to the computed orientation. 

        bank: bool
        	[in] -> if true, the computed orientation will be offset by a bank value derived from the tightness of the path at the sampled point. 

        bankScale: double
        	[in] -> a multiplier on the banking calculation. For example, a value of two will double the banking effect. Negative values are permitted. 

        bankLimit: double
        	[in] -> a threshold to specify that banking effect is clamped past the limit amount. 

        resultPosition: MPoint
        	[out] -> the computed sample position on the path. 

        resultOrientation: MMatrix
        	[out] -> the computed sample orientation on the path.


        '''
        pass

    def parametricToFractional(self, u: double,
                        ReturnStatus: MPxMotionPathNode.MStatus): 
        '''
        parametricToFractional(self, u: double,
                        ReturnStatus: MPxMotionPathNode.MStatus) -> double

        Synopsis
        -----
        Converts a parametric location on the path curve to the
        corresponding fraction of the total path curve length. The
        resulting fractional value will be 0.0 at the start of the path,
        1.0 at the end of the path, and values betwixt the start and end
        being proportionately positioned based on arc length. If `u'
        preceeds the start or succeeds the end of the curve then the
        returned value will be outside the 0 to 1 range.

        Returns: 
        ----- 
        If successful, returns the calculated fractional value
        corresponding to the parametric value `u'. If unsuccessful, -1.0
        is returned and ReturnStatus reports an error code.

        Parameters:
        -----
        u: double
        	[in] -> the location along the path curve in parametric space to convert to a fractional value. 

        ReturnStatus: MPxMotionPathNode.MStatus
        	[out] -> Status Code.


        '''
        pass

    def fractionalToParametric(self, frac: double,
                        ReturnStatus: MPxMotionPathNode.MStatus): 
        '''
        fractionalToParametric(self, frac: double,
                        ReturnStatus: MPxMotionPathNode.MStatus) -> double

        Synopsis
        -----
        Converts a fractional location on the path curve to the
        corresponding parametric location. This method is the converse of
        parametricToFractional().

        Returns: 
        ----- 
        If successful, returns the calculated parametric location that is
        equivalent to the fractional value `frac'. If unsuccessful, -1.0
        is returned and ReturnStatus reports an error code.

        Parameters:
        -----
        frac: double
        	[in] -> the location along the path curve as a fraction of the total length of the path. A value of zero represents the start of the path, one represents the end of the path, and values betwixt zero and one represent the proportionate distance along the path in arc length. 

        ReturnStatus: MPxMotionPathNode.MStatus
        	[out] -> Status Code.


        '''
        pass

    def wraparoundFractionalValue(self, f: double,
                        ReturnStatus: MPxMotionPathNode.MStatus): 
        '''
        wraparoundFractionalValue(self, f: double,
                        ReturnStatus: MPxMotionPathNode.MStatus) -> double

        Synopsis
        -----
        Given the fractional distance `frac' along the path, this method
        checks if the value goes beyond the 0 to 1 range and if so
        chooses the appropriate value to continue the motion on the
        opposing end of the path such that the motion will appear to
        "wrap around" the beginning (or end) of the path as appropriate.
        For example, a value of -0.2 will return the result 0.8.

        Returns: 
        ----- 
        If successful, returns the remapped fractional value in the 0 - 1
        range. If unsuccessful, -1.0 is returned and ReturnStatus reports
        an error code.

        Parameters:
        -----
        f: double
        	[in] -> the fraction of the length along the path to sample at. The value is specified in 0 to 1 range where 0 represents the start of the path and 1 the end of the path. Values within the 0 to 1 range are unchanged. Values outside the range are wrapped around. 

        ReturnStatus: MPxMotionPathNode.MStatus
        	[out] -> Status Code.


        '''
        pass

    def matrix(self, front: MVector,
                        side: MVector,
                        up: MVector,
                        frontAxisIdx: int,
                        upAxisIdx: int,
                        ReturnStatus: MPxMotionPathNode.MStatus): 
        '''
        matrix(self, front: MVector,
                        side: MVector,
                        up: MVector,
                        frontAxisIdx: int,
                        upAxisIdx: int,
                        ReturnStatus: MPxMotionPathNode.MStatus) -> MMatrix

        Synopsis
        -----
        Create a matrix given vector space specified by the three
        orthogonal input vectors. The resulting matrix will be a rotation
        matrix that aligns data with the given vector space. The vectors
        should be normalised and must be orthogonal, otherwise an error
        will be returned.

        Returns: 
        ----- 
        If successful, returns the calculated rotation matrix. If
        unsuccessful, the identity matrix is returned and ReturnStatus
        reports an error code.

        Parameters:
        -----
        front: MVector
        	[in] -> is the first vector. 

        side: MVector
        	[in] -> is the second vector. 

        up: MVector
        	[in] -> is the third vector. 

        frontAxisIdx: int
        	[out] -> an optional index (x=0, y=1, z=2) specifying which local axis of the result is aligned to the front direction. The default is 1. 

        upAxisIdx: int
        	[out] -> an optional index (x=0, y=1, z=2) specifying which local axis of the result is aligned to the up direction. The default is 2. 

        ReturnStatus: MPxMotionPathNode.MStatus
        	[out] -> Status Code.


        '''
        pass

    def thisMObject(self): 
        '''
        thisMObject(self) -> MObject

        Synopsis
        -----
        Returns the MObject associated with this user defined node. This
        makes it possible to use MFnDependencyNode or to construct plugs
        to this node's attributes.It is not necessary to override this
        method.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class worldUpVectorValue:
    '''possible values for worldUpType 
    Non-functional class.  Values for this enum:
    kUpScene
    kUpObject
    kUpObjectRotation
    kUpVector
    kUpNormal
    '''

    def __init__(self):
        pass

    def kUpScene(self):
        '''This is an enum of worldUpVectorValue.
        - Description: Use the scene up vector as world up. 
        - Value: 0
        '''
        pass

    def kUpObject(self):
        '''This is an enum of worldUpVectorValue.
        - Description: Use the object's up vector as world up. 
        - Value: 1
        '''
        pass

    def kUpObjectRotation(self):
        '''This is an enum of worldUpVectorValue.
        - Description: Use the object's rotation up vector as world up. 
        - Value: 2
        '''
        pass

    def kUpVector(self):
        '''This is an enum of worldUpVectorValue.
        - Description: Use the value of the worldUpVector plug as world up. 
        - Value: 3
        '''
        pass

    def kUpNormal(self):
        '''This is an enum of worldUpVectorValue.
        - Description: Use the path normal world up. 
        - Value: 4
        '''
        pass

class MPxMultiPolyTweakUVCommand:
    '''Base class used for moving UV's on multiple objects.
This is the base class for UV editing commands on multiple
polygonal objects.
The purpose of this command class is to simplify the process of
moving UVs on multiple polygonal objects. The use is only
required to provide the new positions of the UVs that have been
modified.
'''
    def __init__(self):
        pass


    def parseSyntax(self, argData: MArgDatabase): 
        '''
        parseSyntax(self, argData: MArgDatabase)

        Synopsis
        -----
        This method parses the additional flags before the command is
        executed.

        Returns:
        -----
        None

        Parameters:
        -----
        argData: MArgDatabase
        	[in] -> Arguments passed to command.


        '''
        pass

    def preProcessUVs(self, mesh: MObject,
                        uvList: MIntArray): 
        '''
        preProcessUVs(self, mesh: MObject,
                        uvList: MIntArray)

        Synopsis
        -----
        This pre-processes UVs.

        Returns:
        -----
        None

        Parameters:
        -----
        mesh: MObject
        	[in] -> The mesh object to be modified 

        uvList: MIntArray
        	[in] -> The list of UV Ids selected by the user.


        '''
        pass

    def getTweakedUVs(self, mesh: MObject,
                        uvList: MIntArray,
                        uPos: MFloatArray,
                        vPos: MFloatArray): 
        '''
        getTweakedUVs(self, mesh: MObject,
                        uvList: MIntArray,
                        uPos: MFloatArray,
                        vPos: MFloatArray)

        Synopsis
        -----
        This computes and returns modified UVs.

        Returns:
        -----
        None

        Parameters:
        -----
        mesh: MObject
        	[in] -> The mesh object to be modified 

        uvList: MIntArray
        	[in] -> The list of UV Ids selected by the user. The method is allowed to change uvList on output. 

        uPos: MFloatArray
        	[out] -> The new u values corresponding to the indices listed in 

        vPos: MFloatArray
        	[out] -> The new v values corresponding to the indices listed in 


        '''
        pass

class MPxNode:
    '''Base class for user defined dependency nodes.
MPxNode is the the parent class for user defined dependency nodes. A
dependency node is an object that resides in the dependency
graph. It computes output attributes based on a set of input
attributes. When an input changes, the compute method is called
for each dependent output.
The dependency graph is made up of nodes that have connections
between their attributes. When an attribute changes,
recomputation propagates through the graph until all affected
values have been updated.
When writing a dependency node, there is a very basic rule that
should be observed. The outputs should be calculated only using
the values of the inputs. All information about the world outside
the node should come from input attributes. If this rule is not
observed, then the results may be unpredictable.
Developers must decide whether to support the
 setting of the
 attribute. {
 means that a node should pass through all data without
performing computations on it. For example, a deformer node will
pass geometry through unmodified when
 is set to
. It is up the the plug-in writer to observe the
 if it is relevant to the type of node.
'''
    def __init__(self):
        pass


    def postConstructor(self): 
        '''
        postConstructor(self)

        Synopsis
        -----
        Post constructor. Internally maya creates two objects when a user
        defined node is created, the internal MObject and the user
        derived object. The association between the these two objects is
        not made until after the MPxNode constructor is called. This
        implies that no MPxNode member function can be called from the
        MPxNode constructor. The postConstructor will get called
        immediately after the constructor when it is safe to call any
        MPxNode member function. Reimplemented in MPxTransform, and
        MPxPolyTrg.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def compute(self, plug: MPlug,
                        block: MDataBlock): 
        '''
        compute(self, plug: MPlug,
                        block: MDataBlock)

        Synopsis
        -----
        This method should be overridden in user defined nodes. Recompute
        the given output based on the nodes inputs. The plug represents
        the data value that needs to be recomputed, and the data block
        holds the storage for all of the node's attributes.The MDataBlock
        will provide smart handles for reading and writing this node's
        attribute values. Only these values should be used when
        performing computations.When evaluating the dependency graph,
        Maya will first call the compute method for this node. If the
        plug that is provided to the compute indicates that the attribute
        was defined by the Maya parent node, the compute method should
        return MS::kUnknownParameter. When this occurs, Maya will call
        the internal Maya node from which the user-defined node is
        derived to compute the plug's value.This means that a user
        defined node does not need to be concerned with computing
        inherited output attributes. However, if desired, these can be
        safely recomputed by this method to change the behaviour of the
        node.Reimplemented in MPxTransform, MPxPolyTrg, MPxEmitterNode,
        MPxFieldNode, MPxFluidEmitterNode, and
        MPxParticleAttributeMapperNode.

        Returns:
        -----
        None

        Parameters:
        -----
        plug: MPlug
        	[in] -> plug representing the attribute that needs to be recomputed 

        block: MDataBlock
        	[out] -> data block containing storage for the node's attributes


        '''
        pass

    def getInternalValue(self, plug: MPlug,
                        dataHandle: MDataHandle): 
        '''
        getInternalValue(self, plug: MPlug,
                        dataHandle: MDataHandle) -> bool

        Synopsis
        -----
        This method is overridden by nodes that store attribute data in
        some internal format. The internal state of attributes can be set
        or queried using the setInternal and internal methods of
        MFnAttribute.When internal attribute values are queried via
        getAttr or MPlug::getValue this method is called.

        Returns: 
        ----- 
        true the attribute was placed in the datablock  false could not
        handle the specified attribute, pass this request to the default
        handler

        Parameters:
        -----
        plug: MPlug
        	[in] -> the attribute that is being queried 

        dataHandle: MDataHandle
        	[out] -> the dataHandle to store the attribute value


        '''
        pass

    def setInternalValue(self, plug: MPlug,
                        dataHandle: MDataHandle): 
        '''
        setInternalValue(self, plug: MPlug,
                        dataHandle: MDataHandle) -> bool

        Synopsis
        -----
        This method is overridden by nodes that store attribute data in
        some internal format. The internal state of attributes can be set
        or queried using the setInternal and internal methods of
        MFnAttribute.When internal attribute values are set via setAttr
        or MPlug::setValue this method is called.Another use for this
        method is to impose attribute limits.

        Returns:
        -----
        None

        Parameters:
        -----
        plug: MPlug
        	[in] -> the attribute that is being set 

        dataHandle: MDataHandle
        	[in] -> the dataHandle containing the value to set 


        '''
        pass

    def internalArrayCount(self, plug: MPlug): 
        '''
        internalArrayCount(self, plug: MPlug) -> int

        Synopsis
        -----
        This method is overridden by nodes that have internal array
        attributes which are not stored in Maya's datablock. This method
        is used by Maya to determine the non-sparse count of array
        elements during file io. If the internal array is stored
        sparsely, you should return the maximum index of the array plus
        one. If the internal array is non-sparse then return the length
        of the array.This method does not need to be implemented for
        attributes that are stored in the datablock since Maya will use
        the datablock size.If this method is overridden, it should return
        -1 for attributes which it does not handle. Maya will use the
        datablock size to determine the array length when -1 is returned.

        Returns:
        -----
        None

        Parameters:
        -----
        plug: MPlug
        	[in] -> the array plug 


        '''
        pass

    def copyInternalData(self, node: MPxNode): 
        '''
        copyInternalData(self, node: MPxNode)

        Synopsis
        -----
        This method is overridden by nodes that store attribute data in
        some internal format. On duplication this method is called on the
        duplicated node with the node being duplicated passed as the
        parameter. Overriding this method gives your node a chance to
        duplicate any internal data you've been storing and manipulating
        outside of normal attribute data.Reimplemented in MPxTransform.

        Returns:
        -----
        None

        Parameters:
        -----
        node: MPxNode
        	[in] -> the node that is being duplicated 


        '''
        pass

    def legalConnection(self, plug: MPlug,
                        otherPlug: MPlug,
                        asSrc: bool,
                        isLegal: bool): 
        '''
        legalConnection(self, plug: MPlug,
                        otherPlug: MPlug,
                        asSrc: bool,
                        isLegal: bool)

        Synopsis
        -----
        This method allows you to check for legal connections being made
        to attributes of this node. You should return kUnknownParameter
        to specify that maya should handle this connection if you are
        unable to determine if it is legal.

        Returns:
        -----
        None

        Parameters:
        -----
        plug: MPlug
        	[in] -> attribute on this node 

        otherPlug: MPlug
        	[in] -> attribute on other node 

        asSrc: bool
        	[in] -> is this plug a source of the connection 

        isLegal: bool
        	[in] -> set this to true if the connection is legal, false otherwise


        '''
        pass

    def legalDisconnection(self, plug: MPlug,
                        otherPlug: MPlug,
                        asSrc: bool,
                        isLegal: bool): 
        '''
        legalDisconnection(self, plug: MPlug,
                        otherPlug: MPlug,
                        asSrc: bool,
                        isLegal: bool)

        Synopsis
        -----
        This method allows you to check for legal disconnections being
        made to attributes of this node. You should return
        kUnknownParameter to specify that maya should handle this
        disconnection if you are unable to determine if it is legal.

        Returns:
        -----
        None

        Parameters:
        -----
        plug: MPlug
        	[in] -> attribute on this node 

        otherPlug: MPlug
        	[in] -> attribute on other node 

        asSrc: bool
        	[in] -> is this plug a source of the connection 

        isLegal: bool
        	[out] -> set this to true if the disconnection is legal, false otherwise


        '''
        pass

    def setDependentsDirty(self, plugBeingDirtied: MPlug,
                        affectedPlugs: MPlugArray): 
        '''
        setDependentsDirty(self, plugBeingDirtied: MPlug,
                        affectedPlugs: MPlugArray)

        Synopsis
        -----
        This method can be overridden in user defined nodes to specify
        which plugs should be set dirty based upon an input plug
        {plugBeingDirtied} which Maya is marking dirty. The list of plugs
        for Maya to mark dirty is returned by the plug array
        {affectedPlugs}. This method handles both dynamic as well as non-
        dynamic plugs and is useful in the following ways:This method is
        designed to work harmoniously with MPxNode::attributeAffects on
        the same node. Alternately, you can do all affects relationships
        within a yourNode::setDependentsDirty() implementation.The body
        of a user-implemented setDependentsDirty() implementation might
        look like the following example, which causes the plug called "B"
        to be set dirty whenever plug "A" is changed, i.e. A affects B.In
        the above example, whenever plugBeingDirtied is A, we add B to
        affectedPlugs so that Maya will dirty B and also any plugs which
        depend upon B.For cases where multi compound attributes are
        dirtied, it is the programmer's responsibility to define ALL
        affects relationships. Dirtying the parent plug of a multi does
        not imply that all of its children will be marked dirty.
        Likewise, dirtying a child attribute does not imply the parent of
        the multi is dirty. This must be explicitly defined using the
        affected plug array. The following example demonstrates how one
        would dirty both the element affected and the parent
        plug.IMPORTANT NOTE: since the setDependentsDirty() method is
        called during dirty propagation, you must be careful not to
        perform any dependency graph computations from within the
        routine. Instead, if you want to know the value of a plug, use
        MDataBlock::outputValue() because it will not result in
        computation (and thus recursion). In general, the majority of
        {setDependentsDirty()} methods which users will implement should
        involve only fixed relationships. In the rare occurrence where
        you need to look at plug values, please heed the warning with
        {MDataBlock::outputValue()} and use plugs which contain values
        which you know to be up to date prior to the start of dirty
        propagation.

        Returns:
        -----
        None

        Parameters:
        -----
        plugBeingDirtied: MPlug
        	[in] -> plug which is being set dirty by Maya 

        affectedPlugs: MPlugArray
        	[in] -> the programmer should add any plugs which they want to set dirty to this list.


        '''
        pass

    def preEvaluation(self, context: MDGContext,
                        evaluationNode: MEvaluationNode): 
        '''
        preEvaluation(self, context: MDGContext,
                        evaluationNode: MEvaluationNode)

        Synopsis
        -----
        Prepare a node's internal state for threaded evaluation. During
        the evaluation graph execution each node gets a chance to reset
        its internal states just before being evaluated.This code has to
        be thread safe, non-blocking and work only on data owned by the
        node.The timing of this callback is at the discretion of
        evaluation graph dependencies and individual evaluators. This
        means, it should be used purely to prepare this node for
        evaluation and no particular order should be assumed.This call
        will most likely happen from a worker thread.When using
        Evaluation Caching or VP2 Custom Caching, preEvaluation() is
        called as part of the evaluation process. This function is not
        called as part of the cache restore process because no evaluation
        takes place in that case.

        Returns:
        -----
        None

        Parameters:
        -----
        context: MDGContext
        	[in] -> Context in which the evaluation is happening. This should be respected and only internal state information pertaining to it should be modified. 

        evaluationNode: MEvaluationNode
        	[in] -> Evaluation node which contains information about the dirty plugs that are about to be evaluated for the context. Should be only used to query information. 


        '''
        pass

    def postEvaluation(self, context: MDGContext,
                        evaluationNode: MEvaluationNode,
                        evalType: MPxNode.PostEvaluationType): 
        '''
        postEvaluation(self, context: MDGContext,
                        evaluationNode: MEvaluationNode,
                        evalType: MPxNode.PostEvaluationType)

        Synopsis
        -----
        Clean up node's internal state after threaded evaluation. After
        the evaluation graph execution, each node gets a chance to update
        its internal states. For example, resetting draw state.This code
        has to be thread safe, non-blocking and work only on data owned
        by the node.This call will most likely happen from a worker
        thread.When using Evaluation Caching or VP2 Custom Caching,
        postEvaluation() will be called as part of the evaluation
        process. In addition to its role in regular EM evaluation, it can
        also be used to notify VP2 to ensure correctness of VP2 cached
        buffers, and perform pull evaluation to ensure any internal
        secondary data is up to date after evaluation. Similar to
        preEvaluation() this function is not called as part of the cache
        restore process.

        Returns:
        -----
        None

        Parameters:
        -----
        context: MDGContext
        	[in] -> Context in which the evaluation happened. This should be respected and only internal state information pertaining to it should be modified.

        evaluationNode: MEvaluationNode
        	[in] -> Evaluation node which contains information about the dirty plugs that were evaluated for this context.

        evalType: MPxNode.PostEvaluationType
        	[out] -> kEvaluatedIndirectly: The node's compute function handled evaluation. kEvaluatedDirectly: Evaluation was performed externally and the results injected back into the node. This would happen in situations such as extracting values from an external cache. The node needs to update any additional internal state based on the new values. kLeaveDirty: Evaluation was performed without updating this node. Internal state should be updated to reflect that the node is dirty. 


        '''
        pass

    def schedulingType(self): 
        '''
        schedulingType(self) -> MPxNode.MPxNode

        Synopsis
        -----
        When overridden this method controls the degree of parallelism
        supported by the node during threaded evaluation.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getCacheSetup(self, evalNode: MEvaluationNode,
                        disablingInfo: MNodeCacheDisablingInfo,
                        cacheSetupInfo: MNodeCacheSetupInfo,
                        monitoredAttributes: MObjectArray): 
        '''
        getCacheSetup(self, evalNode: MEvaluationNode,
                        disablingInfo: MNodeCacheDisablingInfo,
                        cacheSetupInfo: MNodeCacheSetupInfo,
                        monitoredAttributes: MObjectArray)

        Synopsis
        -----
        Introduced in 2020.0 Provide node-specific setup info for the
        Cached Playback system.This method will be called at EM
        partitioning time. It works in one of two ways.In case the answer
        depends on the value of attributes (for example, a node can have
        multiple modes, some of them working with caching and some of
        them not), the node can add the attributes to the monitored
        attribute list so they can be monitored in case the value
        changes.By default, this method states that Cached Playback is
        supported, but does not request to be cached by default.Note that
        regardless of the preferences expressed by a node, Caching Rules
        can always override the preferences from this method. Caching
        Rules always have the last world. This method simply indicates
        the built-in Evaluation Cache rule used by Maya's default Caching
        Modes that this node is to be cached. Other rules can ignore or
        override this behavior.Reimplemented in MPxLocatorNode.

        Returns:
        -----
        None

        Parameters:
        -----
        evalNode: MEvaluationNode
        	[in] -> This node's evaluation node, contains animated plug information 

        disablingInfo: MNodeCacheDisablingInfo
        	[out] -> Information about why the node disables Cached Playback to be reported to the user 

        cacheSetupInfo: MNodeCacheSetupInfo
        	[out] -> Preferences and requirements this node has for Cached Playback 

        monitoredAttributes: MObjectArray
        	[out] -> Attributes impacting the behavior of this method that will be monitored for change 


        '''
        pass

    def configCache(self, evalNode: MEvaluationNode,
                        schema: MCacheSchema): 
        '''
        configCache(self, evalNode: MEvaluationNode,
                        schema: MCacheSchema)

        Synopsis
        -----
        Introduced in 2020.0 Defines the node's behavior when
        participating in Cached Playback.This method will be called at EM
        partitioning time, after rules evaluation.

        Returns:
        -----
        None

        Parameters:
        -----
        evalNode: MEvaluationNode
        	[in] -> 

        schema: MCacheSchema
        	[in] -> 


        '''
        pass

    def transformInvalidationRange(self, source: MPlug,
                        input: MTimeRange): 
        '''
        transformInvalidationRange(self, source: MPlug,
                        input: MTimeRange) -> MTimeRange

        Synopsis
        -----
        Introduced in 2020.0 Override this method to register this node
        as an Invalidation-Range-Transformation kernel (IRT kernel) An
        IRT kernel node will change the invalidation time range for its
        downstream nodes For example, Dynamics-solver will transform
        invalidation time range [a,b] to [a,+inf) And Clip-Time-Editor
        will send out the invalidation range for each of the clip [a,b]
        to ( [t0+a,t0+b] U [t1+a,t1+b] U [t2+a,t2+b] U ...)

        Returns: 
        ----- 
        The output invalidation range for all the dependents of plug
        'source'

        Parameters:
        -----
        source: MPlug
        	[in] -> The source plug in this node where the dirty propagation comes from 

        input: MTimeRange
        	[in] -> The incoming invalidation range 


        '''
        pass

    def hasInvalidationRangeTransformation(self): 
        '''
        hasInvalidationRangeTransformation(self) -> bool

        Synopsis
        -----
        Introduced in 2020.0 Checks if this MPxNode derived node
        overrides the MPxNode::transformInvalidationRange method.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def connectionMade(self, plug: MPlug,
                        otherPlug: MPlug,
                        asSrc: bool): 
        '''
        connectionMade(self, plug: MPlug,
                        otherPlug: MPlug,
                        asSrc: bool)

        Synopsis
        -----
        This method gets called when connections are made to attributes
        of this node. You should return kUnknownParameter to specify that
        maya should handle this connection or if you want maya to process
        the connection as well.Only in very exceptional circumstances
        would you want to bypass maya's internal processing so when
        overriding this method the safest thing to do is to return the
        result from the base class as shown below.

        Returns:
        -----
        None

        Parameters:
        -----
        plug: MPlug
        	[in] -> attribute on this node 

        otherPlug: MPlug
        	[in] -> attribute on other node 

        asSrc: bool
        	[in] -> is this plug a source of the connection


        '''
        pass

    def connectionBroken(self, plug: MPlug,
                        otherPlug: MPlug,
                        asSrc: bool): 
        '''
        connectionBroken(self, plug: MPlug,
                        otherPlug: MPlug,
                        asSrc: bool)

        Synopsis
        -----
        This method gets called when connections are broken with
        attributes of this node. You should return kUnknownParameter to
        specify that maya should handle this connection or if you want
        maya to process the connection as well.Only in very exceptional
        circumstances would you want to bypass maya's internal processing
        so when overriding this method the safest thing to do is to
        return the result from the base class as shown below.

        Returns:
        -----
        None

        Parameters:
        -----
        plug: MPlug
        	[in] -> attribute on this node 

        otherPlug: MPlug
        	[in] -> attribute on other node 

        asSrc: bool
        	[in] -> is this plug a source of the connection


        '''
        pass

    def dependsOn(self, plug: MPlug,
                        otherPlug: MPlug,
                        depends: bool): 
        '''
        dependsOn(self, plug: MPlug,
                        otherPlug: MPlug,
                        depends: bool)

        Synopsis
        -----
        This method may be overridden by the user defined node. It should
        only be required to override this on rare occasions.This method
        determines whether a specific attribute depends on another
        attribute.You should return kUnknownParameter to specify that
        Maya should determines the dependency (default).This is mainly to
        define dependency of dynamic attributes, since attributeAffects
        does not work with dynamic attributes.

        Returns:
        -----
        None

        Parameters:
        -----
        plug: MPlug
        	[in] -> plug representing the attribute 

        otherPlug: MPlug
        	[in] -> plug representing the attribute to check for dependency 

        depends: bool
        	[out] -> boolean telling whether there is a dependency between the two attributes


        '''
        pass

    def isPassiveOutput(self, plug: MPlug): 
        '''
        isPassiveOutput(self, plug: MPlug) -> bool

        Synopsis
        -----
        This method may be overridden by the user defined node if it
        wants to provide output attributes which do not prevent value
        modifications to the destination attribute. For example, output
        plugs on animation curve nodes are passive. This allows the
        attributes driven by the animation curves to be set to new values
        by the user.

        Returns: 
        ----- 
        true indicates passive

        Parameters:
        -----
        plug: MPlug
        	[in] -> plug representing output in question


        '''
        pass

    def shouldSave(self, plug: MPlug,
                        isSaving: bool): 
        '''
        shouldSave(self, plug: MPlug,
                        isSaving: bool)

        Synopsis
        -----
        This method may be overridden by the user defined node. It should
        only be required to override this on rare occasions.This method
        determines whether a specific attribute of this node should be
        written out during a file save. The default behavior is to only
        write the value if it differs from the default and is not being
        supplied by a connection. This behavior should be sufficient in
        most cases. This method is not called for ramp attributes since
        they should always be written.

        Returns:
        -----
        None

        Parameters:
        -----
        plug: MPlug
        	[in] -> plug representing the attribute to be saved 

        isSaving: bool
        	[in] -> boolean telling whether to save or not


        '''
        pass

    def passThroughToOne(self, plug: MPlug): 
        '''
        passThroughToOne(self, plug: MPlug) -> MPlug

        Synopsis
        -----
        This method may be overridden by nodes that have a one-to-one
        relationship between an input attribute and a corresponding
        output attribute. This method is used by Maya to perform the
        following capabilities:

        Returns: 
        ----- 
        The corresponding plug, or an empty plug if no corresponding plug
        exists

        Parameters:
        -----
        plug: MPlug
        	[in] -> the plug


        '''
        pass

    def passThroughToMany(self, plug: MPlug,
                        plugArray: MPlugArray): 
        '''
        passThroughToMany(self, plug: MPlug,
                        plugArray: MPlugArray) -> bool

        Synopsis
        -----
        This method is overridden by nodes that want to control the
        traversal behavior of some Maya search algorithms which traverse
        the history/future of shape nodes looking for directly related
        nodes. In particular, the Artisan paint code uses this method
        when searching for paintable nodes, and the disk cache code uses
        this method when searching for upstream cacheFile nodes.If this
        method is not implemented or returns false, the base class Maya
        implementation of this method calls passThroughToOne and returns
        the results of that call.

        Returns: 
        ----- 
        true if plug was handled, false to invoke base class
        implementation

        Parameters:
        -----
        plug: MPlug
        	[in] -> the plug 

        plugArray: MPlugArray
        	[in] -> the corresponding plugs


        '''
        pass

    def type(self): 
        '''
        type(self) -> MPxNode.MPxNode

        Synopsis
        -----
        Returns the type of node that this is. This is used to
        differentiate user defined nodes that are derived off different
        MPx base classes.It is not necessary to override this
        method.Reimplemented in MPxAssembly, MPxGeometryFilter,
        MPxManipContainer, MPxHwShaderNode, MPxTransform,
        MPxThreadedDeviceNode, MPxHardwareShader, MPxMotionPathNode,
        MPxIkSolverNode, MPxClientDeviceNode, MPxEmitterNode,
        MPxSpringNode, MPxSurfaceShape, MPxLocatorNode, MPxImagePlane,
        MPxObjectSet, MPxFieldNode, MPxBlendShape, MPxDeformerNode,
        MPxFluidEmitterNode, MPxSkinCluster, MPxCameraSet, and
        MPxParticleAttributeMapperNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def isAbstractClass(self): 
        '''
        isAbstractClass(self) -> bool

        Synopsis
        -----
        Override this class to return true if this node is an abstract
        node. An abstract node can only be used as a base class. It
        cannot be created using the 'createNode' command.It is not
        necessary to override this method.Reimplemented in MPxPolyTrg.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def isTrackingTopology(self): 
        '''
        isTrackingTopology(self) -> bool

        Synopsis
        -----
        Introduced in 2019.0 Override this class to return true if this
        node wants to track topology.This is necessary to enable certain
        optimizations done when geometry created by this node does not
        alter topology.It is not necessary to override this method.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def addAttribute(self, attr: MObject): 
        '''
        addAttribute(self, attr: MObject)

        Synopsis
        -----
        This method adds a new attribute to a user defined node type
        during the type's initialization. This method will only work
        during the static initialization method of the user defined node
        class. The initialization method is the one that is passed into
        MFnPlugin::registerNode. The attributes must first be created
        using one of the MFnAttribute classes, and can then be added
        using this method.For compound attributes, the proper way to use
        this method is by calling it with the parent attribute. If a
        compound attribute is passed, this method will add all of its
        children. NOTE: A failure will occur if you attempt to call
        addAttribute() on the children of a compound attribute.

        Returns:
        -----
        None

        Parameters:
        -----
        attr: MObject
        	[in] -> new attribute to add


        '''
        pass

    def inheritAttributesFrom(self, parentClassName: MString): 
        '''
        inheritAttributesFrom(self, parentClassName: MString)

        Synopsis
        -----
        This method allows a class of plugin node to inherit all of the
        attributes of a second class of plugin node. This method will
        only work during the static initialization method of the user
        defined node class and must be called before any other attributes
        have been added. The initialization method is the one that is
        passed into MFnPlugin::registerNode.A plugin node may only
        inherit attributes from one other class of plugin node.
        Attempting to call this method multiple times within a node's
        initialization method will result in an error.Both node classes
        must be registered using the same MPxNode::Type.

        Returns:
        -----
        None

        Parameters:
        -----
        parentClassName: MString
        	[in] -> class of node to inherit attributes from


        '''
        pass

    @overload
    def attributeAffects(self, whenChanges: MObject,
                        isAffected: MObject): 
        '''
        attributeAffects(self, whenChanges: MObject,
                        isAffected: MObject)

        Synopsis
        -----
        This method specifies that a particular input attribute affects a
        specific output attribute. This is required to make evaluation
        efficient. When an input changes, only the affected outputs will
        be computed. Output attributes cannot be keyable - if they are
        keyable, this method will fail.This method must be called for
        every attribute dependency when initializing the node's
        attributes. The attributes must first be added using the
        MPxNode::addAttribute method. Failing to call this method will
        cause the node not to update when its inputs change. If there are
        no calls to this method in a node's initialization, then the
        compute method will never be called.This method will only work
        during the static initialization method of the user defined node
        class. The initialization method is the one that is passed into
        MFnPlugin::registerNode. As a result, it does not work with
        dynamic attributes. For an alternate solution which handles
        dynamic as well as non-dynamic attributes refer to
        MPxNode::setDependentsDirty.

        Returns:
        -----
        None

        Parameters:
        -----
        whenChanges: MObject
        	[in] -> input attribute - 

        isAffected: MObject
        	[in] -> affected output attribute - 


        '''
        pass

    @overload
    def attributeAffects(self, whenChanges: MObject,
                        isAffected: MObject,
                        affectsTopology: bool): 
        '''
        attributeAffects(self, whenChanges: MObject,
                        isAffected: MObject,
                        affectsTopology: bool)

        Synopsis
        -----
        Introduced in 2019.0 This method is an extension to the other
        version of the attributeAffects method.It allows specifying where
        the input attribute can affect the topology of the output
        attribute through this relationship.Calling this method with the
        affectsTopology parameter set to true is the same as calling the
        2-parameter version of this method. Calling it with false can
        enable certain optimizations done when geometry created by this
        node does not alter topology.

        Returns:
        -----
        None

        Parameters:
        -----
        whenChanges: MObject
        	[in] -> input attribute - 

        isAffected: MObject
        	[in] -> affected output attribute - 

        affectsTopology: bool
        	[in] -> whether this relationship affects topology or not


        '''
        pass

    def getFilesToArchive(self, shortName: bool,
                        unresolvedName: bool,
                        markCouldBeImageSequence: bool): 
        '''
        getFilesToArchive(self, shortName: bool,
                        unresolvedName: bool,
                        markCouldBeImageSequence: bool) -> MStringArray

        Synopsis
        -----
        Use this method to return all external files used by this node.
        This file list will be used by the File > Archive zip feature,
        maya.exe -archive and the `file -q -list` mel command.Only
        include files that exist.If shortName is true, return just the
        filename portion of the path (can be obtained with
        MString::baseName()). Otherwise, return a full path.If
        unresolvedName is true, return the path before any resolution has
        been done (i.e leave it as a relative path, include unexpanded
        environment variables, tildes, ".."s etc). Otherwise, resolve the
        file path and return an absolute path (to resolve with standard
        Maya path resolution, use MFileObject::resolvedFullName()).

        Returns: 
        ----- 
        Array of file paths

        Parameters:
        -----
        shortName: bool
        	[in] -> If true, only add the filename of the path 

        unresolvedName: bool
        	[in] -> If true, add paths before any resolution, rather than absolute paths. 

        markCouldBeImageSequence: bool
        	[in] -> If true, append an asterisk after any file path that could be an image sequence (note: only used by maya.exe -archive)


        '''
        pass

    def getExternalContent(self, table: MExternalContentInfoTable): 
        '''
        getExternalContent(self, table: MExternalContentInfoTable)

        Synopsis
        -----
        Returns the external content (files) that this node depends on.
        The table populated by this method must include the location of
        all the content (files) used by this node, including those that
        do not exist. See MExternalContentInfoTable for details.Keys used
        to add items to this table will be the same that get passed to
        setExternalContent through its MExternalContentLocationTable
        parameter to perform a batched change of content location.When
        implementing getExternalContent, you are responsible for
        forwarding the call to the base class when it makes sense to do
        so, so that base classes can also add their external content to
        the table.The default implementation does nothing.

        Returns:
        -----
        None

        Parameters:
        -----
        table: MExternalContentInfoTable
        	[out] -> Content information table that this method must populate. 


        '''
        pass

    def addExternalContentForFileAttr(self, table: MExternalContentInfoTable,
                        attr: MObject): 
        '''
        addExternalContentForFileAttr(self, table: MExternalContentInfoTable,
                        attr: MObject) -> bool

        Synopsis
        -----
        Adds content info to the specified table from a file path
        attribute. This method is a helper for derived clases
        implementing getExternalContent(). It augments the external
        content info table passed in with an entry describing external
        content whose location is described by the specified
        attribute.The method will not overwrite existing items, i.e.
        items with the same key. (attribute name). In this context,
        overwriting an item means the caller has called this function
        twice with the same attribute, or that two separate but
        identically named attributes were used. If replacing an entry is
        the desired effect, it is the caller's responsibility to erase
        the previous item first.

        Returns: 
        ----- 
        true if an item was sucessfully added to the table. false if the
        attribute does not describe a non-empty location, or an item with
        the same key was already present in the table.

        Parameters:
        -----
        table: MExternalContentInfoTable
        	[out] -> The table in which the new entry will be added. 

        attr: MObject
        	[in] -> The attribute for which the plug value will be queried for a location.


        '''
        pass

    def setExternalContentForFileAttr(self, attr: MObject,
                        table: MExternalContentLocationTable): 
        '''
        setExternalContentForFileAttr(self, attr: MObject,
                        table: MExternalContentLocationTable) -> bool

        Synopsis
        -----
        Sets content info in the specified attribute from the table. This
        method is a helper for derived clases implementing
        setExternalContent(). It assigns a value to a plug with the one
        from the table whose key is the same as the passed in attribute
        name.The method will not write to the plug if the attribute is
        not found in the table.

        Returns: 
        ----- 
        true if the plug was successfully written to. false if no entry
        in the table was named after the attribute or if no plug was
        found.

        Parameters:
        -----
        attr: MObject
        	[in] -> The attribute of the plug we want to write to. 

        table: MExternalContentLocationTable
        	[in] -> A table which may hold or not the value for a given plug. 


        '''
        pass

    def setExternalContent(self, table: MExternalContentLocationTable): 
        '''
        setExternalContent(self, table: MExternalContentLocationTable)

        Synopsis
        -----
        Changes the location of external content in batch. This is useful
        in the context of content relocation. This will be called while
        the scene is being loaded to apply path changes performed
        externally. Consequently, interaction with the rest of the scene
        must be kept to a minimum. It is however valid to call this
        method outside of scene loading contexts.The keys in the map must
        be the same as the ones provided by the node in
        getExternalContent. The values are the new locations.When
        implementing setExternalContent, you are responsible for
        forwarding the call to the base class when it makes sense to do
        so, so that base classes can also set their external content.The
        default implementation does nothing.

        Returns:
        -----
        None

        Parameters:
        -----
        table: MExternalContentLocationTable
        	[in] -> Key->location table with new content locations. 


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

    def typeId(self): 
        '''
        typeId(self) -> MTypeId

        Synopsis
        -----
        Returns the TYPEID of this node. The TYPEID is a four byte
        identifier that uniquely identifies this type of node to the
        binary file format.It is not necessary to override this
        method.Reimplemented in MPxAssembly.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def typeName(self): 
        '''
        typeName(self) -> MString

        Synopsis
        -----
        Returns the type name of this node. The type name identifies the
        node type to the ASCII file format. It may also be used with the
        MEL command "createNode" to create a new node of this type.It is
        not necessary to override this method.Reimplemented in
        MPxAssembly.

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
        Returns the name of this particular instance of this class. Each
        object in the dependency graph has a name. This name will be used
        by the UI and by MEL.It is not necessary to override this
        method.Reimplemented in MPxAssembly.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def thisMObject(self): 
        '''
        thisMObject(self) -> MObject

        Synopsis
        -----
        Returns the MObject associated with this user defined node. This
        makes it possible to use MFnDependencyNode or to construct plugs
        to this node's attributes.It is not necessary to override this
        method.Reimplemented in MPxTransform, MPxAssembly,
        MPxSurfaceShape, MPxMotionPathNode, MPxImagePlane,
        MPxManipContainer, MPxGeometryFilter, MPxEmitterNode,
        MPxLocatorNode, MPxManipulatorNode, MPxThreadedDeviceNode,
        MPxIkSolverNode, MPxFieldNode, MPxObjectSet,
        MPxParticleAttributeMapperNode, MPxConstraint, MPxSpringNode, and
        MPxCameraSet.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setExistWithoutInConnections(self, flag: bool): 
        '''
        setExistWithoutInConnections(self, flag: bool)

        Synopsis
        -----
        This method specifies whether or not the node can exist without
        input connections. If a node connected to this node is deleted
        resulting in no more input connections and if this flag is false,
        then this node will be deleted.Reimplemented in MPxAssembly.

        Returns:
        -----
        None

        Parameters:
        -----
        flag: bool
        	[in] -> true if this node can exist without input connections, false otherwise


        '''
        pass

    def existWithoutInConnections(self, ReturnStatus: MPxNode.MStatus): 
        '''
        existWithoutInConnections(self, ReturnStatus: MPxNode.MStatus) -> bool

        Synopsis
        -----
        Determines whether or not this node can exist without input
        connections. If a node connected to this node is deleted
        resulting in no more input connections and if this flag is false,
        then this node will be deleted.Reimplemented in MPxAssembly.

        Returns: 
        ----- 
        true is this node can exist without input connections, false
        otherwise

        Parameters:
        -----
        ReturnStatus: MPxNode.MStatus
        	[out] -> Status code.


        '''
        pass

    def setExistWithoutOutConnections(self, flag: bool): 
        '''
        setExistWithoutOutConnections(self, flag: bool)

        Synopsis
        -----
        This method specifies whether or not the node can exist without
        output connections. If a node connected to this node is deleted
        resulting in no more output connections and if this flag is
        false, then this node will be deleted.Reimplemented in
        MPxAssembly.

        Returns:
        -----
        None

        Parameters:
        -----
        flag: bool
        	[in] -> true if this node can exist without output connections, false otherwise


        '''
        pass

    def existWithoutOutConnections(self, ReturnStatus: MPxNode.MStatus): 
        '''
        existWithoutOutConnections(self, ReturnStatus: MPxNode.MStatus) -> bool

        Synopsis
        -----
        Determines whether or not this node can exist without output
        connections. If a node connected to this node is deleted
        resulting in no more output connections and if this flag is
        false, then this node will be deleted.Reimplemented in
        MPxAssembly.

        Returns: 
        ----- 
        true is this node can exist without output connections, false
        otherwise

        Parameters:
        -----
        ReturnStatus: MPxNode.MStatus
        	[out] -> Status code.


        '''
        pass

    def forceCache(self): 
        '''
        forceCache(self) -> MDataBlock

        Synopsis
        -----
        USE _forceCache() IN SCRIPT. Get the datablock for this node at
        the current evaluation context.If there is no datablock then one
        will be created.Reimplemented in MPxAssembly.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setDoNotWrite(self, flag: bool): 
        '''
        setDoNotWrite(self, flag: bool)

        Synopsis
        -----
        USE _setDoNotWrite() IN SCRIPT. Use this method to mark the "do
        not write" state of this proxy node.If set, this node will not be
        saved when the Maya model is written out.NOTES: 1. Plug-in
        "requires" information will be written out with the model when
        saved. But a subsequent reload and resave of the file will cause
        these to go away. 2. If this node is a DAG and has a parent or
        children, the "do not write" flag of the parent or children will
        not be set. It is the developers responsibility to ensure that
        the resulting scene file is capable of being read in without
        errors due to unwritten nodes.Reimplemented in MPxAssembly.

        Returns:
        -----
        None

        Parameters:
        -----
        flag: bool
        	[in] -> True if the user node should not be saved. 


        '''
        pass

    def doNotWrite(self, ReturnStatus: MPxNode.MStatus): 
        '''
        doNotWrite(self, ReturnStatus: MPxNode.MStatus) -> bool

        Synopsis
        -----
        USE _doNotWrite() IN SCRIPT. Use this method to query the "do not
        write" state of this proxy node.True is returned if this node
        will not be saved when the Maya model is written
        out.Reimplemented in MPxAssembly.

        Returns:
        -----
        None

        Parameters:
        -----
        ReturnStatus: MPxNode.MStatus
        	[out] -> 


        '''
        pass

class Type:
    '''Defines the type of node. 
    Non-functional class.  Values for this enum:
    kDependNode
    kLocatorNode
    kDeformerNode
    kManipContainer
    kSurfaceShape
    kFieldNode
    kEmitterNode
    kSpringNode
    kIkSolverNode
    kHardwareShader
    kHwShaderNode
    kTransformNode
    kObjectSet
    kFluidEmitterNode
    kImagePlaneNode
    kParticleAttributeMapperNode
    kCameraSetNode
    kConstraintNode
    kManipulatorNode
    kMotionPathNode
    kClientDeviceNode
    kThreadedDeviceNode
    kAssembly
    kSkinCluster
    kGeometryFilter
    kBlendShape
    kLast
    '''

    def __init__(self):
        pass

    def kDependNode(self):
        '''This is an enum of Type.
        - Description: Custom node derived from MPxNode. 
        - Value: 0
        '''
        pass

    def kLocatorNode(self):
        '''This is an enum of Type.
        - Description: Custom locator derived from MPxLocatorNode. 
        - Value: 1
        '''
        pass

    def kDeformerNode(self):
        '''This is an enum of Type.
        - Description: Custom deformer derived from MPxDeformerNode. 
        - Value: 2
        '''
        pass

    def kManipContainer(self):
        '''This is an enum of Type.
        - Description: Custom container derived from MPxManipContainer. 
        - Value: 3
        '''
        pass

    def kSurfaceShape(self):
        '''This is an enum of Type.
        - Description: Custom shape derived from MPxSurfaceShape. 
        - Value: 4
        '''
        pass

    def kFieldNode(self):
        '''This is an enum of Type.
        - Description: Custom field derived from MPxFieldNode. 
        - Value: 5
        '''
        pass

    def kEmitterNode(self):
        '''This is an enum of Type.
        - Description: Custom emitter derived from MPxEmitterNode. 
        - Value: 6
        '''
        pass

    def kSpringNode(self):
        '''This is an enum of Type.
        - Description: Custom spring derived from MPxSpringNode. 
        - Value: 7
        '''
        pass

    def kIkSolverNode(self):
        '''This is an enum of Type.
        - Description: Custom IK solver derived from MPxIkSolverNode. 
        - Value: 8
        '''
        pass

    def kHardwareShader(self):
        '''This is an enum of Type.
        - Description: Custom shader derived from MPxHardwareShader. 
        - Value: 9
        '''
        pass

    def kHwShaderNode(self):
        '''This is an enum of Type.
        - Description: Custom shader derived from MPxHwShaderNode. 
        - Value: 10
        '''
        pass

    def kTransformNode(self):
        '''This is an enum of Type.
        - Description: Custom transform derived from MPxTransform. 
        - Value: 11
        '''
        pass

    def kObjectSet(self):
        '''This is an enum of Type.
        - Description: Custom set derived from MPxObjectSet. 
        - Value: 12
        '''
        pass

    def kFluidEmitterNode(self):
        '''This is an enum of Type.
        - Description: Custom fluid emitter derived from MpxFluidEmitterNode. 
        - Value: 13
        '''
        pass

    def kImagePlaneNode(self):
        '''This is an enum of Type.
        - Description: Custom image plane derived from MPxImagePlane. 
        - Value: 14
        '''
        pass

    def kParticleAttributeMapperNode(self):
        '''This is an enum of Type.
        - Description: Custom particle attribute mapper derived from MPxParticleAttributeMapperNode. 
        - Value: 15
        '''
        pass

    def kCameraSetNode(self):
        '''This is an enum of Type.
        - Description: Custom director derived from MPxCameraSet. 
        - Value: 16
        '''
        pass

    def kConstraintNode(self):
        '''This is an enum of Type.
        - Description: Custom constraint derived from MPxConstraint. 
        - Value: 17
        '''
        pass

    def kManipulatorNode(self):
        '''This is an enum of Type.
        - Description: Custom manipulator derived from MPxManipulatorNode. 
        - Value: 18
        '''
        pass

    def kMotionPathNode(self):
        '''This is an enum of Type.
        - Description: Custom motionPath derived from MPxMotionPathNode. 
        - Value: 19
        '''
        pass

    def kClientDeviceNode(self):
        '''This is an enum of Type.
        - Description: Custom threaded device derived from MPxThreadedDeviceNode. 
        - Value: 20
        '''
        pass

    def kThreadedDeviceNode(self):
        '''This is an enum of Type.
        - Description: Custom threaded device node. 
        - Value: 21
        '''
        pass

    def kAssembly(self):
        '''This is an enum of Type.
        - Description: Custom assembly derived from MPxAssembly. 
        - Value: 22
        '''
        pass

    def kSkinCluster(self):
        '''This is an enum of Type.
        - Description: Custom deformer derived from MPxSkinCluster. 
        - Value: 23
        '''
        pass

    def kGeometryFilter(self):
        '''This is an enum of Type.
        - Description: Custom deformer derived from MPxGeometryFilter. 
        - Value: 24
        '''
        pass

    def kBlendShape(self):
        '''This is an enum of Type.
        - Description: Custom deformer derived from MPxBlendShape. 
        - Value: 25
        '''
        pass

    def kLast(self):
        '''This is an enum of Type.
        - Description: Last value, used for counting. 
        - Value: 26
        '''
        pass

class SchedulingType:
    '''Defines the degree of parallelism of a node. 
    Non-functional class.  Values for this enum:
    kParallel
    kSerial
    kGloballySerial
    kUntrusted
    kDefaultScheduling
    kSerialize
    kGloballySerialize
    '''

    def __init__(self):
        pass

    def kParallel(self):
        '''This is an enum of SchedulingType.
        - Description: This schedulingType indicates that the node can be evaluated concurrently to any other nodes without restrictions. 
        - Value: 1
        '''
        pass

    def kSerial(self):
        '''This is an enum of SchedulingType.
        - Description: Groups are formed for nodes having this ShedulingType when they are directly connected to each other. Within a same group nodes are guaranteed to not to be concurrently evaluated. However nodes in distinct groups can still be concurently be evaluated. 
        - Value: 2
        '''
        pass

    def kGloballySerial(self):
        '''This is an enum of SchedulingType.
        - Description: Nodes having the kGloballySerial SchedulingType are guaranteed not to be evaluated concurrently to any other node having the same schedulingType. 
        - Value: 3
        '''
        pass

    def kUntrusted(self):
        '''This is an enum of SchedulingType.
        - Description: Untrusted nodes are guaranteed not to be evaluately concurrently to any other node. Last value, used for counting 
        - Value: 4
        '''
        pass

    def kDefaultScheduling(self):
        '''This is an enum of SchedulingType.
        - Description: This is obsolete. as of Maya2017, use kSerial 
        - Value: 2
        '''
        pass

    def kSerialize(self):
        '''This is an enum of SchedulingType.
        - Description: This is obsolete. as of Maya2017, use kSerial 
        - Value: 2
        '''
        pass

    def kGloballySerialize(self):
        '''This is an enum of SchedulingType.
        - Description: This is obsolete. as of Maya2017, use kGloballySerial 
        - Value: 3
        '''
        pass

class MPxObjectSet:
    '''Parent class of all user defined object sets.
MPxObjectSet is the parent class of all user defined sets.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MPxNode.MPxNode

        Synopsis
        -----
        Returns the type of node that this is. This is used to
        differentiate user defined nodes that are derived off different
        MPx base classes.It is not necessary to override this
        method.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def canBeDeleted(self, isSrcNode: bool): 
        '''
        canBeDeleted(self, isSrcNode: bool) -> bool

        Synopsis
        -----
        A method that is called whenever a neighboring node is deleted,
        to check if this node should be deleted alongside or as a result
        of the neighboring node. This method will not be called in the
        case where construction history is being deleted.By default, the
        object set will be deleted when all of the following criteria are
        met:It is not necessary to override this method.

        Returns: 
        ----- 
        true Delete this node  false Do not delete this node

        Parameters:
        -----
        isSrcNode: bool
        	[in] -> True if this node is the source node of the connection to the neighboring node.


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

    def thisMObject(self): 
        '''
        thisMObject(self) -> MObject

        Synopsis
        -----
        Returns the MObject associated with this user defined node. This
        makes it possible to use MFnDependencyNode or to construct plugs
        to this node's attributes.It is not necessary to override this
        method.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def dagSetMembers(self): 
        '''
        dagSetMembers(self) -> MObject

        Synopsis
        -----
        Connections to this attribute specify the dagNodes or parts
        (components) of the same that are members of this set.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def memberWireframeColor(self): 
        '''
        memberWireframeColor(self) -> MObject

        Synopsis
        -----
        The index of a user defined color in which the dag object
        component members should appear. A value of -1 disables use of
        the color. Values outside the range [-1,7] may give unpredictable
        results.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def verticesOnlySet(self): 
        '''
        verticesOnlySet(self) -> MObject

        Synopsis
        -----
        Is set membership restricted to objects with vertices? This
        attribute should not be explicitly changed by the user.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def edgesOnlySet(self): 
        '''
        edgesOnlySet(self) -> MObject

        Synopsis
        -----
        Is set membership restricted to objects with edges? This
        attribute should not be explicitly changed by the user.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def facetsOnlySet(self): 
        '''
        facetsOnlySet(self) -> MObject

        Synopsis
        -----
        Is set membership restricted to objects with facets? This
        attribute should not be explicitly changed by the user.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def editPointsOnlySet(self): 
        '''
        editPointsOnlySet(self) -> MObject

        Synopsis
        -----
        Is set membership restricted to objects with edit points? This
        attribute should not be explicitly changed by the user.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def renderableOnlySet(self): 
        '''
        renderableOnlySet(self) -> MObject

        Synopsis
        -----
        Is set membership restricted to renderable objects only? This
        attribute should not be explicitly changed by the user.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def groupNodes(self): 
        '''
        groupNodes(self) -> MObject

        Synopsis
        -----
        When parts (components) of dagNodes are in the set, connections
        are made to this attribute to hold references to groupId nodes,
        with the id uniquely identifying the group in the dagNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MPxParticleAttributeMapperNode:
    '''User defined per particle attribute mapping nodes.
MPxParticleAttributeMapperNode is the parent class of all user defined per particle attribute
mapping nodes. This class extends Maya's internal 'arrayMapper'
node, inheriting its attributes and default behaviour.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MPxNode.MPxNode

        Synopsis
        -----
        Returns the type of node that this is. This is used to
        differentiate user defined nodes that are derived off different
        MPx base classes.It is not necessary to override this
        method.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def compute(self, plug: MPlug,
                        dataBlock: MDataBlock): 
        '''
        compute(self, plug: MPlug,
                        dataBlock: MDataBlock)

        Synopsis
        -----
        This method should be overridden in user defined nodes. Recompute
        the given output based on the nodes inputs. The plug represents
        the data value that needs to be recomputed, and the data block
        holds the storage for all of the node's attributes.The MDataBlock
        will provide smart handles for reading and writing this node's
        attribute values. Only these values should be used when
        performing computations.When evaluating the dependency graph,
        Maya will first call the compute method for this node. If the
        plug that is provided to the compute indicates that that the
        attribute was defined by the Maya parent node, the compute method
        should return MS::kUnknownParameter. When this occurs, Maya will
        call the internal Maya node from which the user-defined node is
        derived to compute the plug's value.This means that a user
        defined node does not need to be concerned with computing
        inherited output attributes. However, if desired, these can be
        safely recomputed by this method to change the behaviour of the
        node.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
        plug: MPlug
        	[in] -> plug representing the attribute that needs to be recomputed 

        dataBlock: MDataBlock
        	[out] -> data block containing storage for the node's attributes


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

    def thisMObject(self): 
        '''
        thisMObject(self) -> MObject

        Synopsis
        -----
        Returns the MObject associated with this user defined node. This
        makes it possible to use MFnDependencyNode or to construct plugs
        to this node's attributes.It is not necessary to override this
        method.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MPxPolyTrg:
    '''User defined poly triangulation support.
 is the the parent class for nodes which define a custom face
triangulation for meshes. In order to override default maya
triangulation, the user has to do the following things:
Derive a new node from
 class.
Define a static function on the new node to triangulate a single
face in the mesh. The signature of this function is given by
 type.
The input to the triangulation function is:
Note: The number of vertices can be calculated by adding all the
loop sizes.
 The output of this function is an array of triangle description:
Register that function when the node is created for the first
time (in the
postConstructor() method) by calling the
.
Once the node is defined, the user has to inform the mesh about
it. For each mesh the user wants to override the default
triangulation, he has to set the
 attribute on the mesh to the name under which the function has
been registered.
Example:
Once that attribute is set, the default maya triangulation is
turned off and the one provided by the user is used to draw the
mesh.
'''
    def __init__(self):
        pass


    def postConstructor(self): 
        '''
        postConstructor(self)

        Synopsis
        -----
        Post constructor. Internally maya creates two objects when a user
        defined node is created, the internal MObject and the user
        derived object. The association between the these two objects is
        not made until after the MPxPolyTrg constructor is called. This
        implies that no MPxPolyTrg member function can be called from the
        MPxPolyTrg constructor. The postConstructor will get called
        immediately after the constructor when it is safe to call any
        MPxPolyTrg member function. Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def compute(self, plug: MPlug,
                        block: MDataBlock): 
        '''
        compute(self, plug: MPlug,
                        block: MDataBlock)

        Synopsis
        -----
        This method should be overridden in user defined nodes. However,
        fror this particaular node we don't need to to do anything in the
        compute functione. Therefore, all we do is return MS:kSuccess in
        the derive class.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
        plug: MPlug
        	[in] -> plug representing the attribute that needs to be recomputed 

        block: MDataBlock
        	[out] -> data block containing storage for the node's attributes


        '''
        pass

    def isAbstractClass(self): 
        '''
        isAbstractClass(self) -> bool

        Synopsis
        -----
        Each new node has to implement that fuction. It returns false
        since this is not an abstract class.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def registerTrgFunction(self, functName: char,
                        funct: polyTrgFnct): 
        '''
        registerTrgFunction(self, functName: char,
                        funct: polyTrgFnct)

        Synopsis
        -----
        Register a triangulation function with maya. The name provided as
        a first argument is the name under which the function is
        registered. This name has to be used when setting 'userTrg'
        attribute on a mesh.

        Returns:
        -----
        None

        Parameters:
        -----
        functName: char
        	[in] -> Function name under which the function is register with maya. 

        funct: polyTrgFnct
        	[in] -> Pointer to the static function which implement a face triangulation.


        '''
        pass

    def unregisterTrgFunction(self, functName: char): 
        '''
        unregisterTrgFunction(self, functName: char)

        Synopsis
        -----

        Returns:
        -----
        None

        Parameters:
        -----
        functName: char
        	[in] -> Function name under which the function is register with maya.


        '''
        pass

class MPxPolyTweakUVCommand:
    '''Base class used for moving polygon UV's.
This is the base class for UV editing commands on polygonal
objects.
The purpose of this command class is to simplify the process of
moving UVs on a polygonal object. The use is only required to
provide the new positions of the UVs that have been modified.
'''
    def __init__(self):
        pass


    def parseSyntax(self, argData: MArgDatabase): 
        '''
        parseSyntax(self, argData: MArgDatabase)

        Synopsis
        -----
        This method parses the additional flags before the command is
        executed.

        Returns:
        -----
        None

        Parameters:
        -----
        argData: MArgDatabase
        	[in] -> Arguments passed to command.


        '''
        pass

    def getTweakedUVs(self, mesh: MObject,
                        uvList: MIntArray,
                        uPos: MFloatArray,
                        vPos: MFloatArray): 
        '''
        getTweakedUVs(self, mesh: MObject,
                        uvList: MIntArray,
                        uPos: MFloatArray,
                        vPos: MFloatArray)

        Synopsis
        -----
        This computes and returns modified UVs.

        Returns:
        -----
        None

        Parameters:
        -----
        mesh: MObject
        	[in] -> The mesh object to be modified 

        uvList: MIntArray
        	[in] -> The list of UV Ids selected by the user. The method is allowed to change uvList on output. 

        uPos: MFloatArray
        	[out] -> The new u values corresponding to the indices listed in 

        vPos: MFloatArray
        	[out] -> The new v values corresponding to the indices listed in 


        '''
        pass

class MPxPolyTweakUVInteractiveCommand:
    '''Base class used for moving polygon UV's.
This is the base class for UV editing interactive commands on
polygonal objects.
The purpose of this tool command class is to simplify the process
of moving UVs on a polygonal object. The use is only required to
provide the new positions of the UVs that being modified, and
finalize at the end of editing.
'''
    def __init__(self):
        pass


    def setUVs(self, mesh: MObject,
                        uvList: MIntArray,
                        uPos: MFloatArray,
                        vPos: MFloatArray,
                        uvSet: MString): 
        '''
        setUVs(self, mesh: MObject,
                        uvList: MIntArray,
                        uPos: MFloatArray,
                        vPos: MFloatArray,
                        uvSet: MString)

        Synopsis
        -----
        This method sets the uv to new values. Call this method during
        the editting, for example mouse drag.

        Returns:
        -----
        None

        Parameters:
        -----
        mesh: MObject
        	[in] -> The mesh object to be modified 

        uvList: MIntArray
        	[in] -> The list of UV Ids selected by the user. 

        uPos: MFloatArray
        	[in] -> The new u values corresponding to the indices listed in 

        vPos: MFloatArray
        	[in] -> The new v values corresponding to the indices listed in 

        uvSet: MString
        	[in] -> UV set to work with 


        '''
        pass

    def isUndoable(self): 
        '''
        isUndoable(self) -> bool

        Synopsis
        -----
        This method is used to specify whether or not the command is
        undoable. In the base class, it always returns false. If you are
        writing a command that might be eligible for undo, you should
        override this method.After Maya executes the command's doIt
        method, it will call isUndoable. If isUndoable returns true, Maya
        will retain the instance of the class and pass it to Maya's undo
        manager so that the undoIt and redoIt methods can be called when
        appropriate. If isUndoable returns false, the command instance
        will be immediately destroyed.So, for example, if a command
        supports both query and edit modes, in query mode the command
        should set a flag so that the isUndoable method returns false to
        prevent that command instance from being retained by the undo
        manager. In edit mode, where the state of Maya is changed,
        isUndoable should return true to enable undo and
        redo.Reimplemented from MPxCommand.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def doIt(self, args: MArgList): 
        '''
        doIt(self, args: MArgList)

        Synopsis
        -----
        This method should perform a command by setting up internal class
        data and then calling the redoIt method. The actual action
        performed by the command should be done in the redoIt method.
        This is a pure virtual method, and must be overridden in derived
        classes.Implements MPxToolCommand.

        Returns:
        -----
        None

        Parameters:
        -----
        args: MArgList
        	[in] -> List of arguments passed to the command.


        '''
        pass

    def cancel(self): 
        '''
        cancel(self)

        Synopsis
        -----
        This method cancels the command. Reimplemented from
        MPxToolCommand.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def finalize(self): 
        '''
        finalize(self)

        Synopsis
        -----
        This method finishs the editing of uv. It will register the
        command with the undo manager for journalling. Call this method
        at the end of editing, for example mouse release.Reimplemented
        from MPxToolCommand.

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

class MPxRenderPassImpl:
    '''Render pass implementation.
The
MPxRenderPassImpl class is an abstract base class which provides a common
interface for pass implementations. Extend this class to create
custom pass implementations.
'''
    def __init__(self):
        pass


    def isCompatible(self, renderer: MString): 
        '''
        isCompatible(self, renderer: MString) -> bool

        Synopsis
        -----
        Called by Maya check whether this pass implementation is
        compatible with the given renderer.

        Returns: 
        ----- 
        true if the implementation is compatible

        Parameters:
        -----
        renderer: MString
        	[in] -> The renderer to test compatibility against


        '''
        pass

    def typesSupported(self): 
        '''
        typesSupported(self) -> MPxRenderPassImpl.PassTypeMask

        Synopsis
        -----
        Called by Maya to determine which types are supported by this
        pass.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getDefaultType(self): 
        '''
        getDefaultType(self) -> MPxRenderPassImpl.PassTypeBit

        Synopsis
        -----
        Called by Maya to determine the default type for this pass.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getNumChannels(self): 
        '''
        getNumChannels(self) -> int

        Synopsis
        -----
        Called by Maya to get the number of channels supported by this
        pass.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def frameBufferSemantic(self): 
        '''
        frameBufferSemantic(self) -> MPxRenderPassImpl.PassSemantic

        Synopsis
        -----
        Called by Maya to get the frame buffer semantic. The semantic is
        an enum that provides a hint on the nature of the data stored in
        the frame buffer. This hint may affect how the renderer
        interpolates and filters sample values.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def perLightPassContributionSupported(self): 
        '''
        perLightPassContributionSupported(self) -> bool

        Synopsis
        -----
        Called by Maya to determine if this pass implementation supports
        per-light contributions defined by pass contribution maps.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class PassTypeBit:
    '''Data types that implementation may support. 
    Non-functional class.  Values for this enum:
    kUInt8
    kUInt16
    kUInt32
    kUInt64
    kInt8
    kInt16
    kInt32
    kInt64
    kFloat16
    kFloat32
    kFloat64
    kBit
    kOther
    '''

    def __init__(self):
        pass

    def kUInt8(self):
        '''This is an enum of PassTypeBit.
        - Description: Unsigned 8-bit integer. 
        - Value: 1
        '''
        pass

    def kUInt16(self):
        '''This is an enum of PassTypeBit.
        - Description: Unsigned 16-bit integer. 
        - Value: 2
        '''
        pass

    def kUInt32(self):
        '''This is an enum of PassTypeBit.
        - Description: Unsigned 32-bit integer. 
        - Value: 4
        '''
        pass

    def kUInt64(self):
        '''This is an enum of PassTypeBit.
        - Description: Unsigned 64-bit integer. 
        - Value: 8
        '''
        pass

    def kInt8(self):
        '''This is an enum of PassTypeBit.
        - Description: Signed 8-bit integer. 
        - Value: 16
        '''
        pass

    def kInt16(self):
        '''This is an enum of PassTypeBit.
        - Description: Signed 16-bit integer. 
        - Value: 32
        '''
        pass

    def kInt32(self):
        '''This is an enum of PassTypeBit.
        - Description: Signed 32-bit integer. 
        - Value: 64
        '''
        pass

    def kInt64(self):
        '''This is an enum of PassTypeBit.
        - Description: Signed 64-bit integer. 
        - Value: 128
        '''
        pass

    def kFloat16(self):
        '''This is an enum of PassTypeBit.
        - Description: half precision floating point 
        - Value: 256
        '''
        pass

    def kFloat32(self):
        '''This is an enum of PassTypeBit.
        - Description: single precision floating point 
        - Value: 512
        '''
        pass

    def kFloat64(self):
        '''This is an enum of PassTypeBit.
        - Description: double precision floating point 
        - Value: 1024
        '''
        pass

    def kBit(self):
        '''This is an enum of PassTypeBit.
        - Description: single bit 
        - Value: 2048
        '''
        pass

    def kOther(self):
        '''This is an enum of PassTypeBit.
        - Description: undefined type 
        - Value: 4096
        '''
        pass

class PassSemantic:
    '''Description of the nature of the data stored in the frame buffer. 
    Non-functional class.  Values for this enum:
    kInvalidSemantic
    kColorSemantic
    kVectorSemantic
    kDirectionVectorSemantic
    kDepthSemantic
    kLabelSemantic
    kMaskSemantic
    kOtherSemantic
    '''

    def __init__(self):
        pass

    def kInvalidSemantic(self):
        '''This is an enum of PassSemantic.
        - Description: Invalid. 
        - Value: 0
        '''
        pass

    def kColorSemantic(self):
        '''This is an enum of PassSemantic.
        - Description: RGB, RGBA, alpha, luminance, etc. 
        - Value: 1
        '''
        pass

    def kVectorSemantic(self):
        '''This is an enum of PassSemantic.
        - Description: General vector data (e.g. motion vectors, surface displacements) 
        - Value: 2
        '''
        pass

    def kDirectionVectorSemantic(self):
        '''This is an enum of PassSemantic.
        - Description: Vectors that represent a direction (e.g. surface normals, light directions) 
        - Value: 3
        '''
        pass

    def kDepthSemantic(self):
        '''This is an enum of PassSemantic.
        - Description: Depth or range data. 
        - Value: 4
        '''
        pass

    def kLabelSemantic(self):
        '''This is an enum of PassSemantic.
        - Description: Labels, such as material tags or object tags. 
        - Value: 5
        '''
        pass

    def kMaskSemantic(self):
        '''This is an enum of PassSemantic.
        - Description: Pixel mask (e.g. a stencil buffer) 
        - Value: 6
        '''
        pass

    def kOtherSemantic(self):
        '''This is an enum of PassSemantic.
        - Description: Undefined, unknown or custom semantic. 
        - Value: 7
        '''
        pass

class MPxRepresentation:
    '''Abstract base class for user defined representations.
MPxRepresentation is an abstract base class that can be used to provide an
interface and services for user defined representations.
Representations are owned by a scene assembly node (see
MPxAssembly). A scene assembly node will activate one of its
representations; representations must therefore support activate
and inactivate operations.
This class can be used to implement new kinds of representations
within Maya that behave in a similar manner to the
representations included in the scene assembly reference Maya
plugin, which uses
MPxRepresentation as a base class for its representations.
Note that use of this class to implement representations is not
mandatory: it provides an interface that is convenient for
dealing consistently with representations, as well as an
inactivate() implementation that is widely useful (clear out the assembly).
Also note that
MPxRepresentation is not associated with a corresponding Maya DAG or DG node.
For use of scene assembly nodes, see function set
MFnAssembly.
'''
    def __init__(self):
        pass


    def activate(self): 
        '''
        activate(self) -> bool

        Synopsis
        -----
        Activate this representation.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def inactivate(self): 
        '''
        inactivate(self) -> bool

        Synopsis
        -----
        Inactivate this representation. Implementation in this class is
        to clear out the assembly. Inactivation will fail and return
        false if the name of the currently-active representation doesn't
        match the name of this representation.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getType(self): 
        '''
        getType(self) -> MString

        Synopsis
        -----
        Return the representation type string.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getName(self): 
        '''
        getName(self) -> MString

        Synopsis
        -----
        Returns the name of the representation.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def canApplyEdits(self): 
        '''
        canApplyEdits(self) -> bool

        Synopsis
        -----
        Determines whether this representation can apply tracked edits to
        its data. Implementation in this class returns false.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getExternalContent(self, table: MExternalContentInfoTable): 
        '''
        getExternalContent(self, table: MExternalContentInfoTable)

        Synopsis
        -----
        Get external content for this representation. This is a
        propagation of the method of the same name on MPxNode.
        Representation owners (most likely derived from MPxAssembly) are
        expected to call this method from their own implementation of
        this method. In the context of representations, external content
        is any file or other piece of information that is stored
        externally to the representation.For example, a representation
        that would load a cache file will insert this cache file's path
        into the table passed in.The default implementation does nothing.

        Returns:
        -----
        None

        Parameters:
        -----
        table: MExternalContentInfoTable
        	[out] -> The table into which the representation must add its external content item(s). 


        '''
        pass

    def setExternalContent(self, table: MExternalContentLocationTable): 
        '''
        setExternalContent(self, table: MExternalContentLocationTable)

        Synopsis
        -----
        Set external content for this representation. This is a
        propagation of the method of the same name on MPxNode.
        Representation owners (most likely derived from MPxAssembly) are
        expected to call this method from their own implementation of
        this method. In the context of representations, external content
        is any file or other piece of information that is stored
        externally to the representation.For example, a representation
        that would load a cache file will read the cache's path from the
        table passed in and change its internal representation to this
        path. The path will be at the same key that was used when it was
        inserted in the corresponding table by getExternalContent.The
        default implementation does nothing.

        Returns:
        -----
        None

        Parameters:
        -----
        table: MExternalContentLocationTable
        	[in] -> The table into which the representation must add its external content item(s). 


        '''
        pass

class MPxSelectionContext:
    '''Base class for interative selection tools.
This class is used in creating user defined tools that use the
internal selection mechanism in maya.
'''
    def __init__(self):
        pass


    def doPress(self, event: MEvent): 
        '''
        doPress(self, event: MEvent)

        Synopsis
        -----
        This method is called when any mouse button is pressed. The base
        method does nothing and should be overridden if the user needs to
        do anything on a button press.The event can be used to get more
        explicit information about the press such as the button number.
        See MEvent for more information.Reimplemented from MPxContext.

        Returns:
        -----
        None

        Parameters:
        -----
        event: MEvent
        	[in] -> The button press event information.


        '''
        pass

    def doRelease(self, event: MEvent): 
        '''
        doRelease(self, event: MEvent)

        Synopsis
        -----
        This method is called when any mouse button is released. The base
        method does nothing except marquee selection and should be
        overriden if the user needs to do anything on a button
        release.The event can be used to get more explicit information
        about the release such as the button number. See MEvent for more
        information.Reimplemented from MPxContext.

        Returns:
        -----
        None

        Parameters:
        -----
        event: MEvent
        	[in] -> The mouse button release information.


        '''
        pass

    def doDrag(self, event: MEvent): 
        '''
        doDrag(self, event: MEvent)

        Synopsis
        -----
        This method is called when a mouse drag event occurs. The base
        method does nothing except marquee selection and should be
        overriden if the user needs to do anything during a mouse
        drag.The event can be used to get more explicit information about
        the drag such as the cursor location. See MEvent for more
        information.Reimplemented from MPxContext.

        Returns:
        -----
        None

        Parameters:
        -----
        event: MEvent
        	[in] -> The mouse drag event information.


        '''
        pass

    def doHold(self, event: MEvent): 
        '''
        doHold(self, event: MEvent)

        Synopsis
        -----
        This method is called when after a mouse button is pressed but
        before the mouse is dragged. The base method does nothing except
        marquee selection and should be overriden if the user needs to do
        anything on a button hold.The event can be used to get more
        explicit information about the hold such as the button number.
        See MEvent for more information.Reimplemented from MPxContext.

        Returns:
        -----
        None

        Parameters:
        -----
        event: MEvent
        	[in] -> The mouse button hold event information.


        '''
        pass

    def helpStateHasChanged(self, event: MEvent): 
        '''
        helpStateHasChanged(self, event: MEvent)

        Synopsis
        -----
        This method is called whenever the help state may need to be
        updated. The base method does nothing and should be overriden if
        the user needs to change the help information based on events.The
        event can be used to get more explicit information about the
        event. See MEvent for more information.Reimplemented from
        MPxContext.

        Returns:
        -----
        None

        Parameters:
        -----
        event: MEvent
        	[in] -> The event information. Unused in the base class.


        '''
        pass

    def addManipulator(self, manipulator: MObject): 
        '''
        addManipulator(self, manipulator: MObject)

        Synopsis
        -----
        This method adds a manipulator to the context, and also adds the
        manipulator to the DAG. Note that the manipulator should not yet
        be added to the DAG when this method is called.Reimplemented from
        MPxContext.

        Returns:
        -----
        None

        Parameters:
        -----
        manipulator: MObject
        	[in] -> the manipulator to be added to the context


        '''
        pass

    def deleteManipulators(self): 
        '''
        deleteManipulators(self)

        Synopsis
        -----
        This method deletes all the manipulators that belong to the
        context. Reimplemented from MPxContext.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setAllowPreSelectHilight(self): 
        '''
        setAllowPreSelectHilight(self)

        Synopsis
        -----
        This method enables the support of pre-selection highlight for
        this context. It needs to be called by the user-overriden
        MPxContext::toolOnSetup method.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setAllowSoftSelect(self): 
        '''
        setAllowSoftSelect(self)

        Synopsis
        -----
        This method enables the support of soft selection for this
        context.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setAllowSymmetry(self): 
        '''
        setAllowSymmetry(self)

        Synopsis
        -----
        This method enables the support of symmetrical selection for this
        context.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setAllowDoubleClickAction(self): 
        '''
        setAllowDoubleClickAction(self)

        Synopsis
        -----
        This method enables the support of double click smart selection
        for this context.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setAllowPaintSelect(self): 
        '''
        setAllowPaintSelect(self)

        Synopsis
        -----
        Introduced in 2023.0 This method enables drag selection mode for
        this context.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setImage(self, image: MString,
                        index: MPxSelectionContext.ImageIndex): 
        '''
        setImage(self, image: MString,
                        index: MPxSelectionContext.ImageIndex)

        Synopsis
        -----
        This method is used to set an XPM icon image that is to be used
        to represent this tool context in various places including the
        tool bar and can be queried from mel using the contextInfo
        command.

        Returns:
        -----
        None

        Parameters:
        -----
        image: MString
        	[in] -> the name of an XPM file to be used as the icon 

        index: MPxSelectionContext.ImageIndex
        	[in] -> the index of the image being set; three image representations are permitted: kImage1, kImage2, kImage3


        '''
        pass

    def image(self, index: MPxSelectionContext.ImageIndex,
                        ReturnStatus: MPxSelectionContext.MStatus): 
        '''
        image(self, index: MPxSelectionContext.ImageIndex,
                        ReturnStatus: MPxSelectionContext.MStatus) -> MString

        Synopsis
        -----
        This method is used to retrieve an XPM icon image that has
        previously been set for this tool context. This icon image will
        be used to represent this tool context in various places
        including the tool bar and can be queried from mel using the
        contextInfo command.

        Returns: 
        ----- 
        String name

        Parameters:
        -----
        index: MPxSelectionContext.ImageIndex
        	[in] -> the index for the image being retrieved; three image representations are permitted: kImage1, kImage2, kImage3 

        ReturnStatus: MPxSelectionContext.MStatus
        	[out] -> Status code (see below)


        '''
        pass

    def isSelecting(self): 
        '''
        isSelecting(self) -> bool

        Synopsis
        -----
        USE _isSelecting() IN SCRIPT. Determines whether an object is
        selected.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def startPoint(self): 
        '''
        startPoint(self) -> MPoint

        Synopsis
        -----
        USE _startPoint() IN SCRIPT. Returns the position of button
        press.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def lastDragPoint(self): 
        '''
        lastDragPoint(self) -> MPoint

        Synopsis
        -----
        USE _lastDragPoint() IN SCRIPT. Returns the position of the last
        drag point.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def abortAction(self): 
        '''
        abortAction(self)

        Synopsis
        -----
        This method is called when the abort key is pressed. The default
        abort key in Maya is the escape key. Users can override this
        method if they wish to perform certain operations when the abort
        key is pressed. Reimplemented from MPxContext.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def processNumericalInput(self, values: MDoubleArray,
                        flags: MIntArray,
                        isAbsolute: bool): 
        '''
        processNumericalInput(self, values: MDoubleArray,
                        flags: MIntArray,
                        isAbsolute: bool) -> bool

        Synopsis
        -----
        This method processes the input from the numerical input field.
        Users can override this method if they wish to process numerical
        input. For a given entry in the numeric input field, if the user
        types a dot ".", this indicates that the entry should not be
        modified. The overridden version of this method should take this
        into account using the ignoreEntry method with the flags that are
        passed in. The overridden version of this method should also
        process the numeric input as an absolute input or relative input
        depending on whether the isAbsolute flag is true or not. The
        return value should indicate whether or not the numerical input
        has been processed.Reimplemented from MPxContext.

        Returns: 
        ----- 
        false the default return value.

        Parameters:
        -----
        values: MDoubleArray
        	[in] -> the values from the numerical input field 

        flags: MIntArray
        	[in] -> used in conjunction with the ignoreEntry method, determines whether or not a given entry should be ignored 

        isAbsolute: bool
        	[in] -> whether or not the input should be interpreted as absolute


        '''
        pass

    def feedbackNumericalInput(self): 
        '''
        feedbackNumericalInput(self) -> bool

        Synopsis
        -----
        This method is called to update the numerical feedback. The
        format and values for the feedback line can be set through the
        methods in MFeedbackLine, specifically setFormat and setValue.
        The return value should indicate whether or not the numerical
        feedback has been provided.Reimplemented from MPxContext.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def argTypeNumericalInput(self, index: int): 
        '''
        argTypeNumericalInput(self, index: int) -> MSyntax.MSyntax

        Synopsis
        -----
        This method is used by the feedback line to determine what units
        to display. Users should override this method to return the
        appropriate argument type for the given index of the numeric
        input field. Specifically, this method should be overridden to
        return one of the following:Reimplemented from MPxContext.

        Returns: 
        ----- 
        MSyntax::kNoArg the default return value

        Parameters:
        -----
        index: int
        	[in] -> the index of the numerical input whose argument type is requested


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

class MPxSkinCluster:
    '''Base class for user-defined skin deformers.
MPxSkinCluster allows the creation of user-defined skin deformers. It derives
from
MPxGeometryFilter and so offers all the functionality of that class. Additionally,
it has the per-vertex skin weights and other skin-related
attributes of the Maya built-in skinCluster node.
Custom nodes derived from
MPxSkinCluster are treated by Maya just like the built-in skinCluster, so all
the weight painting/editing etc. tools that artists are used to
also work on the custom nodes.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MPxNode.MPxNode

        Synopsis
        -----
        This method returns the type of the node. This method should not
        be overridden by the user. It will return
        MPxNode::kSkinCluster.Reimplemented from MPxGeometryFilter.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def weightValue(self, block: MDataBlock,
                        multiIndex: int,
                        wtIndex: int): 
        '''
        weightValue(self, block: MDataBlock,
                        multiIndex: int,
                        wtIndex: int) -> float

        Synopsis
        -----
        This method returns the weightValue stored in the datablock for
        the given geometry's lattice point/CV/vertex.

        Returns: 
        ----- 
        Weight

        Parameters:
        -----
        block: MDataBlock
        	[in] -> the datablock for the node 

        multiIndex: int
        	[in] -> the index corresponding to the geometry 

        wtIndex: int
        	[in] -> the index corresponding to the component


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

class MPxSpringNode:
    '''Base class for user defined spring law.
MPxSpringNode allows the creation and manipulation of dependency graph nodes
representing a spring law. The class is a DAG node and Maya
manages the drawing, creation, and selection of springs.
A user defined spring node is a DAG node that can have attributes
and a
applySpringLaw() method. To derive the full benefit of the
MPxSpringNode class, it is suggested that you do not write your own
compute() method. Instead, write the
applySpringLaw() method. All of the parameters passed into this method will be
supplied by Maya.
To create a user defined spring node, derive from this class and
override the
applySpringLaw() method. The other methods of the parent class
MPxNode may also be overridden to perform dependency node capabilities.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MPxNode.MPxNode

        Synopsis
        -----
        This method returns the type of the node. It should not be
        overridden by the user. It will return
        MPxNode::kSpringNode.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def applySpringLaw(self, stiffness: double,
                        damping: double,
                        restLength: double,
                        endMass1: double,
                        endMass2: double,
                        endP1: MVector,
                        endP2: MVector,
                        endV1: MVector,
                        endV2: MVector,
                        forceV1: MVector,
                        forceV2: MVector): 
        '''
        applySpringLaw(self, stiffness: double,
                        damping: double,
                        restLength: double,
                        endMass1: double,
                        endMass2: double,
                        endP1: MVector,
                        endP2: MVector,
                        endV1: MVector,
                        endV2: MVector,
                        forceV1: MVector,
                        forceV2: MVector)

        Synopsis
        -----
        This method should be overridden in user defined nodes.

        Returns:
        -----
        None

        Parameters:
        -----
        stiffness: double
        	[in] -> The strength with which springs are trying to maintain their length. 

        damping: double
        	[in] -> How strongly the motion of springs are damped by the 'physical' properties of the springs. A larger value makes the springs converge faster to their rest length. 

        restLength: double
        	[in] -> The length at which springs try to stay. 

        endMass1: double
        	[in] -> The mass value at one end of the spring. 

        endMass2: double
        	[in] -> The mass value at the other end of the spring. 

        endP1: MVector
        	[in] -> The position of one end of the spring. 

        endP2: MVector
        	[in] -> The position of the other end of the spring. 

        endV1: MVector
        	[in] -> The velocity of one end of the spring. 

        endV2: MVector
        	[in] -> The velocity of the other end of the spring. 

        forceV1: MVector
        	[in] -> The output force vector at one end of the spring. 

        forceV2: MVector
        	[in] -> The output force vector at the other end of the spring.


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

    def thisMObject(self): 
        '''
        thisMObject(self) -> MObject

        Synopsis
        -----
        Returns the MObject associated with this user defined node. This
        makes it possible to use MFnDependencyNode or to construct plugs
        to this node's attributes.It is not necessary to override this
        method.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MPxSurfaceShape:
    '''Parent class of all user defined shapes.
MPxSurfaceShape is the parent class of all user defined shapes. User defined
shapes are dependency nodes (and DAG nodes) which contain
overridable drawing, selection, and component methods.
This class can be used to implement new kinds of shapes within
Maya that can have selectable/manipulatable components and behave
in a similar manner to the default shapes in maya.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MPxNode.MPxNode

        Synopsis
        -----
        Returns the type of node that this is. This is used to
        differentiate user defined nodes that are derived off different
        MPx base classes.It is not necessary to override this
        method.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def isBounded(self): 
        '''
        isBounded(self) -> bool

        Synopsis
        -----
        This method should be overridden to return true if the user
        supplies a bounding box routine. Supplying a bounding box routine
        makes refresh and selection more efficient.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def boundingBox(self): 
        '''
        boundingBox(self) -> MBoundingBox

        Synopsis
        -----
        This method should be overridden to return a bounding box for the
        shape. If this method is overridden, then
        MPxSurfaceShape::isBounded should also be overridden to return
        true.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def evalNodeAffectsDrawDb(self, evaluationNode: MEvaluationNode): 
        '''
        evalNodeAffectsDrawDb(self, evaluationNode: MEvaluationNode) -> bool

        Synopsis
        -----
        This method should be overridden to return true if the
        evaluationNode contains any dirty plugs that will affect the
        drawing of your plug-in.

        Returns: 
        ----- 
        True if the evaluationNode contains plugs that will affect
        drawing

        Parameters:
        -----
        evaluationNode: MEvaluationNode
        	[in] -> Evaluation information for this surface node


        '''
        pass

    @overload
    def transformUsing(self, matrix: MMatrix,
                        componentList: MObjectArray): 
        '''
        transformUsing(self, matrix: MMatrix,
                        componentList: MObjectArray)

        Synopsis
        -----
        Transform the given components using the specified transformation
        matrix. This method should be overridden if the shape supports
        components that can be transformed using maya's move, scale, and
        rotate tools.Reimplemented in MPxComponentShape.

        Returns:
        -----
        None

        Parameters:
        -----
        matrix: MMatrix
        	[in] -> the matrix representing the transformation that is to be applied to the components 

        componentList: MObjectArray
        	[in] -> a list of components to be tranformed. If the list is empty, it indicates that every point in the geometry should be transformed. 


        '''
        pass

    @overload
    def transformUsing(self, mat: MMatrix,
                        componentList: MObjectArray,
                        cachingMode: MPxSurfaceShape.MVertexCachingMode,
                        pointCache: MPointArray): 
        '''
        transformUsing(self, mat: MMatrix,
                        componentList: MObjectArray,
                        cachingMode: MPxSurfaceShape.MVertexCachingMode,
                        pointCache: MPointArray)

        Synopsis
        -----
        Transform the given components using the specified transformation
        matrix. This method should be overridden if the shape supports
        components that can be transformed using maya's move, scale, and
        rotate tools.Reimplemented in MPxComponentShape.

        Returns:
        -----
        None

        Parameters:
        -----
        mat: MMatrix
        	[in] -> the matrix representing the transformation that is to be applied to the components 

        componentList: MObjectArray
        	[in] -> a list of components to be transformed. If the list is empty, it indicates that every point in the geometry should be transformed. 

        cachingMode: MPxSurfaceShape.MVertexCachingMode
        	[in] -> whether the points should be cached in the pointCache argument, or restored from the pointCache 

        pointCache: MPointArray
        	[in] -> used to store for undo and restore points during undo 


        '''
        pass

    def tweakUsing(self, mat: MMatrix,
                        componentList: MObjectArray,
                        cachingMode: MPxSurfaceShape.MVertexCachingMode,
                        pointCache: MPointArray,
                        handle: MArrayDataHandle): 
        '''
        tweakUsing(self, mat: MMatrix,
                        componentList: MObjectArray,
                        cachingMode: MPxSurfaceShape.MVertexCachingMode,
                        pointCache: MPointArray,
                        handle: MArrayDataHandle)

        Synopsis
        -----
        Transform the given components using the specified transformation
        matrix. This method should be overridden if the shape supports
        components that can be transformed using maya's move, scale, and
        rotate tools. This method is called when the shape has history &
        connected to a tweak node. The most common reason why the shape
        would be connected to a tweak node is if it is being deformed.
        When a shape is connected to a tweak node, transformations
        applied to the points are placed in the tweak node rather than in
        the shape itself.

        Returns:
        -----
        None

        Parameters:
        -----
        mat: MMatrix
        	[in] -> the matrix representing the transformation that is to be applied to the components 

        componentList: MObjectArray
        	[in] -> a list of components to be tranformed. If the list is empty, it indicates that every point in the geometry should be transformed. 

        cachingMode: MPxSurfaceShape.MVertexCachingMode
        	[in] -> whether the points should be cached in the pointCache argument, or restored from the pointCache 

        pointCache: MPointArray
        	[in] -> used to store for undo and restore points during undo 

        handle: MArrayDataHandle
        	[in] -> array data handle where the tweaks are stored 


        '''
        pass

    def convertToTweakNodePlug(self, plug: MPlug): 
        '''
        convertToTweakNodePlug(self, plug: MPlug) -> bool

        Synopsis
        -----
        Check if a tweak node is connected to this node. If it is, then
        reset the supplied plug to contain the controlPoints attribute on
        the tweak node.

        Returns: 
        ----- 
        true if a tweak node was found, false if the plug was unchanged

        Parameters:
        -----
        plug: MPlug
        	[in] -> plug which will be set to point to the associated tweak node plug if a tweak node is connected


        '''
        pass

    def weightedTransformUsing(self, xform: MTransformationMatrix,
                        space: MMatrix,
                        componentList: MObjectArray,
                        cachingMode: MPxSurfaceShape.MVertexCachingMode,
                        pointCache: MPointArray,
                        freezePlane: MPlane): 
        '''
        weightedTransformUsing(self, xform: MTransformationMatrix,
                        space: MMatrix,
                        componentList: MObjectArray,
                        cachingMode: MPxSurfaceShape.MVertexCachingMode,
                        pointCache: MPointArray,
                        freezePlane: MPlane)

        Synopsis
        -----
        Transform the given components with interpolation using the
        specified transformation matrix. If not overridden, then a
        default implementation will be used to perform the transformation
        and interpolation. The default implementation calls setPoint()
        for each transformed point.

        Returns:
        -----
        None

        Parameters:
        -----
        xform: MTransformationMatrix
        	[in] -> the matrix representing the transformation that is to be applied to the components 

        space: MMatrix
        	[in] -> the matrix representing the transformation space to perform the interpolated transformation. A value of NULL indicates it should be ignored. 

        componentList: MObjectArray
        	[in] -> a list of components to be transformed and their weights. This list will not be empty. 

        cachingMode: MPxSurfaceShape.MVertexCachingMode
        	[in] -> whether the points should be added/updated in the pointCache, restored from the pointCache, or transform using use the original values in the pointCache. 

        pointCache: MPointArray
        	[in] -> used to store for undo and restore points during undo 

        freezePlane: MPlane
        	[in] -> used for symmetric transformation of components. A value of NULL indicates it is not used and there is no symmetric transformation. 


        '''
        pass

    def weightedTweakUsing(self, xform: MTransformationMatrix,
                        space: MMatrix,
                        componentList: MObjectArray,
                        cachingMode: MPxSurfaceShape.MVertexCachingMode,
                        pointCache: MPointArray,
                        freezePlane: MPlane,
                        handle: MArrayDataHandle): 
        '''
        weightedTweakUsing(self, xform: MTransformationMatrix,
                        space: MMatrix,
                        componentList: MObjectArray,
                        cachingMode: MPxSurfaceShape.MVertexCachingMode,
                        pointCache: MPointArray,
                        freezePlane: MPlane,
                        handle: MArrayDataHandle)

        Synopsis
        -----
        Transform the given components with interpolation using the
        specified transformation matrix. This method is called for
        transforming components using maya's move, scale, and rotate
        tools when the shape has history and is connected to a tweak
        node. The most common reason why the shape would be connected to
        a tweak node is if it is being deformed. When a shape is
        connected to a tweak node, transformations applied to the points
        are placed in the tweak node rather than in the shape itself.If
        not overridden, then a default implementation will be used to
        perform the transformation and interpolation. The default
        implementation calls setPoint() for each transformed point.

        Returns:
        -----
        None

        Parameters:
        -----
        xform: MTransformationMatrix
        	[in] -> the matrix representing the transformation that is to be applied to the components 

        space: MMatrix
        	[in] -> the matrix representing the transformation space to perform the interpolated transformation. A value of NULL indicates it should be ignored. 

        componentList: MObjectArray
        	[in] -> a list of components to be transformed and their weights. This list will not be empty. 

        cachingMode: MPxSurfaceShape.MVertexCachingMode
        	[in] -> whether the points should be added/updated in the pointCache, restored from the pointCache, or transform using the original values in the pointCache. 

        pointCache: MPointArray
        	[in] -> used to store for undo and restore points during undo 

        freezePlane: MPlane
        	[in] -> used for symmetric transformation of components. A value of NULL indicates it is not used and there is no symmetric transformation. 

        handle: MArrayDataHandle
        	[in] -> array data handle where the tweaks are stored 


        '''
        pass

    def vertexOffsetDirection(self, component: MObject,
                        direction: MVectorArray,
                        mode: MPxSurfaceShape.MVertexOffsetMode,
                        normalize: bool): 
        '''
        vertexOffsetDirection(self, component: MObject,
                        direction: MVectorArray,
                        mode: MPxSurfaceShape.MVertexOffsetMode,
                        normalize: bool) -> bool

        Synopsis
        -----
        This method should be overridden if the shape supports components
        that can be moved in the direction of the normal or UV's using
        the move vertex normal tool. This method should calculate the
        offset direction for a vertex components. The direction vector
        array is an array of offsets corresponding to the elements in the
        component. The mode argument specifies the type of movement that
        is being performed.The default for this method is to return
        false, i.e. no support for move normal tool.

        Returns: 
        ----- 
        true if the shape supports the current mode, false if the shape
        cannot do the requested vertex move

        Parameters:
        -----
        component: MObject
        	[in] -> 

        direction: MVectorArray
        	[in] -> 

        mode: MPxSurfaceShape.MVertexOffsetMode
        	[in] -> The type of vertex movement

        normalize: bool
        	[in] -> specifies whether the offset vectors should be normalized


        '''
        pass

    def newControlPointComponent(self): 
        '''
        newControlPointComponent(self) -> MObject

        Synopsis
        -----
        The default action of this method is to return an
        MFnSingleIndexedComponent (of type MFn::kMeshVertComponent) in
        order to support rigid skinning binds. This method can be
        overridden to support other types of components such as
        MFnDoubleIndexedComponent and MFnTripleIndexedComponent and
        should return a new component of that type. The types allowed are
        those listed in the create() method docs for each
        MFn*IndexedComponent.No argument is required.The skinning code
        handles the deallocation of the new component.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def componentToPlugs(self, component: MObject,
                        list: MSelectionList): 
        '''
        componentToPlugs(self, component: MObject,
                        list: MSelectionList)

        Synopsis
        -----
        Converts the given component into a selection list of plugs. This
        method is used to associate a shapes components into the
        corresponding attributes (plugs) within the shape. For example,
        it gets called by the translate manipulator to determine which
        attributes should be driven by the manipulator, and by the
        setKeyframe command to determine where to connect animCurves for
        components.This method should be overridden if the shape supports
        components that can be selected and moved in Maya.Reimplemented
        in MPxComponentShape.

        Returns:
        -----
        None

        Parameters:
        -----
        component: MObject
        	[in] -> the component to be converted 

        list: MSelectionList
        	[in] -> a selection list where the plug should be added 


        '''
        pass

    def match(self, mask: MSelectionMask,
                        componentList: MObjectArray): 
        '''
        match(self, mask: MSelectionMask,
                        componentList: MObjectArray) -> bool

        Synopsis
        -----
        This method is used to check for matches between a selection type
        (or mask) and a given component. If your shape has components
        representing attributes then this method is used to match up your
        components with selection masks.This is used by sets and
        deformers to make sure that the selected components fall into the
        "vertex only" category. This is useful when you want to make sure
        that only a particular component can be deformed.Reimplemented in
        MPxComponentShape.

        Returns: 
        ----- 
        true the match was successfull  false the match failed

        Parameters:
        -----
        mask: MSelectionMask
        	[in] -> the selection mask to test against 

        componentList: MObjectArray
        	[in] -> a list of components to be tested


        '''
        pass

    def matchComponent(self, item: MSelectionList,
                        spec: MAttributeSpecArray,
                        list: MSelectionList): 
        '''
        matchComponent(self, item: MSelectionList,
                        spec: MAttributeSpecArray,
                        list: MSelectionList) -> MPxSurfaceShape.MPxSurfaceShape

        Synopsis
        -----
        This method is used to convert the string representation of a
        component into a component object and to validate that the
        indices. This method should be overridden if the shape has
        components.

        Returns: 
        ----- 
        The component match result

        Parameters:
        -----
        item: MSelectionList
        	[in] -> DAG selection item for the object being matched 

        spec: MAttributeSpecArray
        	[in] -> attribute specification object 

        list: MSelectionList
        	[in] -> list to add components to


        '''
        pass

    def getShapeSelectionMask(self): 
        '''
        getShapeSelectionMask(self) -> MSelectionMask

        Synopsis
        -----
        This routine must be overridden if the shape is to support
        interactive object selection in Viewport 2.0 and should provide
        information about the selection mask of the shape.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getComponentSelectionMask(self): 
        '''
        getComponentSelectionMask(self) -> MSelectionMask

        Synopsis
        -----
        This routine must be overridden if the shape is to support
        interactive component selection in Viewport 2.0 and should
        provide information about the selection mask of the shape
        component.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def createFullVertexGroup(self): 
        '''
        createFullVertexGroup(self) -> MObject

        Synopsis
        -----
        This method is used to create a component containing every
        vertex/CV in the object. This method is supposed to return non-
        NULL only if the dag object contains vertices/CVs (control
        points), so derived classes that do should override this
        method.Eg: use MFnSingleIndexedComponent::setCompleteData(
        numVertices ) to specify that a component represents all the
        vertices of the shape.Reimplemented in MPxComponentShape.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def createFullRenderGroup(self): 
        '''
        createFullRenderGroup(self) -> MObject

        Synopsis
        -----
        This method is used to create a component containing every
        renderable element in the object. This method is supposed to
        return non-NULL only if the dag object contains renderable
        components. Type of the return component should is the same as
        the one returned by
        MPxSurfaceShape::renderGroupComponentType().Eg: use
        MFnSingleIndexedComponent::setCompleteData( numFaces ) to specify
        that a component represents all the faces of the shape.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def renderGroupComponentType(self): 
        '''
        renderGroupComponentType(self) -> MFn.MFn

        Synopsis
        -----
        This method is used to return the type of renderable components
        for this shape. It should return a type among
        MFn::kMeshPolygonComponent, MFn::kSubdivFaceComponent and
        MFn::kSurfaceFaceComponent, which is used in the creation of per-
        face/patch shader assignment.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def deleteComponents(self, componentList: MObjectArray,
                        undoInfo: MDoubleArray): 
        '''
        deleteComponents(self, componentList: MObjectArray,
                        undoInfo: MDoubleArray) -> bool

        Synopsis
        -----
        This method should be overridden if the shape is to support
        deletion of components. A list of components to be deleted will
        be passed in as well as an array of doubles where information
        about each deleted component can be stored for undo purposes. A
        typical use for this array is to store knot values or weights for
        control points that are deleted.

        Returns: 
        ----- 
        true if this method was successful, false otherwise

        Parameters:
        -----
        componentList: MObjectArray
        	[in] -> List of components to be deleted 

        undoInfo: MDoubleArray
        	[in] -> Values used for undo purposes


        '''
        pass

    def undeleteComponents(self, componentList: MObjectArray,
                        undoInfo: MDoubleArray): 
        '''
        undeleteComponents(self, componentList: MObjectArray,
                        undoInfo: MDoubleArray) -> bool

        Synopsis
        -----
        This method should be overridden if the shape is to support
        undeletion of components. A list of components to be deleted will
        be passed in as well as an array of doubles where information
        about each deleted component is stored for undo purposes. A
        typical use for this array is to store knot values or weights for
        control points that are deleted.

        Returns: 
        ----- 
        true if this method was successful, false otherwise

        Parameters:
        -----
        componentList: MObjectArray
        	[in] -> List of components that were deleted 

        undoInfo: MDoubleArray
        	[in] -> Values used for undo purposes


        '''
        pass

    def localShapeInAttr(self): 
        '''
        localShapeInAttr(self) -> MObject

        Synopsis
        -----
        Returns the attribute containing the shape's input geometry in
        local space. The attribute must be writable and of a geometry
        data type (e.g. MFn::kGeometryData, MFn::kPluginGeometryData,
        etc).This method will be called by Maya to determine if the shape
        has construction history and must be overridden if the shape is
        to support deformers.Reimplemented in MPxComponentShape.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def localShapeOutAttr(self): 
        '''
        localShapeOutAttr(self) -> MObject

        Synopsis
        -----
        Returns the attribute containing the shape's output geometry in
        local space. The attribute must be readable and of a geometry
        data type (e.g. MFn::kGeometryData, MFn::kPluginGeometryData,
        etc).This method must be overridden if the shape is to support
        deformers.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def worldShapeOutAttr(self): 
        '''
        worldShapeOutAttr(self) -> MObject

        Synopsis
        -----
        Returns the attribute containing the shape's output geometry in
        world space. The attribute must be readable and of a geometry
        data type (e.g. MFn::kGeometryData, MFn::kPluginGeometryData,
        etc).This method must be overridden if the shape is to support
        deformers.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def cachedShapeAttr(self): 
        '''
        cachedShapeAttr(self) -> MObject

        Synopsis
        -----
        Returns the attribute containing the shape's cached geometry, if
        it has one. The attribute must be readable, writable and of a
        geometry data type (e.g. MFn::kGeometryData,
        MFn::kPluginGeometryData, etc).

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def geometryData(self): 
        '''
        geometryData(self) -> MObject

        Synopsis
        -----
        Returns the geometry data of the shape. The geometry data must be
        derived from the MPxGeometryData class.The data is used by Maya
        to add, edit and query component grouping (set) information for
        the shape. This set information is stored and managed by Maya's
        shape base class, geometryShape.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def canMakeLive(self): 
        '''
        canMakeLive(self) -> bool

        Synopsis
        -----
        This method is used by Maya to determine whether a surface can be
        made live. It can be overridden to return true if you wish to
        allow your surface to be made live. If you return true, you will
        also need to implement both closestPoint() overloads. The default
        is to return false.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def closestPoint(self, raySource: MPoint,
                        rayDirection: MVector,
                        theClosestPoint: MPoint,
                        theClosestNormal: MVector,
                        findClosestOnMiss: bool,
                        tolerance: double): 
        '''
        closestPoint(self, raySource: MPoint,
                        rayDirection: MVector,
                        theClosestPoint: MPoint,
                        theClosestNormal: MVector,
                        findClosestOnMiss: bool,
                        tolerance: double) -> bool

        Synopsis
        -----
        This method is used by Maya for snapping queries when your
        surface is live. If you override this method, you should set
        theClosestPoint to the closest point on your surface intersected
        by the ray defined by raySource and rayDirection. You should also
        populate the theClosestNormal parameter with the surface normal
        at that intersection point.If no intersection is found and
        findClosestOnMiss is true, you should still provide a point on
        your surface closest to the ray defined by raySource and
        rayDirection. When used for live snapping, this allows the user
        to click and drag outside the bounds of a live surface and still
        have it snap to the nearest point on it within the viewport.
        Note, performing a pure 3D closest point of approach test in this
        situation may not give the most natural result for live mesh
        snapping. To provide behavior that matches Maya, you can project
        your surface onto the plane defined by the ray, then perform your
        calculations. This will account for view perspective and give
        accurate live snap points along the silhouette of the surface.If
        findClosestOnMiss is false, you should not provide a point and
        normal when the ray misses.canMakeLive() must also be overridden
        to return true.

        Returns: 
        ----- 
        true if theClosestPoint and theClosestNormal have been set, false
        otherwise

        Parameters:
        -----
        raySource: MPoint
        	[in] -> the origin of the ray to test against 

        rayDirection: MVector
        	[in] -> the direction of the ray to test against 

        theClosestPoint: MPoint
        	[out] -> the closest point on your surface 

        theClosestNormal: MVector
        	[out] -> the normal at the closest point on your surface 

        findClosestOnMiss: bool
        	[in] -> when true, you should calculate theClosestPoint and theClosestNormal even if the ray misses your surface. 

        tolerance: double
        	[in] -> tolerance to use in your calculations


        '''
        pass

    @overload
    def closestPoint(self, toThisPoint: MPoint,
                        theClosestPoint: MPoint,
                        tolerance: double): 
        '''
        closestPoint(self, toThisPoint: MPoint,
                        theClosestPoint: MPoint,
                        tolerance: double)

        Synopsis
        -----
        This method is used by Maya in functions (such as select) that
        require closest point information from your surface. If you've
        overridden canMakeLive() to return true, this method is also used
        by Maya for some snapping queries when your surface is live.

        Returns:
        -----
        None

        Parameters:
        -----
        toThisPoint: MPoint
        	[in] -> the point to test against 

        theClosestPoint: MPoint
        	[out] -> the closest point on your surface 

        tolerance: double
        	[in] -> tolerance to use in your calculations 


        '''
        pass

    def pointAtParm(self, atThisParm: MPoint,
                        evaluatedPoint: MPoint): 
        '''
        pointAtParm(self, atThisParm: MPoint,
                        evaluatedPoint: MPoint) -> bool

        Synopsis
        -----
        This method is used by Maya in functions (such as select) that
        require point at parameter values. This only makes sense for
        parametric surfaces such as NURBS.

        Returns: 
        ----- 
        true if a point was found, false otherwise

        Parameters:
        -----
        atThisParm: MPoint
        	[in] -> the parameter to check 

        evaluatedPoint: MPoint
        	[out] -> the surface point


        '''
        pass

    @overload
    def acceptsGeometryIterator(self, writeable: bool): 
        '''
        acceptsGeometryIterator(self, writeable: bool) -> bool

        Synopsis
        -----
        If the shape can supply a component iterator then then this
        method should be overridden to return true. The default is to
        return false.

        Returns: 
        ----- 
        true the shape can supply an iterator  false the shape cannot
        supply an iterator

        Parameters:
        -----
        writeable: bool
        	[in] -> is this component type writable by an iterator


        '''
        pass

    @overload
    def acceptsGeometryIterator(self, component: MObject,
                        writeable: bool,
                        forReadOnly: bool): 
        '''
        acceptsGeometryIterator(self, component: MObject,
                        writeable: bool,
                        forReadOnly: bool) -> bool

        Synopsis
        -----
        If the shape can supply a component iterator then then this
        method should be overridden to return true. The default is to
        return false. The component argument can be used to when the
        shape has multiple components and not all of them can be iterator
        over.

        Returns: 
        ----- 
        true the shape can supply an iterator  false the shape cannot
        supply an iterator

        Parameters:
        -----
        component: MObject
        	[in] -> the component to test 

        writeable: bool
        	[in] -> is this component type writable by an iterator 

        forReadOnly: bool
        	[in] -> is this component type readable by an iterator


        '''
        pass

    def excludeAsPluginShape(self): 
        '''
        excludeAsPluginShape(self) -> bool

        Synopsis
        -----
        A Maya viewport can be set to not display "Plugin Shapes", which
        means shapes derived from MPxSurfaceShape. By overriding
        excludeAsPluginShape() to return false, you can change that
        behaviour so that this shape is still displayed even when the
        display of "Plugin Shapes" is disabled.The default implementation
        returns true.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def activeComponents(self): 
        '''
        activeComponents(self) -> MObjectArray

        Synopsis
        -----
        Returns a list of active (selected) components for the shape.
        This method does not trigger evaluation.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def hasActiveComponents(self): 
        '''
        hasActiveComponents(self) -> bool

        Synopsis
        -----
        This method is used to determine whether or not the shape has
        active (selected) components. This method does not trigger
        evaluation.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def childChanged(self, state: MPxSurfaceShape.MChildChanged): 
        '''
        childChanged(self, state: MPxSurfaceShape.MChildChanged)

        Synopsis
        -----
        This method can be used to trigger the shape to recalculate its
        bounding box.

        Returns:
        -----
        None

        Parameters:
        -----
        state: MPxSurfaceShape.MChildChanged
        	[in] -> the type of change that has occurred 


        '''
        pass

    def isRenderable(self): 
        '''
        isRenderable(self) -> bool

        Synopsis
        -----
        Returns true if the shape is a renderable shape. Making a shape
        renderable allows the shape to have shading group assignments.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setRenderable(self, flag: bool): 
        '''
        setRenderable(self, flag: bool)

        Synopsis
        -----
        Specifies whether the shape is a renderable shape. Making a shape
        renderable allows the shape to have shading group assignments.

        Returns:
        -----
        None

        Parameters:
        -----
        flag: bool
        	[in] -> true if the shape is to be renderable, false otherwise 


        '''
        pass

    def getWorldMatrix(self, block: MDataBlock,
                        instanceGeom: int): 
        '''
        getWorldMatrix(self, block: MDataBlock,
                        instanceGeom: int) -> MMatrix

        Synopsis
        -----
        Returns MMatrix which takes a point from local object space to
        world space.

        Returns:
        -----
        None

        Parameters:
        -----
        block: MDataBlock
        	[in] -> a 

        instanceGeom: int
        	[in] -> the instance this 


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

    def thisMObject(self): 
        '''
        thisMObject(self) -> MObject

        Synopsis
        -----
        Returns the MObject associated with this user defined node. This
        makes it possible to use MFnDependencyNode or to construct plugs
        to this node's attributes.It is not necessary to override this
        method.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MVertexCachingMode:
    '''Vertex caching modes. 
    Non-functional class.  Values for this enum:
    kNoPointCaching
    kSavePoints
    kRestorePoints
    kUpdatePoints
    kTransformOriginalPoints
    '''

    def __init__(self):
        pass

    def kNoPointCaching(self):
        '''This is an enum of MVertexCachingMode.
        - Description: No point caching. 
        - Value: 0
        '''
        pass

    def kSavePoints(self):
        '''This is an enum of MVertexCachingMode.
        - Description: Points should be saved for undo in the point cache. 
        - Value: 1
        '''
        pass

    def kRestorePoints(self):
        '''This is an enum of MVertexCachingMode.
        - Description: Points should be restored from the point cache. 
        - Value: 2
        '''
        pass

    def kUpdatePoints(self):
        '''This is an enum of MVertexCachingMode.
        - Description: Transform and update the points in the point cache. 
        - Value: 3
        '''
        pass

    def kTransformOriginalPoints(self):
        '''This is an enum of MVertexCachingMode.
        - Description: Transform using use the original pre-transformation values stored in the pointCache. 
        - Value: 4
        '''
        pass

class MVertexOffsetMode:
    '''Vertex offset modes. 
    Non-functional class.  Values for this enum:
    kNormal
    kUTangent
    kVTangent
    kUVNTriad
    '''

    def __init__(self):
        pass

    def kNormal(self):
        '''This is an enum of MVertexOffsetMode.
        - Description: Move in normal direction. 
        - Value: 0
        '''
        pass

    def kUTangent(self):
        '''This is an enum of MVertexOffsetMode.
        - Description: Move in u tangent direction. 
        - Value: 1
        '''
        pass

    def kVTangent(self):
        '''This is an enum of MVertexOffsetMode.
        - Description: Move in v tangent direction. 
        - Value: 2
        '''
        pass

    def kUVNTriad(self):
        '''This is an enum of MVertexOffsetMode.
        - Description: Calculate u, v, and normal offsets. 
        - Value: 3
        '''
        pass

class MatchResult:
    '''Return values for the matchComponent() method. 
    Non-functional class.  Values for this enum:
    kMatchOk
    kMatchNone
    kMatchTooMany
    kMatchInvalidName
    kMatchInvalidAttribute
    kMatchInvalidAttributeIndex
    kMatchInvalidAttributeRange
    kMatchInvalidAttributeDim
    '''

    def __init__(self):
        pass

    def kMatchOk(self):
        '''This is an enum of MatchResult.
        - Description: The component was matched without error. 
        - Value: 0
        '''
        pass

    def kMatchNone(self):
        '''This is an enum of MatchResult.
        - Description: No component was matched. 
        - Value: 1
        '''
        pass

    def kMatchTooMany(self):
        '''This is an enum of MatchResult.
        - Description: Not used. 
        - Value: 2
        '''
        pass

    def kMatchInvalidName(self):
        '''This is an enum of MatchResult.
        - Description: One of the names in the attribute specification was not valid. 
        - Value: 3
        '''
        pass

    def kMatchInvalidAttribute(self):
        '''This is an enum of MatchResult.
        - Description: Not used. 
        - Value: 4
        '''
        pass

    def kMatchInvalidAttributeIndex(self):
        '''This is an enum of MatchResult.
        - Description: The attribute specification contained an index for a non-array attribute. 
        - Value: 5
        '''
        pass

    def kMatchInvalidAttributeRange(self):
        '''This is an enum of MatchResult.
        - Description: An attribute index was out of range. 
        - Value: 6
        '''
        pass

    def kMatchInvalidAttributeDim(self):
        '''This is an enum of MatchResult.
        - Description: The attribute specification provided the wrong number of dimensions for an attribute. 
        - Value: 7
        '''
        pass

class MChildChanged:
    '''Scope of change. 
    Non-functional class.  Values for this enum:
    kObjectChanged
    kBoundingBoxChanged
    '''

    def __init__(self):
        pass

    def kObjectChanged(self):
        '''This is an enum of MChildChanged.
        - Description: Object geometry changed. Internal caches need to be updated. 
        - Value: 0
        '''
        pass

    def kBoundingBoxChanged(self):
        '''This is an enum of MChildChanged.
        - Description: Object geometry is unchanged but its bounding box has changed. This might happen if the object was moved or an offset changed. 
        - Value: 1
        '''
        pass

class MPxSurfaceShapeUI:
    '''drawing and selection for user defined shapes
The base class for the UI portion of all user defined shapes.
'''
    def __init__(self):
        pass


    def select(self, selectInfo: MSelectInfo,
                        selectionList: MSelectionList,
                        worldSpaceSelectPts: MPointArray): 
        '''
        select(self, selectInfo: MSelectInfo,
                        selectionList: MSelectionList,
                        worldSpaceSelectPts: MPointArray) -> bool

        Synopsis
        -----
        This routine must be overriden if the shape is to support
        interactive object and/or component selection. The implementation
        of this method should call selectInfo.addSelection with
        information about the selected item and its selection mask. For
        single click selection, detected using the
        selectInfo.singleSection() method, the hit point should also be
        passed as an argument to selectInfo.addSelection.

        Returns: 
        ----- 
        true something was selected  false nothing was selected

        Parameters:
        -----
        selectInfo: MSelectInfo
        	[in] -> the Selection state information. 

        selectionList: MSelectionList
        	[out] -> List of items selected by this method. Do not update directly: use MSelectInfo::addSelection instead. 

        worldSpaceSelectPts: MPointArray
        	[out] -> List of points used to sort corresponding selections in single-select mode. (Closest to camera wins.) Do not update directly: use MSelectInfo::addSelection instead.


        '''
        pass

    def snap(self, snapInfo: MSelectInfo): 
        '''
        snap(self, snapInfo: MSelectInfo) -> bool

        Synopsis
        -----
        Maya calls this method when snapping to the shape's vertices. If
        you wish your custom shape to support point snapping then you
        must override this method and have it call snapInfo's
        MSelectInfo::setSnapPoint() method to set the point to be snapped
        to. If setSnapPoint() is called multiple times then the point
        closest to the cursor will be used.

        Returns: 
        ----- 
        true found a vertex to be snapped to  false found no vertex to be
        snapped to

        Parameters:
        -----
        snapInfo: MSelectInfo
        	[in] -> the Selection state information. 


        '''
        pass

    def canDrawUV(self): 
        '''
        canDrawUV(self) -> bool

        Synopsis
        -----
        Called by Maya to determine if this surface shape supports UV
        drawing.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def drawUV(self, view: M3dView,
                        info: MTextureEditorDrawInfo): 
        '''
        drawUV(self, view: M3dView,
                        info: MTextureEditorDrawInfo)

        Synopsis
        -----
        This method is called when the surface shape is selected and the
        texture view is open. Users should override this method if their
        custom shape supports UVs.

        Returns:
        -----
        None

        Parameters:
        -----
        view: M3dView
        	[in] -> Texture view in which to draw UVs. 

        info: MTextureEditorDrawInfo
        	[in] -> Drawing parameters. 


        '''
        pass

    def selectUV(self, view: M3dView,
                        selType: MPxSurfaceShapeUI.MPxSurfaceShapeUI,
                        xmin: int,
                        ymin: int,
                        xmax: int,
                        ymax: int,
                        singleSelect: bool,
                        selList: MSelectionList): 
        '''
        selectUV(self, view: M3dView,
                        selType: MPxSurfaceShapeUI.MPxSurfaceShapeUI,
                        xmin: int,
                        ymin: int,
                        xmax: int,
                        ymax: int,
                        singleSelect: bool,
                        selList: MSelectionList) -> bool

        Synopsis
        -----
        This method is called when the user performs a selection within
        the texture view. The method is called only when the surface
        shape is member of the active selection list.Maya provides the
        current viewport instance, the type of the selection, the extents
        of the selection rectangle (in viewport coordinates), and if the
        selection mode is single selection. The API user is expected to
        fill the selection list and return a result of true if 'something
        was selected'.To properly use this method, you must make sure
        that you have a valid component type that Maya can recognize.
        Selection tests can be done using a pick buffer or by spatially
        determining the selected objects.Important Currently Maya does
        not know how to manipulate custom UV components. This method only
        provides the facilities to visualize what has been selected in
        the viewport. The API user is responsible for implementing
        commands that can manipulate the currently selected UVs.

        Returns: 
        ----- 
        true if something was selected, false otherwise.

        Parameters:
        -----
        view: M3dView
        	[in] -> the texture drawing view 

        selType: MPxSurfaceShapeUI.MPxSurfaceShapeUI
        	[in] -> the selection type 

        xmin: int
        	[in] -> minimum x coordinate value of the selection rectangle. 

        ymin: int
        	[in] -> minimum y coordinate value of the selection rectangle. 

        xmax: int
        	[in] -> maximum x coordinate value of the selection rectangle. 

        ymax: int
        	[in] -> maximum y coordinate value of the selection rectangle. 

        singleSelect: bool
        	[in] -> indicates if the user is in single selection mode. 

        selList: MSelectionList
        	[out] -> the selection list to be populated.


        '''
        pass

    def material(self, path: MDagPath): 
        '''
        material(self, path: MDagPath) -> MMaterial

        Synopsis
        -----
        Returns the material associated with this shape. The user must
        supply a DAG path as a shape can have several materials if
        instanced.

        Returns: 
        ----- 
        The material associated with this shape

        Parameters:
        -----
        path: MDagPath
        	[in] -> the path for which to get the material


        '''
        pass

    def materials(self, path: MDagPath,
                        componentFilter: MObjectArray,
                        materials: MMaterialArray,
                        componentSet: MObjectArray): 
        '''
        materials(self, path: MDagPath,
                        componentFilter: MObjectArray,
                        materials: MMaterialArray,
                        componentSet: MObjectArray)

        Synopsis
        -----
        Returns a list of materials associated with this shape and a
        given list of components. The user must supply a DAG path as a
        shape can have several materials if instanced.

        Returns:
        -----
        None

        Parameters:
        -----
        path: MDagPath
        	[in] -> the path for which to get materials 

        componentFilter: MObjectArray
        	[in] -> the (optional) list of components to iterate over. If the list is empty, it will return materials for all components. 

        materials: MMaterialArray
        	[out] -> materials associated with this shape. 

        componentSet: MObjectArray
        	[out] -> optional output for components associated with each returned material. A 


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

class UVSelectionType:
    '''Selection modes for UVs. 
    Non-functional class.  Values for this enum:
    kSelectMeshUVs
    kSelectMeshVerts
    kSelectMeshFaces
    kSelectMeshEdges
    '''

    def __init__(self):
        pass

    def kSelectMeshUVs(self):
        '''This is an enum of UVSelectionType.
        - Description: The UV selection type is UVs. 
        - Value: 0
        '''
        pass

    def kSelectMeshVerts(self):
        '''This is an enum of UVSelectionType.
        - Description: The UV selection type is vertices. 
        - Value: 1
        '''
        pass

    def kSelectMeshFaces(self):
        '''This is an enum of UVSelectionType.
        - Description: The UV selection type is faces. 
        - Value: 2
        '''
        pass

    def kSelectMeshEdges(self):
        '''This is an enum of UVSelectionType.
        - Description: The UV selection type is edges. 
        - Value: 3
        '''
        pass

class MPxTexContext:
    '''Base class for user defined contexts working on uv editor.
This is the base class for user defined contexts working on uv
editor.
'''
    def __init__(self):
        pass


    def viewToPort(self, xView: double,
                        yView: double,
                        xPort: short,
                        yPort: short): 
        '''
        viewToPort(self, xView: double,
                        yView: double,
                        xPort: short,
                        yPort: short)

        Synopsis
        -----
        This method is used to convert view coordinates to port (window)
        coordinates.

        Returns:
        -----
        None

        Parameters:
        -----
        xView: double
        	[in] -> the x position at view coordinate 

        yView: double
        	[in] -> the y position at view coordinate 

        xPort: short
        	[out] -> the x position at window coordinate 

        yPort: short
        	[out] -> the y position at window coordinate 


        '''
        pass

    def portToView(self, xPort: short,
                        yPort: short,
                        xView: double,
                        yView: double): 
        '''
        portToView(self, xPort: short,
                        yPort: short,
                        xView: double,
                        yView: double)

        Synopsis
        -----
        This method is used to convert port (window) coordinates to view
        coordinates.

        Returns:
        -----
        None

        Parameters:
        -----
        xPort: short
        	[in] -> The x position at window coordinate 

        yPort: short
        	[in] -> The y position at window coordinate 

        xView: double
        	[out] -> The x position at view coordinate 

        yView: double
        	[out] -> The y position at view coordinate 


        '''
        pass

    def viewRect(self, left: double,
                        right: double,
                        bottom: double,
                        top: double): 
        '''
        viewRect(self, left: double,
                        right: double,
                        bottom: double,
                        top: double)

        Synopsis
        -----
        This method is used to get the current uv viewport dimensions.

        Returns:
        -----
        None

        Parameters:
        -----
        left: double
        	[out] -> Left coordinate of uv viewport. 

        right: double
        	[out] -> Right coordinate of uv viewport. 

        bottom: double
        	[out] -> Bottom coordinate of uv viewport. 

        top: double
        	[out] -> Top coordinate of uv viewport. 


        '''
        pass

    def portSize(self, width: double,
                        height: double): 
        '''
        portSize(self, width: double,
                        height: double)

        Synopsis
        -----
        This method is used to get the window dimension of the current uv
        viewport.

        Returns:
        -----
        None

        Parameters:
        -----
        width: double
        	[out] -> Width of the window. 

        height: double
        	[out] -> Height of the window. 


        '''
        pass

    def getMarqueeSelection(self, xMin: double,
                        yMin: double,
                        xMax: double,
                        yMax: double,
                        mask: MSelectionMask,
                        bPickSingle: bool,
                        bIgnoreSelectionMode: bool,
                        selectionList: MSelectionList): 
        '''
        getMarqueeSelection(self, xMin: double,
                        yMin: double,
                        xMax: double,
                        yMax: double,
                        mask: MSelectionMask,
                        bPickSingle: bool,
                        bIgnoreSelectionMode: bool,
                        selectionList: MSelectionList) -> bool

        Synopsis
        -----
        This method is called when the user performs a selection within
        the uv editor.

        Returns: 
        ----- 
        true if something was selected, false otherwise.

        Parameters:
        -----
        xMin: double
        	[in] -> Minimum x coordinate value of the selection rectangle. 

        yMin: double
        	[in] -> Minimum y coordinate value of the selection rectangle. 

        xMax: double
        	[in] -> Maximum x coordinate value of the selection rectangle. 

        yMax: double
        	[in] -> Maximum y coordinate value of the selection rectangle. 

        mask: MSelectionMask
        	[in] -> The selection mask. 

        bPickSingle: bool
        	[in] -> Indicate if the user is in single selection mode. 

        bIgnoreSelectionMode: bool
        	[in] -> If true, the user can select components even if component selection mode is not on. 

        selectionList: MSelectionList
        	[out] -> The selection list to be populated.


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

class MPxToolCommand:
    '''Base class for interactive tool commands.
This is the base class for interactive tool commands.
An interactive tool command is a command that can be invoked as a
MEL command or from within a user defined context (see
MPxContext).
Tool commands have the same functionality as MPxCommands, but
include several additional methods for use in interactive
contexts:
,
,
, and
.
'''
    def __init__(self):
        pass


    def doIt(self, args: MArgList): 
        '''
        doIt(self, args: MArgList)

        Synopsis
        -----
        This method should perform a command by setting up internal class
        data and then calling the redoIt method. The actual action
        performed by the command should be done in the redoIt method.
        This is a pure virtual method, and must be overridden in derived
        classes.Reimplemented from MPxCommand.Implemented in
        MPxPolyTweakUVInteractiveCommand.

        Returns:
        -----
        None

        Parameters:
        -----
        args: MArgList
        	[in] -> List of arguments passed to the command.


        '''
        pass

    def cancel(self): 
        '''
        cancel(self)

        Synopsis
        -----
        This method cancels the command. The user should override this
        method when the original program state needs to be
        restored.Reimplemented in MPxPolyTweakUVInteractiveCommand.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def finalize(self): 
        '''
        finalize(self)

        Synopsis
        -----
        This method is used to create a string representing the command
        and its arguments. Users should override this method and contruct
        an MArgList and then pass it to doFinalize for
        journalling.Reimplemented in MPxPolyTweakUVInteractiveCommand.

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

    def doFinalize(self, command: MArgList): 
        '''
        doFinalize(self, command: MArgList)

        Synopsis
        -----
        USE _doFinalize() IN SCRIPT. Call this method with an MArgList
        representing your command.This method will register the command
        with the undo manager for journalling.

        Returns:
        -----
        None

        Parameters:
        -----
        command: MArgList
        	[in] -> An 


        '''
        pass

class MPxTransform:
    '''Base class for user defined transforms.
MPxTransform allows the creation of user defined transform nodes. User
defined transform nodes can introduce new transform types or
change the transformation order. They are designed to be an
extension of the standard Maya transform node and include all of
the normal transform attributes. Standard behaviors such as limit
enforcement and attribute locking are managed by this class, but
may be overriden in derived classes.
In general, a complete implementation of user defined transforms
will require the deriving from two classes;
MPxTransform defines the node while
MPxTransformationMatrix describes the mathematical functions of the user defined
transform.
The
MPxTransform class is registered using the
MFnPlugin::registerTransform() method. Both the
MPxTransform and the
MPxTransformationMatrix classes are registered in the same method. This allows for a
clear association between a
MPxTransform and a
MPxTransformationMatrix. Both the
MPxTransform and the
MPxTransformationMatrix classes need unique MTypeIds.
MPxTransform nodes are DAG nodes and therefore a change to one element will
affect every node beneath the changed node. Since this can
involve quite a bit of calculation, DAG nodes internally handle
clean and dirty differently than other nodes. What this means is
that the
updateMatrixAttrs() method should be used when getting one of the matrix attributes
from a method on this node. Additionally, after a value is
changed, the appropriate dirty method (i.e. dirtyTranslate(),
dirtyRotate(), etc.) should be called. When in doubt,
dirtyMatrix() will flag everything as needing to be updated.
It is up to each transform node to determine if it will obey
limits or not. Since transform attributes may have limits or may
be involved in some sort of constraint, there needs to be a way
to accept, reject, or modify a value when a plug is set on the
node. The
mustCallValidateAndSet() method allows for this kind of control. When an attribute is
flagged with the
mustCallValidateAndSet() method in the initialize() method, every plug change will call
the
validateAndSetValue() method for approval. From the
validateAndSetValue() method things like limits and value locking can be enforced. It
is important to note that for new attributes on the transform
node, any locking or limits are left as an implementation detail.
If any of the public methods are affected by the addition of
transform components, or by the order of computation, they should
be overriden in the derived class. Many of the public methods are
used by internal Maya code and exist for more than just
convenience.
The
createTransformationMatrix() class must be overloaded if a transformation matrix other than
the default
MPxTransformationMatrix is used.
NOTES: 1) The
setDependentsDirty() virtual method is available in this class since
MPxTransform derives from
MPxNode. During a call to
MPxTransform::setDependentsDirty(), a plug-in should not invoke any of the dirty*() or
updateMatrixAttrs() calls of this class. For example, the methods
dirtyMatrix(),
dirtyTranslation() or
updateMatrixAttrs() should not be called. 2) Updating world space attributes is an
expensive operation. Maya updates world space attributes on
demand such as in the case of a getAttr being issued or a
connection exists for the attribute.
'''
    def __init__(self):
        pass


    def postConstructor(self): 
        '''
        postConstructor(self)

        Synopsis
        -----
        Post constructor. Internally maya creates two objects when a user
        defined node is created, the internal MObject and the user
        derived object. The association between the these two objects is
        not made until after the MPxNode constructor is called. This
        implies that no MPxNode member function can be called from the
        MPxNode constructor. The postConstructor will get called
        immediately after the constructor when it is safe to call any
        MPxNode member function. Reimplemented from MPxNode.

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
        type(self) -> _OPENMAYA_DEPRECATION_POP_WARNING MPxNode._OPENMAYA_DEPRECATION_POP_WARNING MPxNode

        Synopsis
        -----
        This method returns the type of the node. This method should not
        be overridden by the user. It will return
        MPxNode::kTransformNode.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def isBounded(self): 
        '''
        isBounded(self) -> bool

        Synopsis
        -----
        This method should be overridden to return true if the user
        supplies a bounding box routine. Supplying a bounding box routine
        makes refresh and selection more efficient.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def boundingBox(self): 
        '''
        boundingBox(self) -> MBoundingBox

        Synopsis
        -----
        This method should be overridden to return a bounding box for the
        transform. If this method is overridden, then
        MPxTransform::isBounded should also be overridden to return true.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def treatAsTransform(self): 
        '''
        treatAsTransform(self) -> bool

        Synopsis
        -----
        Maya's base transform node type is treated differently from node
        types which are derived from it. For example, the 'viewFit'
        command does not include transform nodes in its calculations but
        does include pointConstraint nodes which are derived from the
        transform node.By default, all custom transform node types are
        treated the same as Maya's base transform node type. Using the
        same example, by default a custom transform node will be excluded
        from the 'viewFit' command's calculations.This method allows that
        default behaviour to be changed. By overriding this method to
        return false, a custom node can turn off the special treatment
        accorded to transform nodes and instead have itself treated the
        same as Maya treats derived transform nodes.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def transformationMatrix(self): 
        '''
        transformationMatrix(self) -> const MPxTransformationMatrix&

        Synopsis
        -----
        This method returns a reference to the cached transformation
        matrix for current context.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def resetTransformation(self, matrix: MMatrix): 
        '''
        resetTransformation(self, matrix: MMatrix)

        Synopsis
        -----
        This method will reset the transformation matrix to one that is
        constructed with the passed MMatrix. How the new transformation
        matrix is created will depend on the transformation matrix class
        and its decomposeMatrix() method.

        Returns:
        -----
        None

        Parameters:
        -----
        matrix: MMatrix
        	[in] -> The matrix used for resetting this transform. 


        '''
        pass

    @overload
    def resetTransformation(self, xform: MPxTransformationMatrix): 
        '''
        resetTransformation(self, xform: MPxTransformationMatrix)

        Synopsis
        -----
        This method will reset the transformation matrix to the one
        specified by the passed transformation matrix pointer. The
        contents of the passed transformation matrix are copied into this
        class's transformation matrix.

        Returns:
        -----
        None

        Parameters:
        -----
        xform: MPxTransformationMatrix
        	[in] -> A pointer to the source transformation matrix. 


        '''
        pass

    def compute(self, plug: MPlug,
                        block: MDataBlock): 
        '''
        compute(self, plug: MPlug,
                        block: MDataBlock)

        Synopsis
        -----
        The transform's compute method. The compute method should call
        any supporting methods to proper handle limits as well as the
        cases where the plug's value should not change. The
        MPlug::isFreeToChange() method is used to determine if a plug's
        value may be changed.When the compute method on derived classes
        is invoked for an attribute not handled by the derived class, the
        derived class should call MPxTransform::compute to allow the base
        classes to handle the attribute.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
        plug: MPlug
        	[in] -> The plug to compute. 

        block: MDataBlock
        	[in] -> The data block.


        '''
        pass

    def computeLocalTransformation(self, xform: MPxTransformationMatrix,
                        block: MDataBlock): 
        '''
        computeLocalTransformation(self, xform: MPxTransformationMatrix,
                        block: MDataBlock)

        Synopsis
        -----
        This method computes the transformation matrix for a passed data
        block and places the output into a passed transformation matrix.
        The caller needs to allocate space for the passed transformation
        matrix.

        Returns:
        -----
        None

        Parameters:
        -----
        xform: MPxTransformationMatrix
        	[out] -> The transformation matrix to fill with computed values. 

        block: MDataBlock
        	[in] -> The data block used for the transformation matrix computation.


        '''
        pass

    def clearLimits(self): 
        '''
        clearLimits(self)

        Synopsis
        -----
        This method turns off all of the limits and sets them to their
        default values. Before this method is called, the base class
        clears all of the limits on the standard transform attributes, so
        this method only needs to be implemented for custom transform
        attributes.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def isLimited(self, type: MFnTransform.MFnTransform,
                        ReturnStatus: MPxTransform.MStatus): 
        '''
        isLimited(self, type: MFnTransform.MFnTransform,
                        ReturnStatus: MPxTransform.MStatus) -> bool

        Synopsis
        -----
        Determine if the specified limit attribute is enabled or
        disabled.

        Returns: 
        ----- 
        Returns true if the limit is enabled, otherwise false is
        returned.

        Parameters:
        -----
        type: MFnTransform.MFnTransform
        	[in] -> An enum specifying the type of limit to query. 

        ReturnStatus: MPxTransform.MStatus
        	[out] -> Status.


        '''
        pass

    def limitValue(self, type: MFnTransform.MFnTransform,
                        ReturnStatus: MPxTransform.MStatus): 
        '''
        limitValue(self, type: MFnTransform.MFnTransform,
                        ReturnStatus: MPxTransform.MStatus) -> double

        Synopsis
        -----
        Returns the current value of the specified limit in internal
        units as a double.

        Returns: 
        ----- 
        Returns the current value of the specified limit in internal
        units as a double.

        Parameters:
        -----
        type: MFnTransform.MFnTransform
        	[in] -> An enum indicating the type of limit to query. 

        ReturnStatus: MPxTransform.MStatus
        	[out] -> Status.


        '''
        pass

    def setLimit(self, type: MFnTransform.MFnTransform,
                        value: double): 
        '''
        setLimit(self, type: MFnTransform.MFnTransform,
                        value: double)

        Synopsis
        -----
        Change the limit value for the specified limit type, and
        automatically enable the limit to be true.

        Returns:
        -----
        None

        Parameters:
        -----
        type: MFnTransform.MFnTransform
        	[in] -> An enum indicating the limit to set. 

        value: double
        	[in] -> The new limit value in internal units (centimeters or radians).


        '''
        pass

    def enableLimit(self, type: MFnTransform.MFnTransform,
                        flag: bool): 
        '''
        enableLimit(self, type: MFnTransform.MFnTransform,
                        flag: bool)

        Synopsis
        -----
        Enable or disable the limit value for the specified limit type.

        Returns:
        -----
        None

        Parameters:
        -----
        type: MFnTransform.MFnTransform
        	[in] -> An enum indicating the limit to enable or disable. 

        flag: bool
        	[in] -> The enable value; true will enable while false will disable the limit.


        '''
        pass

    def validateAndSetValue(self, plug: MPlug,
                        handle: MDataHandle): 
        '''
        validateAndSetValue(self, plug: MPlug,
                        handle: MDataHandle) -> _OPENMAYA_DEPRECATION_PUSH_AND_DISABLE_WARNING MStatus

        Synopsis
        -----
        When a plug's value is set, and the plug is on a default
        transform attribute, or has been flagged by the
        mustCallValidateAndSet() method, then this method will be called.
        The purpose of validateAndSetValue() is to enforce limits,
        constraints, or plug value locking.If the plug passed into this
        method is not an attribute related to the derived class, the
        derived class should call the validateAndSetValue method of its
        parent class in order to allow the base classes to handle their
        attributes.If any adjustments or corrections are required, they
        are placed in the data block and if the context is normal, into
        the cached transformation matrix. Values on the data block are in
        transform space.Formerly the context was passed in; now the
        context will already be set as the current one for evaluation so
        it isn't necessary. To retrieve the current evaluation context,
        call MDGContext::current.If you have specialty code that calls
        this method directly you'll have to ensure the current context is
        set using MDGContextGuard or MDGContext::makeCurrent.

        Returns: 
        ----- 
        Status code.

        Parameters:
        -----
        plug: MPlug
        	[in] -> The plug that is to be set. 

        handle: MDataHandle
        	[in] -> The inputValue handle of the data.


        '''
        pass

    def getMatrix(self, ReturnStatus: MPxTransform.MStatus): 
        '''
        getMatrix(self, ReturnStatus: MPxTransform.MStatus) -> MMatrix

        Synopsis
        -----
        This method returns a 4x4 matrix that is produced by applying all
        of the components of the transform.

        Returns: 
        ----- 
        The transform as a MMatrix.

        Parameters:
        -----
        ReturnStatus: MPxTransform.MStatus
        	[out] -> Return status.


        '''
        pass

    def getMatrixInverse(self, ReturnStatus: MPxTransform.MStatus): 
        '''
        getMatrixInverse(self, ReturnStatus: MPxTransform.MStatus) -> MMatrix

        Synopsis
        -----
        This method returns the inverse of the 4x4 matrix that describes
        this transformation in the current evaluation context.

        Returns: 
        ----- 
        The inverse of the transform as a MMatrix.

        Parameters:
        -----
        ReturnStatus: MPxTransform.MStatus
        	[out] -> Return status.


        '''
        pass

    def getTranslation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransform.MStatus): 
        '''
        getTranslation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransform.MStatus) -> MVector

        Synopsis
        -----
        This method returns the translation component of the transform as
        a MVector in internal units (centimeters).

        Returns: 
        ----- 
        The translation MVector in internal units (centimeters).

        Parameters:
        -----
        space: MSpace.MSpace
        	[in] -> The space used for setting the translation. 

        ReturnStatus: MPxTransform.MStatus
        	[out] -> Return status.


        '''
        pass

    def translateTo(self, newTrans: MVector,
                        space: MSpace.MSpace): 
        '''
        translateTo(self, newTrans: MVector,
                        space: MSpace.MSpace)

        Synopsis
        -----
        Set the translation component of the transform in centimeters.

        Returns:
        -----
        None

        Parameters:
        -----
        newTrans: MVector
        	[in] -> The new translation component in centimeters. 

        space: MSpace.MSpace
        	[in] -> The space in which to perform the translation.


        '''
        pass

    def translateBy(self, transOffset: MVector,
                        space: MSpace.MSpace): 
        '''
        translateBy(self, transOffset: MVector,
                        space: MSpace.MSpace)

        Synopsis
        -----
        Add to the translation component by translating relative to the
        existing transform. The transform value should be in internal
        units (centimeters).

        Returns:
        -----
        None

        Parameters:
        -----
        transOffset: MVector
        	[in] -> The relative translation value in centimeters. 

        space: MSpace.MSpace
        	[in] -> The space in which to perform the translation.


        '''
        pass

    def getRotation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransform.MStatus): 
        '''
        getRotation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransform.MStatus) -> MQuaternion

        Synopsis
        -----
        This method returns the rotation of the transform as a
        quaternion. The rotation is returned in MSpace::kTransform space.
        If an invalid space is used, MQuaternion::identity will be
        returned.

        Returns: 
        ----- 
        The rotate component of the transform as a quaternion.

        Parameters:
        -----
        space: MSpace.MSpace
        	[in] -> The space used for getting the rotate value. 

        ReturnStatus: MPxTransform.MStatus
        	[out] -> Return status.


        '''
        pass

    def getEulerRotation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransform.MStatus): 
        '''
        getEulerRotation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransform.MStatus) -> MEulerRotation

        Synopsis
        -----
        Returns the rotation component of the transform as a euler
        rotation. The rotation is returned in MSpace::kTransform space.
        If an invalid space is used, MEulerRotation::identity will be
        returned.

        Returns: 
        ----- 
        The rotation component of the transform as an euler rotation.

        Parameters:
        -----
        space: MSpace.MSpace
        	[in] -> The space used for getting the rotation. 

        ReturnStatus: MPxTransform.MStatus
        	[out] -> Return status.


        '''
        pass

    @overload
    def rotateTo(self, newRot: MQuaternion,
                        space: MSpace.MSpace): 
        '''
        rotateTo(self, newRot: MQuaternion,
                        space: MSpace.MSpace)

        Synopsis
        -----
        Sets the rotation component of the transform using a quaternion.
        The rotation is performed in MSpace::kTransform space. The
        transform's existing order of rotation is preserved.

        Returns:
        -----
        None

        Parameters:
        -----
        newRot: MQuaternion
        	[in] -> The new rotation value as a quaternion. 

        space: MSpace.MSpace
        	[in] -> The space of the passed rotation value.


        '''
        pass

    @overload
    def rotateBy(self, rotateOffset: MQuaternion,
                        space: MSpace.MSpace): 
        '''
        rotateBy(self, rotateOffset: MQuaternion,
                        space: MSpace.MSpace)

        Synopsis
        -----
        Adds to the rotation component of the transform by rotating
        relative to the existing transformation using a quaternion. The
        only valid transformation spaces for this method are
        MSpace::kTransform and MSpace::kPreTransform. All other spaces
        are treated as being equivalent to MSpace::kTransform. The
        transform's existing order of rotation is preserved.

        Returns:
        -----
        None

        Parameters:
        -----
        rotateOffset: MQuaternion
        	[in] -> The relative rotation to apply to the transform. 

        space: MSpace.MSpace
        	[in] -> The space of the passed rotation.


        '''
        pass

    @overload
    def rotateTo(self, euler: MEulerRotation,
                        space: MSpace.MSpace): 
        '''
        rotateTo(self, euler: MEulerRotation,
                        space: MSpace.MSpace)

        Synopsis
        -----
        Sets the rotation component of the transform using an euler
        rotation. If the new rotation's order of rotation is different
        from that of the transform it will be reordered to match the
        transform.

        Returns:
        -----
        None

        Parameters:
        -----
        euler: MEulerRotation
        	[in] -> The new rotation value as an euler rotation. 

        space: MSpace.MSpace
        	[in] -> The space of the passed rotation value.


        '''
        pass

    @overload
    def rotateBy(self, euler: MEulerRotation,
                        space: MSpace.MSpace): 
        '''
        rotateBy(self, euler: MEulerRotation,
                        space: MSpace.MSpace)

        Synopsis
        -----
        Adds to the rotation component of the transform by rotating
        relative to the existing transform using a euler rotation. The
        only valid transformation spaces for this method are
        MSpace::kTransform and MSpace::kPreTransform/MSpace::kObject. All
        other spaces are treated as being equivalent to
        MSpace::kTransform. If the supplied rotation's order of rotation
        is different from that of the transform, it will be reordered to
        match the transform before being added in.

        Returns:
        -----
        None

        Parameters:
        -----
        euler: MEulerRotation
        	[in] -> The rotation value of the relative euler rotation. 

        space: MSpace.MSpace
        	[in] -> The space used for the relative rotation.


        '''
        pass

    def getScale(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransform.MStatus): 
        '''
        getScale(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransform.MStatus) -> MVector

        Synopsis
        -----
        Returns the scale component of the transform. If the space is
        invalid a <1.0, 1.0, 1.0> vector is returned.

        Returns: 
        ----- 
        A MVector holding the x, y, and z scale components

        Parameters:
        -----
        space: MSpace.MSpace
        	[in] -> The space used to get the scale. 

        ReturnStatus: MPxTransform.MStatus
        	[out] -> The return status.


        '''
        pass

    def scaleTo(self, newScale: MVector,
                        space: MSpace.MSpace): 
        '''
        scaleTo(self, newScale: MVector,
                        space: MSpace.MSpace)

        Synopsis
        -----
        This method will set the scale of the transform to the passed
        value.

        Returns:
        -----
        None

        Parameters:
        -----
        newScale: MVector
        	[in] -> A 

        space: MSpace.MSpace
        	[in] -> The space of the passed scale value.


        '''
        pass

    def scaleBy(self, scaleOffset: MVector,
                        space: MSpace.MSpace): 
        '''
        scaleBy(self, scaleOffset: MVector,
                        space: MSpace.MSpace)

        Synopsis
        -----
        This method will apply a relative scale to an existing scale.

        Returns:
        -----
        None

        Parameters:
        -----
        scaleOffset: MVector
        	[in] -> A 

        space: MSpace.MSpace
        	[in] -> The space of the passed scale values.


        '''
        pass

    def getShear(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransform.MStatus): 
        '''
        getShear(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransform.MStatus) -> MVector

        Synopsis
        -----
        Get the shear value for this transform.

        Returns: 
        ----- 
        A MVector holding the xy, xz, yz values of shear.

        Parameters:
        -----
        space: MSpace.MSpace
        	[in] -> The space used for retrieving the shear value. 

        ReturnStatus: MPxTransform.MStatus
        	[out] -> Return status.


        '''
        pass

    def shearTo(self, newShear: MVector,
                        space: MSpace.MSpace): 
        '''
        shearTo(self, newShear: MVector,
                        space: MSpace.MSpace)

        Synopsis
        -----
        The method sets the shear component of the transform.

        Returns:
        -----
        None

        Parameters:
        -----
        newShear: MVector
        	[in] -> A 

        space: MSpace.MSpace
        	[in] -> The space of the passed shear value.


        '''
        pass

    def shearBy(self, shearOffset: MVector,
                        space: MSpace.MSpace): 
        '''
        shearBy(self, shearOffset: MVector,
                        space: MSpace.MSpace)

        Synopsis
        -----
        This method will apply a relative shear to the existing shear.

        Returns:
        -----
        None

        Parameters:
        -----
        shearOffset: MVector
        	[in] -> The relative shear value as a 

        space: MSpace.MSpace
        	[in] -> The space of the passed shear value.


        '''
        pass

    def getScalePivot(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransform.MStatus): 
        '''
        getScalePivot(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransform.MStatus) -> MPoint

        Synopsis
        -----
        This method returns the position of the pivot used by the scale
        component of the transform. The position is represented in
        internal units (centimeters).

        Returns: 
        ----- 
        A MPoint given the position of the scale pivot in centimeters.

        Parameters:
        -----
        space: MSpace.MSpace
        	[in] -> The space used to get the scale pivot. 

        ReturnStatus: MPxTransform.MStatus
        	[out] -> Return status.


        '''
        pass

    def getRotatePivot(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransform.MStatus): 
        '''
        getRotatePivot(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransform.MStatus) -> MPoint

        Synopsis
        -----
        This method returns the position of the pivot used by the rotate
        component of the transform. The position is represented in
        internal units (centimeters).

        Returns: 
        ----- 
        A MPoint given the position of the rotate pivot in centimeters.

        Parameters:
        -----
        space: MSpace.MSpace
        	[in] -> The space used to get the rotate pivot. 

        ReturnStatus: MPxTransform.MStatus
        	[out] -> Status code.


        '''
        pass

    def getScalePivotTranslation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransform.MStatus): 
        '''
        getScalePivotTranslation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransform.MStatus) -> MVector

        Synopsis
        -----
        This method returns the scale pivot translation in internal units
        (centimeters). The scale pivot translation is an offset applied
        to the transform to allow adjustments to the scale pivot to be
        made without changing the overall transform.

        Returns: 
        ----- 
        An MVector containing the value of the scale pivot translation in
        centimeters.

        Parameters:
        -----
        space: MSpace.MSpace
        	[in] -> The spaced used to get the scale pivot translation. 

        ReturnStatus: MPxTransform.MStatus
        	[out] -> Return status.


        '''
        pass

    def getRotatePivotTranslation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransform.MStatus): 
        '''
        getRotatePivotTranslation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransform.MStatus) -> MVector

        Synopsis
        -----
        This method returns the rotate pivot translation in internal
        units (centimeters). The rotate pivot translation is an offset
        applied to the transform to allow adjustments to the rotate pivot
        to be made without changing the overall transform.

        Returns: 
        ----- 
        An MVector containing the value of the rotate pivot translation
        in centimeters.

        Parameters:
        -----
        space: MSpace.MSpace
        	[in] -> The spaced used to get the rotate pivot translation. 

        ReturnStatus: MPxTransform.MStatus
        	[out] -> Return status.


        '''
        pass

    def setScalePivot(self, newSP: MPoint,
                        space: MSpace.MSpace,
                        balance: bool): 
        '''
        setScalePivot(self, newSP: MPoint,
                        space: MSpace.MSpace,
                        balance: bool)

        Synopsis
        -----
        This method sets the position of the scale pivot. The position of
        the pivot is defined as a MPoint in internal units
        (centimeters).If the balance argument is true, then the scale
        pivot translation will be adjusted such that the overall
        transform remains unchanged after the new scale pivot is set.If
        an invalid space is used, the scale pivot will not change.

        Returns:
        -----
        None

        Parameters:
        -----
        newSP: MPoint
        	[in] -> The position of the new scale pivot. 

        space: MSpace.MSpace
        	[in] -> The space used to set the scale pivot. 

        balance: bool
        	[in] -> Should transform be rebalanced afterward?


        '''
        pass

    def setScalePivotTranslation(self, newPT: MVector,
                        space: MSpace.MSpace): 
        '''
        setScalePivotTranslation(self, newPT: MVector,
                        space: MSpace.MSpace)

        Synopsis
        -----
        This method sets the scale pivot translation in internal units
        (centimeters). The scale pivot translation is normally used to
        automatically compensate for changes in the scale pivot when the
        setScalePivot() method is used.

        Returns:
        -----
        None

        Parameters:
        -----
        newPT: MVector
        	[in] -> The scale pivot translation as a 

        space: MSpace.MSpace
        	[in] -> The space used to set the scale pivot translation.


        '''
        pass

    def setRotatePivot(self, newRP: MPoint,
                        space: MSpace.MSpace,
                        balance: bool): 
        '''
        setRotatePivot(self, newRP: MPoint,
                        space: MSpace.MSpace,
                        balance: bool)

        Synopsis
        -----
        This method sets the position of the rotate pivot. The position
        of the pivot is defined as a MPoint in internal units
        (centimeters).If the balance argument is true, then the rotate
        pivot translation will be adjusted such that the overall
        transform remains unchanged after the new rotate pivot is set.If
        an invalid space is used, the rotate pivot will not change.

        Returns:
        -----
        None

        Parameters:
        -----
        newRP: MPoint
        	[in] -> The position of the new rotate pivot. 

        space: MSpace.MSpace
        	[in] -> The space used to set the rotate pivot. 

        balance: bool
        	[in] -> Should transform be rebalanced afterward?


        '''
        pass

    def setRotatePivotTranslation(self, newPT: MVector,
                        space: MSpace.MSpace): 
        '''
        setRotatePivotTranslation(self, newPT: MVector,
                        space: MSpace.MSpace)

        Synopsis
        -----
        This method sets the rotate pivot translation in internal units
        (centimeters). The rotate pivot translation is normally used to
        automatically compensate for changes in the rotate pivot when the
        setRotatePivot() method is used.

        Returns:
        -----
        None

        Parameters:
        -----
        newPT: MVector
        	[in] -> The rotate pivot translation as a 

        space: MSpace.MSpace
        	[in] -> The space used to set the rotate pivot translation.


        '''
        pass

    def getRotationOrder(self): 
        '''
        getRotationOrder(self) -> MTransformationMatrix.MTransformationMatrix

        Synopsis
        -----
        Returns the rotation order used by the rotation component of the
        transformation matrix. Note that there are two different
        enumerations used to represent order of rotation:
        MTransformationMatrix::RotationOrder and
        MEulerRotation::RotationOrder. The actual value stored in the
        transform's rotateOrder attribute is an
        MEulerRotation::RotationOrder. The value returned by this method
        is the corresponding MTransformationMatrix::RotationOrder value.
        If you need to convert between these two rotation order
        representations use the
        MPxTransformationMatrix::convertTransformationRotationOrder and
        MPxTransformationMatrix::convertEulerRotationOrder methods.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setRotationOrder(self, ro: MTransformationMatrix.MTransformationMatrix,
                        reorder: bool): 
        '''
        setRotationOrder(self, ro: MTransformationMatrix.MTransformationMatrix,
                        reorder: bool)

        Synopsis
        -----
        Sets the rotation order used by the rotation component of the
        transformation matrix. See the getRotationOrder method for a
        discussion of the difference between
        MTransformationMatrix::RotationOrder values and
        MEulerRotation::RotationOrder values.

        Returns:
        -----
        None

        Parameters:
        -----
        ro: MTransformationMatrix.MTransformationMatrix
        	[in] -> The new rotation order as a 

        reorder: bool
        	[in] -> If true, rotations will be adjusted so that the net transformation under the new order will be the same as it was under the old order.


        '''
        pass

    def getRotateOrientation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransform.MStatus): 
        '''
        getRotateOrientation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransform.MStatus) -> MQuaternion

        Synopsis
        -----
        Returns the rotate orientation for the transformation matrix as a
        quaternion. The rotate orientation is the value associated with
        the rotateAxis attribute on this node. The rotate orientation
        value is used to orient the local rotation space of the
        transform.

        Returns: 
        ----- 
        A MQuaternion representing the rotate orientation.

        Parameters:
        -----
        space: MSpace.MSpace
        	[in] -> The space used for getting the rotate orientation. 

        ReturnStatus: MPxTransform.MStatus
        	[out] -> Return status.


        '''
        pass

    def setRotateOrientation(self, newRO: MQuaternion,
                        space: MSpace.MSpace,
                        balance: bool): 
        '''
        setRotateOrientation(self, newRO: MQuaternion,
                        space: MSpace.MSpace,
                        balance: bool)

        Synopsis
        -----
        This method sets the rotate orientation for this transform. The
        rotate orientation is used to define the local rotation space.
        The rotate orientation is the value associated with the
        rotateAxis attribute on this node.The balance argument allows the
        rotate orientation to be changed without affecting the overall
        transformation. The rotate value is adjusted to compensate for
        the change in rotate orientation.

        Returns:
        -----
        None

        Parameters:
        -----
        newRO: MQuaternion
        	[in] -> The quaternion used to set the rotate orientation. 

        space: MSpace.MSpace
        	[in] -> The space used when setting the rotate orientation. 

        balance: bool
        	[in] -> If true is used, then the rotation will change to compensate for the change in the rotate orientation.


        '''
        pass

    def getPreRotation(self): 
        '''
        getPreRotation(self) -> MQuaternion

        Synopsis
        -----
        This methods returns preRotation, which is an optional rotation
        that can be applied after the rotation channel and before the
        translation channel in the transform matrix. It is functionally
        equivalent to jointOrient and can be used to replicate joint-like
        behavior in a custom transform.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def updateMatrixAttrs(self): 
        '''
        updateMatrixAttrs(self) -> _OPENMAYA_DEPRECATION_POP_WARNING MStatus

        Synopsis
        -----
        This method is used only for the MPxTransform and MPxTransform
        derived classes. It will ensure that the values which change the
        resulting 4x4 matrix are current. It should be called before
        getting values that affect the matrix calculation.If only a
        specific value needs to be updated, then use the
        updateMatrixAttrs(MObject &attr, const MDGContext &context)
        method.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def updateMatrixAttrs(self, attr: MObject): 
        '''
        updateMatrixAttrs(self, attr: MObject)

        Synopsis
        -----
        This method ensures that a passed attribute will have its values
        current.

        Returns:
        -----
        None

        Parameters:
        -----
        attr: MObject
        	[in] -> The attribute.


        '''
        pass

    def mustCallValidateAndSet(self, obj: MObject): 
        '''
        mustCallValidateAndSet(self, obj: MObject)

        Synopsis
        -----
        This method must be called in the initialize() method for all
        attributes that affect the matrix of the transform. It will
        ensure that the matrix is properly calculated when the passed
        attribute is changed and that the validateAndSetValue method will
        get called for this attribute.It is only for MPxTransform derived
        classes.If a custom attribute on an MPxTransform derived classes
        is declared as "mustValidateAndSetValue", then the
        validateAndSetValue method must be implemented, so that it takes
        the data out of the data handle, and sets it into the datablock
        of the node.

        Returns:
        -----
        None

        Parameters:
        -----
        obj: MObject
        	[in] -> the attribute 


        '''
        pass

    def setNonAffineMatricesEnabled(self, enabled: bool): 
        '''
        setNonAffineMatricesEnabled(self, enabled: bool)

        Synopsis
        -----
        Normal Maya transforms consist of translate, rotate, scale, and
        shear. All of these transform types produce an affine matrix.
        With MPxTransform it is possible to introduce non-affine matrices
        into places that previously did not consider their effects.If
        non-affine matrices are enabled, then all calculations which
        require additional operations when handling non-affine matrices
        will perform the addition mathematical operations.This is a
        static method and will affect all transforms when enabled.

        Returns:
        -----
        None

        Parameters:
        -----
        enabled: bool
        	[in] -> If true, then non-afine calculations will be used.


        '''
        pass

    def isNonAffineMatricesEnabled(self, ReturnStatus: MPxTransform.MStatus): 
        '''
        isNonAffineMatricesEnabled(self, ReturnStatus: MPxTransform.MStatus) -> bool

        Synopsis
        -----
        This method returns true is non-affine matrix calculations are
        being used for transforms.

        Returns: 
        ----- 
        true if non-affine matrix calculations are enabled.

        Parameters:
        -----
        ReturnStatus: MPxTransform.MStatus
        	[out] -> The status


        '''
        pass

    def copyInternalData(self, node: MPxNode): 
        '''
        copyInternalData(self, node: MPxNode)

        Synopsis
        -----
        This function copies the internal data of the transform node.
        Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
        node: MPxNode
        	[in] -> the node that is being duplicated 


        '''
        pass

    def applyTranslationLimits(self, unlimitedT: MVector,
                        block: MDataBlock,
                        ReturnStatus: MPxTransform.MStatus): 
        '''
        applyTranslationLimits(self, unlimitedT: MVector,
                        block: MDataBlock,
                        ReturnStatus: MPxTransform.MStatus) -> MVector

        Synopsis
        -----
        This method returns a copy of the passed translation value with
        its members limited by any enabled translation limits on this
        node.

        Returns: 
        ----- 
        The limited translation value.

        Parameters:
        -----
        unlimitedT: MVector
        	[in] -> The value before limits are applied. 

        block: MDataBlock
        	[in] -> The datablock to use. 

        ReturnStatus: MPxTransform.MStatus
        	[out] -> Return status.


        '''
        pass

    def applyTranslationLocks(self, toTest: MVector,
                        savedT: MVector,
                        ReturnStatus: MPxTransform.MStatus): 
        '''
        applyTranslationLocks(self, toTest: MVector,
                        savedT: MVector,
                        ReturnStatus: MPxTransform.MStatus) -> MVector

        Synopsis
        -----
        This method allows the custom transform to apply its own locking
        mechanism to translation. Standard dependency graph attribute
        locking happens automatically and cannot be modified by custom
        nodes.If the plug should not be changed, then the value from the
        passed savedT argument should be return to be used in the
        transformation matrix.

        Returns: 
        ----- 
        The value after the locking checks are applied.

        Parameters:
        -----
        toTest: MVector
        	[in] -> The values to use if the plug is not locked. 

        savedT: MVector
        	[in] -> The values to revert to if the plug cannot be changed. 

        ReturnStatus: MPxTransform.MStatus
        	[out] -> status


        '''
        pass

    def applyRotationLimits(self, unlimitedR: MEulerRotation,
                        block: MDataBlock,
                        ReturnStatus: MPxTransform.MStatus): 
        '''
        applyRotationLimits(self, unlimitedR: MEulerRotation,
                        block: MDataBlock,
                        ReturnStatus: MPxTransform.MStatus) -> MEulerRotation

        Synopsis
        -----
        This method returns a copy of the passed rotation value with its
        members limited by any enabled rotation limits on this node.

        Returns: 
        ----- 
        A MEulerRotation with limits applied to it.

        Parameters:
        -----
        unlimitedR: MEulerRotation
        	[in] -> The value before applying the limits. 

        block: MDataBlock
        	[in] -> The datablock. 

        ReturnStatus: MPxTransform.MStatus
        	[out] -> Return status.


        '''
        pass

    def applyRotationLocks(self, toTest: MEulerRotation,
                        savedR: MEulerRotation,
                        ReturnStatus: MPxTransform.MStatus): 
        '''
        applyRotationLocks(self, toTest: MEulerRotation,
                        savedR: MEulerRotation,
                        ReturnStatus: MPxTransform.MStatus) -> MEulerRotation

        Synopsis
        -----
        This method allows the custom transform to apply its own locking
        mechanism to rotation. Standard dependency graph attribute
        locking happens automatically and cannot be modified by custom
        nodes.If the plug should not be changed, then the value from the
        passed savedR argument should be returned to be used in the
        transformation matrix.

        Returns: 
        ----- 
        The value after the locking checks are applied.

        Parameters:
        -----
        toTest: MEulerRotation
        	[in] -> The values to use if the plug is not locked. 

        savedR: MEulerRotation
        	[in] -> The values to revert to if the plug cannot be changed. 

        ReturnStatus: MPxTransform.MStatus
        	[in] -> status


        '''
        pass

    def applyScaleLimits(self, unlimitedS: MVector,
                        block: MDataBlock,
                        ReturnStatus: MPxTransform.MStatus): 
        '''
        applyScaleLimits(self, unlimitedS: MVector,
                        block: MDataBlock,
                        ReturnStatus: MPxTransform.MStatus) -> MVector

        Synopsis
        -----
        This method returns a copy of the passed scale value with its
        members limited by any enabled scale limits on this node.

        Returns: 
        ----- 
        The scale value with limits applied.

        Parameters:
        -----
        unlimitedS: MVector
        	[in] -> The scale before applying limits. 

        block: MDataBlock
        	[in] -> The datablock. 

        ReturnStatus: MPxTransform.MStatus
        	[out] -> Return status.


        '''
        pass

    def applyScaleLocks(self, toTest: MVector,
                        savedS: MVector,
                        ReturnStatus: MPxTransform.MStatus): 
        '''
        applyScaleLocks(self, toTest: MVector,
                        savedS: MVector,
                        ReturnStatus: MPxTransform.MStatus) -> MVector

        Synopsis
        -----
        This method allows the custom transform to apply its own locking
        mechanism to scale. Standard dependency graph attribute locking
        happens automatically and cannot be modified by custom nodes.If
        the plug should not be changed, then the value from the passed
        savedS argument should be return to be used in the transformation
        matrix.

        Returns: 
        ----- 
        The scale value after the locking checks are applied.

        Parameters:
        -----
        toTest: MVector
        	[in] -> The values to use if the plug is not locked. 

        savedS: MVector
        	[in] -> The values to revert to if the plug cannot be changed. 

        ReturnStatus: MPxTransform.MStatus
        	[out] -> status


        '''
        pass

    def applyShearLocks(self, toTest: MVector,
                        savedS: MVector,
                        ReturnStatus: MPxTransform.MStatus): 
        '''
        applyShearLocks(self, toTest: MVector,
                        savedS: MVector,
                        ReturnStatus: MPxTransform.MStatus) -> MVector

        Synopsis
        -----
        This method allows the custom transform to apply its own locking
        mechanism to shear. Standard dependency graph attribute locking
        happens automatically and cannot be modified by custom nodes.If
        the plug should not be changed, then the value from the passed
        savedS argument should be return to be used in the transformation
        matrix.

        Returns: 
        ----- 
        The shear value after the locking checks are applied.

        Parameters:
        -----
        toTest: MVector
        	[in] -> The values to use if the plug is not locked. 

        savedS: MVector
        	[in] -> The values to revert to if the plug cannot be changed. 

        ReturnStatus: MPxTransform.MStatus
        	[out] -> status


        '''
        pass

    def applyRotateOrientationLocks(self, toTest: MEulerRotation,
                        savedRO: MEulerRotation,
                        ReturnStatus: MPxTransform.MStatus): 
        '''
        applyRotateOrientationLocks(self, toTest: MEulerRotation,
                        savedRO: MEulerRotation,
                        ReturnStatus: MPxTransform.MStatus) -> MEulerRotation

        Synopsis
        -----
        This method allows the custom transform to apply its own locking
        mechanism to rotation orientation. Standard dependency graph
        attribute locking happens automatically and cannot be modified by
        custom nodes.If the plug should not be changed, then the value
        from the passed savedRO argument should be return to be used in
        the transformation matrix.

        Returns: 
        ----- 
        The rotate orientation value after the locking checks are
        applied.

        Parameters:
        -----
        toTest: MEulerRotation
        	[in] -> The values to use if the plug is not locked. 

        savedRO: MEulerRotation
        	[in] -> The values to revert to if the plug cannot be changed. 

        ReturnStatus: MPxTransform.MStatus
        	[out] -> status


        '''
        pass

    def applyScaleLocksPivot(self, toTest: MPoint,
                        savedSP: MPoint,
                        ReturnStatus: MPxTransform.MStatus): 
        '''
        applyScaleLocksPivot(self, toTest: MPoint,
                        savedSP: MPoint,
                        ReturnStatus: MPxTransform.MStatus) -> MVector

        Synopsis
        -----
        This method allows the custom transform to apply its own locking
        mechanism to scale pivot. Standard dependency graph attribute
        locking happens automatically and cannot be modified by custom
        nodes.If the plug should not be changed, then the value from the
        passed savedSP argument should be return to be used in the
        transformation matrix.

        Returns: 
        ----- 
        The scale pivot value after the locking checks are applied.

        Parameters:
        -----
        toTest: MPoint
        	[in] -> The values to use if the plug is not locked. 

        savedSP: MPoint
        	[in] -> The values to revert to if the plug cannot be changed. 

        ReturnStatus: MPxTransform.MStatus
        	[out] -> status


        '''
        pass

    def applyRotatePivotLocks(self, toTest: MPoint,
                        savedRP: MPoint,
                        ReturnStatus: MPxTransform.MStatus): 
        '''
        applyRotatePivotLocks(self, toTest: MPoint,
                        savedRP: MPoint,
                        ReturnStatus: MPxTransform.MStatus) -> MVector

        Synopsis
        -----
        This method allows the custom transform to apply its own locking
        mechanism to rotation pivots. Standard dependency graph attribute
        locking happens automatically and cannot be modified by custom
        nodes.If the plug should not be changed, then the value from the
        passed savedRP argument should be return to be used in the
        transformation matrix.

        Returns: 
        ----- 
        The value after the locking checks are applied.

        Parameters:
        -----
        toTest: MPoint
        	[in] -> The values to use if the plug is not locked. 

        savedRP: MPoint
        	[in] -> The values to revert to if the plug cannot be changed. 

        ReturnStatus: MPxTransform.MStatus
        	[out] -> status


        '''
        pass

    def applyScaleLocksPivotTranslate(self, toTest: MVector,
                        savedSPT: MVector,
                        ReturnStatus: MPxTransform.MStatus): 
        '''
        applyScaleLocksPivotTranslate(self, toTest: MVector,
                        savedSPT: MVector,
                        ReturnStatus: MPxTransform.MStatus) -> MVector

        Synopsis
        -----
        This method allows the custom transform to apply its own locking
        mechanism to the scalePivotTranslate attribute. Standard
        dependency graph attribute locking happens automatically and
        cannot be modified by custom nodes.If the plug should not be
        changed, then the value from the passed savedR argument should be
        return to be used in the transformation matrix.

        Returns: 
        ----- 
        The value after the locking checks are applied.

        Parameters:
        -----
        toTest: MVector
        	[in] -> The values to use if the plug is not locked. 

        savedSPT: MVector
        	[in] -> The values to revert to if the plug cannot be changed. 

        ReturnStatus: MPxTransform.MStatus
        	[out] -> status


        '''
        pass

    def applyRotatePivotLocksTranslate(self, toTest: MVector,
                        savedRPT: MVector,
                        ReturnStatus: MPxTransform.MStatus): 
        '''
        applyRotatePivotLocksTranslate(self, toTest: MVector,
                        savedRPT: MVector,
                        ReturnStatus: MPxTransform.MStatus) -> MVector

        Synopsis
        -----
        This method allows the custom transform to apply its own locking
        mechanism to the rotatePivotTranslate attribute. Standard
        dependency graph attribute locking happens automatically and
        cannot be modified by custom nodes.If the plug should not be
        changed, then the value from the passed savedR argument should be
        return to be used in the transformation matrix.

        Returns: 
        ----- 
        The value after the locking checks are applied.

        Parameters:
        -----
        toTest: MVector
        	[in] -> The values to use if the plug is not locked. 

        savedRPT: MVector
        	[in] -> The values to revert to if the plug cannot be changed. 

        ReturnStatus: MPxTransform.MStatus
        	[out] -> status


        '''
        pass

    def dirtyMatrix(self): 
        '''
        dirtyMatrix(self)

        Synopsis
        -----
        USE _dirtyMatrix() IN SCRIPT. This marks the entire matrix
        dirty.When a value is changed and that value should also update
        the matrix, use this method, or one of the specific dirty methods
        (i.e. dirtyTranslation())

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def checkAndSetTranslation(self, block: MDataBlock,
                        plug: MPlug,
                        newT: MVector,
                        space: MSpace.MSpace): 
        '''
        checkAndSetTranslation(self, block: MDataBlock,
                        plug: MPlug,
                        newT: MVector,
                        space: MSpace.MSpace)

        Synopsis
        -----
        This method is used to modify and set the new translate values
        being passed in from the compute method or from the
        validateAndSetValue. The data block should be set with the
        corrected values. Corrections would come from enforcing any
        active limits as well as verifying that the plug's value may be
        changed. If the plug is locked or if it is the destination in a
        connection that disallows value changes, then the plug will be
        set to its unchanged value.

        Returns:
        -----
        None

        Parameters:
        -----
        block: MDataBlock
        	[in] -> The data block to set. 

        plug: MPlug
        	[in] -> The translate plug (or one of its child plugs). 

        newT: MVector
        	[in] -> The new translate value. 

        space: MSpace.MSpace
        	[in] -> The space used for the new translation value.


        '''
        pass

    def checkAndSetRotation(self, block: MDataBlock,
                        plug: MPlug,
                        newR: MEulerRotation,
                        space: MSpace.MSpace): 
        '''
        checkAndSetRotation(self, block: MDataBlock,
                        plug: MPlug,
                        newR: MEulerRotation,
                        space: MSpace.MSpace)

        Synopsis
        -----
        This method verifies that the passed value can be set on the
        rotate plugs. In the base class, limits as well as locking are
        checked by this method.The compute, validateAndSetValue, and
        rotateTo functions all use this method.

        Returns:
        -----
        None

        Parameters:
        -----
        block: MDataBlock
        	[in] -> The data block 

        plug: MPlug
        	[in] -> The plug. This should be rotate or one of its children. 

        newR: MEulerRotation
        	[in] -> The new rotate value. 

        space: MSpace.MSpace
        	[in] -> The space that the newR value is using.


        '''
        pass

    def checkAndSetScale(self, block: MDataBlock,
                        plug: MPlug,
                        newS: MVector,
                        space: MSpace.MSpace): 
        '''
        checkAndSetScale(self, block: MDataBlock,
                        plug: MPlug,
                        newS: MVector,
                        space: MSpace.MSpace)

        Synopsis
        -----
        This method verifies that the passed value can be set on the
        scale plugs. In the base class, limits as well as locking are
        checked by this method.The compute, validateAndSetValue, and
        scaleTo functions all use this method.

        Returns:
        -----
        None

        Parameters:
        -----
        block: MDataBlock
        	[in] -> The data block 

        plug: MPlug
        	[in] -> The plug. This should be scale or one of its children. 

        newS: MVector
        	[in] -> The new scale value. 

        space: MSpace.MSpace
        	[in] -> The space that the newS value is using.


        '''
        pass

    def checkAndSetShear(self, block: MDataBlock,
                        plug: MPlug,
                        newS: MVector,
                        space: MSpace.MSpace): 
        '''
        checkAndSetShear(self, block: MDataBlock,
                        plug: MPlug,
                        newS: MVector,
                        space: MSpace.MSpace)

        Synopsis
        -----
        This method verifies that the passed value can be set on the
        shear plugs. In the base class, only the locking conditions are
        enforced.The compute, validateAndSetValue, and shearTo functions
        all use this method. If limits are desired on shear, then the
        limit enforcement should be implemented in this method in a
        derived class.

        Returns:
        -----
        None

        Parameters:
        -----
        block: MDataBlock
        	[in] -> The data block 

        plug: MPlug
        	[in] -> The plug. This should be shear or one of its children. 

        newS: MVector
        	[in] -> The new shear value. 

        space: MSpace.MSpace
        	[in] -> The space that the newS value is using.


        '''
        pass

    def checkAndSetRotateOrientation(self, block: MDataBlock,
                        plug: MPlug,
                        newRO: MEulerRotation,
                        space: MSpace.MSpace,
                        balance: bool): 
        '''
        checkAndSetRotateOrientation(self, block: MDataBlock,
                        plug: MPlug,
                        newRO: MEulerRotation,
                        space: MSpace.MSpace,
                        balance: bool)

        Synopsis
        -----
        This method verifies that the passed value can be set on the
        rotateAxis plugs. In the base class, only the locking conditions
        are enforced. This method will also update the rotation value if
        balance is true.The compute, validateAndSetValue, and
        setRotateOrientation functions all use this method. If limits are
        desired on rotateAxis, then the limit enforcement should be
        implemented in this method in a derived class.

        Returns:
        -----
        None

        Parameters:
        -----
        block: MDataBlock
        	[in] -> The data block 

        plug: MPlug
        	[in] -> The plug. This should be rotateAxis or one of its children. 

        newRO: MEulerRotation
        	[in] -> The new rotate orientation value. 

        space: MSpace.MSpace
        	[in] -> The space that the newRO value is using. 

        balance: bool
        	[in] -> If balance is true, then the rotation is modified to compensate for the change in rotateAxis such that the transform remains unchanged.


        '''
        pass

    def checkAndSetRotatePivot(self, block: MDataBlock,
                        plug: MPlug,
                        newRP: MPoint,
                        space: MSpace.MSpace,
                        balance: bool): 
        '''
        checkAndSetRotatePivot(self, block: MDataBlock,
                        plug: MPlug,
                        newRP: MPoint,
                        space: MSpace.MSpace,
                        balance: bool)

        Synopsis
        -----
        This method verifies that the passed value can be set on the
        rotatePivot plugs. In the base class, only the locking conditions
        are enforced. This method will also update the
        rotatePivotTranslate value if balance is true.The compute,
        validateAndSetValue, and setRotatePivot functions all use this
        method. If limits are desired on rotatePivot, then the limit
        enforcement should be implemented in this method in a derived
        class.

        Returns:
        -----
        None

        Parameters:
        -----
        block: MDataBlock
        	[in] -> The data block 

        plug: MPlug
        	[in] -> The plug. This should be rotatePivot or one of its children. 

        newRP: MPoint
        	[in] -> The new rotate pivot value. 

        space: MSpace.MSpace
        	[in] -> The space that the newRP value is using. 

        balance: bool
        	[in] -> If balance is true, then the rotatePivotTranslate is modified to compensate for the change in rotatePivot such that the transform remains unchanged.


        '''
        pass

    def checkAndSetRotatePivotTranslation(self, block: MDataBlock,
                        plug: MPlug,
                        newPT: MVector,
                        space: MSpace.MSpace): 
        '''
        checkAndSetRotatePivotTranslation(self, block: MDataBlock,
                        plug: MPlug,
                        newPT: MVector,
                        space: MSpace.MSpace)

        Synopsis
        -----
        This method verifies that the passed value can be set on the
        rotatePivotTranslate plugs. In the base class, only the locking
        conditions are enforced.The compute, validateAndSetValue, and
        setRotatePivotTranslation functions all use this method. If
        limits are desired on rotatePivotTranslate, then the limit
        enforcement should be implemented in this method in a derived
        class.

        Returns:
        -----
        None

        Parameters:
        -----
        block: MDataBlock
        	[in] -> The data block 

        plug: MPlug
        	[in] -> The plug. This should be rotatePivotTranslate or one of its children. 

        newPT: MVector
        	[in] -> The new rotate pivot translate value. 

        space: MSpace.MSpace
        	[in] -> The space that the newPT value is using.


        '''
        pass

    def checkAndSetScalePivot(self, block: MDataBlock,
                        plug: MPlug,
                        newSP: MPoint,
                        space: MSpace.MSpace,
                        balance: bool): 
        '''
        checkAndSetScalePivot(self, block: MDataBlock,
                        plug: MPlug,
                        newSP: MPoint,
                        space: MSpace.MSpace,
                        balance: bool)

        Synopsis
        -----
        This method verifies that the passed value can be set on the
        scalePivot plugs. In the base class, only the locking conditions
        are enforced. This method will also update the
        scalePivotTranslate value if balance is true.The compute,
        validateAndSetValue, and setScalePivot functions all use this
        method. If limits are desired on scalePivot, then the limit
        enforcement should be implemented in this method in a derived
        class.

        Returns:
        -----
        None

        Parameters:
        -----
        block: MDataBlock
        	[in] -> The data block 

        plug: MPlug
        	[in] -> The plug. This should be scalePivot or one of its children. 

        newSP: MPoint
        	[in] -> The new scale pivot value. 

        space: MSpace.MSpace
        	[in] -> The space that the newSP value is using. 

        balance: bool
        	[in] -> If balance is true, then the scalePivotTranslate is modified to compensate for the change in scalePivot such that the transform remains unchanged.


        '''
        pass

    def checkAndSetScalePivotTranslation(self, block: MDataBlock,
                        plug: MPlug,
                        newPT: MVector,
                        space: MSpace.MSpace): 
        '''
        checkAndSetScalePivotTranslation(self, block: MDataBlock,
                        plug: MPlug,
                        newPT: MVector,
                        space: MSpace.MSpace)

        Synopsis
        -----
        This method verifies that the passed value can be set on the
        scalePivotTranslate plugs. In the base class, only the locking
        conditions are enforced.The compute, validateAndSetValue, and
        setScalePivotTranslation functions all use this method. If limits
        are desired on scalePivotTranslate, then the limit enforcement
        should be implemented in this method in a derived class.

        Returns:
        -----
        None

        Parameters:
        -----
        block: MDataBlock
        	[in] -> The data block 

        plug: MPlug
        	[in] -> The plug. This should be scalePivotTranslate or one of its children. 

        newPT: MVector
        	[in] -> The new scale pivot translate value. 

        space: MSpace.MSpace
        	[in] -> The space that the newPT value is using.


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

    def thisMObject(self): 
        '''
        thisMObject(self) -> MObject

        Synopsis
        -----
        Returns the MObject associated with this user defined node. This
        makes it possible to use MFnDependencyNode or to construct plugs
        to this node's attributes.It is not necessary to override this
        method.Reimplemented from MPxNode.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def renderInfo(self): 
        '''
        renderInfo(self) -> MObject

        Synopsis
        -----
        This is obsolete. Obsolete attribute

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def identification(self): 
        '''
        identification(self) -> MObject

        Synopsis
        -----
        This is obsolete. Obsolete attribute

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def layerRenderable(self): 
        '''
        layerRenderable(self) -> MObject

        Synopsis
        -----
        This is obsolete. Obsolete attribute

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def layerOverrideColor(self): 
        '''
        layerOverrideColor(self) -> MObject

        Synopsis
        -----
        This is obsolete. Obsolete attribute

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def offsetParentMatrix(self): 
        '''
        offsetParentMatrix(self) -> MObject

        Synopsis
        -----
        Introduced in 2022.0 Offset parent matrix attribute

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MPxTransformationMatrix:
    '''Base class of all user defined transformation matrices.
MPxTransformationMatrix is the parent class for all user defined transformation
matrices. A transformation matrix is a class that holds the
individual components (i.e. translate, rotate, scale, pivots,
etc.) that are used to construct a 4x4 matrix. Given that
different combinations of transform components may produce
similar 4x4 matrices, it is not always possible to get a generic
4x4 matrix and decompose it into unique components. This class
allows better control over which components are changed than a
generic 4x4
MMatrix could offer.
The
MPxTransformationMatrix class is designed for use as the mathematical brains behind the
MPxTransform node. This separation is useful for class reuse (different types
of
MPxTransform nodes may still use the same
MPxTransformationMatrix class) as well as simplifying the
MPxTransform class.
The
MPxTransformationMatrix class is registered using the
MFnPlugin::registerTransform() method. Both the
MPxTransform and the
MPxTransformationMatrix classes are registered in the same method. This allows for a
clear association between a
MPxTransform and a
MPxTransformationMatrix.
When registering the
MPxTransformationMatrix, a
MTypeId is required. For nodes using the default
MPxTransformationMatrix, a statically defined
MTypeId is provided by the
MPxTransformationMatrix::baseTransformationMatrixId data member.
Since the
MPxTransformationMatrix class gives extended functionality to a native Maya class,
several methods are given that are needed by Maya for this class
to properly function in different settings.
To create a transformation matrix, derive from this class and
overload the
creator() method and the assignment operator for the derived class. If any
additional data items are added to this class, the
copyValues() method should also be overloaded. This will ensure that the new
values will get properly handed by Maya. The rest of the methods
may be overloaded as needed.
'''
    def __init__(self):
        pass


    def copyValues(self, xform: MPxTransformationMatrix): 
        '''
        copyValues(self, xform: MPxTransformationMatrix)

        Synopsis
        -----
        This method should be overridden for any transform that uses more
        then the default transform values. The values from the passed
        class (which should be type checked and downcast to its
        appropriate value) should be copied to this class.Without this
        method being overridden, only the default transform components
        will get copied.

        Returns:
        -----
        None

        Parameters:
        -----
        xform: MPxTransformationMatrix
        	[in] -> The user defined transformation matrix that should be copied. 


        '''
        pass

    def typeId(self): 
        '''
        typeId(self) -> MTypeId

        Synopsis
        -----
        Returns the MTypeId of this transformation matrix. The MTypeId is
        a four byte identifier that uniquely identifies this type of
        transformation matrix.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def __eq__(self, rhs: MPxTransformationMatrix): 
        '''
        __eq__(self, rhs: MPxTransformationMatrix) -> bool

        Synopsis
        -----
        Equality operator.

        Returns: 
        ----- 
        Boolean value: true if the transformation matrices are identical,
        false otherwise.

        Parameters:
        -----
        rhs: MPxTransformationMatrix
        	[in] -> The user defined transformation matrix to compare.


        '''
        pass

    @overload
    def __neq__(self, rhs: MPxTransformationMatrix): 
        '''
        __neq__(self, rhs: MPxTransformationMatrix) -> bool

        Synopsis
        -----
        Inequality operator. This method will compare the resulting 4x4
        matrices for inequality.

        Returns: 
        ----- 
        Boolean value: true The transformation matrices are not identical
        false otherwise.

        Parameters:
        -----
        rhs: MPxTransformationMatrix
        	[in] -> The user defined transformation matrix to compare.


        '''
        pass

    @overload
    def __eq__(self, rhs: MTransformationMatrix): 
        '''
        __eq__(self, rhs: MTransformationMatrix) -> bool

        Synopsis
        -----
        Equality operator. This method will compare the resulting 4x4
        matrices for equality.

        Returns: 
        ----- 
        Boolean value: true The transformation matrices are identical,
        false otherwise.

        Parameters:
        -----
        rhs: MTransformationMatrix
        	[in] -> The user defined transformation matrix to compare.


        '''
        pass

    @overload
    def __neq__(self, rhs: MTransformationMatrix): 
        '''
        __neq__(self, rhs: MTransformationMatrix) -> bool

        Synopsis
        -----
        Inequality operator. This method will compare the resulting 4x4
        matrices for inequality.

        Returns: 
        ----- 
        Boolean value: true The matrices are not identical, false
        otherwise.

        Parameters:
        -----
        rhs: MTransformationMatrix
        	[in] -> The 


        '''
        pass

    @overload
    def __eq__(self, rhs: MMatrix): 
        '''
        __eq__(self, rhs: MMatrix) -> bool

        Synopsis
        -----
        Equality operator.

        Returns: 
        ----- 
        Boolean value: true The matrices are identical, false otherwise.

        Parameters:
        -----
        rhs: MMatrix
        	[in] -> the 


        '''
        pass

    @overload
    def __neq__(self, rhs: MMatrix): 
        '''
        __neq__(self, rhs: MMatrix) -> bool

        Synopsis
        -----
        Equality operator. This method will compare the resulting 4x4
        matrices for equality.

        Returns: 
        ----- 
        Boolean value: true The matrices are not identical, false
        otherwise.

        Parameters:
        -----
        rhs: MMatrix
        	[in] -> The 


        '''
        pass

    @overload
    def isEquivalent(self, other: MPxTransformationMatrix,
                        tolerance: double): 
        '''
        isEquivalent(self, other: MPxTransformationMatrix,
                        tolerance: double) -> bool

        Synopsis
        -----
        Determine if the MPxTransformationMatrix is equivalent within a
        specified tolerance. The comparison is done with the resulting
        4x4 MMatrix and not on a component by component basis.

        Returns: 
        ----- 
        Boolean value; true The matrices are identical within the
        specified tolerance, false otherwise.

        Parameters:
        -----
        other: MPxTransformationMatrix
        	[in] -> The user defined transformation matrix to compare to. 

        tolerance: double
        	[in] -> The tolerance used in the comparison.


        '''
        pass

    @overload
    def isEquivalent(self, other: MTransformationMatrix,
                        tolerance: double): 
        '''
        isEquivalent(self, other: MTransformationMatrix,
                        tolerance: double) -> bool

        Synopsis
        -----
        Determine if the MTransformationMatrix is equivalent within a
        specified tolerance. The comparison is done with the resulting
        4x4 MMatrix and not on a component by component basis.

        Returns: 
        ----- 
        Boolean value; true The matrices are identical within the
        specified tolerance, false otherwise.

        Parameters:
        -----
        other: MTransformationMatrix
        	[in] -> The transformation matrix to compare to 

        tolerance: double
        	[in] -> The tolerance used in the comparison.


        '''
        pass

    @overload
    def isEquivalent(self, other: MMatrix,
                        tolerance: double): 
        '''
        isEquivalent(self, other: MMatrix,
                        tolerance: double) -> bool

        Synopsis
        -----
        Determine if the MMatrix is equivalent within a specified
        tolerance.

        Returns: 
        ----- 
        Boolean value; true The matrices are identical within the
        specified tolerance, false otherwise.

        Parameters:
        -----
        other: MMatrix
        	[in] -> The matrix to compare to. 

        tolerance: double
        	[in] -> The tolerance used in the comparison.


        '''
        pass

    def reverse(self): 
        '''
        reverse(self) -> MPxTransformationMatrix

        Synopsis
        -----
        Returns the negated translate, rotate, and scale without taking
        the pivots into account. This method is provided only as a
        convenience: it is not called internally by Maya.Note that the
        value returned by this method is an instance of
        MPxTransformationMatrix not an instance of your derived class. As
        such, caution must be exercised when using it with derived
        classes which provide their own data members as those members
        will not be preserved in the result.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def transformBy(self, transMat: MTransformationMatrix): 
        '''
        transformBy(self, transMat: MTransformationMatrix) -> MPxTransformationMatrix

        Synopsis
        -----
        Transforms the transformation matrix by the passed
        MTransformationMatrix. The individual components are considered
        with the exception of the pivot translations.

        Returns: 
        ----- 
        This transformation matrix.

        Parameters:
        -----
        transMat: MTransformationMatrix
        	[in] -> The transformation matrix to transform by.


        '''
        pass

    @overload
    def asMatrix(self): 
        '''
        asMatrix(self) -> MMatrix

        Synopsis
        -----
        Returns the four by four matrix that describes this
        transformation. The default matrix math is defined by:Where [Sp]
        is the scale pivot, [S] is the scale matrix, [Sh] is the shear
        matrix, [St] is the scale pivot translation, [Rp] is the rotate
        pivot, [Ro] is the rotate orientation, [R] is the rotate matrix,
        [Rt] is the rotate picot translation, and [T] is the translation.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def asMatrixInverse(self): 
        '''
        asMatrixInverse(self) -> MMatrix

        Synopsis
        -----
        Returns the inverse of the four by four matrix that describes
        this transformation. By default this is described as:Where [Sp]
        is the scale pivot, [S] is the scale matrix, [Sh] is the shear
        matrix, [St] is the scale pivot translation, [Rp] is the rotate
        pivot, [Ro] is the rotate orientation, [R] is the rotate matrix,
        [Rt] is the rotate picot translation, and [T] is the translation.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def asScaleMatrix(self): 
        '''
        asScaleMatrix(self) -> MMatrix

        Synopsis
        -----
        Returns scale matrix. The scale matrix takes points from object
        space to the space immediately following scale and shear
        transformations.For the default matrix, the scale matrix combines
        the space pivot [Sp], scale [S], shear [Sh], and scale translate
        [St] components as follows:Where [Sp] is the scale pivot, [S] is
        the scale matrix, [Sh] is the shear matrix, and [St] is the scale
        pivot translation.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def asScaleMatrixInverse(self): 
        '''
        asScaleMatrixInverse(self) -> MMatrix

        Synopsis
        -----
        Returns inverse of the scale matrix. The scale matrix takes
        points from object space to the space immediately following scale
        and shear transformations.By default this value is described by:
        Where [Sp] is the scale pivot, [S] is the scale matrix, [Sh] is
        the shear matrix, and [St] is the scale pivot translation.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def asRotateMatrix(self): 
        '''
        asRotateMatrix(self) -> MMatrix

        Synopsis
        -----
        Returns the rotate section of the transformation matrix. By
        default this is described as:Where [Rp] is the rotate pivot, [Ro]
        is the rotate orientation, [R] is the rotate matrix, and [Rt] is
        the rotate pivot translation.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def asRotateMatrixInverse(self): 
        '''
        asRotateMatrixInverse(self) -> MMatrix

        Synopsis
        -----
        Returns the inverse of the rotate matrix. By default this is
        described as:Where [Rp] is the rotate pivot, [Ro] is the rotate
        orientation, [R] is the rotate matrix, and [Rt] is the rotate
        picot translation.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def asMatrix(self, percent: double): 
        '''
        asMatrix(self, percent: double) -> MMatrix

        Synopsis
        -----
        Returns a matrix that represents the specified percentage of this
        transformation matrix. This is performed on a per-component
        basis.

        Returns: 
        ----- 
        The resulting matrix.

        Parameters:
        -----
        percent: double
        	[in] -> 


        '''
        pass

    def asInterpolationMatrix(self, toM: MTransformationMatrix,
                        percent: double,
                        rot: bool,
                        direction: int): 
        '''
        asInterpolationMatrix(self, toM: MTransformationMatrix,
                        percent: double,
                        rot: bool,
                        direction: int) -> MMatrix

        Synopsis
        -----
        Returns a matrix that represents the specified percentage of this
        transformation matrix. The two matrices involved in the
        interpolation are this transformation matrix and the passed
        transformation matrix, toMatrix.This is used by clusters.

        Returns: 
        ----- 
        The interpolated matrix.

        Parameters:
        -----
        toM: MTransformationMatrix
        	[in] -> The matrix to interpolate to. 

        percent: double
        	[in] -> The percentage of the interpolation (between 0 and 1) 

        rot: bool
        	[in] -> Should the rotation values be included? 

        direction: int
        	[in] -> The desired direction of the interpolation.


        '''
        pass

    def asTransformationMatrix(self): 
        '''
        asTransformationMatrix(self) -> MTransformationMatrix

        Synopsis
        -----
        Returns the custom transformation matrix as a standard
        MTransformationMatrix.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def translation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransformationMatrix.MStatus): 
        '''
        translation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransformationMatrix.MStatus) -> MVector

        Synopsis
        -----
        Returns the translation component of the transformation matrix as
        a MVector in centimeters (the internal Maya linear unit).

        Returns: 
        ----- 
        The translation vector in centimeters.

        Parameters:
        -----
        space: MSpace.MSpace
        	[in] -> The space to use. 

        ReturnStatus: MPxTransformationMatrix.MStatus
        	[out] -> Return status.


        '''
        pass

    def translateTo(self, t: MVector,
                        space: MSpace.MSpace): 
        '''
        translateTo(self, t: MVector,
                        space: MSpace.MSpace)

        Synopsis
        -----
        Sets the translate component of the transformation matrix in
        centimeters.

        Returns:
        -----
        None

        Parameters:
        -----
        t: MVector
        	[in] -> The new translate value in centimeters. 

        space: MSpace.MSpace
        	[in] -> The space to use.


        '''
        pass

    def translateBy(self, t: MVector,
                        space: MSpace.MSpace): 
        '''
        translateBy(self, t: MVector,
                        space: MSpace.MSpace)

        Synopsis
        -----
        Add to the translate component by translating relative to the
        existing transformation. The relative translate should be in
        centimeters.

        Returns:
        -----
        None

        Parameters:
        -----
        t: MVector
        	[in] -> The relative translate value in centimeters. 

        space: MSpace.MSpace
        	[in] -> The space to use.


        '''
        pass

    def rotation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransformationMatrix.MStatus): 
        '''
        rotation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransformationMatrix.MStatus) -> MQuaternion

        Synopsis
        -----
        Returns the rotation component of the transformation matrix as a
        quaternion. If an invalid space is used, MQuaternion::identity
        will be returned.

        Returns: 
        ----- 
        The quaternion that is the rotation component of the
        transformation matrix

        Parameters:
        -----
        space: MSpace.MSpace
        	[in] -> The space in which to get the rotation. 

        ReturnStatus: MPxTransformationMatrix.MStatus
        	[out] -> The status.


        '''
        pass

    def eulerRotation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransformationMatrix.MStatus): 
        '''
        eulerRotation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransformationMatrix.MStatus) -> MEulerRotation

        Synopsis
        -----
        Returns the rotation component of the transformation matrix as a
        euler rotation. If an invalid space is used,
        MEulerRotation::identity will be returned.

        Returns: 
        ----- 
        The euler angle that is the rotation component of the
        transformation matrix.

        Parameters:
        -----
        space: MSpace.MSpace
        	[in] -> The space in which to get the rotation. 

        ReturnStatus: MPxTransformationMatrix.MStatus
        	[out] -> Return status.


        '''
        pass

    @overload
    def rotateTo(self, quat: MQuaternion,
                        space: MSpace.MSpace): 
        '''
        rotateTo(self, quat: MQuaternion,
                        space: MSpace.MSpace)

        Synopsis
        -----
        Sets the rotation component of the transformation matrix using a
        quaternion.

        Returns:
        -----
        None

        Parameters:
        -----
        quat: MQuaternion
        	[in] -> The quaternion used to set the rotation component of the transformation matrix. 

        space: MSpace.MSpace
        	[in] -> The space to use.


        '''
        pass

    @overload
    def rotateBy(self, quat: MQuaternion,
                        space: MSpace.MSpace): 
        '''
        rotateBy(self, quat: MQuaternion,
                        space: MSpace.MSpace)

        Synopsis
        -----
        Rotates relative to the current rotation value of the
        transformation matrix. By default, the only valid transformation
        spaces for this method are MSpace::kTransform and
        MSpace::kPreTransform. All other spaces are treated as being
        equivalent to MSpace::kTransform.

        Returns:
        -----
        None

        Parameters:
        -----
        quat: MQuaternion
        	[in] -> The relative rotation as a quaternion. 

        space: MSpace.MSpace
        	[in] -> The space in which the rotation is performed.


        '''
        pass

    @overload
    def rotateTo(self, euler: MEulerRotation,
                        space: MSpace.MSpace): 
        '''
        rotateTo(self, euler: MEulerRotation,
                        space: MSpace.MSpace)

        Synopsis
        -----
        Sets the rotation component of the transformation matrix using an
        euler rotation.

        Returns:
        -----
        None

        Parameters:
        -----
        euler: MEulerRotation
        	[in] -> The euler rotation used to set the transformation matrix. 

        space: MSpace.MSpace
        	[in] -> The space used to set the rotation.


        '''
        pass

    @overload
    def rotateBy(self, euler: MEulerRotation,
                        space: MSpace.MSpace): 
        '''
        rotateBy(self, euler: MEulerRotation,
                        space: MSpace.MSpace)

        Synopsis
        -----
        Rotates relative to the current rotation value of the
        transformation matrix. By default, the only valid transformation
        spaces for this method are MSpace::kTransform and
        MSpace::kPreTransform. All other spaces are treated as being
        equivalent to MSpace::kTransform.

        Returns:
        -----
        None

        Parameters:
        -----
        euler: MEulerRotation
        	[in] -> The relative rotation as an euler angle. 

        space: MSpace.MSpace
        	[in] -> The space in which the rotation is performed.


        '''
        pass

    def rotationOrder(self, ReturnStatus: MPxTransformationMatrix.MStatus): 
        '''
        rotationOrder(self, ReturnStatus: MPxTransformationMatrix.MStatus) -> MTransformationMatrix.MTransformationMatrix

        Synopsis
        -----
        Returns the rotation order used by the rotation component of the
        transformation matrix.

        Returns: 
        ----- 
        The rotation order use by the rotation component of the
        transformation matrix.

        Parameters:
        -----
        ReturnStatus: MPxTransformationMatrix.MStatus
        	[out] -> Return status.


        '''
        pass

    def setRotationOrder(self, rotOrder: MTransformationMatrix.MTransformationMatrix,
                        preserve: bool): 
        '''
        setRotationOrder(self, rotOrder: MTransformationMatrix.MTransformationMatrix,
                        preserve: bool)

        Synopsis
        -----
        Sets the rotation order used by the rotation component of the
        transformation matrix.

        Returns:
        -----
        None

        Parameters:
        -----
        rotOrder: MTransformationMatrix.MTransformationMatrix
        	[in] -> The rotation order to use 

        preserve: bool
        	[in] -> If true then the values will change to preserve the rotation.


        '''
        pass

    def rotateOrientation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransformationMatrix.MStatus): 
        '''
        rotateOrientation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransformationMatrix.MStatus) -> MQuaternion

        Synopsis
        -----
        Returns the rotate orientation for the transformation matrix as a
        quaternion. The rotate orientation orients the local rotation
        space.

        Returns: 
        ----- 
        The rotate orientation.

        Parameters:
        -----
        space: MSpace.MSpace
        	[in] -> The space to use. 

        ReturnStatus: MPxTransformationMatrix.MStatus
        	[out] -> The return status.


        '''
        pass

    @overload
    def setRotateOrientation(self, q: MQuaternion,
                        space: MSpace.MSpace,
                        balance: bool): 
        '''
        setRotateOrientation(self, q: MQuaternion,
                        space: MSpace.MSpace,
                        balance: bool)

        Synopsis
        -----
        Sets the rotate orientation for the transformation matrix to the
        passed quaternion. The rotate orientation is the rotation that
        orients the local rotation space.

        Returns:
        -----
        None

        Parameters:
        -----
        q: MQuaternion
        	[in] -> The rotate orientation. 

        space: MSpace.MSpace
        	[in] -> The space to use. 

        balance: bool
        	[in] -> If true, the overall rotation will be preserved by altering the rotation to compensate for the change in rotate orientation.


        '''
        pass

    def eulerRotateOrientation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransformationMatrix.MStatus): 
        '''
        eulerRotateOrientation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransformationMatrix.MStatus) -> MEulerRotation

        Synopsis
        -----
        Returns the rotate orientation for the transformation matrix as
        an euler rotation. The rotate orientation orients the local
        rotation space.

        Returns: 
        ----- 
        The rotate orientation as an euler angle.

        Parameters:
        -----
        space: MSpace.MSpace
        	[in] -> The space to use. 

        ReturnStatus: MPxTransformationMatrix.MStatus
        	[out] -> Return status.


        '''
        pass

    @overload
    def setRotateOrientation(self, euler: MEulerRotation,
                        space: MSpace.MSpace,
                        balance: bool): 
        '''
        setRotateOrientation(self, euler: MEulerRotation,
                        space: MSpace.MSpace,
                        balance: bool)

        Synopsis
        -----
        Sets the rotate orientation for the transformation matrix to the
        passed euler rotation. The rotate orientation is the rotation
        that orients the local rotation space.

        Returns:
        -----
        None

        Parameters:
        -----
        euler: MEulerRotation
        	[in] -> The rotate orientation. 

        space: MSpace.MSpace
        	[in] -> The space to use. 

        balance: bool
        	[in] -> If true, the overall rotation will be preserved by altering the rotation to compensate for the change in rotate orientation.


        '''
        pass

    def preRotation(self): 
        '''
        preRotation(self) -> MQuaternion

        Synopsis
        -----
        This methods returns preRotation, which is an optional rotation
        that can be applied after the rotation channel and before the
        translation channel in the transform matrix. It is functionally
        equivalent to jointOrient and can be used to replicate joint-like
        behavior in a custom transform.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def scale(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransformationMatrix.MStatus): 
        '''
        scale(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransformationMatrix.MStatus) -> MVector

        Synopsis
        -----
        Returns the scale component of the transformation matrix. If the
        space is invalid a MVector with all of its components being 1.0
        is returned.Only the scale is returned, without the scale pivot,
        scale pivot translate, or shear values applied.

        Returns: 
        ----- 
        Vector holding the x, y, and z scale components

        Parameters:
        -----
        space: MSpace.MSpace
        	[in] -> transform space in which to get the scale 

        ReturnStatus: MPxTransformationMatrix.MStatus
        	[out] -> return status


        '''
        pass

    def scaleTo(self, newScale: MVector,
                        space: MSpace.MSpace): 
        '''
        scaleTo(self, newScale: MVector,
                        space: MSpace.MSpace)

        Synopsis
        -----
        Set the scale component of the transformation matrix. If an
        invalid space is passed, the scale will not be changed.

        Returns:
        -----
        None

        Parameters:
        -----
        newScale: MVector
        	[in] -> A vector holding the scale components. 

        space: MSpace.MSpace
        	[in] -> The space in which to perform the scale.


        '''
        pass

    def scaleBy(self, scaleFactor: MVector,
                        space: MSpace.MSpace): 
        '''
        scaleBy(self, scaleFactor: MVector,
                        space: MSpace.MSpace)

        Synopsis
        -----
        Apply a relative scale to the existing scale.

        Returns:
        -----
        None

        Parameters:
        -----
        scaleFactor: MVector
        	[in] -> A 

        space: MSpace.MSpace
        	[in] -> The space in which to perform the scale.


        '''
        pass

    def shear(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransformationMatrix.MStatus): 
        '''
        shear(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransformationMatrix.MStatus) -> MVector

        Synopsis
        -----
        Returns the shear component of the transformation matrix.

        Returns: 
        ----- 
        A MVector holding the xy, xz, yz values of shear.

        Parameters:
        -----
        space: MSpace.MSpace
        	[in] -> The space to use. 

        ReturnStatus: MPxTransformationMatrix.MStatus
        	[out] -> Return status.


        '''
        pass

    def shearTo(self, newShear: MVector,
                        space: MSpace.MSpace): 
        '''
        shearTo(self, newShear: MVector,
                        space: MSpace.MSpace)

        Synopsis
        -----
        Sets the shear component of the transformation matrix.

        Returns:
        -----
        None

        Parameters:
        -----
        newShear: MVector
        	[in] -> The new shear value. 

        space: MSpace.MSpace
        	[in] -> The space to use for setting the shear.


        '''
        pass

    def shearBy(self, shearOffset: MVector,
                        space: MSpace.MSpace): 
        '''
        shearBy(self, shearOffset: MVector,
                        space: MSpace.MSpace)

        Synopsis
        -----
        Apply a new shear to the existing shear component of the
        transformation matrix. The shear values are added by multiplying
        the individual shear components with the offset values.

        Returns:
        -----
        None

        Parameters:
        -----
        shearOffset: MVector
        	[in] -> The relative shear value. 

        space: MSpace.MSpace
        	[in] -> The space to use.


        '''
        pass

    def scalePivot(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransformationMatrix.MStatus): 
        '''
        scalePivot(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransformationMatrix.MStatus) -> MPoint

        Synopsis
        -----
        Returns the pivot used by the scale. The value is in centimeters.

        Returns: 
        ----- 
        The scale pivot point.

        Parameters:
        -----
        space: MSpace.MSpace
        	[in] -> The space to use. 

        ReturnStatus: MPxTransformationMatrix.MStatus
        	[out] -> Return status.


        '''
        pass

    def setScalePivot(self, scalePivot: MPoint,
                        space: MSpace.MSpace,
                        balance: bool): 
        '''
        setScalePivot(self, scalePivot: MPoint,
                        space: MSpace.MSpace,
                        balance: bool)

        Synopsis
        -----
        Set the pivot used by the scale. If balance if true, then the
        overall transformation matrix will not change and a compensating
        translation will be added to the scale pivot transformation to
        achieve this.If an invalid space is used, the scale pivot will
        not change.

        Returns:
        -----
        None

        Parameters:
        -----
        scalePivot: MPoint
        	[in] -> The new scale pivot value. 

        space: MSpace.MSpace
        	[in] -> The space to use. 

        balance: bool
        	[in] -> Set true is the overall transform should remain unchanged after setting the new scale pivot value.


        '''
        pass

    def scalePivotTranslation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransformationMatrix.MStatus): 
        '''
        scalePivotTranslation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransformationMatrix.MStatus) -> MVector

        Synopsis
        -----
        Returns the scale pivot translation, which is used to compensate
        for changes of the scale pivot.

        Returns: 
        ----- 
        The scale pivot translation.

        Parameters:
        -----
        space: MSpace.MSpace
        	[in] -> The space to use. 

        ReturnStatus: MPxTransformationMatrix.MStatus
        	[out] -> Return status.


        '''
        pass

    def setScalePivotTranslation(self, v: MVector,
                        space: MSpace.MSpace): 
        '''
        setScalePivotTranslation(self, v: MVector,
                        space: MSpace.MSpace)

        Synopsis
        -----
        Set the scale pivot translation. When the scale pivot is changed,
        there is an option to automatically compensate for the change so
        that the overall transformation is not altered. The compensating
        factor is the scale pivot translation.This method will manually
        change the scale pivot translation.

        Returns:
        -----
        None

        Parameters:
        -----
        v: MVector
        	[in] -> The new scale pivot translation. 

        space: MSpace.MSpace
        	[in] -> The space to use.


        '''
        pass

    def rotatePivot(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransformationMatrix.MStatus): 
        '''
        rotatePivot(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransformationMatrix.MStatus) -> MPoint

        Synopsis
        -----
        Returns the pivot used by the rotation.

        Returns: 
        ----- 
        The rotation pivot point.

        Parameters:
        -----
        space: MSpace.MSpace
        	[in] -> The space to use. 

        ReturnStatus: MPxTransformationMatrix.MStatus
        	[out] -> Return status.


        '''
        pass

    def setRotatePivot(self, rotatePivot: MPoint,
                        space: MSpace.MSpace,
                        balance: bool): 
        '''
        setRotatePivot(self, rotatePivot: MPoint,
                        space: MSpace.MSpace,
                        balance: bool)

        Synopsis
        -----
        Set the pivot used by the rotation. If balance if true, then the
        overall transformation will not change and a compensating
        translation will be added to the rotation transformation to
        achieve this.For the default case, the balance calculation is as
        follows:

        Returns:
        -----
        None

        Parameters:
        -----
        rotatePivot: MPoint
        	[in] -> The new rotate pivot. 

        space: MSpace.MSpace
        	[in] -> The space to use. 

        balance: bool
        	[in] -> Set true is the overall transform should remain unchanged after setting the new rotate pivot value.


        '''
        pass

    def rotatePivotTranslation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransformationMatrix.MStatus): 
        '''
        rotatePivotTranslation(self, space: MSpace.MSpace,
                        ReturnStatus: MPxTransformationMatrix.MStatus) -> MVector

        Synopsis
        -----
        Returns the rotate pivot translation, which is used to compensate
        for changes of the rotate pivot.

        Returns: 
        ----- 
        The rotate pivot translation.

        Parameters:
        -----
        space: MSpace.MSpace
        	[in] -> The space to use. 

        ReturnStatus: MPxTransformationMatrix.MStatus
        	[out] -> Return status.


        '''
        pass

    def setRotatePivotTranslation(self, v: MVector,
                        space: MSpace.MSpace): 
        '''
        setRotatePivotTranslation(self, v: MVector,
                        space: MSpace.MSpace)

        Synopsis
        -----
        Set the rotate pivot translation. When the scale pivot is
        changed, there is an option to automatically compensate for the
        change so that the overall transformation is not altered. The
        compensating factor is the rotate pivot translation.See the
        documentation for setRotatePivot for an explanation of the
        compensating calculation.

        Returns:
        -----
        None

        Parameters:
        -----
        v: MVector
        	[in] -> The new rotate pivot translation. 

        space: MSpace.MSpace
        	[in] -> The space to use.


        '''
        pass

    def unSquishIt(self): 
        '''
        unSquishIt(self)

        Synopsis
        -----
        Remove any shearing and any non-proportional scaling from this
        transform. If the scaling is non-proportional, then the maximum
        scale of the three scale axes will be used on all of the scale
        axes.If new scaling or shearing types are added to a derived
        class, this method should be overloaded.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def unSquishMatrix(self): 
        '''
        unSquishMatrix(self) -> MMatrix

        Synopsis
        -----
        Remove any shearing and any non-proportional scaling. If the
        scaling is non-proportional, then the maximum scale of the three
        scale axes will be used on all of the scale axes. The method
        creates a new 4x4 MMatrix and leaves this transformation matrix
        unchanged.If new scaling or shearing types are added to a derived
        class, this method should be overloaded.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def convertTransformationRotationOrder(self, xformOrder: MTransformationMatrix.MTransformationMatrix,
                        ReturnStatus: MPxTransformationMatrix.MStatus): 
        '''
        convertTransformationRotationOrder(self, xformOrder: MTransformationMatrix.MTransformationMatrix,
                        ReturnStatus: MPxTransformationMatrix.MStatus) -> MEulerRotation.MEulerRotation

        Synopsis
        -----
        Convert from MTransformationMatrix::RotationOrder to
        MEulerRotation::RotationOrder. If MTransformationMatrix::kLast or
        MTransformationMatrix::kInvalid is passed in,
        MEulerRotation::kXYZ will be returned along with a
        kInvalidParameter return status.

        Returns: 
        ----- 
        The corresponding MEulerRotation::RotationOrder.

        Parameters:
        -----
        xformOrder: MTransformationMatrix.MTransformationMatrix
        	[in] -> The 

        ReturnStatus: MPxTransformationMatrix.MStatus
        	[out] -> return status


        '''
        pass

    def convertEulerRotationOrder(self, eulerOrder: MEulerRotation.MEulerRotation,
                        ReturnStatus: MPxTransformationMatrix.MStatus): 
        '''
        convertEulerRotationOrder(self, eulerOrder: MEulerRotation.MEulerRotation,
                        ReturnStatus: MPxTransformationMatrix.MStatus) -> MTransformationMatrix.MTransformationMatrix

        Synopsis
        -----
        Convert from MEulerRotation::RotationOrder to
        MTransformationMatrix::RotationOrder.

        Returns: 
        ----- 
        The corresponding MTransformationMatrix::RotationOrder.

        Parameters:
        -----
        eulerOrder: MEulerRotation.MEulerRotation
        	[in] -> The 

        ReturnStatus: MPxTransformationMatrix.MStatus
        	[out] -> return status


        '''
        pass

    def decomposeMatrix(self, m: MMatrix): 
        '''
        decomposeMatrix(self, m: MMatrix)

        Synopsis
        -----
        This method converts a passed MMatrix into individual
        transformation matrix components. The default algorithm will
        solve under the assumption that the pivots and pivot translates
        are all zero.It is possible that multiple transformation matrices
        may produce identical 4x4 matrices. This means that taking a
        generic transformation matrix and converting it to a MMatrix and
        back to a transformation matrix may have different components,
        but the net transformation will still be the same.

        Returns:
        -----
        None

        Parameters:
        -----
        m: MMatrix
        	[in] -> The matrix to break up into components.


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

class MPxUIControl:
    '''Base class for control creation.
MPxUIControl is the base class for user defined UI. This class should never
be extended. Extend the derived classes of this class.
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

class MPxUITableControl:
    '''Base class for creating new spreadsheet controls.
MPxUITableControl is the base class for creating new spreadsheet like interfaces.
Every UI control has an associated command that is 'in-charge' of
that control. Therefore, when creating a new table control, you
will need to create an associated
MPxControlCommand. Please refer to the
MPxControlCommand documentation for details on how to use these class together.
At a minimum, when creating a new table control, you must
overload getCell( ... ). Other methods available for overloading
are getLabel(...), allowEdit( ... ), allowSelection( ... ), and
collapseOrExpandRow( ... ).
'''
    def __init__(self):
        pass


    def redrawLabels(self, labelType: MPxUITableControl.MPxUITableControl): 
        '''
        redrawLabels(self, labelType: MPxUITableControl.MPxUITableControl)

        Synopsis
        -----
        Tells the table control to redraw the label entries.

        Returns:
        -----
        None

        Parameters:
        -----
        labelType: MPxUITableControl.MPxUITableControl
        	[in] -> Specifies which labels to redraw.


        '''
        pass

    def redrawCells(self): 
        '''
        redrawCells(self)

        Synopsis
        -----
        Tells the UI control to redraw the cells of the table. The table
        control maintains a database of cell entries and it will populate
        these entries using getCell interface.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def addToSelection(self, row: int,
                        col: int): 
        '''
        addToSelection(self, row: int,
                        col: int)

        Synopsis
        -----
        Add the follow cell to the selection data structure. To keep
        track of which entries that should be highlighted, an internal
        table is maintained.

        Returns:
        -----
        None

        Parameters:
        -----
        row: int
        	[in] -> table row entry. 

        col: int
        	[in] -> table col entry.


        '''
        pass

    def removeFromSelection(self, row: int,
                        column: int): 
        '''
        removeFromSelection(self, row: int,
                        column: int)

        Synopsis
        -----
        Removes the specified cell entry from the internal selection
        list.

        Returns:
        -----
        None

        Parameters:
        -----
        row: int
        	[in] -> cell row entry 

        column: int
        	[in] -> cell column entry


        '''
        pass

    def clearSelection(self): 
        '''
        clearSelection(self)

        Synopsis
        -----
        Clears the selection table. This will remove all highlighted
        cells from the table.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def setSelection(self, row: int,
                        column: int): 
        '''
        setSelection(self, row: int,
                        column: int)

        Synopsis
        -----
        Sets the table selection list based on the row & column entry.
        This replaces the current selection list with the new entry.

        Returns:
        -----
        None

        Parameters:
        -----
        row: int
        	[in] -> cell row entry 

        column: int
        	[in] -> cell column entry


        '''
        pass

    @overload
    def setSelection(self, firstRow: int,
                        lastRow: int,
                        firstCol: int,
                        lastCol: int): 
        '''
        setSelection(self, firstRow: int,
                        lastRow: int,
                        firstCol: int,
                        lastCol: int)

        Synopsis
        -----
        Sets the selection to be the range of cells specified. This
        replaces the current selection with the specified selection
        range.

        Returns:
        -----
        None

        Parameters:
        -----
        firstRow: int
        	[in] -> first row of the selection 

        lastRow: int
        	[in] -> last row of the selection 

        firstCol: int
        	[in] -> first column of the selection 

        lastCol: int
        	[in] -> last column of the selection


        '''
        pass

    def setNumberOfRows(self, count: int): 
        '''
        setNumberOfRows(self, count: int)

        Synopsis
        -----
        Specifies the number of rows for the table.

        Returns:
        -----
        None

        Parameters:
        -----
        count: int
        	[in] -> number of rows desired.


        '''
        pass

    def numberOfRows(self, ReturnStatus: MPxUITableControl.MStatus): 
        '''
        numberOfRows(self, ReturnStatus: MPxUITableControl.MStatus) -> int

        Synopsis
        -----
        Returns the number of rows in the table.

        Returns: 
        ----- 
        Number of rows in the table or zero on failure.

        Parameters:
        -----
        ReturnStatus: MPxUITableControl.MStatus
        	[out] -> Status of the call.


        '''
        pass

    def setNumberOfColumns(self, count: int): 
        '''
        setNumberOfColumns(self, count: int)

        Synopsis
        -----
        Specifies the number of columns for the table.

        Returns:
        -----
        None

        Parameters:
        -----
        count: int
        	[in] -> number of columns desired.


        '''
        pass

    def numberOfColumns(self, ReturnStatus: MPxUITableControl.MStatus): 
        '''
        numberOfColumns(self, ReturnStatus: MPxUITableControl.MStatus) -> int

        Synopsis
        -----
        Returns the number of columns in the table.

        Returns: 
        ----- 
        MS::kSuccess Successfully returned the number of rows.
        MS::kFailure Internal error.

        Parameters:
        -----
        ReturnStatus: MPxUITableControl.MStatus
        	[out] -> status of the call.


        '''
        pass

    def suspendUpdates(self, update: bool,
                        ReturnStatus: MPxUITableControl.MStatus): 
        '''
        suspendUpdates(self, update: bool,
                        ReturnStatus: MPxUITableControl.MStatus) -> bool

        Synopsis
        -----
        When set to true, it prevents the UI from updating the table. The
        old suspend status is returned.

        Returns: 
        ----- 
        MS::kSuccess Suspend status updated.  MS::kFailure Internal
        error.

        Parameters:
        -----
        update: bool
        	[in] -> state the new suspend status. 

        ReturnStatus: MPxUITableControl.MStatus
        	[out] -> status of the call.


        '''
        pass

    def isSelected(self, row: int,
                        col: int,
                        ReturnStatus: MPxUITableControl.MStatus): 
        '''
        isSelected(self, row: int,
                        col: int,
                        ReturnStatus: MPxUITableControl.MStatus) -> bool

        Synopsis
        -----
        Returns true if the specified cell is selected.

        Returns: 
        ----- 
        MS::kSuccess Successfully returned the selected state.
        MS::kFailure Internal error.

        Parameters:
        -----
        row: int
        	[in] -> cell row position. 

        col: int
        	[in] -> cell col position. 

        ReturnStatus: MPxUITableControl.MStatus
        	[out] -> Status code.


        '''
        pass

    def collapseOrExpandRow(self, row: int): 
        '''
        collapseOrExpandRow(self, row: int) -> bool

        Synopsis
        -----
        This is called when a row should be collapsed or expanded
        (depending on its current state).

        Returns: 
        ----- 
        true the action was handled.  false the action was not handled.

        Parameters:
        -----
        row: int
        	[in] -> the row to collapse.


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

    def cellString(self, r: int,
                        c: int,
                        isValidCell: bool): 
        '''
        cellString(self, r: int,
                        c: int,
                        isValidCell: bool) -> MString

        Synopsis
        -----
        Returns the contents of a cell. Derived classes MUST override
        either this method or getCell().

        Returns: 
        ----- 
        Contents of the specified cell, as a string, or an empty string
        if an invalid cell was specified.

        Parameters:
        -----
        r: int
        	[in] -> Row index of the cell. 

        c: int
        	[in] -> Column index of the cell. 

        isValidCell: bool
        	[out] -> True if the row and column specify a valid cell, false otherwise.


        '''
        pass

    def labelString(self, labelType: MPxUITableControl.MLabelType,
                        n: int): 
        '''
        labelString(self, labelType: MPxUITableControl.MLabelType,
                        n: int) -> MString

        Synopsis
        -----
        Returns the text of the label for the given row or column. The
        base implementation of the method always returns an empty string.

        Returns: 
        ----- 
        Text of the requested label or an empty string if 'index' is
        invalid.

        Parameters:
        -----
        labelType: MPxUITableControl.MLabelType
        	[in] -> Specifies whether a row or column label is requested. 

        n: int
        	[in] -> Row or column index.


        '''
        pass

    def allowEdit(self): 
        '''
        allowEdit(self) -> bool

        Synopsis
        -----
        Tells the base UI table control class if this control is
        editable. It is possible to implement tables that simple display
        information and do not allow the user to edit them.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def allowSelection(self, top: int,
                        left: int,
                        bottom: int,
                        right: int): 
        '''
        allowSelection(self, top: int,
                        left: int,
                        bottom: int,
                        right: int) -> bool

        Synopsis
        -----
        This method is called when a selection occurs. In this base
        implementation it always returns true. However, this method can
        be overridden to allow or disallow a selection.

        Returns: 
        ----- 
        true the table can be edited.  false the table should not be
        edited.

        Parameters:
        -----
        top: int
        	[in] -> top cell coordinate 

        left: int
        	[in] -> left cell coordinate 

        bottom: int
        	[in] -> bottom cell coordinate 

        right: int
        	[in] -> right cell coordinate


        '''
        pass

    def getCellColor(self, row: int,
                        column: int,
                        red: int,
                        green: int,
                        blue: int): 
        '''
        getCellColor(self, row: int,
                        column: int,
                        red: int,
                        green: int,
                        blue: int) -> bool

        Synopsis
        -----
        Returns the background color of a cell.

        Returns: 
        ----- 
        True state if 'row' and 'column' specify a valid cell, false
        otherwise.

        Parameters:
        -----
        row: int
        	[in] -> Row index of cell. 

        column: int
        	[in] -> Column index of cell. 

        red: int
        	[out] -> The Red component of the colour 

        green: int
        	[out] -> The Green component of the colour 

        blue: int
        	[out] -> The Blue component of the colour


        '''
        pass

class MLabelType:
    '''Types of labels available in the control. 
    Non-functional class.  Values for this enum:
    kNoLabel
    kRowLabel
    kColumnLabel
    kAllLabels
    '''

    def __init__(self):
        pass

    def kNoLabel(self):
        '''This is an enum of MLabelType.
        - Description:  
        - Value: 0
        '''
        pass

    def kRowLabel(self):
        '''This is an enum of MLabelType.
        - Description:  
        - Value: 1
        '''
        pass

    def kColumnLabel(self):
        '''This is an enum of MLabelType.
        - Description:  
        - Value: 2
        '''
        pass

    def kAllLabels(self):
        '''This is an enum of MLabelType.
        - Description:  
        - Value: 3
        '''
        pass

