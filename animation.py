#conda create -n anim_oct_env python=3.6 xarray numpy scikit-image matplotlib netcdf4

import xarray as xr
import os
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from skimage import measure


start=0
end=300
file_add='~/Dropbox/Public/vis_contest.nc'

ds=xr.open_dataset(file_add)



def plot_cond(time,ds,outDir=''):
    # plt.close()
    # Use marching cubes to obtain the surface mesh of these ellipsoids
#     arr=np.transpose((ds['QCLOUD'].isel(Time=time)+ds['QICE'].isel(Time=time)).values)
    arr=np.transpose((ds['qcond'].isel(Time=time)).values)
    verts, faces, normals, values = measure.marching_cubes_lewiner(arr, 2e-5)
    # verts2, faces2, normals2, values2 = measure.marching_cubes_lewiner(arr, 5e-5)


    # Display resulting triangular mesh using Matplotlib. This can also be done
    # with mayavi (see skimage.measure.marching_cubes_lewiner docstring).
    fig = plt.figure(figsize=(9,6))
    ax = fig.add_subplot(111, projection='3d')

    # Fancy indexing: `verts[faces]` to generate a collection of triangles
    # to make it look less triangle like, reduce alpha
    mesh = Poly3DCollection(verts[faces],alpha=0.05)
    mesh.set_edgecolor('w')
    mesh.set_facecolor(mpl.cm.Greys(250))
    ax.add_collection3d(mesh)

    # mesh2 = Poly3DCollection(verts2[faces2],alpha=1)
    # mesh2.set_edgecolor('w')
    # mesh2.set_facecolor((0,0,1))
    # ax.add_collection3d(mesh2)

    ax.set_xlabel("x (km)")
    ax.set_ylabel("y (km)")
    ax.set_zlabel("z (km)")
    ax.set_xticks([0,96])
    ax.set_xticklabels([192,0])
    ax.set_yticks([0,96])
    ax.set_yticklabels([0,192])
    ax.set_zticks([0,18,35])
    ax.set_zticklabels([0,4,13]) #hts at ztick levels

    ax.set_xlim(0, 95)  # a = 6 (times two for 2nd ellipsoid)
    ax.set_ylim(0, 95)  # b = 10
    ax.set_zlim(0, 35)  # c = 16


    ax.grid(False)
    ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    # ax.w_zaxis.set_pane_color((1.0, 0.0, 1.0, 1.0))
    # ax.set_axis_off()


    ax.view_init(elev=0., azim=-35)
    ax.view_init(elev=5., azim=-35)


    ax.w_xaxis.line.set_lw(0.)
    ax.w_yaxis.line.set_lw(0.)
    ax.w_zaxis.line.set_lw(0.)


    #turning off tick marks only
    ax.xaxis._axinfo['tick']['inward_factor'] = 0
    ax.xaxis._axinfo['tick']['outward_factor'] = 0.
    ax.yaxis._axinfo['tick']['inward_factor'] = 0
    ax.yaxis._axinfo['tick']['outward_factor'] = 0.
    ax.zaxis._axinfo['tick']['inward_factor'] = 0
    ax.zaxis._axinfo['tick']['outward_factor'] = 0.




    plt.title('t='+str(time+1))
    plt.tight_layout()
    # plt.show()
    plt.savefig(outDir+'img'+str(time).zfill(4)+'.png')
    plt.close("all")
    return

for time in range(start,end):
    plot_cond(time,ds)
    
os.system('convert  -loop 1 -extent 900x584 img*png animation.gif ')
