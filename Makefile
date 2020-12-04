#

FF=gfortran

all:
        ${FF} -o fit_geoblocks_tropos fit_geoblocks_tropos.f
        ${FF} -o fit_geoblocks_w_baselines fit_geoblocks_w_baselines.f
        ${FF} -o fit_parallax_multi fit_parallax_multi.f

clean:
        rm fit_geoblocks_tropos  fit_geoblocks_w_baselines fit_parallax_multi

install:
        cp fit_geoblocks_tropos ~/bin/fit_geoblocks_tropos
        cp fit_geoblocks_w_baselines ~/bin/fit_geoblocks_w_baselines
        cp fit_parallax_multi ~/bin/fit_parallax_multi

#End of the makefile
