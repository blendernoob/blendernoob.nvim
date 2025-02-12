
'''
Stub class file for:
OpenMayaFX

Maya2024 Python API stub file
Pycharm Version
Generated from original Maya documentation.
Autodesk Maya2024  c1997-2023 Autodesk, Inc. All rights reserved. 
'''


from typing import overload




class MnCloth:
    '''Class for wrapping N cloth objects.
This class wraps the internal Maya representation of N cloth
objects suitable for use with the Nucleus solver.
'''
    def __init__(self):
        pass


    def createNCloth(self): 
        '''
        createNCloth(self)

        Synopsis
        -----
        Creates the underlying Maya TnCloth and sets this class to wrap
        it.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setTopology(self, numFaces: int,
                        numVertsPerFace: int,
                        faces: int,
                        numEdges: int,
                        edges: int): 
        '''
        setTopology(self, numFaces: int,
                        numVertsPerFace: int,
                        faces: int,
                        numEdges: int,
                        edges: int)

        Synopsis
        -----
        sets the topology of the underlying N Object. Before calling
        other methods, this must be the first method you call once the
        cloth object is created.

        Returns:
        -----
        None

        Parameters:
        -----
        numFaces: int
        	[in] -> number of faces 

        numVertsPerFace: int
        	[in] -> an array of size numFaces, where each element describes the number of verts on that face 

        faces: int
        	[in] -> an array containing the actual face description. Each element is a vertex index. 

        numEdges: int
        	[in] -> number of edges 

        edges: int
        	[in] -> an array containing the edge description. Each element is a vertex index.


        '''
        pass

    def setPositions(self, positions: MFloatPointArray,
                        startFrame: bool): 
        '''
        setPositions(self, positions: MFloatPointArray,
                        startFrame: bool)

        Synopsis
        -----
        Sets the positions of the vertices of the underlying N cloth
        object.

        Returns:
        -----
        None

        Parameters:
        -----
        positions: MFloatPointArray
        	[in] -> the array containing the position information 

        startFrame: bool
        	[in] -> whether this information represents the state of the object at the start frame.


        '''
        pass

    def setVelocities(self, velocities: MFloatPointArray): 
        '''
        setVelocities(self, velocities: MFloatPointArray)

        Synopsis
        -----
        Sets the velocities of the vertices of the underlying Ncloth
        object.

        Returns:
        -----
        None

        Parameters:
        -----
        velocities: MFloatPointArray
        	[in] -> the array containing the velocity information


        '''
        pass

    def setBendRestAngleFromPositions(self, positions: MFloatPointArray): 
        '''
        setBendRestAngleFromPositions(self, positions: MFloatPointArray)

        Synopsis
        -----
        Sets the the bend rest angle from the list of positions for the
        underlying N Object This sets the shape that bend resistance is
        trying to achieve.

        Returns:
        -----
        None

        Parameters:
        -----
        positions: MFloatPointArray
        	[in] -> the array containing the position information


        '''
        pass

    def setLinksRestLengthFromPositions(self, positions: MFloatPointArray): 
        '''
        setLinksRestLengthFromPositions(self, positions: MFloatPointArray)

        Synopsis
        -----
        Sets the the rest length from the list of positions for the
        underlying N Object. This sets the shape that the
        stretch/compression resistance are trying to achieve.

        Returns:
        -----
        None

        Parameters:
        -----
        positions: MFloatPointArray
        	[in] -> the array containing the position information


        '''
        pass

    def setInputMeshAttractPositions(self, positions: MFloatPointArray): 
        '''
        setInputMeshAttractPositions(self, positions: MFloatPointArray)

        Synopsis
        -----
        Sets the positions for input mesh attract.

        Returns:
        -----
        None

        Parameters:
        -----
        positions: MFloatPointArray
        	[in] -> the array containing the position information


        '''
        pass

    def setInputMeshAttractDamping(self, damping: float): 
        '''
        setInputMeshAttractDamping(self, damping: float)

        Synopsis
        -----
        Defines how springy the effect of Input Mesh Attract is. At a
        value of zero input mesh attract will behave like a spring
        connection from the input mesh to the output dynamic mesh. The
        cloth will tend to wiggle about the input mesh position. As the
        Input Attract Damp is increased to 1 the cloth mesh will still
        move to the input mesh position but not have the momentum to
        travel past it, so will no longer occillate about the input
        position.

        Returns:
        -----
        None

        Parameters:
        -----
        damping: float
        	[in] -> the damping value


        '''
        pass

    def setInputMeshAttractAndRigidStrength(self, inputAttractArray: float,
                        rigidArray: float,
                        deformArray: float): 
        '''
        setInputMeshAttractAndRigidStrength(self, inputAttractArray: float,
                        rigidArray: float,
                        deformArray: float)

        Synopsis
        -----
        Sets on a per particle basis, the amount by which each particle
        is affected by the input mesh attract, rigidity, and
        deformability. High values for the input mesh attract will make
        points stick closely to the input mesh. High values for the
        rigidArray will make the object behave like a rigid body.These
        arguments actually encode 2 pieces of information in 1. It
        contains instructions for:A) The number of iterations and B) The
        strength of the effectThe number of iterations is the maximum
        value over the array passed in. The relative strength, measured
        from 0 to 1, is the normalized value of each element of the
        array.For example, if for the inputAttractArray one were to
        specify a value of 10.0 for the first element, and 1.0 for the
        rest, it means that the solver should take 10 steps to compute
        inputMeshAttract, and the first particle has a strength of 1
        while the rest have a strength of 0.1.

        Returns:
        -----
        None

        Parameters:
        -----
        inputAttractArray: float
        	[in] -> values for the input mesh attract 

        rigidArray: float
        	[in] -> values for rigidity 

        deformArray: float
        	[in] -> values for deformability


        '''
        pass

    def setComputeRestLength(self, b: bool): 
        '''
        setComputeRestLength(self, b: bool)

        Synopsis
        -----
        Sets whether rest lengths will be automatically computed, or
        overridden manually. If this is set to false, then you must call
        setLinksRestLengthFromPositions() to set the rest lengths.

        Returns:
        -----
        None

        Parameters:
        -----
        b: bool
        	[in] -> whether to compute rest lengths


        '''
        pass

    def setComputeRestAngles(self, b: bool): 
        '''
        setComputeRestAngles(self, b: bool)

        Synopsis
        -----
        Sets whether rest angles will be automatically computed, or
        overridden manually. If this is set to false, then you must call
        setBendRestAngleFromPositions() to set the rest lengths.

        Returns:
        -----
        None

        Parameters:
        -----
        b: bool
        	[in] -> whether to compute rest angles


        '''
        pass

    @overload
    def setThickness(self, radius: float): 
        '''
        setThickness(self, radius: float)

        Synopsis
        -----
        sets a radius on each point of the mesh for collision purposes.
        The bigger the radius/thickness, the more easily things collide.

        Returns:
        -----
        None

        Parameters:
        -----
        radius: float
        	[in] -> the radius to set


        '''
        pass

    @overload
    def setThickness(self, radius: float): 
        '''
        setThickness(self, radius: float)

        Synopsis
        -----
        sets a radius (thickness) on a per point basis for the mesh for
        collision purposes. The bigger the radius, the more easily things
        collide.

        Returns:
        -----
        None

        Parameters:
        -----
        radius: float
        	[in] -> the radius to set


        '''
        pass

    @overload
    def setInverseMass(self, invMass: float): 
        '''
        setInverseMass(self, invMass: float)

        Synopsis
        -----
        sets the mass for every point in this mesh

        Returns:
        -----
        None

        Parameters:
        -----
        invMass: float
        	[in] -> the inverse of the mass. A value of 0 means an infinitely heave object.


        '''
        pass

    @overload
    def setInverseMass(self, invMass: float): 
        '''
        setInverseMass(self, invMass: float)

        Synopsis
        -----
        sets the mass on a per point basis in this mesh

        Returns:
        -----
        None

        Parameters:
        -----
        invMass: float
        	[in] -> the inverse of the mass. A value of 0 means an infinitely heave object.


        '''
        pass

    @overload
    def setBounce(self, bounce: float): 
        '''
        setBounce(self, bounce: float)

        Synopsis
        -----
        sets the bounce for every point in this mesh

        Returns:
        -----
        None

        Parameters:
        -----
        bounce: float
        	[in] -> value of bounce to set


        '''
        pass

    @overload
    def setBounce(self, bounce: float): 
        '''
        setBounce(self, bounce: float)

        Synopsis
        -----
        sets the bounce on a per point basis in this mesh

        Returns:
        -----
        None

        Parameters:
        -----
        bounce: float
        	[in] -> value of bounce to set


        '''
        pass

    @overload
    def setFriction(self, friction: float): 
        '''
        setFriction(self, friction: float)

        Synopsis
        -----
        sets the friction for every point in this mesh

        Returns:
        -----
        None

        Parameters:
        -----
        friction: float
        	[in] -> the friction to set


        '''
        pass

    @overload
    def setFriction(self, friction: float): 
        '''
        setFriction(self, friction: float)

        Synopsis
        -----
        sets the friction on a per point basis for this mesh

        Returns:
        -----
        None

        Parameters:
        -----
        friction: float
        	[in] -> the friction to set


        '''
        pass

    @overload
    def setDamping(self, damping: float): 
        '''
        setDamping(self, damping: float)

        Synopsis
        -----
        sets the damping for every point in this mesh

        Returns:
        -----
        None

        Parameters:
        -----
        damping: float
        	[in] -> the damping value to set


        '''
        pass

    @overload
    def setDamping(self, damping: float): 
        '''
        setDamping(self, damping: float)

        Synopsis
        -----
        sets the on a per point basis in this mesh

        Returns:
        -----
        None

        Parameters:
        -----
        damping: float
        	[in] -> the damping value to set


        '''
        pass

    def setSelfCollisionFlags(self, vertToVert: bool,
                        vertToEdge: bool,
                        vertToFace: bool,
                        edgeToEdge: bool,
                        edgeToFace: bool): 
        '''
        setSelfCollisionFlags(self, vertToVert: bool,
                        vertToEdge: bool,
                        vertToFace: bool,
                        edgeToEdge: bool,
                        edgeToFace: bool)

        Synopsis
        -----
        Sets how (or if) this object will collide with itself.

        Returns:
        -----
        None

        Parameters:
        -----
        vertToVert: bool
        	[in] -> whether to calculate vertex - vertex collisions 

        vertToEdge: bool
        	[in] -> whether to calculate vertex - edge collisions 

        vertToFace: bool
        	[in] -> whether to calculate vertex - face collisions 

        edgeToEdge: bool
        	[in] -> whether to calculate edge - edge collisions 

        edgeToFace: bool
        	[in] -> whether to calculate edge - face collisions


        '''
        pass

    def setCollisionFlags(self, vertToVert: bool,
                        edgeToEdge: bool,
                        faceToFace: bool): 
        '''
        setCollisionFlags(self, vertToVert: bool,
                        edgeToEdge: bool,
                        faceToFace: bool)

        Synopsis
        -----
        Sets how (or if) this object will collide with other objects.

        Returns:
        -----
        None

        Parameters:
        -----
        vertToVert: bool
        	[in] -> whether to calculate vertex - vertex collisions 

        edgeToEdge: bool
        	[in] -> whether to calculate edge - edge collisions 

        faceToFace: bool
        	[in] -> whether to calculate face - face collisions


        '''
        pass

    def setDisableGravity(self, b: bool): 
        '''
        setDisableGravity(self, b: bool)

        Synopsis
        -----
        Sets whether gravity will affect this object.

        Returns:
        -----
        None

        Parameters:
        -----
        b: bool
        	[in] -> whether to calculate gravity


        '''
        pass

    def setMaxIterations(self, it: int): 
        '''
        setMaxIterations(self, it: int)

        Synopsis
        -----
        Sets the number of iterations the solver will perform on various
        dynamic properties like drag, damping, stretch and bend. Higher
        iterations take longer, and the primary use of this attribute is
        to keep things from locking up should high iteration values be
        requested.

        Returns:
        -----
        None

        Parameters:
        -----
        it: int
        	[in] -> number of iterations


        '''
        pass

    def setMaxSelfCollisionIterations(self, it: int): 
        '''
        setMaxSelfCollisionIterations(self, it: int)

        Synopsis
        -----
        Sets the number of iterations the solver will perform for self
        collisions on this object.

        Returns:
        -----
        None

        Parameters:
        -----
        it: int
        	[in] -> number of iterations


        '''
        pass

    def setSelfCollisionSoftness(self, softness: float): 
        '''
        setSelfCollisionSoftness(self, softness: float)

        Synopsis
        -----
        This allows one to lower the repulsive force of self collisions
        such that some interpenetration within the collide width is
        allowed. This can in some cases reduce jitter due to self
        collision with low selfCollideIterations. In general its use
        should be avoided, however.

        Returns:
        -----
        None

        Parameters:
        -----
        softness: float
        	[in] -> value to set.


        '''
        pass

    def setSelfTrappedCheck(self, on: bool): 
        '''
        setSelfTrappedCheck(self, on: bool)

        Synopsis
        -----
        This tracks self collision crossovers and attempts to push the
        crossed over points back. It assumes that the surface is in a
        good state at the start and attempts to preserve that relative
        state. It is useful in cases where cloth can get caught between
        passive objects than interpenetrate (for example an elbow passing
        through a chest). Rather than get stuck on the wrong side this
        allows the cloth to push back to the correct side when the
        passive objects later separate.

        Returns:
        -----
        None

        Parameters:
        -----
        on: bool
        	[in] -> whether to turn on self trapped check.


        '''
        pass

    def setSelfCrossoverPush(self, val: float): 
        '''
        setSelfCrossoverPush(self, val: float)

        Synopsis
        -----
        See node documentation.

        Returns:
        -----
        None

        Parameters:
        -----
        val: float
        	[in] -> value for crossover push


        '''
        pass

    def setDragAndLift(self, drag: float,
                        lift: float): 
        '''
        setDragAndLift(self, drag: float,
                        lift: float)

        Synopsis
        -----
        Sets the drag and lift values for the cloth.

        Returns:
        -----
        None

        Parameters:
        -----
        drag: float
        	[in] -> value of drag 

        lift: float
        	[in] -> value of lift


        '''
        pass

    def setTangentialDrag(self, tangentialDrag: float): 
        '''
        setTangentialDrag(self, tangentialDrag: float)

        Synopsis
        -----
        Sets the tangential drag values for the cloth. Defines the
        component of drag tangent to the surface. With a value of zero a
        flat plane will slice through air with no resistance and only
        have drag when moving along its normal axis. With a value of 1.0
        the effect of drag will be equal in all directions.

        Returns:
        -----
        None

        Parameters:
        -----
        tangentialDrag: float
        	[in] -> the tangential drag


        '''
        pass

    def setStartPressure(self, startPressure: float): 
        '''
        setStartPressure(self, startPressure: float)

        Synopsis
        -----
        With the volume tracking pressure method this defines the
        relative air pressure inside the object at the startframe.

        Returns:
        -----
        None

        Parameters:
        -----
        startPressure: float
        	[in] -> the start pressure


        '''
        pass

    def setSealHoles(self, seal: bool): 
        '''
        setSealHoles(self, seal: bool)

        Synopsis
        -----
        When the volume tracking pressure method is used this determines
        if physical holes in the cloth model are treated as being capped
        or not. If holes are not sealed, then air can escape out them,
        which also has the effect of pushing the cloth. For example, this
        can simulate a rubber balloon that is suddenly released. It also
        allows for inflow based on motion of the cloth. The opening in a
        parachute will allow air to flow in as it falls down, causing
        sideways pressure that inflates it. Note that drag alone cannot
        achieve this sort of effect

        Returns:
        -----
        None

        Parameters:
        -----
        seal: bool
        	[in] -> whether to seal holes


        '''
        pass

    def setPressure(self, pressure: float): 
        '''
        setPressure(self, pressure: float)

        Synopsis
        -----
        Sets the pressure within the cloth. This defines a force applied
        along the surface normal direction

        Returns:
        -----
        None

        Parameters:
        -----
        pressure: float
        	[in] -> the value of pressure to set


        '''
        pass

    def setTrackVolume(self, track: bool): 
        '''
        setTrackVolume(self, track: bool)

        Synopsis
        -----

        Returns:
        -----
        None

        Parameters:
        -----
        track: bool
        	[in] -> whether to track volume


        '''
        pass

    def setIncompressibility(self, v: float): 
        '''
        setIncompressibility(self, v: float)

        Synopsis
        -----
        When the volume tracking pressure model is used this defines how
        incompressible the internal volume of fluid is. This also will
        affect how much force is applied to the cloth when air is pumped
        in. In the case of a balloon higher values of incompressibility
        will overcome higher stretch resistance. Note that higher
        incompressibility may require more calculation time.

        Returns:
        -----
        None

        Parameters:
        -----
        v: float
        	[in] -> how incompressible the cloth is


        '''
        pass

    def setPressureDamping(self, damp: float): 
        '''
        setPressureDamping(self, damp: float)

        Synopsis
        -----
        Sets the damping value for pressure.

        Returns:
        -----
        None

        Parameters:
        -----
        damp: float
        	[in] -> value to set


        '''
        pass

    def setPumpRate(self, pump: float): 
        '''
        setPumpRate(self, pump: float)

        Synopsis
        -----
        Defines the rate at which air pressure is added to the object.

        Returns:
        -----
        None

        Parameters:
        -----
        pump: float
        	[in] -> value to set


        '''
        pass

    def setAirTightness(self, airTightness: float): 
        '''
        setAirTightness(self, airTightness: float)

        Synopsis
        -----
        Defines the rate at which air can escape from the object, or how
        permiable the surface is. This is in addition to any physical
        holes in the model, which can be be capped or not using the seal
        holes method.

        Returns:
        -----
        None

        Parameters:
        -----
        airTightness: float
        	[in] -> value to set


        '''
        pass

    def setAddCrossLinks(self, addCrossLinks: bool): 
        '''
        setAddCrossLinks(self, addCrossLinks: bool)

        Synopsis
        -----
        For faces with more than 3 vertices this will create additional
        stretch and bends links such that each vertex is connected to
        each other vertex. If this is off then the links will exactly
        match the meshes list of edges. For a quad meshes having
        addCrossLinks off would allow the cloth to shear, unless shear
        resistance was used.

        Returns:
        -----
        None

        Parameters:
        -----
        addCrossLinks: bool
        	[in] -> value to set


        '''
        pass

    def setBendAngleDropoff(self, dropoff: float): 
        '''
        setBendAngleDropoff(self, dropoff: float)

        Synopsis
        -----
        Defines the way bend resistance changes with the angle. At higher
        values the bend will resist more at high angles then when the
        surface is nearly flat.

        Returns:
        -----
        None

        Parameters:
        -----
        dropoff: float
        	[in] -> value to set


        '''
        pass

    def setShearResistance(self, resistance: float): 
        '''
        setShearResistance(self, resistance: float)

        Synopsis
        -----
        Sets the shear resistance. Shear can be thought of as the bend in
        the plane of the cloth.

        Returns:
        -----
        None

        Parameters:
        -----
        resistance: float
        	[in] -> value to set


        '''
        pass

    @overload
    def setStretchAndCompressionResistance(self, stretchResist: float,
                        compressionResist: float): 
        '''
        setStretchAndCompressionResistance(self, stretchResist: float,
                        compressionResist: float)

        Synopsis
        -----
        Stretch Resistance: Defines the amount that the material will
        resist stretching when under tension. Large values generally
        require more computation, so they may result in longer simulation
        times. Note that the scalingRelation attribute affects how this
        value is defined. Also one may need to additionally make the both
        collision iterations on the solver and constraint strength values
        high to keep stretching low.Compression Resistance:Defines the
        amount that the material will resist compression. Note that
        sometimes it is useful to have this value be lower than the
        Stretch Resistance, because the mesh resolution is only an
        approximation to a true surface, which could possibly fold within
        the length of a triangle. If one has a rest position for a cloth
        that is not flat and the compression and stretch resistance are
        both high then this can make cloth appear too stiff because the
        topology locks up. This problem is most noticable when the faces
        have relatively high angles relative to each other. Having a low
        compression resistance allows the material keep from locking up,
        yet still not appear to stretchy. Large values generally require
        more computation, so they may result in longer simulation times.

        Returns:
        -----
        None

        Parameters:
        -----
        stretchResist: float
        	[in] -> value to set for stretch 

        compressionResist: float
        	[in] -> value to set for compression


        '''
        pass

    @overload
    def setStretchAndCompressionResistance(self, stretchResist: float,
                        compressionResist: float): 
        '''
        setStretchAndCompressionResistance(self, stretchResist: float,
                        compressionResist: float)

        Synopsis
        -----
        Sets the stretch and compression resistance for the mesh on a per
        vertex basis.

        Returns:
        -----
        None

        Parameters:
        -----
        stretchResist: float
        	[in] -> value to set for stretch 

        compressionResist: float
        	[in] -> value to set for compression


        '''
        pass

    def setBendAngleScale(self, scale: float): 
        '''
        setBendAngleScale(self, scale: float)

        Synopsis
        -----
        Defines the amount by which the rest state of the bend angle is
        scaled.

        Returns:
        -----
        None

        Parameters:
        -----
        scale: float
        	[in] -> value to set


        '''
        pass

    def setRestitutionAngle(self, angle: float): 
        '''
        setRestitutionAngle(self, angle: float)

        Synopsis
        -----
        Defines how far we can bend across an edge before it will fail to
        go back to the rest angle when there are no forces acting on the
        cloth.

        Returns:
        -----
        None

        Parameters:
        -----
        angle: float
        	[in] -> value to set


        '''
        pass

    def setRestitutionTension(self, tension: float): 
        '''
        setRestitutionTension(self, tension: float)

        Synopsis
        -----
        How far can the links be stretched before they fail to go back to
        their rest length when there are no forces acting on the cloth.
        When the tension is greater than the defined value the defined
        rest length will increase until the tension is equal this value.
        For very low values the material will pull apart like taffy, yet
        still resist stretching under mild forces.

        Returns:
        -----
        None

        Parameters:
        -----
        tension: float
        	[in] -> value to set


        '''
        pass

    def setSelfCollideWidth(self, width: float): 
        '''
        setSelfCollideWidth(self, width: float)

        Synopsis
        -----
        Sets the self collision width.

        Returns:
        -----
        None

        Parameters:
        -----
        width: float
        	[in] -> value to set


        '''
        pass

    def setBendResistance(self, strength: float): 
        '''
        setBendResistance(self, strength: float)

        Synopsis
        -----
        Bend resistance measures the amount of attraction to the
        restAngle, which is defined between cvs on either side of an
        edge. Larger values will tend to make the surface more rigid and
        will take longer to compute.

        Returns:
        -----
        None

        Parameters:
        -----
        strength: float
        	[in] -> value to set


        '''
        pass

    def getNumVertices(self, numVerts: int): 
        '''
        getNumVertices(self, numVerts: int)

        Synopsis
        -----
        Returns the number of vertices in the underlying n Cloth.

        Returns:
        -----
        None

        Parameters:
        -----
        numVerts: int
        	[out] -> Number of vertices.


        '''
        pass

    def getPositions(self, positions: MFloatPointArray): 
        '''
        getPositions(self, positions: MFloatPointArray)

        Synopsis
        -----
        gets the positions of the points of the underlying N Object.

        Returns:
        -----
        None

        Parameters:
        -----
        positions: MFloatPointArray
        	[out] -> the array will be filled with the positions.


        '''
        pass

    def getVelocities(self, velocities: MFloatPointArray): 
        '''
        getVelocities(self, velocities: MFloatPointArray)

        Synopsis
        -----
        gets the velocities of the points of the underlying N cloth
        object.

        Returns:
        -----
        None

        Parameters:
        -----
        velocities: MFloatPointArray
        	[out] -> the array will be filled with the positions.


        '''
        pass

    def getThickness(self, radius: MFloatArray): 
        '''
        getThickness(self, radius: MFloatArray)

        Synopsis
        -----
        gets the thickness at each point of the underlying N cloth
        object.

        Returns:
        -----
        None

        Parameters:
        -----
        radius: MFloatArray
        	[out] -> the array will be filled with the thickness.


        '''
        pass

    def getInverseMass(self, inverseMass: MFloatArray): 
        '''
        getInverseMass(self, inverseMass: MFloatArray)

        Synopsis
        -----
        gets the inverseMass at each point of the underlying N cloth
        object.

        Returns:
        -----
        None

        Parameters:
        -----
        inverseMass: MFloatArray
        	[out] -> the array will be filled with the inverse masses.


        '''
        pass

    def getBounce(self, bounce: MFloatArray): 
        '''
        getBounce(self, bounce: MFloatArray)

        Synopsis
        -----
        gets the bounce at each point of the underlying N cloth object.

        Returns:
        -----
        None

        Parameters:
        -----
        bounce: MFloatArray
        	[out] -> the array will be filled with the bounce.


        '''
        pass

    def getFriction(self, friction: MFloatArray): 
        '''
        getFriction(self, friction: MFloatArray)

        Synopsis
        -----
        gets the friction at each point of the underlying N cloth object.

        Returns:
        -----
        None

        Parameters:
        -----
        friction: MFloatArray
        	[out] -> the array will be filled with the friction.


        '''
        pass

    def setNCloth(self, nObj: MnCloth.TnCloth,
                        own: bool): 
        '''
        setNCloth(self, nObj: MnCloth.TnCloth,
                        own: bool)

        Synopsis
        -----
        Sets the TnCloth pointer which this class wraps. If own is true,
        then the TnCloth will be deleted when this class is destroyed.

        Returns:
        -----
        None

        Parameters:
        -----
        nObj: MnCloth.TnCloth
        	[in] -> 

        own: bool
        	[in] -> 


        '''
        pass

class MnObject:
    '''Class for wrapping N cloth objects.
This class wraps the internal Maya representation of N cloth
objects suitable for use with the Nucleus solver.
'''
    def __init__(self):
        pass


    def setNObject(self, nObj: MnObject.TnObject,
                        own: bool): 
        '''
        setNObject(self, nObj: MnObject.TnObject,
                        own: bool)

        Synopsis
        -----
        Sets the TnObject pointer which this class wraps. If own is true,
        then the TnObject will be deleted when this class is destroyed.

        Returns:
        -----
        None

        Parameters:
        -----
        nObj: MnObject.TnObject
        	[in] -> 

        own: bool
        	[in] -> 


        '''
        pass

class MnParticle:
    '''Class for wrapping N cloth objects.
This class wraps the internal Maya representation of N cloth
objects suitable for use with the Nucleus solver.
'''
    def __init__(self):
        pass


    def createNParticle(self): 
        '''
        createNParticle(self)

        Synopsis
        -----
        Creates the underlying Maya TnParticle and sets this class to
        wrap it.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setTopology(self, numPoints: int): 
        '''
        setTopology(self, numPoints: int)

        Synopsis
        -----
        Sets the topology of the underlying N Object. This must be called
        whenever the number of particles changes, before setting any
        particle properties

        Returns:
        -----
        None

        Parameters:
        -----
        numPoints: int
        	[in] -> number of particles


        '''
        pass

    def setPositions(self, positions: MFloatPointArray,
                        startFrame: bool): 
        '''
        setPositions(self, positions: MFloatPointArray,
                        startFrame: bool)

        Synopsis
        -----
        Sets the positions of the vertices of the underlying nParticle
        object.

        Returns:
        -----
        None

        Parameters:
        -----
        positions: MFloatPointArray
        	[in] -> the array containing the position information 

        startFrame: bool
        	[in] -> whether this information represents the state of the object at the start frame.


        '''
        pass

    def setVelocities(self, velocities: MFloatPointArray): 
        '''
        setVelocities(self, velocities: MFloatPointArray)

        Synopsis
        -----
        Sets the velocities of the vertices of the underlying nParticle
        object.

        Returns:
        -----
        None

        Parameters:
        -----
        velocities: MFloatPointArray
        	[in] -> the array containing the velocity information


        '''
        pass

    @overload
    def setThickness(self, radius: float): 
        '''
        setThickness(self, radius: float)

        Synopsis
        -----
        sets a radius on each point collision purposes. The bigger the
        radius/thickness, the more easily things collide.

        Returns:
        -----
        None

        Parameters:
        -----
        radius: float
        	[in] -> the radius to set


        '''
        pass

    @overload
    def setThickness(self, radius: float): 
        '''
        setThickness(self, radius: float)

        Synopsis
        -----
        sets a radius (thickness) on a per point basis for collision
        purposes. The bigger the radius, the more easily things collide.

        Returns:
        -----
        None

        Parameters:
        -----
        radius: float
        	[in] -> the radius to set


        '''
        pass

    @overload
    def setInverseMass(self, invMass: float): 
        '''
        setInverseMass(self, invMass: float)

        Synopsis
        -----
        sets the mass for every particle

        Returns:
        -----
        None

        Parameters:
        -----
        invMass: float
        	[in] -> the inverse of the mass. A value of 0 means an infinitely heavy object.


        '''
        pass

    @overload
    def setInverseMass(self, invMass: float): 
        '''
        setInverseMass(self, invMass: float)

        Synopsis
        -----
        sets the mass on a per point basis

        Returns:
        -----
        None

        Parameters:
        -----
        invMass: float
        	[in] -> the inverse of the mass. A value of 0 means an infinitely heave object.


        '''
        pass

    @overload
    def setBounce(self, bounce: float): 
        '''
        setBounce(self, bounce: float)

        Synopsis
        -----
        sets the bounce for every particle

        Returns:
        -----
        None

        Parameters:
        -----
        bounce: float
        	[in] -> value of bounce to set


        '''
        pass

    @overload
    def setBounce(self, bounce: float): 
        '''
        setBounce(self, bounce: float)

        Synopsis
        -----
        sets the bounce on a per point basis for these particles

        Returns:
        -----
        None

        Parameters:
        -----
        bounce: float
        	[in] -> value of bounce to set


        '''
        pass

    @overload
    def setFriction(self, friction: float): 
        '''
        setFriction(self, friction: float)

        Synopsis
        -----
        sets the friction for every particle

        Returns:
        -----
        None

        Parameters:
        -----
        friction: float
        	[in] -> the friction to set


        '''
        pass

    @overload
    def setFriction(self, friction: float): 
        '''
        setFriction(self, friction: float)

        Synopsis
        -----
        sets the friction on a per point basis for these particles

        Returns:
        -----
        None

        Parameters:
        -----
        friction: float
        	[in] -> the friction to set


        '''
        pass

    @overload
    def setDamping(self, damping: float): 
        '''
        setDamping(self, damping: float)

        Synopsis
        -----
        sets the damping for every particle

        Returns:
        -----
        None

        Parameters:
        -----
        damping: float
        	[in] -> the damping value to set


        '''
        pass

    @overload
    def setDamping(self, damping: float): 
        '''
        setDamping(self, damping: float)

        Synopsis
        -----
        sets the damping on a per point basis for these particles

        Returns:
        -----
        None

        Parameters:
        -----
        damping: float
        	[in] -> the damping value to set


        '''
        pass

    def setDisableGravity(self, b: bool): 
        '''
        setDisableGravity(self, b: bool)

        Synopsis
        -----
        Sets whether gravity will affect this object.

        Returns:
        -----
        None

        Parameters:
        -----
        b: bool
        	[in] -> whether to calculate gravity


        '''
        pass

    def setLiquidSimulation(self, b: bool): 
        '''
        setLiquidSimulation(self, b: bool)

        Synopsis
        -----
        Sets whether this object will solve as a liquid.

        Returns:
        -----
        None

        Parameters:
        -----
        b: bool
        	[in] -> whether to calculate liquid


        '''
        pass

    def setIncompressibility(self, incompressibility: float): 
        '''
        setIncompressibility(self, incompressibility: float)

        Synopsis
        -----
        sets the incompressibility

        Returns:
        -----
        None

        Parameters:
        -----
        incompressibility: float
        	[in] -> the incompressibility value to set


        '''
        pass

    def setRestDensity(self, restDensity: float): 
        '''
        setRestDensity(self, restDensity: float)

        Synopsis
        -----
        sets the rest density for every particle

        Returns:
        -----
        None

        Parameters:
        -----
        restDensity: float
        	[in] -> the rest density value to set


        '''
        pass

    def setLiquidRadiusScale(self, liquidRadiusScale: float): 
        '''
        setLiquidRadiusScale(self, liquidRadiusScale: float)

        Synopsis
        -----
        sets the liquidRadiusScale for every particle

        Returns:
        -----
        None

        Parameters:
        -----
        liquidRadiusScale: float
        	[in] -> the liquidRadiusScale value to set


        '''
        pass

    @overload
    def setViscosity(self, viscosity: float): 
        '''
        setViscosity(self, viscosity: float)

        Synopsis
        -----
        sets the viscosity for every particle

        Returns:
        -----
        None

        Parameters:
        -----
        viscosity: float
        	[in] -> the viscosity value to set


        '''
        pass

    @overload
    def setViscosity(self, viscosity: float): 
        '''
        setViscosity(self, viscosity: float)

        Synopsis
        -----
        sets the viscosity on a per point basis for these particles

        Returns:
        -----
        None

        Parameters:
        -----
        viscosity: float
        	[in] -> the viscosity value to set


        '''
        pass

    @overload
    def setSurfaceTension(self, surfaceTension: float): 
        '''
        setSurfaceTension(self, surfaceTension: float)

        Synopsis
        -----
        sets the surfaceTension for every particle

        Returns:
        -----
        None

        Parameters:
        -----
        surfaceTension: float
        	[in] -> the surfaceTension value to set


        '''
        pass

    @overload
    def setSurfaceTension(self, surfaceTension: float): 
        '''
        setSurfaceTension(self, surfaceTension: float)

        Synopsis
        -----
        sets the surfaceTension on a per point basis for these particles

        Returns:
        -----
        None

        Parameters:
        -----
        surfaceTension: float
        	[in] -> the surfaceTension value to set


        '''
        pass

    def setMaxIterations(self, it: int): 
        '''
        setMaxIterations(self, it: int)

        Synopsis
        -----
        Sets the number of iterations the solver will perform on various
        dynamic properties like drag, damping, stretch and bend. Higher
        iterations take longer, and the primary use of this attribute is
        to keep things from locking up should high iteration values be
        requested.

        Returns:
        -----
        None

        Parameters:
        -----
        it: int
        	[in] -> number of iterations


        '''
        pass

    def setMaxSelfCollisionIterations(self, it: int): 
        '''
        setMaxSelfCollisionIterations(self, it: int)

        Synopsis
        -----
        Sets the number of iterations the solver will perform for self
        collisions on this object.

        Returns:
        -----
        None

        Parameters:
        -----
        it: int
        	[in] -> number of iterations


        '''
        pass

    def setSelfCollisionSoftness(self, softness: float): 
        '''
        setSelfCollisionSoftness(self, softness: float)

        Synopsis
        -----
        This allows one to lower the repulsive force of self collisions
        such that some interpenetration within the collide width is
        allowed. This can in some cases reduce jitter due to self
        collision with low selfCollideIterations. In general its use
        should be avoided, however.

        Returns:
        -----
        None

        Parameters:
        -----
        softness: float
        	[in] -> value to set.


        '''
        pass

    def setDragAndLift(self, drag: float,
                        lift: float): 
        '''
        setDragAndLift(self, drag: float,
                        lift: float)

        Synopsis
        -----
        Sets the drag and lift values for the nParticle.

        Returns:
        -----
        None

        Parameters:
        -----
        drag: float
        	[in] -> value of drag 

        lift: float
        	[in] -> value of lift


        '''
        pass

    def setCollide(self, b: bool): 
        '''
        setCollide(self, b: bool)

        Synopsis
        -----
        Sets whether collisions will affect this object.

        Returns:
        -----
        None

        Parameters:
        -----
        b: bool
        	[in] -> whether to calculate collision


        '''
        pass

    def setSelfCollide(self, b: bool): 
        '''
        setSelfCollide(self, b: bool)

        Synopsis
        -----
        Sets whether self collisions will affect this object.

        Returns:
        -----
        None

        Parameters:
        -----
        b: bool
        	[in] -> whether to calculate self collision


        '''
        pass

    def setSelfCollideWidth(self, width: float): 
        '''
        setSelfCollideWidth(self, width: float)

        Synopsis
        -----
        Sets the self collision width.

        Returns:
        -----
        None

        Parameters:
        -----
        width: float
        	[in] -> value to set


        '''
        pass

    def getNumVertices(self, numVerts: int): 
        '''
        getNumVertices(self, numVerts: int)

        Synopsis
        -----
        Returns the number of vertices in the underlying nParticle.

        Returns:
        -----
        None

        Parameters:
        -----
        numVerts: int
        	[out] -> Number of vertices.


        '''
        pass

    def getPositions(self, positions: MFloatPointArray): 
        '''
        getPositions(self, positions: MFloatPointArray)

        Synopsis
        -----
        gets the positions of the points of the underlying N Object.

        Returns:
        -----
        None

        Parameters:
        -----
        positions: MFloatPointArray
        	[out] -> the array will be filled with the positions.


        '''
        pass

    def getVelocities(self, velocities: MFloatPointArray): 
        '''
        getVelocities(self, velocities: MFloatPointArray)

        Synopsis
        -----
        gets the velocities of the points of the underlying nParticle
        object.

        Returns:
        -----
        None

        Parameters:
        -----
        velocities: MFloatPointArray
        	[out] -> the array will be filled with the positions.


        '''
        pass

    def getThickness(self, radius: MFloatArray): 
        '''
        getThickness(self, radius: MFloatArray)

        Synopsis
        -----
        gets the radii of the points of the underlying N particle object.

        Returns:
        -----
        None

        Parameters:
        -----
        radius: MFloatArray
        	[out] -> the array will be filled with the radii.


        '''
        pass

    def getInverseMass(self, inverseMass: MFloatArray): 
        '''
        getInverseMass(self, inverseMass: MFloatArray)

        Synopsis
        -----
        gets the inverseMass of the points of the underlying N particle
        object.

        Returns:
        -----
        None

        Parameters:
        -----
        inverseMass: MFloatArray
        	[out] -> the array will be filled with the inverse masses.


        '''
        pass

    def getBounce(self, bounce: MFloatArray): 
        '''
        getBounce(self, bounce: MFloatArray)

        Synopsis
        -----
        gets the Bounce of the points of the underlying N particle
        object.

        Returns:
        -----
        None

        Parameters:
        -----
        bounce: MFloatArray
        	[out] -> the array will be filled with the bounce.


        '''
        pass

    def getFriction(self, friction: MFloatArray): 
        '''
        getFriction(self, friction: MFloatArray)

        Synopsis
        -----
        gets the friction of the points of the underlying N particle
        object.

        Returns:
        -----
        None

        Parameters:
        -----
        friction: MFloatArray
        	[out] -> the array will be filled with the friction.


        '''
        pass

    def setNParticle(self, nObj: MnParticle.TnParticle,
                        own: bool): 
        '''
        setNParticle(self, nObj: MnParticle.TnParticle,
                        own: bool)

        Synopsis
        -----
        Sets the TnParticle pointer which this class wraps. If own is
        true, then the TnParticle will be deleted when this instance is
        destroyed.

        Returns:
        -----
        None

        Parameters:
        -----
        nObj: MnParticle.TnParticle
        	[in] -> TnParticle object. 

        own: bool
        	[in] -> Should this instance take ownership of the TnParticle? 


        '''
        pass

class MnRigid:
    '''Class for wrapping N cloth objects.
This class wraps the internal Maya representation of N cloth
objects suitable for use with the Nucleus solver.
'''
    def __init__(self):
        pass


    def setTopology(self, numFaces: int,
                        numVertsPerFace: int,
                        faces: int,
                        numEdges: int,
                        edges: int): 
        '''
        setTopology(self, numFaces: int,
                        numVertsPerFace: int,
                        faces: int,
                        numEdges: int,
                        edges: int)

        Synopsis
        -----
        sets the topology of the underlying N Object. Before calling
        other methods, this must be the first method you call once the
        rigid object is created.

        Returns:
        -----
        None

        Parameters:
        -----
        numFaces: int
        	[in] -> number of faces 

        numVertsPerFace: int
        	[in] -> an array of size numFaces, where each element describes the number of verts on that face 

        faces: int
        	[in] -> an array containing the actual face description. Each element is a vertex index. 

        numEdges: int
        	[in] -> number of edges 

        edges: int
        	[in] -> an array containing the edge description. Each element is a vertex index.


        '''
        pass

    def createNRigid(self): 
        '''
        createNRigid(self)

        Synopsis
        -----
        Creates the underlying Maya TnRigid and sets this class to wrap
        it.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setPositions(self, positions: MFloatPointArray,
                        startFrame: bool): 
        '''
        setPositions(self, positions: MFloatPointArray,
                        startFrame: bool)

        Synopsis
        -----
        Sets the positions of the vertices of the underlying nRigid
        object.

        Returns:
        -----
        None

        Parameters:
        -----
        positions: MFloatPointArray
        	[in] -> the array containing the position information 

        startFrame: bool
        	[in] -> whether this information represents the state of the object at the start frame.


        '''
        pass

    def setVelocities(self, velocities: MFloatPointArray): 
        '''
        setVelocities(self, velocities: MFloatPointArray)

        Synopsis
        -----
        Sets the velocities of the vertices of the underlying nRigid
        object.

        Returns:
        -----
        None

        Parameters:
        -----
        velocities: MFloatPointArray
        	[in] -> the array containing the velocity information


        '''
        pass

    @overload
    def setThickness(self, radius: float): 
        '''
        setThickness(self, radius: float)

        Synopsis
        -----
        sets a radius on each point of the mesh for collision purposes.
        The bigger the radius/thickness, the more easily things collide.

        Returns:
        -----
        None

        Parameters:
        -----
        radius: float
        	[in] -> the radius to set


        '''
        pass

    @overload
    def setThickness(self, radius: float): 
        '''
        setThickness(self, radius: float)

        Synopsis
        -----
        sets a radius (thickness) on a per point basis for the mesh for
        collision purposes. The bigger the radius, the more easily things
        collide.

        Returns:
        -----
        None

        Parameters:
        -----
        radius: float
        	[in] -> the radius to set


        '''
        pass

    @overload
    def setBounce(self, bounce: float): 
        '''
        setBounce(self, bounce: float)

        Synopsis
        -----
        sets the bounce for every point in this mesh

        Returns:
        -----
        None

        Parameters:
        -----
        bounce: float
        	[in] -> value of bounce to set


        '''
        pass

    @overload
    def setBounce(self, bounce: float): 
        '''
        setBounce(self, bounce: float)

        Synopsis
        -----
        sets the bounce on a per point basis in this mesh

        Returns:
        -----
        None

        Parameters:
        -----
        bounce: float
        	[in] -> value of bounce to set


        '''
        pass

    @overload
    def setFriction(self, friction: float): 
        '''
        setFriction(self, friction: float)

        Synopsis
        -----
        sets the friction for every point in this mesh

        Returns:
        -----
        None

        Parameters:
        -----
        friction: float
        	[in] -> the friction to set


        '''
        pass

    @overload
    def setFriction(self, friction: float): 
        '''
        setFriction(self, friction: float)

        Synopsis
        -----
        sets the friction on a per point basis for this mesh

        Returns:
        -----
        None

        Parameters:
        -----
        friction: float
        	[in] -> the friction to set


        '''
        pass

    def setCollisionFlags(self, vertToVert: bool,
                        edgeToEdge: bool,
                        faceToFace: bool): 
        '''
        setCollisionFlags(self, vertToVert: bool,
                        edgeToEdge: bool,
                        faceToFace: bool)

        Synopsis
        -----
        Sets how (or if) this object will collide with other objects.

        Returns:
        -----
        None

        Parameters:
        -----
        vertToVert: bool
        	[in] -> whether to calculate vertex - vertex collisions 

        edgeToEdge: bool
        	[in] -> whether to calculate edge - edge collisions 

        faceToFace: bool
        	[in] -> whether to calculate face - face collisions


        '''
        pass

    def getNumVertices(self, numVerts: int): 
        '''
        getNumVertices(self, numVerts: int)

        Synopsis
        -----
        Returns the number of vertices in the underlying nRigid.

        Returns:
        -----
        None

        Parameters:
        -----
        numVerts: int
        	[out] -> Number of vertices.


        '''
        pass

    def getPositions(self, positions: MFloatPointArray): 
        '''
        getPositions(self, positions: MFloatPointArray)

        Synopsis
        -----
        gets the positions of the points of the underlying N Object.

        Returns:
        -----
        None

        Parameters:
        -----
        positions: MFloatPointArray
        	[out] -> the array will be filled with the positions.


        '''
        pass

    def getVelocities(self, velocities: MFloatPointArray): 
        '''
        getVelocities(self, velocities: MFloatPointArray)

        Synopsis
        -----
        gets the velocities of the points of the underlying nRigid
        object.

        Returns:
        -----
        None

        Parameters:
        -----
        velocities: MFloatPointArray
        	[out] -> the array will be filled with the positions.


        '''
        pass

    def getThickness(self, radius: MFloatArray): 
        '''
        getThickness(self, radius: MFloatArray)

        Synopsis
        -----
        gets the thickness at each point of the underlying N rigid
        object.

        Returns:
        -----
        None

        Parameters:
        -----
        radius: MFloatArray
        	[out] -> the array will be filled with the thickness.


        '''
        pass

    def getInverseMass(self, inverseMass: MFloatArray): 
        '''
        getInverseMass(self, inverseMass: MFloatArray)

        Synopsis
        -----
        gets the inverseMass at each point of the underlying N rigid
        object.

        Returns:
        -----
        None

        Parameters:
        -----
        inverseMass: MFloatArray
        	[out] -> the array will be filled with the inverse masses.


        '''
        pass

    def getBounce(self, bounce: MFloatArray): 
        '''
        getBounce(self, bounce: MFloatArray)

        Synopsis
        -----
        gets the bounce at each point of the underlying N rigid object.

        Returns:
        -----
        None

        Parameters:
        -----
        bounce: MFloatArray
        	[out] -> the array will be filled with the bounce.


        '''
        pass

    def getFriction(self, friction: MFloatArray): 
        '''
        getFriction(self, friction: MFloatArray)

        Synopsis
        -----
        gets the friction at each point of the underlying N rigid object.

        Returns:
        -----
        None

        Parameters:
        -----
        friction: MFloatArray
        	[out] -> the array will be filled with the friction.


        '''
        pass

    def setNRigid(self, nObj: MnRigid.TnRigid,
                        own: bool): 
        '''
        setNRigid(self, nObj: MnRigid.TnRigid,
                        own: bool)

        Synopsis
        -----
        Sets the TnRigid pointer which this class wraps. If own is true,
        then the TnRigid will be deleted when this class is destroyed.

        Returns:
        -----
        None

        Parameters:
        -----
        nObj: MnRigid.TnRigid
        	[in] -> 

        own: bool
        	[in] -> 


        '''
        pass

class MnSolver:
    '''Class for wrapping N solver objects.
This class wraps the internal Maya representation of a Nucleus
solver suitable for use with the Nucleus objects such as nCloth
or nParticles
'''
    def __init__(self):
        pass


    def createNSolver(self): 
        '''
        createNSolver(self)

        Synopsis
        -----
        Creates the underlying Maya solver object and sets this class to
        wrap it.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def addNObject(self, obj: MnObject): 
        '''
        addNObject(self, obj: MnObject)

        Synopsis
        -----
        Assign the nucleus object to be solved by this solver.

        Returns:
        -----
        None

        Parameters:
        -----
        obj: MnObject
        	[in] -> Nucleus object.


        '''
        pass

    def removeNObject(self, obj: MnObject): 
        '''
        removeNObject(self, obj: MnObject)

        Synopsis
        -----
        Remove the nucleus object from being solved by this solver.

        Returns:
        -----
        None

        Parameters:
        -----
        obj: MnObject
        	[in] -> Nucleus object.


        '''
        pass

    def setGravity(self, grav: float): 
        '''
        setGravity(self, grav: float)

        Synopsis
        -----
        Sets the gravity magnitude for the objects being solved. Note the
        the objects should already be added to the solver when applying
        gravity

        Returns:
        -----
        None

        Parameters:
        -----
        grav: float
        	[in] -> New gravity value.


        '''
        pass

    def setGravityDir(self, gravX: float,
                        gravY: float,
                        gravZ: float): 
        '''
        setGravityDir(self, gravX: float,
                        gravY: float,
                        gravZ: float)

        Synopsis
        -----
        Sets the gravity direction for the underlying Maya solver object.

        Returns:
        -----
        None

        Parameters:
        -----
        gravX: float
        	[in] -> X coordinate of new gravity direction. 

        gravY: float
        	[in] -> Y coordinate of new gravity direction. 

        gravZ: float
        	[in] -> Z coordinate of new gravity direction.


        '''
        pass

    def setAirDensity(self, dens: float): 
        '''
        setAirDensity(self, dens: float)

        Synopsis
        -----
        Sets the air Density for the solver.

        Returns:
        -----
        None

        Parameters:
        -----
        dens: float
        	[in] -> New density value.


        '''
        pass

    def setWindSpeed(self, speed: float): 
        '''
        setWindSpeed(self, speed: float)

        Synopsis
        -----
        Sets the wind magnitude for the underlying Maya solver object.

        Returns:
        -----
        None

        Parameters:
        -----
        speed: float
        	[in] -> New wind speed.


        '''
        pass

    def setWindDir(self, windX: float,
                        windY: float,
                        windZ: float): 
        '''
        setWindDir(self, windX: float,
                        windY: float,
                        windZ: float)

        Synopsis
        -----
        Sets the wind direction for the underlying Maya solver object.

        Returns:
        -----
        None

        Parameters:
        -----
        windX: float
        	[in] -> X coordinate of new wind direction. 

        windY: float
        	[in] -> Y coordinate of new wind direction. 

        windZ: float
        	[in] -> Z coordinate of new wind direction.


        '''
        pass

    def setWindNoiseIntensity(self, noise: float): 
        '''
        setWindNoiseIntensity(self, noise: float)

        Synopsis
        -----
        Sets the wind noise intensity for the underlying Maya solver
        object.

        Returns:
        -----
        None

        Parameters:
        -----
        noise: float
        	[in] -> New wind noise intensity.


        '''
        pass

    def setDisabled(self, disabled: bool): 
        '''
        setDisabled(self, disabled: bool)

        Synopsis
        -----
        Disables the solver - or re-enables it again.

        Returns:
        -----
        None

        Parameters:
        -----
        disabled: bool
        	[in] -> True to disable the solver, false to re-enable it.


        '''
        pass

    def setSubsteps(self, substeps: int): 
        '''
        setSubsteps(self, substeps: int)

        Synopsis
        -----
        Set the number of substeps used by the solver.

        Returns:
        -----
        None

        Parameters:
        -----
        substeps: int
        	[in] -> New number of substeps to use.


        '''
        pass

    def setMaxIterations(self, maxIter: int): 
        '''
        setMaxIterations(self, maxIter: int)

        Synopsis
        -----
        Set the max number of collision iterations used by the solver.

        Returns:
        -----
        None

        Parameters:
        -----
        maxIter: int
        	[in] -> New maximum number of iterations to use.


        '''
        pass

    def setStartTime(self, startTime: float): 
        '''
        setStartTime(self, startTime: float)

        Synopsis
        -----
        Sets the start Time in seconds for the solver.

        Returns:
        -----
        None

        Parameters:
        -----
        startTime: float
        	[in] -> New start time.


        '''
        pass

    def makeAllCollide(self): 
        '''
        makeAllCollide(self)

        Synopsis
        -----
        Allow all the objects assigned to the Maya solver object to
        collide.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def removeAllCollisions(self): 
        '''
        removeAllCollisions(self)

        Synopsis
        -----
        Remove the collisions between all the objects assigned to the
        Maya solver object.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def solve(self, solveTime: float): 
        '''
        solve(self, solveTime: float)

        Synopsis
        -----
        Solve from the last eval time until the specified time (in
        seconds).

        Returns:
        -----
        None

        Parameters:
        -----
        solveTime: float
        	[in] -> Time to solve up to.


        '''
        pass

class MDynamicsUtil:
    '''Utility class for Maya dynamics.
MDynamicsUtil provides utility methods related to Maya dynamics (eg. particles
and fluids).
'''
    def __init__(self):
        pass


    def hasValidDynamics2dTexture(self, node: MObject,
                        texAttr: MObject,
                        status: MDynamicsUtil.MStatus): 
        '''
        hasValidDynamics2dTexture(self, node: MObject,
                        texAttr: MObject,
                        status: MDynamicsUtil.MStatus) -> bool

        Synopsis
        -----
        Certain aspects of Maya's dynamics can be textured using 2d
        textures. For example, surface particle emitters can use a 2d
        texture to modulate the emission rate over the surface. For these
        purposes, only a subset of Maya's textures are supported, namely
        the default 2d textures (bulge, checker, cloth, file, fluid
        texture 2d, fractal, grid, mountain, movie, noise, ocean, ramp,
        water). No other nodes are supported. This method takes an
        attribute and determines if there is a supported texture
        connected to it. If the texture is supported, then the
        evalDynamics2dTexture() method can be called to evaluate the
        texture at various (u,v) coordinate values.

        Returns: 
        ----- 
        true if the node connected to the specified attribute is a
        texture that can be evaluated using the evalDynamics2dTexture()
        method, false otherwise.

        Parameters:
        -----
        node: MObject
        	[in] -> node to be tested for a valid texture connection. 

        texAttr: MObject
        	[in] -> attribute to be tested for a valid texture connection. 

        status: MDynamicsUtil.MStatus
        	[out] -> status code.


        '''
        pass

    def evalDynamics2dTexture(self, node: MObject,
                        texAttr: MObject,
                        uCoords: MDoubleArray,
                        vCoords: MDoubleArray,
                        resultColors: MVectorArray,
                        resultAlphas: MDoubleArray): 
        '''
        evalDynamics2dTexture(self, node: MObject,
                        texAttr: MObject,
                        uCoords: MDoubleArray,
                        vCoords: MDoubleArray,
                        resultColors: MVectorArray,
                        resultAlphas: MDoubleArray)

        Synopsis
        -----
        If a supported 2d texture (see hasValidDynamics2dTexture() method
        documentation) is connected to the specified attribute, this
        method can be called to evaluate that texture at a number of
        (u,v) texture coordinate values.

        Returns:
        -----
        None

        Parameters:
        -----
        node: MObject
        	[in] -> node whose connected texture is to be evaluated. 

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

    def inRunup(self): 
        '''
        inRunup(self) -> bool

        Synopsis
        -----
        Is Maya's dynamics system currently doing a runup?

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def runupIfRequired(self): 
        '''
        runupIfRequired(self) -> bool

        Synopsis
        -----
        If the dynamics runup prefs are set, do a runup.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def addNodeTypeToRunup(self, nodeTypeName: MString): 
        '''
        addNodeTypeToRunup(self, nodeTypeName: MString) -> bool

        Synopsis
        -----
        Add this node to the list of nodes participating in runup. The
        node should respond to timeChanged and delayedTimeChangedRunup
        messages, or have a forceDynamics attribute. The node should have
        lastEvalTime and lastCacheTime attributes to determine whether
        runup is needed. Optionally the node may have a boolean
        checkForRunup attribute that when false will fully disable runup
        checking.

        Returns: 
        ----- 
        true if the node was added to the list, false if it was already
        on the list

        Parameters:
        -----
        nodeTypeName: MString
        	[in] -> node type to be included in runup.


        '''
        pass

    def removeNodeTypeFromRunup(self, nodeTypeName: MString): 
        '''
        removeNodeTypeFromRunup(self, nodeTypeName: MString) -> bool

        Synopsis
        -----
        Remove this node from the list of nodes participating in runup.

        Returns: 
        ----- 
        true if the node was removed from the list, false if it was not
        on the list to start with

        Parameters:
        -----
        nodeTypeName: MString
        	[in] -> node type to be removed from runup.


        '''
        pass

class MDynSweptLine:
    '''Class for evaluating curve segments as lines over time.
A
MDynSweptLine provides access to a curve segment defined as a line. It can
only be accessed with the
MFnDynSweptGeometryData class that is provided as an output from the geoConnector node.
The class provides parametric time evaluation for a curve. Time
is in the range 0 to 1, where 1 represents the current frame and
0 represents the previous frame. In this way you can get
interpolated values of a curve in motion.
'''
    def __init__(self):
        pass


    def vertex(self, vertexId: int,
                        t: double): 
        '''
        vertex(self, vertexId: int,
                        t: double) -> MVector

        Synopsis
        -----
        Return the vertex requested by id, at the parametric time value.

        Returns: 
        ----- 
        The vertex position

        Parameters:
        -----
        vertexId: int
        	[in] -> index 0 or 1 

        t: double
        	[in] -> time value in the range 1.0 to 0.0 


        '''
        pass

    def normal(self, x: double,
                        y: double,
                        z: double,
                        t: double): 
        '''
        normal(self, x: double,
                        y: double,
                        z: double,
                        t: double) -> MVector

        Synopsis
        -----
        Given a parametric time specified by 't' and a vector, returns a
        normalized vector perpendicular to the tangent, and rotated into
        the plane defined by the tangent and vector argument.

        Returns: 
        ----- 
        A normalized vector

        Parameters:
        -----
        x: double
        	[in] -> x component of a vector 

        y: double
        	[in] -> y component of a vector 

        z: double
        	[in] -> z component of a vector 

        t: double
        	[in] -> time value in the range 1.0 to 0.0 


        '''
        pass

    def tangent(self, t: double): 
        '''
        tangent(self, t: double) -> MVector

        Synopsis
        -----
        Given a parametric time specified by 't', returns normalized
        tangent of the line.

        Returns: 
        ----- 
        A normalized vector

        Parameters:
        -----
        t: double
        	[in] -> time value in the range 1.0 to 0.0 


        '''
        pass

    def length(self, t: double): 
        '''
        length(self, t: double) -> double

        Synopsis
        -----
        Given a parametric time specified by 't', returns the total
        length of the line.

        Returns: 
        ----- 
        Total line length

        Parameters:
        -----
        t: double
        	[in] -> time value in the range 1.0 to 0.0 


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

class MDynSweptTriangle:
    '''Class for evaluating surfaces as triangles over time.
MDynSweptTriangle provides access to surfaces (Nurbs and Polys) defined as
triangles. It can only be accessed with the
MFnDynSweptGeometryData class that is provided as an output from the geoConnector node.
The class provides parametric time evaluation for a triangle.
Time is in the range 0 to 1, where 1 represents the current frame
and 0 represents the previous frame. In this way you can get
interpolated values of a triangle in motion.
'''
    def __init__(self):
        pass


    def vertex(self, vertexId: int,
                        t: double): 
        '''
        vertex(self, vertexId: int,
                        t: double) -> MVector

        Synopsis
        -----
        Return the vertex requested by id, at the parametric time value.

        Returns: 
        ----- 
        The vertex position.

        Parameters:
        -----
        vertexId: int
        	[in] -> index 0, 1, or 2 

        t: double
        	[in] -> time value in the range 1.0 to 0.0 


        '''
        pass

    def normal(self, t: double): 
        '''
        normal(self, t: double) -> MVector

        Synopsis
        -----
        Given a parametric time specified by 't', returns the normal of
        the triangle.

        Returns: 
        ----- 
        A normalized vector

        Parameters:
        -----
        t: double
        	[in] -> time value in the range 1.0 to 0.0 


        '''
        pass

    def normalToPoint(self, x: double,
                        y: double,
                        z: double,
                        t: double): 
        '''
        normalToPoint(self, x: double,
                        y: double,
                        z: double,
                        t: double) -> MVector

        Synopsis
        -----
        Given a point, returns the normal of the triangle in the
        direction towards the point. Determines which side of the
        triangle to return the normal.

        Returns: 
        ----- 
        A normalized vector

        Parameters:
        -----
        x: double
        	[in] -> x component of the point 

        y: double
        	[in] -> y component of the point 

        z: double
        	[in] -> z component of the point 

        t: double
        	[in] -> time value in the range 1.0 to 0.0 


        '''
        pass

    def uvPoint(self, vertexId: int): 
        '''
        uvPoint(self, vertexId: int) -> MVector

        Synopsis
        -----
        Given a vertex id, this method returns the UV point for the
        vertex as a MVector.

        Returns: 
        ----- 
        A vector. The u and v values are stored in the first two
        coordinates. The third coordinate is not meaningful.

        Parameters:
        -----
        vertexId: int
        	[in] -> Id of the vertex for retrieving the UV point.


        '''
        pass

    def area(self): 
        '''
        area(self) -> double

        Synopsis
        -----
        This method returns the area.

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

class MFnAirField:
    '''Function set for Air Fields.
Function set for creation, edit, and query of Air Fields.
An air field simulates the effects of moving air.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kAir.Reimplemented from MFnField.

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

    def direction(self, ReturnStatus: MFnAirField.MStatus): 
        '''
        direction(self, ReturnStatus: MFnAirField.MStatus) -> MVector

        Synopsis
        -----
        Returns the direction the air is blowing.

        Returns: 
        ----- 
        A vector representing direction.

        Parameters:
        -----
        ReturnStatus: MFnAirField.MStatus
        	[out] -> Status code


        '''
        pass

    def setDirection(self, airDirection: MVector): 
        '''
        setDirection(self, airDirection: MVector)

        Synopsis
        -----
        Sets the direction vector for the air to blow.

        Returns:
        -----
        None

        Parameters:
        -----
        airDirection: MVector
        	[in] -> A vector representing direction.


        '''
        pass

    def speed(self, ReturnStatus: MFnAirField.MStatus): 
        '''
        speed(self, ReturnStatus: MFnAirField.MStatus) -> double

        Synopsis
        -----
        Returns the control setting on how quickly objects match the
        velocity of the air field.

        Returns: 
        ----- 
        The value of the speed setting.

        Parameters:
        -----
        ReturnStatus: MFnAirField.MStatus
        	[out] -> Status code


        '''
        pass

    def setSpeed(self, value: double): 
        '''
        setSpeed(self, value: double)

        Synopsis
        -----
        Sets the control setting on how quickly the objects match the
        velocity of the air field.

        Returns:
        -----
        None

        Parameters:
        -----
        value: double
        	[in] -> A value representing speed. 


        '''
        pass

    def inheritVelocity(self, ReturnStatus: MFnAirField.MStatus): 
        '''
        inheritVelocity(self, ReturnStatus: MFnAirField.MStatus) -> double

        Synopsis
        -----
        Returns the amount of the moving air field's velocity that is
        added to the direction and magnitude of the wind.

        Returns: 
        ----- 
        A value from 0 to 1 representing the amount of velocity added.

        Parameters:
        -----
        ReturnStatus: MFnAirField.MStatus
        	[out] -> Status code


        '''
        pass

    def setInheritVelocity(self, velocity: double): 
        '''
        setInheritVelocity(self, velocity: double)

        Synopsis
        -----
        Sets the amount of the moving air field's velocity that is added
        to the direction and magnitude of the wind.

        Returns:
        -----
        None

        Parameters:
        -----
        velocity: double
        	[in] -> A value from 0 to 1 representing the amount of velocity that is added.


        '''
        pass

    def inheritRotation(self, ReturnStatus: MFnAirField.MStatus): 
        '''
        inheritRotation(self, ReturnStatus: MFnAirField.MStatus) -> bool

        Synopsis
        -----
        Returns true if the air field is rotating or parented to a
        rotating object, and will undergo that same rotation.

        Returns: 
        ----- 
        true Rotations will change the direction the air field points.
        false Rotations do not change the air field direction.

        Parameters:
        -----
        ReturnStatus: MFnAirField.MStatus
        	[out] -> Status code


        '''
        pass

    def setInheritRotation(self, enable: bool): 
        '''
        setInheritRotation(self, enable: bool)

        Synopsis
        -----
        Enables the air field to undergo rotations and effect the
        direction that the air field points.

        Returns:
        -----
        None

        Parameters:
        -----
        enable: bool
        	[in] -> Flag to enable or disable rotations effects.


        '''
        pass

    def componentOnly(self, ReturnStatus: MFnAirField.MStatus): 
        '''
        componentOnly(self, ReturnStatus: MFnAirField.MStatus) -> bool

        Synopsis
        -----
        Returns true if the air field will apply force only in the
        direction specified by the combination of its direction, speed,
        and inherit velocity attributes. Returns false if the force is
        made to effect the object's velocity to match the air field's
        velocity.

        Returns: 
        ----- 
        true Force applied only in direction of attributes.  false Force
        applied to match velocities.

        Parameters:
        -----
        ReturnStatus: MFnAirField.MStatus
        	[out] -> Status code


        '''
        pass

    def setComponentOnly(self, enable: bool): 
        '''
        setComponentOnly(self, enable: bool)

        Synopsis
        -----
        Enables the air field to apply force specified as a combination
        of its direction, speed, and inherit veloicty attributes.

        Returns:
        -----
        None

        Parameters:
        -----
        enable: bool
        	[in] -> Flag to enable or disable combination of attributes.


        '''
        pass

    def spread(self, ReturnStatus: MFnAirField.MStatus): 
        '''
        spread(self, ReturnStatus: MFnAirField.MStatus) -> double

        Synopsis
        -----
        Returns a value that represents an angle which objects are
        affected by the air fields direction setting. This value is taken
        into account when the Enable Spread attribute is turned on.

        Returns: 
        ----- 
        A value from 0 to 1 representing an angle.  A value of 0 effects
        objects only exactly in front of the direction vector.  A value
        of 1 effects objects in front by 180 degrees along the direction
        vector.

        Parameters:
        -----
        ReturnStatus: MFnAirField.MStatus
        	[out] -> Status code


        '''
        pass

    def setSpread(self, value: double): 
        '''
        setSpread(self, value: double)

        Synopsis
        -----
        Sets the value representing an angle which objects are affected
        by the air fields direction setting. This value is taken into
        account when the Enable Spread attribute is turned on.

        Returns:
        -----
        None

        Parameters:
        -----
        value: double
        	[in] -> A value representing an angle. 


        '''
        pass

    def enableSpread(self, ReturnStatus: MFnAirField.MStatus): 
        '''
        enableSpread(self, ReturnStatus: MFnAirField.MStatus) -> bool

        Synopsis
        -----
        Returns true if the air field is using the spread angle to define
        the influence of the air field.

        Returns: 
        ----- 
        true Objects are affected in the area of the spread angle.  false
        Objects are affected by the max distance setting.

        Parameters:
        -----
        ReturnStatus: MFnAirField.MStatus
        	[out] -> Status code


        '''
        pass

    def setEnableSpread(self, enable: bool): 
        '''
        setEnableSpread(self, enable: bool)

        Synopsis
        -----
        Enables the air field to influence objects based on the spread
        angle setting.

        Returns:
        -----
        None

        Parameters:
        -----
        enable: bool
        	[in] -> Flag to enable or disable use of the spread angle.


        '''
        pass

class MFnDragField:
    '''Function set for Drag Fields.
Function set for creation, edit, and query of Drag Fields.
A drag field exerts a friction, or braking force, proportional to
the speed of a moving object.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kDrag.Reimplemented from MFnField.

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

    def direction(self, ReturnStatus: MFnDragField.MStatus): 
        '''
        direction(self, ReturnStatus: MFnDragField.MStatus) -> MVector

        Synopsis
        -----
        Returns the direction of the drag force's influence along the x,
        y, and z axes. You must have the Use Direction setting turned on
        for this attribute to take effect.

        Returns: 
        ----- 
        A vector representing direction.

        Parameters:
        -----
        ReturnStatus: MFnDragField.MStatus
        	[out] -> Status code


        '''
        pass

    def setDirection(self, dragDirection: MVector): 
        '''
        setDirection(self, dragDirection: MVector)

        Synopsis
        -----
        Sets the direction of the drag force's influence along the x, y,
        and z axes. You must have the Use Direction setting turned on for
        this attribute to take effect.

        Returns:
        -----
        None

        Parameters:
        -----
        dragDirection: MVector
        	[in] -> A vector representing direction.


        '''
        pass

    def useDirection(self, ReturnStatus: MFnDragField.MStatus): 
        '''
        useDirection(self, ReturnStatus: MFnDragField.MStatus) -> bool

        Synopsis
        -----
        Returns true if the braking force is exerted only against the
        component of the object's velocity that lies along the direction
        of the drag force.

        Returns: 
        ----- 
        true Use the direction setting to determine the braking force.
        false Use the objects velocity to determine the braking force.

        Parameters:
        -----
        ReturnStatus: MFnDragField.MStatus
        	[out] -> Status code


        '''
        pass

    def setUseDirection(self, enable: bool): 
        '''
        setUseDirection(self, enable: bool)

        Synopsis
        -----
        Enables the braking force to be exerted only against the
        component of the object's velocity that lies along the direction
        setting of the drag force.

        Returns:
        -----
        None

        Parameters:
        -----
        enable: bool
        	[in] -> Flag to enable or disable direction setting.


        '''
        pass

class MFnDynSweptGeometryData:
    '''Swept Geometry function set for dependency node data.
MFnDynSweptGeometryData provides access to the
MDynSweptLine and
MDynSweptTriangle data for use in a user defined dependency graph node. The data
is provided as an output from the geoConnector node and is
primarily used to determine positional information over time.
If a user written dependency node accepts
MFnDynSweptGeometryData, then this class is used to extract data that comes from the
geoConnector node. The
MDataHandle::type method will return kDynSweptGeometry when data of this type is
present. To access it, the
MDataHandle::data() method is used to get an
MObject for the data and this should then be used to initialize an
instance of
MFnDynSweptGeometryData.
Important note: Users can create the data for connections but
cannot produce the contents of the data as this is reserved for
the Maya Dynamics internals.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kDynSweptGeometryData.Reimplemented from MFnData.

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
        "MFnDynSweptGeometryData".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def lineCount(self, ReturnStatus: MFnDynSweptGeometryData.MStatus): 
        '''
        lineCount(self, ReturnStatus: MFnDynSweptGeometryData.MStatus) -> int

        Synopsis
        -----
        Return the number of line segments contained in the data.

        Returns: 
        ----- 
        Number of line segments

        Parameters:
        -----
        ReturnStatus: MFnDynSweptGeometryData.MStatus
        	[out] -> kFailure if the instance is not attached to an 


        '''
        pass

    def triangleCount(self, ReturnStatus: MFnDynSweptGeometryData.MStatus): 
        '''
        triangleCount(self, ReturnStatus: MFnDynSweptGeometryData.MStatus) -> int

        Synopsis
        -----
        Return the number of triangles contained in the data.

        Returns: 
        ----- 
        Number of triangles

        Parameters:
        -----
        ReturnStatus: MFnDynSweptGeometryData.MStatus
        	[out] -> kFailure if the instance is not attached to an 


        '''
        pass

    def sweptLine(self, index: int,
                        ReturnStatus: MFnDynSweptGeometryData.MStatus): 
        '''
        sweptLine(self, index: int,
                        ReturnStatus: MFnDynSweptGeometryData.MStatus) -> MDynSweptLine

        Synopsis
        -----
        Return data for a swept line.

        Returns: 
        ----- 
        A const reference to the MDynSweptLine

        Parameters:
        -----
        index: int
        	[in] -> Index of the swept line to return data for. Must be in the range 0 to (

        ReturnStatus: MFnDynSweptGeometryData.MStatus
        	[out] -> kFailure if the instance is not attached to an 


        '''
        pass

    def sweptTriangle(self, index: int,
                        ReturnStatus: MFnDynSweptGeometryData.MStatus): 
        '''
        sweptTriangle(self, index: int,
                        ReturnStatus: MFnDynSweptGeometryData.MStatus) -> MDynSweptTriangle

        Synopsis
        -----
        Return data for a swept triangle.

        Returns: 
        ----- 
        A const reference to the MDynSweptTriangle

        Parameters:
        -----
        index: int
        	[in] -> Index of the swept triangle to return data for. Must be in the range 0 to (

        ReturnStatus: MFnDynSweptGeometryData.MStatus
        	[out] -> kFailure if the instance is not attached to an 


        '''
        pass

    def create(self, ReturnStatus: MFnDynSweptGeometryData.MStatus): 
        '''
        create(self, ReturnStatus: MFnDynSweptGeometryData.MStatus) -> MObject

        Synopsis
        -----
        This method create a new swept geometry data object for use with
        the dependency graph.

        Returns: 
        ----- 
        A handle to the new swept geometry data object

        Parameters:
        -----
        ReturnStatus: MFnDynSweptGeometryData.MStatus
        	[out] -> return status


        '''
        pass

class MFnField:
    '''Function set for Dynamic Fields.
Function set for creation, edit, and query of Dynamic Fields.
There are several types of dynamic fields: Air, Drag, Gravity,
Newton Radial, Turbulence, Uniform, and Vortex.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kField.Reimplemented from MFnDagNode.Reimplemented in
        MFnDragField, MFnNewtonField, MFnRadialField, MFnVortexField,
        MFnGravityField, MFnTurbulenceField, MFnUniformField,
        MFnVolumeAxisField, and MFnAirField.

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
    def getForceAtPoint(self, point: MPointArray,
                        velocity: MVectorArray,
                        mass: MDoubleArray,
                        force: MVectorArray,
                        deltaTime: double): 
        '''
        getForceAtPoint(self, point: MPointArray,
                        velocity: MVectorArray,
                        mass: MDoubleArray,
                        force: MVectorArray,
                        deltaTime: double)

        Synopsis
        -----
        Compute the force of a field on an array of points, given their
        position, velocity, and mass. Note that only the Air and Vortex
        fields require a time increment to compute forces, all other
        fields will ignore this argument.This method uses MPointArray to
        represent the positions of points. If a point instance is in a
        rational form or a homogenous form, you should reset it to be in
        the cartesian form P(x, y, z, 1).

        Returns:
        -----
        None

        Parameters:
        -----
        point: MPointArray
        	[in] -> array of positions for each point. 

        velocity: MVectorArray
        	[in] -> array of velocities for each point. If the length of the velocity array is 0, a velocity of 0.0 is assumed for all the points. Note the velocity array is a requirement for the Air and Drag fields to compute forces. 

        mass: MDoubleArray
        	[in] -> array of mass values for each point. If the length of the mass array is 0, a mass of 1.0 is assumed for all the points. 

        force: MVectorArray
        	[out] -> output array of forces applied to each point. If the length of the force array supplied is 0, the array is automatically resized. If the contents of the force array contains data, the computed force is added to the supplied data. This can be useful to accumulate forces of multiple fields. 

        deltaTime: double
        	[in] -> time increment in seconds for usage with the Air and Vortex fields. Default is (1.0 / 24.0 fps).


        '''
        pass

    @overload
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
        Compute the force of a field on an array of points, given their
        position, velocity, and mass. Note that only the Air and Vortex
        fields require a time increment to compute forces, all other
        fields will igonore this argument.This method uses MVectorArray
        to represent the positions of a point.

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
        	[in] -> time increment in seconds for usage with the Air and Vortex fields. Default is (1.0 / 24.0 fps).


        '''
        pass

    def magnitude(self, ReturnStatus: MFnField.MStatus): 
        '''
        magnitude(self, ReturnStatus: MFnField.MStatus) -> double

        Synopsis
        -----
        Returns the strength of the field.

        Returns: 
        ----- 
        A value representing the strength of the field.

        Parameters:
        -----
        ReturnStatus: MFnField.MStatus
        	[out] -> Status code


        '''
        pass

    def setMagnitude(self, mag: double): 
        '''
        setMagnitude(self, mag: double)

        Synopsis
        -----
        Sets the strength of the field.

        Returns:
        -----
        None

        Parameters:
        -----
        mag: double
        	[in] -> A value representing the strength of the field.


        '''
        pass

    def attenuation(self, ReturnStatus: MFnField.MStatus): 
        '''
        attenuation(self, ReturnStatus: MFnField.MStatus) -> double

        Synopsis
        -----
        Returns the rate of change where the strength of the field
        changes as the distance between the field and the affected object
        increases.

        Returns: 
        ----- 
        A positive value representing the exponent for rate of change.  A
        value of 0 and the force remains constant over distance.

        Parameters:
        -----
        ReturnStatus: MFnField.MStatus
        	[out] -> Status code


        '''
        pass

    def setAttenuation(self, atten: double): 
        '''
        setAttenuation(self, atten: double)

        Synopsis
        -----
        Sets the rate of change where the strength of the field changes
        as the distance between the field and the affected object
        increases.

        Returns:
        -----
        None

        Parameters:
        -----
        atten: double
        	[in] -> A positive value representing the exponent for rate of change. A value of 0 and the force remains constant over distance.


        '''
        pass

    def maxDistance(self, ReturnStatus: MFnField.MStatus): 
        '''
        maxDistance(self, ReturnStatus: MFnField.MStatus) -> double

        Synopsis
        -----
        Returns the maximum distance from the field at which the force of
        the field is exerted. The Use Max Distance setting must be turned
        on for maximum distance to take effect. The maximum distance is
        scaled by the falloff curve's non-zero range.

        Returns: 
        ----- 
        A value representing distance in internal linear units.

        Parameters:
        -----
        ReturnStatus: MFnField.MStatus
        	[out] -> Status code


        '''
        pass

    def setMaxDistance(self, dist: double): 
        '''
        setMaxDistance(self, dist: double)

        Synopsis
        -----
        Sets the maximum distance from the field at which the force of
        the field is exerted. The Use Max Distance setting must be turned
        on for maximum distance to take effect.

        Returns:
        -----
        None

        Parameters:
        -----
        dist: double
        	[in] -> A value representing distance in internal linear units.


        '''
        pass

    def perVertex(self, ReturnStatus: MFnField.MStatus): 
        '''
        perVertex(self, ReturnStatus: MFnField.MStatus) -> bool

        Synopsis
        -----
        Returns true if the field exerts its force on each individual
        point (cv, particle, vertex) equally. Returns false if the force
        is exerted only from the geometric center of the object or set of
        points.

        Returns: 
        ----- 
        true Force is applied to each individual point.  false Force is
        applied from the geometric center.

        Parameters:
        -----
        ReturnStatus: MFnField.MStatus
        	[out] -> Status code


        '''
        pass

    def setPerVertex(self, enable: bool): 
        '''
        setPerVertex(self, enable: bool)

        Synopsis
        -----
        Enables the field to exert its force on each individual point
        (cv, particle, vertex) equally. Otherwise, the force is exerted
        only from the geometric center of the object or set of points.

        Returns:
        -----
        None

        Parameters:
        -----
        enable: bool
        	[in] -> Flag to enable or disable individual point forces.


        '''
        pass

    def useMaxDistance(self, ReturnStatus: MFnField.MStatus): 
        '''
        useMaxDistance(self, ReturnStatus: MFnField.MStatus) -> bool

        Synopsis
        -----
        Returns true if the field will use the maximum distance setting
        to determine the area of influence.

        Returns: 
        ----- 
        true Field uses the maximum distance setting.  false Field
        ignores the maximum distance setting.

        Parameters:
        -----
        ReturnStatus: MFnField.MStatus
        	[out] -> Status code


        '''
        pass

    def setUseMaxDistance(self, enable: bool): 
        '''
        setUseMaxDistance(self, enable: bool)

        Synopsis
        -----
        Enables the field to use the maximum distance setting to
        determine the area of influence.

        Returns:
        -----
        None

        Parameters:
        -----
        enable: bool
        	[in] -> Flag to enable or disable maximum distance.


        '''
        pass

    def falloffCurve(self, param: double,
                        ReturnStatus: MFnField.MStatus): 
        '''
        falloffCurve(self, param: double,
                        ReturnStatus: MFnField.MStatus) -> double

        Synopsis
        -----
        Returns falloff given the param in [0,1]. This is enabled if the
        use the maximum distance is enabled.

        Returns: 
        ----- 
        The falloff value given the param.

        Parameters:
        -----
        param: double
        	[in] -> Parameter 

        ReturnStatus: MFnField.MStatus
        	[out] -> Status code


        '''
        pass

    def isFalloffCurveConstantOne(self, ReturnStatus: MFnField.MStatus): 
        '''
        isFalloffCurveConstantOne(self, ReturnStatus: MFnField.MStatus) -> bool

        Synopsis
        -----
        Returns true if falloffCurve is a constant one (default) or false
        if not.

        Returns: 
        ----- 
        If falloff curve always returns a constant one

        Parameters:
        -----
        ReturnStatus: MFnField.MStatus
        	[out] -> Status code


        '''
        pass

class MFnFluid:
    '''Fluid node function set.
This is the function set for fluid objects.
A fluid object is a node in the dependency graph that contains a
grid which is made up of cells. Each cell has a variety of values
assigned to it such as density, velocity, temperature, and color.
The grid may be 2D or 3D. See the methods below for full details.
Fluid objects may be used for simulation purposes. This function
set allows read and write access to the values in the cells of
the fluid object.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kFluid.Reimplemented from MFnDagNode.

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
        className(self) -> MFnFluid.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnFluid".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def create3D(self, Xres: int,
                        Yres: int,
                        Zres: int,
                        Xdim: double,
                        Ydim: double,
                        Zdim: double,
                        parent: MObject,
                        ReturnStatus: MFnFluid.MStatus): 
        '''
        create3D(self, Xres: int,
                        Yres: int,
                        Zres: int,
                        Xdim: double,
                        Ydim: double,
                        Zdim: double,
                        parent: MObject,
                        ReturnStatus: MFnFluid.MStatus) -> MObject

        Synopsis
        -----
        Creates a fluid object from the specified data and sets this
        function set to operate on the new fluid object. The parent
        argument is used to specify the DAG parent of the new fluid. If
        parent is NULL then a new transform will be created and returned
        which will be the parent for the new fluid shape. The new
        transform will be added to the DAG.If parent is a DAG node then
        the new fluid will be returned and the parent passed in will
        become the new node's parent.

        Returns: 
        ----- 
        If parent is NULL then the transform for this fluid shape is
        returned  If parent is a DAG object then the new fluid shape is
        returned

        Parameters:
        -----
        Xres: int
        	[in] -> number of fluid grid cells in the x dimension 

        Yres: int
        	[in] -> number of fluid grid cells in the y dimension 

        Zres: int
        	[in] -> number of fluid grid cells in the z dimension 

        Xdim: double
        	[in] -> object space size in the x dimension 

        Ydim: double
        	[in] -> object space size in the y dimension 

        Zdim: double
        	[in] -> object space size in the z dimension 

        parent: MObject
        	[in] -> specifies what to do with the new fluid object. If a DAG object or NULL is given then a transform will be created for the new fluid shape and placed under the specified (optional)parent. 

        ReturnStatus: MFnFluid.MStatus
        	[out] -> Status code


        '''
        pass

    def create2D(self, Xres: int,
                        Yres: int,
                        Xdim: double,
                        Ydim: double,
                        parent: MObject,
                        ReturnStatus: MFnFluid.MStatus): 
        '''
        create2D(self, Xres: int,
                        Yres: int,
                        Xdim: double,
                        Ydim: double,
                        parent: MObject,
                        ReturnStatus: MFnFluid.MStatus) -> MObject

        Synopsis
        -----
        Creates a fluid object from the specified data and sets this
        function set to operate on the new fluid object. The parent
        argument is used to specify the DAG parent of the new fluid. If
        parent is NULL then a new transform will be created and returned
        which will be the parent for the new fluid shape. The new
        transform will be added to the DAG.If parent is a DAG node then
        the new fluid will be returned and the parent passed in will
        become the new node's parent.

        Returns: 
        ----- 
        If parent is NULL then the transform for this fluid shape is
        returned  If parent is a DAG object then the new fluid shape is
        returned

        Parameters:
        -----
        Xres: int
        	[in] -> number of fluid grid cells in the x dimension 

        Yres: int
        	[in] -> number of fluid grid cells in the y dimension 

        Xdim: double
        	[in] -> object space size in the x dimension 

        Ydim: double
        	[in] -> object space size in the y dimension 

        parent: MObject
        	[in] -> specifies what to do with the new fluid object. If a DAG object or NULL is given then a transform will be created for the new fluid shape and placed under the specified (optional)parent. 

        ReturnStatus: MFnFluid.MStatus
        	[out] -> Status code


        '''
        pass

    @overload
    def getResolution(self, Xres: int,
                        Yres: int,
                        Zres: int): 
        '''
        getResolution(self, Xres: int,
                        Yres: int,
                        Zres: int)

        Synopsis
        -----
        Gets the resolution of the fluid. The resolution gives the number
        of cells in the fluid grid in each direction.

        Returns:
        -----
        None

        Parameters:
        -----
        Xres: int
        	[out] -> storage for returning the number of fluid grid cells in the x dimension 

        Yres: int
        	[out] -> storage for returning the number of fluid grid cells in the y dimension 

        Zres: int
        	[out] -> storage for returning the number of fluid grid cells in the z dimension


        '''
        pass

    @overload
    def getResolution(self, Xres: int,
                        Yres: int): 
        '''
        getResolution(self, Xres: int,
                        Yres: int)

        Synopsis
        -----
        Gets the resolution of the fluid. The resolution gives the number
        of cells in the fluid grid in each direction.

        Returns:
        -----
        None

        Parameters:
        -----
        Xres: int
        	[out] -> storage for returning the number of fluid grid cells in the x dimension 

        Yres: int
        	[out] -> storage for returning the number of fluid grid cells in the y dimension


        '''
        pass

    def getDimensions(self, Xdim: double,
                        Ydim: double,
                        Zdim: double): 
        '''
        getDimensions(self, Xdim: double,
                        Ydim: double,
                        Zdim: double)

        Synopsis
        -----
        Gets the dimensions of the fluid. The dimensions give the object
        space size of the fluid object in each direction.

        Returns:
        -----
        None

        Parameters:
        -----
        Xdim: double
        	[out] -> storage for returning the dimension of the fluid in x 

        Ydim: double
        	[out] -> storage for returning the dimension of the fluid in y 

        Zdim: double
        	[out] -> storage for returning the dimension of the fluid in z


        '''
        pass

    @overload
    def setSize(self, Xres: int,
                        Yres: int,
                        Zres: int,
                        Xdim: double,
                        Ydim: double,
                        Zdim: double,
                        resample: bool): 
        '''
        setSize(self, Xres: int,
                        Yres: int,
                        Zres: int,
                        Xdim: double,
                        Ydim: double,
                        Zdim: double,
                        resample: bool)

        Synopsis
        -----
        Sets the size and resolution of the grid. The resolution
        parameters control the number of cells in the fluid grid and the
        dimension parameters set the size of the fluid shape in object
        space.

        Returns:
        -----
        None

        Parameters:
        -----
        Xres: int
        	[in] -> number of fluid grid cells in the x dimension 

        Yres: int
        	[in] -> number of fluid grid cells in the y dimension 

        Zres: int
        	[in] -> number of fluid grid cells in the z dimension 

        Xdim: double
        	[in] -> object space size in the x dimension 

        Ydim: double
        	[in] -> object space size in the y dimension 

        Zdim: double
        	[in] -> object space size in the z dimension 

        resample: bool
        	[in] -> true if the previous contents of the grid should be scaled to fit the new size by resampling the previous data at the new resolution


        '''
        pass

    @overload
    def setSize(self, Xres: int,
                        Yres: int,
                        Xdim: double,
                        Ydim: double,
                        resample: bool): 
        '''
        setSize(self, Xres: int,
                        Yres: int,
                        Xdim: double,
                        Ydim: double,
                        resample: bool)

        Synopsis
        -----
        Sets the size and resolution of the grid. The resolution
        parameters control the number of cells in the fluid grid and the
        dimension parameters set the size of the fluid shape in object
        space.

        Returns:
        -----
        None

        Parameters:
        -----
        Xres: int
        	[in] -> number of fluid grid cells in the x dimension 

        Yres: int
        	[in] -> number of fluid grid cells in the y dimension 

        Xdim: double
        	[in] -> object space size in the x dimension 

        Ydim: double
        	[in] -> object space size in the y dimension 

        resample: bool
        	[in] -> true if the previous contents of the grid should be scaled to fit the new size by resampling the previous data at the new resolution


        '''
        pass

    def gridSize(self, ReturnStatus: MFnFluid.MStatus): 
        '''
        gridSize(self, ReturnStatus: MFnFluid.MStatus) -> int

        Synopsis
        -----
        Returns the number of elements in the grid. This is equal to (x
        resolution * y resolution * z resolution). This routine is
        provided as a convenience to be used with the methods that give
        direct access to the fluid data. This gives the upper bound on
        the arrays. This size applies to all grids except for the 3
        velocity grids.

        Returns: 
        ----- 
        The number of elements.

        Parameters:
        -----
        ReturnStatus: MFnFluid.MStatus
        	[out] -> Status code.


        '''
        pass

    def velocityGridSizes(self, xsize: int,
                        ysize: int,
                        zsize: int): 
        '''
        velocityGridSizes(self, xsize: int,
                        ysize: int,
                        zsize: int)

        Synopsis
        -----
        Returns the number of elements in the velocity grids. X velocity
        size = (x resolution+1 * y resolution * z resolution). Y velocity
        size = (x resolution * y resolution+1 * z resolution). Z velocity
        size = (x resolution * y resolution * z resolution+1).This
        routine is provided as a convenience to be used with the methods
        that give direct access to the velocity grids.

        Returns:
        -----
        None

        Parameters:
        -----
        xsize: int
        	[out] -> storage for the x velocity grid size 

        ysize: int
        	[out] -> storage for the y velocity grid size 

        zsize: int
        	[out] -> storage for the z velocity grid size


        '''
        pass

    def falloff(self, ReturnStatus: MFnFluid.MStatus): 
        '''
        falloff(self, ReturnStatus: MFnFluid.MStatus) -> float*

        Synopsis
        -----
        This method returns a pointer to the storage for the falloff data
        in the fluid. The size of this array can be obtained using the
        "gridSize" call.The returned pointer points to an array of float
        values, each one representing the falloff value in a cell of the
        fluid grid. To get the array index corresponding to a cell index
        (x,y,z), use the "index" helper method.If you modify the data via
        the pointer returned, you must call the "updateGrid" call or you
        will not see your changes.Values from the falloff grid are used
        when the fluid's Falloff Shape attribute is set to "Grid". This
        mode allows users to specify arbitrary falloff values between 0
        and 1 at each grid cell. At render time, the shaded opacity
        values of the fluid will be multiplied by the interpolated
        falloff grid value raised to the power of 1/(1-ed), where "ed" is
        the value of the fluid's "edgeDropoff" attribute. When
        edgeDropoff=0, the opacity multiplier is 1, and when edgeDropoff
        is 1, the opacity multiplier is 0. Assuming that falloff grid
        values are in the range [0,1], raising the edge dropoff value
        from 0 to 1 will cause the fluid opacity to smoothly fall off
        towards complete transparency.

        Returns: 
        ----- 
        Pointer to the float data of the grid

        Parameters:
        -----
        ReturnStatus: MFnFluid.MStatus
        	[out] -> Status code


        '''
        pass

    def density(self, ReturnStatus: MFnFluid.MStatus): 
        '''
        density(self, ReturnStatus: MFnFluid.MStatus) -> float*

        Synopsis
        -----
        This method returns a pointer to the storage for the density data
        in the fluid. The size of this array can be obtained using the
        "gridSize" call.The pointer returned points to an array of float
        values, each one representing the density value in a cell of the
        fluid grid. To get the index of in the array for a cell at a
        given (x, y, z) use the "index" helper method.If you modify the
        data via the pointer returned, you must call the "updateGrid"
        call or you will not see your changes.

        Returns: 
        ----- 
        Pointer to the density data of the grid

        Parameters:
        -----
        ReturnStatus: MFnFluid.MStatus
        	[out] -> Status code


        '''
        pass

    def getVelocity(self, Xvel: float,
                        Yvel: float,
                        Zvel: float): 
        '''
        getVelocity(self, Xvel: float,
                        Yvel: float,
                        Zvel: float)

        Synopsis
        -----
        This method returns pointers to the storage for the velocity data
        in the fluid. The size of these arrays can be obtained using the
        "velocityGridSizes" call.Each of the pointers returned points to
        an array of float values, each value representing the velocity in
        a cell of the fluid grid . The three arrays contain the x
        components, y components, and z components of the velocity
        respectively.The grid sizes are different for each of the
        velocity grids. The Xvel grid is one larger in X, the Yvel in Y,
        the Zvel in Z. This is because the velocity components are stored
        at the voxel face centers, not at the voxel centers. The index
        methods that specify the resolutions explicitly should be used
        for the velocity grids.If you modify the data via the pointers
        returned, you must call the "updateGrid" call or you will not see
        your changes.

        Returns:
        -----
        None

        Parameters:
        -----
        Xvel: float
        	[out] -> storage for returning a pointer to the x components of the velocity values in the grid 

        Yvel: float
        	[out] -> storage for returning a pointer to the y components of the velocity values in the grid 

        Zvel: float
        	[out] -> storage for returning a pointer to the z components of the velocity values in the grid


        '''
        pass

    def pressure(self, ReturnStatus: MFnFluid.MStatus): 
        '''
        pressure(self, ReturnStatus: MFnFluid.MStatus) -> float*

        Synopsis
        -----
        This method returns a pointer to the storage for the pressure
        data in the fluid. The size of this array can be obtained using
        the "gridSize" call. Note that the pressure data only exists if
        the velocity method is kStaticGrid or kDynamicGridThe pointer
        returned points to an array of float values, each one
        representing the pressure value in a cell of the fluid grid. To
        get the index of in the array for a cell at a given (x, y, z) use
        the "index" helper method.If you modify the data via the pointer
        returned, you must call the "updateGrid" call or you will not see
        your changes. Note that the pressure data is an output of the
        velocity calculation. if you modify the pressure grid and the
        velocity grid is dynamic, your changes will be replaced after the
        next fluid evaluation.

        Returns: 
        ----- 
        Pointer to the pressure data of the grid

        Parameters:
        -----
        ReturnStatus: MFnFluid.MStatus
        	[out] -> Status code


        '''
        pass

    def temperature(self, ReturnStatus: MFnFluid.MStatus): 
        '''
        temperature(self, ReturnStatus: MFnFluid.MStatus) -> float*

        Synopsis
        -----
        This method returns a pointer to the storage for the temperature
        data in the fluid. The size of this array can be obtained using
        the "gridSize" call.The pointer returned points to an array of
        float values, each one representing the temperature value in a
        cell of the fluid grid. To get the index of in the array for a
        cell at a given (x, y, z) use the "index" helper method.If you
        modify the data via the pointer returned, you must call the
        "updateGrid" call or you will not see your changes.

        Returns: 
        ----- 
        Pointer to the temperature data of the grid

        Parameters:
        -----
        ReturnStatus: MFnFluid.MStatus
        	[out] -> Status code


        '''
        pass

    def fuel(self, ReturnStatus: MFnFluid.MStatus): 
        '''
        fuel(self, ReturnStatus: MFnFluid.MStatus) -> float*

        Synopsis
        -----
        This method returns a pointer to the storage for the fuel data in
        the fluid. The size of this array can be obtained using the
        "gridSize" call.The pointer returned points to an array of float
        values, each one representing the fuel value in a cell of the
        fluid grid. To get the index of in the array for a cell at a
        given (x, y, z) use the "index" helper method.If you modify the
        data via the pointer returned, you must call the "updateGrid"
        call or you will not see your changes.

        Returns: 
        ----- 
        Pointer to the fuel data of the grid

        Parameters:
        -----
        ReturnStatus: MFnFluid.MStatus
        	[out] -> Status code


        '''
        pass

    def getCoordinates(self, u: float,
                        v: float,
                        w: float): 
        '''
        getCoordinates(self, u: float,
                        v: float,
                        w: float)

        Synopsis
        -----
        This method returns pointers to the storage for the uvw
        coordinate data in the fluid. The size of these arrays can be
        obtained using the "gridSize" call. The uvw values supply the 3D
        texture mapping coordinates for each cell.Each of the pointers
        returned points to an array of float values, each value
        representing the u, v, or w value in a cell of the fluid grid. To
        get the index of in the array for a cell at a given (x, y, z) use
        the "index" helper method. The three arrays contain the u values,
        v values, and w values of the texture coordinates
        respectively.For a 2D fluid, a NULL pointer will be returned for
        the w array.If you modify the data via the pointers returned, you
        must call the "updateGrid" call or you will not see your changes.

        Returns:
        -----
        None

        Parameters:
        -----
        u: float
        	[out] -> storage for returning a pointer to the u values in the grid 

        v: float
        	[out] -> storage for returning a pointer to the v values in the grid 

        w: float
        	[out] -> storage for returning a pointer to the w values in the grid


        '''
        pass

    def getColors(self, r: float,
                        g: float,
                        b: float): 
        '''
        getColors(self, r: float,
                        g: float,
                        b: float)

        Synopsis
        -----
        This method returns pointers to the storage for the color data in
        the fluid. The size of these arrays can be obtained using the
        "gridSize" call.Each of the pointers returned points to an array
        of float values, each value representing the color in a cell of
        the fluid grid. To get the index of in the array for a cell at a
        given (x, y, z) use the "index" helper method. The three arrays
        contain the r components, g components, and b components of the
        color respectively.If you modify the data via the pointers
        returned, you must call the "updateGrid" call or you will not see
        your changes.

        Returns:
        -----
        None

        Parameters:
        -----
        r: float
        	[out] -> storage for returning a pointer to the red components of the color values in the grid 

        g: float
        	[out] -> storage for returning a pointer to the green components of the color values in the grid 

        b: float
        	[out] -> storage for returning a pointer to the blue components of the color values in the grid


        '''
        pass

    def setFalloffMode(self, method: MFnFluid.MFnFluid): 
        '''
        setFalloffMode(self, method: MFnFluid.MFnFluid)

        Synopsis
        -----
        Set the modes by which the shader falloff values in the grid are
        determined. If the falloff grid is enabled, its values must be
        set by the user.The method parameter may have the following
        values:

        Returns:
        -----
        None

        Parameters:
        -----
        method: MFnFluid.MFnFluid
        	[in] -> method for determining the falloff value in the grid


        '''
        pass

    def getFalloffMode(self, method: MFnFluid.MFnFluid): 
        '''
        getFalloffMode(self, method: MFnFluid.MFnFluid)

        Synopsis
        -----
        Get the modes by which the falloff values in the grid are
        determined. If the falloff grid is enabled, its values must be
        set by the user.The method parameter may return the following
        values:

        Returns:
        -----
        None

        Parameters:
        -----
        method: MFnFluid.MFnFluid
        	[out] -> storage for returning the method by which the falloff value in the grid is determined


        '''
        pass

    def setDensityMode(self, method: MFnFluid.MFnFluid,
                        gradient: MFnFluid.MFnFluid): 
        '''
        setDensityMode(self, method: MFnFluid.MFnFluid,
                        gradient: MFnFluid.MFnFluid)

        Synopsis
        -----
        Set the modes by which the density values in the grid are
        determined. The values may be set by the user in various ways, or
        they may be computed as part of a simulation.The method parameter
        may have the following values:If the method is set to be
        kGradient, then the gradient argument is also used. This
        deterines how a gradient is applied to the volume. The possible
        values are as follows:

        Returns:
        -----
        None

        Parameters:
        -----
        method: MFnFluid.MFnFluid
        	[in] -> method for determining the fluid density in the grid 

        gradient: MFnFluid.MFnFluid
        	[in] -> gradient type, only used if the method is kGradient


        '''
        pass

    def getDensityMode(self, method: MFnFluid.MFnFluid,
                        gradient: MFnFluid.MFnFluid): 
        '''
        getDensityMode(self, method: MFnFluid.MFnFluid,
                        gradient: MFnFluid.MFnFluid)

        Synopsis
        -----
        Get the modes by which the density values in the grid are
        determined. The values may be set by the user in various ways, or
        they may be computed as part of a simulation.The method parameter
        may return the following values:If the method returns kGradient,
        then the gradient type is also returned. This deterines how a
        gradient is applied to the volume. The possible return values are
        as follows:

        Returns:
        -----
        None

        Parameters:
        -----
        method: MFnFluid.MFnFluid
        	[out] -> storage for returning the method by which the fluid density in the grid is determined 

        gradient: MFnFluid.MFnFluid
        	[out] -> storage for returning the gradient type, which is only relevant if the method is kGradient


        '''
        pass

    def setVelocityMode(self, method: MFnFluid.MFnFluid,
                        gradient: MFnFluid.MFnFluid): 
        '''
        setVelocityMode(self, method: MFnFluid.MFnFluid,
                        gradient: MFnFluid.MFnFluid)

        Synopsis
        -----
        Set the modes by which the velocity values in the grid are
        determined. The values may be set by the user in various ways, or
        they may be computed as part of a simulation.The method parameter
        may have the following values:If the method is set to be
        kGradient, then the gradient argument is also used. This
        deterines how a gradient is applied to the volume. The possible
        values are as follows:

        Returns:
        -----
        None

        Parameters:
        -----
        method: MFnFluid.MFnFluid
        	[in] -> method for determining the fluid velocity in the grid 

        gradient: MFnFluid.MFnFluid
        	[in] -> gradient type, only used if the method is kGradient


        '''
        pass

    def getVelocityMode(self, method: MFnFluid.MFnFluid,
                        gradient: MFnFluid.MFnFluid): 
        '''
        getVelocityMode(self, method: MFnFluid.MFnFluid,
                        gradient: MFnFluid.MFnFluid)

        Synopsis
        -----
        Get the modes by which the velocity values in the grid are
        determined. The values may be set by the user in various ways, or
        they may be computed as part of a simulation.The method parameter
        may return the following values:If the method returns kGradient,
        then the gradient type is also returned. This deterines how a
        gradient is applied to the volume. The possible return values are
        as follows:

        Returns:
        -----
        None

        Parameters:
        -----
        method: MFnFluid.MFnFluid
        	[out] -> storage for returning the method by which the fluid velocity in the grid is determined 

        gradient: MFnFluid.MFnFluid
        	[out] -> storage for returning the gradient type, which is only relevant if the method is kGradient


        '''
        pass

    def setTemperatureMode(self, method: MFnFluid.MFnFluid,
                        gradient: MFnFluid.MFnFluid): 
        '''
        setTemperatureMode(self, method: MFnFluid.MFnFluid,
                        gradient: MFnFluid.MFnFluid)

        Synopsis
        -----
        Set the modes by which the temperature values in the grid are
        determined. The values may be set by the user in various ways, or
        they may be computed as part of a simulation.The method parameter
        may have the following values:If the method is set to be
        kGradient, then the gradient argument is also used. This
        deterines how a gradient is applied to the volume. The possible
        values are as follows:

        Returns:
        -----
        None

        Parameters:
        -----
        method: MFnFluid.MFnFluid
        	[in] -> method for determining the fluid temperature in the grid 

        gradient: MFnFluid.MFnFluid
        	[in] -> gradient type, only used if the method is kGradient


        '''
        pass

    def getTemperatureMode(self, method: MFnFluid.MFnFluid,
                        gradient: MFnFluid.MFnFluid): 
        '''
        getTemperatureMode(self, method: MFnFluid.MFnFluid,
                        gradient: MFnFluid.MFnFluid)

        Synopsis
        -----
        Get the modes by which the temperature values in the grid are
        determined. The values may be set by the user in various ways, or
        they may be computed as part of a simulation.The method parameter
        may return the following values:If the method returns kGradient,
        then the gradient type is also returned. This deterines how a
        gradient is applied to the volume. The possible return values are
        as follows:

        Returns:
        -----
        None

        Parameters:
        -----
        method: MFnFluid.MFnFluid
        	[out] -> storage for returning the method by which the fluid temperature in the grid is determined 

        gradient: MFnFluid.MFnFluid
        	[out] -> storage for returning the gradient type, which is only relevant if the method is kGradient


        '''
        pass

    def setFuelMode(self, method: MFnFluid.MFnFluid,
                        gradient: MFnFluid.MFnFluid): 
        '''
        setFuelMode(self, method: MFnFluid.MFnFluid,
                        gradient: MFnFluid.MFnFluid)

        Synopsis
        -----
        Set the modes by which the fuel values in the grid are
        determined. The values may be set by the user in various ways, or
        they may be computed as part of a simulation. The fuel value for
        a cell can be thought of as the amount of fuel contained in the
        cell that will be consumed during the simulation.The method
        parameter may have the following values:Note that kStatic is not
        an option for the fuel mode. A static grid of fuel values would
        not make sense as the solver needs to use up the fuel during the
        simulation.If the method is set to be kGradient, then the
        gradient argument is also used. This deterines how a gradient is
        applied to the volume. The possible values are as follows:

        Returns:
        -----
        None

        Parameters:
        -----
        method: MFnFluid.MFnFluid
        	[in] -> method for determining the fluid fuel in the grid 

        gradient: MFnFluid.MFnFluid
        	[in] -> gradient type, only used if the method is kGradient


        '''
        pass

    def getFuelMode(self, method: MFnFluid.MFnFluid,
                        gradient: MFnFluid.MFnFluid): 
        '''
        getFuelMode(self, method: MFnFluid.MFnFluid,
                        gradient: MFnFluid.MFnFluid)

        Synopsis
        -----
        Get the modes by which the fuel values in the grid are
        determined. The values may be set by the user in various ways, or
        they may be computed as part of a simulation.The method parameter
        may return the following values:If the method returns kGradient,
        then the gradient type is also returned. This deterines how a
        gradient is applied to the volume. The possible return values are
        as follows:

        Returns:
        -----
        None

        Parameters:
        -----
        method: MFnFluid.MFnFluid
        	[out] -> storage for returning the method by which the fluid fuel values in the grid is determined 

        gradient: MFnFluid.MFnFluid
        	[out] -> storage for returning the gradient type, which is only relevant if the method is kGradient


        '''
        pass

    def setCoordinateMode(self, method: MFnFluid.MFnFluid): 
        '''
        setCoordinateMode(self, method: MFnFluid.MFnFluid)

        Synopsis
        -----
        Set the modes by which the UVW coordinate values in the grid are
        determined. The values may be set by the user in various ways, or
        they may be computed as part of a simulation.The method parameter
        may have the following values:

        Returns:
        -----
        None

        Parameters:
        -----
        method: MFnFluid.MFnFluid
        	[in] -> method for determining the fluid UVW coordinates in the grid


        '''
        pass

    def getCoordinateMode(self, method: MFnFluid.MFnFluid): 
        '''
        getCoordinateMode(self, method: MFnFluid.MFnFluid)

        Synopsis
        -----
        Get the modes by which the UVW coordinates values in the grid are
        determined. The values may be set by the user in various ways, or
        they may be computed as part of a simulation.The method parameter
        may return the following values:

        Returns:
        -----
        None

        Parameters:
        -----
        method: MFnFluid.MFnFluid
        	[out] -> storage for returning the method by which the fluid coordinate values in the grid is determined


        '''
        pass

    def setColorMode(self, method: MFnFluid.MFnFluid): 
        '''
        setColorMode(self, method: MFnFluid.MFnFluid)

        Synopsis
        -----
        Set the modes by which the color values in the grid are
        determined. The values may be set by the user in various ways, or
        they may be computed as part of a simulation.The method parameter
        may have the following values:

        Returns:
        -----
        None

        Parameters:
        -----
        method: MFnFluid.MFnFluid
        	[in] -> method for determining the fluid color in the grid


        '''
        pass

    def getColorMode(self, method: MFnFluid.MFnFluid): 
        '''
        getColorMode(self, method: MFnFluid.MFnFluid)

        Synopsis
        -----
        Get the modes by which the color values in the grid are
        determined. The values may be set by the user in various ways, or
        they may be computed as part of a simulation.The method parameter
        may return the following values:

        Returns:
        -----
        None

        Parameters:
        -----
        method: MFnFluid.MFnFluid
        	[out] -> storage for returning the method by which the fluid color in the grid is determined


        '''
        pass

    @overload
    def getForceAtPoint(self, point: MPointArray,
                        velocity: MVectorArray,
                        mass: MDoubleArray,
                        force: MVectorArray,
                        deltaTime: double): 
        '''
        getForceAtPoint(self, point: MPointArray,
                        velocity: MVectorArray,
                        mass: MDoubleArray,
                        force: MVectorArray,
                        deltaTime: double)

        Synopsis
        -----
        Compute the force of the fluid as a field on an array of points,
        given their position, velocity, and mass. This method uses
        MPointArray to represent the positions of points. If a point
        instance is in a rational form or a homogenous form, you should
        reset it to be in the cartesian form P(x, y, z, 1).

        Returns:
        -----
        None

        Parameters:
        -----
        point: MPointArray
        	[in] -> array of positions for each point. 

        velocity: MVectorArray
        	[in] -> array of velocities for each point. If the length of the velocity array is 0, a velocity of 0.0 is assumed for all the points. 

        mass: MDoubleArray
        	[in] -> array of mass values for each point. If the length of the mass array is 0, a mass of 1.0 is assumed for all the points. 

        force: MVectorArray
        	[out] -> output array of forces applied to each point. If the length of the force array supplied is 0, the array is automatically resized. If the contents of the force array contains data, the computed force is added to the supplied data. This can be useful to accumulate forces of multiple fields. 

        deltaTime: double
        	[in] -> time increment in seconds. Default is (1.0 / 24.0 fps).


        '''
        pass

    @overload
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
        Compute the force of a field on an array of points, given their
        position, velocity, and mass. Note that only the Air and Vortex
        fields require a time increment to compute forces, all other
        fields will igonore this argument.This method uses MVectorArray
        to represent the positions of a point.

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
        	[in] -> time increment in seconds for usage with the Air and Vortex fields. Default is (1.0 / 24.0 fps).


        '''
        pass

    def toGridIndex(self, objectSpacePoint: MPoint,
                        gridCoords: int3,
                        status: MFnFluid.MStatus): 
        '''
        toGridIndex(self, objectSpacePoint: MPoint,
                        gridCoords: int3,
                        status: MFnFluid.MStatus) -> bool

        Synopsis
        -----
        For the given point in object space, get the grid indices of the
        voxel that it happens to lie in. If the point is outside the
        fluid, the method returns false, and the indices should not be
        used.

        Returns: 
        ----- 
        True if the point is inside the fluid, false otherwise

        Parameters:
        -----
        objectSpacePoint: MPoint
        	[in] -> an object space location 

        gridCoords: int3
        	[out] -> the voxel indices, if the point falls inside a voxel 

        status: MFnFluid.MStatus
        	[out] -> Status code


        '''
        pass

    def voxelCenterPosition(self, xi: int,
                        yi: int,
                        zi: int,
                        objectSpacePoint: MPoint): 
        '''
        voxelCenterPosition(self, xi: int,
                        yi: int,
                        zi: int,
                        objectSpacePoint: MPoint)

        Synopsis
        -----
        For the given voxel, get the location of the center in object
        space. If the voxel indices are not valid, the point may not be
        set to a valid point

        Returns:
        -----
        None

        Parameters:
        -----
        xi: int
        	[in] -> the voxel x index 

        yi: int
        	[in] -> the voxel y index 

        zi: int
        	[in] -> the voxel z index 

        objectSpacePoint: MPoint
        	[out] -> the object space location


        '''
        pass

    def updateGrid(self): 
        '''
        updateGrid(self)

        Synopsis
        -----
        Tells the fluid shape that the contents of the fluid grid has
        changed. It is necessary to call this routine after modifying
        internal fluid data via a pointer recieved from any of the access
        routines in this function set. Failure to call this will result
        in the fluid not drawing with your changes.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def emitIntoArrays(self, val: float,
                        x: int,
                        y: int,
                        z: int,
                        density: float,
                        heat: float,
                        fuel: float,
                        doColor: bool,
                        emitColor: MColor): 
        '''
        emitIntoArrays(self, val: float,
                        x: int,
                        y: int,
                        z: int,
                        density: float,
                        heat: float,
                        fuel: float,
                        doColor: bool,
                        emitColor: MColor)

        Synopsis
        -----
        Use this method to add density, heat, fuel, and/or color to a
        particular voxel of a fluid.

        Returns:
        -----
        None

        Parameters:
        -----
        val: float
        	[in] -> multiplier applied to the specified density, heat, and fuel values. 

        x: int
        	[in] -> voxel index in x 

        y: int
        	[in] -> voxel index in y 

        z: int
        	[in] -> voxel index in z 

        density: float
        	[in] -> amount of density to add to the voxel 

        heat: float
        	[in] -> amount of heat to add to the voxel 

        fuel: float
        	[in] -> amount of fuel to add to the voxel 

        doColor: bool
        	[in] -> if true, then color specified by "emitColor" will be blended into the voxel's current color, with the blend coefficients being determined by the amount of density that is being added to the voxel. 

        emitColor: MColor
        	[in] -> color to be blended into the voxel. 


        '''
        pass

    @overload
    def index(self, xi: int,
                        yi: int): 
        '''
        index(self, xi: int,
                        yi: int) -> int

        Synopsis
        -----
        This is a utility routine for finding the index of a cell in an
        array of fluid data. The data in the fluid shape, such as color
        and density are passed back as single dimensional arrays of
        numeric values. This method converts three dimensional
        coordinates of a cell into the index value that refers the cell's
        value in the single dimensional array.Note that no bounds
        checking is performed.

        Returns: 
        ----- 
        Index in the single dimensional array

        Parameters:
        -----
        xi: int
        	[in] -> index in x 

        yi: int
        	[in] -> index in y


        '''
        pass

    @overload
    def index(self, xi: int,
                        yi: int,
                        zi: int): 
        '''
        index(self, xi: int,
                        yi: int,
                        zi: int) -> int

        Synopsis
        -----
        This is a utility routine for finding the index of a cell in an
        array of fluid data. The data in the fluid shape, such as color
        and density are passed back as single dimensional arrays of
        numeric values. This method converts three dimensional
        coordinates of a cell into the index value that refers the cell's
        value in the single dimensional array.Note that no bounds
        checking is performed.

        Returns: 
        ----- 
        Index in the single dimensional array

        Parameters:
        -----
        xi: int
        	[in] -> index in x 

        yi: int
        	[in] -> index in y 

        zi: int
        	[in] -> index in z


        '''
        pass

    @overload
    def index(self, index: int,
                        xi: int,
                        yi: int,
                        zi: int): 
        '''
        index(self, index: int,
                        xi: int,
                        yi: int,
                        zi: int)

        Synopsis
        -----
        This is a utility routine for finding the coordinates of a cell
        in an array of fluid data given the index. The data in the fluid
        shape, such as color and density are passed back as single
        dimensional arrays of numeric values. This method converts the
        index value that refers to a cell's value in the single
        dimensional array into the three dimensional coordinates of the
        cell.Note that no bounds checking is performed.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> index to convert into coordinates 

        xi: int
        	[out] -> storage for the index in x 

        yi: int
        	[out] -> storage for the index in y 

        zi: int
        	[out] -> storage for the index in z 


        '''
        pass

    @overload
    def index(self, xi: int,
                        yi: int,
                        zi: int,
                        xres: int,
                        yres: int,
                        zres: int): 
        '''
        index(self, xi: int,
                        yi: int,
                        zi: int,
                        xres: int,
                        yres: int,
                        zres: int) -> int

        Synopsis
        -----
        This is a utility routine for finding the index of a cell given
        the X, Y and Z resolutions. This is intended for use primarily
        with the velocity arrays, where the resolutions are different for
        each array. The X velocity array is one bigger in X, etc.This
        method converts three dimensional coordinates of a cell into the
        index value that refers the cell's value in the single
        dimensional array.Note that no bounds checking is performed.

        Returns: 
        ----- 
        Index in the single dimensional array

        Parameters:
        -----
        xi: int
        	[in] -> index in x 

        yi: int
        	[in] -> index in y 

        zi: int
        	[in] -> index in z 

        xres: int
        	[in] -> resolution in x 

        yres: int
        	[in] -> resolution in y 

        zres: int
        	[in] -> resolution in z


        '''
        pass

    @overload
    def index(self, index: int,
                        xres: int,
                        yres: int,
                        zres: int,
                        xi: int,
                        yi: int,
                        zi: int): 
        '''
        index(self, index: int,
                        xres: int,
                        yres: int,
                        zres: int,
                        xi: int,
                        yi: int,
                        zi: int)

        Synopsis
        -----
        This is a utility routine for finding the coordinates of a cell
        given the index, and the X, Y and Z resolutions. This is intended
        for use primarily with the velocity arrays, where the resolutions
        are different for each array. The X velocity array is one bigger
        in X, etc.This method converts the index value that refers to a
        cell's value in the single dimensional array into the three
        dimensional coordinates of the cell.Note that no bounds checking
        is performed.

        Returns:
        -----
        None

        Parameters:
        -----
        index: int
        	[in] -> index to convert into coordinates 

        xres: int
        	[in] -> resolution in x 

        yres: int
        	[in] -> resolution in y 

        zres: int
        	[in] -> resolution in z 

        xi: int
        	[out] -> storage for the index in x 

        yi: int
        	[out] -> storage for the index in y 

        zi: int
        	[out] -> storage for the index in z 


        '''
        pass

    def isAutoResize(self): 
        '''
        isAutoResize(self) -> bool

        Synopsis
        -----
        Is this an autoresize fluid?

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def isResizeToEmitter(self): 
        '''
        isResizeToEmitter(self) -> bool

        Synopsis
        -----
        If this is an autoresize fluid, should it also resize to the
        emitter.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def expandToInclude(self, min: MPoint,
                        max: MPoint): 
        '''
        expandToInclude(self, min: MPoint,
                        max: MPoint)

        Synopsis
        -----
        Tells the fluid shape to autoresize to include these two points
        This would normally be used in a fluid emitter node if the fluid
        had resizeToEmitter turned on. This may fail if the fluid is not
        autoRise and resizeToEmitter, or if the fluid has reached its
        maxResolution

        Returns:
        -----
        None

        Parameters:
        -----
        min: MPoint
        	[in] -> point at lower corner of bounding box 

        max: MPoint
        	[in] -> point at upper corner of boinding box


        '''
        pass

class FluidMethod:
    '''Defines how voxel values are computed for most types of fluid data. 
    Non-functional class.  Values for this enum:
    kZero
    kStaticGrid
    kDynamicGrid
    kGradient
    '''

    def __init__(self):
        pass

    def kZero(self):
        '''This is an enum of FluidMethod.
        - Description: All values in grid are zero. 
        - Value: 0
        '''
        pass

    def kStaticGrid(self):
        '''This is an enum of FluidMethod.
        - Description: Values in the grid are static. 
        - Value: 1
        '''
        pass

    def kDynamicGrid(self):
        '''This is an enum of FluidMethod.
        - Description: Values in the grid come from a dynamic solver. 
        - Value: 2
        '''
        pass

    def kGradient(self):
        '''This is an enum of FluidMethod.
        - Description: Ramps the value based on the gradient setting. 
        - Value: 3
        '''
        pass

class FluidGradient:
    '''Defines the orientation of the gradient. 
    Non-functional class.  Values for this enum:
    kConstant
    kXGradient
    kYGradient
    kZGradient
    kNegXGradient
    kNegYGradient
    kNegZGradient
    kCenterGradient
    '''

    def __init__(self):
        pass

    def kConstant(self):
        '''This is an enum of FluidGradient.
        - Description: Value is set to one across the volume. 
        - Value: 0
        '''
        pass

    def kXGradient(self):
        '''This is an enum of FluidGradient.
        - Description: Ramp the value from zero to one along the X axis. 
        - Value: 1
        '''
        pass

    def kYGradient(self):
        '''This is an enum of FluidGradient.
        - Description: Ramp the value from zero to one along the Y axis. 
        - Value: 2
        '''
        pass

    def kZGradient(self):
        '''This is an enum of FluidGradient.
        - Description: Ramp the value from zero to one along the Z axis. 
        - Value: 3
        '''
        pass

    def kNegXGradient(self):
        '''This is an enum of FluidGradient.
        - Description: Ramp the value from one to zero along the X axis. 
        - Value: 4
        '''
        pass

    def kNegYGradient(self):
        '''This is an enum of FluidGradient.
        - Description: Ramp the value from one to zero along the Y axis. 
        - Value: 5
        '''
        pass

    def kNegZGradient(self):
        '''This is an enum of FluidGradient.
        - Description: Ramp the value from one to zero along the Z axis. 
        - Value: 6
        '''
        pass

    def kCenterGradient(self):
        '''This is an enum of FluidGradient.
        - Description: Ramps the value from one at the center to zero at the edges. 
        - Value: 7
        '''
        pass

class FalloffMethod:
    '''Falloff data only supports a subset of the available fluid methods. 
    Non-functional class.  Values for this enum:
    kNoFalloffGrid
    kStaticFalloffGrid
    '''

    def __init__(self):
        pass

    def kNoFalloffGrid(self):
        '''This is an enum of FalloffMethod.
        - Description: No falloff grid should be defined. 
        - Value: 0
        '''
        pass

    def kStaticFalloffGrid(self):
        '''This is an enum of FalloffMethod.
        - Description: Values in the falloff grid are static. 
        - Value: 1
        '''
        pass

class ColorMethod:
    '''Color data has its own set of methods for computing voxel data. 
    Non-functional class.  Values for this enum:
    kUseShadingColor
    kStaticColorGrid
    kDynamicColorGrid
    '''

    def __init__(self):
        pass

    def kUseShadingColor(self):
        '''This is an enum of ColorMethod.
        - Description: Off, use shading color instead. 
        - Value: 0
        '''
        pass

    def kStaticColorGrid(self):
        '''This is an enum of ColorMethod.
        - Description: Values in the grid are static. 
        - Value: 1
        '''
        pass

    def kDynamicColorGrid(self):
        '''This is an enum of ColorMethod.
        - Description: Values in the grid come from a dynamic solver. 
        - Value: 2
        '''
        pass

class CoordinateMethod:
    '''Coordinate data has its own set of methods for computing voxel data. 
    Non-functional class.  Values for this enum:
    kFixed
    kGrid
    '''

    def __init__(self):
        pass

    def kFixed(self):
        '''This is an enum of CoordinateMethod.
        - Description: Values are equal the object space coordinates. 
        - Value: 0
        '''
        pass

    def kGrid(self):
        '''This is an enum of CoordinateMethod.
        - Description: Coordinate values will be moved using the current density solver. 
        - Value: 1
        '''
        pass

class MFnGravityField:
    '''Function set for Gravity Fields.
Function set for creation, edit, and query of Gravity Fields.
A gravity field simulates the Earth's gravitational force. It
pulls objects in a fixed direction entirely independent of their
position or mass.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kGravity.Reimplemented from MFnField.

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

    def direction(self, ReturnStatus: MFnGravityField.MStatus): 
        '''
        direction(self, ReturnStatus: MFnGravityField.MStatus) -> MVector

        Synopsis
        -----
        Returns the direction of the gravitational force.

        Returns: 
        ----- 
        A vector representing direction.

        Parameters:
        -----
        ReturnStatus: MFnGravityField.MStatus
        	[out] -> Status code


        '''
        pass

    def setDirection(self, gravityDirection: MVector): 
        '''
        setDirection(self, gravityDirection: MVector)

        Synopsis
        -----
        Sets the direction vector of the gravitational force.

        Returns:
        -----
        None

        Parameters:
        -----
        gravityDirection: MVector
        	[in] -> A vector representing direction.


        '''
        pass

class MFnInstancer:
    '''Particle Instancer object access class.
Class for obtaining information about a particle instancer node.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kInstancer.Reimplemented from MFnDagNode.

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

    def particleCount(self): 
        '''
        particleCount(self) -> int

        Synopsis
        -----
        Returns the number of particles feeding the active instancer.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def instancesForParticle(self, p: int,
                        paths: MDagPathArray,
                        instancerMatrix: MMatrix,
                        ReturnStatus: MFnInstancer.MStatus): 
        '''
        instancesForParticle(self, p: int,
                        paths: MDagPathArray,
                        instancerMatrix: MMatrix,
                        ReturnStatus: MFnInstancer.MStatus) -> int

        Synopsis
        -----
        Returns the DAG paths and instancer matrix for all instances
        generated by a specified particle.

        Returns: 
        ----- 
        The number of visible paths instanced for the given particle. It
        is possible for no paths to be instanced for a particular
        particle. Note that in order to use this method, the MDagPath
        must be used in the constructor.

        Parameters:
        -----
        p: int
        	[in] -> The index of the particle being queried. 

        paths: MDagPathArray
        	[out] -> Visible DAG paths generated by particle p 

        instancerMatrix: MMatrix
        	[out] -> The transformation matrix that the instancer applies to the instanced paths to produce the final particle-instanced geometry. The final world matrix of each instance can be constructed by premultiplying the path's inclusive world matrix by this matrix. 

        ReturnStatus: MFnInstancer.MStatus
        	[out] -> status code


        '''
        pass

    def allInstances(self, paths: MDagPathArray,
                        matrices: MMatrixArray,
                        particlePathStartIndices: MIntArray,
                        pathIndices: MIntArray): 
        '''
        allInstances(self, paths: MDagPathArray,
                        matrices: MMatrixArray,
                        particlePathStartIndices: MIntArray,
                        pathIndices: MIntArray)

        Synopsis
        -----
        Returns information about all instances generated by a particular
        particle instancer node. Since many particles will typically
        instance similar sets of paths, the information is returned in a
        compact representation. An array of paths is returned,
        representing the unique set of paths that are instanced by any
        particle in the system. For each particle, the routine returns a
        set of indices into this path array to illustrate the paths
        instanced at that particle. The index arrays for all particles
        are concatenated together, so a "start index" array is used to
        indicate which is the first entry in the index array for each
        particle. For each particle, the routine also returns the
        transformation matrix applied to that particle's instanced paths
        to generate the final particle instance transformations.

        Returns:
        -----
        None

        Parameters:
        -----
        paths: MDagPathArray
        	[out] -> Receives the unique set of paths instanced by any particle in the system. 

        matrices: MMatrixArray
        	[out] -> For each particle p, matrices[p] receives the matrix that the instancer applies to the paths instanced under that particle to generate the final instance transformations. 

        particlePathStartIndices: MIntArray
        	[out] -> Receives indices into the 

        pathIndices: MIntArray
        	[out] -> Receives indices into the 


        '''
        pass

class MFnNewtonField:
    '''Function set for Newton Fields.
Function set for creation, edit, and query of Newton Fields.
A newton field pulls an object toward another with a force that
is dependent on the mass of the object exerting the field. It
follows Newton's Law of Universal Gravitation.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kNewton.Reimplemented from MFnField.

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

    def minDistance(self, ReturnStatus: MFnNewtonField.MStatus): 
        '''
        minDistance(self, ReturnStatus: MFnNewtonField.MStatus) -> double

        Synopsis
        -----
        Returns the minimum distance from the newton field at which the
        force of the field is exerted.

        Returns: 
        ----- 
        A value representing distance in internal linear units.

        Parameters:
        -----
        ReturnStatus: MFnNewtonField.MStatus
        	[out] -> Status code


        '''
        pass

    def setMinDistance(self, distance: double): 
        '''
        setMinDistance(self, distance: double)

        Synopsis
        -----
        Sets the minimum distance from the newton field at which the
        force of the field is exerted.

        Returns:
        -----
        None

        Parameters:
        -----
        distance: double
        	[in] -> A value representing distance in internal linear units.


        '''
        pass

class MFnNIdData:
    '''function set for nId object data
Class for transferring N id data between connections
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kNIdData.Reimplemented from MFnData.

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
        "MFnNIdData".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def create(self): 
        '''
        create(self) -> MObject

        Synopsis
        -----
        Creates an underlying Maya nId data object and return it as an
        MObject.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

class MFnNObjectData:
    '''function set for nCloth object data
Class for transferring N object data between connections
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kNObjectData.Reimplemented from MFnData.

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
        "MFnNObjectData".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def create(self): 
        '''
        create(self) -> MObject

        Synopsis
        -----
        Creates an underlying Maya N data object and return it as an
        MObject.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def setObjectPtr(self, ptr: MnCloth): 
        '''
        setObjectPtr(self, ptr: MnCloth)

        Synopsis
        -----
        Set the nCloth pointer.

        Returns:
        -----
        None

        Parameters:
        -----
        ptr: MnCloth
        	[in] -> pointer to the N cloth


        '''
        pass

    @overload
    def setObjectPtr(self, ptr: MnRigid): 
        '''
        setObjectPtr(self, ptr: MnRigid)

        Synopsis
        -----
        Set the nRigid pointer.

        Returns:
        -----
        None

        Parameters:
        -----
        ptr: MnRigid
        	[in] -> pointer to the nRigid


        '''
        pass

    @overload
    def setObjectPtr(self, ptr: MnParticle): 
        '''
        setObjectPtr(self, ptr: MnParticle)

        Synopsis
        -----
        Set the nParticle pointer.

        Returns:
        -----
        None

        Parameters:
        -----
        ptr: MnParticle
        	[in] -> pointer to the nParticle


        '''
        pass

    def getCollide(self, collide: bool): 
        '''
        getCollide(self, collide: bool)

        Synopsis
        -----
        Get wether the nObject is allowed to participate in collisions.

        Returns:
        -----
        None

        Parameters:
        -----
        collide: bool
        	[out] -> the collision state


        '''
        pass

    def isCached(self, status: MFnNObjectData.MStatus): 
        '''
        isCached(self, status: MFnNObjectData.MStatus) -> bool

        Synopsis
        -----
        Get whether the nObject is cached.

        Returns: 
        ----- 
        the cache state

        Parameters:
        -----
        status: MFnNObjectData.MStatus
        	[out] -> Status Code


        '''
        pass

    def setCached(self, cached: bool): 
        '''
        setCached(self, cached: bool)

        Synopsis
        -----
        Set wether the nObject is cached.

        Returns:
        -----
        None

        Parameters:
        -----
        cached: bool
        	[in] -> the cache state


        '''
        pass

class MFnParticleSystem:
    '''Class for obtaining information about a particle system.
Particle object access class.
Use this chart to determine which methods to call based on the
render type of the particle object:
Valid Methods for render type kCloud:
Valid Methods for render type kTube:
Valid Methods for render type kBlobby:
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kParticle.Reimplemented from MFnDagNode.

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
    def create(self, ReturnStatus: MFnParticleSystem.MStatus): 
        '''
        create(self, ReturnStatus: MFnParticleSystem.MStatus) -> MObject

        Synopsis
        -----
        To create a new particleShape with a transform.

        Returns: 
        ----- 
        The newly created particleShape

        Parameters:
        -----
        ReturnStatus: MFnParticleSystem.MStatus
        	[out] -> Status code


        '''
        pass

    @overload
    def create(self, parentMObj: MObject,
                        ReturnStatus: MFnParticleSystem.MStatus): 
        '''
        create(self, parentMObj: MObject,
                        ReturnStatus: MFnParticleSystem.MStatus) -> MObject

        Synopsis
        -----
        To create a new particleShape. If the parent is not specified, a
        new transform will be created as the parent.

        Returns: 
        ----- 
        The newly created particleShape

        Parameters:
        -----
        parentMObj: MObject
        	[in] -> The parent as an 

        ReturnStatus: MFnParticleSystem.MStatus
        	[out] -> Status code


        '''
        pass

    @overload
    def emit(self, v: MPoint): 
        '''
        emit(self, v: MPoint)

        Synopsis
        -----
        To add a new particle at the given position.

        Returns:
        -----
        None

        Parameters:
        -----
        v: MPoint
        	[in] -> The particle's position


        '''
        pass

    @overload
    def emit(self, pArray: MPointArray): 
        '''
        emit(self, pArray: MPointArray)

        Synopsis
        -----
        To add an array of new particles at the given positions.

        Returns:
        -----
        None

        Parameters:
        -----
        pArray: MPointArray
        	[in] -> The particle's position array


        '''
        pass

    @overload
    def emit(self, p: MPoint,
                        v: MVector): 
        '''
        emit(self, p: MPoint,
                        v: MVector)

        Synopsis
        -----
        To add a new particle at the position with its velocity.

        Returns:
        -----
        None

        Parameters:
        -----
        p: MPoint
        	[in] -> The particle's position 

        v: MVector
        	[in] -> The particle's velocity


        '''
        pass

    @overload
    def emit(self, pArray: MPointArray,
                        vArray: MVectorArray): 
        '''
        emit(self, pArray: MPointArray,
                        vArray: MVectorArray)

        Synopsis
        -----
        To add an array of new particles at the given positions with
        their velocity values.

        Returns:
        -----
        None

        Parameters:
        -----
        pArray: MPointArray
        	[in] -> The particle's position array 

        vArray: MVectorArray
        	[in] -> The particle's velocity array


        '''
        pass

    def saveInitialState(self): 
        '''
        saveInitialState(self)

        Synopsis
        -----
        To reset the particle's current state as the initial state.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def evaluateDynamics(self, to: MTime,
                        runupFromStart: bool): 
        '''
        evaluateDynamics(self, to: MTime,
                        runupFromStart: bool)

        Synopsis
        -----
        Run up the particle system to a certain frame, from either the
        current frame, or from the start of the simulation.

        Returns:
        -----
        None

        Parameters:
        -----
        to: MTime
        	[in] -> Time to run the particle system up to. 

        runupFromStart: bool
        	[in] -> If true runup will begin at the start of the simulation, otherwise it will begin from the current frame. 


        '''
        pass

    def isValid(self): 
        '''
        isValid(self) -> bool

        Synopsis
        -----
        Returns false if the particle array is nullptr. Returns true
        otherwise.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def setCount(self, count: int): 
        '''
        setCount(self, count: int)

        Synopsis
        -----
        Set the particle count at the current frame.

        Returns:
        -----
        None

        Parameters:
        -----
        count: int
        	[in] -> Particle count. 


        '''
        pass

    def position(self, positions: MVectorArray): 
        '''
        position(self, positions: MVectorArray)

        Synopsis
        -----
        Compute each particle's position at the start of the time step.
        This is done by taking the particle's current position and
        velocity, and extrapolation backwards in time.NOTE: For an
        MFnParticleSystem of renderType kTube, use position0() and
        position1() instead.

        Returns:
        -----
        None

        Parameters:
        -----
        positions: MVectorArray
        	[in] -> 


        '''
        pass

    def velocity(self, array: MVectorArray): 
        '''
        velocity(self, array: MVectorArray)

        Synopsis
        -----
        To return velocity array for all particles.

        Returns:
        -----
        None

        Parameters:
        -----
        array: MVectorArray
        	[out] -> The resulting velocity array 


        '''
        pass

    def acceleration(self, array: MVectorArray): 
        '''
        acceleration(self, array: MVectorArray)

        Synopsis
        -----
        To return acceleration array for all particles.

        Returns:
        -----
        None

        Parameters:
        -----
        array: MVectorArray
        	[out] -> The resulting acceleration array 


        '''
        pass

    def position0(self, positions: MVectorArray): 
        '''
        position0(self, positions: MVectorArray)

        Synopsis
        -----
        Only for use with an MFnParticleSystem of renderType kTube.
        Calculates particle start positions.

        Returns:
        -----
        None

        Parameters:
        -----
        positions: MVectorArray
        	[in] -> 


        '''
        pass

    def position1(self, positions: MVectorArray): 
        '''
        position1(self, positions: MVectorArray)

        Synopsis
        -----
        Only for use with an MFnParticleSystem of renderType kTube.
        Calculates particle end positions.

        Returns:
        -----
        None

        Parameters:
        -----
        positions: MVectorArray
        	[in] -> 


        '''
        pass

    def radius(self, radii: MDoubleArray): 
        '''
        radius(self, radii: MDoubleArray)

        Synopsis
        -----
        Calculates particle radii. NOTE: For an MFnParticleSystem of
        renderType kTube, use position0() and position1() instead.

        Returns:
        -----
        None

        Parameters:
        -----
        radii: MDoubleArray
        	[in] -> 


        '''
        pass

    def radius0(self, radii: MDoubleArray): 
        '''
        radius0(self, radii: MDoubleArray)

        Synopsis
        -----
        Only for use with an MFnParticleSystem of renderType kTube.
        Calculates the particles' start radii.

        Returns:
        -----
        None

        Parameters:
        -----
        radii: MDoubleArray
        	[in] -> 


        '''
        pass

    def radius1(self, radii: MDoubleArray): 
        '''
        radius1(self, radii: MDoubleArray)

        Synopsis
        -----
        Only for use with an MFnParticleSystem of renderType kTube.
        Calculates the particles' end radii.

        Returns:
        -----
        None

        Parameters:
        -----
        radii: MDoubleArray
        	[in] -> 


        '''
        pass

    def surfaceShading(self): 
        '''
        surfaceShading(self) -> double

        Synopsis
        -----
        Only for use with an MFnParticleSystem of renderType kCloud.
        Returns the object surface shading value.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def threshold(self): 
        '''
        threshold(self) -> double

        Synopsis
        -----
        Only for use with an MFnParticleSystem of renderType kCloud or
        kBlobby. Returns the object threshold.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def betterIllum(self): 
        '''
        betterIllum(self) -> bool

        Synopsis
        -----
        Only for use with an MFnParticleSystem of renderType kCloud.
        Returns a boolean indicating whether or not thick cloud sampling
        is already enabled.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def flatShaded(self): 
        '''
        flatShaded(self) -> bool

        Synopsis
        -----
        To check if a particle shape of cloud type is flat shaded. This
        is only for use with an MFnParticleSystem of renderType kCloud.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def disableCloudAxis(self): 
        '''
        disableCloudAxis(self) -> bool

        Synopsis
        -----
        Only for use with an MFnParticleSystem of renderType kCloud.
        Internal use for better illum.NOTE: Internal use only. Do not
        call.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def tailSize(self): 
        '''
        tailSize(self) -> double

        Synopsis
        -----
        Only for use with an MFnParticleSystem of renderType kTube.
        Returns the length scale factor.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def particleIds(self, ids: MIntArray): 
        '''
        particleIds(self, ids: MIntArray)

        Synopsis
        -----
        Return an array of particle identifiers at the start of the time
        step. The array of particle id's is correlated with the other
        per-particle arrays returned by this class, so ids[i] will be the
        id for the particle with position position[i], velocity[i], etc.,
        as long as all these arrays were retrieved for the same time
        step.The particle id is a constant identifier for an individual
        particle that does not change between time steps. The particle id
        can be used to follow the path of a single particle between
        frames. Only living particle identifiers are returned by this
        method.

        Returns:
        -----
        None

        Parameters:
        -----
        ids: MIntArray
        	[out] -> Array of particle identifiers. The contents of the array are overwritten with the current list of particle identifiers. 


        '''
        pass

    def lifespan(self, lifespans: MDoubleArray): 
        '''
        lifespan(self, lifespans: MDoubleArray)

        Synopsis
        -----
        Populates the given array with the lifespan values of the
        particles in this system, if the particles have this attribute.
        See hasLifespan().

        Returns:
        -----
        None

        Parameters:
        -----
        lifespans: MDoubleArray
        	[in] -> 


        '''
        pass

    def rgb(self, colors: MVectorArray): 
        '''
        rgb(self, colors: MVectorArray)

        Synopsis
        -----
        Populates the given array with the color values of the particles
        in this system, if the particles have this attribute. See
        hasRgb().For each particle, processes the internal representation
        into RGB color values, which are mapped to a vector.

        Returns:
        -----
        None

        Parameters:
        -----
        colors: MVectorArray
        	[in] -> 


        '''
        pass

    def opacity(self, opacities: MDoubleArray): 
        '''
        opacity(self, opacities: MDoubleArray)

        Synopsis
        -----
        Populates the given array with the opacity values of the
        particles in this system, if the particles have this attribute.
        See hasOpacity().

        Returns:
        -----
        None

        Parameters:
        -----
        opacities: MDoubleArray
        	[in] -> 


        '''
        pass

    def mass(self, array: MDoubleArray): 
        '''
        mass(self, array: MDoubleArray)

        Synopsis
        -----
        To return mass array for all particles.

        Returns:
        -----
        None

        Parameters:
        -----
        array: MDoubleArray
        	[out] -> The resulting mass array 


        '''
        pass

    def emission(self, emissions: MVectorArray): 
        '''
        emission(self, emissions: MVectorArray)

        Synopsis
        -----
        Populates the given array with the incandescence values of the
        particles in this system, if the particles have this attribute.
        See hasEmission().

        Returns:
        -----
        None

        Parameters:
        -----
        emissions: MVectorArray
        	[in] -> 


        '''
        pass

    def hasLifespan(self): 
        '''
        hasLifespan(self) -> bool

        Synopsis
        -----
        Returns whether or not the particles in this system have a
        lifespan attribute. See lifespan().

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def hasRgb(self): 
        '''
        hasRgb(self) -> bool

        Synopsis
        -----
        Returns whether or not the particles in this system have an rgb
        attribute. See rgb().

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def hasOpacity(self): 
        '''
        hasOpacity(self) -> bool

        Synopsis
        -----
        Returns whether or not the particles in this system have an
        opacity attribute. See opacity().

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def hasEmission(self): 
        '''
        hasEmission(self) -> bool

        Synopsis
        -----
        Returns whether or not the particles in this system have an
        emission attribute. See emission().

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    @overload
    def getPerParticleAttribute(self, attrName: MString,
                        array: MIntArray,
                        ReturnStatus: MFnParticleSystem.MStatus): 
        '''
        getPerParticleAttribute(self, attrName: MString,
                        array: MIntArray,
                        ReturnStatus: MFnParticleSystem.MStatus) -> int

        Synopsis
        -----
        To get per particle integer attribute with its attribute name.

        Returns: 
        ----- 
        The size of the returned integer array

        Parameters:
        -----
        attrName: MString
        	[in] -> The input attribute name 

        array: MIntArray
        	[out] -> The returned integer array 

        ReturnStatus: MFnParticleSystem.MStatus
        	[out] -> The returned status


        '''
        pass

    @overload
    def getPerParticleAttribute(self, attrName: MString,
                        array: MVectorArray,
                        ReturnStatus: MFnParticleSystem.MStatus): 
        '''
        getPerParticleAttribute(self, attrName: MString,
                        array: MVectorArray,
                        ReturnStatus: MFnParticleSystem.MStatus) -> int

        Synopsis
        -----
        To get the per particle vector attribute of the given name.

        Returns: 
        ----- 
        The size of the returned vector array

        Parameters:
        -----
        attrName: MString
        	[in] -> The input attribute name 

        array: MVectorArray
        	[out] -> The returned vector array 

        ReturnStatus: MFnParticleSystem.MStatus
        	[out] -> The return status


        '''
        pass

    @overload
    def getPerParticleAttribute(self, attrName: MString,
                        array: MDoubleArray,
                        ReturnStatus: MFnParticleSystem.MStatus): 
        '''
        getPerParticleAttribute(self, attrName: MString,
                        array: MDoubleArray,
                        ReturnStatus: MFnParticleSystem.MStatus) -> int

        Synopsis
        -----
        To get the per particle double attribute of the given name.

        Returns: 
        ----- 
        The size of the returned double array

        Parameters:
        -----
        attrName: MString
        	[in] -> The input attribute name 

        array: MDoubleArray
        	[out] -> The returned double array 

        ReturnStatus: MFnParticleSystem.MStatus
        	[out] -> The return status


        '''
        pass

    @overload
    def setPerParticleAttribute(self, attrName: MString,
                        array: MVectorArray,
                        ReturnStatus: MFnParticleSystem.MStatus): 
        '''
        setPerParticleAttribute(self, attrName: MString,
                        array: MVectorArray,
                        ReturnStatus: MFnParticleSystem.MStatus)

        Synopsis
        -----
        To set the per particle vector attribute of the given name with
        the given values.

        Returns:
        -----
        None

        Parameters:
        -----
        attrName: MString
        	[in] -> The input attribute name 

        array: MVectorArray
        	[in] -> The input vector array 

        ReturnStatus: MFnParticleSystem.MStatus
        	[out] -> The return status


        '''
        pass

    @overload
    def setPerParticleAttribute(self, attrName: MString,
                        array: MDoubleArray,
                        ReturnStatus: MFnParticleSystem.MStatus): 
        '''
        setPerParticleAttribute(self, attrName: MString,
                        array: MDoubleArray,
                        ReturnStatus: MFnParticleSystem.MStatus)

        Synopsis
        -----
        To set the per particle double attribute of the given name with
        the given values.

        Returns:
        -----
        None

        Parameters:
        -----
        attrName: MString
        	[in] -> The input attribute name 

        array: MDoubleArray
        	[in] -> The input double array 

        ReturnStatus: MFnParticleSystem.MStatus
        	[out] -> The return status


        '''
        pass

    def isPerParticleIntAttribute(self, attrName: MString,
                        ReturnStatus: MFnParticleSystem.MStatus): 
        '''
        isPerParticleIntAttribute(self, attrName: MString,
                        ReturnStatus: MFnParticleSystem.MStatus) -> bool

        Synopsis
        -----
        To check if the input attribute is a per particle integer
        attribute.

        Returns:
        -----
        None

        Parameters:
        -----
        attrName: MString
        	[in] -> The input attribute name 

        ReturnStatus: MFnParticleSystem.MStatus
        	[out] -> The return status


        '''
        pass

    def isPerParticleDoubleAttribute(self, attrName: MString,
                        ReturnStatus: MFnParticleSystem.MStatus): 
        '''
        isPerParticleDoubleAttribute(self, attrName: MString,
                        ReturnStatus: MFnParticleSystem.MStatus) -> bool

        Synopsis
        -----
        To check if the input attribute is a per particle double
        attribute.

        Returns:
        -----
        None

        Parameters:
        -----
        attrName: MString
        	[in] -> The input attribute name 

        ReturnStatus: MFnParticleSystem.MStatus
        	[out] -> The return status


        '''
        pass

    def isPerParticleVectorAttribute(self, attrName: MString,
                        ReturnStatus: MFnParticleSystem.MStatus): 
        '''
        isPerParticleVectorAttribute(self, attrName: MString,
                        ReturnStatus: MFnParticleSystem.MStatus) -> bool

        Synopsis
        -----
        To check if the input attribute is a per particle vector
        attribute.

        Returns:
        -----
        None

        Parameters:
        -----
        attrName: MString
        	[in] -> The input attribute name 

        ReturnStatus: MFnParticleSystem.MStatus
        	[out] -> The return status


        '''
        pass

    def isDeformedParticleShape(self, ReturnStatus: MFnParticleSystem.MStatus): 
        '''
        isDeformedParticleShape(self, ReturnStatus: MFnParticleSystem.MStatus) -> bool

        Synopsis
        -----
        To return if this particle shape is deformed.

        Returns: 
        ----- 
        true  particle shape is deformed, false otherwise.

        Parameters:
        -----
        ReturnStatus: MFnParticleSystem.MStatus
        	[out] -> Status code


        '''
        pass

    def deformedParticleShape(self, ReturnStatus: MFnParticleSystem.MStatus): 
        '''
        deformedParticleShape(self, ReturnStatus: MFnParticleSystem.MStatus) -> MObject

        Synopsis
        -----
        To get the deformed particleShape.

        Returns: 
        ----- 
        The particle shape connecting to the output of the deformer(s)

        Parameters:
        -----
        ReturnStatus: MFnParticleSystem.MStatus
        	[out] -> Status code


        '''
        pass

    def originalParticleShape(self, ReturnStatus: MFnParticleSystem.MStatus): 
        '''
        originalParticleShape(self, ReturnStatus: MFnParticleSystem.MStatus) -> MObject

        Synopsis
        -----
        To get the original particleShape.

        Returns: 
        ----- 
        The particle shape connecting to the input of the deformer(s)

        Parameters:
        -----
        ReturnStatus: MFnParticleSystem.MStatus
        	[out] -> Status code


        '''
        pass

class RenderType:
    '''Ways in which particles can be rendered. 
    Non-functional class.  Values for this enum:
    kCloud
    kTube
    kBlobby
    kMultiPoint
    kMultiStreak
    kNumeric
    kPoints
    kSpheres
    kSprites
    kStreak
    '''

    def __init__(self):
        pass

    def kCloud(self):
        '''This is an enum of RenderType.
        - Description:  
        - Value: 0
        '''
        pass

    def kTube(self):
        '''This is an enum of RenderType.
        - Description:  
        - Value: 1
        '''
        pass

    def kBlobby(self):
        '''This is an enum of RenderType.
        - Description:  
        - Value: 2
        '''
        pass

    def kMultiPoint(self):
        '''This is an enum of RenderType.
        - Description:  
        - Value: 3
        '''
        pass

    def kMultiStreak(self):
        '''This is an enum of RenderType.
        - Description:  
        - Value: 4
        '''
        pass

    def kNumeric(self):
        '''This is an enum of RenderType.
        - Description:  
        - Value: 5
        '''
        pass

    def kPoints(self):
        '''This is an enum of RenderType.
        - Description:  
        - Value: 6
        '''
        pass

    def kSpheres(self):
        '''This is an enum of RenderType.
        - Description:  
        - Value: 7
        '''
        pass

    def kSprites(self):
        '''This is an enum of RenderType.
        - Description:  
        - Value: 8
        '''
        pass

    def kStreak(self):
        '''This is an enum of RenderType.
        - Description:  
        - Value: 9
        '''
        pass

class MFnPfxGeometry:
    '''PfxGeometry node function set.
This is the function set for paint effects objects.
PfxGeometry is the parent class for the stroke and pfxHair node.
The output geometry for pfxHair and stroke nodes may be accessed
through this class.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kPfxGeometry.Reimplemented from MFnDagNode.

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
        className(self) -> MFnPfxGeometry.OPENMAYA_MAJOR_NAMESPACE_OPENchar*

        Synopsis
        -----
        Returns the name of this class. Return the class name :
        "MFnPfxGeometry".

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getLineData(self, mainLines: MRenderLineArray,
                        leafLines: MRenderLineArray,
                        flowerLines: MRenderLineArray,
                        doLines: bool,
                        doTwist: bool,
                        doWidth: bool,
                        doFlatness: bool,
                        doParameter: bool,
                        doColor: bool,
                        doIncandescence: bool,
                        doTransparency: bool,
                        worldSpace: bool): 
        '''
        getLineData(self, mainLines: MRenderLineArray,
                        leafLines: MRenderLineArray,
                        flowerLines: MRenderLineArray,
                        doLines: bool,
                        doTwist: bool,
                        doWidth: bool,
                        doFlatness: bool,
                        doParameter: bool,
                        doColor: bool,
                        doIncandescence: bool,
                        doTransparency: bool,
                        worldSpace: bool)

        Synopsis
        -----
        Get line data for the current output pfx tubes. The passed in
        arrays will be filled with pointers to MrenderLine classes. If
        there are no leaves or flowers then the passed in leafLine and
        flowerLine arrays will be left empty. Arrays are generated for
        only the specified attributes. This routine creates the memory
        for the arrays that it computes. This memory can only be released
        using the deleteArray method on the MRenderLineArray class.
        DeleteArray should be called for the mainLine, leafLine, and
        flowerLine variables when done. These variables wrap the returned
        data and allow access but the MRenderLineArray destructer does
        not delete this wrapped memory, so one must use
        MRenderLineArray::deleteArray(). The MRenderLine, MVectorArray
        and MDoubleArrays returned from MRenderLineArray will point to
        deleted memory after calling deleteArray, so be careful to only
        call deleteArray when finished using the line data(or copy the
        arrays first).

        Returns:
        -----
        None

        Parameters:
        -----
        mainLines: MRenderLineArray
        	[out] -> primary 

        leafLines: MRenderLineArray
        	[out] -> leaf 

        flowerLines: MRenderLineArray
        	[out] -> flower 

        doLines: bool
        	[in] -> create line(vertex) arrays 

        doTwist: bool
        	[in] -> create twist arrays 

        doWidth: bool
        	[in] -> create width arrays 

        doFlatness: bool
        	[in] -> create flatness arrays 

        doParameter: bool
        	[in] -> create parameter arrays 

        doColor: bool
        	[in] -> create color arrays 

        doIncandescence: bool
        	[in] -> create incandescence arrays 

        doTransparency: bool
        	[in] -> create transparency arrays 

        worldSpace: bool
        	[in] -> compute lines in worldspace, instead of the stroke objectspace


        '''
        pass

    def getBoundingBox(self, min: double,
                        max: double): 
        '''
        getBoundingBox(self, min: double,
                        max: double)

        Synopsis
        -----
        Gets the bounding box of the specified geometry. The passed in
        double arrays will be filled with minimum and maximum coordinates
        of the geometry.

        Returns:
        -----
        None

        Parameters:
        -----
        min: double
        	[out] -> minimum coordinates 

        max: double
        	[out] -> maximum coordinates


        '''
        pass

class MFnRadialField:
    '''Function set for Radial Fields.
Function set for creation, edit, and query of Radial Fields.
A radial field pushes objects directly away or pulls them
directly toward itself, like a magnet.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kRadial.Reimplemented from MFnField.

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

    def radialType(self, ReturnStatus: MFnRadialField.MStatus): 
        '''
        radialType(self, ReturnStatus: MFnRadialField.MStatus) -> double

        Synopsis
        -----
        Returns a type that controls the way the radial field is
        attenuated.

        Returns: 
        ----- 
        A value representing a type of radial field attenuation.  A value
        of 1 uses the magnitude, attenuation, and distance settings from
        the field to determine the net force of the radial field.  A
        value of 0 will use the ratio of the absolute distance and the
        maximum distance setting.  A value between 0 and 1 will create a
        linear blend between the two types.

        Parameters:
        -----
        ReturnStatus: MFnRadialField.MStatus
        	[out] -> Status code


        '''
        pass

    def setType(self, value: double): 
        '''
        setType(self, value: double)

        Synopsis
        -----
        Sets a radial field type that controls the way the field is
        attenuated.

        Returns:
        -----
        None

        Parameters:
        -----
        value: double
        	[in] -> A value representing a type of radial field attenuation. 


        '''
        pass

class MFnTurbulenceField:
    '''Function set for Turbulence Fields.
Function set for creation, edit, and query of Turbulence Fields.
A turbulence field causes irregularities in the motion of
affected objects. These irregularities are also called noise or
jitter.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kTurbulence.Reimplemented from MFnField.

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

    def frequency(self, ReturnStatus: MFnTurbulenceField.MStatus): 
        '''
        frequency(self, ReturnStatus: MFnTurbulenceField.MStatus) -> double

        Synopsis
        -----
        Returns the frequency parameter that generates irregularities in
        the fields motion.

        Returns: 
        ----- 
        A value representing a noise generation parameter.

        Parameters:
        -----
        ReturnStatus: MFnTurbulenceField.MStatus
        	[out] -> Status code


        '''
        pass

    def setFrequency(self, value: double): 
        '''
        setFrequency(self, value: double)

        Synopsis
        -----
        Sets the frequency parameter of the Perlin noise function used by
        the turbulence field. Values are positive, with larger values
        causing more frequent irregularities in the motion.

        Returns:
        -----
        None

        Parameters:
        -----
        value: double
        	[in] -> A value representing a noise generation parameter.


        '''
        pass

    def phase(self, ReturnStatus: MFnTurbulenceField.MStatus): 
        '''
        phase(self, ReturnStatus: MFnTurbulenceField.MStatus) -> double

        Synopsis
        -----
        Returns the phase shift parameter that influences the direction
        of the turbulence field disruption. Currently this returns the
        phaseZ attribute, which was called simply phase in versions of
        Maya prior to 3.0.

        Returns: 
        ----- 
        A value representing a noise generation parameter.

        Parameters:
        -----
        ReturnStatus: MFnTurbulenceField.MStatus
        	[out] -> Status code


        '''
        pass

    def setPhase(self, value: double): 
        '''
        setPhase(self, value: double)

        Synopsis
        -----
        Sets the phase shift parameter of the Perlin noise function used
        by the turbulence field. Both positive and negative values are
        legal and influence the direction of the disruption. Sets the
        phaseZ parameter, which was called simply phase in versions of
        Maya prior to 3.0.

        Returns:
        -----
        None

        Parameters:
        -----
        value: double
        	[in] -> A value representing a noise generation parameter.


        '''
        pass

class MFnUniformField:
    '''Function set for Uniform Fields.
Function set for creation, edit, and query of Uniform Fields.
A uniform field pushes objects uniformly in a single direction.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kUniform.Reimplemented from MFnField.

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

    def direction(self, ReturnStatus: MFnUniformField.MStatus): 
        '''
        direction(self, ReturnStatus: MFnUniformField.MStatus) -> MVector

        Synopsis
        -----
        Returns the direction the uniform field pushes objects.

        Returns: 
        ----- 
        A vector representing direction.

        Parameters:
        -----
        ReturnStatus: MFnUniformField.MStatus
        	[out] -> Status code


        '''
        pass

    def setDirection(self, uniformDirection: MVector): 
        '''
        setDirection(self, uniformDirection: MVector)

        Synopsis
        -----
        Sets the direction the uniform field pushes objects.

        Returns:
        -----
        None

        Parameters:
        -----
        uniformDirection: MVector
        	[in] -> A vector representing direction.


        '''
        pass

class MFnVolumeAxisField:
    '''Function set for VolumeAxis Fields.
Function set for creation, edit, and query of VolumeAxis Fields.
A volume axis field provides in field form some of the speed
controls of volume emitters.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kVolumeAxis.Reimplemented from MFnField.

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

    def invertAttenuation(self, ReturnStatus: MFnVolumeAxisField.MStatus): 
        '''
        invertAttenuation(self, ReturnStatus: MFnVolumeAxisField.MStatus) -> bool

        Synopsis
        -----
        Returns the value of the invertAttenuation attribute for the
        field force.

        Returns: 
        ----- 
        true Field is strongest close to volume outer boundary.  false
        Field is strongest close to volume center.

        Parameters:
        -----
        ReturnStatus: MFnVolumeAxisField.MStatus
        	[out] -> Status code


        '''
        pass

    def direction(self, ReturnStatus: MFnVolumeAxisField.MStatus): 
        '''
        direction(self, ReturnStatus: MFnVolumeAxisField.MStatus) -> MVector

        Synopsis
        -----
        Returns the direction attribute for the field force.

        Returns: 
        ----- 
        A vector representing direction.

        Parameters:
        -----
        ReturnStatus: MFnVolumeAxisField.MStatus
        	[out] -> Status code


        '''
        pass

    def speedAlongAxis(self, ReturnStatus: MFnVolumeAxisField.MStatus): 
        '''
        speedAlongAxis(self, ReturnStatus: MFnVolumeAxisField.MStatus) -> double

        Synopsis
        -----
        Returns the alongAxis attribute of the field.

        Returns: 
        ----- 
        A double value representing the speed along axis.

        Parameters:
        -----
        ReturnStatus: MFnVolumeAxisField.MStatus
        	[out] -> Status code


        '''
        pass

    def speedAroundAxis(self, ReturnStatus: MFnVolumeAxisField.MStatus): 
        '''
        speedAroundAxis(self, ReturnStatus: MFnVolumeAxisField.MStatus) -> double

        Synopsis
        -----
        Returns the aroundAxis attribute of the field.

        Returns: 
        ----- 
        A double value representing the speed around axis.

        Parameters:
        -----
        ReturnStatus: MFnVolumeAxisField.MStatus
        	[out] -> Status code


        '''
        pass

    def speedAwayFromAxis(self, ReturnStatus: MFnVolumeAxisField.MStatus): 
        '''
        speedAwayFromAxis(self, ReturnStatus: MFnVolumeAxisField.MStatus) -> double

        Synopsis
        -----
        Returns the awayFromAxis attribute of the field.

        Returns: 
        ----- 
        A double value representing the speed away from axis.

        Parameters:
        -----
        ReturnStatus: MFnVolumeAxisField.MStatus
        	[out] -> Status code


        '''
        pass

    def speedAwayFromCenter(self, ReturnStatus: MFnVolumeAxisField.MStatus): 
        '''
        speedAwayFromCenter(self, ReturnStatus: MFnVolumeAxisField.MStatus) -> double

        Synopsis
        -----
        Returns the awayFromCenter attribute of the field.

        Returns: 
        ----- 
        A double value representing the speed away from center.

        Parameters:
        -----
        ReturnStatus: MFnVolumeAxisField.MStatus
        	[out] -> Status code


        '''
        pass

    def directionalSpeed(self, ReturnStatus: MFnVolumeAxisField.MStatus): 
        '''
        directionalSpeed(self, ReturnStatus: MFnVolumeAxisField.MStatus) -> double

        Synopsis
        -----
        Returns the directionalSpeed attribute of the field.

        Returns: 
        ----- 
        A double value representing the directional speed.

        Parameters:
        -----
        ReturnStatus: MFnVolumeAxisField.MStatus
        	[out] -> Status code


        '''
        pass

    def turbulence(self, ReturnStatus: MFnVolumeAxisField.MStatus): 
        '''
        turbulence(self, ReturnStatus: MFnVolumeAxisField.MStatus) -> double

        Synopsis
        -----
        Returns the turbulence intensity of the field.

        Returns: 
        ----- 
        A double value representing the turbulence intensity.

        Parameters:
        -----
        ReturnStatus: MFnVolumeAxisField.MStatus
        	[out] -> Status code


        '''
        pass

    def turbulenceSpeed(self, ReturnStatus: MFnVolumeAxisField.MStatus): 
        '''
        turbulenceSpeed(self, ReturnStatus: MFnVolumeAxisField.MStatus) -> double

        Synopsis
        -----
        Returns the rate of change of the turbulence over time.

        Returns: 
        ----- 
        A double value representing the turbulence speed.

        Parameters:
        -----
        ReturnStatus: MFnVolumeAxisField.MStatus
        	[out] -> Status code


        '''
        pass

    def turbulenceFrequency(self, ReturnStatus: MFnVolumeAxisField.MStatus): 
        '''
        turbulenceFrequency(self, ReturnStatus: MFnVolumeAxisField.MStatus) -> MVector

        Synopsis
        -----
        Returns the turbulenceFrequency attribute for the field force.

        Returns: 
        ----- 
        A vector representing frequency or scale of the turbulence.

        Parameters:
        -----
        ReturnStatus: MFnVolumeAxisField.MStatus
        	[out] -> Status code


        '''
        pass

    def turbulenceOffset(self, ReturnStatus: MFnVolumeAxisField.MStatus): 
        '''
        turbulenceOffset(self, ReturnStatus: MFnVolumeAxisField.MStatus) -> MVector

        Synopsis
        -----
        Returns the turbulenceOffset attribute for the field force.

        Returns: 
        ----- 
        A vector representing an offset or translation of the turbulence.

        Parameters:
        -----
        ReturnStatus: MFnVolumeAxisField.MStatus
        	[out] -> Status code


        '''
        pass

    @overload
    def detailTurbulence(self, ReturnStatus: MFnVolumeAxisField.MStatus): 
        '''
        detailTurbulence(self, ReturnStatus: MFnVolumeAxisField.MStatus) -> double

        Synopsis
        -----
        Returns the intensity of a second higher frequency turbulence.

        Returns: 
        ----- 
        A double value for the intensity of fine scale turbulence.

        Parameters:
        -----
        ReturnStatus: MFnVolumeAxisField.MStatus
        	[out] -> Status code


        '''
        pass

    def setInvertAttenuation(self, enable: bool): 
        '''
        setInvertAttenuation(self, enable: bool)

        Synopsis
        -----
        Enables the field will be stronger the closer to the edge of the
        volume a point is.

        Returns:
        -----
        None

        Parameters:
        -----
        enable: bool
        	[in] -> Flag to invert falloff of intensity.


        '''
        pass

    def setDirection(self, direction: MVector): 
        '''
        setDirection(self, direction: MVector)

        Synopsis
        -----
        Sets the direction attribute for the field force.

        Returns:
        -----
        None

        Parameters:
        -----
        direction: MVector
        	[in] -> A vector representing direction.


        '''
        pass

    def setSpeedAlongAxis(self, speed: double): 
        '''
        setSpeedAlongAxis(self, speed: double)

        Synopsis
        -----
        Sets the speed along axis attribute for the field force.

        Returns:
        -----
        None

        Parameters:
        -----
        speed: double
        	[in] -> A double representing the speed along axis.


        '''
        pass

    def setSpeedAroundAxis(self, speed: double): 
        '''
        setSpeedAroundAxis(self, speed: double)

        Synopsis
        -----
        Sets the speed around axis attribute for the field force.

        Returns:
        -----
        None

        Parameters:
        -----
        speed: double
        	[in] -> A double representing the speed around axis.


        '''
        pass

    def setSpeedAwayFromAxis(self, speed: double): 
        '''
        setSpeedAwayFromAxis(self, speed: double)

        Synopsis
        -----
        Sets the speed away from axis attribute for the field force.

        Returns:
        -----
        None

        Parameters:
        -----
        speed: double
        	[in] -> A double representing the speed away from axis.


        '''
        pass

    def setSpeedAwayFromCenter(self, speed: double): 
        '''
        setSpeedAwayFromCenter(self, speed: double)

        Synopsis
        -----
        Sets the speed away from center attribute for the field force.

        Returns:
        -----
        None

        Parameters:
        -----
        speed: double
        	[in] -> A double representing the speed away from center.


        '''
        pass

    def setDirectionalSpeed(self, speed: double): 
        '''
        setDirectionalSpeed(self, speed: double)

        Synopsis
        -----
        Sets the directional speed attribute for the field force.

        Returns:
        -----
        None

        Parameters:
        -----
        speed: double
        	[in] -> A double representing the directional speed.


        '''
        pass

    def setTurbulence(self, value: double): 
        '''
        setTurbulence(self, value: double)

        Synopsis
        -----
        Sets the turbulence attribute for the field force.

        Returns:
        -----
        None

        Parameters:
        -----
        value: double
        	[in] -> A double representing the turbulence intensity.


        '''
        pass

    def setTurbulenceSpeed(self, value: double): 
        '''
        setTurbulenceSpeed(self, value: double)

        Synopsis
        -----
        Sets the turbulence speed attribute for the field force.

        Returns:
        -----
        None

        Parameters:
        -----
        value: double
        	[in] -> A double representing the rate of change of the turbulence.


        '''
        pass

    def setTurbulenceFrequency(self, value: MVector): 
        '''
        setTurbulenceFrequency(self, value: MVector)

        Synopsis
        -----
        Sets the turbulenceFrequency attribute for the field force.

        Returns:
        -----
        None

        Parameters:
        -----
        value: MVector
        	[in] -> A vector representing the frequency of turbulence.


        '''
        pass

    def setTurbulenceOffset(self, value: MVector): 
        '''
        setTurbulenceOffset(self, value: MVector)

        Synopsis
        -----
        Sets the turbulenceOffset attribute for the field force.

        Returns:
        -----
        None

        Parameters:
        -----
        value: MVector
        	[in] -> A vector representing the translation of turbulence.


        '''
        pass

    @overload
    def detailTurbulence(self, value: double): 
        '''
        detailTurbulence(self, value: double)

        Synopsis
        -----
        Sets the detailTurbulence attribute for the field force.

        Returns:
        -----
        None

        Parameters:
        -----
        value: double
        	[in] -> A double representing the intensity of a second higher frequency turbulence.


        '''
        pass

class MFnVortexField:
    '''Function set for Vortex Fields.
Function set for creation, edit, and query of Vortex Fields.
A vortex field pulls objects in a circular direction, like a
whirlpool or tornado.
'''
    def __init__(self):
        pass


    def type(self): 
        '''
        type(self) -> MFn.MFn

        Synopsis
        -----
        Function set type. Return the class type :
        MFn::kVortex.Reimplemented from MFnField.

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

    def axis(self, ReturnStatus: MFnVortexField.MStatus): 
        '''
        axis(self, ReturnStatus: MFnVortexField.MStatus) -> MVector

        Synopsis
        -----
        Returns the axis around which the vortex field exerts it's force.

        Returns: 
        ----- 
        A vector representing an axis.

        Parameters:
        -----
        ReturnStatus: MFnVortexField.MStatus
        	[out] -> Status code


        '''
        pass

    def setAxis(self, axisVector: MVector): 
        '''
        setAxis(self, axisVector: MVector)

        Synopsis
        -----
        Sets the axis around which the vortex field exerts it's force.

        Returns:
        -----
        None

        Parameters:
        -----
        axisVector: MVector
        	[in] -> A vector representing an axis.


        '''
        pass

class MHairSystem:
    '''Interface with Maya's Dynamic Hair System.
MHairSystem provides an interface with Maya's Dynamic Hair System.
At present, this interface only supports the ability to override
the geometry collision component of hair. There is currently no
support for overriding the other hair collision components (i.e.
implicit object collision and hair self collision).
The rationale for providing a hair collision API is to allow the
user to override Maya's internal algorithm which is a high-
performance simulation. There is an example plug-in provided in
the Developer's Toolkit called hairCollisionSolver.cpp.
'''
    def __init__(self):
        pass


    def registerCollisionSolverCollide(self, fnPtr: MHairSystemCollisionSolverCollideFnPtr): 
        '''
        registerCollisionSolverCollide(self, fnPtr: MHairSystemCollisionSolverCollideFnPtr)

        Synopsis
        -----
        Register the user-supplied collision solver `fnPtr' with Maya.
        This method will be invoked per-hair times the number of
        iterations specified by the hairSystem node and the method can be
        used to perfrom several functions:The effect of registering a
        collision solver is to override Maya's internal solver, thus ALL
        hair to object collision detection will now route into your
        callback. To revert to Maya's internal solver, de-register the
        solver using unregisterCollisionSolverCollide(). Also note that
        exatly one collision solver can be registered. If a second solver
        is registered, it overrides the previous definition.The hair that
        gets passed into your collision solver is defined by three
        parameters: the desired position where Maya's hair system wants
        the hair to be at the current time, the previous position (where
        the hair was at the last frame), and the width of the hair. These
        three parameters are represented as arrays. The first element in
        each array corresponds to the root of the hair, and the remaining
        elements are the points along the hair with the tip as the last
        element. Maya has the ability for the user to lock the root and
        or tip so that they cannot be moved. This locking is specified by
        the `startIndex' and `endIndex' parameters. A pair of hair points
        forms what is termed a "hair segment", and each segment is thus a
        moving cylinder in which each end can have a different width.The
        goal of your collision solver is to detect any collisions between
        the hair as it moves linearly from previous towards its desired
        position and any collision objects. As the hair is moving and the
        collision objects are moving, the collision calculation is a
        complex time-based equation. If you take into consideration that
        the hair has variable width, things are even more
        complicated.Since you have full access to computing and reacting
        to the collision, you can make assumptions (such has collision
        objects can't move) then you can get speed improvements over
        Maya's built-in solver. You can also go the other way:
        implementing very accurate continuous-time collision
        detection.The MHairSystemCollisionSolverCollideFnPtr type is
        defined as follows.

        Returns:
        -----
        None

        Parameters:
        -----
        fnPtr: MHairSystemCollisionSolverCollideFnPtr
        	[in] -> Pointer to a function which implements the user's collision solver algorithm.


        '''
        pass

    def registerCollisionSolverPreFrame(self, fnPtr: MHairSystemCollisionSolverPreFrameFnPtr): 
        '''
        registerCollisionSolverPreFrame(self, fnPtr: MHairSystemCollisionSolverPreFrameFnPtr)

        Synopsis
        -----
        Register the user-supplied pre-frame method `fnPtr' with Maya.
        This method will be invoked at the start of each frame.Note that
        this method is optional. You only need to define this method if
        you want to perform pre-frame initialisation. One strategy is to
        perform expensive pre-preprocessing once per frame so that it can
        be utilised during your collide() callback. If there is more than
        one collision geometry associated with the hair system, be sure
        to store the pre-processed data so that it can be referenced in
        the order the objects are returned via the getCollisionObject()
        call.Note: if you decide to define private data, you will need to
        manage it somehow. You will need to be able to find the data
        again to reuse at the next frame and delete it when the collision
        object is removed from the hairSystem's collision list. The best
        way to do this is to implement a listener method which watches
        for changes to the hair system's collision object list attribute
        and clean up your private data as appropriate.The
        MHairSystemCollisionSolverPreFrameFnPtr type is defined as
        follows.

        Returns:
        -----
        None

        Parameters:
        -----
        fnPtr: MHairSystemCollisionSolverPreFrameFnPtr
        	[in] -> Pointer to a function which implements the user's pre-frame algorithm.


        '''
        pass

    @overload
    def getCollisionObject(self, hairSystem: MObject,
                        index: int,
                        ReturnStatus: MHairSystem.MStatus): 
        '''
        getCollisionObject(self, hairSystem: MObject,
                        index: int,
                        ReturnStatus: MHairSystem.MStatus) -> MObject

        Synopsis
        -----
        Returns the requested collision object from the hair system.
        Status codes

        Returns: 
        ----- 
        The requested collision object, or the NULL object if not found.

        Parameters:
        -----
        hairSystem: MObject
        	[in] -> The hair system. 

        index: int
        	[in] -> Which collision object to retrieve. The objectIndex parameter passed into your pre-frame callback or collision solver callback can be specified here. 

        ReturnStatus: MHairSystem.MStatus
        	[out] -> Status code.


        '''
        pass

    @overload
    def getCollisionObject(self, hairSystem: MObject,
                        objects: MObjectArray,
                        logicalIndices: MIntArray): 
        '''
        getCollisionObject(self, hairSystem: MObject,
                        objects: MObjectArray,
                        logicalIndices: MIntArray)

        Synopsis
        -----
        Returns all collision objects for the hair system.

        Returns:
        -----
        None

        Parameters:
        -----
        hairSystem: MObject
        	[in] -> The hair system. 

        objects: MObjectArray
        	[out] -> Returns the collision objects in the same order that index-based 

        logicalIndices: MIntArray
        	[out] -> Logical indices of each collision object returned.


        '''
        pass

    @overload
    def getFollicle(self, hairSystem: MObject,
                        index: int,
                        ReturnStatus: MHairSystem.MStatus): 
        '''
        getFollicle(self, hairSystem: MObject,
                        index: int,
                        ReturnStatus: MHairSystem.MStatus) -> MObject

        Synopsis
        -----
        Returns the requested follicle from the hair system. Status codes

        Returns: 
        ----- 
        The requested follicle, or the NULL object if not found.

        Parameters:
        -----
        hairSystem: MObject
        	[in] -> The hair system. 

        index: int
        	[in] -> Which follicle to retrieve. The follicleIndex parameter passed into your collision solver callback can be specified here. 

        ReturnStatus: MHairSystem.MStatus
        	[out] -> Status code.


        '''
        pass

    @overload
    def getFollicle(self, hairSystem: MObject,
                        follicles: MObjectArray,
                        logicalIndices: MIntArray): 
        '''
        getFollicle(self, hairSystem: MObject,
                        follicles: MObjectArray,
                        logicalIndices: MIntArray)

        Synopsis
        -----
        Returns all follicles for the hair system.

        Returns:
        -----
        None

        Parameters:
        -----
        hairSystem: MObject
        	[in] -> The hair system. 

        follicles: MObjectArray
        	[out] -> Returns the array of follicles in the same order that the index-based 

        logicalIndices: MIntArray
        	[out] -> Logical indices of each follicle returned.


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

class MRenderLine:
    '''Class for accessing paint effects output curve data.
A
MRenderLine provides access to paint effects curve rendering info. This
class contains arrays for per vertex attributes along an
individual curve: line: the vertices in worldspace twist: a twist
vector at each vertice width: the tube widths flatness: the tube
flatness along the twist vector direction parameter: the u
parameterization value for each vertice color: color rgb value
for each vertice incandescence: incandescence rgb value for each
vertice transpareancy: transparency rgb value for each vertice
'''
    def __init__(self):
        pass


    def getLine(self): 
        '''
        getLine(self) -> MVectorArray

        Synopsis
        -----
        Return the array of vertices along the curve.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getTwist(self): 
        '''
        getTwist(self) -> MVectorArray

        Synopsis
        -----
        Return the array of twist vectors along the curve.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getWidth(self): 
        '''
        getWidth(self) -> MDoubleArray

        Synopsis
        -----
        Return the array of tube widths along the curve.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getFlatness(self): 
        '''
        getFlatness(self) -> MDoubleArray

        Synopsis
        -----
        Return the array of flatness along the curve.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getParameter(self): 
        '''
        getParameter(self) -> MDoubleArray

        Synopsis
        -----
        Return the array of parameter along the curve.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getColor(self): 
        '''
        getColor(self) -> MVectorArray

        Synopsis
        -----
        Return the array of colors along the curve.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getIncandescence(self): 
        '''
        getIncandescence(self) -> MVectorArray

        Synopsis
        -----
        Return the array of incandescence along the curve.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def getTransparency(self): 
        '''
        getTransparency(self) -> MVectorArray

        Synopsis
        -----
        Return the array of transparency along the curve.

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

class MRenderLineArray:
    '''Class for accessing paint effects output curve data.
A
MRenderLineArray provides access to paint effects curve rendering info. This
class contains arrays for per vertex attributes along an
individual curve: line: the vertices in worldspace twist: a twist
vector at each vertex width: the tube widths flatness: the tube
flatness along the twist vector direction parameter: the u
parameterization value for each vertex color: color rgb value for
each vertex incandescence: incandescence rgb value for each
vertex transpareancy: transparency rgb value for each vertex
'''
    def __init__(self):
        pass


    def deleteArray(self): 
        '''
        deleteArray(self)

        Synopsis
        -----
        Free up the memory held in the render line array. This should be
        called once only and only on one copy of the MRenderLineArray.
        (Assignment copies internal pointer data rather than the data its
        self)

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
        Return the number of entries in the array.

        Returns:
        -----
        None

        Parameters:
        -----
            None

        '''
        pass

    def renderLine(self, index: int,
                        status: MRenderLineArray.MStatus): 
        '''
        renderLine(self, index: int,
                        status: MRenderLineArray.MStatus) -> MRenderLine

        Synopsis
        -----
        Return the render line at the defined index.

        Returns: 
        ----- 
        The render line

        Parameters:
        -----
        index: int
        	[in] -> index of the render line to return 

        status: MRenderLineArray.MStatus
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

