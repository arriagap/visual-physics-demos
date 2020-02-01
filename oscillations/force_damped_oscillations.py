import matplotlib.pyplot as plt
import numpy as np




def forced_vals(k, m, omega_f_ratio, g, f_0, maxtime, fname, omega_f_saved = None, settling_as = None, plot = True):
    mintime = 0.

    deltat = 0.005

    npoints = int((maxtime - mintime) / deltat)

    timevals = np.linspace(mintime, maxtime, npoints)
    integ_vals_velocity = [0.01]
    integ_vals_position = [2.0]

    omega = np.sqrt(k / m)
    omega_1 = omega * omega_f_ratio
    for timeval in timevals:
        a = (-k * integ_vals_position[-1] - g * integ_vals_velocity[-1] + f_0 * np.cos(omega_1 * timeval)) / m
        integ_vals_velocity.append(integ_vals_velocity[-1] + a * deltat)
        integ_vals_position.append(integ_vals_position[-1] + integ_vals_velocity[-1] * deltat + 0.5 * a * deltat**2. )

    

        
    settling_amp = np.max(integ_vals_position[-400:])
    if plot == True:
        plt.clf()
        #    fig = plt.figure(figsize  = (7,7))
#        plt.subplot('211')
        plt.plot(timevals, integ_vals_position[1:])
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
#        plt.ylim([-1.4, 1.4])
        plt.xlim([0, maxtime])
#        plt.hlines([settling_amp, -settling_amp], 0, maxtime, color = 'red', linestyle = '--')
    
        # plt.subplot('212')
        # plt.ylabel('Settling amplitude')
        # plt.xlabel('$\omega_f / \omega_0$')
        # plt.plot(omega_f_saved, settling_as)
        # plt.scatter([omega_f_ratio], [settling_amp], color = 'red', s= 30)
        plt.show()
        plt.savefig(fname)
    return np.max(integ_vals_position[-400:])
    

def forced(save = False):
    maxtime = 20. 
    k = 2.0
    m = 0.5
    c = .03
    f_0 = 0.0
    g = 0.02
    #omega_f_ratios = np.append(np.linspace( 0.7, 0.97, 20), np.linspace( 1.03, 1.2, 20))

    omega_f_ratios = np.linspace(0.01, 0.06, 6)
    settling_a = []
    if save == False:
        omega_f_saved, settling_as = np.loadtxt('f_ratios.txt')
    for i, rat in enumerate(omega_f_ratios):
        fname = 'forced_osc'
        if i < 10:
            fname += '00' + str(i)
        if i >= 10 and i < 100:
            fname += '0' + str(i)
        fname += '.png'
        if save == True:
            amp = forced_vals(k, m, rat, g, f_0, maxtime, fname, omega_f_saved, settling_as, plot = False)
        else:
            amp = forced_vals(k, m, rat, g, f_0, maxtime, fname, omega_f_saved, settling_as, plot = True)
    if save == True:
        np.savetxt('f_ratios.txt', np.array([omega_f_ratios, settling_as]))





        

def damped_vals(k, m, c, fname, plot = True):
    mintime = 0.
    maxtime = 30.
    deltat = 0.005
    
    
    npoints = int((maxtime - mintime) / deltat)

    timevals = np.linspace(mintime, maxtime, npoints)
    integ_vals_velocity = [0.01]
    integ_vals_acceleration = [0.01]
    integ_vals_position = [2.0]

    zeta = c / (2 * np.sqrt( m * k))

    
    omega = np.sqrt(k / m)
    g = 9.8
    for timeval in timevals:
        integ_vals_acceleration.append(integ_vals_acceleration[-1] - omega * integ_vals_position[-1] - g / m)
        integ_vals_velocity.append(integ_vals_acceleration[-1] * deltat - c * integ_vals_position[-1] / m)
        integ_vals_position.append(integ_vals_position[-1] +  integ_vals_velocity[-1] * deltat + 0.5 * integ_vals_acceleration[-1] * deltat**2.)

        
    settling_amp = np.max(integ_vals_position[-400:])

    if plot == True:
        plt.clf()
        #    fig = plt.figure(figsize  = (7,7))
#        plt.subplot('211')
        plt.plot(timevals, integ_vals_position[1:])
        plt.xlabel('Time (s)')
        plt.ylabel('Energy')
#        plt.ylim([-1.4, 1.4])
        plt.xlim([0, maxtime])
        plt.title('Q = ' + str(1 / (2 * zeta))[:4])
        plt.hlines([2, 0.65], 0, maxtime, color = 'red', linestyle = '--', linewidth = 2)
    
        # plt.subplot('212')
        # plt.ylabel('Settling amplitude')
        # plt.xlabel('$\omega_f / \omega_0$')
        # plt.plot(omega_f_saved, settling_as)
        # plt.scatter([omega_f_ratio], [settling_amp], color = 'red', s= 30)
        plt.show()
#        plt.savefig(fname)
    return np.max(integ_vals_position[-400:])
    



def damped():
    maxtime = 20. 
    k = 2.0
    m = 0.5
    c = .03
    f_0 = 0.0
    g = 9.8
    cs = np.linspace(0, 0.08, 40)


    for i, c in enumerate(cs):
        fname = 'damped'
        if i < 10:
            fname += '00' + str(i)
        if i >= 10 and i < 100:
            fname += '0' + str(i)
        fname += '.png'
    
        amp = damped_vals(k, m, c, fname)









def no_foce_vals(k, m):
    mintime = 0.
    maxtime = 100.
    deltat = 0.005

    npoints = int((maxtime - mintime) / deltat)

    timevals = np.linspace(mintime, maxtime, npoints)
    integ_vals_acceleration = [0.01]
    integ_vals_position = [2.0]

    omega = np.sqrt(k / m)
    g = 9.8
    for timeval in timevals:
        integ_vals_acceleration.append(integ_vals_acceleration[-1] - omega * integ_vals_position[-1] - g)
        integ_vals_position.append(integ_vals_position[-1] +  0.5 * integ_vals_acceleration[-1] * deltat**2. )

    

        
    settling_amp = np.max(integ_vals_position[-400:])
    plot = True
    if plot == True:
        plt.clf()
        #    fig = plt.figure(figsize  = (7,7))
#        plt.subplot('211')
        plt.plot(timevals, integ_vals_position[1:])
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
#        plt.ylim([-1.4, 1.4])
        plt.xlim([0, maxtime])
#        plt.hlines([settling_amp, -settling_amp], 0, maxtime, color = 'red', linestyle = '--')
    
        # plt.subplot('212')
        # plt.ylabel('Settling amplitude')
        # plt.xlabel('$\omega_f / \omega_0$')
        # plt.plot(omega_f_saved, settling_as)
        # plt.scatter([omega_f_ratio], [settling_amp], color = 'red', s= 30)
        plt.show()
#        plt.savefig(fname)
    return np.max(integ_vals_position[-400:])
    
