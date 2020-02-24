from manimlib.imports import *
import mytool.FFT_Song as FFT_Song

class Part0(Scene):
    def construct(self):
        fun1 = lambda x: np.cos(2 * PI *x * 2)
        fg1 = FunctionGraph(fun1,color=MAROON_B)
        equation1 = TexMobject("y=cos(2\\pi x\\times 2)")
        equation1.set_y(2 - FRAME_Y_RADIUS - 0.5)
        g1 = VGroup(fg1,equation1)

        fun2 = lambda x: np.cos(2 * PI *x * 4 + 45/180*PI)
        fg2 = FunctionGraph(fun2,color=RED_E)
        equation2 = TexMobject("y=cos(2\\pi x\\times 4+{45\\over 180}\\pi )")
        equation2.set_y(2 - FRAME_Y_RADIUS -0.5)
        g2 = VGroup(fg2,equation2)

        fun3 = lambda x: sum([
                np.cos(2 * PI *x * 2),
                np.cos(2 * PI *x * 4 + 45/180*PI)
            ])
        fg3 = FunctionGraph(fun3,color="#00FF33")
        equation3 = TexMobject("y=cos(2\\pi x\\times 2)+cos(2\\pi x\\times 4+{45\\over 180}\\pi )")
        equation3.set_y(2 - FRAME_Y_RADIUS - 0.5)
        g3 = VGroup(fg3,equation3)

        axes1 = Axes(y_min=-1, y_max=1.5)
        axes2 = Axes(y_min=-2, y_max=2.5)
        self.play( Write( axes1 ) )
        self.wait(1)
        self.play(ShowCreation(g1))
        self.wait(2)
        self.play(ApplyMethod( g1.scale,0.4) )
        self.play( ApplyMethod( g1.shift,( 3-FRAME_X_RADIUS, FRAME_Y_RADIUS ,0) ) )
        self.wait(2)
        self.play(ShowCreation(g2))
        self.wait(2)
        self.play(ApplyMethod( g2.scale,0.4) )
        self.play( ApplyMethod( g2.shift,( FRAME_X_RADIUS - 3, FRAME_Y_RADIUS ,0) ) )
        self.wait(2)

        add = TexMobject("+")
        add.set_y(FRAME_Y_RADIUS-0.5)
        self.play(ShowCreation(add))
        self.play( Transform(axes1,axes2) )
        self.wait(1)

        self.play(ShowCreation(g3))
        self.wait(2)

class Part0_5(MovingCameraScene):
    def construct(self):
        fun1 = lambda x: np.cos(2 * PI *x * 60)
        fg1 = FunctionGraph(fun1,color=MAROON_B)

        fun2 = lambda x: np.cos(2 * PI *x * 0.6)
        fg2 = FunctionGraph(fun2,color=RED_E)
        
        self.play(ShowCreation(fg1))
        self.play(Transform(fg1,fg2))
        self.wait(2)

class Part1(MovingCameraScene):
    def construct(self):

        frame_width = 50
        
        params = FFT_Song.getSongFormula("jojoVoice2.wav",200)
        print(params)
        self.camera.set_frame_center((FRAME_X_RADIUS,0,0))
        self.camera.set_frame_height(1000)
        self.camera.set_frame_width(frame_width)
        fun = lambda x: sum([
                param[0] * np.sin(2 * PI *param[1]* x + param[2]/180*PI)
                for param in params
            ])
        # for i in range(1):
        #     f = FunctionGraph(
        #         fun,
        #         color=GREEN,
        #         x_max=100 * (i+1),
        #         x_min=100 * i
        #     )
        #     self.play(ShowCreation(f))

        curve = VMobject()
        curve.set_points_smoothly([
            (a,0.1*fun(a),0)
            for a in np.linspace(0, frame_width, 10000)
        ])
        curve.set_stroke(YELLOW, 1)
        # self.play(ShowCreation(curve))
        self.add(curve)
        self.play(ShowCreation(Axes()))
        self.play(
            ApplyMethod(self.camera.frame.set_height,5),
            ApplyMethod(self.camera.frame.set_width,10),
        )
        self.wait(2)
        