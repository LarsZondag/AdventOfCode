#%%
import numpy as np
with open('input.txt') as f:
    energies_raw = [list(l.strip()) for l in f.readlines()]
energies_raw = np.array(energies_raw, dtype=int)
# %% P1 & P2
energies = energies_raw.copy()
numberOfFlashes = 0
step = 0
allHaveFlashed = False
while True:
    energies+=1
    flashing = energies == 10
    indices = np.transpose(np.nonzero(flashing))
    while len(indices > 0):
        [y, x], indices = indices[0], indices[1:]
        miny = max(0, y-1)
        minx = max(0, x-1)
        maxy, maxx = energies.shape
        maxy = min(maxy, y+2)
        maxx = min(maxx, x+2)
        energies[miny:maxy, minx:maxx] += 1
        newlyFlashing = (energies == 10) & ~flashing
        newIndices = np.transpose(np.nonzero(newlyFlashing))
        flashing = flashing | newlyFlashing
        indices = np.concatenate((indices,newIndices))
    energies[flashing] = 0
    flashesAtThisStep = np.sum(flashing)
    step+=1

    if step <= 100: numberOfFlashes += flashesAtThisStep
    if flashesAtThisStep == 100: 
        print(f"Everyone flashes at step: {step + 1}")
        allHaveFlashed = True
    if step >= 100 and allHaveFlashed: break


print(f"Number of flashes in 100 steps: {numberOfFlashes}")


# %%
