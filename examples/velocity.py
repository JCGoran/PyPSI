'''

    Velocity field script
    
'''

import PSI as psi
import numpy as np
import matplotlib.pyplot as plt


# load the mesh from a Gadget snapshot 
snap = '../data/snapshot_010'
#snap = '../data/snapshot_999'
mesh = psi.Mesh(filename=snap, loader='gadget2')

# create the Grid, specifying the resolution and projection window
ngrid = 3*(128,) 
win = (mesh.boxmin, mesh.boxmax)
grid = psi.Grid(type='cart', n=ngrid, window=win, fields=['m', 'v']) 

# call PSI.voxels()
psi.voxels(grid=grid, mesh=mesh, mode='density')

print('Velocity components min/max =', np.min(grid.fields['v']), np.max(grid.fields['v']))

# check the total mass
# show a picture
elemmass = np.sum(mesh.mass)
voxmass = np.sum(grid.fields["m"])
err = np.abs(1.0-voxmass/elemmass)

# print the error and show the figure
print('Global error = %.10e' % err) 
#hlp.makeFigs(grid.fields['m'], log=True, title='Example 2: Voxelization of a cosmological density field')
fig, axes = plt.subplots(1,2,figsize=(10,5))
axes[0].imshow(np.log10(np.sum(grid.fields['m'], axis=0)))
axes[1].imshow(np.sum(grid.fields['v'][:,:,:,1], axis=0))
plt.show()


