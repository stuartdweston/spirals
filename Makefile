#

FF=gfortran

all:
        ${FF} -o fit_geoblocks_tropos_v7a fit_geoblocks_tropos_v7a.f
        ${FF} -o fit_geoblocks_w_baselines_v2b fit_geoblocks_w_baselines_v2b.f

clean:
        rm fit_geoblocks_tropos_v7a  fit_geoblocks_w_baselines_v2b

install:
        cp fit_geoblocks_tropos_v7a ~/bin/fit_geoblocks_tropos
        cp fit_geoblocks_w_baselines_v2b ~/bin/fit_geoblocks_w_baselines

#End of the makefile
