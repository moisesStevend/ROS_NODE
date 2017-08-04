#!/usr/bin/env python
import cv2

class ConfigCamera(object):
    def __init__(self):
        #Contadores de entrada y salida
        self.cnt_up   = 0
        self.cnt_down = 0
    def initCamera(self,cam):
        #captura de video
        self.cap = cv2.VideoCapture(cam)
    def propCamera(self, w,h):
        #Propiedades del video
        self.cap.set(3,w) #Width
        self.cap.set(4,h) #Height
    def printProp(self):
        #Imprime las propiedades de captura a consola
        for i in range(19):
            print i, cap.get(i)
    def areaCamera(self):
        self.w = self.cap.get(4)
        self.h = self.cap.get(5)
        frameArea = self.h*self.w
        areaTH = frameArea/250
        print 'Area Threshold', areaTH
        return areaTH
    def lineasCamera(self):
        #Lineas de entrada/salida
        self.line_up = int(2*(self.h/5))
        self.line_down   = int(3*(self.h/5))

        self.up_limit =   int(1*(self.h/5))
        self.down_limit = int(4*(self.h/5))

        print "Red line y:",str(self.line_down)
        print "Blue line y:", str(self.line_up)
        self.line_down_color = (255,0,0)
        self.line_up_color = (0,0,255)
        self.pt1 =  [0, self.line_down];
        self.pt2 =  [self.w, self.line_down];
        self.pts_L1 = np.array([self.pt1,self.pt2], np.int32)
        self.pts_L1 = self.pts_L1.reshape((-1,1,2))
        self.pt3 =  [0, self.line_up];
        self.pt4 =  [w, self.line_up];
        self.pts_L2 = np.array([self.pt3,self.pt4], np.int32)
        self.pts_L2 = self.pts_L2.reshape((-1,1,2))

        self.pt5 =  [0, self.up_limit];
        self.pt6 =  [self.w, self.up_limit];
        self.pts_L3 = np.array([self.pt5,self.pt6], np.int32)
        self.pts_L3 = self.pts_L3.reshape((-1,1,2))
        self.pt7 =  [0, self.down_limit];
        self.pt8 =  [self.w, self.down_limit];
        self.pts_L4 = np.array([self.pt7, self.pt8], np.int32)
        self.pts_L4 = self.pts_L4.reshape((-1,1,2))
