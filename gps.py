#!/usr/bin/env python3
from os import listdir
from os.path import join
import matplotlib.pyplot as plt
import gpxpy


def draw():
    # Initialization
    data_path = 'log'
    data = [i for i in listdir(data_path)]

    fig = plt.figure(facecolor='white')
    ax = plt.Axes(fig, [0., 0., 1., 1.], )
    ax.set_aspect('equal')
    ax.set_axis_off()
    fig.add_axes(ax)

    lat = []
    lon = []

    # Plotting
    for datum in data:
        gpx_filename = join(data_path,datum)
        gpx_file = open(gpx_filename, 'r')
        gpx = gpxpy.parse(gpx_file)

        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    lat.append(point.latitude)
                    lon.append(point.longitude)

        plt.plot(lon, lat, color='#3B4252', lw=1, alpha=0.8)

        lat = []
        lon = []

    # Saving
    filename = data_path + '.png'
    plt.savefig(filename, facecolor=fig.get_facecolor(), bbox_inches='tight',
            pad_inches=0, dpi=300)


if __name__=='__main__':
    draw()
