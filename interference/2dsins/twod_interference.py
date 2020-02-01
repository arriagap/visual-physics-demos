import matplotlib.pyplot as plt
import numpy as np



v_sound = 343.0       #m/s
N = 1000
xmin = -40. / 100
xmax = 40. / 100
ymin = -50. / 100
ymax = -10. / 100
x_axis = np.linspace(xmin, xmax, 1000)
y_axis = np.linspace(ymin, ymax, 1000)

x_coordinates, y_coordinates = np.meshgrid(x_axis, y_axis)


# Locations of sources
x_1= -5./ 100
x_2= 5. / 100
y_1=0.
y_2=0.

# Define f
f = 10e3
lam = v_sound / f

#lam = 34400/10**4

# Calculate k
k = 2 * np.pi / lam
#f = 2 * np.pi * v_sound / lam


# Calculate omega
omega = 2. * np.pi * f

t = np.linspace(0,15.e-3, 50)

# Collection of images
aggreg_ims = []
do_plot = True


for i, time in enumerate(t):
    # Find distance from x0 y0
    x1_dist = np.sqrt((x_coordinates - x_1)**2. + (y_coordinates - y_1)**2.)

    # Find distance from x1 y1
    x2_dist = np.sqrt((x_coordinates - x_2)**2. + (y_coordinates - y_2)**2.)

    # Calculate the interference pattern with r^2
    a = np.cos(k * x1_dist - omega * time) / x1_dist#**2.
    b = np.cos(k * x2_dist - omega * time) / x2_dist#**2
    src_sum = (a + b)**2.
    aggreg_ims.append(src_sum)


        
    if True:
        
        fig, (left_src_ax, right_src_ax, sum_ax) = plt.subplots(1, 3, sharey = True, figsize = (14, 4.5))
    

        aspect = 1.5 #np.abs((ymin - ymax) / (xmin - xmax))

        left_src_ax.imshow(b**2, extent = [xmin, xmax, -ymax, -ymin], aspect = aspect, vmin = 0, vmax = 80, cmap = 'hot')
        left_src_ax.set_title('Left Source')
        left_src_ax.set_xlabel('Distance (m)')
        left_src_ax.set_ylabel('Distance (m)')

        right_src_ax.imshow(a**2, extent = [xmin, xmax, -ymax, -ymin], aspect = aspect, vmin = 0, vmax = 80, cmap = 'hot')
        right_src_ax.set_title('Right Source')
        right_src_ax.set_xlabel('Distance (m)')
        

        sum_ax.set_title('Sum of sources')
        sum_ax.imshow(src_sum, extent = [xmin, xmax, -ymax, -ymin], aspect = aspect, vmin = 0, vmax = 100, cmap = 'hot')
        sum_ax.set_xlabel('Distance (m)')
        plt.subplots_adjust(wspace = 0)
    
        fig.suptitle('Time = ' + str(time * 1000)[:5] + 'ms')

        
        if i < 10:
            print('onesrc_00' + str(i) + '.png') 
            fig.savefig('twod_00' + str(i) + '.png') 
        elif i < 100 and i >= 10:
            fig.savefig('twod_0' + str(i) + '.png')
            print('onesrc_0' + str(i) + '.png')
        else:
            fig.savefig('twod_' + str(i) + '.png')
            print('onesrc_' + str(i) + '.png') 

       
        fig.clf()
        plt.close(fig)
        plt.clf()


# images summed along time axis

im_sum = np.sum(np.array(aggreg_ims), axis = 0)
aspect = np.abs((xmin - xmax) / (ymin - ymax))    
plt.imshow(im_sum, extent = [xmin, xmax, -ymax, -ymin], aspect = aspect, cmap = 'hot')
plt.xlabel('Distance (m)')
plt.ylabel('Distance (m)')
plt.title('Time integrated image')
plt.savefig('integ.jpg')
plt.show()

plt.plot(np.linspace(-500, 500, 1000) , im_sum[10])
plt.title('Intensity as a function of x')
plt.xlabel('Distance from center (arbitrary)')
plt.ylabel('Intensity (arbitrary)')
plt.savefig('integ_1d.jpg')
plt.show()
