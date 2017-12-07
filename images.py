import pygame
import numpy
pygame.init()


# color scheme

purple = (144,156,194)
yellow = (247,181,56)
blue = (8,72,135)
white = (247,245,251)
red = (195,47,39)
grey = (64,64,64)

# hill colors

one = (195,47,39)
two = (195, 31, 151)
roll = (31, 70, 195)
three = (31, 173, 195)
four = (31, 195, 157)
five = (31, 195, 31)


startBackground = pygame.image.load('background.jpg')
# from http://seamless-pixels.blogspot.com/2014/06/seamless-asphalt-tarmac-road-tar-texture.html
asphalt = pygame.image.load('asphalt.jpg')
# from https://assets.bwbx.io/images/users/iqjWHBFdfxIU/ioHMCiOXPLvU/v1/1000x-1.jpg
hill1 = pygame.image.load('hill1.png')
# from http://cmubuggy.org/gallery/2014-2015/Raceday-2015-Saturday/RacedayFinals-2015_bmatzke-037
hill2 = pygame.image.load('hill2.png')
#from http://cmubuggy.org/gallery/2015-2016/Raceday---Finals/IMG_6053
hill3 = pygame.image.load('hill3.png')
# from http://cmubuggy.org/gallery/2016-2017/Raceday---Prelims/IMG_9887
hill4 = pygame.image.load('hill4.png')
# from http://cmubuggy.org/gallery/2015-2016/Raceday---Finals-Finish-Line/MENS-HEAT-3
hill5 = pygame.image.load('hill5.png')
# from \https://static.wixstatic.com/media/3b802c_ebc28522dd624741b8f0aa4664ae986d.png/v1/fill/w_334,h_267,al_c,usm_0.66_1.00_0.01/3b802c_ebc28522dd624741b8f0aa4664ae986d.png
haybale = pygame.image.load('haybale.png')
#from http://www.andrew.cmu.edu/user/buggy/Sweepstakes/img/Course_Map_Horizontal.jpg
courseMap = pygame.image.load('map.jpg')

trainingInstructions = pygame.image.load('trainingInstructions.png')

startInstructions = pygame.image.load('startInstructions.png')

freerollInstructions = pygame.image.load('freerollInstructions.png')

#buggy
#made at https://www.piskelapp.com/p/agxzfnBpc2tlbC1hcHByEwsSBlBpc2tlbBiAgMDhnPqsCAw/edit
buggy = pygame.image.load('sidewaysBuggy.png')
sidewaysBuggyDesign = pygame.image.load('sidewaysBuggyDesign.png')
genericBuggy = pygame.image.load('buggyIMG.png')
buggyDesign = pygame.image.load('buggyDesign.png')



#from https://gamedev.stackexchange.com/questions/26550/how-can-a-pygame-image-be-colored
def color_surface(surface, red, green, blue):
    arr = pygame.surfarray.pixels3d(surface)
    arr[:,:,0] = red
    arr[:,:,1] = green
    arr[:,:,2] = blue


hills = ({
	"hill1": [(101, 91), (104, 91), (107, 91), (110, 91), (114, 91), (120,91), 
	(126, 91), (134,92), (143, 93), (153, 93), (163, 94),(176, 96), (190, 98),
	(196, 100), (212, 104), (230, 105), (242, 107), (251, 109), (264, 112)], 
 	"hill2": [(264, 112), (274,115), (285, 118), (293, 120), (299, 122), 
 	(307, 127), (315, 131), (323, 139), (332, 147)],
 	"freeroll": [(332, 147), (336, 152), (341, 158), (345, 164), (347, 171), 
 	(348, 177), (350, 183), (350, 188), (351, 194), (348, 200), (346, 206), 
 	(340, 212), (335, 219), (328, 225), (321, 231), (316, 237), (312, 243), 
 	(309, 248), (306, 254), (305, 254), (304, 255), (304, 256), (304, 258),
 	(303, 265), (302, 273), (300, 282), (299, 292), (299, 299), (299, 307), 
 	(301, 312), (303, 317), (307, 323), (312, 329), (317, 333), (323, 338), 
 	(327, 342), (332, 347), (335, 351), (338, 356), (341, 360), (344, 365), 
 	(346, 370), (348, 375), (348, 379), (348, 384), (347, 389), (346, 394),
 	(344, 397), (342, 401), (340, 405), (339, 409), (339, 414), (338, 419), 
 	(338, 424), (338, 429), (339, 434), (340, 440), (341, 446), (342, 453),
 	(342, 458), (342, 462), (341, 466), (339, 471), (335, 475), (332, 480), 
 	(328, 486), (324, 492), (323, 493), (322, 494), (319, 495), (316, 497),
 	(302, 506), (289, 516), (272, 525), (255, 535), (241, 540), (227, 546), 
 	(218, 549), (209, 552), (201, 556), (193, 560), (185, 564), (177, 568), 
 	(166, 569),
 	(156, 570)],
 	"hill3":[(156, 570), (140, 566), (125, 563), (113, 558), (102, 553), (95, 553),
 	(88, 544), (81, 540), (75, 536), (69, 530), (63, 524), (60, 519), (57, 515), 
 	(53, 509), (50, 504), (46, 492), (42, 481), (40, 469), (38, 457)],
 	"hill4":[(38, 457), (38, 445), (38, 433), (38, 415), (39, 397), (40, 390),
 	(42, 383), (43, 375), (44, 367), (45, 357), (47, 348), (49, 338), (51, 328), 
 	(53, 317), (56, 306), (59, 294), (62, 288), (65, 277), (68, 267)],
 	"hill5": [(68, 267), (70, 258), (73, 249), (75, 240), (78, 232), (80, 223), 
 	(82, 215), (85, 207), (88, 199), (90, 192), (93, 185), (96, 177), (99, 170), 
 	(101, 162), (103, 155), (105, 146), (107, 137), (107, 132), (108, 127)]})


teamChoice = ["Apex", "CIA", "Fringe", "PIKA", "SAE", "SDC", "SigEp", "SigNu", "Spirit"]
		



