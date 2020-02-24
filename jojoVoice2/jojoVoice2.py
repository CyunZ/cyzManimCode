from manimlib.imports import *
import mytool.FFT_Song as FFT_Song



class Part1(MovingCameraScene):
    def construct(self):

        frame_width = 50
        
        params = FFT_Song.getSongFormula("jojoVoice2.wav",200)
        print(params)
        self.camera.set_frame_center((frame_width/2,0,0))
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
        