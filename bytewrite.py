import numpy as np

file_close=open('close_signal_medium.ft','wb')

file_open=open('open_signal_medium.ft','wb')

freq_active=np.float64(1)
freq_inactive=np.float64(0)

one_high_time=np.uint32(216000)
one_low_time=np.uint32(644000)

zero_high_time=np.uint32(640000)
zero_low_time=np.uint32(208000)

padding=np.uint32(0)

gap=np.uint32(6184000)

reps=50

bitting_open=[0,0,1,0,0,0,1,1,1,1,1,0,1,1,0,0,1,1,1,1,1,1,0,0,1]

bitting_close=[0,0,1,0,0,0,1,1,1,1,1,0,1,1,0,0,1,1,1,1,0,0,1,1,1]

for N in range(1,reps):

    for i in bitting_open:
    
        if i==0:
    
            file_open.write(freq_active)
            file_open.write(zero_high_time)
            file_open.write(padding)
            file_open.write(freq_inactive)
            file_open.write(zero_low_time)
            file_open.write(padding)
    
    
        else:
            file_open.write(freq_active)
            file_open.write(one_high_time)
            file_open.write(padding)
            file_open.write(freq_inactive)
            file_open.write(one_low_time)
            file_open.write(padding)
    
    file_open.write(freq_inactive)
    file_open.write(gap)
    file_open.write(padding)
            
    for j in bitting_close:
    
        if j==0:
    
            file_close.write(freq_active)
            file_close.write(zero_high_time)
            file_close.write(padding)
            file_close.write(freq_inactive)
            file_close.write(zero_low_time)
            file_close.write(padding)
    
    
        else:
            file_close.write(freq_active)
            file_close.write(one_high_time)
            file_close.write(padding)
            file_close.write(freq_inactive)
            file_close.write(one_low_time)
            file_close.write(padding)
    
    file_close.write(freq_inactive)
    file_close.write(gap)
    file_close.write(padding)
    
file_close.close()

file_open.close()
                        

# file.write(f1)
# file.write(d1)
# file.write(pad)
# file.write(f2)
# file.write(d2)
# file.write(pad)
# 
# file.close()

#zeropulse 640+208=848
#onepulse 216+644=860
#average on close = 856 total, 642 for 1, 212 for 0
#6184 microsecond gap, 22 repetitions

#zeropulse 640+208=848
#onepulse 220+644=864
#average on open = 856, 642 for 1, 212 for 0

