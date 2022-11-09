
## Flow directions by Otto Yu 

import array as arr

r1 = arr.array('l', [78,72,68,73,60,48])
r2 = arr.array('l', [75,68,56,50,46,50])
r3 = arr.array('l', [70,55,45,40,39,47])
r4 = arr.array('l', [65,57,53,26,30,27])
r5 = arr.array('l', [67,60,48,23,18,20])
r6 = arr.array('l', [75,55,45,12,10,12])

print("\nDTM dataset :")
print( r1[0] ,r1[1] ,r1[2] ,r1[3] ,r1[4] ,r1[5])
print( r2[0] ,r2[1] ,r2[2] ,r2[3] ,r2[4] ,r2[5])
print( r3[0] ,r3[1] ,r3[2] ,r3[3] ,r3[4] ,r3[5])
print( r4[0] ,r4[1] ,r4[2] ,r4[3] ,r4[4] ,r4[5])
print( r5[0] ,r5[1] ,r5[2] ,r5[3] ,r5[4] ,r5[5])
print( r6[0] ,r6[1] ,r6[2] ,r6[3] ,r6[4] ,r6[5])
print ("\nFlow directions :")

## row1_1
## bottom
bot_row1_1= r1[0]-r2[0]
## bottom right 
bri_row1_1= r1[0]-r2[1]
## right 
rig_row1_1= r1[0]-r1[1]

# find the maximum number
flowdl_row1_1 = {rig_row1_1 : "→", bot_row1_1:"↓",bri_row1_1 :"↘"}
flowd_row1_1  = flowdl_row1_1.get(max(flowdl_row1_1)) 

flowec_row1_1 = {rig_row1_1 : "1", bot_row1_1:"2",bri_row1_1 :"4"}
flowen_row1_1  = flowec_row1_1.get(max(flowec_row1_1)) 

## row1_2
## bottom
bot_row1_2= r1[1]-r2[1]
## bottom left 
ble_row1_2= r1[1]-r2[0]
## bottom right 
bri_row1_2= r1[1]-r2[2]
## left 
lef_row1_2= r1[1]-r1[0]
## right 
rig_row1_2= r1[1]-r1[2]

# find the maximum number
flowdl_row1_2 = {rig_row1_2 : "→", bot_row1_2:"↓",ble_row1_2:"↙",bri_row1_2 :"↘", lef_row1_2:"←"}
flowd_row1_2  = flowdl_row1_2.get(max(flowdl_row1_2)) 

flowec_row1_2 = {rig_row1_2 : "1", bot_row1_2:"4",ble_row1_2:"8",bri_row1_2 :"2", lef_row1_2:"16"}
flowen_row1_2  = flowec_row1_2.get(max(flowec_row1_2)) 

## row1_3
## bottom
bot_row1_3= r1[2]-r2[2]
## bottom left 
ble_row1_3= r1[2]-r2[1]
## bottom right 
bri_row1_3= r1[2]-r2[3]
## left 
lef_row1_3= r1[2]-r1[1]
## right 
rig_row1_3= r1[2]-r1[3]

# find the maximum number
flowdl_row1_3 = {rig_row1_3 : "→", bot_row1_3:"↓",ble_row1_3:"↙",bri_row1_3 :"↘", lef_row1_3:"←"}
flowd_row1_3  = flowdl_row1_3.get(max(flowdl_row1_3)) 

flowec_row1_3 = {rig_row1_3 : "1", bot_row1_3:"4",ble_row1_3:"8",bri_row1_3 :"2", lef_row1_3:"16"}
flowen_row1_3  = flowec_row1_3.get(max(flowec_row1_3)) 

## row1_4
## bottom
bot_row1_4= r1[3]-r2[3]
## bottom left 
ble_row1_4= r1[3]-r2[2]
## bottom right 
bri_row1_4= r1[3]-r2[4]
## left 
lef_row1_4= r1[3]-r1[2]
## right 
rig_row1_4= r4[3]-r1[4]

# find the maximum number
flowdl_row1_4 = {rig_row1_4 : "→", bot_row1_4:"↓",ble_row1_4:"↙",bri_row1_4 :"↘", lef_row1_4:"←"}
flowd_row1_4  = flowdl_row1_4.get(max(flowdl_row1_4)) 

flowec_row1_4 = {rig_row1_4 : "1", bot_row1_4:"4",ble_row1_4:"8",bri_row1_4 :"2", lef_row1_4:"16"}
flowen_row1_4  = flowec_row1_4.get(max(flowec_row1_4)) 

## row1_5
## bottom
bot_row1_5= r1[4]-r2[4]
## bottom left 
ble_row1_5= r1[4]-r2[3]
## bottom right 
bri_row1_5= r1[4]-r2[5]
## left 
lef_row1_5= r1[4]-r1[3]
## right 
rig_row1_5= r1[4]-r1[5]

# find the maximum number
flowdl_row1_5 = {rig_row1_5 : "→", bot_row1_5:"↓",ble_row1_5:"↙",bri_row1_5 :"↘", lef_row1_5:"←"}
flowd_row1_5  = flowdl_row1_5.get(max(flowdl_row1_5)) 

flowec_row1_5 = {rig_row1_5 : "1", bot_row1_5:"4",ble_row1_5:"8",bri_row1_5 :"2", lef_row1_5:"16"}
flowen_row1_5  = flowec_row1_5.get(max(flowec_row1_5)) 

## row1_6
## bottom
bot_row1_6= r1[5]-r2[5]
## bottom left 
ble_row1_6= r1[5]-r2[4]
## left 
lef_row1_6= r1[5]-r1[4]

# find the maximum number
flowdl_row1_6 = {bot_row1_6:"↓",ble_row1_6:"↙", lef_row1_6:"←"}
flowd_row1_6  = flowdl_row1_6.get(max(flowdl_row1_6)) 
flowec_row1_6= {bot_row1_6:"4",ble_row1_6:"8", lef_row1_6:"16"}
flowen_row1_6  = flowec_row1_6.get(max(flowec_row1_6)) 

## row2_1
## top 
top_row2_1= r2[0]-r1[0]
## top right 
tri_row2_1= r2[0]-r1[1]
## bottom
bot_row2_1= r2[0]-r3[0]
## bottom right 
bri_row2_1= r2[0]-r3[1]
## right 
rig_row2_1= r2[0]-r2[1]

# find the maximum number
flowdl_row2_1 = {top_row2_1:"↑",tri_row2_1 :"↗",rig_row2_1 : "→", bot_row2_1:"↓",bri_row2_1 :"↘"}
flowd_row2_1  = flowdl_row2_1.get(max(flowdl_row2_1)) 

flowec_row2_1= {top_row2_1:"64",tri_row2_1 :"128",rig_row2_1 : "1", bot_row2_1:"4",bri_row2_1 :"2"}
flowen_row2_1  = flowec_row2_1.get(max(flowec_row2_1)) 


## row2_2
## top 
top_row2_2= r2[1]-r1[1]
## top left 
tle_row2_2= r2[1]-r1[0]
## top right 
tri_row2_2= r2[1]-r1[2]
## bottom
bot_row2_2= r2[1]-r3[1]
## bottom left 
ble_row2_2= r2[1]-r3[0]
## bottom right 
bri_row2_2= r2[1]-r3[2]
## left 
lef_row2_2= r2[1]-r2[0]
## right 
rig_row2_2= r2[1]-r2[2]

# find the maximum number
flowdl_row2_2 = {top_row2_2:"↑",tle_row2_2:"↖",tri_row2_2 :"↗",rig_row2_2 : "→", bot_row2_2:"↓",ble_row2_2:"↙",bri_row2_2 :"↘", lef_row2_2:"←"}
flowd_row2_2  = flowdl_row2_2.get(max(flowdl_row2_2)) 

flowec_row2_2 = {top_row2_2:"64",tle_row2_2:"32",tri_row2_2 :"128",rig_row2_2 : "1", bot_row2_2:"4",ble_row2_2:"8",bri_row2_2 :"2", lef_row2_2:"16"}
flowen_row2_2  = flowec_row2_2.get(max(flowec_row2_2)) 


## row2_3
## top 
top_row2_3= r2[2]-r1[2]
## top left 
tle_row2_3= r2[2]-r1[1]
## top right 
tri_row2_3= r2[2]-r1[3]
## bottom
bot_row2_3= r2[2]-r3[2]
## bottom left 
ble_row2_3= r2[2]-r3[1]
## bottom right 
bri_row2_3= r2[2]-r3[3]
## left 
lef_row2_3= r2[2]-r2[1]
## right 
rig_row2_3= r2[2]-r2[3]

# find the maximum number
flowdl_row2_3 = {top_row2_3:"↑",tle_row2_3:"↖",tri_row2_3 :"↗",rig_row2_3 : "→", bot_row2_3:"↓",ble_row2_3:"↙",bri_row2_3 :"↘", lef_row2_3:"←"}
flowd_row2_3  = flowdl_row2_3.get(max(flowdl_row2_3)) 

flowec_row2_3 = {top_row2_3:"64",tle_row2_3:"32",tri_row2_3 :"128",rig_row2_3 : "1", bot_row2_3:"4",ble_row2_3:"8",bri_row2_3 :"2", lef_row2_3:"16"}
flowen_row2_3  = flowec_row2_3.get(max(flowec_row2_3)) 

## row2_4
## top 
top_row2_4= r2[3]-r1[3]
## top left 
tle_row2_4= r2[3]-r1[2]
## top right 
tri_row2_4= r2[3]-r1[4]
## bottom
bot_row2_4= r2[3]-r3[3]
## bottom left 
ble_row2_4= r2[3]-r3[2]
## bottom right 
bri_row2_4= r2[3]-r3[4]
## left 
lef_row2_4= r2[3]-r2[2]
## right 
rig_row2_4= r2[3]-r2[4]

# find the maximum number
flowdl_row2_4 = {top_row2_4:"↑",tle_row2_4:"↖",tri_row2_4 :"↗",rig_row2_4 : "→", bot_row2_4:"↓",ble_row2_4:"↙",bri_row2_4 :"↘", lef_row2_4:"←"}
flowd_row2_4  = flowdl_row2_4.get(max(flowdl_row2_4)) 

flowec_row2_4 = {top_row2_4:"64",tle_row2_4:"32",tri_row2_4 :"128",rig_row2_4 : "1", bot_row2_4:"4",ble_row2_4:"8",bri_row2_4 :"2", lef_row2_4:"16"}
flowen_row2_4  = flowec_row2_4.get(max(flowec_row2_4)) 

## row2_5
## top 
top_row2_5= r2[4]-r1[4]
## top left 
tle_row2_5= r2[4]-r1[3]
## top right 
tri_row2_5= r2[4]-r1[5]
## bottom
bot_row2_5= r2[4]-r3[4]
## bottom left 
ble_row2_5= r2[4]-r3[3]
## bottom right 
bri_row2_5= r2[4]-r3[5]
## left 
lef_row2_5= r2[4]-r2[3]
## right 
rig_row2_5= r2[4]-r2[5]

# find the maximum number
flowdl_row2_5 = {top_row2_5:"↑",tle_row2_5:"↖",tri_row2_5 :"↗",rig_row2_5 : "→", bot_row2_5:"↓",ble_row2_5:"↙",bri_row2_5 :"↘", lef_row2_5:"←"}
flowd_row2_5  = flowdl_row2_5.get(max(flowdl_row2_5)) 

flowec_row2_5 = {top_row2_5:"64",tle_row2_5:"32",tri_row2_5 :"128",rig_row2_5 : "1", bot_row2_5:"4",ble_row2_5:"8",bri_row2_5 :"2", lef_row2_5:"16"}
flowen_row2_5  = flowec_row2_5.get(max(flowec_row2_5)) 

## row2_6
## top 
top_row2_6= r2[5]-r1[5]
## top left 
tle_row2_6= r2[5]-r1[4]
## bottom
bot_row2_6= r2[5]-r3[5]
## bottom left 
ble_row2_6= r2[5]-r3[4]
## left 
lef_row2_6= r2[5]-r2[4]

# find the maximum number
flowdl_row2_6 = {top_row2_6:"↑",tle_row2_6:"↖", bot_row2_6:"↓",ble_row2_6:"↙", lef_row2_6:"←"}
flowd_row2_6  = flowdl_row2_6.get(max(flowdl_row2_6)) 

flowec_row2_6 = {top_row2_6:"64",tle_row2_6:"32", bot_row2_6:"4",ble_row2_6:"8", lef_row2_6:"16"}
flowen_row2_6  = flowec_row2_6.get(max(flowec_row2_6)) 

## row3_1
## top 
top_row3_1= r3[0]-r2[0]
## top right 
tri_row3_1= r3[0]-r2[1]
## bottom
bot_row3_1= r3[0]-r4[0]
## bottom right 
bri_row3_1= r3[0]-r4[1]
## right 
rig_row3_1= r3[0]-r3[1]

# find the maximum number
flowdl_row3_1 = {top_row3_1:"↑",tri_row3_1 :"↗",rig_row3_1 : "→", bot_row3_1:"↓",bri_row3_1 :"↘"}
flowd_row3_1  = flowdl_row3_1.get(max(flowdl_row3_1)) 

flowec_row3_1 = {top_row3_1:"64",tri_row3_1 :"128",rig_row3_1 : "1", bot_row3_1:"4",bri_row3_1 :"2"}
flowen_row3_1  = flowec_row3_1.get(max(flowec_row3_1)) 

## row3_2
## top 
top_row3_2= r3[1]-r2[1]
## top left 
tle_row3_2= r3[1]-r2[0]
## top right 
tri_row3_2= r3[1]-r2[2]
## bottom
bot_row3_2= r3[1]-r4[1]
## bottom left 
ble_row3_2= r3[1]-r4[0]
## bottom right 
bri_row3_2= r3[1]-r4[2]
## left 
lef_row3_2= r3[1]-r3[0]
## right 
rig_row3_2= r3[1]-r3[2]

# find the maximum number
flowdl_row3_2 = {top_row3_2:"↑",tle_row3_2:"↖",tri_row3_2 :"↗",rig_row3_2 : "→", bot_row3_2:"↓",ble_row3_2:"↙",bri_row3_2 :"↘", lef_row3_2:"←"}
flowd_row3_2  = flowdl_row3_2.get(max(flowdl_row3_2)) 

flowec_row3_2 = {top_row3_2:"64",tle_row3_2:"32",tri_row3_2 :"128",rig_row3_2 : "1", bot_row3_2:"4",ble_row3_2:"8",bri_row3_2 :"2", lef_row3_2:"16"}
flowen_row3_2  = flowec_row3_2.get(max(flowec_row3_2)) 

## row3_3
## top 
top_row3_3= r3[2]-r1[2]
## top left 
tle_row3_3= r3[2]-r2[1]
## top right 
tri_row3_3= r3[2]-r2[3]
## bottom
bot_row3_3= r3[2]-r4[2]
## bottom left 
ble_row3_3= r3[2]-r4[1]
## bottom right 
bri_row3_3= r3[2]-r4[3]
## left 
lef_row3_3= r3[2]-r3[1]
## right 
rig_row3_3= r3[2]-r3[3]

# find the maximum number
flowdl_row3_3 = {top_row3_3:"↑",tle_row3_3:"↖",tri_row3_3 :"↗",rig_row3_3 : "→", bot_row3_3:"↓",ble_row3_3:"↙",bri_row3_3 :"↘", lef_row3_3:"←"}
flowd_row3_3  = flowdl_row3_3.get(max(flowdl_row3_3)) 

flowec_row3_3 = {top_row3_3:"64",tle_row3_3:"32",tri_row3_3 :"128",rig_row3_3 : "1", bot_row3_3:"4",ble_row3_3:"8",bri_row3_3 :"2", lef_row3_3:"16"}
flowen_row3_3  = flowec_row3_3.get(max(flowec_row3_3)) 

## row3_4
## top 
top_row3_4= r3[3]-r2[3]
## top left 
tle_row3_4= r3[3]-r2[2]
## top right 
tri_row3_4= r3[3]-r2[4]
## bottom
bot_row3_4= r3[3]-r4[3]
## bottom left 
ble_row3_4= r3[3]-r4[2]
## bottom right 
bri_row3_4= r3[3]-r4[4]
## left 
lef_row3_4= r3[3]-r3[2]
## right 
rig_row3_4= r3[3]-r3[4]

# find the maximum number
flowdl_row3_4 = {top_row3_4:"↑",tle_row3_4:"↖",tri_row3_4 :"↗",rig_row3_4 : "→", bot_row3_4:"↓",ble_row3_4:"↙",bri_row3_4 :"↘", lef_row3_4:"←"}
flowd_row3_4  = flowdl_row3_4.get(max(flowdl_row3_4)) 

flowec_row3_4 = {top_row3_4:"64",tle_row3_4:"32",tri_row3_4 :"128",rig_row3_4 : "1", bot_row3_4:"4",ble_row3_4:"8",bri_row3_4 :"2", lef_row3_4:"16"}
flowen_row3_4  = flowec_row3_4.get(max(flowec_row3_4)) 

## row3_5
## top 
top_row3_5= r3[4]-r2[4]
## top left 
tle_row3_5= r3[4]-r2[3]
## top right 
tri_row3_5= r3[4]-r2[5]
## bottom
bot_row3_5= r3[4]-r4[4]
## bottom left 
ble_row3_5= r3[4]-r4[3]
## bottom right 
bri_row3_5= r3[4]-r4[5]
## left 
lef_row3_5= r3[4]-r3[3]
## right 
rig_row3_5= r3[4]-r3[5]

# find the maximum number
flowdl_row3_5 = {top_row3_5:"↑",tle_row3_5:"↖",tri_row3_5 :"↗",rig_row3_5 : "→", bot_row3_5:"↓",ble_row3_5:"↙",bri_row3_5 :"↘", lef_row3_5:"←"}
flowd_row3_5  = flowdl_row3_5.get(max(flowdl_row3_5)) 

flowec_row3_5 = {top_row3_5:"64",tle_row3_5:"32",tri_row3_5 :"128",rig_row3_5 : "1", bot_row3_5:"4",ble_row3_5:"8",bri_row3_5 :"2", lef_row3_5:"16"}
flowen_row3_5  = flowec_row3_5.get(max(flowec_row3_5)) 

## row3_6
## top 
top_row3_6= r3[5]-r2[5]
## top left 
tle_row3_6= r3[5]-r2[4]
## bottom
bot_row3_6= r3[5]-r4[5]
## bottom left 
ble_row3_6= r3[5]-r4[4]
## left 
lef_row3_6= r3[5]-r3[4]

# find the maximum number
flowdl_row3_6 = {top_row3_6:"↑",tle_row3_6:"↖", bot_row3_6:"↓",ble_row3_6:"↙", lef_row3_6:"←"}
flowd_row3_6  = flowdl_row3_6.get(max(flowdl_row3_6)) 

flowec_row3_6 = {top_row3_6:"64",tle_row3_6:"32", bot_row3_6:"4",ble_row3_6:"8", lef_row3_6:"16"}
flowen_row3_6  = flowec_row3_6.get(max(flowec_row3_6))

## row4_1
## top 
top_row4_1= r4[0]-r3[0]
## top right 
tri_row4_1= r4[0]-r3[1]
## bottom
bot_row4_1= r4[0]-r5[0]
## bottom right 
bri_row4_1= r4[0]-r5[1]
## right 
rig_row4_1= r4[0]-r4[1]

# find the maximum number
flowdl_row4_1 = {top_row4_1:"↑",tri_row4_1 :"↗",rig_row4_1 : "→", bot_row4_1:"↓",bri_row4_1 :"↘"}
flowd_row4_1  = flowdl_row4_1.get(max(flowdl_row4_1)) 

flowec_row4_1= {top_row4_1:"64",tri_row4_1 :"128",rig_row4_1 : "1", bot_row4_1:"4",bri_row4_1 :"2"}
flowen_row4_1  = flowec_row4_1.get(max(flowec_row4_1))  

## row4_2
## top 
top_row4_2= r4[1]-r3[1]
## top left 
tle_row4_2= r4[1]-r3[0]
## top right 
tri_row4_2= r4[1]-r3[2]
## bottom
bot_row4_2= r4[1]-r5[1]
## bottom left 
ble_row4_2= r4[1]-r5[0]
## bottom right 
bri_row4_2= r4[1]-r5[2]
## left 
lef_row4_2= r4[1]-r4[0]
## right 
rig_row4_2= r4[1]-r4[2]

# find the maximum number
flowdl_row4_2 = {top_row4_2:"↑",tle_row4_2:"↖",tri_row4_2 :"↗",rig_row4_2 : "→", bot_row4_2:"↓",ble_row4_2:"↙",bri_row4_2 :"↘", lef_row4_2:"←"}
flowd_row4_2  = flowdl_row4_2.get(max(flowdl_row4_2)) 

flowec_row4_2 = {top_row4_2:"64",tle_row4_2:"32",tri_row4_2 :"128",rig_row4_2 : "1", bot_row4_2:"4",ble_row4_2:"8",bri_row4_2 :"2", lef_row4_2:"16"}
flowen_row4_2  = flowec_row4_2.get(max(flowec_row4_2)) 

## row4_3
## top 
top_row4_3= r4[2]-r3[2]
## top left 
tle_row4_3= r4[2]-r3[1]
## top right 
tri_row4_3= r4[2]-r3[3]
## bottom
bot_row4_3= r4[2]-r5[2]
## bottom left 
ble_row4_3= r4[2]-r5[1]
## bottom right 
bri_row4_3= r4[2]-r5[3]
## left 
lef_row4_3= r4[2]-r4[1]
## right 
rig_row4_3= r4[2]-r4[3]

# find the maximum number
flowdl_row4_3 = {top_row4_3:"↑",tle_row4_3:"↖",tri_row4_3 :"↗",rig_row4_3 : "→", bot_row4_3:"↓",ble_row4_3:"↙",bri_row4_3 :"↘", lef_row4_3:"←"}
flowd_row4_3  = flowdl_row4_3.get(max(flowdl_row4_3)) 

flowec_row4_3 = {top_row4_3:"64",tle_row4_3:"32",tri_row4_3 :"128",rig_row4_3 : "1", bot_row4_3:"4",ble_row4_3:"8",bri_row4_3 :"2", lef_row4_3:"16"}
flowen_row4_3  = flowec_row4_3.get(max(flowec_row4_3)) 

## row4_4
## top 
top_row4_4= r4[3]-r3[3]
## top left 
tle_row4_4= r4[3]-r3[2]
## top right 
tri_row4_4= r4[3]-r3[4]
## bottom
bot_row4_4= r4[3]-r5[3]
## bottom left 
ble_row4_4= r4[3]-r5[2]
## bottom right 
bri_row4_4= r4[3]-r5[4]
## left 
lef_row4_4= r4[3]-r4[2]
## right 
rig_row4_4= r4[3]-r4[4]

# find the maximum number
flowdl_row4_4 = {top_row4_4:"↑",tle_row4_4:"↖",tri_row4_4 :"↗",rig_row4_4 : "→", bot_row4_4:"↓",ble_row4_4:"↙",bri_row4_4 :"↘", lef_row4_4:"←"}
flowd_row4_4  = flowdl_row4_4.get(max(flowdl_row4_4)) 

flowec_row4_4 = {top_row4_4:"64",tle_row4_4:"32",tri_row4_4 :"128",rig_row4_4 : "1", bot_row4_4:"4",ble_row4_4:"8",bri_row4_4 :"2", lef_row4_4:"16"}
flowen_row4_4  = flowec_row4_4.get(max(flowec_row4_4)) 

## row4_5
## top 
top_row4_5= r4[4]-r3[4]
## top left 
tle_row4_5= r4[4]-r3[3]
## top right 
tri_row4_5= r4[4]-r3[5]
## bottom
bot_row4_5= r4[4]-r5[4]
## bottom left 
ble_row4_5= r4[4]-r5[3]
## bottom right 
bri_row4_5= r4[4]-r5[5]
## left 
lef_row4_5= r4[4]-r4[3]
## right 
rig_row4_5= r4[4]-r4[5]

# find the maximum number
flowdl_row4_5 = {top_row4_5:"↑",tle_row4_5:"↖",tri_row4_5 :"↗",rig_row4_5 : "→", bot_row4_5:"↓",ble_row4_5:"↙",bri_row4_5 :"↘", lef_row4_5:"←"}
flowd_row4_5  = flowdl_row4_5.get(max(flowdl_row4_5)) 

flowec_row4_5 = {top_row4_5:"64",tle_row4_5:"32",tri_row4_5 :"128",rig_row4_5 : "1", bot_row4_5:"4",ble_row4_5:"8",bri_row4_5 :"2", lef_row4_5:"16"}
flowen_row4_5  = flowec_row4_5.get(max(flowec_row4_5)) 

## row4_6
## top 
top_row4_6= r4[5]-r3[5]
## top left 
tle_row4_6= r4[5]-r3[4]
## bottom
bot_row4_6= r4[5]-r5[5]
## bottom left 
ble_row4_6= r4[5]-r5[4]
## left 
lef_row4_6= r4[5]-r5[4]

# find the maximum number
flowdl_row4_6 = {top_row4_6:"↑",tle_row4_6:"↖", bot_row4_6:"↓",ble_row4_6:"↙", lef_row4_6:"←"}
flowd_row4_6  = flowdl_row4_6.get(max(flowdl_row4_6)) 

flowec_row4_6 = {top_row4_6:"64",tle_row4_6:"32", bot_row4_6:"4",ble_row4_6:"8", lef_row4_6:"16"}
flowen_row4_6  = flowec_row4_6.get(max(flowec_row4_6))

## row5_1
## top 
top_row5_1= r5[0]-r4[0]
## top right 
tri_row5_1= r5[0]-r4[1]
## bottom
bot_row5_1= r5[0]-r6[0]
## bottom right 
bri_row5_1= r5[0]-r6[1]
## right 
rig_row5_1= r5[0]-r5[1]

# find the maximum number
flowdl_row5_1 = {top_row5_1:"↑",tri_row5_1 :"↗",rig_row5_1 : "→", bot_row5_1:"↓",bri_row5_1 :"↘"}
flowd_row5_1  = flowdl_row5_1.get(max(flowdl_row5_1)) 

flowec_row5_1= {top_row5_1:"64",tri_row5_1 :"128",rig_row5_1 : "1", bot_row5_1:"4",bri_row5_1 :"2"}
flowen_row5_1  = flowec_row5_1.get(max(flowec_row5_1))  

## row5_2
## top 
top_row5_2= r5[1]-r4[1]
## top left 
tle_row5_2= r5[1]-r4[0]
## top right 
tri_row5_2= r5[1]-r4[2]
## bottom
bot_row5_2= r5[1]-r6[1]
## bottom left 
ble_row5_2= r5[1]-r6[0]
## bottom right 
bri_row5_2= r5[1]-r6[2]
## left 
lef_row5_2= r5[1]-r5[0]
## right 
rig_row5_2= r5[1]-r5[2]

# find the maximum number
flowdl_row5_2 = {top_row5_2:"↑",tle_row5_2:"↖",tri_row5_2 :"↗",rig_row5_2 : "→", bot_row5_2:"↓",ble_row5_2:"↙",bri_row5_2 :"↘", lef_row5_2:"←"}
flowd_row5_2  = flowdl_row5_2.get(max(flowdl_row5_2)) 

flowec_row5_2 = {top_row5_2:"64",tle_row5_2:"32",tri_row5_2 :"128",rig_row5_2 : "1", bot_row5_2:"4",ble_row5_2:"8",bri_row5_2 :"2", lef_row5_2:"16"}
flowen_row5_2  = flowec_row5_2.get(max(flowec_row5_2)) 


## row5_3
## top 
top_row5_3= r5[2]-r4[2]
## top left 
tle_row5_3= r5[2]-r4[1]
## top right 
tri_row5_3= r5[2]-r4[3]
## bottom
bot_row5_3= r5[2]-r6[2]
## bottom left 
ble_row5_3= r5[2]-r6[1]
## bottom right 
bri_row5_3= r5[2]-r6[3]
## left 
lef_row5_3= r5[2]-r5[1]
## right 
rig_row5_3= r5[2]-r5[3]

# find the maximum number
flowdl_row5_3 = {top_row5_3:"↑",tle_row5_3:"↖",tri_row5_3 :"↗",rig_row5_3 : "→", bot_row5_3:"↓",ble_row5_3:"↙",bri_row5_3 :"↘", lef_row5_3:"←"}
flowd_row5_3  = flowdl_row5_3.get(max(flowdl_row5_3)) 

flowec_row5_3 = {top_row5_3:"64",tle_row5_3:"32",tri_row5_3 :"128",rig_row5_3 : "1", bot_row5_3:"4",ble_row5_3:"8",bri_row5_3 :"2", lef_row5_3:"16"}
flowen_row5_3  = flowec_row5_3.get(max(flowec_row5_3)) 

## row5_4
## top 
top_row5_4= r5[3]-r4[3]
## top left 
tle_row5_4= r5[3]-r4[2]
## top right 
tri_row5_4= r5[3]-r4[4]
## bottom
bot_row5_4= r5[3]-r6[3]
## bottom left 
ble_row5_4= r5[3]-r6[2]
## bottom right 
bri_row5_4= r5[3]-r6[4]
## left 
lef_row5_4= r5[3]-r5[2]
## right 
rig_row5_4= r5[3]-r5[4]

# find the maximum number
flowdl_row5_4 = {top_row5_4:"↑",tle_row5_4:"↖",tri_row5_4 :"↗",rig_row5_4 : "→", bot_row5_4:"↓",ble_row5_4:"↙",bri_row5_4 :"↘", lef_row5_4:"←"}
flowd_row5_4  = flowdl_row5_4.get(max(flowdl_row5_4)) 

flowec_row5_4 = {top_row5_4:"64",tle_row5_4:"32",tri_row5_4 :"128",rig_row5_4 : "1", bot_row5_4:"4",ble_row5_4:"8",bri_row5_4 :"2", lef_row5_4:"16"}
flowen_row5_4  = flowec_row5_4.get(max(flowec_row5_4)) 

## row5_5
## top 
top_row5_5= r5[4]-r4[4]
## top left 
tle_row5_5= r5[4]-r4[3]
## top right 
tri_row5_5= r5[4]-r4[5]
## bottom
bot_row5_5= r5[4]-r6[4]
## bottom left 
ble_row5_5= r5[4]-r6[3]
## bottom right 
bri_row5_5= r5[4]-r6[5]
## left 
lef_row5_5= r5[4]-r5[3]
## right 
rig_row5_5= r5[4]-r5[5]

# find the maximum number
flowdl_row5_5 = {top_row5_5:"↑",tle_row5_5:"↖",tri_row5_5 :"↗",rig_row5_5 : "→", bot_row5_5:"↓",ble_row5_5:"↙",bri_row5_5 :"↘", lef_row5_5:"←"}
flowd_row5_5  = flowdl_row5_5.get(max(flowdl_row5_5)) 

flowec_row5_5 = {top_row5_5:"64",tle_row5_5:"32",tri_row5_5 :"128",rig_row5_5 : "1", bot_row5_5:"4",ble_row5_5:"8",bri_row5_5 :"2", lef_row5_5:"16"}
flowen_row5_5  = flowec_row5_5.get(max(flowec_row5_5)) 

## row5_6
## top 
top_row5_6= r5[5]-r4[5]
## top left 
tle_row5_6= r5[5]-r4[4]
## bottom
bot_row5_6= r5[5]-r6[5]
## bottom left 
ble_row5_6= r5[5]-r6[4]
## left 
lef_row5_6= r5[5]-r5[4]

# find the maximum number
flowdl_row5_6 = {top_row5_6:"↑",tle_row5_6:"↖", bot_row5_6:"↓",ble_row5_6:"↙", lef_row5_6:"←"}
flowd_row5_6  = flowdl_row5_6.get(max(flowdl_row5_6)) 

flowec_row5_6 = {top_row5_6:"64",tle_row5_6:"32", bot_row5_6:"4",ble_row5_6:"8", lef_row5_6:"16"}
flowen_row5_6  = flowec_row5_6.get(max(flowec_row5_6))

## row6_1
## top 
top_row6_1= r6[0]-r5[0]
## top right 
tri_row6_1= r6[0]-r5[1]
## right 
rig_row6_1= r6[0]-r6[1]

# find the maximum number
flowdl_row6_1 = {top_row6_1:"↑",tri_row6_1 :"↗",rig_row6_1 : "→"}
flowd_row6_1  = flowdl_row6_1.get(max(flowdl_row6_1)) 

flowec_row6_1 = {top_row6_1:"64",tri_row6_1 :"128",rig_row6_1 : "1"}
flowen_row6_1  = flowec_row6_1.get(max(flowec_row6_1)) 
  
## row6_2
## top 
top_row6_2= r6[1]-r5[1]
## top left 
tle_row6_2= r6[1]-r5[0]
## top right 
tri_row6_2= r6[1]-r5[2]
## left 
lef_row6_2= r6[1]-r6[0]
## right 
rig_row6_2= r6[1]-r6[2]

# find the maximum number
flowdl_row6_2 = {top_row6_2:"↑",tle_row6_2:"↖",tri_row6_2 :"↗",rig_row6_2 : "→", lef_row6_2:"←"}
flowd_row6_2  = flowdl_row6_2.get(max(flowdl_row6_2)) 

flowec_row6_2 = {top_row6_2:"64",tle_row6_2:"32",tri_row6_2 :"128",rig_row6_2 : "1", lef_row6_2:"16"}
flowen_row6_2  = flowec_row6_2.get(max(flowec_row6_2)) 

## row6_3
## top 
top_row6_3= r6[2]-r5[2]
## top left 
tle_row6_3= r6[2]-r5[1]
## top right 
tri_row6_3= r6[2]-r5[3]
## left 
lef_row6_3= r6[2]-r6[1]
## right 
rig_row6_3= r6[2]-r6[3]

# find the maximum number
flowdl_row6_3 = {top_row6_3:"↑",tle_row6_3:"↖",tri_row6_3 :"↗",rig_row6_3 : "→", lef_row6_3:"←"}
flowd_row6_3  = flowdl_row6_3.get(max(flowdl_row6_3)) 

flowec_row6_3 = {top_row6_3:"64",tle_row6_3:"32",tri_row6_3 :"128",rig_row6_3 : "1", lef_row6_3:"16"}
flowen_row6_3  = flowec_row6_3.get(max(flowec_row6_3)) 

## row6_4
## top 
top_row6_4= r6[3]-r5[3]
## top left 
tle_row6_4= r6[3]-r5[2]
## top right 
tri_row6_4= r6[3]-r5[4]
## left 
lef_row6_4= r6[3]-r6[2]
## right 
rig_row6_4= r6[3]-r6[4]

# find the maximum number
flowdl_row6_4 = {top_row6_4:"↑",tle_row6_4:"↖",tri_row6_4 :"↗",rig_row6_4 : "→",lef_row6_4:"←"}
flowd_row6_4  = flowdl_row6_4.get(max(flowdl_row6_4)) 

flowec_row6_4 = {top_row6_4:"64",tle_row6_4:"32",tri_row6_4 :"128",rig_row6_4 : "1", lef_row6_4:"16"}
flowen_row6_4  = flowec_row6_4.get(max(flowec_row6_4)) 

## row6_5
## top 
top_row6_5= r6[4]-r5[4]
## top left 
tle_row6_5= r6[4]-r5[3]
## top right 
tri_row6_5= r6[4]-r5[5]
## left 
lef_row6_5= r6[4]-r6[3]
## right 
rig_row6_5= r6[4]-r6[5]

# find the maximum number
flowdl_row6_5 = {top_row6_5:"↑",tle_row6_5:"↖",tri_row6_5 :"↗",rig_row6_5 : "→", lef_row6_5:"←"}
flowd_row6_5  = flowdl_row6_5.get(max(flowdl_row6_5)) 

flowec_row6_5 = {top_row6_5:"64",tle_row6_5:"32",tri_row6_5 :"128",rig_row6_5 : "1", lef_row6_5:"16"}
flowen_row6_5  = flowec_row6_5.get(max(flowec_row6_5)) 

## row6_6
## top 
top_row6_6= r6[5]-r5[5]
## top left 
tle_row6_6= r6[5]-r5[4]
## left 
lef_row6_6= r6[5]-r6[4]

# find the maximum number
flowdl_row6_6 = {top_row6_6:"↑",tle_row6_6:"↖", lef_row6_6:"←"}
flowd_row6_6  = flowdl_row6_6.get(max(flowdl_row6_6)) 

flowec_row6_6 = {top_row6_6:"64",tle_row6_6:"32", lef_row6_6:"16"}
flowen_row6_6  = flowec_row6_6.get(max(flowec_row6_6)) 

# result of the flow directions 
print (flowd_row1_1, flowd_row1_2, flowd_row1_3,flowd_row1_4,flowd_row1_5,flowd_row1_6)
print (flowd_row2_1, flowd_row2_2, flowd_row2_3,flowd_row2_4,flowd_row2_5,flowd_row2_6)
print (flowd_row3_1, flowd_row3_2, flowd_row3_3,flowd_row3_4,flowd_row3_5,flowd_row3_6)
print (flowd_row4_1, flowd_row4_2, flowd_row4_3,flowd_row4_4,flowd_row4_5,flowd_row4_6)
print (flowd_row5_1, flowd_row5_2, flowd_row5_3,flowd_row5_4,flowd_row5_5,flowd_row5_6)
print (flowd_row6_1, flowd_row6_2, flowd_row6_3,flowd_row6_4,flowd_row6_5,flowd_row6_6)

print("\nFlow encoding :")
print(flowen_row1_1, flowen_row1_2, flowen_row1_3, flowen_row1_4, flowen_row1_5, flowen_row1_6)
print(flowen_row2_1, flowen_row2_2, flowen_row2_3, flowen_row2_4, flowen_row2_5, flowen_row2_6)
print(flowen_row3_1, flowen_row3_2, flowen_row3_3, flowen_row3_4, flowen_row3_5, flowen_row3_6)
print(flowen_row4_1, flowen_row4_2, flowen_row4_3, flowen_row4_4, flowen_row4_5, flowen_row4_6)
print(flowen_row5_1, flowen_row5_2, flowen_row5_3, flowen_row5_4, flowen_row5_5, flowen_row5_6)
print(flowen_row6_1, flowen_row6_2, flowen_row6_3, flowen_row6_4, flowen_row6_5, flowen_row6_6)
