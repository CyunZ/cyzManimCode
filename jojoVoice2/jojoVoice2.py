from manimlib.imports import *
import mytool.FFT_Song as FFT_Song

# 简单举例波形叠加
class Part0(Scene):
    def construct(self):
        fun1 = lambda x: np.cos(2 * PI *x * 2)
        fg1 = FunctionGraph(fun1,color=MAROON_B)
        equation1 = TexMobject("y_1=cos(2\\pi x\\times 2)")
        equation1.set_y(2 - FRAME_Y_RADIUS - 0.5)
        g1 = VGroup(fg1,equation1)
        
        fun2 = lambda x: np.cos(2 * PI *x * 4 + 45/180*PI)
        fg2 = FunctionGraph(fun2,color=BLUE_E)
        equation2 = TexMobject("y_2=cos(2\\pi x\\times 4+{45\\over 180}\\pi )")
        equation2.set_y(2 - FRAME_Y_RADIUS -0.5)
        g2 = VGroup(fg2,equation2)

        fun3 = lambda x: sum([
                np.cos(2 * PI *x * 2),
                np.cos(2 * PI *x * 4 + 45/180*PI)
            ])
        fg3 = FunctionGraph(fun3,color=GREEN_C)
        equation3 = TexMobject("y_3=cos(2\\pi x\\times 2)+cos(2\\pi x\\times 4+{45\\over 180}\\pi )")
        equation3.set_y(2 - FRAME_Y_RADIUS - 0.5)
        g3 = VGroup(fg3,equation3)

        axes1 = Axes(y_min=-1.5, y_max=1.5)
        copy_axes1 = axes1.copy()
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

        self.play(ApplyMethod( g3.scale,0.4) )
        self.play(
            ApplyMethod( g1.shift,( FRAME_X_RADIUS-3, -1*FRAME_Y_RADIUS ,0) ),
            ApplyMethod( g3.shift,( 3-FRAME_X_RADIUS, FRAME_Y_RADIUS-0.8 ,0) ),
        )
        minus = TexMobject("-")
        minus.set_y(FRAME_Y_RADIUS-0.5)
        self.play(
            ApplyMethod( g1.scale,10/4),
            Transform(add,minus),
            Transform(axes1,copy_axes1)
        )
        self.wait(2)

#延伸到声波
class Part0_5(MovingCameraScene):
    def construct(self):
        fun1 = lambda x: np.cos(2 * PI *x * 220)
        fg1 = FunctionGraph(fun1,color=MAROON_B)
        equation1 = TexMobject("y_1=cos(2\\pi x\\times 220)")
        equation1.set_y(2 - FRAME_Y_RADIUS - 0.5)
        g1 = VGroup(fg1,equation1)

        fun2 = lambda x: np.cos(2 * PI *x * 0.22)
        fg2 = FunctionGraph(fun2,color=MAROON_B)
        
        self.play(ShowCreation(g1))
        self.wait(2)
        self.play(ApplyMethod(self.camera.frame.set_width,5))
        self.wait(2)
        self.play(ApplyMethod(self.camera.frame.set_width,FRAME_WIDTH))
        self.wait(2)

        self.play(Transform(fg1,fg2))
        self.wait(2)
        self.play(ApplyMethod( g1.scale,0.4) )
        self.play( ApplyMethod( g1.shift,( 3-FRAME_X_RADIUS, FRAME_Y_RADIUS ,0) ) )
        self.wait(2)

        fun3 = lambda x: np.cos(2 * PI *x * 1080)
        fg3 = FunctionGraph(fun3,color=BLUE_E)
        equation3 = TexMobject("y_2=cos(2\\pi x\\times 1080)")
        equation3.set_y(2 - FRAME_Y_RADIUS -0.5)
        g3 = VGroup(fg3,equation3)

        fun4 = lambda x: np.cos(2 * PI *x * 1.08)
        fg4 = FunctionGraph(fun4,color=BLUE_E)
        
        self.play(ShowCreation(g3))
        self.wait(2)
        self.play(Transform(fg3,fg4))
        self.wait(2)
        self.play(ApplyMethod( g3.scale,0.4) )
        self.play( ApplyMethod( g3.shift,( FRAME_X_RADIUS - 3, FRAME_Y_RADIUS ,0) ) )
        self.wait(2)

        add = TexMobject("+")
        add.set_y(FRAME_Y_RADIUS-0.5)
        self.play(ShowCreation(add))
        self.wait(1)

        fun5 = lambda x: sum([
                np.cos(2 * PI *x * 2),
                np.cos(2 * PI *x * 4 + 45/180*PI)
            ])
        fg5 = FunctionGraph(fun5,color=GREEN_C)
        equation5 = TexMobject("y_3=cos(2\\pi x\\times 220)+cos(2\\pi x\\times 1080)")
        equation5.set_y(2 - FRAME_Y_RADIUS - 0.5)
        g5 = VGroup(fg5,equation5)
        self.play(ShowCreation(g5))
        self.wait(2)
        
        self.play(ApplyMethod( g5.scale,0.4) )
        self.play(
            ApplyMethod( g1.shift,( FRAME_X_RADIUS-3, -1*FRAME_Y_RADIUS ,0) ),
            ApplyMethod( g5.shift,( 3-FRAME_X_RADIUS, FRAME_Y_RADIUS-0.8 ,0) ),
        )
        minus = TexMobject("-")
        minus.set_y(FRAME_Y_RADIUS-0.5)
        self.play(
            ApplyMethod( g1.scale,10/4),
            Transform(add,minus),
        )
        self.wait(2)


# 实际应用 引出FFT
class Part1(MovingCameraScene):
    def construct(self):
        data,Fs,N = FFT_Song.getSongData("jojoVoice2.wav")

        x_scale = 0.01
        y_max = 1000
        frame_width = len(data) * x_scale
        self.camera.set_frame_center((frame_width/2,0,0))
        self.camera.set_frame_height(y_max * 2)
        self.camera.set_frame_width(frame_width)
        
        curve = VMobject()
        max_amplitude = max(data)
        curve.set_points_smoothly([
            (x_scale*i,data[i] / max_amplitude * y_max,0) 
            for i in range(len(data))
        ])

        curve.set_stroke(GREEN_C, 0.5)
        self.play(ShowCreation(curve))
        # self.add(curve)
        # self.play(ShowCreation(Axes()))
        self.wait(2)

class Part1_2(MovingCameraScene):
    def construct(self):
        params = FFT_Song.getSongFormula("jojoVoice2.wav",1)
        # fun = lambda x: sum([
        #         param[0] * np.sin(2 * PI *param[1]* x + param[2]/180*PI)
        #         for param in params
        #     ])

        texes = []
        str1 = "y="
        for i in range(3):
            param = params[i]
            str1 += "{}cos(2\\pi x\\times {} ".format(param[0] if (param[0] != 1) else '',param[1])
            if param[2] > 0:
                str1 += "+"
            else :
                str1 += "-"
            str1 += "{"+ str( abs(param[2]) ) + "\\over 180}\\pi)"
        tex1 = TexMobject(str1)
        tex1.scale(0.6)
        tex1.set_y(3.5)
        texes.append(tex1)

        for k in range(6):
            str2 = "+"
            for i in range((k+1)*3,(k+2)*3):
                param = params[i]
                str2 += "{}cos(2\\pi x\\times {} ".format(param[0],param[1])
                if param[2] > 0:
                    str2 += "+"
                else :
                    str2 += "-"
                str2 += "{"+ str( abs(param[2]) ) + "\\over 180}\\pi)"
                if i%3 < 2:
                    str2 += "+"
            tex2 = TexMobject(str2)
            tex2.scale(0.6)
            tex2.set_y(2.5-k)
            texes.append(tex2)

        str3 = "+\\cdots \\cdots \\cdots"
        tex3 = TexMobject(str3)
        tex3.scale(0.6)
        tex3.set_y(2.5-6)
        texes.append(tex3)

        g = VGroup(*texes)
        self.play(ShowCreation(g))
        self.wait(2)
