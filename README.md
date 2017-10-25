# Cloud_PIXI17

Name: Xin Rong Chua

Email: xchua@princeton.edu

Caption: To better predict changes in global rainfall, we study the statistics of convective processes using a high-resolution (2km) model. These events are visualized by plotting the 2e-5 kg/kg isosurfaces of cloud condensate output for each minute of the simulation. Both shallow (~ 1km) and deep (~10 km) convective events are represented. The latent heat released when the condensates form allow for ascending motion. This rising takes place over a small area. Later, as the condensates re-evaporate or are converted to precipitation, the convective event dissipates. Each event occurs on a timescale of minutes to hours. Viewing the spectrum of convective events in the domain is valuable in building intuition for how the aggregated behavior of convection influences precipitation means and extremes.



Dependencies
============
The data file may be found at /home/xchua/vis_contest.nc on the Adroit cluster or
https://www.dropbox.com/s/xtffww10onk0mzy/vis_contest.nc?dl=0 . 

The script uses the Python libraries xarray, numpy, scikit-image, matplotlib, PIL, and netcdf4, as well as ImageMagick 6.7.8-9. The conda environment used is detailed in animation_environment.yml. 
