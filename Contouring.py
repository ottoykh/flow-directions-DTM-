## Contouring create by Otto 

## Search for a starting point on the DTM 

## lowest point in the DTM
Z_min = 7
## highest point in the DTM
Z_max = 99
## contour interval
cin   = 10

## take the interger only "int()"
int_min= (int(Z_min/(cin+1)))
int_max= (int(Z_max/(cin)))

h_min = int_min *cin
h_max = int_max *cin
print(" The height of the lowest contour line  = % f" 
       %h_min)
print(" The height of the highest contour line = % f" 
       %h_max)

## interpolate the contour point 
CL   =30
P1_X =32
P1_Y =60
P1_Z =27
P2_X =36
P2_Y =60
P2_Z =36

Pth = (P1_Z-CL)*(P2_Z-CL)
if Pth >= 0:
    print("\n This contour line should NOT pass through the grid edge\n ")
else:
    print("\n This contour line should pass through the grid edge\n ")

X_h = P1_X +(((CL-P1_Z)/(P2_Z-P1_Z))*(P2_X-P1_X))
Y_h = P1_Y +(((CL-P1_Z)/(P2_Z-P1_Z))*(P2_Y-P1_Y))

print(" X coordinate of the intersected contour point = % f" 
       %X_h)
print(" Y coordinate of the intersected contour point = % f" 
       %Y_h)
