import matplotlib.pyplot as plt 
import numpy as np 
from scipy.stats import gaussian_kde


path_names = ['a', 'b']
beta_names = {'a':'b11', 'b':"b1"}

for path in path_names:
    qn_name = "qn-path%s-gfpc_alphatest-%s_0.9.dat"%(path, beta_names[path])
    theta_name = "theta-path%s-alphatest-%s_0.9.dat"%(path, beta_names[path])
    print "plotting for %s"%qn_name
    qn_file = np.genfromtxt(qn_name)
    theta_file = np.genfromtxt(theta_name)
    qn_data = qn_file[:,2]
    theta_data = theta_file[:,3]

    # xy = np.vstack([theta_data, qn_data])
    # z = gaussian_kde(xy)(xy)
    # idx = z.argsort()
    # theta_data, qn_data, z =theta_data[idx], qn_data[idx], z[idx]
    # # z = np.ma.masked_where(z < 0.0005, z)
    # fig, ax = plt.subplots()
    # x1 = ax.scatter(theta_data, qn_data, c=z, s = 100, edgecolor='')

    xmin, xmax = theta_data.min(), theta_data.max()
    ymin, ymax = qn_data.min(), qn_data.max()
    xMesh, yMesh = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
    positions = np.vstack([xMesh.ravel(), yMesh.ravel()])
    values = np.vstack([theta_data, qn_data])
    kernel = gaussian_kde(values)
    zMesh = np.reshape(kernel(positions).T, xMesh.shape)
    fig = plt.figure()
    ax = plt.gca()
    cfset = ax.contourf(xMesh, yMesh, zMesh, antialiased=True, cmap='jet')
    clset = ax.contour(xMesh, yMesh, zMesh, colors='black')



    plt.title("scatter_alpha-plot-path%s"%path)
    plt.xlabel("$\\theta$ [$^\circ$]", fontsize = 20)
    plt.ylabel("$Q_N$ $\\alpha$ helix", fontsize = 20)
    # plt.xlim
    plt.ylim(0, 1)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    img_name = "alphahelix_qn_gfpc_theta-scatter-plot-path%s.png"%path
    # fig.colorbar(x1)
    plt.savefig(img_name, format='png', dpi=300, bbox_inches='tight')#, transparent=True)
