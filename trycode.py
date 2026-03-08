from Pol_to_Rec import*
from Rec_to_Pol import*


print(convert_ptr("9∠-30"))
print(getrinput_ptr("9∠-30"))
print(getangleinput_ptr("9∠-30"))
#####################################
# get output
print("Polar to rectangular output ")
print("real part output: " + str(getxresult_ptr("9∠-30")))
print("imaginary part output: " + str(getyresult_ptr("9∠-30")))

print("###############################################")

print(convert_rtp("-9+j9"))
print(getxinput_rtp("-9+j9"))
print(getyinput_rtp("-9+j9"))

print("Rectangular to Polar output ")
print(getangle_rtp("-9+j9"))
print(getrad_rtp("-9+j9"))

x = float((getangle_rtp("-9+j9")))*float((getyresult_ptr("9∠-30")))

print(x)




























